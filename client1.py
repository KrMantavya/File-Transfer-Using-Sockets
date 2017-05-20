import sys
import socket
import os

user = os.system("whoami")
print user

skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skClient.connect(("127.0.0.1",2525))

sFileName = raw_input("Enter Filename to download from server : ")
sData = "Temp"

while True:
    skClient.send(sFileName)
    sData = skClient.recv(1024)
    fDownloadFile = open('/home/mantavya294/socketclient/'+sFileName,"wb")
    while sData:
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print "Download Completed"
    break

skClient.close()
