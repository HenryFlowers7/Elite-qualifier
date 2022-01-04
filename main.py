import random

def generate_response(user_input):
  responses = [
    "That's wonderful to hear!",
    "wow that's awesome i guess",
    "wow!",
    "sounds pretty amazing!",
    "oh wow, that's nice",
    "i don't think i asked for all that",
    "Feel free to stop talking",
    "Im not that interested anymore",
    "why are you still here?",
    "you want to see me care?....you want to see me do it again?",
  ]
  return random.choice(choices)

  #what i was trying to do was as it goes on and you keep talking the chatbot eventually grows very tired of all your talking and it starts to grow bored, but unfortunately i didn't really know any sort of coding that allows me to go in order

def init_chat():
  quit_character = 'q'

  user_input = input("hello how are you?")

  while user_input != quit_character:
    user_input = input(generate_response)

#this is as far as i went, it wouldn't generate the greeting.

