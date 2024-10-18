import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("ingresa tu longitud de contraseña"))
contraseña=None

for i in range(longitud):
    resultado=random.choice(caracteres)

print ( f"tu contraseña con longitud {longitud} es: {resultado}")
