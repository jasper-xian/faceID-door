from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# experimental code for removing people
file = drive.CreateFile({'id':'1sm6gcDNQqzzRxwFYcAqZG_H8ssClwtyQ'})
file.GetContentFile('remove.txt')
f = open('remove.txt','r')
x = f.readline()
while x != '':
    if x[-1:] == '\n':
        x = x[0:-1]
    if x != "start":
        os.remove(os.getcwd() + '/Known/' + x +".jpg")
    x = f.readline()
f.close()
w = open('remove.txt','w')
w.write("start")
w.close()
file.SetContentFile('remove.txt')
file.Upload()