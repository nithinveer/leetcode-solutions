from collections import  deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = food
        self.height = height
        self.width = width
        self.idx = 0
        self.pipe = deque([[0,0]])
        self.snake = set()
        self.snake.add('0#0')
        self.piv = [0,0]
        self.score = 0
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if (direction == 'U'):
            self.piv[0] -=1
        if (direction == 'L'):
            self.piv[1] -=1
        if (direction == 'R'):
            self.piv[1] += 1
        if (direction == 'D'):
            self.piv[0] += 1

        poped = self.pipe.pop()
        self.snake.remove(str(poped[0]) + '#' + str(poped[1]))

        if  self.piv[0] <0 or self.piv[0]>= self.height or self.piv[1] <0 or self.piv[1] >=self.width or str(self.piv[0]) + '#'+ str(self.piv[1]) in self.snake:
            return -1
        elif self.idx < len(self.food) and self.piv == self.food[self.idx] :
            self.score +=1
            self.pipe.append(poped)
            self.snake.add(str(poped[0]) + '#' + str(poped[1]))
            self.idx+=1
        self.pipe.appendleft(self.piv[:])
        self.snake.add(str(self.piv[0]) + '#' + str(self.piv[1]))
        return  self.score
            



width = 3
height = 3
food = [[2,0],[0,0],[0,2],[2,2]]
snake = SnakeGame(width, height, food)
print(snake.move("D")) #[1,0] 0
print(snake.move("D"))
print(snake.move("R"))
print(snake.move("U"))
print(snake.move("U"))
print(snake.move("L"))
print(snake.move("D"))
print(snake.move("R"))
print(snake.move("R"))
print(snake.move("U"))
print(snake.move("L"))
print(snake.move("D"))