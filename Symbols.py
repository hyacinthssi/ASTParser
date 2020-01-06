# a list of keywords
Keywords = """
if
then
else
elif
endif
while
loop
endloop
print
return
exit
"""
Keywords = Keywords.split()


# a list of symbols that are one character long
OneCharacterSymbols = """
=
( )
< >
/ * + -
! &
.  ;
"""

OneCharacterSymbols = OneCharacterSymbols.split()


# a list of symbols that are two characters long

TwoCharacterSymbols = """
==
<=
>=
<>
!=
++
**
--
+=
-=
||
"""

TwoCharacterSymbols = TwoCharacterSymbols.split()

import string

IDENTIFIER_STARTCHARS = string.ascii_letters
IDENTIFIER_CHARS      = string.ascii_letters + string.digits + "_"

NUMBER_STARTCHARS     = string.digits
NUMBER_CHARS          = string.digits + "."

STRING_STARTCHARS = "'" + '"'
WHITESPACE_CHARS  = " \t\n"
#fragment stop constants


# TokenTypes for things other than symbols and keywords
STRING             = "String"
IDENTIFIER         = "Identifier"
NUMBER             = "Number"
WHITESPACE         = "Whitespace"
COMMENT            = "Comment"
EOF                = "Eof"
