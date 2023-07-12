import math

def faktoriyelal():
    deger = int(input("Faktöriyeli alınacak değeri giriniz: "))
    faktoriyel = 1
    for i in range(1,deger+1):
        if(deger>1):
            faktoriyel = faktoriyel * deger
            deger -= 1
        else: print(faktoriyel)

def kalanbul():
    deger1 = int(input("Birinci değeri giriniz: "))
    deger2 = int(input("İkinci değeri giriniz: "))
    if(deger1<deger2):
        sonuc = deger2%deger1
        print("{}'nin {}'den bölümünden kalan: {}".format(deger2,deger1,sonuc))
    if(deger1>deger2):
        sonuc = deger1%deger2
        print("{}'nin {}'den bölümünden kalan: {}".format(deger1,deger2,sonuc))
    else: print("Bölümden kalan 0'dır.")

def farkbul():
    deger1 = int(input("Birinci değeri giriniz: "))
    deger2 = int(input("İkinci değeri giriniz: "))
    if(deger1>deger2): print(deger1-deger2)
    elif(deger1<deger2): print(deger2-deger1)
    else: print("Sayılar eşittir.")

def radyanderecedonusum():
    secim2 = int(input("Dönüşüm türü seçiniz\n1-) Radyan-Derece Dönüşümü\n2-) Derece-Radyan Dönüşümü\n0-) Çıkış.\n"))
    if(secim2 == 1):
        deger = int(input("Dereceye dönüştürülecek radyan değerini giriniz: "))
        print(math.degrees(deger))
    elif(secim2 == 2):
        deger = int(input("Radyana dönüştürülecek derece değerini giriniz: "))
        print(math.radians(deger))

def logaritmaal():
    secim2 = int(input("Dönüşüm türü seçiniz\n1-) Radyan-Derece Dönüşümü\n2-) Derece-Radyan Dönüşümü\n0-) Çıkış.\n"))
    if(secim2 == 1):
        deger = int(input("Dereceye dönüştürülecek radyan değerini giriniz: "))
        print(math.degrees(deger))
    elif(secim2 == 2):
        deger = int(input("Radyana dönüştürülecek radyan değerini giriniz: "))
        print(math.radians(deger))

def asalsorgu():
    deger = int(input("Asal olup olmadığı kontrol edilecek sayıyı giriniz: "))
    if deger > 1:
   
        for i in range(2,deger):
            if (deger % i) == 0:
                print("Sayı asal değildir.")
                break
        else: print("Sayı asaldır.")
 
    else: print("Sayı asal değildir.")

def medyanbul():
    medyanList = []
    while True:
        medyanInput = input("Değer giriniz (Çıkış ve bitirmek için 'q'): ")
        if(medyanInput == "q"):
            medyan = int((len(medyanList)+1)/2)
            print("Girdiğiniz değerlerin medyanı: {}".format(medyanList[medyan-1]))
            break
        else:
            medyanList.append(int(medyanInput))

