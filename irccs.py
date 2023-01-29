import socket
import sys

def send_message(message):
    irc.send(f"PRIVMSG {channel} :{message}\n".encode())

server = sys.argv[1]
channel = sys.argv[2]
nickname = sys.argv[3]
msg = sys.argv[4]
port = int(sys.argv[5])

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"NICK {nickname}\n".encode())
irc.send(f"JOIN {channel}\n".encode())

send_message(msg)
