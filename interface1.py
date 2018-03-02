"""

My python interface

"""

import modules.module1 as m1
import modules.module2 as m2
import numpy as np


def main():
    print "Evaluating modules..."
    m1.module1_func()
    m2.module2_func()
    print "Done!"
    print "Testing required modules..."
    print type(np.array([1,2,3,4,5]))

if __name__ == "__main__":
    main()
