import time
#This allows the use of the time module.
#import random
#This allows the use of the random module.
import climage
#This allows the use of the image module.
text = "normal"
#This is here so the other modes in the settings menu can take effect.
cheats = "false"
#This is here so the cheats setting can take effect.
print(climage.convert('lemon.jpg', is_unicode=True))
print("Loading...")
time.sleep(10)
gamelist = ["1) Settings", "2) Play", "3) Credits"]
print(climage.convert('titlescreen.jpg', is_unicode=True))
game = int(input(gamelist))
while game != 2:
  while game == 1:
    setlist = ["1) Samuel Mode (Displays the word 'Jack' in different text fonts)", "2) Play Normally", "3) Cheats", "4) Cat Mode (Everything is related to cats)", "5) Credits"]
    print("What do you want to do?")
    set = int(input(setlist))
    while set == 1:
      print("Activating Samuel Mode...")
      text = "sam"
      time.sleep(3)
      set = 2
    while set == 2:
      game = 2
    while set == 3:
      print("Activating Cheats...")
      cheats = "true"
      time.sleep(3)
      game = 2
      break
    while set == 4:
      print("Activating Cat Mode...")
      text = "cat"
      time.sleep(3)
      set = 2
    while set == 5:
      game == 3
    while set <= 0:
      set = int(input("Not an option. "))
    while set >= 6:
      set = int(input("Not an option. "))
  while game == 3:
    print("Made by JiovanniJr")
    time.sleep(3)
    print("This game is heavily inspired by The Stanley Parable: Ultra Deluxe!")
    time.sleep(5)
    print("Please go play their game as well if you can or support their developers <3")
    time.sleep(5)
    print("What do you want to do?")
    game = int(input("1) Settings 2) Play"))
if cheats == "true":
  quit("Placeholder... oh and congrats for getting the CHEATER!!! Ending.")
#The beginning of the game is our narrative.
if text == "normal":
  print("This begins our story of an expert programmer named Jack. Jack is a senior at Electrc High Scool who is currently taking a computer science class in room E131.")
elif text == "sam":
  print("JACK")
elif text == "cat":
  print("This begins our story of an expert cat lover named Jack. Jack is a senior at Electrc High Scool who is currently taking an animal science class in room E131.")
time.sleep(5)
#These time.sleep functions help feel the player that someone is actually narrating and also can have time to read the text
print("Jack and his neighboring classmates adore everything about computer science. Even if the subject is hard or complicated, they will always try their best.")
time.sleep(5)
print("However, on this tuesday he was walking to school, the weather was bright and sunny, and none of his teachers talked about a day off of school.")
time.sleep(5)
print("Jack walked into his classroom and nobody was there, no one at all. Jack wondered if he had missed something that nobody notified him for, then he had the right to blame his teacher.")
time.sleep(5)
print("Now that Jack has nothing to do, he decides to leave the room and simply head back to his house.")
time.sleep(3)
#Our options will be in lists.
optlist = ["1) Wander around", "2) Touch everything", "3) Leave the room", "4) Stay and do nothing"]
print(optlist)
#The options will be printed and the user makes a choice which will be stored in the opt variable.
opt = int(input("Type a number "))
while opt != 3:
  #These are the choices' outcomes, they are in a while loop so the user can experience the incorrect options and can only activate if the user picks the numbers between 1 and 4.
  while opt <= 0:
    #If they fail to follow simple instructions, such as typing a number less or equal than 0, and the same thing down below with 5 or greater than, this will print, telling you that wasn't an option. You are prompted to try again.
    print("That isn't an option, try again.")
    print("1) Wander around, 2) Touch everything, 3) Leave the room, 4) Stay and do nothing.")
    opt = int(input(""))
    #This input is placed here so the user has a way to get out of the while loop by typing a different number.
  while opt == 1:
    print("Jack begins to wander around the room, trying to look for his missing classmates and the missing instructor, every room, every corner, there seems to be nobody there.")
    time.sleep(4)
    print("2) Touch everything, 3) Leave the room, 4) Stay and do nothing")
    opt = int(input(""))
  while opt == 2:
    print("Jack thought to himself 'What if I touch everything? There could be some secret room I don't know about. Maybe they're hiding in the secret room and they want me to find it.'")
    time.sleep(5)
    print("And Jack did just that. He touched everything in the room, hoping for some secret room to appear. Frankly, I found this a bit dumb on his choices he made.")
    time.sleep(5)
    print("But who do I care? It's just my simple story and he chose to do... whatever he did. Anyways obviously nothing happened and now he looked dumb.")
    time.sleep(4)
    print("1) Wander around, 3) Leave the room, 4) Stay and do nothing")
    opt = int(input(""))
  while opt == 4:
    print("Yep. The thought of him going home was so bizarre, that he stood frozen right in that exact position.")
    time.sleep(7)
    print("However, one could argue that standing in the same spot will have absolutely no effect of bringing people back, and personally, I agree.")
    time.sleep(4)
    print("1) Wander around, 2) Touch everything, 3) Leave the room")
    opt = int(input(""))
  while opt >= 5:
    print("That isn't an option, try again.")
    print("1) Wander around, 2) Touch everything, 3) Leave the room, 4) Stay and do nothing.")
    opt = int(input(""))
print("test")