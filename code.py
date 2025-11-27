# Student Management System

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade/Class: ")
    
    student = {"Roll": roll, "Name": name, "Grade": grade}
    students.append(student)
    print("\nStudent Added Successfully!\n")

def view_students():
    if len(students) == 0:
        print("\nNo Records Found!\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['Roll']} | Name: {s['Name']} | Grade: {s['Grade']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["Roll"] == roll:
            print(f"\nStudent Found: Roll: {s['Roll']} | Name: {s['Name']} | Grade: {s['Grade']}\n")
            return
    print("\nStudent Not Found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("\nStudent Record Deleted Successfully!\n")
            return
    print("\nStudent Not Found!\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s["Roll"] == roll:
            print("Enter New Details:")
            s["Name"] = input("New Name: ")
            s["Grade"] = input("New Grade: ")
            print("\nRecord Updated Successfully!\n")
            return
    print("\nStudent Not Found!\n")

while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        print("Exiting Program... Thank you!")
        break
    else:
        print("\nInvalid Choice! Try Again.\n")
