#!/usr/bin/env python3
"""Składa makietę MyWay: wspólny nagłówek, stopka i bloki + treść każdej podstrony.
Uruchom: python3 build.py  (pliki .html lądują w katalogu głównym makiety)."""
import pathlib

KAT = pathlib.Path(__file__).parent
NE = '<span class="ne" aria-hidden="true"></span>'

EF_KUP = 'https://myway-szczecin.cms.efitness.com.pl/kup-karnet'
EF_GRAFIK = 'https://myway-szczecin.cms.efitness.com.pl/kalendarz-zajec'
EF_LOGIN = 'https://myway-szczecin.cms.efitness.com.pl/Login/SystemLogin'
FITSSEY = 'https://app.fitssey.com/MywayReformway/backoffice.v4/schedule'
BOOKSY = 'https://booksy.com/pl-pl/347736_myself-cosmetology_salon-kosmetyczny_18078_szczecin'
TEL = 'tel:+48513590488'
MAPA = 'https://www.google.com/maps/search/?api=1&amp;query=MyWay+Fitness+Sarnia+8+Szczecin'

MENU = [('oferta.html', 'Oferta'), (EF_GRAFIK, 'Grafik'), ('cennik.html', 'Cennik'), ('reformway.html', 'Reformway'),
        ('myself.html', 'Myself'), ('squash.html', 'Squash'), ('o-nas.html', 'O nas'), ('kontakt.html', 'Kontakt')]
MENU_MOB = [('oferta.html', 'Oferta'), ('silownia.html', 'Siłownia'), ('zajecia.html', 'Zajęcia fitness'),
            ('reformway.html', 'Reformway'), ('myself.html', 'Myself Cosmetology'), ('squash.html', 'Squash'),
            ('treningi-personalne.html', 'Treningi personalne'), ('cennik.html', 'Cennik'), (EF_GRAFIK, 'Grafik'),
            ('o-nas.html', 'O nas'), ('kontakt.html', 'Kontakt'), (EF_LOGIN, 'Strefa klienta')]


def klasy_grafik():
    """Grafiki z grafiki/PROMPTY.md włączają się dopiero, gdy plik jest na miejscu (bez 404 do tego czasu)."""
    g = KAT / 'grafiki'
    pliki = (('ma-cien', 'cien-okno-desktop.webp'), ('ma-lisc', 'lisc-palma.webp'), ('ma-fakture', 'faktura-tynk.webp'),
             ('ma-swiatlo-ziel', 'swiatlo-na-zieleni.webp'), ('ma-ob-silownia', 'obiekt-silownia.webp'), ('ma-ob-zajecia', 'obiekt-zajecia.webp'),
             ('ma-ob-myself', 'obiekt-myself.webp'), ('ma-ob-squash', 'obiekt-squash.webp'), ('ma-ob-trening', 'obiekt-trening.webp'),
             ('ma-roslina', 'roslina-kentia.webp'), ('ma-galazka', 'cien-galazka.webp'), ('ma-mgla', 'faktura-mgla.webp'), ('ma-recznik', 'obiekt-recznik.webp'))
    k = [n for n, plik in pliki if (g / plik).exists()]
    return f' class="{" ".join(k)}"' if k else ''


def linki(lista, biezaca):
    return ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == biezaca else ""}>{t}</a>' for h, t in lista)


def szkielet(plik, tytul, opis, tresc):
    return f'''<!doctype html>
<html lang="pl"{klasy_grafik()}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tytul}</title>
<meta name="description" content="{opis}">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styl.css">
</head>
<body>
<a class="pomin" href="#tresc">Przejdź do treści</a>

<header class="naglowek"><div class="wrap">
  <a class="logo" href="index.html" aria-label="MyWay Fitness, strona główna"><img src="img/logo-biale-400.png" width="400" height="114" alt="MyWay Fitness Squash Social"></a>
  <nav class="menu" aria-label="Menu główne">{linki(MENU, plik)}</nav>
  <a class="naglowek__strefa" href="{EF_LOGIN}">Strefa klienta</a>
  <a class="btn btn--ziel" href="{EF_KUP}">Kup karnet {NE}</a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-mob"><i></i><span>Menu</span></button>
</div></header>

<div class="menu-mob" id="menu-mob" hidden>
  <div class="menu-mob__gora"><img src="img/logo-biale-400.png" width="400" height="114" alt="MyWay Fitness"><button class="menu-btn" type="button" data-zamknij style="display:inline-flex">Zamknij</button></div>
  <nav aria-label="Menu">{linki(MENU_MOB, plik)}</nav>
  <a class="btn btn--ziel" href="{EF_KUP}">Kup karnet online {NE}</a>
  <a class="menu-mob__tel" href="{TEL}">Zadzwoń: 513 590 488</a>
</div>

<main id="tresc">
{tresc}
</main>

<footer class="stopka">
  <div class="wrap stopka__gora">
    <img src="img/logo-biale-400.png" width="400" height="114" alt="MyWay Fitness Squash Social" loading="lazy">
    <nav aria-label="Stopka"><a href="oferta.html">Oferta</a><a href="{EF_GRAFIK}">Grafik</a><a href="cennik.html">Cennik</a><a href="squash.html">Squash</a><a href="o-nas.html">O nas</a><a href="kontakt.html">Kontakt</a><a href="#">Regulamin</a></nav>
  </div>
  <div class="wrap stopka__srodek">
    <div class="stopka__social"><a href="https://www.youtube.com/channel/UCWiUShpWaqfhhGyXd7vyCig">YouTube</a><a href="https://www.facebook.com/profile.php?id=100063970067813">Facebook</a><a href="https://www.instagram.com/mywayfitness.szczecin/">Instagram</a></div>
    <span>ul. Sarnia 8, 71-777 Szczecin Warszewo</span>
  </div>
  <div class="stopka__dol"><div class="wrap"><span>MyWay Fitness Squash &amp; Social, Szczecin</span><span>Regulamin, polityka prywatności</span></div></div>
</footer>

<script src="js/strona.js" defer></script>
</body>
</html>
'''


# ── wspólne bloki ──────────────────────────────────────────────

def gosc(h2='Przyjdź jako gość, zostań stałym bywalcem: <span class="serif">wykup karnet.</span>',
         p='Pierwsze wejście i trening wprowadzający są u nas gratis. Zadzwoń, a umówimy dzień.',
         akcje=None, foto='img/grupa-usmiech.webp', w=1400, h=933, tlo_ciemne=False):
    akcje = akcje or [(EF_KUP, 'Kup karnet online', 'ziel', True), (TEL, 'Wejście gratis: 513 590 488', 'bialy', False)]
    przyciski = ''.join(f'<a class="btn btn--{k}" href="{u}">{t}{" " + NE if s else ""}</a>' for u, t, k, s in akcje)
    styl = ' style="background:#fff"' if not tlo_ciemne else ''
    return f'''<section class="gosc ciemne"{styl}><div class="wrap" style="padding-top:clamp(56px,7vw,96px)">
  <div class="gosc__scena"><div class="gosc__ramka">
    <img src="{foto}" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">
    <div><h2>{h2}</h2><p>{p}</p></div>
    <div class="gosc__akcje">{przyciski}</div>
  </div></div>
</div></section>'''


def gosc_glowna():
    # na stronie głównej baner zaczyna się na zielonym pasie usług
    return gosc().replace(' style="background:#fff"', '').replace(' style="padding-top:clamp(56px,7vw,96px)"', '')


