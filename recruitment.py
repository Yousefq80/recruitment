skills = ["Python", "C++", "Javascript", "Juggling", "Running", "Eating"]
cv= {}
def get_skills():
    skills = ["Python", "C++", "Javascript", "Juggling", "Running", "Eating"]
    return skills




# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for x, element in enumerate(skills):
     print(str(x+1)+"-",element)



# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
  userskill=[] 
  n =len(skills)  
  usk1=int(input("please choose a skill by entring number form the list:"))
  usk2=int(input("please choose another skill by entring number form the list:"))
  for x in range(n):
        
    if (x+1) == usk1:
      userskill.append(skills[x])
    if (x+1) == usk2:
      userskill.append(skills[x])
        # else:
        #     usk2=int("you have selected this number before please enter another number")
  return userskill
    

# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
      cv= {}
      
      cv["name"] = input("please enter your name:")
      cv["age"]= input("please enter your age:")
      exp=int(input("please enter how many yesrs of experience you have:"))
      cv["experience"]=exp 
      show_skills(skills)
      cv["skills"]=[]
       
      cv["skills"].append(get_user_skills(skills))
      # print(cv) 
      return cv
# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
  # c={}
  # c.update(get_user_cv(skills))
  # print(c)
   
   age=int(cv["age"])
   if age>=20  and cv.get("experience") > 2 and desired_skill not in cv["skills"]:
    return True
   else:
    return False
  


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the recruitment program, please answer the following questions:")
    # ch=check_acceptance(cv,"Python")
    # if ch == True:
    #   print(f"you have been accepted")
    # else:
    #   print("You have been rejected")
    
    c={}
    c.update(get_user_cv(skills))
    ch = check_acceptance(c, "Python")
    name=c["name"]
   
    if ch:
        print(f"You have been accepted:",name)
    else:
        print(f"You have been rejected:",name)
    #print(f"you have been accepted,{cv.get("name")")
    
if __name__ == "__main__":
    main()
