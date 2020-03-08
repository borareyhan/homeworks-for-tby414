#Kullanıcının boy ve kilosunu alarak Beden-Kitle indeksini hesaplıyoruz
boy = float (input ("Boyunuzu giriniz(CM): "))
kg = float (input ("Kilonuzu giriniz(KG): "))
#İdeal kilo hesabı için boyu santimetre şeklinde almamız gerekiyor bu yüzden metre cinsini ayrı isimlendiriyoruz
boym = boy/100.0
bki = kg/(boym*boym)
print("Beden Kitle İndeks Değeriniz: ", bki)
print("Beden-Kitle İndeks Değer Aralıkları:\n"
"<18.5 : Zayıf\n"
"18.5-24.9 : Sağlıklı\n"
"25-29.9 : Fazla Kilolu\n"
"30-34.9 : 1. Derece Obezite\n"
"35-39.9 : 2. Derece Obezite\n"
"40> : 3. Derece Obezite\n")

#Kullanıcının Beden-Kitle indeksine göre hangi BKİ aralığında olduğunu belirtiyoruz
if bki < 18.5:
    print("BKİ Hesaplarına göre Zayıfsınız")
if bki <= 25:
    print("BKİ Hesaplarına göre Sağlıklısınız")
elif bki <= 30:
    print("BKİ Hesaplarına göre Fazla Kilolusunuz")
elif bki <= 35:
    print("BKİ Hesaplarına göre 1. Derece Obezitesiniz")
elif bki <= 40:
    print("BKİ Hesaplarına göre 2. Derece Obezitesiniz")
else:
    print("BKİ Hesaplarına göre 3. Derece Obezitesiniz")

#Beden kitle indeksinden yola çıkarak kullanıcıya ideal kilosu için bir hedef oluşturuyoruz
#İdeal kilo değerleri hesapları 
mankilo = 50+(2.3/2.54)*(boy-152.4) 
womankilo = 45.5+(2.3/2.54)*(boy-152.4)
print("İdeal Kilo Değeriniz(Erkek): ", mankilo)
print("İdeal Kilo Değeriniz(Kadın): ", womankilo)
idealm = mankilo-kg
idealw = womankilo-kg
print("İdeal kilonuza ulaşmanız için almanız/vermeniz gerekiyor(Erkek)", idealm)
print("İdeal kilonuza ulaşmanız için almanız/vermeniz gerekiyor(Kadın)", idealw)

