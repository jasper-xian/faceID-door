import face_recognition
import os
import time

known_faces = []
known_files = os.listdir(os.getcwd()+'/Known')

for image in known_files:
    face = face_recognition.load_image_file(os.getcwd()+'/Known/'+image)
    known_faces.append(face_recognition.face_encodings(face)[0])

while True:
    # insert code to fetch uknown image from camera

    # processes unknown image then removes it
    unknown = face_recognition.load_image_file("unknown.jpg")
    # os.remove("unknown.jpg")

    unknown_encodings = face_recognition.face_encodings(unknown)

    isKnown = False
    for unknown_encoding in unknown_encodings:
        results = face_recognition.compare_faces(known_faces, unknown_encoding)
        for result in results:
            if result:
                isKnown = True

    if isKnown:
        print("Known -> door is opened")
        time.sleep(0.5)
        print("waiting...")
        time.sleep(9.5)
        print("Door is closed\n")
    else:
        print("Unknown")