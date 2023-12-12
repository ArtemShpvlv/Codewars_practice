# codewars practice Sh.Artem

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    pr_money = 0
    name = ""
    counter = 0
    for student in students:
        money = student.fives * 5 + student.tens * 10 + student.twenties * 20
        if money > pr_money:
            pr_money = money
            name = student.name
        elif money == pr_money:
            counter += 1
            if counter == len(students) - 1:
                name = "all"
        else:
            pr_money = pr_money
            name = name
    return name


phil = Student("Phil", 1, 1, 1)
cam = Student("Cameron", 1, 1, 1)
geoff = Student("Geoff", 1, 1, 1)
artem = Student("Artem", 2, 1, 1)

print(most_money([phil, cam, geoff, artem]))
