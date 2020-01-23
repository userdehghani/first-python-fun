import os
import sys

# vaiables

input_number = input('ye adad sahih behem bede : ')

    
# our functions

def restart():
    restart = input("\nmikhai dobare az aval emtehan koni? [a/n] > ")
    if restart == "a":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    else:
        print("\nchashm alan barname baste mishe ...")
        sys.exit(0)

# our validation
try:
    input_number = int(input_number)
except ValueError:
    print("goftam ke ye adad sahih behem bede")
    restart()


# our app goals maybe conditions


if  input_number > 28 :
        
    print("oooo chedar bozorg shodi")

elif input_number < 28 and input_number > 0 :

    print("khob pas hanoz javoon hasti")




