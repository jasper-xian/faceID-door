import face_recognition
import os

known_faces = []
known_files = os.listdir(os.getcwd()+'/Known')

for image in known_files:
    face = face_recognition.load_image_file(os.getcwd()+'/Known/'+image)
    known_faces.append(face_recognition.face_encodings(face)[0])


unknown = face_recognition.load_image_file("barack.jpg")

unknown_encoding = face_recognition.face_encodings(unknown)[0]

results = face_recognition.compare_faces(known_faces, unknown_encoding)

isKnown = False

for result in results:
    if result:
        isKnown = True

if isKnown:
    print("Known")
else:
    print("Unknown")