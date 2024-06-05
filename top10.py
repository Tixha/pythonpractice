guesses = []
BIGGEST_STARS_ANSWER = ["UY SCUTI", "WOH G64", "WOH 5170", "RSGC1-F01", "HD 269551", "VY CANIS MAJORIS","HD 1463", "CM VELORUM", "AH SCORPIO", "HV 888"]
 # ------ FUNCTIONS --------

# Welcomes the user and introduces the quiz
def intro():
  # Ask the user their name 
  name = input("What is your name?")

# Greet the user
  print("Hello", name, "Welcome to the quiz")
  print("This quiz is about the top 10 largest stars in the universe? Can you name them all?")

# Ask the user how many attempts they want at each question
def getlives():
  while True:
    lives = input("How many chances do you want?")
    try:
      lives = int(lives)
      if lives >= 0:
        return lives
      else:
        print("Please enter a number greater than 0")
    except:
        print("Please enter a number")
# ------- MAIN CODE-------

intro() 