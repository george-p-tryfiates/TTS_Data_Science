
#You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
#Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

#Complete the Student class by writing the following:
#A Student class constructor, which has 4 parameters:
#- A string, firstName
#- A string, lastName
# An integer, id
#An integer array (or vector) of test scores, scores

#A char calculate() method that calculates a Student object's average and returns the grade 
#character representative of their calculated average:
#A | 90-100
#B | 80-89
#C | 70-79
#D | 60-69
#F | <60

class Person(object):
    first = ""
    last = ""
    def __init__(self, first, last):
        self.first = str(first)
        self.last = str(last)

class Student(Person):
    def __init__(self, first, last, id, scores):
        super().__init__(first, last)
        self.id = id
        self.scores = scores
    def __avg__(self, scores):
        avg = sum(scores)/len(scores)
        return avg
    def __calculate__(self, avg):
        if 90<=avg<=100:
            return "A"
        elif 80<=avg<=89:
            return "B"
        elif 70<=avg<=79:
            return "C"
        elif 60<=avg<=69:
            return "D"
        else:
            return "F"

first = input("Hello! Please enter student first name: ")
last = input("Please enter student last name: ")
id = int(input("Please enter student ID: "))
scores = list(map(int, input("Please enter test scores (space-separated #'s): ").split(' ')))
print("Thanks!")
print(" ")
#first, last, id, scores = "jerry", "smith", 4, [12, 33, 99, 44, 100, 88, 40]

student1 = Student(first, last, id, scores)
avg = student1.__avg__(scores)
grade = student1.__calculate__(avg)
print("The student got a letter grade of", grade, "for the year.")