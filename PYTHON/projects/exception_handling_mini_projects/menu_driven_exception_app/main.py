class InvalidAgeError(Exception):
    pass


class MenuApplication:
    def divide(self):
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            result = first / second
        except ValueError:
            print("Error: Enter numbers only.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {result}")
        finally:
            print("Division operation finished.")

    def validate_age(self):
        try:
            age = int(input("Enter age: "))
            if age < 18:
                raise InvalidAgeError("Age must be 18 or above.")
        except ValueError:
            print("Error: Enter a whole number.")
        except InvalidAgeError as error:
            print(f"Custom exception: {error}")
        else:
            print("Age is valid.")
        finally:
            print("Age validation finished.")

    def run(self):
        print("1. Divide numbers")
        print("2. Validate age")
        choice = input("Choose an option: ")
        if choice == "1":
            self.divide()
        elif choice == "2":
            self.validate_age()
        else:
            raise ValueError("Invalid menu choice.")


try:
    MenuApplication().run()
except ValueError as error:
    print(f"Application error: {error}")
