#A00212454

import socket as sk#Imports socket
from sys import argv # Import argument
from ssl import * # Imports ssl module
import logging as lg # Imports logging
from easygui import *

title = "Echo Server"#sets text in variable
msgbox("Welcome to the Echo Server", title)# Creates messagebox and gives it a title

lg.basicConfig(filename='echoserver.log',filemode='a', level=lg.INFO,
format='%(asctime)s %(levelname)s %(message)s',datefmt="%a %d/%m/%Y %I:%M") # Configures the logfile and establishes the format

name = argv[0] # Set name of file to argument 0

if len(argv) == 2: # If arguments is equal to 2
 port = int(argv[1]) # Port is equal to argument 1
 
else: # If not equal to 2 arguments
	port = enterbox("Enter Port number", title) # enterbox used to enter port number
	port = int(port) # setting variable as integer

server_socket=sk.socket(sk.AF_INET, sk.SOCK_STREAM)#create a socket

server_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR,1)#Allow the socket to reuse port
# Keep attempting until we bind until the user quits
while True:
	try:
		# bind to the specified port
		server_socket.bind(("localhost",port)) # port server binds to
		lg.info('Server started on port: %d',port)#Prints info message to logfile when servers started
		break#break loop
	
	except sk.error: # If there is a socket error select one of the following options:
		lg.warning('Cannot bind to port') # Prints message into logfile stating that the port cannot be binded
		msg=("Server unable to bind to a port",title)#Print statment
		choices=['Retry','Change details','Quit']#Sets choices for gui
		choice=choicebox(msg,title,choices)	#Display box of choices
		
		if choice=='Change details': # If change details is selected
			port = enterbox("Enter Port number", title) # enterbox for port number
			port = int(port) # setting variable as integer
			break# break
			
		elif choice=='Quit':#if choice is quit
			exit()#exits the program
			
						

# Listen for connections
server_socket.listen(1)

# Wraps the socket using TLS
try:
	tls_server = wrap_socket(server_socket,ssl_version=PROTOCOL_TLSv1,cert_reqs=CERT_NONE,server_side=True,keyfile='./keyfile.pem',certfile='./certfile.pem')
	lg.info('Socket wraped using TLS')#Prints info message to logfile when socket is wraped
	
except FileNotFoundError:#Except when filenotfound error occors
	msgbox("Cannot source TLS files",title)#Displays message
	lg.error('Cannot source TLS  files')#Prints Error message to logfile if error occors while wraping socket
	exit()#exit	

msgbox("server listening on port: "+str(port)+'',title)# prints statement while looking for connection
lg.info('Server listening on port: %d',port) # information sent to logfile

# Use TLS object to accept a client connection
connection, client_address = tls_server.accept()

msgbox("Accepted client request from "+str(client_address),title )#Prints ip of client when conncections made
lg.info('Client connected: %s',client_address)#Prints info message to logfile when client connects

once=False
while True: # while loop
	while not once: # Message is received without the clients response
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		choice = data_in.decode()#Decode data in as response
		lg.info('Message received: %s',choice) # Prints message received from client into log file
		once=True
	
	# If No is selected the program is terminated
	if choice == 'No':
		break
	
	if choice == 'Yes':	
		response=('Enter The Grade Achieved For The First Module ')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		firstgrade=response # Setting response from client as variable 
		
		response=('Enter The Credit Value For The First Module ')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		firstcredit=response # Setting response from client as variable 
		
		response=('Enter The Grade Achieved For The Second Module')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		secondgrade=response # Setting response from client as variable 
		
		
		response=('Enter The Credit Value For The Second Module')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		secondcredit=response # Setting response from client as variable 
		
		
		response=('Enter The Grade Achieved For The Third Module')# Response sent to the client
		data_out = response.encode()
		connection.send(data_out)
		data_in = connection.recv(1024)
		response = data_in.decode()
		thirdgrade=response # Setting response from client as variable 
		
		response=('Enter The Credit Value For The Third Module')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		thirdcredit=response # Setting response from client as variable 
	
		response=('Enter The Grade Achieved For The Fourth Module')# Response sent to the client
		data_out = response.encode()
		connection.send(data_out)
		data_in = connection.recv(1024)
		response = data_in.decode()
		fourthgrade=response # Setting response from client as variable 
		
		response=('Enter The Credit Value For The Fourth Module')# Response sent to the client
		data_out = response.encode()#encode the message
		connection.send(data_out)#send the message back
		data_in = connection.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as response
		fourthcredit=response # Setting response from client as variable 
			
		gradepoint = int(firstgrade)*int(firstcredit) # gradepoint calculation using client response variables
		gradepoint2 = int(secondgrade)*int(secondcredit)
		gradepoint3 = int(thirdgrade)*int(thirdcredit)
		gradepoint4 = int(fourthgrade)*int(fourthcredit)
		
		totalcredits = (int(firstcredit)+int(secondcredit)+int(thirdcredit)+int(fourthcredit)) # credit calculation using client response variables
		
		totalgradepoints = (gradepoint+gradepoint2+gradepoint3+gradepoint4) # overall gradepoints
		
		TotalGPA = totalgradepoints/totalcredits # overall gpa
		
		response=('Your Total GPA Is '+ str(round(TotalGPA))) # Setting up server response containing overall gpa
		data_out = response.encode() # encode response
		connection.send(data_out) # sending it to the client
		data_in = connection.recv(1024) # response from client
		response = data_in.decode() # decoding response
		
connection.shutdown(sk.SHUT_RDWR)#Shutdown the connection
connection.close()#Close the connection

tls_server.shutdown(sk.SHUT_RDWR)#Shutdown the socket
tls_server.close()#Close the socket
lg.info('Server Stopped') # Prints a message into logfile stating the server has been stopped



