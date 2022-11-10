# rent_iha
Öncelikle merhabalar projemde adımlar hakkında bilgi vermek isterim.

Öncelikle merhabalar projemde adımlar hakkında bilgi vermek isterim.
* Django projesi OLUŞTUR
* Oluşturulan projede postgresql ile connection kur.
* Kullanıcı kayıt ve girişi sağla
* İHA oluşturma,güncelleme ve silme işlemlerini admin nin yapması gerekir bunun için admin için sayfayı oluştur.
* Kimin kiraladığını ve hangi İHA yı kiraladğını görmek için admin page içerisine sayfa ekle.

* Kullanıcı için adminin oluşturduğu iha listesini göster ve kiralamasını sağla

## Django Projesi Oluştur
Burada ilk olarak vs code üzerinde django projemi oluşturuyorum."django-admin startproject iha_kirala".<br>
Daha sonrasında bir application ekliyorum "python manage.py startapp iha_app".<br>
Bu işlemler bittikten sonra oluşturacağım site için bir template oluşturuyorum.
## Oluşturulan projede postgresql ile connection kur
Bu işlem için ilk önce postgresql'i bilgisayarıma kurdum. <br>
Daha sonra Django projem içerisinde settings.py içerisinde postgresql i ayarlamam gerekiyordu.<br>
**![image](https://user-images.githubusercontent.com/63595177/190194294-8b38e0bf-7a57-4574-893d-6647d6cd7ad9.png)<br>**
Ayarlamadan önce postgresql içerisinde iha adında bir database oluşturuyorum.<br>
Daha sonrasında settings.py içerisinde DATABASES bölümünde yukarıdaki gibi database name, password,user,host ve port değerlerini veriyorum.<br>
Models.py içerisinde oluşturacağım scheması belirliyorum projemde shell üzerinde input ve output bilgilerini tutmam gerekiyor bu yüzden;<br>
![image](https://user-images.githubusercontent.com/63595177/201172599-b463f5e6-2d9f-4015-b1eb-80369f085f64.png)
Bu şekilde yapıyorum.<br>
 Sonrasında site içerisinde adminpage içerisinde bu veritabanını görmeyi istediğim için admin.py içerisinde ;<br>
![image](https://user-images.githubusercontent.com/63595177/201172867-def6f99a-fdbc-48b9-89c0-799900af68fc.png)
İşlemleri gerçekleştiriyorum.<br>
bu işlemleri bitirdikten sonra terminal üzerinde bu değişikleri djangoya da göstermem gerekiyor ve sırasıyla "python manage.py makemigrations" "python manage.py migrations" komutlarını çalıştırıp database içerisinde djangonun tablolarını ve models içerisinde benim oluşturduğum tabloyu görebiliyorum.<br>
## Kullanıcı kayıt ve girişi sağla
İlk olarak kayıt ve Login olarak 2 farklı butonumm var ve bunlar arsındaki geçişler aşağıdaki gibidir. Burada views.py içerisinde giriş için djangonun postgrede oluşturduğu user table ı kullandım ve authenticate ile giriş kontrolünü sağladım. Bu sağlamadan sonra giriş yapanın superuser mı olduğunu kontrol edip kullanıcı tipine göre bir index sayfasına geçişini sağladım . Burada ayrıyeten daha sonrasında kullanmak için bir global değişken tanımlayıp içerisine user.id bilgisini tuttum.
![image](https://user-images.githubusercontent.com/63595177/201173453-0a4b1bed-dc7d-4c5f-b853-24c6ee4ad014.png)


![image](https://user-images.githubusercontent.com/63595177/201173037-74da3357-2072-4c1d-9ac9-91424c835010.png)
Kayıt kısmında ise kullanıcıdan çift şifre istedim ve bunların uyumlarını karşılaştırdım. Daha sonrasında kod içerisinde daha önce alınmış bir kullanıcı adı olup olmadığının bilgisini gösterdim. Eğer daha önce alınmış bir isim ise messagebox ile bu bilgiyi göndürdüm.
![image](https://user-images.githubusercontent.com/63595177/201174345-acca7210-ef2a-4def-9f06-4a350a2339f1.png)
![image](https://user-images.githubusercontent.com/63595177/201174422-e49a8ba4-e9ee-4761-b241-f186882fbe3e.png)

![image](https://user-images.githubusercontent.com/63595177/201173079-bb93c978-905e-49b9-9bc5-fe11d5172e68.png)

## İHA oluşturma,güncelleme ve silme işlemlerini admin nin yapması gerekir bunun için admin için sayfayı oluştur.
İlk önce yöneticinin iha bilgilerini girmesi için django forms.py içerisinde gerekli bilgileri önceden tanımlıyorum. Daha sonrasında index sayfası içerisinde Jinja kullanarak bu formun çalışmasını sağlıyorum.Bunuda Djangoyla birlikte index sayfası içerisine boş formu yani forms.py içerisinde oluşturduğum formu render ile gönderip jinjayla kullanıyorum .
![image](https://user-images.githubusercontent.com/63595177/201176013-7a6bdbd8-f05f-4667-9e8b-9b314094bce8.png)
Ekleme işlemini adminin direkt olarak görmesini sağlamak için eklme kısmının hemen yanında İha bilgilerini görmesini sağlıyorum. Bunuda aynı şekilde render ile database üzerindeki tüm iha bilgilerini alıp html sayfamın içerisine gönderiyorum.
![image](https://user-images.githubusercontent.com/63595177/201176265-e1467dad-5d32-48fb-b551-dafe2d0dcf0c.png)
![image](https://user-images.githubusercontent.com/63595177/201176310-00ff0aba-8347-4afb-8371-518fecb6dcb5.png)
![image](https://user-images.githubusercontent.com/63595177/201176356-1c33213e-9d81-4452-aed8-795120877ecc.png)

Güncelleme ve Silme işlemi için oluşturduğum tabloda her indise bir güncelle ve sil butonu aktarıp bunlar üzerinde kodlama yapıyorum.
![image](https://user-images.githubusercontent.com/63595177/201176562-0fa931c5-7fae-4be4-8981-15dae223d36a.png)
Buradaki en önemli dikkat edilecek şey id bilgisinin doğru olarak alınması. Güncelle işleminde farklı bir html sayfasına admin yönlendiriliyor ve gerekli düzenlemeleri yaptıktan sonra index sayfasına geri geliyor.
![image](https://user-images.githubusercontent.com/63595177/201176790-b0592537-44fb-4ed0-b741-17fd601e064b.png)
Sil işleminde index sayfasından hiçbir çıkış işlemi gerçekleştirmiyor.
Arama ve filtreleme işlemlerini javascript ile biraz araştırma yaparak yazılan kodları inceleyerek kendi projeme göre bir kod yazmaya başlıyorum.
![image](https://user-images.githubusercontent.com/63595177/201177449-8c014501-adc4-425f-ab56-db7cb94644ef.png)
arama işlemi görüldüğü gibi "my input" id sine sahip bir input oluşturuyorum ve mytable içerisinde bir filtrele işlemine geçiyorum.

![image](https://user-images.githubusercontent.com/63595177/201177721-9204c796-8115-4748-9cf4-e1afdcece9b5.png)
burada iha nın kategory bilgilerine göre gidiyorum. Gözcü ve savaş olarak ikiye ayırdığım için dropdown menume 2 farklı ve all olmak üzere 3 farklı kategorileştirme verisi ekliyorum. Sonuç olarak;
![image](https://user-images.githubusercontent.com/63595177/201178099-00870f6c-20e4-4122-bc18-f3805dc04e71.png)
![image](https://user-images.githubusercontent.com/63595177/201178140-f5fdaf21-cbdf-43f6-af71-492438b602b2.png)


# Kimin kiraladığını ve hangi İHA yı kiraladğını görmek için admin page içerisine sayfa ekle.
![image](https://user-images.githubusercontent.com/63595177/201180035-1cc3bf9c-0c4c-4899-a5ec-dd3c678d7401.png)
Burada ektra olarak iha kiralaması için bir table daha oluşturdum ve içerisinde iha bilgileri ve kiralıyan kullanıcın ad soyad ve username bilgileri bulunmaktadır.

## Kullanıcı için adminin oluşturduğu iha listesini göster ve kiralamasını sağla
![image](https://user-images.githubusercontent.com/63595177/201180241-e43cbbef-a3fc-499b-a83a-ea3ed4c57f7b.png)
Admin pagede olduğuğu gibi tablo olarak iha bilgilerini gösteriyorum farklı olarak güncelle ve sil butonu yerine kirala butonunu ekliyorum. Kirala butonuna kullanıcı tıkladığında az önce bahsettiğim bilgilerle birlikte database e kayıt oluyor.







