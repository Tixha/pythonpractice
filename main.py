import random 

QUESTION_FORMAT = "{}\ nA. {}\ nB. {}\ nC. {}\ nD. {}\ n"
GOOD_COMMENTS = ["Good job!", "Nice!", "Well done!"]
BAD_COMMENTS = ["Wrong!", "Incorrect!", "Try again"]
QUESTIONS = ["What is the capital of Italy?", 
             "What is the capital of the USA?",    
             "What is the capital of the Philippines?", 
             "What is the capital of Spain?", "What is the capital of Russia?"] 
OPTIONS = [["Florence", "Venice", "Rome", "Milan"]
          ["Washington DC", "New York", "Los Angeles", "Chicago"] 
          ["Quezon City", "Davao City", "Cebu City", "Manila"]
          ["Barcelona", "Valencia", "Madrid", "Seville"]
          ["St.Petersburg", "Moscow", "Kazan", "Samara"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
score = 0
play = "yes"

# Ask the user their name
name = input("What is your name?")

# Greet the user
print("Hello", name, "Welcome to the quiz")

# Check number of question attempts
while True:
  try:
    tries = input ("How many attempts do you want at each question? 1-3")
    tries = int(tries)
    break
  except:
    print("Enter a number please")
# Start the quiz
while play == "yes":

  question_attempts = tries
  while question_attempts > 0:
   # Ask the user a question
    question = "What is the capital of Italy?"
    a = "Florence"
    b = "Venice"
    c = "Rome"
    d = "Milan"
    answer = input("{}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(question, a, b, c, d)).lower()
    # Check user's answer
    if answer == c or answer == "c":
      print("Correct")
      score += 5
      break
    elif answer == "":
      print("please enter a answer")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d:
      print("Please enter a valid answer")
    else:
      print("Incorrect")
    question_attempts -= 1
    print("The answer is Rome")
    question = input("What is the capital of USA?")
      a = "Washington DC"
      b = "New York"
      c = "Los Angeles"
      d = "Chicago"
      answer = input("{}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(question, a, b, c, d)).lower()
      # Check the user's answer
      if answer == a or answer == "a":
        print("Good job!")
      elif answer =="":
        print("No answer?")
      else:
        print("Try again")
      # Ask the user a question
      question = input("What is the capital of the Philippines?")
      a = "Quezon City"
      b = "Davao City"
      c = "Cebu City"
      d = "Manila"
      answer = input("{}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(question, a, b, c, d)).lower()
      #Check the user's answer
      if answer == c or answer == "c":
        print("Correct!")
        score += 5
      elif answer == "":
        print("No answer?")
      else:
        print("That's not the answer")
        print(BAD_COMMENTS[0])
      # Ask the user a question
      question = input("What is the capital of Spain?") .lower()
      a = "Barcelona"
      b = "Valencia"
      c = "Madrid"
      d = "Seville"
      answer = input("{}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(question, a, b, c, d)).lower()
      # Check the user's answer
      if answer == c or answer == "c":
        print("Correct!") 
        score += 5
      elif answer == "":
        print("No answer?")
      else:
        print("That's not the answer")
        print(GOOD_COMMENTS[2])
      # Ask the user a question 
      question = "What is the capital of Russia?"
      a = "St. Petersburg"
      b = "Moscow" 
      c = "Kazan"
      d = "Samara"
      answer = input("{}\nA.{} B.{} C.{} D.{}\n" .format(question, a, b, c, d)) .lower()
      # Check the user's answer
      if answer == b or answer == "b":
        print("Correct!")
        score += 5
      elif answer == "":
        print("Not sure?")
      else:
        print("Wrong!, the answer is b")
  # End the quiz
  print("Well done! {} your score is {}" .format(name, score))
  # Replay
  play = input("Would you like to play again?").lower()