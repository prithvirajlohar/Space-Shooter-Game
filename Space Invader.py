import pygame	#pip install pygame
import random
import math
from pygame import mixer

pygame.init()											#pygame constructor

screen = pygame.display.set_mode((800,600))				#pygame screen builder with its size

pygame.display.set_caption("Spaceship Infinity WAR")	#title of screen
icon = pygame.image.load("gameboy.png")					#icon of screen
pygame.display.set_icon(icon)							#icon of screen

background = pygame.image.load("Space BKG.jpg")
explosionImg = pygame.image.load("explosionImg.png")

playerimg = pygame.image.load("spaceship.png")	
pX = 370
pY = 520
Change = 0

bulletimg = pygame.image.load("bullet (2).png")
bX  = pX
bY = 0
fire = False

images = ["enemy.png","monster.png","insect.png"]
enemy_images=[]
eX=[]
eY=[]
cex=[]

for i in range(6):
	enemy_images.append(pygame.image.load(random.choice(images)))
	eX.append(random.randint(i+1+0,736))
	eY.append(random.randint(0,64))
	cex.append(2)

score_value = 0
font = pygame.font.Font("freesansbold.ttf",35)
scr_X = 10
scr_Y = 10

Gameover_font = pygame.font.Font("freesansbold.ttf",70)

def player(px,py):
	screen.blit(playerimg,(px,py))

def enemy(ex,ey,i):
	screen.blit(enemy_images[i],(ex,ey))

def bullet(bx,by):
	global fire
	fire = True
	screen.blit(bulletimg,(bx+19,by))
	

def is_hit(ex,ey,bx,by):
	distance = math.sqrt(math.pow(ex-bx,2) + math.pow(ey-by,2))
	if distance < 32	 :
		screen.blit(explosionImg,(eX[i],eY[i]))
		return True
	return False

def show_score(x,y):
	safe = font.render("_________________________________________________",True,(231, 76, 60))
	screen.blit(safe,(0,456))
	score = font.render("Score: "+str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))
	

def GameOver():
	GameOvertext = Gameover_font.render("GAMEOVER",True,(255,255,255))
	screen.blit(GameOvertext,(200,255))


running = True

while running:

	screen.fill((0,0,0))					# To get background colors in RGB from

	screen.blit(background,(0,0))
	for event in pygame.event.get():		# To get input from keybord/mouse
		
		if event.type == pygame.QUIT:		# QUIT Game
			running = False

		if event.type == pygame.KEYDOWN:	# type = Any key  && KEYDOWN is action when key is pressed
			
			if event.key == pygame.K_ESCAPE:	# QUIT Game with ESC_Key
				running = False
			if event.key == pygame.K_LEFT:
				Change = -4
			if event.key == pygame.K_RIGHT:
				Change = 4
			if event.key == pygame.K_SPACE:
				fire = False
				bX = pX
				bullet(bX,bY)
				bs = mixer.Sound("laser.wav")
				bs.play()

		if event.type == pygame.KEYUP:		# KEYUP is action when key is released
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				Change = 0

	#Spaceship Position code
	pX += Change
	if pX <= 0:
		pX = 0

	elif pX >= 736:
		pX = 736
	
	#Enemy  Position code	
	for i in range(6):
		eX[i] += cex[i]

		if eY[i] >= 440:
			for j in range(6):
				eX[j] == 2000
			GameOver()
			break

		if eX[i] <= 0:
			eY[i] += 10
			cex[i] += 1

		elif eX[i] >= 736:
			eY[i] += 10
			cex[i] += -1
			
		hit = is_hit(eX[i],eY[i],bX,bY)
		if hit:
			explosion = mixer.Sound("explosion.wav")
			explosion.play()
			bY = 480
			fire = False 
			score_value += 1
			eX[i] = random.randint(0,736)
			eY[i] = random.randint(0,64)	
		
		enemy(eX[i],eY[i],i)
		
	if bY <= 0:
		fire = False	
		bY = 480

	if fire == True :	
		bullet(bX,bY)
		bY-=5

	#Functions callers
	player(pX,pY)
	show_score(scr_X, scr_Y)

	pygame.display.update()	# its continously updates screen to get color/events