KARNETY = {
    'caly': [
        ('', 'Sport', 'Trenujesz, kiedy chcesz', '239 zł', 'abonament, miesiąc wypowiedzenia',
         ['Siłownia i zajęcia bez limitu', 'Sauna fińska', '1 h z trenerem personalnym co rok', '30 dni zawieszenia w roku'], False),
        ('Najkorzystniej', 'MyWay 360', '12 miesięcy w cenie 9', '179 zł', 'płacisz raz 2 151 zł za 12 miesięcy',
         ['Siłownia i zajęcia bez limitu', 'Sauna fińska', 'Pomiary składu ciała bez limitu', '3 miesiące gratis'], True),
        ('', 'Sailor', 'Często wyjeżdżasz', '299 zł', 'abonament',
         ['Siłownia i zajęcia bez limitu', 'Sauna fińska', 'Wielokrotne zawieszenie karnetu'], False)],
    'rano': [
        ('Hit poranków', 'Południowy', 'W tygodniu do 15:00, weekendy bez limitu', '199 zł', 'abonament',
         ['Siłownia i poranne zajęcia', 'Sauna w godzinach karnetu', 'Pomiary składu ciała bez limitu'], True),
        ('55+', 'Senior', 'Pon.-pt. do 15:00', '179 zł', 'abonament',
         ['Siłownia i poranne zajęcia', 'Sauna w godzinach karnetu', 'Pomiary składu ciała bez limitu'], False),
        ('Z legitymacją', 'Student', 'Do 15:00, weekendy bez limitu', '179 zł', 'abonament',
         ['Siłownia i poranne zajęcia', 'Sauna w godzinach karnetu', '30 dni zawieszenia w roku'], False)],
    'ref': [
        ('Reformway', 'Reformer rano', 'Zajęcia 7:00-16:00', '389 zł', '4-5 wejść w miesiącu, grupa 3-5 osób',
         ['Maszyny Balanced Body', 'Siłownia OPEN i sauna fińska', 'Strefa relaksu: herbata i ciasteczka'], False),
        ('Reformway', 'Reformer po pracy', 'Zajęcia 16:00-21:00', '419 zł', '4-5 wejść w miesiącu, grupa 3-5 osób',
         ['Maszyny Balanced Body', 'Siłownia OPEN i sauna fińska', 'Strefa relaksu: herbata i ciasteczka'], True)],
}


def karta(k):
    znak, nazwa, dla, cena, uwaga, lista, hit = k
    li = ''.join(f'<li>{x}</li>' for x in lista)
    return (f'<div class="karnet{" karnet--hit" if hit else ""}"><p class="karnet__znak">{znak}</p><h3>{nazwa}</h3>'
            f'<p class="karnet__dla">{dla}</p><p class="karnet__cena">{cena}<small> / mies.</small></p><p class="karnet__uwaga">{uwaga}</p>'
            f'<ul>{li}</ul><a class="btn btn--{"ziel" if hit else "obrys"}" href="{EF_KUP}">Kup {nazwa} {NE}</a></div>')


def tabela(klucz):
    k = KARNETY[klucz]
    return f'<div class="tabela{" tabela--2" if len(k) == 2 else ""}">{"".join(karta(x) for x in k)}</div>'


def karnety(h2='Wybierz karnet <span class="serif">w minutę.</span>', poziom='h2'):
    return f'''<section class="sekcja karnety" id="cennik"><div class="wrap">
  <{poziom}>{h2}</{poziom}>
  <p class="karnety__lead">Powiedz, kiedy chcesz trenować, a pokażemy tylko pasujące karnety.</p>
  <div class="wybor" role="tablist" aria-label="Kiedy chcesz trenować">
    <button role="tab" aria-selected="true" aria-controls="p-caly" id="t-caly">Cały dzień</button>
    <button role="tab" aria-selected="false" aria-controls="p-rano" id="t-rano">Rano, do 15:00</button>
    <button role="tab" aria-selected="false" aria-controls="p-ref" id="t-ref">Pilates reformer</button>
  </div>
  <div class="panel" id="p-caly" role="tabpanel" aria-labelledby="t-caly">{tabela("caly")}</div>
  <div class="panel" id="p-rano" role="tabpanel" aria-labelledby="t-rano" hidden>{tabela("rano")}</div>
  <div class="panel" id="p-ref" role="tabpanel" aria-labelledby="t-ref" hidden>{tabela("ref")}</div>
  <p class="karnety__info">Cennik aktualny na listopad 2026. W każdym karnecie pomiary składu ciała Jawon Medical i sauna fińska. Abonament ma miesięczny okres wypowiedzenia.</p>
</div></section>'''


KONTAKT = f'''<section class="kontakt ciemne" id="kontakt"><div class="wrap">
  <div class="kontakt__gora">
    <h2>Chcesz poćwiczyć? <span class="serif">Wzmocnić kondycję?</span></h2>
    <div>
      <p>Zadbać o swoje zdrowie, a może po prostu aktywnie wypocząć? Przyjdź do nas. A jeśli masz pytania, zadzwoń lub napisz.</p>
      <a class="btn btn--bialy" href="{MAPA}">Wyznacz trasę {NE}</a>
    </div>
  </div>
  <dl class="kontakt__dane">
    <div><dt>Zadzwoń do nas</dt><dd><a href="{TEL}">+48 513 590 488</a></dd></div>
    <div><dt>Napisz do nas</dt><dd><a href="mailto:kontakt@mywayfitness.pl">kontakt@mywayfitness.pl</a></dd></div>
    <div><dt>Odwiedź nas</dt><dd>ul. Sarnia 8, 71-777 Szczecin<br>parking przy klubie</dd></div>
    <div><dt>Godziny</dt><dd>pon.-pt. 6:00-23:00<br>sob.-nd. 8:00-18:00</dd></div>
  </dl>
</div></section>'''

MEDICOVER = '''<section class="medicover"><div class="wrap">
  <h2>Honorujemy karty <span class="serif">Medicover Sport.</span></h2>
  <img src="img/medicover-sport.webp" width="360" height="233" alt="Karta Medicover Sport" loading="lazy" decoding="async">
</div></section>'''


def pod_hero(foto, w, h, alt, h1, lead, akcje=(), poz='center 45%', okruszki=()):
    sciezka = [('index.html', 'Strona główna')] + list(okruszki or OKRUSZKI.get(BIEZACA, []))
    ol = ''.join(f'<li><a href="{u}">{t}</a></li>' if u else f'<li aria-current="page">{t}</li>' for u, t in sciezka)
    przyciski = ''.join(f'<a class="btn btn--{k}" href="{u}">{t} {NE}</a>' for u, t, k in akcje)
    return f'''<section class="pod-hero">
  <div class="hero__tlo"><img src="{foto}" width="{w}" height="{h}" sizes="100vw" alt="{alt}" fetchpriority="high" style="object-position:{poz}"></div>
  <div class="wrap pod-hero__srodek">
    <nav class="okruszki" aria-label="Jesteś tutaj"><ol>{ol}</ol></nav>
    <h1>{h1}</h1>
    <p class="pod-hero__lead">{lead}</p>
    {f'<div class="pod-hero__akcje">{przyciski}</div>' if przyciski else ''}
  </div>
</section>'''


# przedmiot ze świata usługi na krawędzi zdjęcia i następnej sekcji (grafiki/PROMPTY.md, część 6)
OBIEKTY = {'silownia.html': 'silownia', 'zajecia.html': 'zajecia', 'reformway.html': 'lisc',
           'myself.html': 'myself', 'squash.html': 'squash', 'treningi-personalne.html': 'trening'}


