# logic for creating the canvas that the image parts will generate onto 

# TODO:
# 1. create the canvas -- COMPLETE
# 2. get the canvas to show -- COMPLETE
# 3. get the canvas to save -- COMPLETE
# 4. add colours from user input to the canvas -- COMPLETE
# 5. save the canvas -- COMPLETE

from PIL import Image, ImageDraw
import os

class Canvas:
    # function to create the canvas
    def __init__(self, width, height, background_color):
        # width, heigh and colour of canvas
        self.width = width
        self.height = height
        self.background_color = background_color

        # creates the canvas
        self.image = Image.new('RGB', (width, height), background_color)
        self.draw = ImageDraw.Draw(self.image)
        # self.image.show()
    
    # function to show the canvas
    def show(self):
        self.image.show()

    # function to save the canvas
    def save(self):
        while True:
            # ask if image wants to be saved
            choice = input('Do you want to save the image? (y/n): ').lower()

            if choice == 'y':
                while True:
                    name = input('Enter the name you want for your image: ').replace(' ', '_')
                    # if yes but no name is given ask again
                    if not name:
                        print('\nName cannot be empty, please try again')
                        continue # back to the start of while loop

                    filename = name + '.png' # save as png

                    if os.path.exists(filename):
                        print(f'\nA file named {filename} already exists, please enter a new name')
                        continue # back to start of while loop

                    self.image.save(filename)
                    print(f'Image saved as {filename}') # tell user what they are looking for 
                    break
                break

            elif choice == 'n':
                print('\nImage not saved')
                break

            # if nothing or random input given then ask again
            else:
                print('\nPlease choose y or n')