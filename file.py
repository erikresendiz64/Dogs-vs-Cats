import os 
from tqdm import tqdm 
import shutil

# os.mkdir("Cats")
# os.mkdir("Dogs")

for img in os.listdir("./train"):
  if "cat" in img:
      shutil.copy(f'./train/{img}', f'./Cats/{img}')
  elif img == "cat.666.jpg":
      os.remove(f'./train/{img}')
      print('''
      Removed Corrupt Cat Image from Training Dataset.
      Will not add to the Cat Dataset''')
  elif img == "dog.11702.jpg":
      os.remove(f'./train/{img}')
      print('''
      Removed Corrupt Dog Image from Training Dataset.
      Will Not Add to the Dog Dataset''')
  else:
      shutil.copy(f'./train/{img}', f'./Dogs/{img}')