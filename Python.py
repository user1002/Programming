#User can provide input in the terminal
name=input()
print(f'hello,{name}!') 

#Call function from another file called PythonFunctions
from PythonFunctions import square
print(square(10))

