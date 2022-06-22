giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karekök hesapla
"""

print(giriş)

anahtar = 1

while anahtar == 1:
   soru = input("Yapmak istediğiniz işlemin numarasını girin: ")
   
   if soru == "q":
      print("çıkılıyor...")
      anahtar = 0

   elif soru == "1":
       sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
       sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
       print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

   elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)
        
   elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))