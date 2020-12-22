# HELLO
# THIS IS THE PYTHON CODE FOR THE GAME "CATCH THE EGG"
# THESE COMMENTS WILL BE GUIDING YOU ACROSS THE CODE
# PROGRAMMED BY KANISHK SINGHAL(1ST YEAR BTECH) 

# IMPORTING SOME NECCESSARY LIBRARIES FOR THE GAME
import pygame
import random
import math
from pygame import mixer

pygame.init()

# SETTING THE DISPLAY SCREEN SIZE TO 800 X 533 
screen = pygame.display.set_mode((800,533))

#FIXING BORDERS FOR THE EGG BASKET
r_bound = 736
l_bound = 0

#INITIALIZING SOME IMPORTANT VARIABLE FOR LATER USE
is_pause = False
is_over = False
is_rules = False
is_running = True
high_score = 0

#INITIALIZING FONTS
font = []
font.append(pygame.font.Font('Fast Hand.otf',16))
font.append(pygame.font.Font('Fast Hand.otf',30))
font.append(pygame.font.Font('28 Days Later.ttf',50))

#COORDINATES TO DISPLAY SCORE ON TOP LEFT
scorex = 10
scorey = 10


# CHANGING TITLE, ICON, BACKGROUND MUSIC
pygame.display.set_caption(" CATCH THE EGG")
pygame.display.set_icon(pygame.image.load('001-easter.png'))
mixer.music.load('mystery them music.mp3')
mixer.music.play(-1)

#INITIALIZING 
def initialize_values():
	global eggimg,eggx,eggy,eggy_change
	global black_eggimg,black_eggx,black_eggy,black_eggy_change
	global basketimg,basketx,baskety,basketx_change,basket_speed
	global score
	score = 0
	
	# SOME BASE VALUES FOR BASKET
	basketimg = pygame.image.load('005-wicker-basket.png')
	basketx = 384
	baskety = 430
	basketx_change = 0
	basket_speed = 10

	# SOME BASE VALUES FOR BROWN EGGS
	eggimg = pygame.image.load('001-egg.png')
	eggx = random.randint(50,750)
	eggy = 10
	eggy_change = 4

	# SOME BASE VALUES FOR BLACK EGGS
	black_eggimg = pygame.image.load('002-egg-1.png')
	black_eggx = random.randint(50,750)
	black_eggy = 10
	black_eggy_change = 3

	# TO AVOID CASES IN WHICH BLACK AND WHITE EGGS DROP FROM SAME POSITION
	if black_eggx in range(eggx-64,eggx+64):
		black_eggx = random.randint(50,750)

#FUNCTION TO DISPLAY RULES
def rules():
	global is_rules,is_running
	while not is_rules:
		screen.blit( font[1].render("RULES: ",True,(0, 0, 0)), (380,100))
		screen.blit( font[1].render("1. CATCH THE FALLING WHITE EGGS IN THE BASKET",True,(147, 80, 32)), (60,180))
		screen.blit( font[1].render("2. DO NOT CATCH THE BLACK EGGS",True,(147, 80, 32)), (60,230))
		screen.blit( font[1].render("3. USE ARROW KEYS TO MOVE THE BASKET ",True,(147, 80, 32)), (60,280))
		screen.blit( font[1].render("ENJOY THE GAME",True,(147, 80, 32)), (270,350))
		screen.blit( font[1].render("PRESS ANY KEY TO CONTINUE",True,(147, 80, 32)), (200,400))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_rules = True
				is_running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					is_rules = True
					is_running = False
				else:
					is_rules = True
		
		pygame.display.update()

# FUNCTION TO PRINT BASKET
def m_basket(x,y):
	screen.blit( basketimg, (x, y) )

# FUNCTION TO PRINT EGGS
def m_egg(eggimg,x,y):
	screen.blit( eggimg, (x, y) )

# TO CHECK CATHCING WHITE(BROWN) EGG
def is_catch(bx,by,ex,ey):
	distance = math.sqrt( math.pow( ex - bx ,2) + math.pow( ey - by, 2) )
	if distance < 25:
		return True
	else:
		return False

#GAMEOVER
def game_over(reason):
	global eggx,eggy,black_eggx,black_eggy,eggy_change
	global is_over,score,is_running,is_rules
	global basketimg,basketx,baskety,basketx_change,basket_speed
	flag = 0
	while not is_over:
		# IF LOST DUE TO MISSING WHITE EGG
		if reason == 'w':
			screen.blit( font[2].render("GAME OVER",True,(60, 60, 60)), (310,70))
			screen.blit( font[2].render("YOU MISSED A            EGG",True,(60, 60, 60)), (140,130))
			screen.blit( font[2].render("WHITE",True,(230, 203, 163)), (430,130))
			screen.blit( pygame.image.load('003-egg-2.png'),(eggx,eggy))
			screen.blit( basketimg,(basketx,baskety))
		
		# IF LOST DUE TO CATCHING BLACK EGG
		if reason == 'b':
			screen.blit( font[2].render("GAME OVER",True,(60, 60, 60)), (310,70))
			screen.blit( font[2].render("YOU CAUGHT A BLACK EGG",True,(60, 60, 60)), (160,130))
			screen.blit( basketimg,(basketx,baskety))
		
		# DEFAULT SYNTAXES
		screen.blit( font[1].render("Score : " + str(score),True,(175, 74, 0)), (350,260))
		screen.blit( font[1].render("PRESS R TO RESTART",True,(175, 74, 0)), (260,300))
		screen.blit( font[1].render("PRESS ANY KEY TO EXIT",True,(175, 74, 0)), (240,340))
		screen.blit( font[1].render("(OTHER THAN ARROW KEYS)",True,(175, 74, 0)), (220,380))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_over = True
				is_running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_r:
					initialize_values()
					is_rules = False
					flag = 1
				else:	
					is_running = False
					is_over = True
					
			
		if flag:
			break
		pygame.display.update()

