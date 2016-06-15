from graphics import *
import time
import random


def drawBlanks(win, xcoord, ycoord):
  l1blanks = Text(Point(xcoord, ycoord), "___ ")
  l1blanks.setTextColor("black")
  l1blanks.setSize(17)
  l1blanks.draw(win)
  return

def unDrawBlanks(win, xcoord, ycoord):
  l1blanks = Text(Point(xcoord, ycoord), "___ ")
  l1blanks.setTextColor("black")
  l1blanks.setSize(17)
  l1blanks.draw(win)
  return

'''
The welcome screen is drawn
'''
def drawWelcomeScreen(win):
  # Create the game title.
  welcome1 = Text(Point(200, 400), "Welcome")
  welcome1.setTextColor("cyan")
  welcome1.setSize(12)
  welcome1.draw(win)

  welcome2 = Text(Point(230, 400), "to")
  welcome2.setTextColor("yellow")
  welcome2.setSize(12)
  welcome2.draw(win)

  welcome3 = Text(Point(260, 400), "Wynna's")
  welcome3.setTextColor("purple1")
  welcome3.setSize(12)
  welcome3.draw(win)

  welcome4 = Text(Point(300, 400), "Game")
  welcome4.setTextColor("maroon")
  welcome4.setSize(12)
  welcome4.draw(win)

  # TextBox to go to next screen
  click1 = Text(Point(250, 50), "Click to begin")
  click1.setTextColor("white")
  click1.draw(win)

  # Animate the title.
  # TODO: Make it non-blocking
  while True:
    
    if win.checkMouse() != None:
      break
    time.sleep(1)
    welcome1.move(50, -100)
    welcome2.move(55, -100)
    welcome3.move(60, -100)
    welcome4.move(65, -100)
    if win.checkMouse() != None:
      break
    time.sleep(1)
    welcome1.move(-50, -100)
    welcome2.move(-55, -100)
    welcome3.move(-60, -100)
    welcome4.move(-65, -100)
    if win.checkMouse() != None:
      break
    time.sleep(1)
    welcome1.move(30, 100)
    welcome2.move(35, 100)
    welcome3.move(40, 100)
    welcome4.move(45, 100)
    # Add another phrase going up


  # Go to the next screen
  welcome1.undraw()
  welcome2.undraw()
  welcome3.undraw()
  welcome4.undraw()
  click1.undraw()

  return

'''
The rules/procedures of the game will be shown to the player
'''
def drawProceduresScreen(win):
  win.setBackground("blue")

  procedures = Text(Point(250,450),"Game Procedures")
  procedures.setTextColor("yellow1")
  procedures.setSize(25)
  procedures.draw(win)

  rule1 = Text(Point(175,400), "1. Guess the letters that go in the given blanks")
  rule1.setTextColor("pink3")
  rule1.setSize(15)
  rule1.draw(win)

  rule2 = Text(Point(220,350), "2. If the letter is wrong, then a part of the figure will be drawn.")
  rule2.setTextColor("green")
  rule2.setSize(15)
  rule2.draw(win)

  rule3 = Text(Point(260, 300), "3. If you guess the word before the entire figure is drawn, then you pass.")
  rule3.setTextColor("purple")
  rule3.setSize(15)
  rule3.draw(win)

  
  rule4 = Text(Point(130, 250), "4. If not, then you have to restart.")
  rule4.setTextColor("maroon")
  rule4.setSize(15)
  rule4.draw(win)

  rule5 = Text(Point(60,200), "5. Have fun!")
  rule5.setTextColor("cyan")
  rule5.setSize(15)
  rule5.draw(win)

  click2 = Text(Point(250,50), "Click to move on")
  click2.setTextColor("white")
  click2.draw(win)

  win.getMouse()

  procedures.undraw()
  rule1.undraw()
  rule2.undraw()
  rule3.undraw()
  rule4.undraw()
  rule5.undraw()
  click2.undraw()

  return


