import time

a = time.time()
b = a
count = 0

while count <= 10:
    b = time.time()
    if int(b) - int(a) == 1:
        print(count)
        count += 1
        a = time.time()
        b = a
         


