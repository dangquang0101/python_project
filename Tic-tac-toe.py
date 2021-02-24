import random, time
print(
	'########  ##  ########        ########     ##      ########        ########  ########  ########\n'+
	'   ##     ##  ##                 ##       ####     ##                 ##     ##    ##  ##      \n'+
	'   ##     ##  ##        ####     ##      ##  ##    ##        ####     ##     ##    ##  ########\n'+
	'   ##     ##  ##                 ##     ########   ##                 ##     ##    ##  ##      \n'+
	'   ##     ##  ########           ##    ##      ##  ########           ##     ########  ########'
	)
time.sleep(1)
rule=(
	'Here there are all nine numbered boxes as shown below.\n'+
	'                     1 | 2 | 3 \n'+
	'                    -----------\n'+
	'                     4 | 5 | 6 \n'+
	'                    -----------\n'+
	'                     7 | 8 | 9 \n'+
	'Keep in mind the order of the cells as you will need to enter them later.'
	)
print(rule)
time.sleep(1)

def per():
	global a1, a2, a3, a4, a5, a6, a7, a8, a9
	player = input('Enter the location of your choice: ')
	while player != '1' and player != '2' and player != '3' and player != '4' and player != '5' and player != '6' and player != '7' and player != '8' and player != '9':
		player = input('Please select positions 1 through 9: ')
	if player == '1':
		if a1==' ':a1='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '2':
		if a2==' ':a2='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9; ');per()
	elif player == '3':
		if a3==' ':a3='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '4':
		if a4==' ':a4='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '5':
		if a5==' ':a5='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '6':
		if a6==' ':a6='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '7':
		if a7==' ':a7='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	elif player == '8':
		if a8==' ':a8='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()
	else:
		if a9==' ':a9='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per()	
def com():
	global a1, a2, a3, a4, a5, a6, a7, a8, a9
	c=str(random.randint(1,9))
	if c=='1':
		if a1==' ':a1='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='2':
		if a2==' ':a2='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='3':
		if a3==' ':a3='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='4':
		if a4==' ':a4='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='5':
		if a5==' ':a5='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='6':
		if a6==' ':a6='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='7':
		if a7==' ':a7='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	elif c=='8':
		if a8==' ':a8='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
	else:
		if a9==' ':a9='O';print('\n'+board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:com()
def check_1():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,s1
	if a1==a2 and a2==a3:
		if a1=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a1=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a1==a4 and a4==a7:
		if a1=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a1=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a1==a5 and a5==a9:
		if a1=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a1=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a2==a5 and a5==a8:
		if a2=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a2=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a3==a6 and a6==a9:
		if a3=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a3=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a3==a5 and a5==a7:
		if a3=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a3=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a4==a5 and a5==a6:
		if a4=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a4=='O':print('Computer won (n_n)'.upper());s1='Y'
	elif a7==a8 and a8==a9:
		if a7=='X':print('Congratulations! You won (=^_^=)');s1='Y'
		elif a8=='O':print('Computer won (n_n)'.upper());s1='Y'
	return s1
def check_2():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,s1
	if a1==a2 and a2==a3:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a1==a4 and a4==a7:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a1==a5 and a5==a9:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a2==a5 and a5==a8:
		if a2=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a2=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a3==a6 and a6==a9:
		if a3=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a3=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a3==a5 and a5==a7:
		if a3=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a3=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a4==a5 and a5==a6:
		if a4=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a4=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a7==a8 and a8==a9:
		if a7=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a8=='O':print('PLAYER 2 won (n_n)');s1='Y'
	return s1
def mode_1():
	ask=input("Who's first: PERSON or COMPUTER (P/C): ")
	while ask != 'P' and ask != 'C':
		ask=input("Please type only P or C to select mode: ")
	if ask == 'P':
		while a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5 == ' ' or a6 == ' ' or a7 == ' ' or a8 == ' ' or a9 == ' ':
			if s1!='Y':
				per()
				check_1()
				if a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5==' ' or a6==' ' or a7==' ' or a8==' ' or a9==' ':
					if s1!='Y':com();check_1()
			else:break
	else:
		while a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5 == ' ' or a6 == ' ' or a7 == ' ' or a8 == ' ' or a9 == ' ':
			if s1!='Y':
				com()
				check_1()
				if a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5==' ' or a6==' ' or a7==' ' or a8==' ' or a9==' ':
					if s1!='Y':per();check_1()
			else:break
def check_2():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,s1
	if a1==a2 and a2==a3:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a1==a4 and a4==a7:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a1==a5 and a5==a9:
		if a1=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a1=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a2==a5 and a5==a8:
		if a2=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a2=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a3==a6 and a6==a9:
		if a3=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a3=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a3==a5 and a5==a7:
		if a3=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a3=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a4==a5 and a5==a6:
		if a4=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a4=='O':print('PLAYER 2 won (n_n)');s1='Y'
	elif a7==a8 and a8==a9:
		if a7=='X':print('PLAYER 1 won (=^_^=)');s1='Y'
		elif a8=='O':print('PLAYER 2 won (n_n)');s1='Y'
	return s1
def per_1():
	global a1, a2, a3, a4, a5, a6, a7, a8, a9
	player = input('Enter the location of player 1 choice: ')
	while player != '1' and player != '2' and player != '3' and player != '4' and player != '5' and player != '6' and player != '7' and player != '8' and player != '9':
		player = input('Please select positions 1 through 9: ')
	if player == '1':
		if a1==' ':a1='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '2':
		if a2==' ':a2='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9; ');per_1()
	elif player == '3':
		if a3==' ':a3='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '4':
		if a4==' ':a4='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '5':
		if a5==' ':a5='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '6':
		if a6==' ':a6='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '7':
		if a7==' ':a7='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	elif player == '8':
		if a8==' ':a8='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
	else:
		if a9==' ':a9='X';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_1()