'''
Displays the three levels and the player can choose which level to start off with. 
'''
def drawPickLevelScreen(win):
  win.setBackground("black")
  level_1 = Text(Point(250, 450), "LEVEL")
  level_1.setTextColor("purple")
  level_1.setSize(30)
  level_1.draw(win)
  level_1A = Text(Point(285, 450), "     1")
  level_1A.setTextColor("orange")
  level_1A.setSize(30)
  level_1A.draw(win)
  level_1B = Text(Point(250, 400), ' Type "e" for easy level')
  level_1B.setTextColor("pink")
  level_1B.setSize(20)
  level_1B.draw(win)

  level_2 = Text(Point(250, 350), "LEVEL")
  level_2.setTextColor("cyan")
  level_2.setSize(30)
  level_2.draw(win)
  level_2A = Text(Point(290, 350), "     2")
  level_2A.setTextColor("white")
  level_2A.setSize(30)
  level_2A.draw(win)
  level_2B = Text(Point(250, 300), ' Type "m" for medium level')
  level_2B.setTextColor("green")
  level_2B.setSize(20)
  level_2B.draw(win)

  level_3 = Text(Point(250, 250), "LEVEL")
  level_3.setTextColor("red")
  level_3.setSize(30)
  level_3.draw(win)
  level_3A = Text(Point(285, 250), "      3")
  level_3A.setTextColor("maroon")
  level_3A.setSize(30)
  level_3A.draw(win)
  level_3B = Text(Point(250, 200), ' Type "h" for hard level')
  level_3B.setTextColor("blue1")
  level_3B.setSize(20)
  level_3B.draw(win)

  while True:
    level_choice = win.getKey()
    if level_choice == "e" or level_choice == "E" or level_choice == "m" or level_choice == "M" or level_choice == "h" or level_choice == "H":
      level_1.undraw()
      level_1A.undraw()
      level_1B.undraw()
      level_2.undraw()
      level_2A.undraw()
      level_2B.undraw()
      level_3.undraw()
      level_3A.undraw()
      level_3B.undraw()
      return level_choice
    else:
      #Add a line that says "please enter e, m, or h"
      time.sleep(1)
    
'''
'''
def processNextUserInput(win, entry_box, next_word, incorrect_guesses, blank_positions, y_coordinate, guessed_letters, wrong_letter_positions):
    global list_easy_words
    alphabet = win.getKey()
    print (alphabet)
    if len(alphabet) > 0:
        print (alphabet)
        # Check for repeating letters
        if guessed_letters[alphabet] == 1:
          warning = Text(Point(100, 50), alphabet + " was already picked.")
          warning.setTextColor("red")
          warning.setSize(17)
          warning.draw(win)
          time.sleep(1)
          warning.undraw()
          return -1
        
        guessed_letters[alphabet] = 1
        num_matches = 0
        if alphabet in next_word:
            for i in range(len(next_word)):
                if alphabet == next_word[i]:
                    matching_index = i
                    num_matches = num_matches + 1
                    x = Text(Point(blank_positions[matching_index], y_coordinate+10), alphabet)
                    x.setTextColor("green")
                    x.draw(win)
            return num_matches 
        else:
            # Letter not in word
            # Put letter in box
      
            alphabet = Text(Point(wrong_letter_positions[incorrect_guesses], 430), alphabet)
            alphabet.setTextColor("black")
            alphabet.draw(win)
            # Draw hangman part. Draw different things at different incorrect guesses

            if incorrect_guesses == 0:
              head = Circle(Point(150,400), 30)
              head.draw(win)
            elif incorrect_guesses == 1:
              # Draw body
              body = Line(Point(150, 370), Point(150, 290))
              body.draw(win)
            elif incorrect_guesses == 2:
              right_arm = Line(Point(150, 350), Point(170, 310))
              right_arm.draw(win)
            elif incorrect_guesses == 3:
              left_arm = Line(Point(150, 350), Point(130, 310))
              left_arm.draw(win)
            elif incorrect_guesses == 4:
              right_leg = Line(Point(150, 290), Point (170, 230))
              right_leg.draw(win)
            else:
              left_leg = Line(Point(150, 290), Point (120,230))
              left_leg.draw(win)
            
            return 0
    return -1

def InitializeGuessedLetters(guessed_letters):
  alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for i in range(len(alphabet_array)):
    guessed_letters[alphabet_array[i]] = 0

