from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


file = drive.CreateFile({'id':'1sm6gcDNQqzzRxwFYcAqZG_H8ssClwtyQ'})
file.GetContentFile('remove.txt')
f = open('remove.txt','r')
print(f.read())
f.close()
w = open('remove.txt','w')
w.write("start")
w.close()
file.SetContentFile('remove.txt')
file.Upload()