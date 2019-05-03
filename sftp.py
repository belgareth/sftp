import datetime, paramiko, os, zipfile, shutil

#Formatting Date and Creating Directory
today = datetime.date.today()-datetime.timedelta(days=0)
formattedtime = today.strftime('%d%m%Y')	
destination = '%s'%formattedtime
if not os.path.exists(destination):
	os.mkdir(destination)

# This function downloads the file using Paramiko
# and saves in specfied directory

def file_download(host, username,port, password):
#	mykey = paramiko.RSAKey.from_private_key_file('~/My-ssh.priv')  # This is when password less login is setup
	password = 'pass'                                             # This is used when password is used to login  	
	host = 'ip'
	username = 'user'
	port = port
	transport = paramiko.Transport((host, port))
#	transport.connect(username = username, pkey = mykey) 		# This is when password less login is setup
	transport.connect(username = username, password = password)	# This is used when password is used to login
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.chdir('/dbs/reports')
	for filename in sftp.listdir():
		try:
			if filename.startswith('07-Jun%s.aes'%formattedtime):
				localpath= os.getcwd() + '/' + filename
				print "Downloading files ==> " + filename
				sftp.get(filename, localpath)	
		except IOError as e:
			print e
	sftp.close()
	transport.close()

# This function calls the file_download function 
# and moves the files to required directory. If 
# using shutil.move() then it copies permissions 
# also which is not desirable always. 

def main():
	try:	
		file_download('host', 'username', 'port', 'password')
		currentfile = os.getcwd() + '\\' + '%s'%formattedtime 	
		shutil.copy(currentfile, destination)	
		os.remove(currentfile)
	except Exception as e:
		print e

if __name__ == '__main__':
	main()
