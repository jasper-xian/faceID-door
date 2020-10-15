import face_recognition
import os
import time
import shutil
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

known_faces = []

known_files = os.listdir(os.getcwd()+'/Known')

for image in known_files:
    face = face_recognition.load_image_file(os.getcwd()+'/Known/'+image)
    known_faces.append(face_recognition.face_encodings(face)[0])

while True:
    #add new faces from database to new folder

    # process new faces, then add them to Known folder
    file_list = drive.ListFile({'q': "'1B0MakdPdPHCq569YeJLbVx6fcCdBAXPi' in parents and trashed=false"}).GetList()

    for file in file_list:
        file2 = drive.CreateFile({'id': file['id']})
        file2.GetContentFile(file['title'])
        face = face_recognition.load_image_file(file['title'])
        known_faces.append(face_recognition.face_encodings(face)[0])
        shutil.move(file['title'], os.getcwd() + '/Known/' + file['title'])
        file.Delete()

    # insert code to fetch unknown image from camera


    # processes image then changes removes it
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