from PIL import Image
from PIL.ExifTags import TAGS

im = Image.open( "sample.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in im._getexif().items()
    if k in TAGS
}