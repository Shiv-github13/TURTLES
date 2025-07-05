import pygame as shiv
import random

shiv.init()

width,height =800,600
screen=shiv.display.set_mode((width,height))
shiv.display.set_caption("ShivRainEffect")

flower_img = shiv.image.load("flower.png")
flower_rect = flower_img.get_rect()
flower_rect.topleft = (250, 200)  

WHITE =(255,255,255)
BLUE = (0,0,255)

raindrop_length = 20 
raindrop_speed= 7
raindrops= []

running= True
clock=shiv.time.Clock()

while running:
    for event in shiv.event.get():
        if event.type == shiv.QUIT:
            running = False

if len(raindrops)<100:
    x = random.randint(0, width)
    y = random.randint(-height, 0)
    raindrops.append([x, y])

for i in range(len(raindrops)):
    raindrops[i][1]+=raindrop_speed

if raindrops[i][1]>height:
    raindrops[i][1] =random.randint(-height, 0)

screen.fill(WHITE)

for drop in raindrops:
    shiv.draw.line(screen,
                   BLUE,(drop[0],
                         drop[1]),
                         (drop[0],drop[1]+
                          raindrop_length),2)
    
screen.blit(flower_img, flower_rect)

shiv.display.flip()

clock.tick(60)

shiv.quite()

