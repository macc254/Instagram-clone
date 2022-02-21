print("what is your age?")
age = int(input())
currentyear = 2021
yob = currentyear - age

print( 'Hello you ere born in the year '+ str(yob) )

print('Enter your bill')
bill = int(input())
tip = bill * 0.15
totalbill = bill + tip

print("input service")
service = int(input())

if service == 0:
        print("The service was Terrible")
elif service < 20:
        print("The service was Good")
elif service < 60:
    print(" The service was Better")
else:
    print("The service was the Best!!")

print('Your totalbill is ' + str(totalbill))

name = ""
list_a = []

if list_a:
    print("I will not run")
else:
        print("I am Empty")



name = "James"
age = 19
weight = '79' # Kilograms

age_weight_ratio = int(weight)/age

print(age_weight_ratio)

greetings = 'Hello, Moringa!'

part_one = greetings[0:7] # slicing starting from the front 
print(part_one)

greetings = 'Hello, Moringa!'

part_one = greetings[-8:-1] #backwards slicing
print(part_one)

greetings = 'Hello, Moringa!'

part_one = greetings[0:] #no slicing
print(part_one)

number = [1,2,3,4,5,6,7,8,9]
four_digits = number[:4] # slicing lists
print(four_digits)