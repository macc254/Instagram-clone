my_list = []
my_other_list =list()

list_a = ["a","b","c","d"] # list of strings
list_b = [1,2,3,4,5,6] # list of numbers
list_c = [1,"west",34,"longitude"] # mixed list
list_d = [ ["a","b","c","d"],[1,2,3,4,5,6],[1,"west",34,"longitude"]] # nested list
list_a = ["a","b","c","d"] 
list_b = [1,2,3,4,5,6]

# Joining list_b to list_a

list_a.extend(list_b)

print(list_a) # this will print ["a","b","c","d",1,2,3,4,5,6]
print(list_b) # this will print [1,2,3,4,5,6]

list_a.append("e")

print(list_a) # ["a","b","c","d","e"] e wil be added to the list

list_a.reverse()

print(list_a) # ['d', 'c', 'b', 'a'] this will reverse the list

list_a = [1,3,4,8,5,7,6,2]
list_a.sort()

print(list_a) # [1, 2, 3, 4, 5, 6, 7, 8] will arrange the list in order

#tuples- values cannot be changed once created

tuple_a = ("a","b","c","d") # tuple of strings
tuple_b = (1,2,3,4,5,6) # tuple of numbers
tuple_c = (1,"west",34,"longitude") # mixed tuple
tuple_d = tuple() #empty tuple

#dictionaries--dictionaries store collections of many values of different types. Unlike indexes for lists - which are integers and start from 0, dictionary indexes don't have to be integers. They can be of different data types like strings. Indexes in dictionaries are called keys. The value here is appropriately called the value.
# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name':'Mr sniffles','age':18, 'color':'black'}
cat_name = my_cat['name']
print(cat_name) # 'Mr sniffles'

birthdays = {"John":"August 1","Marcus":"April 8"}
birthdays["mary"] = "September 14"
print(birthdays) # this prints {"John":"August 1","Marcus":"April 8","Mary":"September 14"}

birthday = {"John":"August 1","Marcus":"April 8","Mary":"September 14"}

print(birthday.keys()) # this prints dict_keys(['John', 'Marcus', 'Mary'])

birthday = {"John":"August 1","Marcus":"April 8","Mary":"September 14"}

print(list(birthday.keys())) # this prints ['John', 'Marcus', 'Mary'] convert to list

