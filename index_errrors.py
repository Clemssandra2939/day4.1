
# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi","Plateau",
# "Akwa Ibom","Bayelsa","Benue","Borno","Delta","Gombe","Jigawa","Kano","Katsina","Nasarawa","Ogun","Ondo","Osun","Oyo","Rivers","Sokoto","Taraba","Yobe","Zamfara",]
# # print(len(states_in_nigeria))
# print(states_in_nigeria[33 ])

# where by a situation like this:to get rid of a index error making 1 to be 0

# states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi","Plateau",
# "Akwa Ibom","Bayelsa","Benue","Borno","Delta","Gombe","Jigawa","Kano","Katsina","Nasarawa","Ogun","Ondo","Osun","Oyo","Rivers","Sokoto","Taraba","Yobe","Zamfara",]
# num_of_states= (len(states_in_nigeria))
# print(states_in_nigeria[num_of_states -1 ])


# Nested list(making a list in a list)
# dirty dozen are fruits and vegetables that high in pesticide

# # Create a list of dirty dozen
# dirty_dozen=["Strawberries","Spinach","Kale","Nectarines","apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
# # Split between fruit and vegetable
# fruits =["Strawberries","Nectarines","apples","Grapes","Peaches","Cherries","Pears"]
# vegetables =["Kale","Spinach","Tomatoes","Celery","Potatoes"]

# dirty_dozen=[fruits,vegetables]
# print(dirty_dozen)

# now we hv a list in a list


# Treasure Map coding char
row1 =["⬜","⬜","⬜"]
row2 =["⬜","⬜","⬜"]
row3 =["⬜","⬜","*"]
map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
poistion =input("Where do u want to put the treasure?")

horizonital_side =int(poistion[0])

vertical_side =int(poistion[0])

used_row = map[vertical_side- 1]
used_row = map[horizonital_side - 1 ]



print(f"{row1}\n{row2}\n{row3}")