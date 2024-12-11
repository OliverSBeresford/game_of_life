from cell import Cell
import pygame as py
import numpy
import sys, random
from pygame.locals import QUIT
from time import sleep

class Simulation:

    def __init__(self):
        self.cells = 10
        self.cellSize = 10
        self.board = [[Cell(x, y, self.cellSize) for x in range(40)]
                                    for y in range(40)]
        self.board[19][18].isAlive = True
        self.board[19][19].isAlive = True
        self.board[19][20].isAlive = True
        self.screen = py.display.set_mode((400, 400))
        py.display.set_caption('The Game of Life')
        self.clock = py.time.Clock()
        self.width = 400
        self.height = 400
        self.paused = False
        self.temp = []
        self.speed = 0.5
        self.color = (255, 120, 120)
        self.colors = [(173, 216, 230), (255, 120, 120), (5, 252, 42), (0, 255, 0), (141, 5, 252), (255, 0, 0), (0, 0, 255), (0, 0, 0)]

    def update(self):
        [j.willLive(self.board) for i in self.board for j in i]
        for i in self.board:
            for j in i:
                if j.will:
                    j.isAlive = True
                else:
                    j.isAlive = False

    def start(self):
        while True:
            for event in py.event.get():
                if event.type == QUIT:
                    py.quit()
                    sys.exit()
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_p:
                        self.paused = True if not self.paused else False
                    elif event.key == py.K_c:
                        x = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        self.colors.append(x)
                        self.color = x
                    if event.key == py.K_UP:
                        if self.speed >= 0.1:
                            self.speed -= 0.1
                    elif event.key == py.K_DOWN:
                        self.speed += 0.1
                    elif event.key == py.K_LEFT:
                        self.color = self.colors[self.colors.index(self.color) -1] if self.colors.index(self.color) else self.colors[len(self.colors) - 1]
                    elif event.key == py.K_RIGHT:
                        self.color = self.colors[self.colors.index(self.color) + 1] if self.colors.index(self.color) != len(self.colors) -1 else self.colors[0]
                    elif event.key == py.K_r:
                        for i in self.board:
                            for j in i:
                                if not random.randint(0, 2):
                                    j.isAlive = True
                        self.draw(self.cellSize, self.cellSize)
                    [
                        py.draw.rect(self.screen,
                                                 self.color, j.rect) if j.isAlive else py.draw.rect(
                                                     self.screen, (255, 255, 255), j.rect)
                        for i in self.board for j in i
                    ]
                    py.display.flip()
                elif self.paused and event.type == py.MOUSEBUTTONUP:
                    position = py.mouse.get_pos()
                    self.board[position[1] // self.cellSize][
                        position[0] // self.cellSize].isAlive = True if self.board[
                            position[1] //
                            self.cellSize][position[0] //
                                                         self.cellSize].isAlive == False else False
                    self.draw(self.cellSize, self.cellSize)
                    [
                        py.draw.rect(self.screen,
                                                 self.color, j.rect) if j.isAlive else py.draw.rect(
                                                     self.screen, (255, 255, 255), j.rect)
                        for i in self.board for j in i
                    ]
                    py.display.flip()

            if not self.paused:
                self.update()
                self.draw(self.cellSize, self.cellSize)
                [
                    py.draw.rect(self.screen, self.color, j.rect)
                    if j.isAlive else py.draw.rect(self.screen, (255, 255, 255), j.rect)
                    for i in self.board for j in i
                ]
                py.display.flip()
                sleep(self.speed)

    def draw(self, boxHeight: int, boxWidth: int):
        x = 0
        y = 0
        self.screen.fill((255, 255, 255))
        for i in range(len(self.board)):
            x += boxWidth
            y += boxHeight
            py.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.width))
            py.draw.line(self.screen, (0, 0, 0), (0, y), (self.width, y))
