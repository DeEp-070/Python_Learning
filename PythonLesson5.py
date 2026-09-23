import math
from Module.calculator import add # or from Module.calculator import *

print(math.sqrt(add(10,20)))

#Pathlib

from pathlib import Path
path = Path("data") / "user.json"
print(path)