'''
Displays the background and sets up level 
'''
def drawLevelScreen(win, level):
  win.setBackground("white")

  level1 = Text(Point(50, 450), "Level " + str(level))
  level1.setTextColor("green")
  level1.setSize(20)
  level1.draw(win)

  l1wordbox = Rectangle(Point(300, 400), Point(500, 450))
  l1wordbox.draw(win)


  l1wrongwords = Text(Point(350, 475), "Wrong Letters: ")
  l1wrongwords.setTextColor("cyan")
  l1wrongwords.setSize(15)
  l1wrongwords.draw(win)
  
  blank_positions = (200, 240, 280, 320)
  wrong_letter_positions = (320, 330, 340, 350, 360, 370)
  y_coordinate = 150
  for i in range(4):
    drawBlanks(win, blank_positions[i], y_coordinate)
  
  entry_box = Entry(Point(100, 100), 20)
  alphabet1 = Text(Point(250, 50), "a b c d e f g h i j k l m")
  alphabet2 = Text(Point(250, 30), "n o p q r s t u v w x y z")
  #entry_box.draw(win)
  alphabet1.draw(win)
  alphabet2.draw(win)

  list_easy_words = ['make', 'jump', 'dogs', "fall", "leaf", "bowl", "food", "milk", "card", "made"]

  random.seed()
  next_word_index = random.randint(0, len(list_easy_words)-1)
  next_word = list_easy_words[next_word_index]
  print (next_word)
  
  correct_guesses = 0
  incorrect_guesses = 0

  guessed_letters = {}
  InitializeGuessedLetters(guessed_letters)
  
  while(correct_guesses < 4 and incorrect_guesses < 6):
    y = processNextUserInput(win, entry_box, next_word, incorrect_guesses, blank_positions, y_coordinate, guessed_letters, wrong_letter_positions)
    if y == 0:
      # Incorrect guess
      incorrect_guesses = incorrect_guesses + 1
    elif y >= 1:
      # Correct guess
      correct_guesses = correct_guesses + y
    else:
      print("No input")
  if correct_guesses == 4:
    level1.undraw()
    l1wordbox.undraw()
    l1wrongwords.undraw()
    #unDrawBlanks.undraw()
    entry_box.undraw()
    alphabet1.undraw()
    alphabet2.undraw()
    #next_word_index.undraw()
    win.setBackground("black")
    you = Text(Point (200, 450), "YOU   ")
    you.setSize(30)
    you.setTextColor("white")
    you.draw(win)
    won = Text(Point (280, 450), "WON!!!")
    won.setSize(30)
    won.setTextColor("cyan")
    won.draw(win)
    image1 = Image(Point(250, 250), "you_won_screen.gif")
    image1.draw(win)
    
    # Draw "You won" screen 
  elif incorrect_guesses == 6:
    level1.undraw()
    l1wordbox.undraw()
    l1wrongwords.undraw()
    entry_box.undraw()
    alphabet1.undraw()
    alphabet2.undraw()
    '''head.undraw()
    body.undraw()
    right_arm.undraw()
    left_arm.undraw()
    left_leg.undraw()'''
    you2 = Text(Point (200, 450), "YOU ")
    you2.setSize(30)
    you2.setTextColor("maroon")
    you2.draw(win)
    lost = Text(Point (285, 450), "LOST!!!")
    lost.setSize(30)
    lost.setTextColor("red")
    lost.draw(win)
    
    image2 = Image(Point(250, 250), "you_lost_screen.gif")
    image2.draw(win)
    
    #next_word_index.undraw()
    win.setBackground("black")
    # Draw "Try again" screen
  return

def main():
  win = GraphWin("Magic Project", 500, 500)
  win.setBackground("black")
  win.setCoords(0, 0, 500, 500)
  drawWelcomeScreen(win)
  drawProceduresScreen(win)
  user_choice = drawPickLevelScreen(win)
  if user_choice == "e" or user_choice == "E":
    drawLevelScreen(win, 1)
  elif user_choice == "m" or user_choice == "M":
    drawLevelScreen(win, 2)
  elif user_choice == "h" or user_choice == "H":
    drawLevelScreen(win, 3)
  else:
    print ("Invalid choice")
  
  win.getMouse()
  win.close()

main()
