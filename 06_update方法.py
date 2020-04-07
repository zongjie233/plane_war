import pygame
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

while True:#保证程序启动之后不会立刻结束，称之为游戏循环
    pass



pygame.quit()

