import pygame

#游戏的初始化
pygame.init()
#创建游戏窗口
#返回一个surface对象
screen = pygame.display.set_mode((480, 700))

#绘制背景图像
background = pygame.image.load("./images/background.png")#./表示当前目录下
screen.blit(background, (0,0))


#绘制飞机
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero,(100, 300))

#可以在所有的绘制工作完成之后统一调用此方法
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()
#1.定义飞机的初始位置
hero_rect = pygame.Rect(200, 300, 102, 126)

#游戏循环，意味着游戏的正式开始
while True:

    #可以指定循环体内部代码执行的频率
    clock.tick(60)

    #2.修改飞机的位置
    hero_rect.y -= 1

    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    #3.调用blit方法绘制图像
    screen.blit(background,(0,0))
    screen.blit(hero, hero_rect)#blit方法两个参数：1.要绘制的对象 2.坐标的元组，或者一个矩形的对象

    #4.调用update更新显示
    #每一次调用update()方法之前，需要把所有的游戏图像都重新绘制一边
    pygame.display.update()

    pass



pygame.quit()

