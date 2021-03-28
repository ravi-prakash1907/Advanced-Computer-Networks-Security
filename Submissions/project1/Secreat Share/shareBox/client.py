"""   Client / Receiver Side   """

import os
import json
import socket

# Defining some Global Variables
CHUNK = 1024

class client:

	def __init__(self):

		# Creating Socket Object
		self.sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Input Hostname and define Port
		self.host = input("\nHost Address / URL \n(just press enter to use default): ")
		if self.host is None:
			self.host = '127.0.0.1'
		self.port = 55555

		# Binding socket with the host and port
		self.connected = False
		try:
			self.sockClient.connect((self.host, self.port))
			try:
				os.mkdir('received')
				print("Connected...")
			except:
				print("Connected...")
			self.connected = True

		except:
			print("Currently server is down!! Try later!")

	def formatFileName(self, gotName):
		if '/' in gotName:
			gotName = gotName.split('/')[-1]
		gotName = 'received/'+gotName
		
		return gotName

	def client(self):
		if self.connected:		
			# Receiving the Header for the Main Data
			detailHeader = self.sockClient.recv(CHUNK)

			# Loading the Json Data from the header received
			detailHeader = json.loads(detailHeader)
			#print(detailHeader)

			for i in range(1, len(detailHeader) + 1):
				filename = self.formatFileName(detailHeader[str(i)]['filename'])

				# Opening new file to write the receiving data
				with open(filename, 'wb') as f:
					print("Saving {}".format(filename), end=" ")

					# Writing the received data to the file opened
					# Checking If the file size exceeds the original file size
					while detailHeader[str(i)]['filesize'] > f.tell():
						fileData = self.sockClient.recv(CHUNK)
						if not fileData:	# Checking if the File Ends
							break
						f.write(fileData)
					print("(size {})".format(f.tell()))

				f.close()

			print("\nFile(s) received...\n"+"-"*12)
		

		###########
		self.sockClient.close()	# Closing the Connection