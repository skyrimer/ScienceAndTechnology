choices = {
    'Cv Creator': [1, 6, 7, 8],
    'Folder manager': [9, 9, 9, 10, 10],
    'Finding simular pictures': [5, 6, 6, 8, 8],
    'Timetable': [5, 8, 10, 10],
    'Custom calculators': [5, 6, 6, 7, 9],
    'Parser': [4, 5, 7, 8, 9],
    'Basics of Excel': [1, 7, 8, 9],
    'Routine stuff': [5, 8, 8, 8, 9],
    'Simple games': [4, 5, 6, 8, 9],
    'Password manager and generator': [1, 7, 8, 9, 10],
    'Creating websites': [5, 6, 8, 8, 9],
}
sorted_choices = dict(
    sorted(choices.items(), key=lambda choice: sum(choice[1]), reverse=True))
counter = 0
for key, value in sorted_choices.items():
    counter += 1
    print(f"{counter} - {key} with score {sum(value)}")
