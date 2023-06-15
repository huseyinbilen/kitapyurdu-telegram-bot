# Kitapyurdu Telegram Botu :robot:

Bu proje, kitapyurdu.com'daki 3 farklı kategorideki kitapları listeleyen bir Telegram botu geliştirmeyi amaçlamaktadır.

## Amaç

Bu proje, kitapseverlere popüler kitapları ve en çok satan kitapları sunarak kitap seçimlerini kolaylaştırmayı hedeflemektedir. Bot, kullanıcılara kitap listelerini sağlayacak ve istedikleri kitaplar hakkında daha fazla bilgi edinmelerini sağlayacaktır.

## Hazırlık

Projenin hazırlık aşamaları aşağıda belirtilmiştir:

1. Öncelikle, Telegram BotFather aracılığıyla bir Telegram botu oluşturuldu. Bu adım, botun kimlik bilgilerini (token) almayı sağladı.

2. Kitapyurdu.com sitesinde mevcut bir API anahtarının olmaması nedeniyle, verileri çekmek için bir "scrapper" geliştirildi. Bu "scrapper" ile kitap bilgileri ve en çok satan kitaplar elde edildi.

3. Son olarak, Telegram botu için mesajları yakalama ve cevaplama algoritması geliştirildi. Bu algoritma, "scrapper" ile bağlantı kurarak kullanıcılara kitap listelerini iletecek ve istek üzerine daha fazla bilgi sunacaktır.

## Kütüphaneler

Proje için aşağıdaki kütüphaneler kullanıldı:

1. Scrapper için: 👁️‍🗨️
   - beautifulsoup4
   - requests
   - unidecode (kurulum için: `pip install unidecode`)

2. Telegram Bot için: :robot:
   - python-dotenv
   - python-telegram-bot

Bu kütüphaneler, veri çekme işlemleri için Beautiful Soup ve Requests kütüphanelerini, Unicode karakter dönüşümleri için unidecode kütüphanesini, Telegram Bot ile iletişim için ise python-dotenv ve python-telegram-bot kütüphanelerini içermektedir.

## Nasıl Kullanılır

1. Telegram botunu kullanmak için öncelikle Telegram üzerinden oluşturduğunuz botun token bilgisini almalısınız.

2. Botun çalışabilmesi için projedeki kütüphaneleri yüklemelisiniz. Kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz ya da `pip install requirements.txt` yazarak indire bilirsiniz:
```
pip install beautifulsoup4
pip install requests
pip install unidecode
pip install python-dotenv
pip install python-telegram-bot
```

3. Proje klasöründe bulunan `.env.example` dosyasını `.env` olarak kaydedin ve Telegram botunuzun token bilgisini ilgili alana yerleştirin.

4. `bot.py` dosyasını çalıştırarak Telegram botunu başlatın.

5. Telegram üzerinde botunuzla etkileşime geçmek için botun kullanıcı adını girin ve sohbeti başlatın. 
