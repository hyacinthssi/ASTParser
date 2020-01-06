ENDMARK = "\0"  # aka "lowvalues"

#CHARACTER

class Character:

	def __init__(self, c, lineIndex, colIndex, sourceIndex, textFile):
		'''The __init__ method is the constructor. It is called when an object is created
	 	from the class and allow the class to initialize the attributes of a class.'''	
		self.cargo          = c
		self.sourceIndex    = sourceIndex
		self.lineIndex      = lineIndex
		self.colIndex       = colIndex
		self.textFile       = textFile

 	# return a displayable string representation of the Character
	# object using the str __str__method
	def __str__(self):

		cargo = self.cargo
		if   cargo == " "     : cargo = "   space"
		elif cargo == "\n"    : cargo = "   newline"
		elif cargo == "\t"    : cargo = "   tab"
		elif cargo == ENDMARK : cargo = "   eof"

		return (
			  str(self.lineIndex).rjust(6)
			+ str(self.colIndex).rjust(4)
			+ "  "
			+ cargo
			)

