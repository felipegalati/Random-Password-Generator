import random
passlen = int(input("digite o tamanho da senha: "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
p = "".join(random.sample(s,passlen ))
print(p)

