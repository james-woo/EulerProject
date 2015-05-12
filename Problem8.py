import fileinput
import sys
digit = ""
for line in sys.stdin:
	digit += line
digit = digit.replace("\n", "")
def gProd(digit):
    p = 1
    highest = 0
    for i in range(987):
   	 for j in range(i,i+13):
   		 p *= int(digit[j])
   	 if p > highest:
   		 highest = p
   	 p = 1
    return highest
print(gProd(digit))