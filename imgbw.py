from PIL import Image 
image_file = Image.open("gfx/partlycloudy.gif") # open colour image
#image_file = image_file.resize((100,100),Image.ANTIALIAS)
image_file = image_file.convert('L') # convert image to black and white
image_file.save('result.png')
image_file = Image.open("result.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.gif')