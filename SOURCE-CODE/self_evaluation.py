# hypothetical atm
# logic for system to self evaluate and make changes to the image to best suit users taste
# based off coltons tripod system for evaluation

# TODO:
# 1. add function(s) to evaluate the image 
# 2. get users feedback on the image
# 3. make functions to change parts of image, basically alter biomes / colours / clouds sun moon etc

# was the image perfect? Yes or no -- if anything else then throw error and ask for yes or no again
# what was wrong with the image, print each part of the word colour associations to show all parts of image
# know what parts were wrong are known iether ask for specifics or just alter the things and generate it as a new image
# ask user to compare before and after and ask if this is okay 
# ask for yes and no again -- if yes save image -- if no go back to previous step and try again

# 1. if image is perfect then go to step 9
# 2. what part did you not like?
# 3. if part is not in list then list all the parts
# 4. ask what was wrong with that part
# 5. change that part
# 6. ask if this is better
# 7. back to step 1
# 8. if unhappy back to step 1
# 9. if happy with it then save the image and retunr or break 

import random
from PIL import Image, ImageEnhance
from biomes import get_biome_colour_associations, generate_sun_or_moon, generate_sky, generate_night_sky

# holds common issues for each biome
biome_issues = {
    'sky': ['too bright', 'too dark'],
    'night': ['too bright', 'too dark'],
    # 'sun': ['too left', 'too right', 'too big', 'too small', 'too bright', 'too dark'],
    # 'moon': ['too left', 'too right', 'too big', 'too small', 'too bright', 'too dark'],
    'stars': ['too many', 'too little', 'too bright', 'too dark', 'wrong colour'],
    # 'clouds': ['too many', 'too little'],
    # 'trees': ['not enough'],
}

def evaluate_image(biomes_colours, canvas):
    changed_parts = [] # keep track of what parts have been changed

    while True:
        #  STEP 1 -- ask if the image is perfect as is
        perfect = input('Is the image perfect for you? (y/n): ').lower()
        if perfect == 'y':
            print('Perfect! Glad you like it!')
            #  STEP 9 -- evaluation is finished, call the save function from canvas
            break

        elif perfect == 'n':
            # STEP 2 -- ask what part they did not like
            biomes = list(biomes_colours.keys())

            # if there are no parts to change
            if not biomes:
                print('Nothing found to change')
                return
            
            # print the parts of the image available to change 
            print('What part were you unhappy with? Please enter the number:')
            for number, part in enumerate(biomes, start = 1):
                print(f'{number}. {part}')

            while True:
                try:
                    choice = int(input('> '))
                    if 1 <= choice <= len(biomes):
                        disliked_part = biomes[choice - 1]
                        break
                    # error handling for invalid inputs
                    else:
                        print('Please enter a number from the given list')
                except ValueError:
                    print('Please input a number')

            # STEP 4 -- ask whats wrong with the part
            problem = biome_issues.get(disliked_part, [])
            if problem:
                print(f'what is wrong with the {disliked_part}? Please enter the number:')
                for number, issue in enumerate(problem, start = 1):
                    print(f'{number}. {issue}')

                while True:
                    try:
                        selected_issue = int(input('> '))
                        if 1 <= selected_issue <= len(problem):
                            choice = problem[selected_issue - 1]
                            break
                        else:
                            print('Please enter a number from the given list')
                    except ValueError:
                        print('Please input a number')
            # the parts currently available to change 
            if disliked_part == 'sky':
                change_sky(choice, canvas)

            elif disliked_part == 'night':
                change_sky(choice, canvas)

            elif disliked_part == 'stars':
                change_stars(choice, canvas)
        # error handling 
        else:
            print('Please choose y or n: ')

# function to change the sky
def change_sky(issue, canvas):
    pixels = canvas.image.load()
    width, height = canvas.width, canvas.height

    # lowering or birghtening each pixel of the canvas / sky / night sky
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if issue == 'too bright':
                r = max(0, r - 30)
                g = max(0, g - 30)
                b = max(0, b - 30)

            elif issue == 'too dark':
                r = min(255, r + 30)
                g = min(255, g + 30)
                b = min(255, b + 30)
            pixels[x, y] = (r, g, b)

    canvas.show()

# function to change the stars
def change_stars(issue, canvas, amount = 0.5, count = 200):
    pixels = canvas.image.load()
    width, height = canvas.width, canvas.height

    # change pixels which are stars back to the colour of the night sky
    if issue == 'too many':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if r > 200 and g > 200 and b > 100 and random.random() < amount:
                    pixels[x, y] = (0, 0, 0)
    # change pixels which are night sky to stars
    elif issue == 'too little':
        for i in range(count):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pixels[x, y] = (255, 255, 255)

    # BUG -- not working when you make stars brighter
    elif issue == 'wrong colour':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if (r, g, b) == (255, 255, 255):
                    pixels[x, y] = (255, 255, 0) # yellow

                elif (r, g, b) == (255, 255, 0):
                    pixels[x, y] = (255, 255, 255) # white 

    # lwoers brightness of stars
    elif issue == 'too bright':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if r > 200 and g > 200 and b > 200:
                    r = max(0, r - 100)
                    g = max(0, g - 100)
                    b = max(0, b - 100)
                    pixels[x, y] = (r, g, b)

    # increases brightness of stars
    elif issue == 'too dark':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if r < 200 and g < 200 and b < 200:
                    r = min(255, r + 100)
                    g = min(255, g + 100)
                    b = min(255, b + 100)
                    pixels[x, y] = (r, g, b)

    canvas.show()