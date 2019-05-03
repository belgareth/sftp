#!/usr/bin/python

import sys
import chilkat

#  Important: It is helpful to send the contents of the
#  sftp.LastErrorText property when requesting support.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()#incase of missing keys
sftp = chilkat.CkSFtp()

#  Any string automatically begins a fully-functional 30-day trial.
success = sftp.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Set some timeouts, in milliseconds:
sftp.put_ConnectTimeoutMs(5000)
sftp.put_IdleTimeoutMs(10000)

#  Connect to the SSH server.
#  The standard SSH port = 22
#  The hostname may be a hostname or IP address.

hostname = "1.1.1.1"
port = 22
success = sftp.Connect(hostname,port)
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Authenticate with the SSH server.  Chilkat SFTP supports
#  both password-based authenication as well as public-key
#  authentication.  This example uses password authenication.
success = sftp.AuthenticatePw("fltbackup","2succeeD")
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  After authenticating, the SFTP subsystem must be initialized:
success = sftp.InitializeSftp()
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Open a file on the server:
handle = sftp.openFile("/home/fltbackup/Dropbox/dbs/dbs-04-Jun-2017.log","readOnly","openExisting")
if (sftp.get_LastMethodSuccess() != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Download the file:
success = sftp.DownloadFile(handle,"/home/fltbackup/Dropbox/dbs/dbs-04-Jun-2017.log")
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Close the file.
success = sftp.CloseHandle(handle)
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

print("Success.")