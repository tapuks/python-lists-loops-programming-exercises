#Remember import random function here:
import random
my_list = [4,5,734,43,45]

#The magic is here:

for x in range(10):
    my_list.append( random.randint(1,999) )

print(my_list)