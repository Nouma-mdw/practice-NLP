# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
    "Why are you here? ",
    "Are there many humans like you? ",
    "What do you consume for sustenance? ",
    "Is there intelligent life on this planet? ",
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet? "
  )
  # defining instance varialbes
  def __init__(self):
    self.alienbabble = {
      'describe_planet_intent': r'.*(how|tell.*about|interest.*in).*your.*planet',
      'answer_why_intent': r'why are you.*(here|asking me?\s?so?\s?many questions)\??',
      'cubed_intent': r'can.*you.*cube.*number (\d+)?',
      'alien_interest_intent': r'what.*about.*you\??'
      }
  
    # Define .greet() below:
  def greet(self):
    self.name =  input("Hello stranger, what is your name? ").lower()

    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about this planet? ").lower()

    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return

    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a nice day!")
        return True
    # return False

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply)).lower()


  # Define .match_reply() below:
  def match_reply(self, reply):
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply)
    # the task expects the if-elif-else conditions under the for loop. 
    # But in that case the for loop will iterate only once:
    # if it matches the first pattern, that will be the output.
    # Otherwise the else condition applies, and this will break the loop. That is why I change the code a bit
      if found_match:
        break
    if found_match and intent == 'describe_planet_intent':
      return self.describe_planet_intent()
    elif found_match and intent == 'answer_why_intent':
      return self.answer_why_intent()
    elif found_match and intent == 'cubed_intent':
      return self.cubed_intent(found_match.groups()[0])
    elif found_match and intent == 'alien_interest_intent':
      return self.alien_interest_intent()
    else:
      return self.no_match_intent()


  # defining methods for the intents

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = (r'My planet is a utopia of diverse organisms and species.', r'I am from Opidipus, the capital of the Wayward Galaxies.')
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = (r'I come in peace.', r'I am here to collect data on your planet and its inhabitants.', r'I heard the coffee is good.')
    return random.choice(responses)

       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    print(number)
    number = int(number)
    return f"The cube of {number} is {number**3}. Isn't that cool?"

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = ("Please, tell me more. ", "Tell me more! ", "Why do you say that? ", "I see. Can you elaborate? ", "Interesting. Can you tell me more? ", "I see. How do you think?", "Why? ", "How do you think I fell when you say that? ")
    return random.choice(responses)

  def alien_interest_intent(self):
    responses = ("I don't like talking about myself", "I'd like to keep that to me.", "Sorry, you are asking for too much information.")
    return random.choice(responses)


# Create an instance of AlienBot below:
Alienbot = AlienBot()

Alienbot.greet()
