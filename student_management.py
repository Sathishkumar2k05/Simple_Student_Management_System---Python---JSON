import json
import os



class StudentManagementSystem:
    def __init__(self, json_file = "students.json"):
        self.jsonfile = json_file
        self.students = self.load_students()
    def load_students(self):
        if not os.path.exists(self.jsonfile):
            return []
        with open(self.jsonfile, "r") as file:
            return json.load(file)
    def save_students(self):
        with open(self.jsonfile, "w") as file:
            json.dump(self.students, file, indent=4)
    def add_student(self):
        try:
            print(" --- Student Add Page --- ")
            reg_no = input("Enter register number : ")
            name = input("Enter name : ")
            age = int(input("Enter age : "))

            for student in self.students:
                if student["reg_no"] == reg_no:
                    print("Duplicate entry! student already exists!")
                    print()
                    return

            student = {
                "reg_no": reg_no,
                "name": name,
                "age": age
            }
            self.students.append(student)
            self.save_students()
            print("Student added successfully!")
            print()
        except ValueError:
            print("Invalid Age! Try Again!")
            print()
    def view_students(self):
        print(" --- Student List Page --- ")
        if not self.students:
            print("Students not found")
            print()
        else:
            for student in self.students:
                print(f"""Register Number : {student["reg_no"]}, Name : {student["name"]}, Age : {student["age"]}""")
        print()
    def search_student(self):
        print(" --- Search Student --- ")
        reg_no = input("Enter register number for search : ")
        for student in self.students:
            if student["reg_no"] == reg_no:
                print(f"""Register Number : {student["reg_no"]}, Name : {student["name"]}, Age : {student["age"]} """)
                print()
                break
        else:
            print("Student not found!")
            print()
    def update_student(self):
        print(" --- Student Update Page --- ")
        try:
            reg_no = input("Enter a register number for update : ")
            for student in self.students:
                if student["reg_no"]==reg_no:
                    student["name"] = input("Enter new name : ")
                    student["age"] = int(input("Enter new age : "))
                    self.save_students()
                    print("Student updated successfully")
                    print()
                    return
            else:
                print("student register number does not match!")
            print()
        except ValueError:
            print("Invalid Age! Try Again!")
            print()
    def delete_student(self):
        print(" --- Student Delete Page --- ")
        reg_no = input("Enter register number for delete : ")
        for student in self.students:
            if student["reg_no"] == reg_no:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                print()
                return
        else:
            print("Student not found!")
        print()
def main():
    sms = StudentManagementSystem()
    while True:
        print("Add student enter 1")
        print("View all students enter 2")
        print("Search student enter 3")
        print("Update student enter 4")
        print("Delete student enter 5")
        print("Exit student enter 6")
        print()
        choice = input("Enter your choice : ")
        if choice=="1":
            sms.add_student()
        elif choice=="2":
            sms.view_students()
        elif choice=="4":
            sms.update_student()
        elif choice=="3":
            sms.search_student()
        elif choice=="5":
            sms.delete_student()
        elif choice=="6":
            print("exiting...")
            break
        else:
            print("incorrect choice")
main()