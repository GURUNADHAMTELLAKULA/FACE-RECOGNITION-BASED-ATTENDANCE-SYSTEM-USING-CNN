from face_recognition import load_image_file
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import cv2
from datetime import datetime
from tensorflow.keras import layers, models

# Define the number of classes for your classification problem
num_classes = 7  

# Create a more complex CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))  # Additional convolutional layer
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation='relu'))  # Additional convolutional layer
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Function to make attendance entry
def makeAttendanceEntry(name, attendance_list, marked_present):
    now = datetime.now()
    dtString = now.strftime('%d/%b/%Y, %H:%M:%S')

    # Check if the person has already been marked present
    if name not in marked_present:
        entry = f'{name},{dtString}'
        attendance_list.append(entry)
        marked_present.add(name)

# Function to update the attendance sheet
def updateAttendanceSheet(attendance_list):
    file_path = r'C:\Users\DELL\OneDrive\Desktop\Demo\Face-Recognition\attendance_list.csv'
    with open(file_path, 'a') as FILE:
        for entry in attendance_list:
            FILE.writelines(f'\n{entry}')

# Load known faces
face_1 = face_recognition.load_image_file("Guru.jpg")
face_1_encoding = face_recognition.face_encodings(face_1)[0]

# ... Repeat for other known faces ...

known_face_encodings = [
    face_1_encoding,
    # ... Add other known face encodings ...
]

known_face_names = [
    "Guru",
    # ... Add other known face names ...
]

attendance_list = []
marked_present = set()

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
            makeAttendanceEntry(name, attendance_list, marked_present)

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
