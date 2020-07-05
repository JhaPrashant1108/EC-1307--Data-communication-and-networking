from ftplib import FTP
import sys

ftp = FTP('')
ftp.connect('127.0.0.1',1026)
ftp.login()
ftp.cwd('.')
ftp.retrlines('LIST')

args = sys.argv

def uploadFile():
 filename = args[1]
 ftp.storbinary('STOR '+args[2], open(filename, 'rb'))

def downloadFile():
 filename = args[1]
 localfile = open(""+args[2], 'wb+')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 localfile.close()

if args[3]=="u" :
    uploadFile()
if args[3]=="d" :
    downloadFile()
ftp.close()