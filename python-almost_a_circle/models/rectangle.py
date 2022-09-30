#!/usr/bin/python3
"""
	Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
	"""
		This class creates a rectangle.
	"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""
			Args:
				width (int): is the width of the rectangle
				height (int): is the height of the rectangle
				x: is the x position of the rectangle
				y: is the y position of the rectangle
				id(int): is the identification of rectangle

		"""
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		  return self.__width

	@width.setter
	def width(self, value):
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.__y = value