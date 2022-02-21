handle = open("text.txt","r")
data = handle.read()
print (data)
handle.close()

counter = 0 # split fn transforms data into word that can be looped thru to find python
for word in data.split(): #for loop to count number of times the word python
    if word == "Python": #appears in the text
       counter += 1

print(counter)