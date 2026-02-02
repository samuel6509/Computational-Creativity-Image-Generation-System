# logic for choosing the colour pallete of the scene
# may have to give the 12 colours values that the project can process rather than their name value

# TODO:
# 1. defined the 12 colours in the lexicon in hex and rgb values -- COMPLETE
# 2. loop through tokens in user input to see if they have a colour associated with them -- COMPLETE
# 3. if they do then tag them with the clour -- COMPLETE

from word_processing import user_input

# function defining the 12 colours found in the lexicon as hex values
def hex_colours():
    # hex values for the 12 colours
    hex_values = {
        'white': '#FFFFFF',
        'black': '#000000',
        'red': '#FF0000',
        'green': '#00FF00',
        'yellow': '#FFFF00',
        'blue': '#0000FF',
        'brown': '#8B4513',
        'pink': '#FFC0CB',
        'purple': '#800080',
        'orange': '#FFA500',
        'grey': '#808080',
    }
    return hex_values

#  function defining the 12 colours of the lexicon in rgb values
def colours():
    # rgb values for the 12 colours
    rgb_values = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'blue': (0, 0, 255),
    'brown': (139, 69, 19),
    'pink': (255, 192, 203),
    'purple': (128, 0, 128),
    'orange': (255, 165, 0),
    'grey': (128, 128, 128),
}
    return rgb_values

# function to get colour associated with each token
def colour_association():
    # path to word colour association text file
    filepath = 'source_code/NRC-color-lexicon-NONsenselevel-v0.92.txt'
    # tokens from user input
    input = user_input()
    # gets the hex values for the colours
    hex_values = hex_colours()
    # gets the rgb values for the colours
    rgb_values = colours()
    # stores the colours associated with tokens
    associations = {}

    # opens the lexicon file
    with open(filepath, 'r', encoding='utf-8') as file:
        # break up every line into 2 parts
        for line in file:
            parts = line.strip().split('\t')
            word = parts[0]
            colour = parts[1]
            # if word in lexicon matches user input
            if word in input:
                rgb_value = rgb_values.get(colour)
                # if word is already in associations
                if word in associations:
                    # if the specific colour is not associated with the word
                    if rgb_value not in associations[word]:
                        # associate it
                        associations[word].append(rgb_value)
                # must be a new association
                else:
                    associations[word] = [rgb_value]

    # print nicely
    for word, colour in associations.items():
        print(f"{word}: {', '.join(str(c) for c in colour)}")
    # print(associations)

    #  collect all colours from associations
    collected_colours = [c for colour in associations.values() for c in colour]
    print('Collected colours: ', collected_colours)
    return collected_colours, associations, input
    # print(associations)
    # return associations
   
# function to test getting the data from word_processing file to be used in this file
def test():
    test = user_input()
    print(test)

# user_input()
# test()
# colour_association()