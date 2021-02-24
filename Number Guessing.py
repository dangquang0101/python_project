import random
print(
	"##    ##  ##    ##  ##          ##  #######   ########  ####### \n"+
	"####  ##  ##    ##  ####      ####  ##    ##  ##        ##    ##\n"+
	"## ## ##  ##    ##  ## ##    ## ##  #######   ########  ####### \n"+
	"##  ####  ##    ##  ##  ######  ##  ##    ##  ##        ##   ## \n"+
	"##    ##  ########  ##    ##    ##  #######   ########  ##    ##\n"+
	"------------------------------------------------\n"+
	"########  ##    ##  ########  ########  ########\n"+
	"##        ##    ##  ##        ##        ##      \n"+
	"##  ####  ##    ##  ########  ########  ########\n"+
	"##    ##  ##    ##  ##              ##        ##\n"+
	"########  ########  ########  ########  ########")
intro='Rule: the game will choose one of number from 1 to 100, your mission is quessing that number, each time will have a hint.'
print(intro+'\nThe game is starting:')
def hint1(num):
	an=random.randint(0,100)
	bn=random.randint(0,100)
	while an<num:
		an=random.randint(0,100)
	while bn>num:
		bn=random.randint(0,100)
	hint1='this number is from {} to {}'.format(bn,an)
	print(hint1)
def hint2(num):
	if 0<num<10:print('This number has 1 digit.')
	elif 9<num<100:print('This number has 2 digit')
	else:print('This number has 3 digit')
def hint3(num):
	an=random.randint(0,100)
	bn=random.randint(0,100)
	while an<num:
		an=random.randint(0,100)
	while bn>num:
		bn=random.randint(0,100)
	h=random.randint(0,101)
	hint3='this number is from {} - {} to {}'.format(bn+h,h,an)
	print(hint3)
def play_continue():
	ans=input('Do you want to play more(Y/N): ')
	if ans=='Y':
		game()
	elif ans=='N':
		exit()
	else:
		print("Please write only 'Y' or 'N'")
		play_continue()
def game():
	turn=0
	num=random.randint(1,100)
	ans=int(input('Type a number here: '))
	w_ans=['Wrong Q.Q','Incorrect =((','False T.T']
	c_ans=['Wow, this is a corect answer (^-^)',"That's right (^○^)",'Welldone (^_^)']
	if ans == num:
		a=random.randint(0,len(w_ans)-1)
		print(c_ans[a])
		turn=turn+1
		rint('You have found that number within {} turns'.format(turn).upper())
		play_continue()
	else:
		b=random.randint(0,len(c_ans)-1)
		print(w_ans[b])
		while ans != num:
			if num==88:
				print('This number, when reversed, remains unchanged.')
				turn=turn+1
			elif num==99:
				print('If this number is reversed, it will be equal to 2/3 of the original number.')
				turn=turn+1
			elif num==66:
				print('If you reverse this number, it will be 1.5 times the original number.')
				turn=turn+1
			else:
				cn=random.randint(1,3)
				if cn==1:
					hint1(num)
					turn=turn+1
				elif cn==2:
					hint2(num)
					turn=turn+1
				elif cn==3:
					hint3(num)
					turn=turn+1
			ans=int(input('One more time: '))
		print("Finally, that's right")
		print('You have found that number within {} turns'.format(turn+1).upper())
		play_continue()
game()
