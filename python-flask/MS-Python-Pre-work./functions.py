# create function
def fun_a():
    print("I have been called")

fun_a()

#pass parameters into a function

def fun_a (a,b):
    print(a+b)

fun_a(1,4)
# reassign parameters
def fun_a(a = 1,b = 4):
    print(a+b)

fun_a(a=6,b=7)

#without passing parameters
def fun_a(a = 1,b = 4):
    print(a+b)

fun_a()

# Empty function ensure to use pass so that you dont get an error
def fun_a():
    pass

# return values
def fun_a (a,b):
    return a+b

sum = fun_a(4,5)

print(sum)