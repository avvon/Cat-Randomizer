import random
from PIL import Image

for i in range (57):
    number = random.uniform(1, 57)

int = int(number)

cat = Image.open('cat pictures/' + str(int) + '.jpg')

cat.show()