def hero_uslugi(foto, w, h, alt, h1, lead, akcje=(), poz='center 45%', okruszki=()):
    """Nagłówek strony usługowej: panel w zieleni klubu (tynk + światło z okien) z tekstem, zdjęcie do prawej krawędzi."""
    sciezka = [('index.html', 'Strona główna')] + list(okruszki or OKRUSZKI.get(BIEZACA, []))
    ol = ''.join(f'<li><a href="{u}">{t}</a></li>' if u else f'<li aria-current="page">{t}</li>' for u, t in sciezka)
    przyciski = ''.join(f'<a class="btn btn--{k}" href="{u}">{t} {NE}</a>' for u, t, k in akcje)
    obiekt = OBIEKTY.get(BIEZACA, '')
    return f'''<section class="hero-usl">
  <div class="hero-usl__foto"><img src="{foto}" width="{w}" height="{h}" sizes="(min-width: 901px) 56vw, 100vw" alt="{alt}" fetchpriority="high" style="object-position:{poz}">{f'<div class="obiekt obiekt--{obiekt}" aria-hidden="true"></div>' if obiekt else ''}</div>
  <div class="wrap hero-usl__siatka">
    <div class="hero-usl__tekst">
      <nav class="okruszki" aria-label="Jesteś tutaj"><ol>{ol}</ol></nav>
      <h1>{h1}</h1>
      <p class="hero-usl__lead">{lead}</p>
      {f'<div class="hero-usl__akcje">{przyciski}</div>' if przyciski else ''}
    </div>
  </div>
</section>'''


def wiersz(foto, w, h, alt, h2, wstep='', tekst=(), lista=(), akcje=(), odwr=False, id_=''):
    t = ''.join(f'<p class="usluga__tekst">{x}</p>' for x in tekst)
    li = f'<ul class="lista">{"".join(f"<li>{x}</li>" for x in lista)}</ul>' if lista else ''
    btn = ''.join(f'<a class="btn btn--{k}" href="{u}">{tx} {NE}</a>' for u, tx, k in akcje)
    return f'''<div class="usluga{" usluga--odwr" if odwr else ""}"{f' id="{id_}"' if id_ else ''}>
    <div class="usluga__foto"><img src="{foto}" width="{w}" height="{h}" sizes="(min-width: 900px) 55vw, 100vw" alt="{alt}" loading="lazy" decoding="async"></div>
    <div><h2>{h2}</h2>{f'<p class="usluga__wstep">{wstep}</p>' if wstep else ''}{t}{li}{btn}</div>
  </div>'''


def sekcja(tresc, klasa='', id_=''):
    return f'<section class="sekcja {klasa}"{f" id=\"{id_}\"" if id_ else ""}><div class="wrap">{tresc}</div></section>'


def naglowek(h2, p=''):
    return f'<div class="naglowek-sekcji"><h2>{h2}</h2>{f"<p>{p}</p>" if p else ""}</div>'


def kolumny(lista):
    return f'<div class="kolumny kolumny--{len(lista)}">' + ''.join(
        f'<div class="kolumna"><h3>{h}</h3><p>{p}</p>{f"<a href=\"{u}\">{t} {NE}</a>" if u else ""}</div>'
        for h, p, u, t in lista) + '</div>'


def trenerzy(lista, duze=False, kol=0):
    klasa = ' trenerzy--duze' if duze else (f' trenerzy--k{kol}' if kol else '')
    przewijane = ' role="region" aria-label="Trenerki, przesuń w bok" tabindex="0"' if duze else ''
    return f'<div class="trenerzy{klasa}"{przewijane}>' + ''.join(
        f'<figure class="trener"><div class="trener__foto"><img src="img/{f}.webp" width="{"733" if duze else "800"}" height="{"1100" if duze else "1200"}" alt="{n}" sizes="{"(min-width: 900px) 30vw, 80vw" if duze else "(min-width: 1000px) 22vw, 45vw"}" loading="lazy" decoding="async"></div><figcaption><h3>{n}</h3>{f"<p>{r}</p>" if r else ""}</figcaption></figure>'
        for f, n, r in lista) + '</div>'


def faq(lista):
    return '<div class="faq">' + ''.join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="faq__odp">{a}</div></details>'
        for i, (q, a) in enumerate(lista)) + '</div>'


def ceny(bloki):
    return f'<div class="ceny{" ceny--1" if len(bloki) == 1 else ""}">' + ''.join(
        f'<div><h3>{h}</h3><ul>{"".join(f"<li><span>{a}</span><b>{b}</b></li>" for a, b in pozycje)}</ul></div>'
        for h, pozycje in bloki) + '</div>'


# ── dane ───────────────────────────────────────────────────────

T_FITNESS = [('t-julia', 'Julia', ''), ('t-dagmara', 'Dagmara', 'Instruktorka fitness od sztang oraz pilatesu'),
             ('t-daniel', 'Daniel', ''), ('t-michal', 'Michał', 'Instruktor cross’a, Hyroxa i mocnego brzucha'),
             ('t-magda', 'Magda', ''), ('t-kamila', 'Kamila', ''), ('t-krzysztof', 'Krzysztof', ''),
             ('t-ola-w', 'Ola Wójcik', 'Instruktorka zajęć step basic'),
             ('t-ola-f', 'Ola Fydryszewska', 'Instruktorka treningu obwodowego'),
             ('t-jakub', 'Jakub Kurowski', 'Instruktor zajęć zdrowy kręgosłup i gymnastic movement'),
             ('t-maciej', 'Maciej Pawłowski', 'Instruktor BJJ'), ('t-hania', 'Hania Paluta', ''),
             ('t-agnieszka-s', 'Agnieszka Szelążek', ''), ('t-irmina', 'Irmina Łachacz', ''),
             ('t-joanna', 'Joanna Szpotańska', 'Instruktorka zajęć fit boost')]
T_SILOWNIA = [('t-julia', 'Julia', ''), ('t-krzysztof', 'Krzysztof', ''), ('t-kamila', 'Kamila', ''),
              ('t-michal', 'Michał', 'Instruktor cross’a, Hyroxa i mocnego brzucha'),
              ('t-ola-f', 'Ola Fydryszewska', 'Instruktorka treningu obwodowego'),
              ('t-maciej', 'Maciej Pawłowski', 'Instruktor BJJ'), ('t-wojciech', 'Wojciech Galant', 'Trener squasha')]
T_REFORMWAY = [
    ('rw-sara', 'Sara', 'Z ruchem jestem od zawsze, najpierw była scena i taniec: balet, współczesny, rewia, musical. Dziś łączę pilatesowe fundamenty z tanecznym charakterem. Głównie reformer, czasem mata.'),
    ('rw-dagmara', 'Dagmara', 'Z fitnessem jestem związana od 2008 roku, a z pilatesem od 2011. Najbliższy jest mi klasyczny styl pracy: precyzyjny, świadomy i wymagający.'),
    ('rw-julia', 'Julia', 'Zaczęłam od treningu siłowego, potem przyszła joga i pilates. Lubię łączyć siłę, mobilność, kontrolę i świadomość ciała.'),
    ('rw-hania', 'Hania', 'Zaczęłam od zajęć fitness, potem przyszedł pilates: najpierw mata, z czasem reformer. Na zajęciach stawiam na świadomy ruch i dobrą energię.'),
    ('rw-agnieszka', 'Agnieszka', 'Magister wychowania fizycznego, trenerka personalna i medyczna, certyfikowana trenerka Blackroll. Prowadzę treningi 1:1, zajęcia prozdrowotne i reformer.'),
    ('rw-ania', 'Ania', 'Interesuje mnie, jak świadomy ruch wspiera nas w przeciążeniu, stresie czy wypaleniu. Łączę intensywną, dopasowaną pracę z uważnością.')]

