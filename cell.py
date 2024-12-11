import pygame

class Cell:
    def __init__(self, x: int, y: int, size: int):
        self.pos = [x, y]
        self.isAlive = False
        self.will = False
        self.rect = pygame.Rect(x * size + 1, y * size + 1, size - 1, size - 1)

    def willLive(self, board: list):
        around = self.around(board)
        count = 0
        for i in around:
            if i:
                count += 1
        if count == 3:
            self.will = True
        elif count == 2:
            self.will = True if self.isAlive else False
        else:
            self.will = False

    def around(self, board: list):
        return [board[r][c].isAlive for r in range(self.pos[1] - 1, self.pos[1] + 2) for c in range(self.pos[0] - 1, self.pos[0] + 2) if (r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and [c, r] != self.pos)]

"""
Translation into readable txt:
thing = []
        for r in range(self.pos[1] - 1 , self.pos[1] + 2): #2 3 4
            for c in range(self.pos[0] - 1, self.pos[0] + 2): # 3 4 5
                if (r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and [c,r] != self.pos):
                    thing.append(board[r][c].isAlive)
        return thing
"""