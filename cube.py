#cube.py
#created by Jenna Hebert 
#code can be run by typing "python cube.py"
#takes no input arguments 
#code prints even numbers and the cube of odd numbers, from 0-19
def cb(x):
        x=x*x*x
        return x
for j in range(20):
    if j%2 == 0:
        print j
    else:
        print cb(j)


