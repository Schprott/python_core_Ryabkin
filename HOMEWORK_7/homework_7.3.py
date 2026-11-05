# Создаём класс врача
class Doctor:
    def treat(self):
        print("Общий метод лечения")

# Создаём класс хирурга и наследуем от родительского
class Surgeon(Doctor):
    def treat(self):
        print("Лечение у хирурга")

# Создаём класс дантистаи  наследуем от родительского
class Dentist(Doctor):
    def treat(self):
        print("Лечение у дантиста")

# Создаём класс терапевта и наследуем от родительского
class Therapist(Doctor):
    def treat(self):
        print("Лечение у терапевта")

    # Создаём метод назначения врача
    def assign_doctor(self, patient):
        # Если план лечения равен 1, назначаем хирурга
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        # Если план лечения равен 3, назначаем дантиста
        elif patient.treatment_plan == 3:
            patient.doctor = Dentist()
        # Во всех остальных случаях назначаем терапевта
        else:
            patient.doctor = Therapist()

# Создаём класс пациента
class Patient:
    # Задаём план лечения
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None

# Создаём переменную терапевта для назначения врачей
therapist = Therapist()
# Создаём переменную пациента с планом лечения
patient = Patient(1)

# Назначаем пациенту врача по результаатм перебора
therapist.assign_doctor(patient)

# Вызываем метод лечения назначенного врача
patient.doctor.treat()