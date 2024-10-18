#python output command

firstName = "Olowe"
lastName = " Daniel"
Age = 18
occupation = "Student"
fullName = firstName + lastName
#Expression 1

# print(" My name is "+ fullName + "\n My age is "+str(Age) + "\n I am a "+occupation)

# statement = f" My name is {fullName} \n I am {Age} years old \n I am a {occupation}"

# # print(statement)

# x, *y = 20,40, 50

# N = 20
# print(f"+{N}")

#DATA TYPES
    #i. Integgers e.g 10,30,343
    #ii. Floats e.g 10.3, 3.14, 2.718
    #iii. Complex e,g 3+4i
    #iiii. Strings e.g "Hello", "World", "AI"
    #v. Boolean e.g True, False

# name = 10

# namee = complex(name)
# print(namee)

    #2. text type
    #string str() e.g 'Dami'

    #3.
    # Boolean Type bool() e.g True, False

# isMarried = True
# print(str(isMarried))

# 4.) sequence type 
    # i.) tuple tuple() e.g ('ope','Mercy',34,True)
    #ii.) List list() e.g ['ope','Mercy',34,True]
    #iii.) range range() e.g range(20)

# myTuple = ('ope','Mercy',34,True)
# # print(len(myTuple))

# myList = ['ope','Mercy',34,True]

# print(type(myList,myTuple))

# var = range(1,22,4)

# print(list(var))

#5.) Mapping Type
#i. dictionary dict() e.g {name;'Dami',age: 20}

# person1 = {
#     'name':'Dami',
#     'age': 20,
#     'isMarried':True
# }

# print(type((person1)))

# print(person1['name'])

#6. set types

# i.) set set() e.g {'Ope','mercy','Daniel','Aliya'}
# ii.) frozen set

# frozenset(9,4,6,7,3,2,2,1)
# mySet = {'Ope','mercy','Daniel','Aliya'}



# num = {9,4,6,7,3,2,2,1}
# print(len((num)))

#7. Binary types
#   i.bytearray
#   ii.byte
# print(hex(100000))

# print(bytes(10))

# print(ord('+'))
# print(chr(99))


#comparison operator == !=

#modulous
# print(5//2)

#conditional statements
# num = 5

# if num == 5:
#     print('num is 5')
# else:
#     print('num is not 5')

# name = input('input your username: ')
# password = input('input your password: ')


# print(name, password)
# #password validation

# if len(password) < 8:
#     print('Your password must be greater than 8 characters')

# else:
#     print('Strong Password')

#     confirm_password = input('input confirm password: ')

#     if password == confirm_password:
#         print('passwords match. continue')
#     else:
#         print('password does not match')

# 4. LOGICAL OPERATORS and or not

#AND 

# username  ='Dami'
# password = '12345'

# print('Login')
# inp_user = input('username: ')
# inp_pass = input('Password: ')

# if inp_user == username and inp_pass == password:
#     print('Login successful')
# else:
#     print('wrong username or password')

# isActive = True

# if not isActive:
#     print('Access Denied')
# else:
#         print('Welcome')

# #5 MEMBERSHIP OPERATOR ==> in not in

# favourite_dishes = ['yam','rice','iyan',]

# print('rice' in favourite_dishes)

# #6. IDENTITY OPERATORS   is, is not

# num = 5
# num2 = 55
# print(num is not num2)

# # A simple calculator

# value1 = float(input('Firts value: '))
# # value2 = float(input('Second value: '))

# print(
#     '''
#         Option;
#     1. Addition
#     2. Subtraction
#     3. Division
#     #. Exit
#     '''
# )

# option = input('option: ')
# if option == '1':
#     result = value1 + value2
#     print(f'The Result is:{result}')
# elif option == '2':
#     result = value1 - value2
#     print(f'Result: {result}')
# elif option == '3':
#     result = value1 / value2
#     print(f'Result: {result}')
# elif option == '#':
#     print("goodbye ...")
#     exit()
# else:

# #Python Strings
# #Strings are s(equences of characters
# stud_name = 'DANIEL' #['D','A','N','I','E','L']
# print(stud_name[-6])
# #slicing
# print(stud_name[1:])

# num = int(input('number: '))
# res = num/2
# if isinstance(res, float) :
#     print('a odd dnum')
# else:
#     print('even')

expression = ' --Daniel/ is a python programmer and a /student at SQI college of ICT-- '
# # print(expression.capitalize())

# # print(expression.title())

# print('1. what is thecpital of Nigeria ?  a.)Lagos b.)Abuja')
# answer = input("Your Answer")

# if answer == 'b':
#     print('Correct Answer')


# print((expression.strip('-')))
# #leading white space and trailing white space, the space before and after spacing

# #strip() removes trailing and leading

# # print(expression.count('x'))

# # print(expression.split('/'))

# # item = ['+234','9042823291']
# # print(''.join(item))

# #LISTS IN DEPTH
# #Escape character

# students = ['mercy', 'ope', 'daniel', 'aliya','mercy']


# students[:2] = ['Abimbola','Abimbola']
# print(students)

# print(students.pop())

# arr = [
#     ['bannana','Apple','Orange'],
#     ['Rice','Beans'],
#     'Water',
#     34,
#     True
# ]

# print(arr[0][0])

# #For loop

# # for each_student in students:
# #     print(f'Welcome {each_student}')
# #  
# #    print('------------------------')

# info = []

# for i in range(5):
#     name = input(f'name{i+1}: ')
#     info.append(name)

# # print(info)

scores = [21,23,44,55,90,2,35]

# print(sum(scores))

# #Min Score

# min_score = min(scores)
# print(min_score)

# #Max scores

# max_score = max(scores)
# print(max_score)

students = ['Ayo','Dele','Ade','Danny','john','lee','bob']

for student, score in zip(students,scores):
    print(f'{student} scored {score}')

# join = zip(students,scores)

# question = [
#     'what is the capital of Nigeria? a.)accre b.)lagos',
#     'what is the most famous landmark in Africa? a.)Eiffel Tower b.)Mount Everest',
# ]

# answers = ['a','b']

# for quest, ans in zip(question,answers):
#     print(quest)
#     answer = input('Answer: ')
#     if answer.lower() == ans:
#         print('Correct')
#     else:
#         print('wrong')

# fruits = ('Banana','Orange','Apple')
# print(fruits)

# #unpacking

#Set : immutable/unchangeable, can't be indexed, not ordered, it doesn't accept duplicate value
#set() or {}

# fruits = {'Banana','mango','apple'}



# setA = {1,3,6,7,3,4,2,5,9,0}
# setB = {12,13,2,1,11}
# print(setA.union(setB))
# setC = {1,3,4}

# print(setA.issuperset(setC))

#Dictionary: ordered, not indexed but keyed, changeable, doesn't allow duplicates
phone = {
    'model':'Iphone16',
    'color':'Black',
    'rom':'128gb',
    'version':'ios18',
    'owner':{
        'name':'John Doe',
        'address':'Lagos'
    }
}

phone['model'] = 'Iphone18'
phone['sold'] = True

print(phone)

phone.values()

for val in phone.values():
    print(val)

print(phone.items())

ques_and_ans = {
    'Who was the first man in space?', 'a.) Niel Armstrong b.)Yuri Gagarin'
    'What is the capital of ghana?','a.)accra b.)Lagos'
}

for ques, ans in ques_and_ans:
    print(ques)
    user = input('answer ').strip()
    if user.lower():
        print('correct')
    else:
        print('wrong')

students = []
user = input('insert name , or 1 to stop')
while user != '1':
    user = input('insert name or 1 to stop')
    students.append(user)
print(students)