FAQ_ZAJECIA = [
    ('Czy na zajęcia trzeba się zapisywać wcześniej?', f'Tak, polecamy. Zapiszesz się w <a href="{EF_GRAFIK}">grafiku online</a>, przez aplikację, telefonicznie albo w recepcji klubu.'),
    ('Czy mogę przyjść, jeśli jestem początkujący?', 'Oczywiście. Większość zajęć jest odpowiednia dla początkujących, a instruktor pomoże Ci dobrać poziom. W grafiku znajdziesz zajęcia o różnej intensywności.'),
    ('Jak się ubrać i co zabrać?', 'Wygodny podkoszulek, legginsy albo spodenki, zmienne obuwie sportowe, butelka wody i ręcznik na matę.'),
    ('Czy mogę odwołać rezerwację?', 'Tak, najpóźniej godzinę przed rozpoczęciem zajęć: w aplikacji albo telefonicznie.'),
    ('Czy mogę zobaczyć klub przed zakupem karnetu?', f'Tak. Zadzwoń pod <a href="{TEL}">513 590 488</a>, a chętnie oprowadzimy Cię po klubie. Pierwsze wejście jest gratis.')]

FAQ_SQUASH = [
    ('Jak zacząć grać w squasha?', 'Na start nie musisz znać zasad. Polecamy pierwszy trening z trenerem: pokaże, jak trzymać rakietę, serwować i o co chodzi w grze. Umówimy Cię w recepcji.'),
    ('Jak przygotować się do pierwszej gry?', 'Pamiętaj o właściwym obuwiu halowym. Wystarczy koszulka, krótkie spodenki, ręcznik i woda. Rakietę i piłeczki wypożyczysz w recepcji.'),
    ('Nie mam pary. Z kim zagram?', 'Daj znać w recepcji. Znajdziemy klubowicza na Twoim poziomie albo umówimy Cię na grę z trenerem.')]

CENY_SQUASH = [
    ('Pon.-pt. 6:00-16:00, weekendy i święta', [('Kort, 1 h', '64 zł'), ('Cena ulgowa*, 1 h', '54 zł'), ('Karnet 9 h + 1 h gratis', '580 zł')]),
    ('Pon.-pt. 16:00-23:00', [('Kort, 1 h', '84 zł'), ('Karnet 9 h + 1 h gratis', '760 zł')]),
    ('Wypożyczenie sprzętu', [('Rakieta, 1 h', '10 zł'), ('Piłeczki', '3,5 zł')])]
PRZYPIS_SQUASH = ('<p class="przypis">* Cena ulgowa: młodzież szkolna z aktualną legitymacją i studenci do 26 lat, przy wynajmie kortu do 15:00 od poniedziałku do piątku oraz w weekendy i święta.</p>'
                  '<p class="przypis">Rezerwacja nieodwołana 24 godziny przed grą jest traktowana jak wykorzystana.</p>')
CENY_PT = [('Treningi personalne', [('1 trening', '210 zł'), ('4 treningi', '799 zł'), ('8 treningów', '1390 zł'), ('Trening dla 2 osób', '340 zł')])]

OPINIE_MYSELF = [
    ('Klimatyczne miejsce, z cudownymi Paniami. Profesjonalne podejście do klienta. Polecam gorąco.', 'Agnieszka, Booksy'),
    ('Pani Kornelia cudownie zadbała o to, bym poczuła się rozluźniona i zrelaksowana. Po masażu w lustrze widzę realne uniesienie skóry oraz czuję rozluźnienie szczęki.', 'Hanna, Booksy'),
    ('Zdecydowanie najlepszy gabinet kosmetologiczny! Dziewczyny mają ogromną wiedzę i potrafią idealnie dobrać zabiegi do potrzeb skóry.', 'Gosia, Google'),
    ('Po zabiegu czuję się doskonale. Gabinet jest bardzo elegancki, a pani Magda wykonuje zabieg z dużą wprawą.', 'Ewa, Booksy'),
    ('Jestem bardzo zadowolona z masażu Kobido wykonanego przez Panią Kornelię. Pełen profesjonalizm, zaangażowanie i bardzo miła atmosfera.', 'Wiktoria, Booksy'),
    ('Pani Magda ma złote ręce: pełne wyczucia, siły i delikatności jednocześnie. Zdecydowanie polecam.', 'Marzena, Booksy')]


# ── podstrony ──────────────────────────────────────────────────

def oferta():
    karty = [('silownia.html', 'zajecia-hyrox', 734, 1100, 'Siłownia', 'Sprzęt SportsArt Premium i ECO-POWR'),
             ('zajecia.html', 'zajecia-grupa', 1067, 1600, 'Zajęcia fitness', 'Ponad 60 h zajęć w tygodniu'),
             ('reformway.html', 'reformway-800', 800, 1066, 'Reformway', 'Pilates na reformerach, grupy 3-5 osób'),
             ('myself.html', 'myself-twarz', 1067, 1600, 'Myself Cosmetology', 'Gabinet kosmetologii w klubie'),
             ('squash.html', 'squash-800', 800, 800, 'Squash', '2 korty i Akademia Squasha'),
             ('treningi-personalne.html', 'personalny', 900, 900, 'Treningi personalne', 'Pierwszy trening wprowadzający gratis')]
    rzad = '<div class="strefy__rzad strefy__rzad--3">' + ''.join(
        f'<a class="strefa" href="{u}"><img src="img/{f}.webp" width="{w}" height="{h}" sizes="(min-width: 1000px) 33vw, (min-width: 560px) 50vw, 100vw" alt="" loading="lazy" decoding="async"><span class="strefa__tresc"><span class="strefa__nazwa">{n}</span><span class="strefa__opis">{o}</span><span class="strefa__wiecej">Zobacz więcej {NE}</span></span></a>'
        for u, f, w, h, n, o in karty) + '</div>'
    return '\n'.join([
        pod_hero('img/hero-pelny.webp', 2000, 1333, 'Klubowicze MyWay na zajęciach', 'Oferta. <span class="serif">Wszystko pod jednym dachem.</span>',
                 'Siłownia, zajęcia, pilates na reformerach, squash, treningi personalne i kosmetologia. Klub przy Sarniej 8 na Warszewie.'),
        sekcja(naglowek('Strefa <span class="serif">aktywności.</span>') + rzad),
        sekcja(naglowek('Dla dzieci <span class="serif">i młodzieży.</span>', 'Trenujesz spokojnie, bo dziecko też ma swoje zajęcia.') + kolumny([
            ('Klubik dla dzieci', 'Gdy trenujesz, dziecko bawi się pod opieką animatorek. W cenie Twojego karnetu.', '', ''),
            ('Akademia Squasha', 'Zajęcia w grupach 4-6 osób z trenerem Wojciechem Galantem. Sprzęt do nauki zapewniamy.', 'squash.html', 'Zobacz squash'),
            ('Półkolonie', 'Organizujemy je w wakacje: sport, zabawa i nowe przyjaźnie pod okiem doświadczonych opiekunów.', '', ''),
            ('Treningi dla młodzieży', 'Indywidualne treningi z trenerem personalnym, dopasowane do wieku i formy.', 'treningi-personalne.html', 'Treningi personalne')]), 'sekcja--mgla'),
        sekcja(naglowek('Strefa <span class="serif">rozwoju.</span>') + kolumny([
            ('Treningi personalne', 'Trener dobierze plan do Twojego celu i będzie pilnował postępów. Karnety treningów kupisz w recepcji.', 'treningi-personalne.html', 'Zobacz więcej'),
            ('Trening squasha z trenerem', 'Chcesz nauczyć się grać albo podnieść poziom gry? Umówimy Cię na trening indywidualny.', 'squash.html', 'Zobacz squash'),
            ('Weekendowe warsztaty', 'Krótkie spotkania z fizjoterapeutą, trenerami, dietetykiem i blogerami sportowymi.', '', ''),
            ('Eventy', 'Wydarzenia w klubie i aktywności poza nim, które łączą ludzi, ruch i dobrą energię.', '', '')])),
        sekcja(naglowek('Strefa <span class="serif">relaksu.</span>', 'Po treningu nie musisz od razu wychodzić.') + kolumny([
            ('Kawiarnia i fit bar', 'Świeżo parzona kawa, zdrowe przekąski, koktajle po treningu i shoty przed nim.', '', ''),
            ('Sushi bar', 'W budynku klubu jest restauracja sushi: zupa miso, nigiri i maki, także na wynos.', '', ''),
            ('Sauna fińska', 'W każdym karnecie. Najlepsze zakończenie wieczornego treningu.', 'cennik.html', 'Zobacz karnety')]), 'ciemne'),
        gosc(), MEDICOVER])


