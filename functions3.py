# tpolama ve çıkarma işlemi yapan fonksiyon yazınız.
# return ifadesi fonksiyonun bir değeri geri döndürmesidir.

def topla(number1, number2):
    return number1 + number2


def cikar(number1, number2):
    return number1 - number2


# çarpma ve bölme olsun ancak bölmede 0 a bölüm işlemi engelli olsun.

def carp(number1,number2):
    return number1 * number2

def bol(number1,number2):
    if number2 == 0:
        return "sıfıra bölüm yapılamaz"
    else:
        return number1 / number2


print("Toplama işleminin sonucu: {}".format(topla(10, 20)))
print("Çıkarma işleminin sonucu: {}".format(cikar(70,30)))
print("Çarpma işleminin sonucu: {}".format(carp(3,15)))
print("Bölme işleminin sonucu: {}".format(carp(3,0)))