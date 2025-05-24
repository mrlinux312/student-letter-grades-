print("Student Grading Data")
def grade(scale):
    #Grading scale
      if scale >= 90:
        return "A"
      elif scale >= 80:
        return "B"
      elif scale >= 70:
        return "C"
      elif scale >= 60:
        return "D"
      elif scale < 60:
        return "F"

def main():
    run_pro = input("Would you like to start the Grading program? y/n: ").lower()
    if run_pro != "y":
        return

    low = 100
    high = 0
    total = 0
    user_ct = 0
    #User enters last name and grade in numerical form
    while True:
      try:  
       lastname = input("Please enter last name of student:")

       scale = int(input("Please enter score on scale from 0-100:  "))
       if 0 < scale > 100:
           print("This score is out of range. Score must be between 0-100.")
           cont_pro = input("Would you like to proceed with program? y/n?: ").lower()
           if cont_pro != "y":
                break
           if cont_pro == "y":
              lastname = input("Please enter last name of student:")

              scale = int(input("Please enter score on scale from 0-100:  "))
      except ValueError:
           print("This is not a number. Enter number between 0-100.")
           cont_pro = input("Would you like to proceed with program? y/n?: ").lower()
           
           if cont_pro != "y":
                break
           if cont_pro == "y":
              lastname = input("Please enter last name of student:")

              scale = int(input("Please enter score on scale from 0-100:  "))
      letter_grade = grade(scale)

      if scale < low:
             low = scale
      if scale > high:
            high = scale
      user_ct += 1
      total += scale
      avg = total / user_ct


      print(f"Last name: {lastname}, Grade: {letter_grade}")
      print(f"Highest Score: {high}")
      print(f"Lowest Score: {low}")
      print(f"Average Score: {avg}")
      another_stu = input("Would you like to enter another student? y/n?: ")
      if another_stu != "y":
         break
if __name__ == "__main__":
  main()