class InvalidPatientError(Exception):
    pass


class Hospital:
    def register_patient(self, name, age, phone):
        if not name.strip():
            raise InvalidPatientError("Patient name cannot be empty.")
        if age <= 0:
            raise InvalidPatientError("Patient age must be positive.")
        if not phone.isdigit():
            raise InvalidPatientError("Patient phone must contain digits only.")
        return "Patient registered successfully."


try:
    hospital = Hospital()
    print(hospital.register_patient("", 25, "9876543210"))
except InvalidPatientError as error:
    print(f"InvalidPatientError: {error}")
