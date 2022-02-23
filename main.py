def winner_check(GameBoard, size, turn):
	## Function which will check the board to see if there is  a  winner.
	## It will take "GameBoard" list and "size" variable as parameter also there is no need to check if the player 2 won the game after player 1 made the move and vice versa
	## hence, function will also take "turn" as parameter to skip unnecessary checks
	if turn == 1:												# checking if the "turn" is 1 if it is that means player 1 made a valid move and the function will check the board for "X"s
		check = "X";											# assigning "X" to "check" variable, this variable will be used in comparing operations
	else:														# else player 2 made the last move so function should look for "O" values		
		check = "O";											# assigning "O" to "check" variable, this variable will be used in comparing operations
	i = 0														# variable which will help searching the board assigning it to 0
	for x in range(size):										# loop which will search the columns, since theres only size amount of columns loop will iterate size times
		if(GameBoard[i::size] == [check]*size):					# checking if the the column has the same values with "check"
			return turn											# if the winning column exists returning "turn" value 
		i += 1													# increasing "i" with 1 since every column needs to be checked "i" will move to next element in every iteration
	i = 0														# reassigning 0 to "i" since it will be used while checking rows as well 
	for x in range(size):										# loop which will search the rows, since theres only size amount of rows loop will iterate size times
		if(GameBoard[i:i+size:1] == [check]*size):				# checking if the the row has the same values with "check"
			return turn											# if the row column exists returning "turn" value 
		i += size												# increasing "i" with size since every rows first element is "size" number apart from previous ones
	if(GameBoard[i::size+1] == [check]*size):					# checking for the diagonal winning condition starting from top left to bottom right
		return turn												# if it is in a winning position returning turn again
	if(GameBoard[size-1:-1:size-1] == [check]*size):			# checking for the diagonal winning condition starting from top right to bottom left
		return turn												# if it is in a winning position returning turn again

def Board_Print(GameBoard, size):
# function which will print the list in the desired form
	i = 0																	# variable which will be incremented while moving inside the list and will be used as the index
	for x in range(size):													# loop for rows
		for x in range(size):												# loop for elements in the rows
			if (i < 10) or (GameBoard[i] == "X") or (GameBoard[i] == "O"):	# pure aesthetic checking if the element needs to be printed is only 1 character
				print(" ",end='')											# if so printing white spaces accordingly
			print(GameBoard[i], end=' ')									# printing the element
			i += 1															# increasing "i" with 1 it will move to next element in the list
		print()																# printing end line for rows
	
size = int(input("What Size Game GoPy?"))									# asking for "size" input
GameBoard =[]																# creating the GameBoard list
turn = 1																	# assigning 1 to "turn" the variable which will either be 1 or 2 ( 1 for player 1 and 2 for player 2)
Max_number_of_turns = size*size												# creating a variable and assigning the size*size value which is the amount of locations in the table
Valid_turn_count = 0														# creating a variable which will count the number of valid turns

for x in range(size*size):													# loop which will iterate size*size creating a square board
	GameBoard.append(x)														# appending the x value in the loop to list
	
while (Valid_turn_count < Max_number_of_turns):								# loop which will iterate until valid_turn_count reaches max_number_of_turns
	Board_Print(GameBoard, size)											# first print of the board
	if(turn == 1):															# checking if the turn is 1 meaning that it is first players turn
		target = int(input("Player 1 turn--> "))							# print line as requested in pdf and assigning the input value to variable called "target"
		if((target < 0) or (target > size*size-1)):							# checking if the input is valid
			print(" Please enter a valid number")							# if not printing the error message
		elif(GameBoard[target] == "X"):										# checking if the location has "X" in it
			print("You have made this choice before")						# if so printing the requested line
		elif (GameBoard[target] == "O"):									# checking if the location has "O" in it
			print("The other player select this cell before")				# if so printing the requested line
		else:																# else part if the program enters this part it means that the target is empty
			GameBoard[target] = "X"											# updating the location
			Valid_turn_count += 1											# the move is valid hence the valid_turn_counter needs to be increased by 1
			if (winner_check(GameBoard, size, turn) == 1):					# checking board is at winning condition for player 1 using winner_check function
				Board_Print(GameBoard, size)								# calling Board_Print function if it is a winning condition requested in pdf
				print("Winner: X")											# printing the winner in the for given in pdf
				turn = 0													# changing "turn" to 0 which will be used if the loop has ended or braked after this line
				break														# break point since the game has ended and the loop does not need to iterate anymore 
		turn = 2															# changing turn to 2 if it is not a winning position 
	else:																	# else it is player 2's turn
		target = int(input("Player 2 turn--> "))							# print line as requested in pdf and assigning the input value to variable called "target"
		if((target < 0) or (target > size*size-1)):							# checking if the input is valid
			print(" Please enter a valid number")							# if not printing the error message
		elif(GameBoard[target] == "O"):										# checking if the location has "O" in it
			print("You have made this choice before")						# if so printing the requested line
		elif (GameBoard[target] == "X"):									# checking if the location has "O" in it
			print("The other player select this cell before")				# if so printing the requested line
		else:																# else part if the program enters this part it means that the target is empty
			GameBoard[target] = "O"											# updating the location
			Valid_turn_count += 1											# the move is valid hence the valid_turn_counter needs to be increased by 1
			if (winner_check(GameBoard, size, turn) == 2):					# checking board is at winning condition for player 2 using winner_check function
				Board_Print(GameBoard, size)								# calling Board_Print function if it is a winning condition requested in pdf
				print("Winner: O")											# printing the winner in the form given in pdf
				turn = 0													# changing "turn" to 0 which will be used if the loop has ended or braked after this line
				break														# break point since the game has ended and the loop does not need to iterate anymore 
		turn = 1															# changing turn to 1 if it is not a winning position 
if(turn != 0):																# checking if turn is not 0 meaning that the loop ended without reaching to break point also means that there is no winner
	print("no winner")														# print line for no winner condition