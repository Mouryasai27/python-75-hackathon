
#delete the existing file

import os

if os.path.exists("delete1.txt"):
    os.remove("delete.txt")
else:
    print("file not exists")