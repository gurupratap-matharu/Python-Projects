import random
import pdb
pdb.set_trace()

def random_walk(n):
        '''Return the coordinates after 'n' blocks of random walk.'''
        x,y = 0,0

        for i in range(n):
            '''Loops for n blocks and calculates the final x and y coordinates'''                
            step = random.choice(['N','S','W','E'])
            if step == 'N':
                y += 1
            elif step == 'S':
                y -= 1
            elif step == 'E':
                x += 1
            else:
                x -= 1

        return (x,y)

for i in range(25):
    walk = random_walk(20)
    print(walk, "Distance from home {}".format(abs(walk[0])+abs(walk[1])))