#SCORE
def show_score(x,y):
	screen.blit( font[0].render("Score : " + str(score),True,(246, 179, 50)), (x,y))
	screen.blit( font[0].render("High Score : " + str(high_score),True,(246, 179, 50)), (x,y+20))


#FUNCTION TO PAUSE THE GAME
def pause():
	global is_pause,is_running
	while is_pause:
		
		screen.blit( font[2].render("GAME PAUSED",True,(60, 60, 60)), (270,70))
		
		for event in pygame.event.get():
			# QUIT GAME IF PRESSED x BUTTON ON WINDOW
			if event.type == pygame.QUIT:
				is_running = False
				is_pause = False
			
			if event.type == pygame.KEYDOWN:
				# REMOVING PAUSE WINDOW AFTER PRESSING P AGAIN
				if event.key == pygame.K_p:
					is_pause = False
				# QUIT GAME IF PRESSED ESC KEY
				if event.key == pygame.K_ESCAPE:
					is_pause = False
					is_running = False
		pygame.display.update()


# MAIN GAME LOOP
initialize_values()
while is_running:
	
	# DISPLAY BACKGROUND IMAGE
	screen.blit(pygame.image.load('bamboo-leaf-elements-green.png'),(0,0))
	
	# DISPLAY RULES AFTER EVERY GAME
	if not is_rules:
		rules()
	
	for event in pygame.event.get():
		# QUIT GAME IF PRESSED x BUTTON ON WINDOW
		if event.type == pygame.QUIT:
			is_running = False
		
		if event.type == pygame.KEYDOWN:
			# QUIT GAME IF PRESSED ESC KEY
			if event.key == pygame.K_ESCAPE:
				is_running = False
			
			# MOVING BASKET LEFT 		
			if event.key == pygame.K_LEFT:
				basketx_change = -basket_speed
			
			# MOVING BASKET RIGHT
			if event.key == pygame.K_RIGHT:
				basketx_change = basket_speed
			
			# PRESSING P TO PAUSE THE GAME
			if event.key == pygame.K_p:
				is_pause = True
				pause()
		
		# STOPPING BASKET FROM MOVING IF KEY IS NOT LEFT
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				basketx_change = 0

	# TO DISPLAY THE BASKET TO OTHER BORDER IF IT CROSSES ONE BORDER
	if basketx>r_bound:
		basketx=l_bound
	if basketx<l_bound:
		basketx=r_bound
	

	# CALLING GAME OVER FUNCTION AFTER WHITE EGGS FALLS BELOW A CERTAIN LINE
	if eggy>480:
		mixer.Sound('explosion.wav').play()
		game_over('w')
	
	# TRANSFERING BLACK EGG TO TOP IF WE LEFT BLACK EGG
	if black_eggy>480:
		black_eggy = 10
		black_eggx = random.randint(50,750)
		
		# TO AVOID CASES IN WHICH BLACK AND WHITE EGGS DROP FROM SAME POSITION
		if black_eggx in range(eggx-64,eggx+64):
			black_eggx = random.randint(50,750)
	
	# CALLING GAME OVER FUNCTION AFTER CATCHING THE BLACK EGG
	if is_catch(basketx+16, baskety+16, black_eggx, black_eggy):
		mixer.Sound('explosion.wav').play()
		game_over('b')		

	# INCREASING POINTS AFTER CATCHING WHITE EGG
	if is_catch(basketx+16, baskety+16, eggx, eggy):
		eggx = random.randint(50,750)
		eggy = 10
		score += 1
		if score > high_score:
			high_score=score
		mixer.Sound('laser.wav').play()
	
	# INCREASING SPEEDS OF EGG DEPENDING UPON SCORES
	eggy_change = 4 + score//5
	black_eggy_change = 3 + score//5
	
	# LOGIC TO MAKE EGGS FALL
	eggy += eggy_change
	black_eggy += black_eggy_change
	
	# CHANGE X COORDINATE OF BASKET
	basketx += basketx_change 

	m_basket(basketx,baskety)
	m_egg(eggimg,eggx,eggy)
	m_egg(black_eggimg,black_eggx,black_eggy)
	show_score(scorex,scorey)

	pygame.display.update()

# PROGRAMMED BY KANISHK SINGHAL(1ST YEAR BTECH) 