# In python programing contionals are used to make decision and they let your program choose what to do based on conditions.
# Main conditionals statements are (if,else and elif).

#1.Basic (if) statement:
# Used to run code if statement is true.
# example:like Door lock system with one condition. 
pin = 1234
if pin == 1234: # Run if pin is correct
    print('Successfully un_locked the door') 

#2.(if,else) statement:
# Run when (if) statement is wrong.
# example:like Door lock system with two conditions
pin = 123
if pin == 1234: # Run if pin is correct
    print('Successfully un_locked the door')
else: # Run if pin is incorrect
    print('(Wrong) Enter valid pin')

#3. (if,else,elif) statement:
# Used when you have multiple conditions to check.
# example:like players score count system and give rank
score = 80
if score >=90:          # Runs only if score is 90 or more
    print('1st_rank')
elif score >=80:        # Runs if score is 80 or more AND less than 90
    print('2nd_rank')
elif score >=70:        # Runs if score is 70 or more AND less than 80
    print('3rd_rank')
else:                   # Runs if score is below 70
    print('Eliminate')

#4. Nested if (if inside another if) statement:
# Used when one condition depends another condition.
# example:like course eligiblity system
age = 19
student = True
if age>=18 and age<=35: # Check age eligibility
    if student:  # Check student status
        print('You are eligible in this course')  # Both conditions are true  
    else:
        print('You must be a student') # Age is okay, but not a student
else:
    print('You are not eligible')  # Age is outside the range



