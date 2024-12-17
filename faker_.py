from calendar import firstweekday
from encodings.idna import sace_prefix

import psycopg2
from faker import Faker
import random

conn = psycopg2.connect(
    dbname="hospital",
    user="postgres",
    password="0",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

fake = Faker()

def doctors():
    for _ in range(50):
        name = fake.name()
        specialty = random.choice(['Good', 'Higher', 'Junior', 'Middle', 'Senior'])
        experience_years = random.randint(1, 40)
        cursor.execute(
            "INSERT INTO doctors (name, specialty, experience_years) VALUES (%s, %s, %s)",
            (name, specialty, experience_years)
        )

def patients():
    for _ in range(500):
        name = fake.name()
        birth_date = fake.date_between_dates(date_start=1900, date_end=2024)
        gender = random.choice(['Men', 'Woman'])
        cursor.execute(
            "INSERT INTO patients (name, birth_date, gender) VALUES (%s, %s, %s)",
            (name, birth_date, gender)
        )

def appointments():
    for _ in range(1000):
        doctor_id = random.randint(1, 1000)
        patient_id = random.randint(1, 1000)
        appointment_date = fake.date_between(start_date='-30y', end_date='today')
        status = fake.boolean(5)

        cursor.execute(
            "INSERT INTO appointments (doctor_id, patient_id, appointment_date, status) VALUES (%s, %s, %s, %s)",
            (doctor_id, patient_id, appointment_date, status)
        )




doctors()
patients()
appointments()

conn.commit()
cursor.close()
conn.close()

