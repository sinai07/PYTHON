n = 0

if n % 2 == 1:
    print("weird")
elif n % 2 == 0 and n in range(2, 6):
    print("Not weird")
elif n % 2 == 0 and n in range(6, 21):
    print("weird")
elif n % 2 and n > 20:
    print("Not Weird")