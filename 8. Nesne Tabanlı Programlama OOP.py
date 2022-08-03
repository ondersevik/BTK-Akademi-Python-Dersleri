list = [1,2,3,3,3,3,3,4]
print(type(list))  # <class 'list'>
print(list)
# liste class [sınıfı] üzerinden oluşturulan list instance [] 
# liste sınıfında kutuphanede oluşturulan methodlar bulunur.
# list instance aynı zamanda bu methodlarıda kullanır.

list.append(5)
print(list)           # [1, 2, 3, 4, 5]
count = list.count(3) 
print(count)          # 5
clear = list.clear()
print(clear)
copy = list.copy()
print(copy)
list.extend("1")
list.index("1")
list.append(3)
list1 = [2,3,4,5,6,7]
list.append(list1)    # ['1', 3, [2, 3, 4, 5, 6, 7]]

print(list)

# liste sınıfı yerine kendimize ait Person sınıfı yapalım ve 
# Person sınıfında özellikler ve metodlar yapalım.
# name surname birthday özellikleri ile calculateage() methodu oluşturulaım
# Person sınıfından Onder objesi(instance) oluşturup bilgileri yukarıdaki özellik ve methodlara göre tutalım.

# NASIL ?

