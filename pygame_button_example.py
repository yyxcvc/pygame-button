import pygame
import time
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))

# 用来在pygame窗口上按钮
class Button():
    # 变量的定义 button_rect 是一个矩形对象, 颜色, 按钮名字, 窗口对象 
    # front_color 是按钮的颜色, after_color 是按钮按下后的颜色
    # button_name 是按钮的名字, screen 是窗口对象
    # paint_colors 是按钮绘制的实际颜色
    def __init__(self, button_rect, front_color, after_color, button_name, screen):
        self.button_rect = button_rect
        self.front_color = front_color
        self.after_color = after_color
        self.button_name = button_name
        self.screen = screen
        self.paint_colors = front_color

    # 画出按钮
    def draw(self):
        # 定义的名字 self.button_name 是一个矩形对象, 所以可以直接画
        self.button_name = pygame.Rect(self.button_rect)
        # 画出按钮 参数介绍: self.screen = pygame窗口, 颜色, 矩形对象
        pygame.draw.rect(self.screen, self.paint_colors, self.button_name)

    # 检查是否点击了按钮
    def click_events(self, event):
        # 先检测是否点击了按钮, 然后再检测鼠标是否在边框内里面, 最后检测是不是鼠标左键
        if event.type == pygame.MOUSEBUTTONDOWN and self.button_name.collidepoint(event.pos) and event.button == 1:
            self.paint_colors = self.after_color
            self.draw()
            pygame.display.flip()
            return True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.paint_colors = self.front_color
            self.draw()
            pygame.display.flip()



green = (166, 215, 203)
red = (215, 166, 178)

button_rect1 = (100, 150, 200, 30)
button = Button(button_rect1, green, red, "button1", screen)
button.draw()

button_rect2 = (100, 200, 200, 30)
button2 = Button(button_rect2, red, green, "button2", screen)
button2.draw()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
            pygame.quit()

        if button.click_events(event):
            print("hello world1")
        if button2.click_events(event):
            print("hello world2")

    pygame.display.flip()