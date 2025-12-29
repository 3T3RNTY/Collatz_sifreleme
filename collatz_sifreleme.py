import math

# Collatz dizisi tabanlı şifreleme
# Kullanıcıdan pozitif en  az 4 basamaklı tam sayı almalı

liste = []
liste2 = []

def collatz_sequence(n, liste):
    """ girilen Sayı için Collatz dizisini oluşturan fonksiyon """

    if (math.log(int(n), 2).is_integer()):
        n = int(n) + 1

    # 16 eleman elde edene kadar devam et
    while (n != 1 and len(liste) < 16):

        if (int(n) %2 == 0):
            if(math.log(int(n), 2).is_integer()):
                break
            else:
                n = int(n) / 2
                liste.append(n)
        elif (int(n) %2 != 0):
            n = (int(n)*3)+1
            liste.append(n)

    return liste

def cryption_process(sayi):
    """ Girilen sayının Collatz dizisini oluşturur ve şifreleme işlemini yapar """

    collatz_sequence(int(sayi),liste)
    collatz_sequence(int(sayi)+1,liste2)

    # İki Collatz dizisini birleştir
    for i in range(len(liste2)):
        liste.append(liste2[i])

# Her bir elemanın rakamları toplamı çift ise 1, tek ise 0 olarak değiştir
    for i in range(len(liste)):
        temp = int(liste[i])

        digit_sum = sum(int(digit) for digit in str(temp))
        if digit_sum %2 == 0:
            liste[i] = 1
        else:
            liste[i] = 0

    sonuc = ''.join(map(str, liste))
    return sonuc


while(True):

    # Kullanıcıdan alınacak olan sayının uygunluğunu kontrol et

    sayi = input("Bir sayı girin: ")

    if not sayi.isdigit():
        print("Lütfen geçerli bir pozitif tam sayı girin.")

    elif int(sayi) <= 0:
        print("Lütfen pozitif bir tam sayı girin.")

    elif (len(sayi) < 4):
        print("Lütfen en az 4 basamaklı bir sayı girin.")

    else:
        print(cryption_process(sayi))
        liste.clear()
        liste2.clear()



