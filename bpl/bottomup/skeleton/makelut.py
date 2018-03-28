import numpy as np
import scipy.ndimage as ndimage
from PIL import Image

# filename = '/tmp/PerformErosionUsingA2by2NeighborhoodExample_01.png'
# img = Image.open(filename).convert('L')
arr = np.array(img)
def func(x):
    return (x==255).all()*255

arr2 = ndimage.generic_filter(arr, func, size=(2,2))
new_img = Image.fromarray(arr2.astype('uint8'), 'L')
# new_img.save('/tmp/out.png')


