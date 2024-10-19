该示例展示了如何在 Pygame 窗口中创建一个可交互的按钮类 Button。此类简化了按钮的创建和交互过程，使得开发者可以快速添加按钮到他们的 Pygame 应用中。按钮在按下时改变颜色，能够有效地捕捉点击事件并进行相应的操作。

功能
创建自定义按钮：通过定义按钮的位置、颜色和名称。
响应用户交互：在按钮按下时改变颜色并输出信息到控制台。
支持多按钮：可以轻松添加多个按钮并管理它们的事件。
要求
要运行此程序，您需要：

安装 Python 3.x
安装 Pygame 库（使用 pip install pygame）
安装
将此代码保存为 pygame_button_example.py 文件。
确保您的环境中已安装 Pygame 库：
pip install pygame

代码说明
以下是程序的核心代码，定义了 Button 类和创建两个可交互按钮的主要逻辑。

import easygui
import pygame
import time
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

class Button():
    def __init__(self, button_rect, front_color, after_color, button_name, screen):
        self.button_rect = button_rect
        self.front_color = front_color
        self.after_color = after_color
        self.button_name = button_name
        self.screen = screen
        self.paint_colors = front_color

    def draw(self):
        self.button_name = pygame.Rect(self.button_rect)
        pygame.draw.rect(self.screen, self.paint_colors, self.button_name)

    def click_events(self, event):
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
    
代码分解
按钮类 (Button)：

构造函数：初始化按钮的矩形、颜色、名称和 Pygame 窗口对象。
draw 方法：绘制按钮，使用 pygame.draw.rect 绘制矩形。
click_events 方法：处理鼠标事件，判断鼠标是否点击了按钮，并根据按下或释放改变按钮的颜色。
主程序逻辑：

初始化 Pygame 并创建窗口。
创建两个按钮，分别定义它们的颜色和位置。
在主循环中检测用户的事件，并根据点击的按钮输出不同的消息。
运行程序
打开终端并导航到包含 pygame_button_example.py 文件的目录。
使用以下命令运行程序：

python pygame_button_example.py
结论
这个示例为 pygame 开发者提供了一个简单而有效的按钮实现方案，帮助用户快速构建可交互的用户界面。您可以根据需要扩展此示例，添加更多功能或自定义按钮的外观和行为。
