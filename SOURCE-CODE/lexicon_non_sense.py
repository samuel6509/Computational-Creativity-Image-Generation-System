# logic for using the sense version of the lexicon to make the non sense version as I cant find it anywhere
#  this is the link to the page where I got the word colour association lexicon from
# https://saifmohammad.com/WebPages/lexicons.html

inputfile = 'source_code/NRC-color-lexicon-senselevel-v0.92.txt'
outputfile = 'source_code/NRC-color-lexicon-NONsenselevel-v0.92.txt'

# function to extract word and colour associations and add them to the output file
def word_color_extraction(inputfile, outputfile):
    with open(inputfile, 'r', encoding='utf-8') as input, \
         open(outputfile, 'w', encoding='utf-8') as output:
        # go through every line in the input file
        for line in input:
            #  move past these lines
            if line.startswith('NRC') or line.startswith('Version') or line.startswith('>'):
                continue
            #  split lines into parts 
            parts = line.strip().split('\t')
            # if there less than 2 parts skip the line
            if len(parts) < 2:
                continue
            word_part = parts[0]
            colour_part = parts[1]
            #  if theres no colour associated then skip the line
            if 'Colour=None' in colour_part:
                continue
            #  gets the word before the -- and the colour after the =
            word = word_part.split('--')[0].lower()
            colour = colour_part.split('=')[1].lower()
            # add this as a new line in the output file
            output.write(f'{word}\t{colour}\n')

word_color_extraction(inputfile, outputfile)