# Understanding the offset and Appending Items to lists

# list:it is called data structure which is a way of oranizing and storing data in python
# it is used to store a group of data  that have some conctio with each other Unlike variable that can contain one piece of data

# List can be represented like this:
# fruits=[items1,items2] in a set of block bracket like this and those items can be any data type or mixed data types
# eg with storing strings together with numbers or a set of booleans

# states_of_america=["Delaware","Pennsylvania","New Jersey","Geogia"]
# print(states_of_america[0])

# when u want to start counting from the end u use [-] 

# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]
# print(states_in_nigeria[-1])

# if the case where u want to change a piece of data for a exampl like the spelling
# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]
# states_in_nigeria[4]= "Awka"
# print(states_in_nigeria)

# when u hv any extra piece of data u want to add at the end in ur list...u do this:
# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]
# states_in_nigeria[4]= "Awka"
# states_in_nigeria.append("Nnewi")
# print(states_in_nigeria)

# to extend the list
# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]
# states_in_nigeria[4]= "Awka"
# states_in_nigeria.extend(["Nnewi","Onitsha","Nsukka"])
# print(states_in_nigeria)

# Who is paying coding char
import random
test_seed =int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names,separated by a comma:")
names = namesAsCSV.split(",")

# Get the total number of items in list
num_items= len(names)
# generate random number between 0 and the last number
random_names =random.randint(0,num_items - 1)
person_who_will_pay =names[random_names]

print(person_who_will_pay +"  is going to buy the meal today!")