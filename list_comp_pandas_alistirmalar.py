
##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()




# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']



# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#







##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################


#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################




#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################



#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################




#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################



#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################




#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################




#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################



#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################



#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################



#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################




#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################



#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################





#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################



#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################


#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################



#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################




#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################



#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################



#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################



#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################



#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################




#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################



