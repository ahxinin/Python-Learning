import os
from pathlib import Path

print(os.path.abspath("."))

q = Path("/temp/pythonDir")
Path.mkdir(q, parents=True)