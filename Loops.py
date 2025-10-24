# Loops are used to repeat a block of code multiple time either a fixed number of times or until a condition is met
# There are two main types of loops 

# 1.(for) loop:
# Used to iterate over a sequence (like a list, tuple, string, or range).
# 1.example:(for) loop through a list 
student_list = ['kaif','ali','ahamed','abbas','waqas','noor','wahab']
for student_list in student_list:
    print(student_list)

# 2.example: Using range
for i in range(0,5):
    print(i)

# 3.example: Using list and range
student_list = ['kaif','ali','ahamed','abbas','waqas','noor','wahab']
for i in range(5):
    print(student_list[i])

 # 2.(while) loop:
 # Run as long as a condition is true
 # example:
Count = 1
while Count <= 5:
    print("Count:", Count)
    Count += 1

# loop control statements
# Used to control loop
# 1.(break) Stop the loop imediatly
# example: using (break) statement 
for i in range(1,5):
    if i == 3:
        break
    print(i)

# 2.(continue) Skips the current iteration
# example: using (continue) statement
for i in range(1,5):
    if i == 3:  
        continue 
    print(i)
