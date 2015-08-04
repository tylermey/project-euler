import sys, imp, time
SOLVED = 14
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
        if inputArgs <= SOLVED:
            inputArgs = "Euler"+str(inputArgs)
            mod = __import__(("solutions."+inputArgs))
            start = time.clock()
            eval(("mod."+inputArgs+".euler()"))
            end = time.clock()
            print "Time elapsed: %f seconds" % (end - start)
        else:
            print "unsolved, please use input between 1-%d" % SOLVED
    else:
        ##try:
        inputArgs = int(sys.argv[1])
        if inputArgs <= SOLVED:
            inputArgs = "Euler"+str(inputArgs)
            mod = __import__(("solutions."+inputArgs))
            start = time.clock()
            eval(("mod."+inputArgs+".euler()"))
            end = time.clock()
            print "Time elapsed: %f seconds" % (end - start)
        else:
            print "unsolved, please use input between 1-%d" % SOLVED
        #except:
        #    print "catch all errors, CHECK YOUR CODE :)"

if __name__ == "__main__":
    sys.exit(main())