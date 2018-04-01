class Image(object):
    """Base class for images."""

    def __init__(self, height, width):
        self.height, self.width = height, width

    def dimensions(self):
        return (self.height, self.width)
