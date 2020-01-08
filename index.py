import pygame
import random

# Variables:
screen_width = 1000
screen_height = 1000
size = (screen_width, screen_height)
title = 'A bubble sort algorithm'
amount_of_bars = 30

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

y_level = screen_height - 100

class Bar():
    def __init__(self, x, width, height, color = BLACK):
        self.x = x
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        # Make the bar that will be drawn
        margin = self.width * 0.05
        width = self.width - 2 * margin
        # Draw a black  rectangle to clear the previous bar
        clear_rectangle = pygame.Rect(self.x+margin, 0, width, screen_height)
        pygame.draw.rect(screen, BLACK, clear_rectangle)
        rectangle = pygame.Rect(self.x+margin, y_level-self.height, width, self.height)
        # Draw the rectangle
        pygame.draw.rect(screen, self.color, rectangle) 

    
def createBars(screen):
    # Create the bar objects
    width = screen_width / amount_of_bars
    bars = []
    for i in range(0, amount_of_bars):
        height = i*30
        x = i*width
        bar = Bar(x,width,height,WHITE)
        bar.draw(screen)
        bars.append(bar)
    return bars

def shuffle(screen, clock, bars, shuffle_times):
    # shuffle the bars into a random order
    width = screen_width / amount_of_bars

    for i in range(0, shuffle_times):
        print('shuffeling for the %dth time'% i)
        index_1 = random.randint(0,len(bars)-1)
        index_2 = index_1
        while index_2 == index_1:
            index_2 = random.randint(0,len(bars)-1)

        switch_bars(screen, clock, bars, index_1, index_2)


    return bars

def switch_bars(screen, clock, bars, index_1, index_2):
    # Caclulate the bar width
    width = screen_width / amount_of_bars
    # switch bars in the bars array
    bars[index_1], bars[index_2]  = bars[index_2], bars[index_1]
    # Update the x position for both bars
    bars[index_1].x = width*index_1
    bars[index_2].x = width*index_2
    # Re draw bars in new position
    bars[index_1].draw(screen)
    bars[index_2].draw(screen)
    pygame.display.flip()
    clock.tick(10)



def main():
    # Main game loop

    # Start pygame screen and clock
    pygame.init()
    # Set screen size
    screen = pygame.display.set_mode(size)
    # Alternative screen size to easily debug drawing issues
    #screen = pygame.display.set_mode((1000,1000))
    # Set dispaly captionn
    pygame.display.set_caption(title)
    # Define the clock
    clock = pygame.time.Clock()

    bars = createBars(screen)
    pygame.display.flip()
    clock.tick(5)

    bars = shuffle(screen,clock, bars, 15)
    for i in range(0, 5):
        clock.tick(10)
    fully_sorted = False
    # Sort
    while fully_sorted == False:
        switched = False
        for i in range(0, len(bars)-1):
                if bars[i].height > bars[i+1].height:
                    switch_bars(screen, clock, bars, i, i+1)
                    switched = True
        if switched is not True:
            fully_sorted = True
    print('Done')
                    

    while True:
        pass

     

if __name__ == "__main__":
	main()
