import string
import hashlib
import itertools
with open("shadow.txt", "r") as fshadow:
    for line in fshadow:
        for x in range(4, 5):
            result = itertools.product(string.printable[:-6], repeat=x)
            for i in result:
                hashed = hashlib.md5("".join(i).encode("UTF-8")).hexdigest()
                #  print(f"{hashed}    {''.join(i)}")
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {''.join(i)}\n\nThe password is {''.join(i)}")
                    exit(0)
