students = {}

def add_student():
    name = input("Enter student name: ")
    marks = [int(m) for m in input("Enter marks (comma separated): ").split(",")]
    students[name] = marks

def view_results():
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: {marks} | Avg: {avg:.2f}")

def analyze_results():
    all_marks = [m for marks in students.values() for m in marks]
    avg = sum(all_marks) / len(all_marks)
    print("\n=== Analysis ===")
    print("Class Average:", avg)
    print("Highest Mark:", max(all_marks))
    print("Lowest Mark:", min(all_marks))
    passed = sum(1 for m in all_marks if m >= 40)
    print("Pass %:", (passed / len(all_marks)) * 100)

def ascii_chart():
    print("\n=== ASCII Chart ===")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: " + "█" * int(avg // 5) + f" ({avg:.1f})")

# Example run
add_student()
view_results()
analyze_results()
ascii_chart()