def silownia():
    return '\n'.join([
        hero_uslugi('img/silownia.webp', 1400, 933, 'Siłownia MyWay', 'Siłownia <span class="serif">SportsArt Premium.</span>',
                 'Przestronna sala z widokiem na drzewa, sprzęt klasy premium i instruktorzy, którzy zawsze znajdą czas, żeby pomóc.',
                 [(EF_KUP, 'Kup karnet', 'ziel')]),
        sekcja(wiersz('img/silownia-ludzie.webp', 1400, 933, 'Trening z hantlami na siłowni MyWay', 'Trzy strefy <span class="serif">w jednej sali.</span>',
                      'Ładna, przestronna i świetnie wyposażona sala.',
                      lista=['Strefa wolnych ciężarów i maszyn siłowych', 'Strefa cardio przy dużym oknie z widokiem na drzewa i zieleń',
                             'Strefa treningu funkcjonalnego i cross fitu, także dla kalisteniki i street workoutu'])
               + wiersz('img/sarnia-tlo-1200.webp', 1200, 800, 'Klubowiczki na orbitrekach przy oknach', 'Pierwsi w Szczecinie <span class="serif">z ECO-POWR.</span>',
                        tekst=['Urządzenia ECO-POWR zamieniają Twój trening w prąd, który zasila telewizory i oświetlenie w klubie. Na swoim profilu zbierasz punkty i odbierasz za nie nagrody.',
                               'Maszyny SportsArt mają pasy kevlarowe, dzięki którym pracują płynnie, cicho i bezpiecznie.'], odwr=True)
               + wiersz('img/personalny.webp', 900, 900, 'Trener pomaga klubowiczce w ćwiczeniu', 'W cenie <span class="serif">każdego karnetu.</span>',
                        lista=['Pomiary składu ciała analizatorem Jawon Medical', 'Sauna fińska', 'Pomoc instruktora na sali'],
                        akcje=[('cennik.html', 'Zobacz karnety', 'obrys')])),
        sekcja(naglowek('Nasi <span class="serif">trenerzy.</span>') + trenerzy(T_SILOWNIA, kol=4), 'sekcja--mgla'),
        gosc(), MEDICOVER])


def zajecia():
    return '\n'.join([
        hero_uslugi('img/hero-zajecia.webp', 1600, 1067, 'Zajęcia grupowe w MyWay', 'Zajęcia <span class="serif">fitness.</span>',
                 'Ponad 60 godzin zajęć w tygodniu, teraz także w nowej sali. Od Hyroxu po jogę i zdrowy kręgosłup.',
                 [(EF_GRAFIK, 'Grafik i zapisy', 'ziel')]),
        sekcja(wiersz('img/zajecia-hyrox.webp', 734, 1100, 'Trening funkcjonalny w MyWay', 'Hyrox. <span class="serif">Sprawdź swoje granice.</span>',
                      tekst=['Połączenie biegania, siły i treningu funkcjonalnego, które angażuje całe ciało. Pracujesz nad wytrzymałością, mocą i kondycją.',
                             'W grafiku są też treningi siłowe i funkcjonalne, mobility i sporty walki.'])
               + wiersz('img/zajecia-joga.webp', 734, 1100, 'Zajęcia rozciągające w MyWay', 'Joga, pilates, <span class="serif">stretching.</span>',
                        tekst=['Zajęcia, które łączą ruch, regenerację i dobre samopoczucie. Popracujesz nad mobilnością, siłą i elastycznością, a przy okazji oderwiesz się od codziennego tempa.'], odwr=True)
               + wiersz('img/zajecia-mata.webp', 1000, 1008, 'Zajęcia na matach z trenerem', 'Zdrowy kręgosłup <span class="serif">i zajęcia 50+.</span>',
                        tekst=['Spokojny, bezpieczny ruch dla pleców i stawów. Dla osób 55+ jest karnet Senior: siłownia, poranne zajęcia i sauna za 179 zł miesięcznie.'],
                        akcje=[(EF_GRAFIK, 'Sprawdź grafik', 'obrys')])),
        sekcja(naglowek('Poznaj naszych <span class="serif">trenerów.</span>') + trenerzy(T_FITNESS, kol=5), 'sekcja--mgla'),
        sekcja(naglowek('Pytania <span class="serif">i odpowiedzi.</span>') + faq(FAQ_ZAJECIA)),
        gosc(), MEDICOVER])


def reformway():
    return '\n'.join([
        hero_uslugi('img/reformway-studio.webp', 1600, 1067, 'Trenerki w studiu Reformway', 'Reformway. <span class="serif">Pilates na reformerach.</span>',
                 'Kameralne studio w stylu Bali, maszyny Balanced Body i grupy od 3 do 5 osób.',
                 [(FITSSEY, 'Zapisz się w Fitssey', 'ziel'), ('#karnety-ref', 'Karnety', 'bialy')], 'center 35%'),
        sekcja(wiersz('img/reformway-studio-2.webp', 1600, 1067, 'Ćwiczenie na reformerze przy oknie', 'Dla początkujących <span class="serif">i zaawansowanych.</span>',
                      tekst=['Reformer wzmacnia mięśnie, poprawia elastyczność i równowagę. Zajęcia dopasowujemy do poziomu, więc każdy pracuje w swoim tempie i z poprawną techniką.',
                             'Regularny trening pomaga zredukować stres i poprawić postawę.'])
               + wiersz('img/reformer-zajecia.webp', 1000, 1333, 'Wieczorne zajęcia w studiu Reformway', 'Wieczorny reformer <span class="serif">i sauna.</span>',
                        tekst=['Wieczorem światła są przygaszone, muzyka płynie spokojnie, a Ty możesz zwolnić po intensywnym dniu. Po treningu zapraszamy do sauny.'], odwr=True)
               + wiersz('img/reformer-poza.webp', 700, 1050, 'Ćwiczenie na reformerze', 'Zapisy online, <span class="serif">bez stałego grafiku.</span>',
                        tekst=['W aplikacji Fitssey wybierasz termin, który Ci pasuje: rano, po południu albo wieczorem. To dobre rozwiązanie przy pracy zmianowej lub nieregularnym dniu.',
                               'Wolisz stałe zajęcia? Mamy stałe grupy i karnety Reformer.'],
                        akcje=[(FITSSEY, 'Zapisz się w Fitssey', 'ziel')])),
        f'<section class="sekcja sekcja--mgla" id="karnety-ref"><div class="wrap">{naglowek("Karnety <span class=\"serif\">Reformway.</span>", "W karnecie także miesiąc siłowni OPEN, sauna fińska, pomiary składu ciała i strefa relaksu.")}{tabela("ref")}<p class="karnety__info">Karnet w postaci abonamentu z miesięcznym okresem wypowiedzenia.</p></div></section>',
        sekcja(naglowek('Poznaj <span class="serif">trenerki.</span>') + trenerzy(T_REFORMWAY, duze=True)),
        gosc('Pierwszy trening <span class="serif">na reformerze?</span>', 'Zapisz się online w Fitssey albo zadzwoń, a dobierzemy grupę do Twojego poziomu.',
             [(FITSSEY, 'Zapisz się w Fitssey', 'ziel', True), (TEL, 'Zadzwoń: 513 590 488', 'bialy', False)], 'img/studio-okna.webp', 1000, 1333),
        MEDICOVER])


