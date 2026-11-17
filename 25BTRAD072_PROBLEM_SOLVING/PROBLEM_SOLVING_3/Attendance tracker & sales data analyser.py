attendance = {}


def add_student():
name = input("Enter student name: ") if name not in attendance:
attendance[name] = {"present": 0, "total": 0} print("Student added successfully!")
else:
print("Student already exists.")


def mark_attendance():
name = input("Enter student name: ")


if name in attendance:
status = input("Enter status (P/A): ").upper()


if status == "P": attendance[name]["present"] += 1
attendance[name]["total"] += 1
 
elif status == "A": attendance[name]["total"] += 1
else:
print("Invalid status!") return

print("Attendance recorded!") else:
print("Student not found.")


def display_attendance():
print("\n--- Attendance Report ---")
for name, record in attendance.items():
total = record["total"] present = record["present"]

if total > 0:
percentage = (present / total) * 100 else:
percentage = 0


print(f"{name}: Present={present}, Total={total}, " f"Percentage={percentage:.2f}%")

def check_shortage():
threshold = float(input("Enter minimum attendance percentage: "))


for name, record in attendance.items():
 
total = record["total"] present = record["present"]

percentage = (present / total * 100) if total else 0


if percentage < threshold:
print(f"{name}: {percentage:.2f}% - Below threshold")


while True:
print("\n1. Add Student") print("2. Mark Attendance") print("3. Display Attendance")
print("4. Check Attendance Shortage") print("5. Exit")

choice = input("Enter your choice: ")


if choice == "1": add_student()
elif choice == "2": mark_attendance()
elif choice == "3": display_attendance()
elif choice == "4": check_shortage()
elif choice == "5": print("Exiting program.") break
 
else:
print("Invalid choice!")
