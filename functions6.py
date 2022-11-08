# Kullanıcı bir mesaj ve o mesajın yazılacağı adediv fonksiyona göndersin.
# Eğer adet verisi gönderilmezse adet varsayılan 1 olsun.
# Gönderilen adet kadar mesaj ekrana basılsın.
# süre 10 dakika




def mesajVer(mesaj,adet=1):
    for i in range(adet):
        print(mesaj)


mesajVer("Merhaba Python")
mesajVer("Merhaba",5)