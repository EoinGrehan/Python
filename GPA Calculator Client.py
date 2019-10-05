#A00212454

import socket as sk#Imports socket
from sys import argv #Imports arguments
from ssl import * # Imports the ssl module
import logging as lg
from easygui import *

title = "Echo Client"
msgbox("Welcome to the Echo Client", title)

# Configure the logger 
lg.basicConfig(filename='echoclient.log', # store logs in file echo.log
				filemode='a', # Appends logfile
				level=lg.INFO,       # default log level
				format="%(asctime)s %(levelname)s %(message)s", # log format: date and time, log level, message
				datefmt="%a %d/%m/%Y %I:%M") # date format: date time am/pm
				
lg.info('/////////////////////////////////////////////////////////////')

client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM) # Create a socket

# Wrap socket using TLS
try:
	tls_client = wrap_socket(client_socket,ssl_version=PROTOCOL_TLSv1,cert_reqs=CERT_NONE)
	lg.info('Socket wraped using TLS')#Prints info message to logfile when socket is wraped

except FileNotFoundError:#Except when filenotfound error occors
	msgbox("Unable to find TSL security files",title)#Display a message box 
	lg.error('Unable to find TSL security files')#Prints Error message to logfile if error occors while wraping socket
	exit()

name = argv[0] # Setting name of file to argument one
 
if len(argv) == 3: # If argument list is equal to 3 
 address = argv[1] # Set address to argument 1
 port = int(argv[2]) # Set port to argument 2
 
else: # if not equal to 3 arguments
	server, port = multenterbox("Enter the server details", title, ["Hostname/IP Address", "Port Number"])
	port = int(port)
	
# Keep trying until connection is made or user terminates	
while True:
	try:
		# connect to the specified server/port
		tls_client.connect((server, port))
		lg.info('Client connected: %s server , %d port',server, port)
		break
	except sk.error: # Unless there is a socket error
		msg=("Client cant connect to the server",title)#Print statment
		choices=['Retry','Change details','Quit']#Sets up choices 
		choice=choicebox(msg,title,choices)	#Easygui display box of choices
		
		if choice=='Change details':# if choice=change 
			#Promts user to enter another server and port
			server, port = multenterbox("Enter the server details", title, ["Hostname/IP Address", "Port Number"])
			port = int(port)
			lg.info('Client connected: %s server , %d port',server, port)#Logs new parameters
			break#Breaks loop
		elif choice=='Quit':#if choice is quit
			exit()#exits the program

msgbox('Welcome to the GPA Calculator', title='GPA Calculator', image='grades.gif')
while True:
	
	choices_list = ['Yes', 'No'] # Choices within buttonbox
	choice = buttonbox('Would you like to calculate your GPA?', 'GPA Calculator', choices_list) #buttonbox containing choices
	
	if choice == 'No':#If message is 'q', shutdown client
		End_message = 'Thank You For Using The Calculator, Goodbye!'
		msgbox(End_message, title='GPA Calculator', image='bye.gif') # messagebox
		data_out = choice.encode() # encodes selection and sends it to the server
		tls_client.send(data_out) 
		break # break loop
		
	if choice == 'Yes':
	
		data_out = choice.encode()#encode message
		tls_client.send(data_out)#send message
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator")) # enterbox which displays server response and stores integer value as a variable
		data_out = str(choice).encode() # Encodes integer value as string 
		tls_client.send(data_out) # Sends it to server
	
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode() # Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode() # Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode()# Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode()# Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode()# Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode()# Encodes integer value as string
		tls_client.send(data_out)
		
		
		data_in = tls_client.recv(1024)#Receive data in, and set maximum size
		response = data_in.decode()#Decode data in as recieved from server
		choice = int(enterbox(response,"GPA Calculator"))
		data_out = str(choice).encode()# Encodes integer value as string
		tls_client.send(data_out)
		
		data_in = tls_client.recv(1024) # Receives response from server
		response = data_in.decode() # decodes response
		choice = msgbox(response,"GPA Calculator", image='gpa.gif') # message box displaying overall gpa

tls_client.shutdown(sk.SHUT_RDWR)#Shutdown the socket
tls_client.close()#Close the socket
