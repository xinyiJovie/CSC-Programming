import random


#intro
print('\tx----------------------------------x')
print('\t|\tWelcome to Master Mind game.   |')
print('\tx----------------------------------x')

#possible shapes to choose
def shapes(*shape_intro):
  print('\n\t-------------------------------')
  print('\t\t\tHow to play?')
  print('\t-------------------------------')
  print("\n\t\tHere's a list of shapes to choose:")
  for x in shape_intro:
    print(f"\t\t\t{x}")
shapes('Star--------------(S)', 'Circle------------(C)', 'Pentagon----------(P)', 'Triangle----------(T)', 'Rectangle---------(R)', 'Ginger breadman---(G)')


#instructions
def instructions():
  print('\nYou have to guess the secret shapes and their correct position to win the game.')
  print('x--NOTE: Shapes can be repeated.--x')
  start = input('\nAre you ready for the game? (y/n): ')
  if start.lower() == 'y':
    print('\nx------------------------------------------------------------------------------x')
    print('\t------------------------------')
    print('\t\t\tStart Game!')
    print('\t------------------------------')
  else:
    print("Aw, that's a shame :p, see you next time then!")
    exit()
instructions()


#provide random shapes
def provide_shape():
  print("\nGuess four shapes that I have in mind:")
  print('--sample answer: S--')
  print("Enter 'q' at anytime to quit the game\n")
  shape_list = ['C', 'R', 'T', 'S', 'G', 'P']
  comp_shapes = random.choices(shape_list, k=4)
  return comp_shapes


#start the game
def game(shape_list, comp_shapes):
  attempt = 0
  game = True
  while game:
    attempt += 1
    #user's guess
    user_guess = []
    for count in range(1, 5):
      guess = input(f"Enter shape {count}: ")
      if guess == 'q':
        exit(game)
      user_guess.append(guess.upper())
    print(user_guess)
      

    #checking validation
    for b in user_guess:
    # 1 check if the user is entering four shapes
      if b == '':
        print('\nHEY MAN! Please enter four shapes!')
        break
        
    # 2 check if the user is entering the correct shapes provided    
      if b not in shape_list:
        print('\nHEY MAN! Please enter only the shapes provided!')
        break     

      
    #match the shapes and positions
    count1 = 0
    count2 = 0
    #create a copied version so it can be modified 
    copy_comp_shapes = comp_shapes[:]
    #check the shapes are correct and in correct place
    for i in range(4):
      if user_guess[i] == copy_comp_shapes[i]:
        count1 += 1
        copy_comp_shapes[i] = 'X' 
        user_guess[i] = 'O'
          
    #check the shapes that are correct but in the wrong place    
    for i in range (4):
      for j in range(4):
        if user_guess[i] == copy_comp_shapes[j]:
          count2 += 1
             
    print(f'\nCorrect shape and position!- {count1}')
    print(f'Correct shape but wrong position!- {count2}')

    
    #display results
    if count1 == 4:
      print('\nWell done! You win the game!')
      print(f'You took {attempt} attempt(s)!')
      #continue playing or no
      prompt = input('\nDo you want to continue the game?(y/n): ')
      if prompt.lower() == 'y':
        attempt = 0
        comp_shapes = random.choices(shape_list, k=4)
        print("\nOK, let's play again!")
        provide_shape()
        print(comp_shapes)
        continue
        
      else:
        print('\nOK, goodbye! :)')
        break
        
    #let user try again
    elif count1 != 4:
      print('\nTry again:')
      continue

      
shape_list = ['C', 'R', 'T', 'S', 'G', 'P']
comp_shapes = provide_shape()
print(comp_shapes)
game(shape_list, comp_shapes)