from skimage.measure import regionprops
from bwmorph import pixelsFilled


def bwconncomp(BW, conn):
    region = regionprops(BW)[0]
    dimensions = BW.shape

    result = []

# TODO Assert there is only one region
    for coord in region.coords:
        print("coord:", coord)

        if(pixelsFilled(coord[0], coord[1], BW, dimensions[0], dimensions[1]) == conn + 1):
            result.append(coord)

    return result




