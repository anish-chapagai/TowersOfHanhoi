from stack import Stack
print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3:\n"))
temp_num = num_disks  
for i in range(1,num_disks+1):
  print("Pushed")
  left_stack.push(temp_num)
  temp_num -= 1

stacks[0].print_items()

#Calculate Optimal Moves
num_optimal_moves = 2**(num_disks)-1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

#Get User Input
def get_input():
  choices = [i.get_name()[0] for i in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter, name))
    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if choices[i] == user_input:
          return stacks[i]
          
        
#Play the Game
num_user_moves = 0
while right_stack.size != num_disks:
  print(num_disks)
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  moved_stat = False
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.is_empty() == True:    #Stack is empty
      print("\n\nInvalid Move. Cannot move from empty Stack. Try Again")
    elif to_stack.peek() < from_stack.peek():  #cannot move from hight to lower
      print("Invalid Move. Cannot move to smaller disk. Try again")
    else:
      to_stack.push(from_stack.pop())
      num_user_moves += 1
      print("Moved from {} to {}".format(from_stack.get_name(), to_stack.get_name()))
      break

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves, num_optimal_moves))