from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_patients (id INT PRIMARY KEY, name VARCHAR(100), phone VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_doctors (id INT PRIMARY KEY, name VARCHAR(100), specialty VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_appointments (id INT PRIMARY KEY, patient_id INT, doctor_id INT, appointment_date DATE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_bills (id INT PRIMARY KEY, patient_id INT, amount DECIMAL(10,2), status VARCHAR(30))")
    connection.commit()
    cursor.close()


def register_patient(connection, patient_id, name, phone):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_patients VALUES (%s, %s, %s)", (patient_id, name, phone))
    connection.commit()
    cursor.close()


def schedule_appointment(connection, appointment_id, patient_id, doctor_id, appointment_date):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_appointments VALUES (%s, %s, %s, %s)", (appointment_id, patient_id, doctor_id, appointment_date))
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Hospital Management System ready.")
    database.close()
