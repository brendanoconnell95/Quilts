#program to place quilt pieces optimally
import math
from termcolor import colored, cprint

class Piece(): 
	def __init__(self, width, length, color): 
		self.width = width
		self.length = length
		self.color = color
	def printPiece(self): 
		print(self.width, "by", self.length, ": ", self.color)
	def computeArea(self): 
		return self.width*self.length
		
		
class Quilt(): 
	def __init__(self, pieces): 
		total_area = 0
		for piece in pieces: 
			total_area+=piece.computeArea()
		self.exact_area = total_area
		self.exact_width = math.sqrt(self.exact_area/1.3)
		self.exact_length = self.exact_width*1.3
	def printSize(self): 
		down = math.floor(self.exact_width)
		up = math.ceil(self.exact_width)
		if abs(self.exact_width-down) >= abs(self.exact_width-up): 
			#rounding width up is closer
			self.practical_width = up
			#print("rounding up", self.exact_width, self.practical_width)
		else: 
			#rounding width down is closer
			self.practical_width = down
			#print("rounding down", self.exact_width, self.practical_width)
			
		#check if the area divided by the width will be long enough	
		tmp = math.floor(self.exact_area/self.practical_width)
		if tmp*self.practical_width >= self.exact_area: 
			self.practical_length = tmp
		else: 
			self.practical_length = math.ceil(self.exact_area/self.practical_width)
			
		print(self.practical_width, "by", self.practical_length)
		
	def printQuilt(self): 
		#maybe do ASCII art with *'s and x's to display different squares
		current_char = "*"
		
		
		
		
pieces = []		
for i in range(9): 
	tmp = Piece(i,i, "blue")
	pieces.append(tmp)
	#tmp.printPiece()

q1 = Quilt(pieces) #should have area of 140 or 204, sum of squres up to 7x7 or 8x8
q1.printSize()