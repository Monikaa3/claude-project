import json
import os

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        s = Student(data["student_id"], data["name"], data["age"], data["course"])
        s.marks = data["marks"]
        return s


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def list_students(self):
        for s in self.students:
            print(s.student_id, s.name, s.course)

    def save_to_file(self, filename):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
            self.students = [Student.from_dict(d) for d in data]


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def prime_numbers(limit):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def show_menu():
    print("\n1. Add Student")
    print("2. Add Marks")
    print("3. Show Students")
    print("4. Delete Student")
    print("5. Save")
    print("6. Load")
    print("7. Algorithms Demo")
    print("8. Exit")


def algorithms_demo():
    nums = [5, 2, 9, 1, 5, 6]
    print("Original:", nums)
    print("Sorted:", bubble_sort(nums.copy()))

    print("Search 9:", linear_search(nums, 9))

    print("Factorial 5:", factorial(5))

    print("Fibonacci 10:", fibonacci(10))

    print("Primes under 30:", prime_numbers(30))


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")

            s = Student(sid, name, age, course)
            manager.add_student(s)

        elif choice == "2":
            sid = input("Student ID: ")
            student = manager.find_student(sid)

            if student:
                subject = input("Subject: ")
                mark = int(input("Mark: "))
                student.add_mark(subject, mark)
            else:
                print("Student not found")

        elif choice == "3":
            manager.list_students()

            for s in manager.students:
                print("Average:", s.average())

        elif choice == "4":
            sid = input("Student ID: ")
            manager.delete_student(sid)

        elif choice == "5":
            manager.save_to_file("students.json")
            print("Saved")

        elif choice == "6":
            manager.load_from_file("students.json")
            print("Loaded")

        elif choice == "7":
            algorithms_demo()

        elif choice == "8":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()


def extra_function1():
    data = [1,2,3,4,5]
    return [x*x for x in data]


def extra_function2():
    words = ["python","java","dotnet"]
    return [w.upper() for w in words]


def extra_function3():
    d = {"a":1,"b":2,"c":3}
    for k,v in d.items():
        print(k,v)


def extra_function4():
    total = 0
    for i in range(10):
        total += i
    return total


def extra_function5():
    text = "hello world"
    return text[::-1]


def extra_function6():
    nums = list(range(20))
    even = [n for n in nums if n%2==0]
    return even


def extra_function7():
    matrix = [[1,2],[3,4]]
    for row in matrix:
        print(row)


def extra_function8():
    s = set([1,2,2,3,4])
    return list(s)


def extra_function9():
    try:
        x = int("10")
        return x
    except:
        return 0


def extra_function10():
    with open("temp.txt","w") as f:
        f.write("hello")