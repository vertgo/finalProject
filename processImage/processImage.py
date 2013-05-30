from PIL import Image
from PIL.ExifTags import TAGS
import numpy

def exifStuff():
	im = Image.open( "sample.jpg")

	exif = {
	    PIL.ExifTags.TAGS[k]: v
	    for k, v in im._getexif().items()
	    if k in TAGS
	}

def openImage( inFilename ):
	try:
		im = Image.open( "images/" + inFilename )
		#width, height = im.size
		return im
	except:
		return None

#size is aspect ratio, totalPixels, width, height

def populateSizeFields( inImageName ):
	try:
		im = Image.open( "images/" + inImageName )
		width, height = im.size
		aspect = float( width) / float( height )
		pixels = width * height
		return pixels, aspect
	except:
		return numpy.nan, numpy.nan