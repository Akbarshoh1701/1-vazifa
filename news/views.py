from django.shortcuts import HttpResponse


def hom_pech(respons):
    return HttpResponse("""
    <h1 style="color: #333;">Asosiy sahifaga xush kelibsiz</h1>
    <ul>
        <li><a href="http://127.0.0.1:8000/news/">So'nggi Yangiliklar</a></li>
        <li><a href="/maqolalar/">Ilmiy Maqolalar</a></li>
        <!-- Boshqa sahifalar uchun linklar shu yerga qo'shing -->
    </ul>

""")


def news(respons):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yangiliklar</title>
</head>
<body>

    <h1>So'nggi Yangiliklar</h1>

    <div>
        <h2>Sun’iy intellekt qanchalik xavfli yoki foydali?</h2>
        <p>— Sun’iy intellekt odamlardan ishini tortib olmaydimi?

— Rostdan ham bu savol hozir juda dolzarb. Sun’iy intellektning o‘zi odamlarning ishini olib qo‘ymaydi. Lekin sun’iy intellektdan unumli foydalana oladigan boshqa odamlar tortib olishi mumkin. Sun’iy intellektning aynan o‘zidan qo‘rqish kerak emas, balki uni yaxshilab o‘rganish kerak.

— Ayni qaysi sohalarda sun’iy intellekt ta’siri sezilmoqda?

— Sun’iy intellekt media soxasiga shiddat bilan kirib keldi ayniqsa. Tasvir ustida ishlash, montaj qilish kabilarda qo‘l kelyapti. Chet elda shu darajaga chiqdiki, televideniyeda boshlovchilarning sun’iy intellekt shakli yaratilib (avatar), dasturlar olib borilmoqda.

— Salbiy tomonlari qanday?

— Salbiy tomonlar hamma narsada bor. Deylik, oddiy pichoqdan oshxona anjomi sifatida foydalanish mumkin, qurol sifatida ham foydalanish mumkin. Sun’iy intellekt ham nima maqsadda, kimning qo‘lida ishlatilishiga qarab foydali yoki zararli bo‘lishi mumkin. Masalan, 2022 yil oxirlari, 2023 yil boshlarida ko‘pgina feyk suratlar tarqaldi, bu orqali feyk xabarlar ham chiqdi. Bir tomondan yaxshi keys bo‘ldi bular, chunki faktcheking qilish kerakligi, tekshirish lozimligi o‘rtaga chiqdi.

— Olamdan o‘tib ketgan dublyaj aktyorlarimizning ovozini sun’iy intellekt orqali tiklash haqida ham gap bor edi. Shu haqida gapirsangiz.

— 2019 yilda rossiyalik rejissyor o‘sha o‘tib ketgan Rossiya aktyorlarining ovozini tiklash loyihasini taqdimot qilgandi. Shunda o‘zbek aktyorlarining ovozini tiklash g‘oyasi paydo bo‘lgan. Shu loyiha ustida 1 yildan beri ishlayapmiz. Hozir Hojiakbar Nurmatov, Sanjar Sa’dullayev, Hamza Umarovlarning ovoz modellarini yaratib ko‘rdik.

Maqsadimiz — shu durdona ovozlarni efirga qaytarish. Shaxsan men bu ovozlarni juda sog‘inganman, xalqimiz ham shunday bo‘lsa kerak. Asosan dublyaj va audiokitoblar yaratishda ishlatish rejalashtirilgan.

— «Boburnoma» loyihasi, jadidlar qiyofasini tiklash ishlari haqida gaplashsak, bu g‘oyalar qanday paydo bo‘lgan?

— Aynan birinchi loyiham «Boburnoma» bo‘lgan. O‘zim tarixni yaxshi ko‘raman. Bobur o‘z asarida shaxslarni tasvirlashda ham, joylarni tasvirlashda ham batafsil tushuntirishlar bergan, bu esa yaxshi baza bo‘lib xizmat qiladi. Taxminan kitobning yarmini tasvirga ko‘chirdik. Bu ishni matnni tasvirga aylantiruvchi sun’iy intellekt dasturi orqali qilganmiz. Birinchi ishlatib boshlaganimiz 3-avlod dasturi edi, unda suratlar unchalik real ko‘rinishda bo‘lmasdi, hozir esa 6-avlod chiqqan allaqachon, bunda suratlar juda real ko‘rinishga ega bo‘ladi.

