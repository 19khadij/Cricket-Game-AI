import random

#generate random numbers from 0.0 to 1.0
print("generate random numbers from 0.0 to 1.0")
random_number=random.random()
print(random_number,"\n")

#generate random integer 
print("generate random integer ")
random_integer=random.randint(1,10)
print(random_integer,"\n")

#generate random numbers with step
print("generate random numbers with step")
random_step=random.randrange(1,10,2)
print(random_step,"\n")

#Choose a random element
print("Choose a random element")
random_choice=random.choice(["chocolate","beans","caramel"])
print(random_choice,"\n")

#Shuffle the list
print("Shuffle the list")
items=["chocolate","beans","caramel"]
random.shuffle(items)
print(items,"\n")

#Generate random sample
print("Generate random sample")
items=[1,2,3,4,5,6,7,8,9,0]
sample=random.sample(items,3)
print(sample,"\n")

#generate float within a range
print("Generate float within a range")
random_float=random.uniform(1.5,5.5)
print(random_float,"\n")

#You can set a seed to produce the same random sequence every time
print("Generate seed")
#random.seed(50)
print(random.random())
print(random.randint(1,10))

#generating numbers based on a Gaussian (normal) distribution
print("\nGaussian")
gaussian=random.gauss(1,10)
print(gaussian)

import string
#generate password
def generatePassword(param: int):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(param))
    return password


print(generatePassword(12))