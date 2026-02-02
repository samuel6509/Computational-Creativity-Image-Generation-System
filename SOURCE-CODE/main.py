# the main file for this project
# where the main functions will be called 

# import random
# # importing functions from other files
# from colour_pallete import colour_association
# from canvas import Canvas
# from biomes import generate_sky, generate_night_sky, generate_clouds, generate_mountains, generate_sun_or_moon, generate_biomes
# from trees import generate_trees

# colour_pallete, word_colour_associations, users_input = colour_association()
# print(users_input)
# print(word_colour_associations)
# print(colour_pallete)

# REMEMBER -- when creating final generation function use this heirarchy
# background_colour = generate_sky()
# canvas = Canvas(1024, 768, background_colour)
# generate_sun_or_moon(canvas)
# generate_clouds(canvas)
# generate_mountains(canvas)
# # generate_trees(canvas)
# canvas.show()

# background_colour = generate_night_sky()
# canvas2 = Canvas(1024, 768, background_colour)
# canvas2.show()

# sky clouds mountain forest snow sun
# clouds mountain forest snow night moon stars

# Sunny skies with clouds all over
# Sunny skies with clouds all over with mountains with trees on them 

# night sky with moon, stars and clouds visible
# night sky with moon, stars and clear skies with mountains with trees and snow on them

# bright sky, beaming sun filled with tons of fluffy clouds
# bright sky, beaming sun filled with tons of fluffy clouds, looking over mountains containing forests within

# quite night sky, full of stars, clouds and a moon behind them
# quite night sky, full of stars and a moon behind them, with a snowy mountain range 

from biomes import generate_biomes
from self_evaluation import evaluate_image

canvas, biomes_colours = generate_biomes()
canvas.show()
evaluate_image(biomes_colours, canvas)
canvas.save()