import os
import sys


try:
    if len(sys.argv) != 3:
        raise OSError("2 arguments required")
    ret = float(sys.argv[1]) + float(sys.argv[2])
    if ret.is_integer():
        print(int(ret))
    else:
        print(ret)

except Exception as e:
    print("Error: " + str(e))
    exit(os.EX_SOFTWARE)