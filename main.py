# Randomisation and python lists

# import random 
# # for importing random integers
# random.seed(123)
# randomInteger=random.randint(20,40)
# print(randomInteger)

# # for importing random floating numbers from betweeen 0 to 1 but not including 1
# randomFloat=random.random()
# print(randomFloat)

# # How to create a random floating number between 0 to 5
# randomFloat=random.random()* 5
# print(randomFloat)

# in our previous challenge love score
# love_score= random.randint(1,100)
# print(f"Your love score is {love_score}")

# this random function can be used in diccing and games,flipping coins to create randomization


# Head or tail coin coding exercise
import random 
test_seed=int(input("create a seed number "))

random.seed(test_seed)

random_side=random.randint(0,1)
if random_side==1:
    print("Heads")

else:
    print==("Tails")