def myself():
    return '\n'.join([
        hero_uslugi('img/myself-gabinet.webp', 1600, 1067, 'Specjalistki Myself Cosmetology', 'Myself <span class="serif">Cosmetology.</span>',
                 'Gabinet kosmetologii w Myway Fitness. Trening to początek, regeneracja i pielęgnacja to kolejny krok.',
                 [(BOOKSY, 'Umów wizytę w Booksy', 'ziel')], 'center 30%'),
        sekcja(wiersz('img/myself-cialo.webp', 1067, 1600, 'Zabieg na ciało w gabinecie Myself Cosmetology', 'Zabiegi <span class="serif">dla osób aktywnych.</span>',
                      'Po wysiłku ciało potrzebuje odpoczynku i wsparcia w regeneracji.',
                      lista=['Regeneracja i odprężenie', 'Nawilżenie i odżywienie skóry', 'Mniej napięcia i zmęczenia', 'Nowość w gabinecie: zabiegi na ciało'],
                      akcje=[(BOOKSY, 'Zobacz zabiegi i terminy', 'ziel')])),
        sekcja(f'<div class="duet"><div class="duet__tekst"><h2>Magda <span class="serif">i Kornelia.</span></h2><p>Nasze specjalistki dbają o komfort klientek na każdym etapie wizyty: indywidualne podejście, dyskrecja i spokojna, przyjazna atmosfera.</p><a class="btn btn--ziel" href="{BOOKSY}">Umów wizytę {NE}</a></div>'
               + trenerzy([('my-magda', 'Magda', ''), ('my-kornelia', 'Kornelia', '')]) + '</div>', 'sekcja--mgla'),
        sekcja(naglowek('Opinie <span class="serif">klientek.</span>') + '<div class="opinie">' + ''.join(
            f'<figure class="opinia"><blockquote>„{t}”</blockquote><figcaption>{k}</figcaption></figure>' for t, k in OPINIE_MYSELF) + '</div>'),
        gosc('Umów wizytę <span class="serif">w Booksy.</span>', 'Wybierz zabieg i termin online albo zapytaj w recepcji klubu.',
             [(BOOKSY, 'Umów wizytę w Booksy', 'ziel', True), (TEL, 'Zadzwoń: 513 590 488', 'bialy', False)], 'img/myself-gabinet.webp', 1600, 1067),
        MEDICOVER])


def squash():
    return '\n'.join([
        hero_uslugi('img/squash-kort.webp', 1000, 1000, 'Kort do squasha w MyWay', 'Squash. <span class="serif">To dopiero są emocje.</span>',
                 'Dwa nowoczesne korty z amortyzowaną podłogą, wentylacją i klimatyzacją.',
                 [(TEL, 'Zarezerwuj kort: 513 590 488', 'ziel')]),
        sekcja(naglowek('Ceny <span class="serif">kortów.</span>') + ceny(CENY_SQUASH) + PRZYPIS_SQUASH),
        sekcja(wiersz('img/squash.webp', 900, 900, 'Kort do squasha w MyWay', 'Dwa korty, <span class="serif">pełny komfort.</span>',
                      tekst=['Specjalna podłoga amortyzuje każdy krok i odciąża stawy. Wentylacja dostarcza świeże powietrze przez cały mecz, a klimatyzacja trzyma dobrą temperaturę.',
                             'Kort zarezerwujesz w recepcji albo telefonicznie, rakietę i piłeczki wypożyczysz na miejscu.'],
                      akcje=[(TEL, 'Zarezerwuj kort', 'ziel')])),
        sekcja(naglowek('Akademia <span class="serif">Squasha.</span>') + kolumny([
            ('Dla kobiet', 'Trenujesz w grupie, od początku pod okiem trenera. Uczysz się techniki, nabierasz formy i poznajesz osoby, z którymi umówisz się na wspólną grę.', '', ''),
            ('Dla dzieci i młodzieży', 'Im wcześniej, tym lepiej: na korcie świetnie radzi sobie nawet sześciolatek. Grupy 4-6 osób, sprzęt do nauki zapewniamy.', '', ''),
            ('Sekcja juniorska', 'Poniedziałki o 16:00 (6-9 lat) i o 17:00 (10-13 lat). Zajęcia prowadzi trener Wojciech Galant.', '', '')]), 'sekcja--mgla'),
        sekcja('<div class="profil"><div class="profil__foto"><img src="img/t-wojciech.webp" width="800" height="1200" alt="Wojciech Galant, trener squasha" loading="lazy" decoding="async"></div>'
               '<div class="profil__tekst"><h2>Wojciech <span class="serif">Galant.</span></h2><p class="profil__rola">Trener squasha w Myway Fitness</p>'
               '<p>Prowadzi Akademię Squasha i treningi indywidualne. Zapisy dzieci i ceny zajęć ustalisz bezpośrednio z trenerem.</p>'
               '<a class="btn btn--obrys" href="tel:+48728800208">Zadzwoń: 728 800 208 ' + NE + '</a></div></div>'),
        sekcja(naglowek('Pytania <span class="serif">i odpowiedzi.</span>') + faq(FAQ_SQUASH), 'sekcja--mgla'),
        gosc(), MEDICOVER])


def treningi():
    return '\n'.join([
        hero_uslugi('img/trener.webp', 1000, 1000, 'Trener personalny MyWay z klubowiczką', 'Treningi <span class="serif">personalne.</span>',
                 'Twoja przemiana jest naszą motywacją. Pierwszy trening wprowadzający z trenerem jest bezpłatny.',
                 [(TEL, 'Umów pierwszy trening', 'ziel'), ('#ceny-pt', 'Ceny treningów', 'bialy')]),
        sekcja(wiersz('img/personalny.webp', 900, 900, 'Trening personalny w MyWay', 'Plan <span class="serif">tylko dla Ciebie.</span>',
                      tekst=['Pracujemy według indywidualnego planu: ćwiczenia dobieramy do Twojego celu, poziomu, sprawności i ewentualnych dolegliwości.',
                             'Trener pokazuje technikę, na bieżąco poprawia błędy, pilnuje bezpieczeństwa i motywuje.'])),
        sekcja(naglowek('Nad czym <span class="serif">możemy pracować?</span>') + kolumny([
            ('Modelowanie sylwetki', 'Dobrze dobrany trening siłowy uwydatnia mięśnie, a mocniejsze mięśnie to mniejsze ryzyko kontuzji.', '', ''),
            ('Redukcja tkanki tłuszczowej', 'Trening i odpowiednia dieta pomagają zmniejszyć masę ciała, także ze względów zdrowotnych.', '', ''),
            ('Mniej bólu kręgosłupa', 'Ćwiczenia zwiększające ruchomość kręgosłupa zmniejszają dolegliwości i zapobiegają zwyrodnieniom.', '', ''),
            ('Lepsza kondycja', 'Sprawne krążenie to niższe ciśnienie, niższe tętno spoczynkowe i łatwiejsza codzienność.', '', ''),
            ('Zdrowe kości i stawy', 'Trening siłowy zwiększa gęstość kości i pomaga zapobiegać osteoporozie.', '', '')]), 'sekcja--mgla'),
        sekcja(naglowek('Cennik <span class="serif">treningów.</span>', 'O większe pakiety zapytaj w klubie.') + ceny(CENY_PT), id_='ceny-pt'),
        sekcja(naglowek('Nasi <span class="serif">trenerzy.</span>') + trenerzy(T_SILOWNIA, kol=4), 'sekcja--mgla'),
        gosc('Pierwszy trening <span class="serif">z trenerem gratis.</span>', 'Zadzwoń, a dobierzemy trenera do Twojego celu i umówimy termin.',
             [(TEL, 'Zadzwoń: 513 590 488', 'ziel', True), (EF_KUP, 'Kup karnet online', 'bialy', True)]),
        MEDICOVER])


