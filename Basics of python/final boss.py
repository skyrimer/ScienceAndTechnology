age_list = [13, 13, 15, 16, 17, 34]


def my_function(age_list):
    minimum, maximum = age_list[0], age_list[1]
    for age in age_list:
        if age < minimum:
            minimum = age
        if age > maximum:
            maximum = age

    print(age_list)
    print("Minimum age -", minimum)
    print("Maximum age -", maximum)
    print(age_list[1:-1])


my_function(age_list)
my_function(age_list[::-1])











