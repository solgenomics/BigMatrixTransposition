import numpy as np
import sys
matrix=np.genfromtxt(sys.argv[1],delimiter=',', dtype=None)
matrix[0][0]='plant'
np.savetxt(sys.argv[2],matrix.T,delimiter=',', fmt="%s")