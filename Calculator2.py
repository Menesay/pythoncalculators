print("""
==================
|                |
| Hesap Makinesi |
|                |
|   M.ENES AY    |
|     2020       |
==================
İşleçler:
   + toplama
   - çıkarma
   * çarpma
   / bölme

Yapmak istediğiniz işlemi yazıp ENTER tuşuna basın. 
(Örneğin 8 ve 4 sayılarını çarpmak için 8 * 4 yazdıktan sonra ENTER tuşuna basın.)
""")
veri = input("İşleminiz: ")
hesap = eval(veri)

print(hesap)
