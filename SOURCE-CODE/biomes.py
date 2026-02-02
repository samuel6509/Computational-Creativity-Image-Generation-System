# the logic for making the basic biomes which will make up the image

# TODO:
# 1. create the biomes
# 2. add all the biomes to the canvas
# 3. add biomes one at a time to the canvas
# 4. let the users input decide which biomes are present
# 5. let the user decide which colours are present on the image / biomes

# map biomes to words -- COMPLETE
# map colours to words from lexicon -- COMPLETE
# map words to synonyms -- COMPLETE
# make a def for each biome -- COMPLETE
# add the logic for adding biomes to canvas in a realisistc order -- COMPLETE

# IF I HAVE EXTRA TIME:
# FINISH STARS -- COMPLETE
# ADD PARAMETERS INTO THE PASSABLE VARIABLES IN FUNCTION CALLS -- COMPLETE
# ADD RAIN CLOUDS AND RAIN AND LIGHTNING
# ADD SNOW FALLING

import noise
from noise import pnoise2
import random
from PIL import ImageDraw
from canvas import Canvas

# importing functions from other files
from colour_pallete import colour_association
from trees import generate_trees

colour_pallete, word_colour_associations, users_input = colour_association()
print(users_input)
print(word_colour_associations)
print(colour_pallete)

# the biomes for generation
# maybe add clear as a biome which means no clouds
# maybe add a sky and moon biome which links with day and night 
biomes = [
    "sky", # -- IN PROGRESS
    "sun", # -- IN PROGRESS
    "night", # nights after sky to override it # -- IN PROGRESS
    "moon", # -- IN PROGRESS
    "stars", # -- IN PROGRESS
    "clouds", # -- IN PROGRESS -- add dark clouds and rain?
    "forest", # -- IN PROGRESS
    "desert", # -- IN PROGRESS
    "snow", # -- IN PROGRESS -- add snow effect
    "mountain", # -- COMPLETE
    "water", # -- IN PROGRESS
]

# synonyms for biomes
synonyms = {
    "sky": ["skies"],
    "sun": ["sunny", "sunlight", "hot", "summer"],
    "night": ["midnight", "nighttime"],
    "clouds": ["cloud", "cloudy", "overcast", "cloudiness"],
    "moon": [], # -- NEEDS COMPLETING
    "stars": ["star"], # -- NEEDS COMPLETING
    "forest": ["woodland", "woods", "jungle", "trees", "tree"],
    # "desert": ["dunes", "sand", "sandy"],
    "snow": ["ice", "icy", "frost", "frosty", "snowy", "freezing"],
    "mountain": ["hill", "peak", "summit", "mountains"],
    # "water": ["ocean", "sea", "lake", "river"],
}

# function to get the biomes and the colour for generation
def biome_colour_associations(word_colour_associations):
    biomes_colours = {}

    # loop through
    for biome, colours in word_colour_associations.items():
        # if word is in biomes list
        if biome in biomes:
            # if it has a colour associated
            if colours:
                biomes_colours[biome] = colours[0]  # CHANGE AT A LATER DATE, account for multiple colours
        else:
            for syn_biome, syns in synonyms.items():
                # if the user input is a synonym for one of the biomes
                if biome in syns:
                    if colours:
                        biomes_colours[syn_biome] = colours[0] # CHANGE AT A LATER DATE, account for multiple colours

    print(biomes_colours)
    return biomes_colours

# function to be used in self evaluation file
def get_biome_colour_associations():
    biome_colour = biome_colour_associations(word_colour_associations)
    return biome_colour

# function to generate the sky -- COMPLETE
def generate_sky():
    # get the colour associated with sky
    colour = biome_colour_associations(word_colour_associations)
    colour = colour.get('sky')
    print(colour)
    return colour

# function to generate the night sky -- COMPLETE
def generate_night_sky():
    # get colour associated with night 
    colour = biome_colour_associations(word_colour_associations)
    colour = colour.get('night')
    print(colour)
    return colour

#  function to generate clouds -- IN PROGRESS -- add rain clouds
def generate_clouds(canvas, scale = 0.01, octaves = 5, persistence = 0.5, lacunarity = 2.0):
    colour = biome_colour_associations(word_colour_associations)
    colour = colour.get('clouds')
    print(colour)

    # canvas configuration
    # scale = 0.01
    # octaves = 5
    # persistence = 0.5
    # lacunarity = 2.0

    width, height = canvas.width, canvas.height #  cloud limits
    pixels = canvas.image.load() # add clouds to image

    offset = random.randint(0, 1000) # changes cloud pattern
    cutoff = 0.2 # 0.42 # distinguish between clouds and other parts of the image

    for y in range(height):
        for x in range(width):
            # deciding where cloud will be 
            cloud_x = x * scale
            cloud_y = y * scale 
            # the noise value for cloud
            p_noise_val = pnoise2(
                cloud_x, cloud_y,
                octaves = octaves,
                persistence = persistence,
                lacunarity = lacunarity,
                repeatx = 1024, repeaty = 1024,
                base = offset
            )
            normalized = (p_noise_val +1) / 2 # between 0 and 1 

            # blurring effect
            if normalized > cutoff:
                # trying different things to get clouds to be bolder
                # transparency = int((normalized - cutoff) / (1 - cutoff) * 255)
                transparency = int(((normalized - cutoff) / (1 - cutoff)) * 255 * 1.2)
                transparency = min(transparency, 255)

                r, g, b = colour
                current_pixel = pixels[x, y]
                blurred = tuple(
                    int((1 - transparency / 255) * current + (transparency / 255) * new)
                    for current, new in zip(current_pixel, (r, g, b))
                )
                pixels[x, y] = blurred