Jadidlarni yoshlarimiz tanishi, qilgan ishlarini bilishi kerak. Shuning uchun ham birinchilardan bo‘lib jadidlarga to‘xtaldik. Jadidlarning suratini ham yuqorida aytilgan dastur orqali tikladik. Bu suratlarni jamoatchilikka taqdim etganimizda ijobiy qabul qilishdi. Bundan tashqari, oq-qora ko‘rinishdagi suratlarni xam ranglashtirib, detallashtirilgan variantini yaratdik.

Bilamizki, jadidlarimizning saqlangan suratlari asosan qatag‘on paytidagi suratlar, shuning uchun g‘amgin ko‘rinishda va ular tasavvurimizda shunday bo‘lib qolgan. Shuning uchun obrazlarni o‘zgartirib, mag‘rurroq ko‘rinishdagi variantlar ham qilib ko‘rdik.

— Musiqa san’ati borasida sun’iy intellektning ta’siri qanday bo‘lyapti?

— Sun’iy intellektning shunday imkoniyatlari borki, agar qo‘shiq matni berilsa va kerakli janr tanlansa, shunga qarab kuy bastalab qo‘shiq aytib beradi. Masalan, Erkin Vohidovning «Inson» qasidasini rus tiliga tarjima qilib, rok yo‘nalishida qo‘shiq yarattirdik, menimcha, yaxshi chiqdi.

— Boshqa sohalarda sun’iy intellekt ta’siri qanday bo‘lyapti?

— Sun’iy intellekt faqatgina supat generatsiyasi yoki qo‘shiq aytish uchun xizmat qilmaydi. Sun’iy intellekt juda yaxshi yordamchi. Masalan, chet elda sun’iy intellekt yordamida robotlar operatsiyalar o‘tkazyapti, kasallarga tashxis qo‘yyapti.

Bir qiziq keys ham mashhur bo‘ldi. Bir ayol qizi kasal bo‘lganda doktorlarga olib boradi, hech biri aniq tashxis qo‘ya olmaydi. Shunda ayol qizidagi alomatlarni, holatni ChatGPT'ga yozadi, u esa aniq tashxis qo‘yib beradi. Umuman, sun’iy intellekt barcha sohaga kirib bormoqda.

Lekin sun’iy intellekt yordamida haydovchisiz boshqariladigan mashinalarga ishonmagan bo‘lardim. Hali u qadar ideal darajaga yetgani yo‘q.

Media sohasi vakili bo‘lganim uchun ko‘proq shu sohaga urg‘u beraman. Yana masalan, 3D multifilmlarni ishlash uchun oldin bir necha oylab vaqt ketgan bo‘lsa, hozir esa sun’iy intellekt yordamida ancha tezlashdi jarayon. Personajni oddiy so‘zlar yordamida yozib uni yaratish mumkin. Animatsiyada ham sun’iy intellekt juda rivojlanib bormoqda. 2024 yil sun’iy intellekt sohasida animatsiya va jonlashtirish yili bo‘ladi, deb o‘ylayman.</p>
    </div>

    <div>
        <h2>18 davlat sun’iy intellekt texnologiyalarini xavfsiz qilishga chaqirdi</h2>
        <p>AQSh, Buyuk Britaniya, Germaniya va yana 15 davlat iste’molchilarni sun’iy intellektdan (SI) noto‘g‘ri foydalanishdan himoya qilish bo‘yicha kelishuv imzoladi. 27 noyabr, dushanba kuni chop etilgan 20 sahifalik hujjat sun’iy intellekt tizimlarini tajovuzkorlardan himoya qilish bo‘yicha sun’iy intellekt kompaniyalariga tavsiyalar beradi. 

Xususan, sun’iy intellektni ishlab chiquvchi va joriy etuvchi kompaniyalar kiberjinoyatchilarning ulardan foydalanishiga yo‘l qo‘ymaslik va foydalanuvchilar maxfiy ma’lumotlarining uchinchi shaxslarga yetib borishining oldini olish uchun ushbu tizimlarni «tuzilmasi bo‘yicha xavfsiz» qilishi tavsiya etiladi. Shu bilan birga, SI bilan ishlashning barcha bosqichlarida potensial xavflarni hisobga olish kerak: ishlab chiqish, amalga oshirish, foydalanish va texnik xizmat ko‘rsatishda. 

