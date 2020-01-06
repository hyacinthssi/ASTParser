import Parser as parser


def writeln(*args):
    for arg in args:
        f.write(str(arg))
    f.write("\n")

if __name__ == "__main__":
    outputFilename = "output\\Parsed_ast.txt"
    inputFilename = "test.txt"
    textFile = open(inputFilename).read()
    ast = parser.parse(textFile, verbose=False)
    print ("\nABSTRACT SYNTAX TREE (AST):\n")
    f = open(outputFilename,"w")
    f.write(ast.toString())
    f.close()
    print(open(outputFilename).read())