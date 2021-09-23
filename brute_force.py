import string
import hashlib
import itertools

with open("hashed.txt", "r") as fshadow:
    with open("pass_list.txt", "r") as fPass_list:
        for line in fshadow:
            for passwd in fPass_list:
                hashed = hashlib.md5(passwd[:-1].encode("UTF-8")).hexdigest()
                if line[:-1] == hashed:
                    print(f"\n\nCRACKED\n\n{hashed}    {passwd}\n\nThe password is {passwd}")
                    exit(0)

with open("hashed.txt", "r") as fshadow:
    print("Password list failed, falling back to brute force.")
    for line in fshadow:
        for x in range(4, 5):
            result = itertools.product(string.printable[:-6], repeat=x)
            for i in result:
                hashed = hashlib.md5("".join(i).encode("UTF-8")).hexdigest()
                #  print(f"{hashed}    {''.join(i)}")
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {''.join(i)}\n\nThe password is {''.join(i)}")
                    exit(1)