# function to generate mountains -- COMPLETE
def generate_mountains(canvas, scale = 0.01, texture_scale = 0.1, amplitude = 200, starting_height = 500):
    colour = biome_colour_associations(word_colour_associations)

    # getting the mountains colour
    mountain_colour = colour.get('mountain')
    print(colour)

    # get the colours of other biomes which can appear on mountains
    forest_colour = colour.get('forest')
    if forest_colour:
        print('forest included: ', forest_colour)
    snow_colour = colour.get('snow')
    if snow_colour:
        print('snow included: ', snow_colour)

    # canvas configuration
    # scale = 0.01 # how many and how wide hills can go
    # texture_scale = 0.1
    # amplitude = 200 # how high the hills can go 
    # starting_height = 500 # where the hills start

    width, height = canvas.width, canvas.height # width and height of th canvas
    pixels = canvas.image.load() # adds mountains to the image
    mountain_point = [0] * width # used to record the highest point of mountains

    # starting parameters for mountains
    baseline = random.randint(0, 10000)
    offset = random.uniform(0, 1000)
    texture_baseline = random.randint(0, 10000)

    for x in range(width):
        mountain_y = int(noise.pnoise1(x * scale + offset, base = baseline) * amplitude + starting_height)
        mountain_point[x] = mountain_y # recording the top of each mountain

        for y in range(mountain_y, height):
            p_noise_val = pnoise2(
                x * texture_scale,
                y * texture_scale,
                base = texture_baseline
            )
            variation = int(p_noise_val * 20)

            # adding the texture to the mountains
            r, g, b = mountain_colour
            r = max(0, min(255, r + variation))
            g = max(0, min(255, g + variation))
            b = max(0, min(255, b + variation))

            # adds the grass layer
            if forest_colour and y < mountain_y + 40:
                fr, rg, fb = forest_colour
                r = (r + fr) // 2
                g = (g + rg) // 2
                b = (b + fb) // 2

            # adds the snow layer
            if snow_colour and y < mountain_y + 10:
                r, g, b = snow_colour

            # adding mountains to the image
            pixels[x, y] = (r, g, b)
            
    # adding trees
    if forest_colour:
        generate_trees(canvas, mountain_point, count = 15, snow = False)
    if snow_colour:
        generate_trees(canvas, mountain_point, count = 5, snow = True)
    # generate_trees(canvas, mountain_point, count = 10)

# function to generate the sun or the moon -- COMPLETE
def generate_sun_or_moon(canvas, position = None, radius = 50, full_moon = False):
    # draws on the canvas
    draw = ImageDraw.Draw(canvas.image)
    # getting the colour of the sun and moon
    colour = biome_colour_associations(word_colour_associations)
    colour_sun = colour.get('sun')
    colour_moon = colour.get('moon')

    # getting the width and hieght of the canvas
    width, height = canvas.width, canvas.height

    # if not position defined
    if position == None:
        # top right of the image
        x = random.randint(width * 2 // 3, width - radius)
        y = random.randint(0, height // 3)
    # must already be a position defined
    else:
        x, y = position

    left_up = (x - radius, y - radius)
    right_down = (x + radius, y + radius)

    # generating sun
    if colour_sun:
        draw.ellipse([left_up, right_down], fill = colour_sun)

    # generating moon
    if colour_moon and full_moon:
        draw.ellipse([left_up, right_down], fill = colour_moon)
    # if not full moon then half moon
    if colour_moon and not full_moon:
        draw.ellipse([left_up, right_down], fill = colour_moon)
        # shadow covering part of the moon
        shadow_left_up = (x, y - radius)
        shadow_right_down = (x + radius, y + radius)
        draw.ellipse([shadow_left_up, shadow_right_down], fill=(0, 0, 0))

    return(x, y)

# function to generate stars when night and stars is present -- COMPLETE
def generate_stars(canvas, density = 0.002):
    # getting colour of stars
    colour = biome_colour_associations(word_colour_associations)
    colour = colour.get('stars')
    print('stars colour: ', colour)

    pixels = canvas.image.load()
    width, height = canvas.width, canvas.height

    # generating stars on top half of image
    for y in range(height):
        for x in range(width):
            if random.random() < density:
                r,g,b = colour
                pixels[x, y] = (r, g, b)

# main function in this file, used to generate the image in the right way -- IN PROGRESS
def generate_biomes():
    words = biome_colour_associations(word_colour_associations)
    biomes_colours = words

    # if night is present
    if 'night' in words:
        background_colour = generate_night_sky()
        canvas = Canvas(1024, 768, background_colour)
        if 'moon' in words:
            generate_sun_or_moon(canvas)
        if 'stars' in words:
            generate_stars(canvas)

    # if no night then check if sky / day is present
    elif 'sky' in words:
        background_colour = generate_sky()
        canvas = Canvas(1024, 768, background_colour)
        if 'sun' in words:
            generate_sun_or_moon(canvas)

    # if no time of day are mentioned
    else:
        canvas = Canvas(1024, 768, (173, 216, 230)) #light blue

    if 'clouds' in words:
        generate_clouds(canvas)

    if 'mountain' in words:
        generate_mountains(canvas)

    return canvas, biomes_colours

# biome_colour_associations(word_colour_associations)
# generate_sky()