import random


states_in_nigeria=["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]
# print(len(states_in_nigeria))

num_state = len(states_in_nigeria)
print(num_state)
random_state=(random.randint(0,num_state - 1))
state_random =states_in_nigeria[random_state]
print(state_random)

# print(["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"])