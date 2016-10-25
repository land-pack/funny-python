import sys

from time import *
from PIL import Image

class ImageTool(object):
	def __init__(self):
		print 'init something ..'
	
	def get_chars(self, image_pixels, image_width, image_height):
		replace_chars = 'ABCDEFGHIJKLMNO '
		terminal_chars = ''
		for h in xrange(image_height):
			for w in xrange(image_width):
				point_pixel = image_pixels[w, h]
				terminal_chars += replace_chars[int(sum(point_pixel)/3.0/256.0*16)]
			terminal_chars+='\n'
		return terminal_chars
	
	def format_image(self, imagename, image_width, image_height):
		img = Image.open(imagename, 'r')
		if img.mode != 'RGB':
			img = img.convert('RGB')
		w, h = img.size
		rw = image_width * 1.0 / w
		rh = image_height* 1.0/h
		r  = rw if rw < rh else rh
		rw = int(r * w)
		rh = int(r * h)
		img = img.resize((rw, rh), Image.ANTIALIAS)
		return img

	def entrance(self, image_path, out_width, out_height):
		image = self.format_image(imagename = image_path, image_width = out_height, image_height = out_height)
		image_pixels = image.load()
		out_width, out_height = image.size
		terminal_chars = self.get_chars(image_pixels = image_pixels, image_width= out_width, image_height= out_height)
		print terminal_chars 

if __name__ == "__main__":
	tool = ImageTool()
	imagename = sys.argv[1]
	w = int(sys.argv[2])
	h = int(sys.argv[3])
	tool.entrance(imagename, w, h)
