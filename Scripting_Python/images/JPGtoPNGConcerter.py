import sys
import os #to grabs the path
from PIL import Image


# grab the first argument the folder to look in for jpg image
#use the second arguemnt to create the new folder and save the converted images

path = sys.argv[1]
directory = sys.argv[2] #the folder to be created

if not os.path.exits(directory)
    os.makedirs(directory) #if does not exist then create the folder
    
    
for filename in os.listdir(path) #loop thorugh the num items in the pokedex folder
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done')