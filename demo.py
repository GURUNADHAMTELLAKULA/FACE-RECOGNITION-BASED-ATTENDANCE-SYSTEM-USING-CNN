# Import necessary libraries
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import cv2
from datetime import datetime

# Function to make attendance entry
def makeAttendanceEntry(name, attendance_list):
    now = datetime.now()
    dtString = now.strftime('%d/%b/%Y, %H:%M:%S')
    entry = f'{name},{dtString}'
    attendance_list.append(entry)

# Function to update the attendance sheet
def updateAttendanceSheet(attendance_list):
    with open('attendance_list.csv', 'a') as FILE:
        for entry in attendance_list:
            FILE.writelines(f'\n{entry}')

# Load known faces
face_1 = face_recognition.load_image_file("Guru.jpg")
face_1_encoding = face_recognition.face_encodings(face_1)[0]

face_2 = face_recognition.load_image_file("Chakri.jpg")
face_2_encoding = face_recognition.face_encodings(face_2)[0]

face_3 = face_recognition.load_image_file("jeffbezos.jpg")
face_3_encoding = face_recognition.face_encodings(face_3)[0]

face_4 = face_recognition.load_image_file("prabhas.jpg")
face_4_encoding = face_recognition.face_encodings(face_4)[0]

face_5 = face_recognition.load_image_file("subhash .jpg")
face_5_encoding = face_recognition.face_encodings(face_5)[0]

# Create lists of known face encodings and corresponding names
known_face_encodings = [
    face_1_encoding,
    face_2_encoding,
    face_3_encoding,
    face_4_encoding,
    face_5_encoding
]

known_face_names = [
    "Guru",
    "Chakri",
    "Jeff Bezos",
    "Prabhas",
    "subhash",
]

# Initialize an empty list to store attendance entries
attendance_list = []

print("Done learning and creating profiles")

# Open a connection to the webcam (0 is usually the default webcam)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the current frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Save attendance entry
            makeAttendanceEntry(name, attendance_list)

        # Draw a rectangle and label on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Output Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Update the attendance sheet after the video capture loop
updateAttendanceSheet(attendance_list)