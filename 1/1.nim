import strutils
var value = 0
var input : File = open("./input")
while(not input.endOfFile):
    value+=parseInt(input.readLine.string)
echo value