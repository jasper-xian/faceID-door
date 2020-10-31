import face_recognition
import os
import time
import shutil
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import requests


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

known_faces = []

names = []

known_files = os.listdir(os.getcwd()+'/Known')

for image in known_files:
    face = face_recognition.load_image_file(os.getcwd()+'/Known/'+image)
    known_faces.append(face_recognition.face_encodings(face)[0])
    names.append(image[0:-4])

while True:
    # process new faces, then add them to Known folder
    file_list = drive.ListFile({'q': "'1B0MakdPdPHCq569YeJLbVx6fcCdBAXPi' in parents and trashed=false"}).GetList()

    for file in file_list:
        names.append(file['title'][0:-4])
        file2 = drive.CreateFile({'id': file['id']})
        file2.GetContentFile(file['title'])
        face = face_recognition.load_image_file(file['title'])
        known_faces.append(face_recognition.face_encodings(face)[0])
        shutil.move(file['title'], os.getcwd() + '/Known/' + file['title'])
        file.Delete()

    #remove faces on remove list
    file3 = drive.CreateFile({'id': '1sm6gcDNQqzzRxwFYcAqZG_H8ssClwtyQ'})
    file3.GetContentFile('remove.txt')
    f = open('remove.txt', 'r')
    x = f.readline()
    while x != '':
        if x[-1:] == '\n':
            x = x[0:-1]
        if x != "start":
            os.remove(os.getcwd() + '/Known/' + x + ".jpg")
            index = names.index(x)
            known_faces.pop(index)
            names.pop(index)
        x = f.readline()
    f.close()
    w = open('remove.txt', 'w')
    w.write("start")
    w.close()
    file3.SetContentFile('remove.txt')
    file3.Upload()

    # insert code to fetch unknown image from camera
    url = 'http://192.168.0.25/capture'
    r = requests.get(url, allow_redirects=True)

    open('unknown.jpg', 'wb').write(r.content)

    # processes image then removes it
    unknown = face_recognition.load_image_file("unknown.jpg")
    os.remove("unknown.jpg")
    shutil.copyfile("placeholder.jpg","unknown.jpg")

    unknown_encodings = face_recognition.face_encodings(unknown)

    isKnown = False
    for unknown_encoding in unknown_encodings:
        results = face_recognition.compare_faces(known_faces, unknown_encoding)
        for result in results:
            if result:
                isKnown = True

    if isKnown:
        print("\nKnown -> door is opened")
        time.sleep(0.5)
        print("waiting...")
        time.sleep(9.5)
        print("Door is closed\n")
    else:
        print("Unknown")