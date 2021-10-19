fruits = ["apple", "orange"]
for fruit in fruits:
  print(fruit)

student_heights = input("Student heights: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)

counter = 0
sum = 0
for height in student_heights:
  sum += height
  counter += 1

print(f"Average: {sum/counter}")
print(10/4)

