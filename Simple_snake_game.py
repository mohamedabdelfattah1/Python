import random
import curses

screen = curses.initscr()  # initiate the library and screen

curses.curs_set(0)   # hide the mouse

screen_height, screen_width = screen.getmaxyx()  # getting the size of the screen

window = curses.newwin(screen_height, screen_width, 0, 0)  # creating a window

window.keypad(1)  # Allowing receiving inputs 

window.timeout(100)  # Setting the speed of the window

snk_x = screen_width // 4
snk_y = screen_height // 2

# defining the snake body
snake = [
    [snk_y, snk_x],   #head
    [snk_y, snk_x - 1],  #body
    [snk_y, snk_x - 2]  #tail
]
# Creating the food of snake
food = [screen_height // 2, screen_width // 2]

# Adding the food to the snake by using PI character
window.addch(food[0], food[1], curses.ACS_PI) 

# Setting the initial movements to the right
key = curses.KEY_RIGHT

# Creating loop for the game
while True:
  next_key = window.getch()  # Getting the input from the user (next key)
  key = key if next_key == -1 else next_key
  # if next_key == -1:
  #   key = key
  # else:
  #   key = next_key  # Checkig if the user doesn't press anything
  
# Checking if the snake collided with the walls or itself
  if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:

# Ending this game  ---
    curses.endwin()
    quit() #Exit

# Setting the new pos. of the head of snake
  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_DOWN:
    new_head[0] += 1   #pressing down arrow
  
  elif key == curses.KEY_UP:
    new_head[0] -= 1   #pressing up arrow
    
  elif key == curses.KEY_RIGHT:
    new_head[1] += 1   #pressing right arrow
    
  elif key == curses.KEY_LEFT:
    new_head[1] -= 1   #pressing left arrow
    
  snake.insert(0, new_head)  #inserting new head to the postiion of snake list
  
# Checking if the snake ate the food or not
  if snake[0] == food:
    food = None  # Removing food if it eat
    # score += 1   # Incrementing the score
    while food is None:
      # Generating new food by random lib
      new_food = [
          random.randint(1, screen_height - 1),
          random.randint(1, screen_width - 1)
      ]
      food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_PI) 
  else: 
    tail = snake.pop()     # Deleting the last seg. of the body
    window.addch(tail[0], tail[1], ' ')

  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD) # Adding


  



