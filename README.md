# rent_iha
Öncelikle merhabalar projemde adımlar hakkında bilgi vermek isterim.

Öncelikle merhabalar projemde adımlar hakkında bilgi vermek isterim.
* Django projesi OLUŞTUR
* Oluşturulan projede postgresql ile connection kur.
* Kullanıcı kayıt ve girişi sağla
* İHA oluşturma,güncelleme ve silme işlemlerini admin nin yapması gerekir bunun için admin için sayfayı oluştur.
* Kullanıcı için adminin oluşturduğu iha listesini göster ve kiralamasını sağla
* Kimin kiraladığını ve hangi İHA yı kiraladğını görmek için admin page içerisine sayfa ekle.

## Django Projesi Oluştur
Burada ilk olarak vs code üzerinde django projemi oluşturuyorum."django-admin startproject iha_kirala".<br>
Daha sonrasında bir application ekliyorum "python manage.py startapp iha_app".<br>
Bu işlemler bittikten sonra oluşturacağım site için bir template oluşturuyorum.
## Oluşturulan projede postgresql ile connection kur
Bu işlem için ilk önce postgresql'i bilgisayarıma kurdum. <br>
Daha sonra Django projem içerisinde settings.py içerisinde postgresql i ayarlamam gerekiyordu.<br>
![image](https://user-images.githubusercontent.com/63595177/190194294-8b38e0bf-7a57-4574-893d-6647d6cd7ad9.png)<br>
Ayarlamadan önce postgresql içerisinde deneme adında bir database oluşturuyorum.<br>
![image](https://user-images.githubusercontent.com/63595177/190194500-26625230-89e9-4281-a7cf-e2a8443a5d4c.png)<br>
Daha sonrasında settings.py içerisinde DATABASES bölümünde yukarıdaki gibi database name, password,user,host ve port değerlerini veriyorum.<br>
Models.py içerisinde oluşturacağım scheması belirliyorum projemde shell üzerinde input ve output bilgilerini tutmam gerekiyor bu yüzden;<br>
![image](https://user-images.githubusercontent.com/63595177/190195344-31c140c7-63fc-47a3-bf5b-470a0992148e.png)<br>
 Bu şekilde yapıyorum.<br>
 Sonrasında site içerisinde adminpage içerisinde bu veritabanını görmeyi istediğim için admin.py içerisinde ;<br>
 ![image](https://user-images.githubusercontent.com/63595177/190195596-37779b92-5abf-4903-ac67-0da17ed6c789.png)<br>
 İşlemleri gerçekleştiriyorum.<br>
bu işlemleri bitirdikten sonra terminal üzerinde bu değişikleri djangoya da göstermem gerekiyor ve sırasıyla "python manage.py makemigrations" "python manage.py migrations" komutlarını çalıştırıp database içerisinde djangonun tablolarını ve models içerisinde benim oluşturduğum tabloyu görebiliyorum.<br>
![image](https://user-images.githubusercontent.com/63595177/190195801-df76ea9c-b559-4ab3-a248-838b4c15c7d8.png)<br>
