# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
skills={
    "skill_show":[
        {"sk":"Java","id":1},
        {"sk":"python","id":2},
        {"sk":"C++","id":3}
             ]
          }
def get_skills():
    skills={
    "skill_show":[
        {"sk":"Java","id":1},
        {"sk":"python","id":2},
        {"sk":"C++","id":3}
             ]
          }
    return skills




# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print("Skills:\n")
    for skill in skills:
        for skil in skills["skills_show"]:
         print(skil.get("id"),skil.get("sk"))


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    userskill=[]
    
    print(show_skills(skills))
    for x in range(2):
        userskill=input("please choose:")
    return userskill
 


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
      skil= {"name":"","age":"","experience":"",
       "skills":[]
         }

      username = input("please enter your name:")
      userage= input("please ener your age:")
      exp=input("please enter how many experience you have:")
      skil["name"]=username
      skil["age"]=userage
      skil["experience"]=exp
      show_skills(skills)
      get_user_skills(skills)
      

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    get_user_cv(skills)


if __name__ == "__main__":
    main()