def per_2():
	global a1, a2, a3, a4, a5, a6, a7, a8, a9
	player = input('Enter the location of player 2 choice: ')
	while player != '1' and player != '2' and player != '3' and player != '4' and player != '5' and player != '6' and player != '7' and player != '8' and player != '9':
		player = input('Please select positions 1 through 9: ')
	if player == '1':
		if a1==' ':a1='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '2':
		if a2==' ':a2='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9; ');per_2()
	elif player == '3':
		if a3==' ':a3='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '4':
		if a4==' ':a4='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '5':
		if a5==' ':a5='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '6':
		if a6==' ':a6='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '7':
		if a7==' ':a7='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	elif player == '8':
		if a8==' ':a8='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
	else:
		if a9==' ':a9='O';print(board.format(a1,a2,a3,a4,a5,a6,a7,a8,a9))
		else:print('Please select positions 1 through 9: ');per_2()
def mode_2():
	while a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5 == ' ' or a6 == ' ' or a7 == ' ' or a8 == ' ' or a9 == ' ':
		if s1!='Y':
			per_1()
			check_2()
			if a1==' ' or a2==' ' or a3==' ' or a4==' ' or a5==' ' or a6==' ' or a7==' ' or a8==' ' or a9==' ':
				if s1!='Y':per_2();check_2()
		else:break
def call_menu():
	global menu #global gọi biến toàn cục, để còn sử dụng vào nhưng hàm sau
	menu =input(
			'Select game mode: 1. PERSON   vs COMPUTER\n'+
			'                  2. PLAYER 1 vs PLAYER 2\n'
			)
def play_more():
	global ans
	ask = input('Do you want to play more? (Y/N) : ')
def game():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,board,s1
	s1='N'
	a1=' ';a2=' ';a3=' '
	a4=' ';a5=' ';a6=' '
	a7=' ';a8=' ';a9=' '
	board=' {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} '
	call_menu()
	while menu != '1' and menu != '2' :
		print('Please select again')
		call_menu()
	if menu == '1':
		mode_1()
	else:
		mode_2()
	ask = input('Do you want to play more? (Y/N) : ')
	while ask != 'Y' and ask != 'N':
		print('Please select again (Y/N)')
		play_more()
	if ask == 'Y':
		game()
	else:
		exit()
game()