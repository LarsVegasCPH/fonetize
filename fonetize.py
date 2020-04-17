from core import rewriter
import sys
#Example
try:
    translate_this = sys.argv[1]
except IndexError:
    print("You need to supply a string as input parameter. Please have a look at README.md")
    raise
result = rewriter.rewrite(translate_this)
print(result)