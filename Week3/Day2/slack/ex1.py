class Employee:
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job, emp_salary):
        self.firstname = emp_fn
        self.lastname = emp_ln
        self.age = emp_age
        self.job = emp_job
        self.salary = emp_salary

    def get_fullname(self):
        fullname = self.firstname + " " + self.lastname
        return fullname

    def happy_birthday(self):
        self.age += 1

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount

    def show_employee(self):
        print(f"{self.firstname} {self.lastname} {self.age} {self.job} {self.salary}")


class Developer(Employee):
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job="developer", emp_salary=15000, coding_skills=[]):
        super().__init__(emp_fn, emp_ln, emp_age, emp_job, emp_salary)
        self.coding_skills = coding_skills

    def add_skills(self, skills):
        for i in range(len(skills)):
            if (skills[i] not in self.coding_skills):
                self.coding_skills.append(skills[i])

    def coding(self):
        print(self.coding_skills)

    def coding_with_partner(self, other_dv):
        print(f"{self.firstname} is working with {other_dv.firstname} ,{self.firstname} knows {self.coding_skills} and {other_dv.firstname} knows {other_dv.coding_skills}")

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount


class Manager(Employee):
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job="manager", emp_salary=15000, list_employees=[]):
        super().__init__(emp_fn, emp_ln, emp_age, emp_job, emp_salary)
        self.list_employees = list_employees

    def add_new_employee(self, new_employee):
        for i in range(len(new_employee)):
            if (new_employee[i] not in self.list_employees):
                self.list_employees.append(new_employee[i])

    def show_employees(self):
        for employee in self.list_employees:
            print(employee.firstname)


person1 = Developer("tom", "cruiz", 30)
person2 = Developer("angelina", "jolie", 23)
person1.show_employee()
person2.show_employee()
person1.add_skills(["python"])
person1.coding()
person1.coding_with_partner(person2)
person1.get_promotion(2)
person1.show_employee()
manager1 = Manager("brad", "pit", 50)
manager1.add_new_employee([person1, person2])
manager1.show_employee()
manager1.show_employees()
