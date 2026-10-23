
print("=== Grade Calculator ===")

name = input("Enter your name: ")
prelim = float(input("Enter your Prelim grade: "))
midterm = float(input("Enter your Midterm grade: "))
finals = float(input("Enter your Finals grade: "))

average = (prelim + midterm + finals) / 3

print("\nStudent:", name)
print("Average:", round(average, 2))

if average >= 75:
    print("Status: PASSED")
else:
    print("Status: FAILED")
