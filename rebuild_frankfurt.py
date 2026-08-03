#!/usr/bin/env python3
"""
rebuild_frankfurt.py — Builds the merged Frankfurt events file for the portal.
Combines verified live research (Aug-Oct 2026) with the existing curated events,
deduplicates by normalized title, sorts by date, and writes to the portal.
"""
import json
import os
from datetime import date

PORTAL = os.path.expanduser("~/Desktop/PROJECTS/portal")
OUT = os.path.join(PORTAL, "frankfurt_events.json")

# Existing events (curated knowledge base) — kept if they are still useful
# (loaded from current file by the merge below; we just append new research)

# Newly researched & verified events (Aug–Oct 2026) from live web research.
NEW_EVENTS = [
    {
        "title": "Frankfurter Apfelweinfest",
        "date": "2026-08-07", "time": "12:00 - 23:00",
        "description": "Frankfurt's iconic apple-wine festival transforms the Roßmarkt into a celebration of the region's 'Stöffche' with dozens of stands, live music, Hessian specialties and apple-wine tastings against the skyline. The event runs from 7 to 16 August 2026, with extended hours until 00:00 on Fridays and Saturdays. Entry is free; food and drink are paid.",
        "cost_per_person": "Free entry; food & drink from ~5 EUR",
        "location": "Roßmarkt, 60311 Frankfurt am Main", "image_url": "",
        "category": "Food & Drink", "city": "Frankfurt",
        "website": "https://www.visitfrankfurt.travel/erleben/feste-und-veranstaltungen/frankfurter-apfelweinfest",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Ro%C3%9Fmarkt%2C%2060311%20Frankfurt%20am%20Main",
    },
    {
        "title": "Bernemer Kerb (Bornheimer Kerb)",
        "date": "2026-08-07", "time": "17:00 - 23:00",
        "description": "Frankfurt-Bornheim celebrates its traditional parish fair with rides, food stalls and live music around the Hohen Brunnen fountain and along Berger Straße. The festival runs from 7 to 12 August 2026, opening with the Blues & Folk Night on 7 August. A beloved village-festival atmosphere in the heart of the city.",
        "cost_per_person": "Free entry; rides from ~3 EUR",
        "location": "KerbepLatz, Frankfurt-Bornheim, 60385 Frankfurt am Main", "image_url": "",
        "category": "Festival & Culture", "city": "Frankfurt",
        "website": "https://www.bernemerkerb.de/programm/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Berger%20Stra%C3%9Fe%2C%2060385%20Frankfurt%20am%20Main",
    },
    {
        "title": "Freiluftkino Frankfurt (Open Air Cinema)",
        "date": "2026-08-01", "time": "19:30 - 23:00",
        "description": "Frankfurt's summer open-air cinema screens highlights of the past film year in the courtyard of the former police headquarters. Running from 26 June to 23 August 2026, admission starts at 19:30 with screenings beginning after dusk. Organized by the Lichter Filmfestival since 2020.",
        "cost_per_person": "from ~10 EUR",
        "location": "Altes Polizeipräsidium, Friedrich-Ebert-Anlage 5-11, 60327 Frankfurt am Main", "image_url": "",
        "category": "Film & Cinema", "city": "Frankfurt",
        "website": "https://www.freiluftkinofrankfurt.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Friedrich-Ebert-Anlage%205-11%2C%2060327%20Frankfurt%20am%20Main",
    },
    {
        "title": "Museumsuferfest Frankfurt",
        "date": "2026-08-28", "time": "15:00 - 23:00",
        "description": "One of Europe's largest cultural festivals along both banks of the Main, with over 25 museums, 12 stages and some 400 stands of art, music, international food and crafts. Dragon-boat races on the Main and a grand musical fireworks finale on Sunday evening are the highlights. Runs 28-30 August 2026.",
        "cost_per_person": "Free; museum button ~7 EUR for museum entry",
        "location": "Schaumainkai & Mainufer (Museumsufer), 60594 Frankfurt am Main", "image_url": "",
        "category": "Festival & Culture", "city": "Frankfurt",
        "website": "https://www.museumsufer.de/de/ausstellungen-und-veranstaltungen/museumsuferfest/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Schaumainkai%2C%2060594%20Frankfurt%20am%20Main",
    },
    {
        "title": "Museumsuferfest – Großes Abschlussfeuerwerk",
        "date": "2026-08-30", "time": "22:00 - 22:30",
        "description": "The finale of the Museumsuferfest on Sunday 30 August 2026 is the grand musical fireworks display over the Main, seen best from both riverbanks. Earlier in the day, dragon-boat races draw crowds to the river. A spectacular end to three days of culture and celebration.",
        "cost_per_person": "Free",
        "location": "Mainufer along Museumsufer, 60594 Frankfurt am Main", "image_url": "",
        "category": "Festival & Culture", "city": "Frankfurt",
        "website": "https://www.museumsufer.de/de/ausstellungen-und-veranstaltungen/museumsuferfest/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Mainufer%20Frankfurt%20am%20Main",
    },
    {
        "title": "Herbst-Dippemess Frankfurt",
        "date": "2026-09-11", "time": "14:00 - 23:00",
        "description": "Frankfurt's traditional autumn funfair returns to the Festplatz am Ratsweg with rides, apple wine, fairground food and a lively market. The autumn edition is cozier than the spring one but equally beloved by families. Runs daily from 11 to 27 September 2026.",
        "cost_per_person": "Free entry; rides from ~3 EUR",
        "location": "Festplatz am Ratsweg, Eissporthalle, 60385 Frankfurt am Main", "image_url": "",
        "category": "Seasonal & Markets", "city": "Frankfurt",
        "website": "https://www.visitfrankfurt.travel/erleben/feste-und-veranstaltungen/dippemess/dippemess-im-herbst",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Festplatz%20am%20Ratsweg%2C%2060385%20Frankfurt%20am%20Main",
    },
    {
        "title": "Bundesliga: Eintracht Frankfurt vs FC Augsburg",
        "date": "2026-09-06", "time": "17:30 - 19:30",
        "description": "Eintracht Frankfurt's first home Bundesliga match of the 2026/27 season, hosting FC Augsburg at Deutsche Bank Park. The match kicks off the home campaign on Sunday 6 September 2026 at 17:30. Tickets available via the club's official channels.",
        "cost_per_person": "from ~15 EUR",
        "location": "Deutsche Bank Park, Mörfelder Landstraße 362, 60528 Frankfurt am Main", "image_url": "",
        "category": "Sports", "city": "Frankfurt",
        "website": "https://www.eintracht.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Deutsche%20Bank%20Park%2C%20M%C3%B6rfelder%20Landstra%C3%9Fe%20362%2C%2060528%20Frankfurt",
    },
    {
        "title": "Alte Oper Saisoneröffnung mit dem Treppenhausorchester",
        "date": "2026-09-16", "time": "19:30 - 22:00",
        "description": "The Alte Oper Frankfurt opens its 2026/27 concert season with a free performance by the Treppenhausorchester, an ensemble known for innovative, surprising classical concepts. The venue's halls and foyers are filled with music from midday into the evening. This marks the start of a rich new concert season.",
        "cost_per_person": "Free",
        "location": "Alte Oper Frankfurt, Opernplatz 1, 60313 Frankfurt am Main", "image_url": "",
        "category": "Music & Opera", "city": "Frankfurt",
        "website": "https://www.alteoper.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Alte%20Oper%2C%20Opernplatz%201%2C%2060313%20Frankfurt%20am%20Main",
    },
    {
        "title": "FRATOPIA – Festival der Entdeckungen",
        "date": "2026-09-23", "time": "15:00 - 00:00",
        "description": "The Alte Oper Frankfurt transforms into a living sound-scape for five days with around 250 short concerts at free entry, from 15:00 until midnight each day. Visitors assemble their own personal programme across all halls and foyers. Runs 23-27 September 2026.",
        "cost_per_person": "Free",
        "location": "Alte Oper Frankfurt, Opernplatz 1, 60313 Frankfurt am Main", "image_url": "",
        "category": "Music & Opera", "city": "Frankfurt",
        "website": "https://www.alteoper.de/de/programm/fratopia/18875",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Alte%20Oper%2C%20Opernplatz%201%2C%2060313%20Frankfurt%20am%20Main",
    },
    {
        "title": "Tag des offenen Denkmals Frankfurt",
        "date": "2026-09-13", "time": "10:00 - 18:00",
        "description": "On the European Heritage Open Days, historic monuments across Frankfurt open their doors free of charge, offering tours, workshops and behind-the-scenes access. This nationwide day takes place on Sunday 13 September 2026. A chance to discover hidden heritage sites across the city.",
        "cost_per_person": "Free",
        "location": "Various heritage sites across Frankfurt am Main", "image_url": "",
        "category": "Family & Education", "city": "Frankfurt",
        "website": "https://www.tag-des-offenen-denkmals.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Frankfurt%20am%20Main",
    },
    {
        "title": "Oper Frankfurt: Premiere „La Vestale“ (Spontini)",
        "date": "2026-09-26", "time": "19:30 - 22:30",
        "description": "Oper Frankfurt opens its 2026/27 season with the premiere of Gaspare Spontini's opera 'La Vestale', conducted by Carlo Rizzi and directed by Lydia Steier. A dramatic bel canto work about love and duty. The first performance takes place on 26 September 2026 in the Opera House.",
        "cost_per_person": "from ~40 EUR",
        "location": "Oper Frankfurt, Willy-Brandt-Platz 5-7, 60311 Frankfurt am Main", "image_url": "",
        "category": "Music & Opera", "city": "Frankfurt",
        "website": "https://oper-frankfurt.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Oper%20Frankfurt%2C%20Willy-Brandt-Platz%205-7%2C%2060311%20Frankfurt%20am%20Main",
    },
    {
        "title": "Frankfurter Oktoberfest",
        "date": "2026-09-09", "time": "17:30 - 23:00",
        "description": "Frankfurt's own Oktoberfest takes over the large Festhalle Hausmann tent at Deutsche Bank Park with Bavarian brass music, hearty food and lots of Schunkeln. Running from 9 September to 11 October 2026, it offers a Hessian-Bavarian mix of celebration. Tickets go on advance sale.",
        "cost_per_person": "from ~15 EUR (table/ticket dependent)",
        "location": "Festhalle Hausmann, Deutsche Bank Park, Mörfelder Landstraße 362, 60528 Frankfurt am Main", "image_url": "",
        "category": "Seasonal & Markets", "city": "Frankfurt",
        "website": "https://frankfurter-oktoberfest.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Festhalle%20Hausmann%2C%20M%C3%B6rfelder%20Landstra%C3%9Fe%20362%2C%2060528%20Frankfurt",
    },
    {
        "title": "Städel Museum: „Mary Magdalene. Sin. Pray. Love.“",
        "date": "2026-09-17", "time": "10:00 - 19:00",
        "description": "Major special exhibition at the Städel Museum exploring the figure of Mary Magdalene in art from the Renaissance to the present. Runs from 17 September 2026 to 17 January 2027. Features paintings, sculptures and installations from the museum's collection and international loans.",
        "cost_per_person": "from ~16 EUR",
        "location": "Städel Museum, Schaumainkai 63, 60596 Frankfurt am Main", "image_url": "",
        "category": "Art & Exhibitions", "city": "Frankfurt",
        "website": "https://www.staedelmuseum.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=St%C3%A4del%20Museum%2C%20Schaumainkai%2063%2C%2060596%20Frankfurt%20am%20Main",
    },
    {
        "title": "Städel Museum: Elmgreen & Dragset „Stillleben mit Gemüse“",
        "date": "2026-08-28", "time": "10:00 - 19:00",
        "description": "A major solo exhibition by the artist duo Elmgreen & Dragset at the Städel, on view from 20 May 2026 to 17 January 2027. The work transforms the museum's rooms with large-scale sculptural installations and charged still lifes. Open for visit throughout the August-October period.",
        "cost_per_person": "from ~16 EUR",
        "location": "Städel Museum, Schaumainkai 63, 60596 Frankfurt am Main", "image_url": "",
        "category": "Art & Exhibitions", "city": "Frankfurt",
        "website": "https://www.staedelmuseum.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=St%C3%A4del%20Museum%2C%20Schaumainkai%2063%2C%2060596%20Frankfurt%20am%20Main",
    },
    {
        "title": "Schirn Kunsthalle: „The World Through AI“",
        "date": "2026-08-28", "time": "10:00 - 19:00",
        "description": "The Schirn's major summer exhibition shows artworks of the last ten years engaging with the cognitive, political and ecological dimensions of artificial intelligence. On view at the Schirn's interim location in Bockenheim from 11 June to 20 September 2026. A landmark look at art in the age of machine learning.",
        "cost_per_person": "from ~10 EUR",
        "location": "Schirn Kunsthalle (Interim Bockenheim), Niddastraße 74, 60329 Frankfurt am Main", "image_url": "",
        "category": "Art & Exhibitions", "city": "Frankfurt",
        "website": "https://www.schirn.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Niddastra%C3%9Fe%2074%2C%2060329%20Frankfurt%20am%20Main",
    },
    {
        "title": "Schirn Kunsthalle: Anna Hulačová (Guest Country Czechia)",
        "date": "2026-10-06", "time": "10:00 - 19:00",
        "description": "Coinciding with Czechia's guest-of-honour appearance at the Frankfurt Book Fair, the Schirn focuses on the work of Czech artist Anna Hulačová for the first time in Germany. The exhibition opens in October 2026 and runs until 10 January 2027 at the Schirn's Bockenheim location.",
        "cost_per_person": "from ~10 EUR",
        "location": "Schirn Kunsthalle (Interim Bockenheim), Niddastraße 74, 60329 Frankfurt am Main", "image_url": "",
        "category": "Art & Exhibitions", "city": "Frankfurt",
        "website": "https://www.schirn.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Niddastra%C3%9Fe%2074%2C%2060329%20Frankfurt%20am%20Main",
    },
    {
        "title": "Senckenberg Naturmuseum: Sonderausstellung „Stadtinsekten“",
        "date": "2026-08-28", "time": "09:00 - 18:00",
        "description": "The Senckenberg Nature Museum in Frankfurt presents a special exhibition on the insects that share our cities, exploring urban ecosystems and biodiversity. The permanent dinosaur and natural-history collections remain a family favourite. Open throughout the autumn.",
        "cost_per_person": "from 12 EUR",
        "location": "Senckenberg Naturmuseum, Senckenberganlage 25, 60325 Frankfurt am Main", "image_url": "",
        "category": "Family & Education", "city": "Frankfurt",
        "website": "https://www.senckenberg.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Senckenberg%20Naturmuseum%2C%20Senckenberganlage%2025%2C%2060325%20Frankfurt%20am%20Main",
    },
    {
        "title": "Jazz zum Dritten / Jazz on the Third",
        "date": "2026-10-03", "time": "13:00 - 20:30",
        "description": "Frankfurt's open-air jazz festival on German Unity Day weekend transforms the Römerberg in the historic old town into a stage for outstanding jazz artists. On 3-4 October 2026, soulful ballads and energetic bebop alternate across the main stage. A celebration of Frankfurt's deep jazz heritage.",
        "cost_per_person": "Free",
        "location": "Römerberg, 60311 Frankfurt am Main", "image_url": "",
        "category": "Music & Opera", "city": "Frankfurt",
        "website": "https://www.visitfrankfurt.travel/erleben/feste-und-veranstaltungen/jazz-zum-dritten",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=R%C3%B6merberg%2C%2060311%20Frankfurt%20am%20Main",
    },
    {
        "title": "Frankfurter Buchmesse (Frankfurt Book Fair)",
        "date": "2026-10-07", "time": "09:00 - 18:00",
        "description": "The world's largest trade fair for books and publishing runs from 7 to 11 October 2026 in Frankfurt, with the Czech Republic as guest of honour. Publishers, authors, agents and readers from over 100 countries gather for rights trading, debates and readings. Professional and public days are included.",
        "cost_per_person": "from ~15 EUR (public day)",
        "location": "Messe Frankfurt, Ludwig-Erhard-Anlage 1, 60327 Frankfurt am Main", "image_url": "",
        "category": "Literature & Arts", "city": "Frankfurt",
        "website": "https://www.buchmesse.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Messe%20Frankfurt%2C%20Ludwig-Erhard-Anlage%201%2C%2060327%20Frankfurt",
    },
    {
        "title": "Deutsches Jazzfestival Frankfurt",
        "date": "2026-10-13", "time": "19:30 - 23:00",
        "description": "Five days of world-class contemporary jazz from 13 to 17 October 2026 at venues across Frankfurt, organised by hr (Hessischer Rundfunk). The line-up includes Émile Parisien, Myra Melford, Louis Sclavis, Shake Stew, Emma Rawicz and more. The main concert series takes place in the hr-Sendesaal.",
        "cost_per_person": "from ~25 EUR per concert",
        "location": "hr-Sendesaal, Bertramstraße 8, 60320 Frankfurt am Main", "image_url": "",
        "category": "Music & Opera", "city": "Frankfurt",
        "website": "https://www.hr2.de/veranstaltungen/jazzfestival/index.html",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Bertramstra%C3%9Fe%208%2C%2060320%20Frankfurt%20am%20Main",
    },
    {
        "title": "Mainova Frankfurt Marathon",
        "date": "2026-10-25", "time": "08:00 - 15:00",
        "description": "Frankfurt's annual city marathon since 1981 takes place on Sunday 25 October 2026, with tens of thousands of runners on a flat, fast course along the Main and through the city centre. Events include the marathon, relay and a 10K. A highlight of the autumn sports calendar with great roadside atmosphere.",
        "cost_per_person": "from ~70 EUR (runner); free for spectators",
        "location": "Start & Finish Festhalle, Ludwig-Erhard-Anlage, 60327 Frankfurt am Main", "image_url": "",
        "category": "Sports", "city": "Frankfurt",
        "website": "https://www.frankfurt-marathon.com/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Festhalle%2C%20Ludwig-Erhard-Anlage%2C%2060327%20Frankfurt",
    },
    # ── MAINZ events ──
    {
        "title": "Mainzer Weinmarkt – Weekend 1",
        "date": "2026-08-27", "time": "15:00 - 22:00",
        "description": "Rheinhessen's largest wine festival fills the Mainzer Stadtpark with around 100 winemakers, regional food and live music in a romantic Rosengarten setting. Weekend one runs 27-30 August 2026, ahead of a second long weekend in September. Around 300,000 visitors attend across both weekends.",
        "cost_per_person": "Free entry; wine glasses & tasting from ~4 EUR",
        "location": "Stadtpark & Volkspark Mainz, 55116 Mainz", "image_url": "",
        "category": "Food & Drink", "city": "Mainz",
        "website": "https://www.mainzer-weinmarkt.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Stadtpark%20Mainz%2C%2055116%20Mainz",
    },
    {
        "title": "Mainzer Weinmarkt – Weekend 2",
        "date": "2026-09-03", "time": "15:00 - 22:00",
        "description": "The second weekend of the Mainzer Weinmarkt runs from 3 to 6 September 2026 in the Stadtpark, featuring the same celebrated stands, live stages and a special anniversary of '90 Jahre Alt-Mainzer Stadtsoldaten'. Visitors can sample wines from Mainz, Rheinhessen, Rheingau and Nahe.",
        "cost_per_person": "Free entry; wine tasting from ~4 EUR",
        "location": "Stadtpark & Volkspark Mainz, 55116 Mainz", "image_url": "",
        "category": "Food & Drink", "city": "Mainz",
        "website": "https://www.mainzer-weinmarkt.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Stadtpark%20Mainz%2C%2055116%20Mainz",
    },
    {
        "title": "FILMZ Freiluftkino im Landesmuseum Mainz",
        "date": "2026-08-16", "time": "21:00 - 23:00",
        "description": "Ten open-air cinema evenings in the courtyard of the Landesmuseum Mainz, programmed by the FILMZ festival, run from mid-August to 6 September 2026. Films from around the world are screened under the late-summer sky with drinks and popcorn. Tickets available in advance online.",
        "cost_per_person": "from ~10 EUR",
        "location": "Landesmuseum Mainz, Große Bleiche 49-51, 55116 Mainz", "image_url": "",
        "category": "Film & Cinema", "city": "Mainz",
        "website": "https://www.filmz-mainz.de/programm/freiluftkino/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Landesmuseum%20Mainz%2C%20Gro%C3%9Fe%20Bleiche%2049-51%2C%2055116%20Mainz",
    },
    {
        "title": "Mainz leuchtet – Late Light Festival",
        "date": "2026-09-24", "time": "19:00 - 23:00",
        "description": "Mainz's late light festival turns the city centre into a glowing work of art for three evenings, with buildings from the Rheingoldhalle to Schillerplatz illuminated by artistic light and video projections. Runs 24-26 September 2026. A magical, free after-dark experience for all ages.",
        "cost_per_person": "Free",
        "location": "City centre: Rheingoldhalle to Schillerplatz, 55116 Mainz", "image_url": "",
        "category": "Festival & Culture", "city": "Mainz",
        "website": "https://www.mainz.de/freizeit-und-sport/feste-und-veranstaltungen/mainz-leuchtet-late-light-festival.php",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Schillerplatz%2C%2055116%20Mainz",
    },
    {
        "title": "Staatstheater Mainz: Premiere „Lohengrin“ (Wagner)",
        "date": "2026-10-04", "time": "18:00 - 21:30",
        "description": "The Staatstheater Mainz opens its 2026/27 music-theatre season with Richard Wagner's 'Lohengrin', conducted by Generalmusikdirektor Gabriel Venzago and staged by Erik Raskopf. The premiere takes place on 4 October 2026 in the Großes Haus. A grand romantic opera to open the new season.",
        "cost_per_person": "from ~20 EUR",
        "location": "Staatstheater Mainz, Gutenbergplatz 7, 55116 Mainz", "image_url": "",
        "category": "Music & Opera", "city": "Mainz",
        "website": "https://staatstheater-mainz.com/veranstaltungen/oper-25-26/lohengrin",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Staatstheater%20Mainz%2C%20Gutenbergplatz%207%2C%2055116%20Mainz",
    },
    {
        "title": "Interkulturelle Woche & Interkulturelles Fest Mainz",
        "date": "2026-09-13", "time": "11:00 - 19:00",
        "description": "Mainz's Intercultural Week runs 11-20 September 2026 with encounters, talks, exhibitions and cultural dialogue. The highlight Intercultural Festival fills the Domplatz on Sunday 13 September with international food stalls, music and a real Kyrgyz yurt. Free and open to all.",
        "cost_per_person": "Free",
        "location": "Domplatz, 55116 Mainz", "image_url": "",
        "category": "Festival & Culture", "city": "Mainz",
        "website": "https://www.mainz.de/angebote-entdecken/soziales-und-gesellschaft/interkulturelles-arbeitsmarktintegration/interkulturelle-woche",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Domplatz%2C%2055116%20Mainz",
    },
    {
        "title": "Rheingau Musik Festival – Konzerte rund um Mainz",
        "date": "2026-08-28", "time": "19:30 - 22:00",
        "description": "The Rheingau Musik Festival runs from 20 June to early September 2026, offering 158 concerts at 26 venues across the region including Wiesbaden, Mainz and the Rheingau. Classical highlights with international stars such as The King's Singers, VOCES8 and Hayato Sumino close the season in late summer.",
        "cost_per_person": "from ~30 EUR",
        "location": "Various venues around Mainz and Wiesbaden", "image_url": "",
        "category": "Music & Opera", "city": "Mainz",
        "website": "https://www.rheingau-musik-festival.de/",
        "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Wiesbaden%20und%20Mainz",
    },
]

def main():
    # Load existing events to keep
    existing = []
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            existing = json.load(f).get("events", [])

    seen = set()
    merged = []
    for e in existing:
        t = " ".join((e.get("title") or "").lower().split())
        if t and t not in seen:
            seen.add(t)
            merged.append(e)

    added = 0
    for e in NEW_EVENTS:
        t = " ".join((e.get("title") or "").lower().split())
        if t and t not in seen:
            seen.add(t)
            merged.append(e)
            added += 1

    # Sort by date ascending
    merged.sort(key=lambda e: (e.get("date") or "9999-99-99"))

    data = {
        "last_updated": str(date.today()),
        "research_date": str(date.today()),
        "center": {"city": "Frankfurt am Main", "latitude": 50.1109, "longitude": 8.6821},
        "events": merged,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Frankfurt events: {len(merged)} total (kept {len(merged)-added}, added {added} new)")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
