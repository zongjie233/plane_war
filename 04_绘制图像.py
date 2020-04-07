import pygame
pygame.init()
#创建游戏窗口
#返回一个surface对象
screen = pygame.display.set_mode((480, 700))

#绘制背景图像
#1.加载图像数据
background = pygame.image.load("./images/background.png")#./表示当前目录下
#2.blit绘制图像
screen.blit(background, (0,0))
#3.update更新屏幕显示
pygame.display.update()









while True:#保证程序启动之后不会立刻结束，称之为游戏循环
    pass



pygame.quit()

