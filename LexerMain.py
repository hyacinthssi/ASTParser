import Lexer as lexer
from Symbols import EOF


def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")

#main
def main(textFile):
	global f
	f = open(outputFilename, "w")
	writeln("\n\tT O K E N S : \n")

	# create an instance of a lexer
	lexer.initialize(textFile)

	
	# use the lexer.getlist() method repeatedly to get the tokens in
	# the textFile. Then print the tokens.
	while True:
		token = lexer.get()
		writeln(token.show(True))
		if token.type == EOF: break
	f.close()

if __name__ == "__main__":
	outputFilename = "output\\LexerMain.txt"
	inputFilename = "test.txt"
	textFile = open(inputFilename).read()
	main(textFile)
	print(open(outputFilename).read())
