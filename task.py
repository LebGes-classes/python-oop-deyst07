class Bachelor:
    def __init__(self, surname="", specialty="", course=1):
        self.surname = surname
        self.specialty = specialty
        self.set_course(course)
        self.on_leave = False

    def get_surname(self):
        return self.surname

    def get_specialty(self):
        return self.specialty

    def get_course(self):
        return self.course

    def set_surname(self, surname):
        self.surname = surname

    def set_specialty(self, specialty):
        self.specialty = specialty

    def set_course(self, course):
        if 1 <= course <= 4:
            self.course = course
        else:
            print("Ошибка: Курс должен быть от 1 до 4.")

    def info(self):
        status = "в академическом отпуске" if self.on_leave else "обучается"
        print(f"Фамилия: {self.surname}, Специальность: {self.specialty}, Курс: {self.course}, Статус: {status}")

    def change_course(self):
        if self.course < 4:
            self.course += 1
            print("Повышен курс!")
        else:
            print("Максимальный курс — 4.")
    
    def take_academic_leave(self):
        if not self.on_leave:
            self.on_leave = True
            print(f"Бакалавр {self.surname} переведён в академический отпуск.")
        else:
            print(f"Бакалавр {self.surname} уже в академическом отпуске.")


def menu(bachelors):
    while True:
        if not bachelors:
            print("Нет бакалавров. Программа завершена.")
            break
        
        print("\nМеню:")
        print("1. Просмотреть данные")
        print("2. Установить фамилию")
        print("3. Установить специальность")
        print("4. Установить курс")
        print("5. Повысить курс")
        print("6. Академический отпуск")
        print("7. Выход")

        choice = input("Выберите действие: ")
        
        if choice == "7":
            print("Работа завершена.")
            break
        
        idx = int(input(f"Выберите бакалавра (от 1 до {len(bachelors)}): ")) - 1
        if idx not in range(len(bachelors)):
            print("Ошибка выбора!")
            continue

        if choice == "1":
            bachelors[idx].info()
        elif choice == "2":
            surname = input("Введите фамилию: ")
            bachelors[idx].set_surname(surname)
        elif choice == "3":
            specialty = input("Введите специальность: ")
            bachelors[idx].set_specialty(specialty)
        elif choice == "4":
            course = int(input("Введите курс (1-4): "))
            bachelors[idx].set_course(course)
        elif choice == "5":
            bachelors[idx].change_course()
        elif choice == "6":
            bachelors[idx].take_academic_leave()
        else:
            print("Неизвестная команда.")


def main():
    print("Создание первого бакалавра:")
    bachelor1 = Bachelor()
    bachelor1.info()

    print("Создание второго бакалавра с параметрами:")
    bachelor2 = Bachelor("Иванов", "Информатика", 2)
    bachelor2.info()

    bachelors = [bachelor1, bachelor2]
    menu(bachelors)

if __name__ == "__main__":
    main()