def binarycevir(n):
    if(n > 1):
        binarycevir(n//2)
    print(n%2, end=' ')

while True:
    secim = int(input(
    """Hoş geldiniz. Yapmak istediğiniz işlemi giriniz.
    1-) Toplama
    2-) Çıkarma
    3-) Sayılar Arası Fark Bulma
    4-) Çarpma
    5-) Bölme
    6-) Kare Alma
    7-) Bölümden Kalan Bulma
    8-) Karekök Alma
    9-) Üs Alma
    10-) Mutlak Değer Alma
    11-) Faktöriyel Alma
    12-) Ortalama Alma
    13-) EBOB Alma
    14-) Logaritma Alma
    15-) Radyan-Derece Dönüşümleri
    16-) Sinüs Bulma
    17-) Kosinüs Bulma
    18-) Tanjant Bulma
    19-) Kotanjant Bulma
    20-) Asal sorgulama
    21-) Medyan Bulma
    22-) Binary'e çevirme
    0-) Çıkış. \n"""))
    
    if(secim == 0 or secim >= 23):
        print("Hoşça kalın.")
        break
    elif(secim == 1): # Toplama
        deger1 = int(input("Birinci değeri giriniz: "))
        deger2 = int(input("İkinci değeri giriniz: "))
        print("Sayıların toplamı",deger1+deger2)
        break
    elif(secim == 2): # Çıkarma
        deger1 = int(input("Birinci değeri giriniz: "))
        deger2 = int(input("İkinci değeri giriniz: "))
        print(deger1-deger2)
        break
    elif(secim == 3): # 2 sayı arası fark bulma
        farkbul()
        break
    elif(secim == 4): # Çarpma
        deger1 = int(input("Birinci değeri giriniz: "))
        deger2 = int(input("İkinci değeri giriniz: "))
        print(deger1*deger2)
        break
    elif(secim == 5): # Bölme
        deger1 = int(input("Birinci değeri giriniz: "))
        deger2 = int(input("İkinci değeri giriniz: "))
        print(deger1/deger2)
        break
    elif(secim == 6): # Kare alma
        deger = int(input("Karesi alınacak değeri giriniz: "))
        print(deger*deger)
        break
    elif(secim == 7): # Bölümden kalanı bulma
        kalanbul()
        break
    elif(secim == 8): # Kök alma
        deger = int(input("Kökünü almak istediğiniz değeri giriniz: "))
        kok = int(input("Kökün derecesini giriniz: "))
        print(deger**(1/kok))
        break
    elif(secim == 9): # Üs alma
        deger = int(input("Üssü alınacak değeri giriniz: "))
        us = int(input("Üssü giriniz: "))
        basdeger = deger
        for i in range(1,us):
            deger *= basdeger
            i += 1
        print(deger)
        break
    elif(secim == 10): # Mutlak değer alma
        deger = int(input("Mutlak değeri alınacak değeri giriniz: "))
        if(deger<0):
            sonuc = deger * -1
            print(sonuc)
            break
        if(deger>0):
            print(deger)
        else:
            print(0)
    elif(secim == 11): # Faktöriyel alma
        faktoriyelal()
        break
    elif(secim == 12): # Ortalama alma
        toplam = 0
        sayac = 0
        while True:
            deger = int(input("Ortalaması alınacak değerleri giriniz: (Çıkış için 0)"))
            toplam += deger
            sayac += 1
            if(deger == 0):
                sayac -= 1
                ortalama = toplam/sayac
                print(ortalama)
        break
    elif(secim == 13): # EBOB alma
        deger1 = int(input("Birinci değeri giriniz: "))
        deger2 = int(input("İkinci değeri giriniz: "))
        print(math.gcd(deger1,deger2))
        break
    elif(secim == 14): # Logaritma alma
        logaritmaal()
        break
    elif(secim == 15): #Radyan-Derece dönüşümü
        radyanderecedonusum()
        break
    elif(secim == 16): #Sinüs bulma
        deger = int(input("Sinüsü bulunacak değerin derecesini giriniz: "))
        print(math.sin(math.radians(deger)))
        break
    elif(secim == 17): #Kosinüs bulma
        deger = int(input("Kosinüsü bulunacak değerin derecesini giriniz: "))
        print(math.cos(math.radians(deger)))
        break
    elif(secim == 18): #Tanjant bulma
        deger = int(input("Tanjantı bulunacak değerin derecesini giriniz: "))
        print(math.tan(math.radians(deger)))
        break
    elif(secim == 19): #Kotanjant bulma
        deger = int(input("Kotanjantı bulunacak değerin derecesini giriniz: "))
        print(1/(math.tan(math.radians(deger))))
    elif(secim == 20):
        asalsorgu()
        break
    elif(secim == 21):
        medyanbul()
        break
    elif(secim == 22):
        value = int(input("Binary'e çevrilecek decimal değeri giriniz: "))
        binarycevir(value)
        break