import os, time


for i in range(0, 100):
    os.system(f"wget -b -q -O temp/img-{i}.png https://thispersondoesnotexist.com/image")
    print(i)
    time.sleep(2)
