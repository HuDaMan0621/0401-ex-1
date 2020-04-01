#prompt the user for the missing words to a Madlib sentence using the input function.
#you can make up your own madlib sentence.
#example __(name)__'s favorite subject in school is _(subject)__.

print ('Welcome to DigitalCrafts, Please enter the following information')
student_name = input() #gets name input from student

greeting = f'Welcome, {student_name}' #prints  Welcome, (student_name)
print (greeting)

print ('please tell me what do you like to learn')
student_subject = input() #gets subject input from student

subject = f'you entered, {student_subject}' 
#prints student subject 

print ('please tell me where do you live')
student_address = input() #gets student address 
address = f'your address is, {student_address}' #prints student address

print ('please tell me your age')
student_age = input() #gets student age 
age = f'your age is, {student_age}' #see if int prints this way without converting


