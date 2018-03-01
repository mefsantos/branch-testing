"""

My python interface

"""

import os
import sys
import modules.module1 as m1
import modules.module2 as m2


def main():
    print "Evaluating modules..."
    m1.module1_func()
    m2.module2_func()
    print "Done!"


if __name__ == "__main__":
    main()
