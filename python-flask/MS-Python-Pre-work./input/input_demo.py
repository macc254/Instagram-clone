# import sys
# print("What is your name?")

# name = sys.argv[1]

# print("How old are you?")
# age = int(input())

# print(name)
# print(age)

print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
    characters[character] = characters[character] + 1

print(characters)