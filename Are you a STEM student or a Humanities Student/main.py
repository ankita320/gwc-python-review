questions = ["""If you miraculously received a free period from the gods, what would you do during those precious 41 minutes?
A. Sleep
B. Study
C. Debate over what to do before realizing the period has passed
D. Nothing""", 
"""How do you typically feel on Sunday nights?
A. Meh
B. Fatigued
C. Wait -- tomorrow's monday?!
D. I have lost track of time"""]

# print(questions)
score = 0
user_responses = []

# 
def count_most_frequent_response(arr):
  return max(set(arr), key = arr.count)

def convert_result(letter):
  if letter == "A":
    return "the Prodigy"
  elif letter == "B":
    return "the Workaholic"
  elif letter == "C":
    return "the stressed, life-contemplating Stuy student"
  else:
    return "the Confused One"

def run():
  print("Welcome to 'Which Stuy Student Archetype Are You'!\nPress enter to continue")
  input()

  for i in range(len(questions)):
    user_response = input(questions[i] + "\n")
    if user_response != "A" and user_response == "B" and user_response != "C" and user_response != "D":
      user_response = input(questions[i])
    user_responses.append(user_response)
    
  most_similar = count_most_frequent_response(user_responses)
  
  print(f"You are most similar to {convert_result(most_similar)}. Are you doing ok?")


# executing the main function
run()
