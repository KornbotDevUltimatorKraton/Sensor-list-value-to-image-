import numpy as np 
from PIL import Image as im 
lst  = [240,255,250,61,62,63,0,210,165,70]
array = np.array(lst)
array = array.astype(np.uint8)
array = np.reshape(array, (5,2)) 
data = im.fromarray(array)
data.save('test_image.png')
