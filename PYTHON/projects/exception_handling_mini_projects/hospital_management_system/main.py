from datetime import date


class InvalidPatientError(Exception):
    pass


class DoctorUnavailableError(Exception):
    pass


class InvalidAppointmentDateError(Exception):
    pass


class Hospital:
    def __init__(self):
        self.doctors = {"Dr. Rao": True}

    def book_appointment(self, patient_name, doctor, appointment_date):
        if not patient_name.strip():
            raise InvalidPatientError("Patient name cannot be empty.")
        if doctor not in self.doctors or not self.doctors[doctor]:
            raise DoctorUnavailableError("Doctor is unavailable.")
        if appointment_date < date.today():
            raise InvalidAppointmentDateError("Appointment date cannot be in the past.")
        return "Appointment booked successfully."


try:
    hospital = Hospital()
    print(hospital.book_appointment("Anusha", "Dr. Rao", date.today()))
except (InvalidPatientError, DoctorUnavailableError, InvalidAppointmentDateError) as error:
    print(f"Hospital error: {error}")
