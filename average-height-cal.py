print("#######################################")
print("## AVERAGE STUDENT HEIGHT CALCULATOR ##")
print("#######################################")
#test heights: 123 149 175 183 166 179 125
student_heights = input("   Input a list of student heights:\n>> ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#print(student_heights)

total = 0
for num in student_heights:
    total += num
#print(total)

def list_height(student_heights):
  counter = 0
  for char in student_heights:
    counter += 1
  return counter
length = list_height(student_heights)
#print(length)
ave = round(total / length)
print(f"Average student height is: {ave}")