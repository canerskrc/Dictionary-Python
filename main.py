"""kisisel_bilgiler={"ad":"caner","telefon":"05555555555","e_posta":"canerskrc29@gmail.com","ülke":"Türkiye"}
print(kisisel_bilgiler)"""

#dict()

"""sozluk1 = {}
print(sozluk1)
sozluk2={1:'adana',2:'adıyaman'}
print(sozluk2)
sozluk3={'isim':'caner', 1:[5,4,3]}
print(sozluk3)

sozluk4= dict({1:'erik', 2:'ayva'})
print(sozluk4)"""

######################################################################

"""iller={"konya":"42","istanbul":"34", "ankara":"06"}
print(iller.keys())

print(iller.values())"""

################################################### eleman silme####################3

"""meyveler={"adı":"Portakal","türü":"turunçgiller","kg":20,"sekli":"yuvarlak"}
print(meyveler["adı"])
print(meyveler["türü"])
# pop() metoduyla sözlüklerden eleman silinebilir

meyveler.pop("kg")
print(meyveler)

#del()

del meyveler["sekli"]
print(meyveler)

#clear()

meyveler.clear()
print(meyveler)"""

##################################################################eleman ekleme ^#############################

"""sozluk={"adı":"caner"}
print(sozluk)
sozluk['soyadı']='sekerci'
print(sozluk)"""

########################################## eleman değiştirme ################################3

# sözlük adı['anahtar adı']=yeni değer

#sozluk={'isim':'caner', 'yas': 25}
#sozluk['yas']= 40
#print(sozluk['yas'])
########################## sözlükler üzerinde gezinme ##########################3

"""sozluk={'ad': 'ali', 1:[5,4]}
print(sozluk.get(1))"""

############################# tuple oluşturma ############################

"""demet=("Python","Java","C#","Javascript","Python","Java")
print(demet.index('C#'))
print(demet.count("C#"))

for eleman in demet:
      print(eleman)
#sorted metodu

print(sorted(demet))"""






