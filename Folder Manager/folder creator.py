import os


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Structure
# Year -> Subject -> Sections
root_folder = os.getcwd()
year = "2021-2022"
year_folder = os.path.join(root_folder, year)

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
    subject_folder = os.path.join(year_folder, subject)
    create_folder(subject_folder)
    for section in subject_dict[subject] + section_list:
        create_folder(os.path.join(subject_folder, section))
