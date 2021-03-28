"""   Server / Sender Side   """

import os
import json
import socket
import time

# Defining some Global Variables
CHUNK = 1024

class server:

	def __init__(self):
		########################

		# Defining Hostname and Port
		self.host = input("\nSpecify host's URL or IP-Address \n(just press enter to use default): ")
		if self.host is None:
			self.host = '127.0.0.1'
		
		# Creating Socket
		self.sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		self.host = socket.gethostbyname(self.host)
		self.port = 55555

		# file(s') header
		self.headerDetails = {}
		# list of files that are to be send
		self.filelist = []

		#########################

		# Binding socket with the host and port
		self.sockServer.bind((self.host, self.port))
		self.sockServer.listen(5)

		print('Server up at {0}'.format(self.host))
		
		#########################
		
		# Accepting the Connections of the client willing to connect
		self.connection, self.address = self.sockServer.accept()
		print(f"Connection from {self.address} (reciver) has been established!!!")


	def __loadFiles__(self):
		# Getting the filenames from the Input to send to the client
		totalFiles = int(input("How many files you want to share: "))
		filenames = []

		for i in range(totalFiles):
			filename = input("Enter the name (including complete path) of file-{}: ".format(i+1))
			filenames.append(filename)
		
		return filenames


	def definingHeader(self):
		self.filelist = self.__loadFiles__()

		i = 1
		tempHeader = {}

		# Defining Data Dictionary Meta Data
		for filename in self.filelist:
			# Checking File Size
			filesize = os.stat(filename).st_size

			# Defining header to send as MetaData
			tempHeader[i] = {
								'filename' : filename,
								'filesize' : filesize,
							}
			i += 1

		return tempHeader
	
	def printHeader(self):
		print("\nSharing:\n") # printing from next line
		print("{")
		for fileHeaderIndex in self.headerDetails:
			if int(fileHeaderIndex) != len(self.headerDetails):
				print("\t{}: {},".format(str(fileHeaderIndex), self.headerDetails[fileHeaderIndex]))
		print("\t{}: {}".format(str(fileHeaderIndex), self.headerDetails[fileHeaderIndex]))
		print("}")


	def server(self):		
		self.headerDetails = self.definingHeader()	# Calling function to defining the Header
		st = time.time()

		# Sending dictionary after converting into json object as byte data
		self.connection.send(bytes(json.dumps(self.headerDetails).encode()))
		self.printHeader()

		# Looping over the list to send all the files in list
		for filename in self.filelist:

			# Opening and Reading the first chunk of file bytes
			with open(filename, 'rb') as f:
				fileData = f.read(CHUNK)

				# No Indentation Error Check
				while fileData:
					if not fileData:
						break
					# Sending Data through the connection to the client
					self.connection.send(fileData)
					# Reading the other chunks of the file bytes
					fileData = f.read(CHUNK)

			f.close()	# Closing the file

		et = time.time()
		print("\nFile(s) shared in {} seconds!\n".format(et-st)+"-"*12)

		self.connection.close()	# Closing the connection


