## 期中作业

### 一、摘要
   呃，用pygame做一个游戏\
   其实我是妹子hh，但是pygame好像上手也还好，所以没做scratch直接做了pygame，只能按网上的教程一步步学了~

### 二、背景介绍
- 先随便模仿了一个玩，大致了解要怎么来。
- 思考关于炮弹打击的游戏。

### 三、小游戏
* 1、思路\
呃，这是一个没那么正经的模仿教程的小游戏。\
最常见的小时候的射程游戏就是飞机打目标了吧，于是找了一个类似的教程，写了一个不是从下往上发炮弹而是从上往下掉鱼的小游戏。\
游戏有五轮，游戏者有10条lives，接一条鱼score加10分，每100积分升级一个round，丢一条鱼或者碰到一个炸弹都少一条命，命归0游戏结束。\
第一、第二轮只有鱼，第三轮开始有炸弹，并且鱼的下降速度随round增加变快，即游戏难度越来越大。\
每局lives剩下不多时猫会改变图片做出提示。没命了就会回到初始界面。还是挺简单的。

* 2、代码
```python
import sys, random, time, pygame
from pygame.locals import *
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("猫吃鱼")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 18)
font3 = pygame.font.Font(None, 34)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
cat=pygame.image.load("cat1.png")
width,height=cat.get_size()
pic=pygame.transform.scale(cat,(width,height))
fish=pygame.image.load("fish.png")
width,height=fish.get_size()
fish=pygame.transform.smoothscale(fish,(width//3,height//3))
init=pygame.image.load("cat3.jpg")
width,height=init.get_size()
init=pygame.transform.smoothscale(init,(width//3,height//3))
lives = 10
score = 0
clock_start = 0
game_over = 1
mouse_x = mouse_y = 0
Round =1
mine=0
mine_png=pygame.image.load("mine.png")
cat2=pygame.image.load("cat2.png")
flag=0
pos_x = 300
pos_y = 410-40
bomb_x = random.randint(0,500)
mine_x=random.randint(0,500)
bomb_y = -50
vel_y = 0.4
vel_yy=0.6
mine_y=-100
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 10
                score = 0
                Round =1
                vel_y=0.4
                mine=0
                flag=0
                pic=cat
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.fill((0,0,100))
    if game_over:
        screen.blit(init,(60, 60))
        print_text(font3, 400, 150,"Clicked To Play!")
        print_text(font3, 400, 100,"THE CAT & FISH!")
        print_text(font2, 410, 280,"@Happy midterm examination")
    else:
        if score >100 and score <200:
             Round=2
        elif score >200 and score <300:
             Round =3
        elif score >300 and score <400:
             Round=4
        elif score >400 and score <500:
             Round =5
        elif score >=500:
             Round =6
        print_text(font1, 280, 0, "Round: " + str(Round))
        if Round ==1:
            vel_y=0.4
        elif Round ==2:
            vel_y=0.6
        elif Round ==3:
            vel_y=0.8
        elif Round ==4:
            vel_y=1.0
        elif Round ==5:
            vel_y=1.2
        bomb_y += vel_y
        mine_y+=vel_yy 
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        elif bomb_y > pos_y:
            if bomb_x > pos_x-10 and bomb_x < pos_x + 70:
                score += 10
                bomb_x = random.randint(0, 500)
                bomb_y = -50
        if Round >2:
            if mine_y > 500:
                mine_x = random.randint(0, 500)
                mine_y = -50
            elif mine_y > pos_y:
                if mine_x > pos_x and mine_x < pos_x + 40:
                    mine_x = random.randint(0, 500)
                    mine_y = -50
                    lives-=1
                    pic=cat2
                    if lives == 0:
                        game_over = True
        screen.blit(fish,(bomb_x,int(bomb_y)))
        if Round >2:
            screen.blit(mine_png,(mine_x,int(mine_y)))
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 510:
            pos_x = 500
        if lives<5:
            pic=cat2
        screen.blit(pic,(pos_x,pos_y))
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 500, 0, "SCORE: " + str(score))
    pygame.display.update()
```
* 3、文件打包：【[压缩包](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/files/cat%26fish.rar)】
* 4、效果：![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/files/%E7%8C%AB%E5%90%83%E9%B1%BC%E6%95%88%E6%9E%9C.gif)

### 四、炮弹游戏
* 1、update~\
玩了很久还是不知道炮弹咋弄，就搞了个射击进击版~炮弹我再试试\
进阶版加了音乐和音效，改变了视角，有点难玩，，所以命增加到了25条哈哈（因为我自己写的自己也玩不通关……要求熟练度还是有点高hh）\
和前面一样一共25条命，空枪一次少一条，打中一个加10分，\
每个level有三波，每波目标1个2个4个，速度递增。

