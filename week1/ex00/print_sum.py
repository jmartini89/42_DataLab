import os
import sys


try:
    if len(sys.argv) != 3:
        raise OSError("2 arguments required")
    print(int(sys.argv[1]) + int(sys.argv[2]))

except Exception as e:
    print("Error: " + str(e))
    exit(os.EX_SOFTWARE)