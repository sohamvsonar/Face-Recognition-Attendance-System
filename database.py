import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("service_account_Key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fras-ee578-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "id_1":
    {
        "name": "narendra modi",
        "major": "politics",
        "starting_year": 1980,
        "total_attendance": 10,
        "standing": "good",
        "year": "4th",
        "last_attendance_time":"2024-05-12 8:44:00"
    },
    "id_2":
    {
        "name": "dwayne johnson",
        "major": "Wrestling, Hollywood",
        "starting_year": 1995,
        "total_attendance": 15,
        "standing": "good",
        "year": "4th",
        "last_attendance_time":"2024-05-12 8:44:00"
    },
    "id_3":
    {
        "name": "John cena",
        "major": "Wrestling, hollywood",
        "starting_year": 2000,
        "total_attendance": 120,
        "standing": "good",
        "year": "3rd",
        "last_attendance_time":"2024-05-12 8:44:00"
    },
    "id_4":
    {
        "name": "Soham Sonar",
        "major": "politics",
        "starting_year": 2023,
        "total_attendance": 100,
        "standing": "good",
        "year": "2nd",
        "last_attendance_time":"2024-05-12 8:44:00"
    }
    
}

for key, value in data.items():
    ref.child(key).set(value)