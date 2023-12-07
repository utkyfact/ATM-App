
bakiye = 5000
while True:
    kullanıcı = int(input("Python bankasına hoş geldiniz. \n 1-Bakiye göster \n 2-Para çek \n 3-Para yatır \n 4-Çıkış yap"))

    if kullanıcı == 1:
        print(f"Mevcut bakiyeniz {bakiye}")
    elif kullanıcı == 2:
        kacPara = int(input("Kaç para çekeceksiniz?"))
        if int(kacPara) > int(bakiye + 500):
            print("Bakiyeniz yetersiz.")
        else:
            bakiye -= kacPara
            print(f"Mevcut bakiyeniz {bakiye}")
    elif kullanıcı == 3:
        kacPara = int(input("Kaç para yatıracaksınız?"))
        bakiye += kacPara
        print(f"Mevcut bakiyeniz {bakiye}")
    elif kullanıcı == 4:
        print("Başarı ile çıkış yaptınız.")
        break
    else:
        print("Hatalı tuşlama yaptınız.")
