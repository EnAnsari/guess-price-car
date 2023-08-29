# حدس قیمت خودرو
[![en](https://img.shields.io/badge/click_to_README-English-red.svg)](https://github.com/EnAnsari/guess-price-car/edit/main/README-EN.md)
<br>
با کمک این پروژه ما می‌توانیم با دادن اطلاعات ماشین به برنامه قیمت نسبی آن را دریافت کنیم. این برنامه پروژه پایانی
<a href='https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%BE%DB%8C%D8%B4%D8%B1%D9%81%D8%AA%D9%87-mk387/'>دوره پایتون پیشرفته مکتب خونه</a>
هست.
<br><br>

## شروع
    
این برنامه یک برنامه‌ی پایتون است. لذا از نصب بودن پایتون در سیستم خود اطمینان حاصل کنید. همچنین من از`my sql` در این برنامه استفاده کرده‌ام. پس اونو هم نصب کنید. پس از نصب این دو تنها کافیست مراحل زیر را دنبال کنید:
<br>
ابتدا پروژه را کلون میکنیم:
``` git
git clone https://github.com/EnAnsari/guess-price-car.git
```
```
cd guess-price-car
```
سپس پیشنیازهای مورد نیاز را با دستور زیر نصب میکنیم. پیشنهاد من این است که از `vitural environment‍‍‍` استفاده کنید اما ضروری نیست.

```
pip install -r requirements.txt
```
سپس باید یک فایل به نام `local_db.py‍` درست کنید. محتوی این فایل باید شامل یوزرنیم و پسورد دیتابیس شما باشد:
```python
DB_USER = 'username'
DB_PASSWORD = "password"
```
<br>

## اجرا و تست
اجرای این برنامه در دو مرحله است:

### ساخت دیتابیس و crawl

برای اجرا باید مراحل قسمت `شروع` را تکمیل کرده و سپس فایل ‍‍`crawl.py` را اجرا کنید. برای اجرا باید از اتصال خود به اینترنت مطمئن باشید.
```
python crawl.py
```
سپس یک ورودی به برنامه میدهیم که نشان دهنده تعداد صفحات برای گرفتن اطلاعات است. این عدد هر چه بزرگ‌تر باشد دیتابیس بزرگتر و برنامه ما دقیق‌تر خواهد بود. اما در عوض مدت زمان بیشتری برای crawl نیاز پیدا می‌کنیم.
```
Enter number of pages for crawl: 10
```

سپس باید منتظر بمانیم تا برنامه دیتابیس را بسازد. اگر از قبل جدولی ساختید و نیاز دارید اطلاعات آن را پاک کنید با دستور زیر در `my sql` میتوانید آن را پاک کنید:
```
DROP TABLE cars;
```
### حدس قیمت با ماشین لرنینگ
برای اینکار تنها کافیست فایل `ml.py` را اجرا کنیم:
```
python crawl.py
```
در ورودی این برنامه ابتدا از ما پرسیده می‌شود که می‌خواهیم ورودی دیفالت را به برنامه بدیم یا یک اطلاعات دستی. برای دادن اطلاعات دیفالت ‍`d` و برای دادن اطلاعات دستی `m` را وارد کنید.<br>
**البته این رو هم باید بگم که این برنامه از ماشین لرنینگ ساده ای استفاده میکنه و شاید نتیجه خوبی از خرید ماشین با این برنامه نداشته باشید 😅**
<br><br>

<div dir='rtl'>
<details><summary><h2>دیگر</h2> (کلیک کنید برای باز شدن)</summary>
    
## ساخته شده با

* [scikit learn](https://github.com/scikit-learn/) - machine learning
* [my sql](https://github.com/mysql) - database

## نویسنده‌(ها)
<ul>
    <li>
        <a href='https://github.com/enansari'>رحمت انصاری</a>
    </li>
</ul>
<br>

## لایسنس
این نرم افزار از لایسنس 
<a href='https://github.com/EnAnsari/bina-AHLM-django/blob/main/LICENSE'>GPL-3.0 license</a>
استفاده می‌کند.
<br><br>

## قدردانی‌ها
<ul>
    <li>تشکر میکنم از استاد خوب این دوره مهندس <a href='https://github.com/jadijadi'>جادی</a></li>
    <li>همچنین از سایت خوب <a href='https://maktabkhooneh.org/'>مکتب خونه</a> برای <a href='https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%BE%DB%8C%D8%B4%D8%B1%D9%81%D8%AA%D9%87-mk387/'>این دوره</a> عالی</li>
</ul>
<br>
</details>

برای حمایت از این اثر به این مخزن (ریپوزیتوری) ستاره ⭐ بدهید.
<br>
آموزش ساخت اکانت گیت‌هاب را در این مقاله (<a href="https://vrgl.ir/hGsW9">لینک +</a>) ببینید
</div>