* 2、代码：
```python
import pygame, sys, random, time

pygame.init()

size = [500,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooting!")
pygame.mouse.set_visible(False)

black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
yellow = [255,165, 0]
purple = [102, 0, 172]
VOLUME = 5

color = [white, green, yellow, red]

laser = pygame.mixer.Sound("LAZER.wav")

xplode = pygame.mixer.Sound("ExplosionSR.wav")
kaboom = pygame.mixer.Sound("frowny.ogg")
lvlUp = pygame.mixer.Sound("magic.wav")
gun = pygame.image.load("gun.png").convert()
scale = 100, 80
gun = pygame.transform.scale(gun, scale)
gun.set_colorkey(white)
bg1 = pygame.image.load("bj1.jpg").convert()
bg2 = pygame.image.load("bj2.jpg").convert()
bg3 = pygame.image.load("bj3.jpg").convert()
bg4 = pygame.image.load("bj4.jpg").convert()
bg6 = pygame.image.load("bj5.jpg").convert()
bg_sound = pygame.mixer.Sound('bg.ogg')
bg_sound.set_volume(0.3 * VOLUME)
bg_sound.play(-1)


backs = [bg1, bg2, bg3,bg4,bg6]

for i in range(5):
	backs[i] = pygame.transform.scale(backs[i], size)

background = pygame.image.load("blowUp.jpg").convert()

aim = pygame.image.load("aim.png").convert()
aim.set_colorkey(white)
lvl1 = pygame.image.load("tomato.png").convert()
lvl1.set_colorkey(black)
lvl3 = pygame.image.load("mine.png").convert()
lvl3.set_colorkey(white)
lvl5 = pygame.image.load("probe.png").convert()
lvl5.set_colorkey(white)
lvl7 = pygame.image.load("killbots.png").convert()
lvl7.set_colorkey(white)
monster = [lvl1, lvl3, lvl5, lvl7]
lvlup = pygame.image.load("LevelUp.png").convert()
bang = pygame.image.load("boom.png")
game_over = pygame.image.load("game_over.jpg")


clock = pygame.time.Clock()
screenCenter = screen.get_rect().center

monsters = 1;
monster_spot = []
monster_inc = 1
offset =[]
over = False

for i in range(10):
	ranpos = [random.randint(0,500-59), random.randint(0,500-59)]
	monster_spot.append(ranpos)
for i in range(10):
	offset.append([random.randint(1,4),random.randint(1,4)])
	
kill = False
kills = 0
lvl = 1
misses =25
dim = 64, 64
enemy = 0
waves = 1
score = 0
fullSCR = False
bLvl = 0

midx = screen.get_rect().centerx
midy = screen.get_rect().centery
play = 0
done = False
start = True
bonus = 0
hitCount = 0
msg = '' 
msgDisplay = False
msgCounter = 0
nlist = ord('1'),ord('2'),ord('3'),ord('4'),ord('5')
stars = []
for i in range(50):
	stars.append([random.randint(1,500), random.randint(1,500)])

while not done:
	clock.tick(50)	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			if not start:
				for i in range(monsters):
					x = monster_spot[i][0]
					y = monster_spot[i][1]
					if (aim_pos[0] >= x and aim_pos[0] <= x + dim[0]) and (aim_pos[1] >= y and aim_pos[1] <= y + dim[1]):
						hit_spot = monster_spot[i]
						monster_spot.remove(monster_spot[i])
						monsters-= 1
						kills+= 1
						bonus += 15
						hitCount += 1
						kill = True
						msgDisplay = True
				if not kill:
					misses -= 1
					hitCount = 0
					msg = ''
					bonus = 0
					laser.play()
				for i in range(monsters):
					offset.insert(i, [random.randint(lvl,lvl+2),random.randint(lvl,lvl+2)])
		if event.type == pygame.KEYDOWN:
			if event.key == ord(' ') or ord('z'):
				pygame.display.set_caption("BOOM");
		if event.type == pygame.KEYUP:
			if event.key == ord(' '):
				if start:
					start = False
			elif event.key == ord('a'):
				if not fullSCR:
					screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
					fullSCR = True
				else:
					screen = screen = pygame.display.set_mode(size)
					fullSCR = False
			elif event.key == pygame.K_ESCAPE:
				done = True
			elif event.key == ord('r'):
				if over:
					over = False
					misses = 5
					lvl = 1
					enemy = 0
					monsters = 1
					waves = 1
					play = 0
					monster_inc = 1
					kills = 0
					score = 0
					start = True
			elif event.key== ord('x'):
				if start:
					lvl += 1
					play = 0
			elif event.key in nlist:
				misses += int(chr(event.key))
	if start:
		screen.fill(black)
		if lvl == 1:
			screen.blit(background,[0,0])
		if lvl > 1:
			screen.blit(lvlup,[0,0])
			if play < 1:
				lvlUp.play()
				play = 1
			
		font = pygame.font.SysFont(None, 50)
		font2 = pygame.font.SysFont(None, 30)
		text = font.render('LEVEL ' + str(lvl), True, red)
		if lvl > 1 :
			text2 = font2.render('[press space to continue...]', True, white )
		else:
			text2 = font2.render('[press space to continue...]', True, black)
		earn = font2.render('1 EXTRA SHOT AWARDED', True, yellow)
		textRect = text.get_rect()
		textRect.centerx = midx
		textRect.centery = midy	
		screen.blit(text, textRect)		
		screen.blit(text2, [100,300])
		
		if lvl > 1:				
			screen.blit(earn, [120, 470])
		
	elif not over and not start:
		
		screen.fill(black)
		screen.blit(backs[bLvl], [0,0])
		if monsters == 0: 
			if waves < 3:
				monster_inc = waves * 2
				monsters = monster_inc
				waves+= 1
			else :
				monsters = 1
				lvl += 1
				misses += 1
				hitCount = 0
				msg = 0
				monsters_inc = 1
				waves = 1
				play = 0
				start = True
				if bLvl < 4:
					bLvl += 1
				else:
					bLvl = 0
			if lvl == 1:
				enemy = 0
				bLvl = 0
			elif lvl == 3:
				enemy = 1
				bLvl == 1
			elif lvl ==5:
				enemy = 2
				bLvl = 2
			elif lvl == 8:
				enemy = 3
				bLvl = 3
			elif lvl ==9:
				bLvl = 4
			
				
			for i in range(monsters):
				monster_spot.append([random.randint(0,500-59), random.randint(0,500-64)])
				offset[i] = [random.randint(lvl, lvl+2), random.randint(lvl, lvl+2)]
		
		if msgDisplay == True:
			if hitCount > 2:
				msg = str(bonus) + 'pts ' + str(hitCount) + 'x CHAIN BONUS'
				msgCounter += 1
	
			if msgCounter > 150:
				msgCounter = 0
				score += bonus
			
		if kill:
			xplode.play()
			for i in range(monsters):
				screen.blit(monster[enemy], monster_spot[i])
				screen.blit(aim, [aim_x, aim_y])
			for a in range(1,60,3):
				boom = pygame.transform.scale(bang,(a,a +6))
				screen.blit(boom, hit_spot)
				pygame.display.update()
			kill = False	
		
		for i in range(monsters):
			screen.blit(monster[enemy], monster_spot[i])

if monster_spot[i][1] > (size[1] - dim[1]) or monster_spot[i][1]<= 0:

offset[i][1] = -offset[i][1]
			if monster_spot[i][0] > size[0] - dim[0] or monster_spot[i][0] <= 0:
				offset[i][0] = -offset[i][0]
			monster_spot[i][1] += offset[i][1]
			monster_spot[i][0] += offset[i][0]
		
		
		aim_pos = pygame.mouse.get_pos()
	
		if misses < 1:
			play = 0
			over = True
			
		font = pygame.font.SysFont(None, 30)
		text = font.render('KILLS: ' + str(kills), True, red)
		text2 = font.render('MISSES LEFT: ' + str(misses), True, black)
		text3 = font.render('WAVE: ' + str(waves), True, green)
		text4 = font.render('LEVEL: ' + str(lvl), True, yellow)

		screen.blit(text, [5,5]) 
		screen.blit(text2, [300, 5])
		screen.blit(text3, [150,5])
		screen.blit(text4, [200, 470])

	
		aim_x = aim_pos[0] - 30
		aim_y = aim_pos[1] - 30
		if aim_x < size[0] and aim_y < size[1]:
			screen.blit(aim, [aim_x, aim_y ])
			screen.blit(gun, [aim_pos[0]-10, size[0]-scale[1]])

	elif over:
		screen.fill(black)
		if play < 1:
			kaboom.play()
			score += lvl * kills * 10
			play +=1
			
		screen.blit(game_over, [0,0])
		text = font.render('PRESS \'R\' TO RESTART ', True, white)
		text2 = font.render('AND \'ESC\' TO EXIT ', True, white) 
		text3 = font.render('YOU SCORED ' + str(score)+ ' pts', True, yellow)
		textRect = text.get_rect()
		textRect.centerx = midx
		textRect.centery = midy
		textRect2 = text2.get_rect()
		textRect2.centerx = midx
		textRect2.centery = midy + 35
		textRect3 = text3.get_rect()
		textRect3.centerx = midx
		textRect3.centery = midy + 70		
		screen.blit(text, textRect) 
		screen.blit(text2, textRect2)
		screen.blit(text3, textRect3)

	pygame.display.flip()
	
pygame.quit()
```

* 3、文件打包：【[压缩包](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/files/Shooting%EF%BC%81.rar)】

* 4、效果:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/files/shooting%E6%95%88%E6%9E%9C.GIF)

### 五、总结
    好像还是挺好玩的，表现形式比单纯用Python做题丰富
    
### 六、致谢
    感谢自己hhh