def cennik():
    return '\n'.join([
        pod_hero('img/silownia-sala.webp', 1361, 907, 'Sala siłowni MyWay', 'Cennik. <span class="serif">Zostań z nami na dłużej.</span>',
                 'Siłownia, ponad 60 godzin zajęć, sauna i pomiary składu ciała. A dziecko w tym czasie bawi się w klubiku, w cenie Twojego karnetu.',
                 [(EF_KUP, 'Kup karnet online', 'ziel')]),
        karnety(),
        sekcja(naglowek('Treningi personalne <span class="serif">i squash.</span>') + ceny(CENY_PT + CENY_SQUASH) + PRZYPIS_SQUASH
               + '<p class="przypis">Akademia Squasha dla dzieci i młodzieży: zapisy i ceny u trenera Wojciecha Galanta, <a href="tel:+48728800208">728 800 208</a>.</p>', 'sekcja--mgla'),
        gosc(), MEDICOVER])


def o_nas():
    galeria = '<div class="galeria">' + ''.join(
        f'<img src="img/zespol-{n}.webp" width="667" height="1000" sizes="(min-width: 700px) 30vw, 50vw" alt="Zespół MyWay" loading="lazy" decoding="async">'
        for n in ['8140', '0764', '0930', '1341', '9596', '9288']) + '</div>'
    return '\n'.join([
        pod_hero('img/wnetrze.webp', 1200, 798, 'Wnętrze klubu MyWay z dużymi oknami', 'Sportowa <span class="serif">strona życia.</span>',
                 'Klub na Warszewie, w którym każdy, kto chce żyć aktywnie, może powiedzieć: to jest właśnie to.'),
        sekcja(wiersz('img/wlasciciele.webp', 700, 700, 'Agnieszka i Michał, właściciele MyWay', 'Kto stoi <span class="serif">za Myway?</span>',
                      'Agnieszka i Michał, pomysłodawcy i właściciele klubu.',
                      tekst=['„Od kilku lat marzyłam o miejscu, w którym każdy, kto chce prowadzić aktywny tryb życia, mógłby powiedzieć: to jest właśnie to. Sama jestem aktywna i bywałam w wielu klubach, więc wiedziałam, co działa, a czego brakuje.”',
                             '„Na Warszewie brakowało miejsca, w którym można aktywnie spędzić czas z rodziną albo przyjaciółmi, a potem zostać jeszcze chwilę, porozmawiać i odpocząć.”'])),
        sekcja(naglowek('Co wyróżnia <span class="serif">Myway?</span>', 'U nas jest wszystko: intensywny trening, miejsce na relaks i ludzie, którzy się znają. I jest dla wszystkich, bez względu na wiek, kondycję czy sytuację rodzinną.') + kolumny([
            ('Nowocześnie', 'Sprzęt SportsArt Premium, przestronne wnętrza i duże okna z widokiem na drzewa.', '', ''),
            ('Rodzinnie', 'Klubik z animatorkami, Akademia Squasha i Myway Kids Academy dla dzieci.', '', ''),
            ('Ekologicznie', 'Urządzenia ECO-POWR zamieniają trening w prąd dla klubu.', '', ''),
            ('Parking', 'Bezpłatne miejsca bezpośrednio przy klubie.', '', ''),
            ('Chill zone', 'Kawiarnia w lobby, strefa relaksu, sauna fińska i sushi bar w budynku.', '', '')]), 'sekcja--mgla'),
        sekcja(naglowek('Poznaj <span class="serif">Myway Team.</span>') + galeria),
        gosc(), KONTAKT, MEDICOVER])


def kontakt():
    form = f'''<div class="form-kontakt">
  <div class="form-kontakt__opis"><h2>Napisz <span class="serif">do nas.</span></h2><p>Odpowiadamy w godzinach pracy klubu. Szybciej? Zadzwoń pod <a href="{TEL}">513 590 488</a>.</p></div>
  <form id="kontakt-form" novalidate>
    <div class="form-pola">
      <div class="pole"><label for="k-imie">Imię i nazwisko</label><input id="k-imie" name="imie" type="text" autocomplete="name" required></div>
      <div class="pole"><label for="k-tel">Telefon</label><input id="k-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel"></div>
      <div class="pole"><label for="k-mail">E-mail</label><input id="k-mail" name="email" type="email" autocomplete="email" required></div>
      <div class="pole"><label for="k-tresc">Wiadomość</label><textarea id="k-tresc" name="tresc" required></textarea></div>
      <label class="zgoda"><input type="checkbox" required> Zgadzam się na przetwarzanie moich danych przez MyWay Fitness w celu odpowiedzi na wiadomość.</label>
      <button class="btn btn--ziel" type="submit">Wyślij wiadomość {NE}</button>
    </div>
    <div class="dzieki" hidden tabindex="-1"><strong>Dziękujemy!</strong>Odpowiemy najszybciej, jak to możliwe.</div>
  </form>
</div>'''
    return '\n'.join([
        pod_hero('img/sarnia-tlo.webp', 2400, 1600, 'Klubowiczki na orbitrekach przy dużych oknach MyWay', 'Kontakt. <span class="serif">Wpadnij na Sarnią 8.</span>',
                 'Przyjdź do nas. Jeśli masz pytania, zadzwoń lub napisz.',
                 [(TEL, 'Zadzwoń: 513 590 488', 'ziel'), (MAPA, 'Wyznacz trasę', 'bialy')]),
        KONTAKT, sekcja(form), MEDICOVER])


def glowna():
    t = (KAT / 'strony' / 'index.html').read_text(encoding='utf-8')
    return (t.replace('{{gosc}}', gosc_glowna()).replace('{{karnety}}', karnety())
             .replace('{{kontakt}}', KONTAKT).replace('{{medicover}}', MEDICOVER))


