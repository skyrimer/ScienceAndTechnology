# getting the ages from input funcion and assigning the values
my_age = int(input("Enter your age: "))
neighbor_age = int(input("Enter the age of the neighbor: "))

# printing all the variables
# function print can print unlimited amount of values,
# so we can pass different arguments
if my_age == neighbor_age:
    print("Our age is the same")
elif my_age > neighbor_age:
    print("I am the oldest with age -", my_age)
    print("The difference is ", my_age - neighbor_age)
elif my_age < neighbor_age:
    print("My neighbor is the oldest with age -", neighbor_age)
    print("The difference is ", neighbor_age - my_age)












