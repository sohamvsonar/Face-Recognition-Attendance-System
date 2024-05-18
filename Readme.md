# Face Recognition Attendance System

This project is a Face Recognition Attendance System that uses a webcam to recognize students and record their attendance in a Firebase Realtime Database. It integrates face recognition technology with Firebase for efficient attendance tracking.

## Features

- Real-time face detection and recognition using `face_recognition` library.
- Integration with Firebase Realtime Database and Firebase Storage.
- Displays student details and updates attendance records.
- Uses OpenCV for image processing and UI display.
- Custom background and mode images for a better user interface.

## Prerequisites

- Python 3 and above
- OpenCV
- face_recognition
- cvzone
- Firebase Admin SDK
- Firebase Realtime Database and Storage set up

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sohamvsonar/Face-Recognition-Attendance-System.git
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
├──database.py
├── service_account_Key.json
└── main.py ```

## Firebase Structure
Ensure your Firebase Realtime Database follows this structure:
JSON
{
  "Students": {
    "student_id_1": {
      "name": "John Doe",
      "major": "Computer Science",
      "standing": "Senior",
      "year": "4",
      "starting_year": "2020",
      "total_attendance": 10,
      "last_attendance_time": "2024-05-17 10:00:00"
    },
    ...
  }
}


## Acknowledgements
- face_recognition library for face detection and recognition.
- OpenCV for image processing.
- Firebase for backend services.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me at soham.sonar427@gmail.com.
