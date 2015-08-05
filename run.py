import sys, imp, time
SOLVED = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
"""
# this file serves as the main module for interacting with my Euler solutions.
# Running it will start a command line interface to determine which problem you want to solve
#
# To run: python run.py
#
"""
# This is not good python in general, but it's an easy and minimal implementation
# TODO make this function more secure and catch exceptions
def main():
    if len(sys.argv) == 1:
        inputArgs = input("Enter Euler problem number (1-20 currently):  ")
        if inputArgs in SOLVED:
            inputArgs = "Euler"+str(inputArgs)
            mod = __import__(("solutions."+inputArgs))
            start = time.clock()
            eval(("mod."+inputArgs+".euler()"))
            end = time.clock()
            print "Time elapsed: %f seconds" % (end - start)
        else:
            print "unsolved, please use input number of solved"
            print SOLVED
    else:
        try:
            inputArgs = int(sys.argv[1])
            if inputArgs <= SOLVED:
                inputArgs = "Euler"+str(inputArgs)
                mod = __import__(("solutions."+inputArgs))
                start = time.clock()
                eval(("mod."+inputArgs+".euler()"))
                end = time.clock()
                print "Time elapsed: %f seconds" % (end - start)
            else:
                print "please try again"
        except ImportError:
            print "I haven't gotten to that one yet!"

if __name__ == "__main__":
    sys.exit(main())