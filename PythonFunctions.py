#Using functions in python
def square(x):
    return x * x

def main(): #when another file calls function above main() prevents it from running these commands. main code is limited to this file only
    for i in range(10):
        print('{} squared is {}'.format(i,square(i)))
        
if __name__=='__main__':
    main()
