import face_recognition

bohdan = face_recognition.load_image_file("image1.jpg")
unknown = face_recognition.load_image_file("unknown.jpg")

bohdan_encoding = face_recognition.face_encodings(bohdan)[0]
unknown_encoding = face_recognition.face_encodings(unknown)[0]

results = face_recognition.compare_faces([bohdan_encoding], unknown_encoding)

if results[0]:
    print("Bohdan")
else:
    print("Unknown")