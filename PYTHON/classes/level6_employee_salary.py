class Employee:
    def __init__(self, name, daily_rate):
        self.name = name
        self.daily_rate = daily_rate

    def calculate_salary(self, working_days):
        if working_days < 0:
            raise ValueError('Working days cannot be negative')
        return self.daily_rate * working_days

if __name__ == '__main__':
    e = Employee('Vikram', 1000)
    print('Salary for 22 days:', e.calculate_salary(22))
