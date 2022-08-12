number = 10
while number >= 10:
  number -= 1
  print(number)

strings = ["a", "b", "c", "d", "e"]
strings.append("f")
print(strings)
strings.insert(0,1.2)

print(strings)
#strings.pop(0)
#print(strings)

student_info = {"Sally": [10, "Math", 15], "Bob": [12, "History", 18] }
student_info.pop("Bob")
print(student_info)

#CSV Practice
import csv
rows = []
with open("state.csv", 'r) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
