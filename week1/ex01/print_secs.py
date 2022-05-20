import os
import sys


try:
    if len(sys.argv) > 4:
        raise OSError("too many arguments")

    print(sum(int(element) * 60 ** idx for idx, element in enumerate(reversed(sys.argv[1:]))))

except Exception as e:
    print("Error: " + str(e))
    exit(os.EX_SOFTWARE)