STRONY = {
    'index.html': ('MyWay Fitness Szczecin: siłownia, zajęcia, pilates, squash', 'Kameralny klub fitness na Warszewie: siłownia, zajęcia grupowe, pilates na reformerach, squash i kosmetologia.', glowna),
    'oferta.html': ('Oferta | MyWay Fitness Szczecin', 'Siłownia, zajęcia fitness, Reformway, Myself Cosmetology, squash i treningi personalne w jednym klubie na Warszewie.', oferta),
    'silownia.html': ('Siłownia Szczecin Warszewo | MyWay Fitness', 'Siłownia SportsArt Premium z urządzeniami ECO-POWR, strefą cardio przy oknach i pomocą instruktorów.', silownia),
    'zajecia.html': ('Zajęcia fitness Szczecin | MyWay Fitness', 'Ponad 60 godzin zajęć w tygodniu: Hyrox, joga, pilates, stretching, zdrowy kręgosłup. Zapisy online.', zajecia),
    'reformway.html': ('Pilates reformer Szczecin | Reformway w MyWay', 'Studio pilatesu na reformerach Balanced Body, grupy 3-5 osób, zapisy online w Fitssey.', reformway),
    'myself.html': ('Myself Cosmetology | gabinet w MyWay Fitness', 'Gabinet kosmetologii w klubie MyWay: zabiegi regenerujące, pielęgnacja i nowe zabiegi na ciało. Zapisy w Booksy.', myself),
    'squash.html': ('Squash Szczecin | korty MyWay Fitness', 'Dwa nowoczesne korty do squasha na Warszewie, Akademia Squasha dla kobiet i dzieci, cennik kortów.', squash),
    'treningi-personalne.html': ('Trener personalny Szczecin | MyWay Fitness', 'Treningi personalne w MyWay: indywidualny plan, pierwszy trening wprowadzający gratis, cennik od 210 zł.', treningi),
    'cennik.html': ('Cennik karnetów | MyWay Fitness Szczecin', 'Karnety na siłownię i zajęcia od 179 zł miesięcznie, karnety Reformway, treningi personalne i squash.', cennik),
    'o-nas.html': ('O nas | MyWay Fitness Szczecin', 'Agnieszka i Michał oraz zespół MyWay. Rodzinny klub na Warszewie z siłownią, zajęciami, squashem i strefą relaksu.', o_nas),
    'kontakt.html': ('Kontakt | MyWay Fitness, ul. Sarnia 8, Szczecin', 'MyWay Fitness, ul. Sarnia 8, 71-777 Szczecin. Tel. 513 590 488, kontakt@mywayfitness.pl. Pon.-pt. 6-23, sob.-nd. 8-18.', kontakt),
}

OF = ('oferta.html', 'Oferta')
OKRUSZKI = {'oferta.html': [(None, 'Oferta')], 'silownia.html': [OF, (None, 'Siłownia')], 'zajecia.html': [OF, (None, 'Zajęcia fitness')],
            'reformway.html': [OF, (None, 'Reformway')], 'myself.html': [OF, (None, 'Myself Cosmetology')], 'squash.html': [OF, (None, 'Squash')],
            'treningi-personalne.html': [OF, (None, 'Treningi personalne')], 'cennik.html': [(None, 'Cennik')], 'o-nas.html': [(None, 'O nas')],
            'kontakt.html': [(None, 'Kontakt')]}
BIEZACA = ''

_szer = {}


def szerokosc(plik):
    if plik not in _szer:
        from PIL import Image
        _szer[plik] = Image.open(plik).width
    return _szer[plik]


def srcset(html):
    """Każdy obraz bez srcset dostaje warianty 400/800/1200 (z img/), żeby telefon nie pobierał zdjęć 2000 px."""
    import re

    def zamien(m):
        tag = m.group(0)
        if 'srcset=' in tag:
            return tag
        z = re.search(r'src="img/([^"/]+)\.webp"', tag)
        if not z:
            return tag
        baza = re.sub(r'-(400|800|1200)$', '', z.group(1))
        org = KAT / 'img' / f'{baza}.webp'
        if not org.exists():
            return tag
        warianty = [(f'img/{baza}-{v}.webp', v) for v in (400, 800, 1200) if (KAT / 'img' / f'{baza}-{v}.webp').exists()]
        if not warianty:
            return tag
        warianty.append((f'img/{baza}.webp', szerokosc(org)))
        dodatek = ' srcset="' + ', '.join(f'{u} {w}w' for u, w in warianty) + '"'
        if 'sizes=' not in tag:
            dodatek += ' sizes="(min-width: 1000px) 50vw, 100vw"'
        return tag.replace('<img ', '<img' + dodatek + ' ', 1)
    html = re.sub(r'<img [^>]+>', zamien, html)

    def proporcje(m):
        # proporcje z width/height w zmiennej --r: na telefonie zdjęcie bez kadrowania, ale z zarezerwowanym miejscem (CLS)
        tag = m.group(0)
        w, h = re.search(r'width="(\d+)"', tag), re.search(r'height="(\d+)"', tag)
        if not (w and h) or '--r:' in tag:
            return tag
        r = f'--r:{w.group(1)}/{h.group(1)};'
        if 'style="' in tag:
            return tag.replace('style="', 'style="' + r, 1)
        return tag.replace('<img ', f'<img style="{r}" ', 1)
    return re.sub(r'<img [^>]+>', proporcje, html)


def galazka(html):
    """Cień gałązki pada na ścianę przy ramce jednego zdjęcia na stronę: ostatni wiersz w jasnej sekcji, daleko od cienia okna."""
    import re
    ostatni = None
    for m in re.finditer(r'<div class="usluga(?: usluga--\w+)*"', html):
        sekcja = html.rfind('<section class="', 0, m.start())
        klasy = html[sekcja:html.find('"', sekcja + 16)]
        if 'ciemne' not in klasy and 'uslugi' not in klasy:
            ostatni = m
    if not ostatni:
        return html
    return html[:ostatni.end() - 1] + ' usluga--galazka"' + html[ostatni.end():]


def orientacja(html):
    """Wiersz zdjęcie + tekst dostaje kolumny według proporcji zdjęcia: poziome 7/12, kwadratowe 6/12, pionowe 5/12 (bez kadrowania)."""
    import re

    def zamien(m):
        w, h = int(m.group(3)), int(m.group(4))
        r = w / h
        typ = ' usluga--pion' if r < .85 else (' usluga--kw' if r < 1.2 else '')
        return m.group(1) + typ + m.group(2)
    html = re.sub(r'(<div class="usluga(?: usluga--odwr)?)("[^>]*>\s*<div class="usluga__foto"><img[^>]*?width="(\d+)" height="(\d+)")', zamien, html)

    def baner(m):
        w, h = int(m.group(3)), int(m.group(4))
        return m.group(1) + (' gosc__ramka--pion' if w / h < .85 else '') + m.group(2)
    return re.sub(r'(<div class="gosc__ramka)(">\s*<img[^>]*?width="(\d+)" height="(\d+)")', baner, html)


def twarde_spacje(html):
    """Jednoliterowe spójniki i przyimki nie zostają na końcu linii (tylko w widocznym tekście body)."""
    import re
    glowa, cialo = html.split('<body>', 1)
    czesci = re.split(r'(<script[\s\S]*?</script>|<[^>]+>)', cialo)
    for i, c in enumerate(czesci):
        if c and not c.startswith('<'):
            czesci[i] = re.sub(r'(^|[\s(„])([aiouwzAIOUWZ]) ', r'\1\2&nbsp;', c)
    return glowa + '<body>' + ''.join(czesci)


if __name__ == '__main__':
    for plik, (tytul, opis, fn) in STRONY.items():
        BIEZACA = plik
        html = orientacja(twarde_spacje(srcset(szkielet(plik, tytul, opis, fn()))))
        # światło z hero przechodzi na pierwszą jasną sekcję pod nim
        if 'class="pod-hero"' in html or 'class="hero-usl"' in html:
            i = html.index('class="pod-hero"') if 'class="pod-hero"' in html else html.index('class="hero-usl"')
            j = html.find('<section class="sekcja ', i)
            if j > 0:
                html = html[:j] + '<section class="sekcja swiatlo ' + html[j + len('<section class="sekcja '):]
        html = galazka(html)
        (KAT / plik).write_text(html, encoding='utf-8')
        print('zbudowano', plik)
