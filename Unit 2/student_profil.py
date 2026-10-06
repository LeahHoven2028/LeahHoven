name = input("What is your name? ")
age = int(input("What is your age? "))
hometown = input("What is your hometown? ")
favorite_food = input("What is your favorite food? ")
favorite_hobby = input("What is your favorite hobby? ")

school_name = input("What is the name of your school? ")
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? ")
hours_study = float(input("How many hours do you study each week? "))
grad_year = int(input("What year are you graduating? "))

dream_job = input("What is your dream job? ")
skills_to_learn = input("What skills do you want to learn? ")
places_to_visit = input("What places do you want to visit? ")
personal_goal = input("What is your personal goal? ")
school_goal = input("What is your school goal? ")

def profile_one(name, age, hometown, favorite_food, favorite_hobby):
    print("Name: " + name)
    print("Age: " + str(age))
    print("Hometown: " + hometown)
    print("Favorite Food: " + favorite_food)
    print("Favorite Hobby: " + favorite_hobby)

def profile_two(school_name, grade, favorite_subject, hours_study, grad_year):
    print("School Name: " + school_name)
    print("Grade: " + str(grade))
    print("Favorite Subject: " + favorite_subject)
    print("Hours of Study per Week: " + str(hours_study))
    print("Graduation Year: " + str(grad_year))

def profile_three(dream_job, skills_to_learn, places_to_visit, personal_goal, school_goal):
    print("Dream Job: " + dream_job)
    print("Skills to Learn: " + skills_to_learn)
    print("Places to Visit: " + places_to_visit)
    print("Personal Goal: " + personal_goal)
    print("School Goal: " + school_goal)

print(profile_one(name, age, hometown, favorite_food, favorite_hobby))
print(profile_two(school_name, grade, favorite_subject, hours_study, grad_year))
print(profile_three(dream_job, skills_to_learn, places_to_visit, personal_goal, school_goal)) 
