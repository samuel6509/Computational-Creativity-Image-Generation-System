#  the logic for creating trees, to be used in biomes for image generation
# using L system to generate trees

# TODO:
# 1. create a L system function -- COMPLETE
# 2. create a tree generation function -- COMPLETE
# 3. make tree brown make leaves green -- COMPLETE
# 4. improve the way the colours are represented on the tree -- COMPLETE

# IMPORTANT THINGS TO REMEMBER:
# + means turn right
# - means turn left
# [ means save current pos
# ] means returns to current saved pos / [

import random
import math

# function that defines the l system
def l_system():
    # variables used for L system config
    axiom = "F" # starting point
    rules = {"F": "F[+F]F[-F]F"} # rules followed by the L system
    iterations = 4 # number of times it runs -- change for different looking trees 
    # iterations = random.randint(3, 6)

    # result begins at the startping point
    result = axiom
    for i in range(iterations):
        next_result = ''
        for char in result:
            next_result += rules.get(char, char)
        result = next_result
    return result

# function which creates a tree 
def draw_tree(canvas, x, y, l_system, angle, length, snow):
    pixels = canvas.image.load()
    bookmark = [] # where the current pos it saved and restored from / [ or ] 
    current_position = (x, y)
    current_angle = -90

    for char in l_system:
        # moving forwards
        if char == 'F':
            # adding randomness to trees
            new_length = length + random.uniform(-1.5, 1.5)
            radians = math.radians(current_angle)
            current_x = int(current_position[0] + new_length * math.cos(radians))
            current_y = int(current_position[1] + new_length * math.sin(radians))

            difference_x = current_x - current_position[0]
            difference_y = current_y - current_position[1]
            # measure how steps it will take to go from current to new co ords
            steps = max(abs(difference_x), abs(difference_y))
            if steps == 0: 
                continue
            for step in range(steps):
                # calculates the difference between current and target pos 
                px = int(current_position[0] + step * difference_x / steps)
                py = int(current_position[1] + step * difference_y / steps)
                if 0 <= px < canvas.width and 0 <= py < canvas.height:
                    if snow:
                        pixels[px, py] = (139, 69, 19) # all brown dead trees
                    else:
                        if new_length < length:
                            pixels[px, py] = (139, 69, 19) # brown
                        else:
                            pixels[px, py] = (34, 139, 34) # green

            current_position = (current_x, current_y)

        # turning right
        elif char == '+':
            current_angle += angle + random.uniform(-5, 5) 
        # turning left
        elif char == '-':
            current_angle -= angle + random.uniform(-5, 5)
        # save current pos
        elif char == '[':
            bookmark.append((current_position, current_angle))
        # restore to the current saved pos / [
        elif char == ']':
            current_position, current_angle = bookmark.pop()

# function to generate all trees to be added to canvas
def generate_trees(canvas, mountain_point, count, snow = False):
    l_system_ouput = l_system()
    # count = 25 # number of trees to be generated -- CHANGE IF WANT MORE TREES
    # making sure treees are at the top of mountains
    for i in range(count):
        x = random.randint(50, canvas.width - 50)
        y = mountain_point[x] + random.randint(0, 15)
        angle = random.randint(20, 30)
        length = random.randint(1, 3)
        draw_tree(canvas, x, y, l_system_ouput, angle, length, snow)