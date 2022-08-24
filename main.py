import os


for i in range(0, 100):
    os.system(f"wget -O temp/img-{i}.png https://thispersondoesnotexist.com/image")