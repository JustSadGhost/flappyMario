import play
from random import randint
import pygame

background = ['The_space_of_JSG_1.png','The_space_of_JSG_2.png']                    
fon= play.new_image(image=background[0])
# @play.repeat_forever
# async def fon():
#     for i in background:
#         fon.image =i 
#         await play.timer(2/3)
status = 1

play.screen.width = 800
play.screen.height = 640
n=0
count = play.new_text(words='SCORE: {}'.format(n), color= 'yellow', x = play.screen.left+100, y = play.screen.top-50)

u_lose = play.new_image("u_lose.png", size = 750)

exit_demon = play.new_image('Exit_button_vadsl.png', x = play.screen.right-100, y = play.screen.top-50)
exit_demon.hide()

def sdelat_truby(y, delta):
    truba = play.new_box(color = 'yellow', transparency=50, x = 475, y = y, width=75, height=460)
    # truba_image = play.new_image('truba.png', x = truba.x, y = truba.y, size = 25)
    truba_2 = play.new_box(color = 'yellow', transparency=50, x = 475, y = y + 575 + delta, angle = 180, width=75, height=460)
    # truba_2_image = play.new_image('truba.png', x = truba_2.x, y = truba_2.y, size = 25)
    # truba = play.new_image('My space pipe_1.png',  x = 475, y = y, size = 250)
    # truba_2 = play.new_image('My space pipe_2.png', x = 475, y = y + 575 + delta, angle = 180,  size = 250)
    return truba, truba_2
    # return truba_image, truba_2_image


truby = []

@play.repeat_forever
async def make(): 
    global n, status
    if status ==1:
        y = randint(-600, -150)
        delta = randint(200, 300)
        truby.append(sdelat_truby(y, delta))
        n+=1
        count.words = 'SCORE: {}'.format(n)
        await play.timer(3.75)

bird_suits = ['Mario_1.png', 'Mario_2.png']
bird = play.new_image(bird_suits[0], x = -250, y = 0)
bird.start_physics(stable = False, y_speed = 0, bounciness=0.3)


u_lose.hide()


@play.repeat_forever
def game():
    for truba in truby:
        truba[0].x -= 5
        truba[1].x -= 5
        if truba[0].x < -475:
            truba[0].remove()
            truba[1].remove()
            truby.remove(truba)


@play.repeat_forever
async def suits():
    if play.key_is_pressed('Ц','ц','W','w','space','up'):
        bird.image = bird_suits[1]
        await play.timer(0.5)
    else:
        bird.image = bird_suits[0]

@exit_demon.when_clicked
def pozorno_slitsya():
    exit()


@play.repeat_forever
async def keypads():
    global status
    for truba in truby:
        if play.key_is_pressed('Ц','ц','W','w','space','up'):
            bird.physics.y_speed = 50
        if bird.is_touching(truba[1]) or bird.is_touching(truba[0]):
            for g in truby:
                g[1].hide()
                g[0].hide()
            truby.remove(truba)
            bird.stop_physics()
            bird.hide()
            u_lose.show()
            exit_demon.show()
            status = 0 
    await play.timer(1/60)
play.start_program()
#100 : 460
