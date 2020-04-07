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
screen.blit(hero,(100, 300))

#可以在所有的绘制工作完成之后统一调用此方法
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()
i = 0
#保证程序启动之后不会立刻结束，称之为游戏循环，意味着游戏的正式开始
while True:

    #可以指定循环体内部代码执行的频率
    clock.tick(60)
    print(i)
    i += 1
    pass



pygame.quit()

