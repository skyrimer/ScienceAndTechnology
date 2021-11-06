import os


def create_folder(path):
    """will create a folder if it does not exist already

    Args:
        path (str): path of the folder
    """
    if not os.path.exists(path):
        os.makedirs(path)


# Structure
# Year -> Subject -> Sections
root_folder = os.getcwd()
year = "2021-2022"
year_folder = os.path.join(root_folder, year)

# as the keys we have the top level folder
# as the values we have unique folders that are going to be created inside this the key folder
subject_dict = {
    "Business": [],
    "Physics": ["Experiments", "HL only"],
    "Economics": ["Presentations"],
    "Math AA": ["Teacher's notes"],
    "Russian": ["Евгений Онегин", "Мастер и Маргарита", "Анна Каренина", "Теория"],
    "English": ["Fahrenheit 451", "Frederick Douglass", "Paper 1 examples"],
    "CAS": ["Science and Technology", "Calisthenics gym training", "Learning the blind typing"],
    "TOK": ["Exhibition"]
}
section_list = ["Classwork", "Homework", "Written assignments"]

create_folder(year_folder)

for subject in subject_dict.keys():
    create_folder(os.path.join(year_folder, subject))
    for section in subject_dict[subject] + section_list:
        create_folder(os.path.join(subject_folder, section))
