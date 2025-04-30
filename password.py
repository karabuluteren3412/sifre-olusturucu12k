import random  

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_lenght = int(input("şifre uzunluğunu giriniz"))

password =  ""
for i in range(password_lenght):
    sifre += random.choice(characters)

print(password)