«SI tizimlari standart kiberxavfsizlik tahdidlari bilan bir qatorda, ko‘rib chiqilishi kerak bo‘lgan yangi zaifliklarga duchor bo‘lishi mumkin. Rivojlanish tezligi yuqori bo‘lganda - sun’iy intellektda bo‘lgani kabi - xavfsizlik ko‘pincha so‘nggi o‘rinni egallashi mumkin. Biroq, xavfsizlik faqat ishlab chiqish bosqichida emas, balki tizimning butun hayotiy sikli davomida ham asosiy talab bo‘lishi kerak», — deyiladi hujjatda. 

Ko‘rsatmalar majburiy emas, biroq ekspertlar fikricha, 18 davlat ishtirokidagi kelishuv muhim qadamdir. AQSh Kiberxavfsizlik boshqarmasi va Infratuzilma xavfsizligi agentligi direktori Jyen Isterlining so‘zlariga ko‘ra, ushbu hujjatda SI texnologiyalari «bozorga tezda olib kelinishi mumkin bo‘lgan ajoyib xususiyatlar emas» - ularni ishlab chiqishdagi eng muhim jihat xavfsizlik ekanligi ta’kidlanadi. 

Avvalroq Yevropa Ittifoqi, Germaniya, Fransiya, AQSh va boshqa ba’zi davlatlar, shuningdek, yirik IT-konsernlari vakillari, jumladan ChatGPT’ni yaratgan Open AI kompaniyasi menejyerlari hamda Tesla va SpaceX asoschisi Ilon Mask «Blechli deklaratsiyasi»ni imzolagan edi. U sun’iy intellekt texnologiyalarini xavfsiz ishlab chiqish va joriy etishga chaqiradi. </p>
    </div>

    <div>
        <h2>Google o‘zining eng kuchli Gemini sun’iy intellekt modelini ishga tushirdi</h2>
        <p>U OpenAI kompaniyasining GPT-4 modeliga asosiy raqobatchi bo‘lishi mumkin.

Google kompaniyasi Gemini neyron tarmog‘ini ishga tushirdi. Kompaniya uni sun’iy intellektning eng kuchli va samarali modeli deb atamoqda. 

Gemini uchta komponentni o‘z ichiga oladi: Ultra (eng katta va eng funksional), Pro (keng ko‘lamli vazifalar uchun) va Nano (aniq vazifalar va mobil qurilmalar uchun). Ularning barchasi rasmlar, audio va videolarni qo‘llab-quvvatlaydi. 

Ultra eng kuchli tarmoq bo‘lib, 57 ta fan (matematika, fizika, tarix, huquq, tibbiyot, etika va boshqalar) bo‘yicha ma’lumotlarni o‘z ichiga oladi va mustaqil ravishda faktlarni tekshirish va muammolarni hal qilish imkoniyatiga ega. 

«Gemini - bu turli Google jamoalari o‘rtasidagi hamkorlik mahsulidir. Bu model noldan yaratilgan. U matn, kod, audio, tasvir va videoni o‘z ichiga olgan har xil turdagi ma’lumotlarni umumlashtirishi va oson tushunishi, qayta ishlashi va birlashtirishi mumkin», dedi Sundar Pichai, Alphabet (Google) kompaniyasi bosh direktori. 

Gemini API va boshqa vositalar bilan oson integratsiyalasha oladi. Shu sababli, 13 dekabrdan boshlab ishlab chiquvchilar va korporativ mijozlar Pro modelidan foydalanishi mumkin bo‘ladi. 7 dekabrdan boshlab Google Bard rejalashtirish, murakkab mavzularni tushunish va hokazolarda yordam berish uchun undan foydalana boshlaydi.

Keyinchalik Nano model ishga tushiriladi. Uning yordamida ishlab chiquvchilar Android uchun ilovalar yaratishi mumkin bo‘ladi. 

2024 yilda Ultra modeli asosida Bard Advanced ishga tushiriladi. Bu chatbot joriy qilinganidan beri eng katta yangilanish bo‘ladi.</p>
    </div>
<a href='http://127.0.0.1:8000/'>Oretga</a>
</body>
</html>
"""

    )