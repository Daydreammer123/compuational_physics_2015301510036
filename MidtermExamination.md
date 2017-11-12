## 期中作业

### 一、摘要
   呃，用pygame做一个游戏\
   其实我是妹子hh，但是pygame好像上手也还好，所以没做scratch直接做了pygame，只能按网上的教程一步步学了~

### 二、背景介绍
- 先随便模仿了一个玩，大致了解要怎么来。
- 思考关于炮弹打击的游戏。

### 三、小游戏
* 1、思路
呃，这是一个没那么正经的模仿教程的小游戏。\
最常见的小时候的射程游戏就是飞机打目标了吧，于是找了一个类似的教程，写了一个不是从下往上发炮弹而是从上往下掉鱼的小游戏。\
游戏有五轮，游戏者有10条lives，接一条鱼score加100分，碰到一个炸弹减50分，丢一条鱼少一条命，每100积分升级一个round。\
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
文件打包：
效果：

四、炮弹游戏


### 四、总结
    好像还是挺好玩的，表现形式比单纯用Python做题丰富
    
### 五、致谢
    感谢自己hhh
