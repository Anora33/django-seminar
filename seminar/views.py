from django.shortcuts import render


def index(request):
    # Mavzular ro'yxati (rasmlar bilan birga)
    topics = [
        {
            'name': 'Kompyuter tarmoqlarini loyihalash',
            'desc': 'Tarmoq topologiyasini tanlash, IP manzillash, sxemalarni rejalashtirish va tarmoq arxitekturasini qurish. Bu bosqichda siz kichik ofisdan tortib yirik korxonalargacha bo\'lgan tarmoqlarni to\'g\'ri rejalashtirishni o\'rganasiz.',
            'image': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoqni boshqarish (Network Management)',
            'desc': 'Tarmoq qurilmalarini monitoring qilish, konfiguratsiya qilish, nosozliklarni aniqlash va tuzatish. Zamonaviy tarmoqlarni masofadan boshqarish va ularning uzluksiz ishlashini ta\'minlash.',
            'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoq xavfsizligi',
            'desc': 'Firewall, VPN, IDS/IPS tizimlari va tarmoq hujumlaridan himoyalanish usullari. Tarmoqni tashqi tahdidlardan himoya qilish va ma\'lumotlar xavfsizligini ta\'minlash.',
            'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Zamonaviy protokollar',
            'desc': 'TCP/IP, OSPF, BGP, VLAN va SDN kabi zamonaviy tarmoq protokollari. Ushbu protokollarni tushunish orqali siz tarmoqning ichki ishlashini chuqur o\'rganasiz.',
            'image': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoq qurilmalari',
            'desc': 'Router, Switch, Access Point kabi qurilmalarni sozlash va ularning ishlash prinsiplari. Amaliy mashg\'ulotlar orqali real qurilmalar bilan ishlash tajribasiga ega bo\'lasiz.',
            'image': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Amaliy loyiha',
            'desc': 'Kichik korxona tarmog\'ini to\'liq loyihalash va uni ishga tushirish bo\'yicha amaliy mashg\'ulot. Kurs yakunida siz mustaqil ravishda tarmoq qurib, uni boshqara olasiz.',
            'image': 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?q=80&w=1000&auto=format&fit=crop'
        },
    ]

    return render(request, 'seminar/index.html', {'topics': topics})


def topics(request):
    # Mavzular ro'yxati (batafsil ma'lumot bilan)
    topics = [
        {
            'name': 'Kompyuter tarmoqlarini loyihalash',
            'desc': 'Tarmoq topologiyasini tanlash, IP manzillash, sxemalarni rejalashtirish va tarmoq arxitekturasini qurish. Bu bosqichda siz kichik ofisdan tortib yirik korxonalargacha bo\'lgan tarmoqlarni to\'g\'ri rejalashtirishni o\'rganasiz.',
            'image': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoqni boshqarish (Network Management)',
            'desc': 'Tarmoq qurilmalarini monitoring qilish, konfiguratsiya qilish, nosozliklarni aniqlash va tuzatish. Zamonaviy tarmoqlarni masofadan boshqarish va ularning uzluksiz ishlashini ta\'minlash.',
            'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoq xavfsizligi',
            'desc': 'Firewall, VPN, IDS/IPS tizimlari va tarmoq hujumlaridan himoyalanish usullari. Tarmoqni tashqi tahdidlardan himoya qilish va ma\'lumotlar xavfsizligini ta\'minlash.',
            'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Zamonaviy protokollar',
            'desc': 'TCP/IP, OSPF, BGP, VLAN va SDN kabi zamonaviy tarmoq protokollari. Ushbu protokollarni tushunish orqali siz tarmoqning ichki ishlashini chuqur o\'rganasiz.',
            'image': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Tarmoq qurilmalari',
            'desc': 'Router, Switch, Access Point kabi qurilmalarni sozlash va ularning ishlash prinsiplari. Amaliy mashg\'ulotlar orqali real qurilmalar bilan ishlash tajribasiga ega bo\'lasiz.',
            'image': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=1000&auto=format&fit=crop'
        },
        {
            'name': 'Amaliy loyiha',
            'desc': 'Kichik korxona tarmog\'ini to\'liq loyihalash va uni ishga tushirish bo\'yicha amaliy mashg\'ulot. Kurs yakunida siz mustaqil ravishda tarmoq qurib, uni boshqara olasiz.',
            'image': 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?q=80&w=1000&auto=format&fit=crop'
        },
    ]

    return render(request, 'seminar/topics.html', {'topics': topics})


def korea(request):
    return render(request, 'seminar/korea.html')


def seminar_detail(request):
    return render(request, 'seminar/korea.html')


def contact(request):
    return render(request, 'seminar/contact.html')