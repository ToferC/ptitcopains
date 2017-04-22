from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('carecentres:thumbnail', Thumbnail)