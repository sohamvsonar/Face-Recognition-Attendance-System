# Face Recognition Attendance System

This project is a Face Recognition Attendance System that uses a webcam to recognize students and record their attendance in a Firebase Realtime Database. It integrates face recognition technology with Firebase for efficient attendance tracking.

## Features

- Real-time face detection and recognition using `face_recognition` library.
- Integration with Firebase Realtime Database and Firebase Storage.
- Displays student details and updates attendance records.
- Uses OpenCV for image processing and UI display.
- Custom background and mode images for a better user interface.

## Prerequisites

- Python 3.x
- OpenCV
- face_recognition
- cvzone
- Firebase Admin SDK
- Firebase Realtime Database and Storage set up

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sohamvsonar/face-recognition-attendance-system.git
    cd face-recognition-attendance-system
    ```

2. **Install the required libraries:**

    ```bash
    pip install opencv-python
    pip install face-recognition
    pip install cvzone
    pip install firebase-admin
    ```

3. **Firebase Setup:**

    - Create a Firebase project and set up Realtime Database and Storage.
    - Download the service account key JSON file and place it in the project directory.
    - Update the `databaseURL` and `storageBucket` in the code with your Firebase project's details.

## Configuration

Ensure you have the following directory structure:

```plaintext
face-recognition-attendance-system/
│
├── Resources/
│   ├── background.png
│   └── Modes/
│       ├── mode1.png
│       ├── mode2.png
│       └── ... (other mode images)
├── Encodegenerator.py
|── Database.py
├── service_account_Key.json
└── main.py

