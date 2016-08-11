numb2words = {1:'one', 2:'two',3:'three',4:'four', 5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10:'ten', 11:'eleven', 12:'twelve',13:'thirteen', 14:'fourteen', 15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'} 
numb2words2 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

class Parser():
	
	def parse(self, x):
		
		self.numbers = (int, long, float, complex) 
		z, y = divmod(x, 10)  
		if x < 20:
			if isinstance(x, self.numbers):
				return numb2words[x]
		
		if x >= 20: 
			if isinstance (x, self.numbers):
				return numb2words2[z] + numb2words[y]

		else:
			raise ValueError

