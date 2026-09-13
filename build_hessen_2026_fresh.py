#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build hessen_events.json - detailed Hessen (excl. Frankfurt/Mainz) events,
research date 2026-09-13, window 2026-09-13 .. 2026-11-22.
Every entry traces to a live source gathered on 2026-09-13 (festam.app, rheingau.de,
wiesbaden.de Jahreskalender 2026 PDF, giessen.de Veranstaltungen, eventfinder.de,
documenta.de, hlmd.de, schaustellerverband Hessen Kirmes term list, etc.).
"""
import json, urllib.parse, os, datetime

D = {  # city -> (lat, lon, distance_from_frankfurt_km)
    "Wiesbaden": (50.0820, 8.2400, 35),
    "Hochheim am Main": (50.0130, 8.3520, 25),
    "Eltville am Rhein": (50.0250, 8.1180, 45),
    "Rüdesheim am Rhein": (49.9790, 8.2900, 58),
    "Geisenheim": (49.9843, 8.0331, 62),
    "Oestrich-Winkel": (50.0056, 8.0086, 60),
    "Kiedrich": (50.0400, 8.0850, 50),
    "Darmstadt": (49.8728, 8.6512, 29),
    "Marburg": (50.8022, 8.7667, 75),
    "Gießen": (50.5841, 8.6784, 54),
    "Fulda": (50.5558, 9.6808, 103),
    "Kassel": (51.3127, 9.4797, 162),
    "Hanau": (50.1264, 8.9169, 18),
    "Offenbach am Main": (50.0956, 8.7761, 9),
    "Bad Homburg vor der Höhe": (50.2268, 8.6183, 15),
    "Bad Nauheim": (50.3648, 8.7389, 28),
    "Limburg an der Lahn": (50.3833, 8.0500, 55),
    "Wetzlar": (50.5561, 8.5006, 66),
    "Friedberg (Hessen)": (50.3375, 8.7542, 25),
    "Rüsselsheim am Main": (49.9900, 8.4133, 24),
    "Bad Hersfeld": (50.8690, 9.7100, 120),
    "Eschwege": (51.1864, 10.0560, 145),
    "Hofheim am Taunus": (50.0872, 8.4464, 15),
    "Heppenheim": (49.6411, 8.6394, 55),
    "Bensheim": (49.6803, 8.6194, 50),
    "Lorsch": (49.6533, 8.5678, 52),
    "Michelstadt": (49.6744, 9.0031, 65),
    "Groß-Umstadt": (49.8681, 8.9333, 40),
    "Groß-Gerau": (49.9219, 8.4822, 28),
    "Dreieich": (49.9958, 8.7067, 18),
    "Neu-Isenburg": (50.0492, 8.6947, 12),
    "Bad Vilbel": (50.1833, 8.7333, 15),
    "Idstein": (50.2178, 8.2683, 45),
    "Bad Schwalbach": (50.1411, 8.0708, 45),
    "Butzbach": (50.4344, 8.6719, 35),
    "Gelnhausen": (50.2019, 9.1903, 45),
    "Bad Orb": (50.2272, 9.3497, 55),
    "Korbach": (51.2714, 8.8731, 130),
    "Bad Wildungen": (51.1197, 9.1228, 125),
    "Alsfeld": (50.7514, 9.2708, 100),
    "Fritzlar": (51.1306, 9.2753, 140),
    "Melsungen": (51.1286, 9.5428, 140),
    "Baunatal": (51.2500, 9.4167, 155),
    "Hann. Münden": (51.4153, 9.6522, 175),
    "Hofgeismar": (51.4958, 9.3825, 165),
    "Schlitz": (50.6744, 9.5600, 110),
    "Weilmünster": (50.4244, 8.3667, 60),
    "Herborn": (50.6806, 8.3050, 75),
    "Ortenberg": (50.3536, 9.0497, 45),
    "Nidda": (50.4133, 9.0081, 45),
    "Schlüchtern": (50.3500, 9.5250, 70),
    "Viernheim": (49.5408, 8.5783, 60),
    "Usingen": (50.3333, 8.5333, 40),
    "Künzell": (50.5494, 9.7086, 105),
    "Wettenberg": (50.6167, 8.6500, 65),
    "Dietzenbach": (50.0100, 8.7800, 20),
    "Weilburg": (50.4833, 8.2667, 65),
    "Mühlheim am Main": (50.1247, 8.8283, 15),
}

def ev(title, date, time, desc, cost, location, category, city, website=""):
    lat, lon, dist = D[city]
    return {
        "title": title, "date": date, "time": time, "description": desc,
        "cost_per_person": cost, "location": location, "category": category,
        "city": city, "latitude": lat, "longitude": lon, "website": website,
        "google_maps_link": "https://maps.google.com/?q=" + urllib.parse.quote(location),
        "distance_from_frankfurt_km": dist,
    }

E = []
A = E.append

# ---------------- mid September ----------------
A(ev("Usinger Laurentius Markt (Laurentiuskerb)", "2026-09-13", "11:00 - 23:00",
   "Usingen's big traditional fair around St Lawrence, with a Krammarkt, funfair rides, food stalls and live music on the Marktplatz. The 2026 edition runs 11-14 September, closing with a Sunday parade through the old town.",
   "Free entry, ride/food prices on site", "Marktplatz Usingen, 61250 Usingen", "Festival & Culture", "Usingen",
   "https://festam.app/de-de/feste-in-usingen/"))
A(ev("Bad Vilbeler Quellenlauf", "2026-09-13", "09:00 - 13:00",
   "Bad Vilbel's traditional running event through the spa town and along the Nidda, with 5 km, 10 km and half-marathon routes plus school and family runs. Start and finish at the Kurpark; registration on the day usually possible.",
   "From ~15 EUR entry fee", "Kurpark / Nidda-Aue, 61118 Bad Vilbel", "Sports", "Bad Vilbel",
   "https://festam.app/de-de/feste-in-bad-vilbel/"))
A(ev("Tag des offenen Denkmals Idstein - Turm- und Schlossführungen", "2026-09-13", "10:00 - 17:00",
   "Germany's nationwide Heritage Open Day, marked in Idstein with guided tours of the Hexenturm and the historic Residenzschloss, plus free access to the town's medieval centre. Experts explain restoration work on the 17th-century painted castle chapel.",
   "Free (some tours require a small fee)", "Schloss Idstein, Schlossgasse 5, 65510 Idstein", "Literature & Arts", "Idstein",
   "https://festam.app/de-de/feste-in-idstein/"))
A(ev("Herborner Kartoffel-Sonntag", "2026-09-13", "11:00 - 18:00",
   "A relaxed harvest Sunday in Herborn's old town celebrating the potato: roasted potatoes, potato pancakes, potato soup and regional specialities, accompanied by a small farmers' market and live folk music. Shops in the historic centre are open.",
   "Free entry, dishes from ~5 EUR", "Marktplatz Herborn, 35745 Herborn", "Food & Drink", "Herborn",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Eröffnung der Sonderausstellung 'BLACKBOX Heimerziehung' mit Filmvorführung", "2026-09-15", "17:00 - 20:00",
   "Opening of the touring exhibition on the history of West German children's homes, followed by a documentary screening and discussion with contemporary witnesses. Organised in Gießen by the city's cultural office as part of the Liebknecht 200 programme.",
   "Free", "Stadtbibliothek Gießen, Berliner Platz 1, 35390 Gießen", "Art & Exhibitions", "Gießen",
   "https://www.giessen.de/Erleben/Veranstaltungen/"))
A(ev("Großenritter Zeltkirmes Baunatal", "2026-09-17", "14:00 - 23:30",
   "Baunatal-Großenritte's four-day tent fair (17-20 September) with a big marquee, beer wagons, fairground rides and live bands, culminating in a Kirmes parade on Sunday. A classic north Hessian Dorfkirmes with a strong local tradition.",
   "Free entry to grounds, pay per ride", "Festplatz Großenritte, Ziegenhainer Str., 34225 Baunatal", "Festival & Culture", "Baunatal",
   "https://festam.app/de-de/feste-in-baunatal/"))
A(ev("Bessunger Kerb Darmstadt", "2026-09-17", "15:00 - 23:00",
   "Darmstadt-Bessungen's neighbourhood parish fair, running 17-21 September with fairground rides, Kerbeborsch stands, brass music and the traditional Kerbebaum raising. One of the liveliest of Darmstadt's many Kerben.",
   "Free entry", "Bessunger Marktplatz, 64285 Darmstadt", "Festival & Culture", "Darmstadt",
   "https://festam.app/de-de/feste-in-darmstadt/"))
A(ev("Marburger Weinboulevard", "2026-09-18", "16:00 - 23:00",
   "Wine stands along the Oberstadt and Marktplatz bring around 20 German and international wineries to Marburg's old town, with regional food, live music on several small stages and sweeping views over the Lahn valley.",
   "Free entry, wine from ~4 EUR/glass", "Marktplatz Marburg, 35037 Marburg", "Food & Drink", "Marburg",
   "https://festam.app/de-de/feste-in-marburg/"))
A(ev("Friedberger Herbstmarkt", "2026-09-18", "11:00 - 23:00",
   "The Wetterau's largest fair (18-22 September) fills Friedberg's Kaiserstraße and Stadtkirche square with around 200 traders, a big funfair, a Krammarkt and a dedicated fashion and homewares section. Live music every evening and a fireworks finale.",
   "Free entry, pay per ride", "Innenstadt Friedberg, Kaiserstraße, 61169 Friedberg (Hessen)", "Festival & Culture", "Friedberg (Hessen)",
   "https://festam.app/de-de/feste-in-friedberg/"))
A(ev("Groß-Gerauer Street Food Festival", "2026-09-18", "12:00 - 22:00",
   "Around 25 food trucks and street-food stands from across Europe park up in Groß-Gerau's Stadtpark for three days (18-20 September), with DJ sets, craft beer and a children's area. Free entry, pay per dish.",
   "Free entry, dishes from ~7 EUR", "Stadtpark Groß-Gerau, Frankfurter Str., 64521 Groß-Gerau", "Food & Drink", "Groß-Gerau",
   "https://festam.app/de-de/feste-in-gross-gerau/"))
A(ev("Umstädter Winzerfest", "2026-09-18", "17:00 - 23:00",
   "Groß-Umstadt's vintners' festival (18-21 September) celebrates the small but distinctive Odenwald wine region with tastings from local estates, a wine queen, brass bands and the traditional Fassanstich on the Marktplatz.",
   "Free entry, tasting glass ~5 EUR", "Marktplatz Groß-Umstadt, 64823 Groß-Umstadt", "Food & Drink", "Groß-Umstadt",
   "https://festam.app/de-de/feste-in-gross-umstadt/"))
A(ev("Medenbacher Kerb", "2026-09-18", "15:00 - 23:00",
   "Neighbourhood parish fair in Wiesbaden-Medenbach (18-20 September) with rides, a Kerbestand, handcart races and the traditional Kerbebaum. Sunday features an ecumenical service followed by a parade.",
   "Free entry", "Kerbplatz Medenbach, 65199 Wiesbaden", "Festival & Culture", "Wiesbaden",
   "https://festam.app/de-de/feste-in-wiesbaden/"))
A(ev("Delkenheimer Kerb", "2026-09-18", "15:00 - 23:00",
   "Wiesbaden-Delkenheim's village fair (18-20 September), one of the capital's most popular Kerben, with a fairground, Apfelwein stands, live bands and the traditional Kerbepaar. Free entry across the weekend.",
   "Free entry", "Ortsmitte Delkenheim, 65205 Wiesbaden", "Festival & Culture", "Wiesbaden",
   "https://festam.app/de-de/feste-in-wiesbaden/"))
A(ev("Niederzwehrener Märchentage", "2026-09-18", "10:00 - 20:00",
   "Kassel's ten-day fairy-tale festival in the Niederzwehren district (18-27 September): theatre for children, puppet shows, readings from the Brothers Grimm, a masked parade and a fairy-tale market. A core part of Kassel's Grimm heritage programming.",
   "Most events free, some performances ticketed", "Kulturzentrum Schlachthof / Ortsmitte Niederzwehren, 34134 Kassel", "Family & Education", "Kassel",
   "https://festam.app/de-de/feste-in-kassel/"))
A(ev("Haßlocher Eppelwoifest", "2026-09-19", "16:00 - 23:00",
   "Rüsselsheim-Haßloch's apple-wine festival (19-20 September), staged by local clubs around the historic Haßlocher Rathaus, with Ebbelwoi from regional press houses, handkäse, music and a Sunday morning Frühschoppen.",
   "Free entry, drinks from ~3 EUR", "Rathaus Haßloch, 65428 Rüsselsheim am Main", "Food & Drink", "Rüsselsheim am Main",
   "https://festam.app/de-de/feste-in-ruesselsheim/"))
A(ev("Taste of Korea Neu-Isenburg", "2026-09-19", "12:00 - 20:00",
   "A one-day Korean food and culture festival in Neu-Isenburg with street-food stalls (bibimbap, tteokbokki, Korean fried chicken), K-pop dance performances, calligraphy workshops and a hanbok photo corner. Organised with the town's Korean community.",
   "Free entry, dishes from ~6 EUR", "Wilhelmsplatz Neu-Isenburg, 63263 Neu-Isenburg", "Food & Drink", "Neu-Isenburg",
   "https://festam.app/de-de/feste-in-neu-isenburg/"))
A(ev("23. Freudenberger Oktoberfest", "2026-09-19", "17:00 - 01:00",
   "Wiesbaden-Freudenberg's Wiesn night on the Festplatz, now in its 23rd year: Bavarian beer tent, brass and party bands (2026: Die Grummis), dirndl and lederhosen dress code, and a full evening of Wiesn party atmosphere from 17:00.",
   "Tickets from ~15 EUR, drinks extra", "Festplatz Freudenberg, 65201 Wiesbaden", "Nightlife & Social", "Wiesbaden",
   "https://www.eventim.de/event/23-freudenberger-oktoberfest-festplatz-freudenberg-21869384/"))
A(ev("Lorscher Kerb mit Tabakfest", "2026-09-19", "14:00 - 23:00",
   "Lorsch's combined parish fair and tobacco festival (19-21 September) recalls the town's once-thriving tobacco industry with a tobacco-leaf parade, historic machinery demonstrations, a fairground and wine and beer stands in the old town.",
   "Free entry", "Marktplatz / Kloster Lorsch, 64653 Lorsch", "Festival & Culture", "Lorsch",
   "https://festam.app/de-de/feste-in-lorsch/"))
A(ev("Kassel Marathon", "2026-09-20", "09:30 - 16:00",
   "The 20th edition of northern Hesse's biggest running event: marathon, half-marathon, relay, 10 km and a children's run, all finishing in the Auestadion after a flat, fast course through the Karlsaue and along the Fulda. Anniversary edition with a large finish-line festival.",
   "Entry from ~35 EUR, spectating free", "Auestadion Kassel, Damaschkestr. 10, 34121 Kassel", "Sports", "Kassel",
   "https://kassel-marathon.de/"))
A(ev("Herbstzauber im Botanischen Garten Eschwege", "2026-09-20", "10:00 - 18:00",
   "Eschwege's autumn garden market in the Botanical Garden: nursery plants, bulbs, regional honey and preserves, garden art, coffee and cake, plus guided tours of the late-summer borders. A gentle, family-friendly Sunday event.",
   "Free entry", "Botanischer Garten Eschwege, Am Botanischen Garten, 37269 Eschwege", "Seasonal & Markets", "Eschwege",
   "https://festam.app/de-de/feste-in-eschwege/"))
A(ev("Bürgeler Markt Offenbach", "2026-09-20", "10:00 - 18:00",
   "Offenbach-Bürgel's traditional autumn market on the historic Marktplatz, with around 80 traders offering crafts, household goods, textiles and regional produce, plus a small funfair and organ-grinder music. One of the city's oldest market traditions.",
   "Free entry", "Marktplatz Bürgel, 63075 Offenbach am Main", "Markets & Shopping", "Offenbach am Main",
   "https://festam.app/de-de/feste-in-offenbach-am-main/"))
A(ev("Herbst- und Bauernmarkt Hann. Münden", "2026-09-20", "10:00 - 18:00",
   "A regional farmers' and autumn market in Hann. Münden's half-timbered old town, with producers from the Werra and Fulda valleys selling apples, pumpkins, cheese, sausage and cider. Cooking demonstrations and a children's hay-bale play area.",
   "Free entry", "Marktplatz Hann. Münden, 34346 Hann. Münden", "Seasonal & Markets", "Hann. Münden",
   "https://festam.app/de-de/feste-in-hann-muenden/"))
A(ev("Matinée musicale der Hempelstiftung", "2026-09-20", "11:00 - 12:30",
   "A morning chamber concert in the Loge Plato on Wiesbaden's Friedrichstraße, given by young prizewinning musicians supported by the Hempelstiftung. Programme mixes classical sonatas with contemporary chamber works; coffee afterwards.",
   "Free, donations welcome", "Loge Plato, Großer Saal, Friedrichstraße 35, 65185 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Wiesbadener Stadtfest mit Herbstmarkt und Kunsthandwerkermarkt", "2026-09-25", "10:00 - 22:00",
   "Wiesbaden's big city festival (25-27 September) across the Innenstadt, Altstadt, Warmer Damm, Fußgängerzone and Mauritiusplatz: a rotating stage programme, the Herbstmarkt and Kunsthandwerkermarkt, the Erntedankfest, a classic-car show on Schlossplatz and a Sunday shopping day.",
   "Free entry", "Innenstadt / Warmer Damm / Mauritiusplatz, 65183 Wiesbaden", "Festival & Culture", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Erbenheimer Kerb", "2026-09-25", "15:00 - 23:00",
   "Wiesbaden-Erbenheim's parish fair (25-27 September) with a funfair, Kerbebaum, Bratwurst and Apfelwein stands, and the Kerbeborsch procession on Sunday. Live music in the Kerbezelt on all three days.",
   "Free entry", "Kerbplatz Erbenheim, 65205 Wiesbaden", "Festival & Culture", "Wiesbaden",
   "https://festam.app/de-de/feste-in-wiesbaden/"))
A(ev("Kerb Wildsachsen", "2026-09-25", "15:00 - 23:00",
   "Hofheim-Wildsachsen's village fair (25-28 September) with rides, food and drink stands and the traditional Kerbebaum setting. Sunday morning Frühmesse followed by a parade through the village.",
   "Free entry", "Ortsmitte Wildsachsen, 65719 Hofheim am Taunus", "Festival & Culture", "Hofheim am Taunus",
   "https://festam.app/de-de/feste-in-hofheim-am-taunus/"))
A(ev("Bauschemer Kerb", "2026-09-25", "15:00 - 23:00",
   "Rüsselsheim-Bauschheim's parish fair (25-28 September), one of the largest in the Rüsselsheim area, with a big fairground, Kerbehalle, brass music and the Sunday Kerbeumzug. Add a separate Nachkerb the following weekend.",
   "Free entry", "Ortsmitte Bauschheim, 65428 Rüsselsheim am Main", "Festival & Culture", "Rüsselsheim am Main",
   "https://festam.app/de-de/feste-in-ruesselsheim/"))
A(ev("Eltviller Street Food Festival", "2026-09-25", "12:00 - 22:00",
   "Street-food trucks from across Europe set up along the Rhine promenade in Eltville for three days (25-27 September), paired with Rheingau wine and Sekt stands, lounge music and sunset views over the river.",
   "Free entry, dishes from ~8 EUR", "Rheinufer / Kurfürstliche Burg, 65343 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://festam.app/de-de/feste-in-eltville-am-rhein/"))
A(ev("Weiten-Gesäßer Kerb", "2026-09-25", "15:00 - 23:00",
   "Michelstadt-Weiten-Gesäß's Odenwald parish fair (25-28 September) with a Kerbebaum, fairground rides, a lively Kerbedisco and the traditional Sunday Kerbezug. Strongly rooted in the village's club life.",
   "Free entry", "Ortsmitte Weiten-Gesäß, 64720 Michelstadt", "Festival & Culture", "Michelstadt",
   "https://festam.app/de-de/feste-in-michelstadt/"))
A(ev("Gießener Herbstmesse", "2026-09-26", "11:00 - 23:00",
   "Central Hesse's biggest autumn fair (26 September - 4 October), filling the Gießen fairground with more than 100 showmen's businesses, a large Krämermarkt, a beer tent with live music and the traditional Sunday parade. Nine days of rides, food and market stalls.",
   "Free entry, pay per ride", "Festplatz Gießen (Ringallee), 35398 Gießen", "Festival & Culture", "Gießen",
   "https://festam.app/de-de/feste-in-giessen/"))
A(ev("IGO Herbstmarkt Bad Homburg", "2026-09-26", "10:00 - 18:00",
   "The Interessengemeinschaft Ober-Erlenbach's autumn market in Bad Homburg-Ober-Erlenbach, with regional producers, handicraft stalls, pumpkin displays and a small harvest stage programme. Shops and courtyard cafés open alongside.",
   "Free entry", "Ober-Erlenbach Ortsmitte, 61352 Bad Homburg vor der Höhe", "Seasonal & Markets", "Bad Homburg vor der Höhe",
   "https://festam.app/de-de/feste-in-bad-homburg/"))
A(ev("Reckenforst Hüttengaudi Limburg", "2026-09-26", "18:00 - 01:00",
   "An Alpine-themed party night at Limburg's Reckenforst venue, with DJs, bar huts, beer-bench seating and party hits until late. The 2026 edition opens Limburg's autumn event season.",
   "Tickets from ~12 EUR", "Reckenforst, Limburg an der Lahn, 65549 Limburg an der Lahn", "Nightlife & Social", "Limburg an der Lahn",
   "https://festam.app/de-de/feste-in-limburg-an-der-lahn/"))
A(ev("2. Kasseler Oktoberfest", "2026-09-26", "19:00 - 01:00",
   "Kassel's second Oktoberfest in the Ernst-Freudental-Halle (Messe Kassel): Bavarian beer, brass-band entertainment, a Wiesn host, dirndl and lederhosen encouraged and a full party programme into the night.",
   "Tickets from ~20 EUR, drinks extra", "Ernst-Freudental-Halle, Messe Kassel, Damaschkestr. 55, 34121 Kassel", "Nightlife & Social", "Kassel",
   "https://www.regioactive.de/fest/2-oktoberfest-kassel-ernst-freudental-halle-2026-09-26-zb2wrhpwzz"))
A(ev("Erntedankfest am Warmen Damm", "2026-09-26", "10:00 - 18:00",
   "Wiesbaden's harvest-thanksgiving festival in the green space on the Warmer Damm (26-27 September): around 40 market stalls from Hessian farms and growers, an ornamental-gourd display, rural craft demonstrations and a small stage with brass and folk music.",
   "Free entry", "Warmer Damm, 65189 Wiesbaden", "Seasonal & Markets", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Zauberhafte LichterNacht Alsfeld", "2026-09-26", "18:00 - 23:00",
   "Alsfeld's old town is lit by thousands of candles, torches and light installations for one evening, with open shops and courtyards, street musicians, fire artists and regional food stands between the half-timbered houses.",
   "Free entry", "Marktplatz Alsfeld, 36304 Alsfeld", "Festival & Culture", "Alsfeld",
   "https://festam.app/de-de/feste-in-alsfeld/"))
A(ev("Lorscher Kelterfest", "2026-09-27", "11:00 - 18:00",
   "A hands-on wine-pressing festival by the UNESCO World Heritage Lorsch Abbey: visitors help press grapes in a historic wooden press, taste fresh Federweißer and must, and tour the abbey's wine cellars. Regional food and live music all afternoon.",
   "From ~8 EUR", "Kloster Lorsch, Nibelungenstraße 32, 64653 Lorsch", "Food & Drink", "Lorsch",
   "https://festam.app/de-de/feste-in-lorsch/"))
A(ev("Michaelismarkt Melsungen", "2026-09-27", "10:00 - 18:00",
   "Melsungen's historic Michaelismarkt fills the narrow old town and the Bartenwetzer bridge area with market stalls, sweet stalls, pottery and cloth traders, plus brass music and a Punch-and-Judy show for children. Held since the 16th century.",
   "Free entry", "Marktplatz / Altstadt Melsungen, 34212 Melsungen", "Markets & Shopping", "Melsungen",
   "https://festam.app/de-de/feste-in-melsungen/"))
A(ev("Verkaufsoffener Rieslingsonntag Rüsselsheim", "2026-09-27", "13:00 - 18:00",
   "Rüsselsheim's wine-themed Sunday shopping day: shops open through the afternoon while Rheingau and Rheinhessen wineries pour Riesling at stands along the Fußgängerzone, with live music and a children's programme.",
   "Free entry", "Innenstadt Rüsselsheim, Marktplatz, 65428 Rüsselsheim am Main", "Markets & Shopping", "Rüsselsheim am Main",
   "https://festam.app/de-de/feste-in-ruesselsheim/"))
A(ev("Wurschtfest Eschwege", "2026-09-27", "11:00 - 20:00",
   "Eschwege's cheerful sausage festival in the old town, with around 20 local butchers and food stands grilling, boiling and smoking their best sausages, plus beer, brass music and a children's programme on the Marktplatz.",
   "Free entry, food from ~4 EUR", "Marktplatz Eschwege, 37269 Eschwege", "Food & Drink", "Eschwege",
   "https://festam.app/de-de/feste-in-eschwege/"))
A(ev("Rheingau Literatur Preis 2026 - Preisverleihung", "2026-09-27", "17:00 - 19:00",
   "Lukas Rietzschel receives the Rheingau Literatur Preis 2026 for his novel 'Sanditz' at Schloss Johannisberg, in a ceremony with a reading and laudation, framed by Rheingau Musik Festival performers. One of the region's most prestigious literary awards.",
   "From ~20 EUR", "Schloss Johannisberg, Fürst-von-Metternich-Saal, 65366 Geisenheim", "Literature & Arts", "Geisenheim",
   "https://www.rheingau-musik-festival.de/startseite"))
A(ev("Öffentlicher Rundgang: Charles Ray im Fridericianum", "2026-09-27", "15:00 - 16:00",
   "A guided public walk-through of the Charles Ray exhibition at the Fridericianum with the museum's mediators, exploring the American sculptor's monumental, unsettling figures and their dialogue with the building's documenta history.",
   "Included in museum admission (~10 EUR)", "Fridericianum, Friedrichsplatz 18, 34117 Kassel", "Art & Exhibitions", "Kassel",
   "https://documenta.de/de/events/oeffentlicher-rundgang-charles-ray-6"))
A(ev("Rimbacher Kartoffelfest", "2026-09-27", "11:00 - 18:00",
   "Schlitz-Rimbach's potato festival in the Vogelsberg village, with potato dishes of every kind, a potato-sack race, handcart parade and rural craft demonstrations. A genuine, unhurried village harvest festival.",
   "Free entry", "Ortsmitte Rimbach, 36110 Schlitz", "Food & Drink", "Schlitz",
   "https://festam.app/de-de/feste-in-schlitz/"))
A(ev("Interkulturelle Woche Heppenheim", "2026-09-27", "11:00 - 20:00",
   "Heppenheim's intercultural week (27 September - 4 October) opens with an international street festival in the old town: food from a dozen cuisines, music and dance from migrant communities, a bazaar and a children's programme.",
   "Free entry", "Marktplatz Heppenheim, 64646 Heppenheim", "Festival & Culture", "Heppenheim",
   "https://festam.app/de-de/feste-in-heppenheim/"))
A(ev("Eröffnung: Studioausstellung im documenta archiv", "2026-09-29", "18:00 - 20:30",
   "Opening of the studio exhibition 'Zwischen Akten, Fotografien und Leinwand - Einblicke in die Restaurierung' at the documenta archiv, showing how conservators treat photographs, papers and canvases from the documenta holdings. Curators introduce the project.",
   "Free", "documenta archiv, Untere Karlsstr. 4, 34117 Kassel", "Art & Exhibitions", "Kassel",
   "https://documenta.de/de/events"))

# ---------------- October ----------------
A(ev("21. Allergiekongress 2026", "2026-10-01", "09:00 - 18:00",
   "Germany's principal three-day allergy congress (1-3 October) at the RheinMain CongressCenter, with scientific sessions, an industry exhibition and training courses for allergologists, dermatologists and paediatricians.",
   "Congress pass, registration required", "RheinMain CongressCenter (RMCC), Friedrich-Ebert-Allee 1, 65185 Wiesbaden", "Convention & Pop Culture", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("PAUL PANZER - Schöne neue Welt", "2026-10-01", "20:00 - 22:15",
   "The Hessian comedian's new arena show in the Buderus Arena Wetzlar: a fast-paced, opinionated take on digital life, AI and everyday absurdity, with live band and large video staging.",
   "Tickets from ~40 EUR", "Buderus Arena Wetzlar, Wolfgang-Kühle-Str. 1, 35576 Wetzlar", "Literature & Arts", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/oktober/"))
A(ev("Tobias Mann - Real/Fake", "2026-10-01", "20:00 - 22:00",
   "Cabaret in the atmospheric Brentanoscheune at Oestrich-Winkel: Tobias Mann interrogates truth, fake news and self-deception with sharp political satire and piano accompaniment, in a Rheingauer Wein Bühne production.",
   "Tickets from ~28 EUR", "Brentanoscheune, Oestrich-Winkel, 65375 Oestrich-Winkel", "Literature & Arts", "Oestrich-Winkel",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/oktober/"))
A(ev("Dr. Cordelia Schott: Rezeptfrei", "2026-10-01", "20:00 - 22:00",
   "The physician and comedian dissects Germany's pharmacy counter and self-medication culture with medical accuracy and dry humour, live in the Centralstation Darmstadt.",
   "Tickets from ~25 EUR", "Centralstation Darmstadt, Im Carree 1a, 64283 Darmstadt", "Literature & Arts", "Darmstadt",
   "https://www.eventfinder.de/darmstadt/veranstaltungen/oktober/"))
A(ev("Bad Nauheimer Kerb", "2026-10-02", "15:00 - 23:00",
   "Bad Nauheim's parish fair (2-6 October) around the Kerbeborsch tradition, with a fairground in the Kurstraße area, Kerbezelt with live bands, Bratwurst and apple-wine stands, and the traditional Kerbeumzug on the Sunday.",
   "Free entry", "Innenstadt Bad Nauheim, 61231 Bad Nauheim", "Festival & Culture", "Bad Nauheim",
   "https://festam.app/de-de/feste-in-bad-nauheim/"))
A(ev("Internationales Gitarrenfestival Bad Wildungen", "2026-10-02", "19:30 - 22:00",
   "A three-week guitar festival (2-25 October) bringing international classical and flamenco guitarists to Bad Wildungen's spa architecture, with concerts, masterclasses and a young talent competition. Concerts mostly weekend evenings.",
   "Tickets from ~18 EUR", "Kurhaus Bad Wildungen, Brunnenallee 1, 34537 Bad Wildungen", "Music & Opera", "Bad Wildungen",
   "https://festam.app/de-de/feste-in-bad-wildungen/"))
A(ev("Michelstädter Weinbrunnenfest", "2026-10-02", "16:00 - 23:00",
   "Michelstadt's Odenwald wine festival (2-4 October) around the historic Marktbrunnen, with regional Odenwald and Bergstrasse wines, a wine queen, brass music and guided tastings in the town's vaulted cellars.",
   "Free entry, tasting glass ~6 EUR", "Marktbrunnen / Altstadt Michelstadt, 64720 Michelstadt", "Food & Drink", "Michelstadt",
   "https://festam.app/de-de/feste-in-michelstadt/"))
A(ev("Gießener Krämermarkt", "2026-10-02", "09:00 - 18:00",
   "A classic three-day Krämermarkt (2-4 October) on Gießen's Brandplatz and Marktplatz, running in parallel with the Herbstmesse: textiles, kitchenware, sweets, spices and household goods from around 80 travelling traders.",
   "Free entry", "Brandplatz / Marktplatz Gießen, 35390 Gießen", "Markets & Shopping", "Gießen",
   "https://festam.app/de-de/feste-in-giessen/"))
A(ev("Eröffnung: Mohammed Sami - Hostless", "2026-10-02", "19:00 - 22:00",
   "Opening of the solo exhibition by Iraqi-Swedish painter Mohammed Sami at the Fridericianum, with a children's vernissage earlier the same afternoon. Sami's large canvases address memory, displacement and domestic space.",
   "Opening free, exhibition ~10 EUR", "Fridericianum, Friedrichsplatz 18, 34117 Kassel", "Art & Exhibitions", "Kassel",
   "https://documenta.de/de/events"))
A(ev("'Drachen. Mythos und Wirklichkeit' - Sonderausstellung", "2026-10-02", "10:00 - 18:00",
   "Opening of the Hessisches Landesmuseum Darmstadt's major special exhibition on dragons (from 2 October), spanning myth, natural history and popular culture, with Chinese dragon processions, medieval bestiaries, fossils and fantasy film props.",
   "Museum admission ~12 EUR", "Hessisches Landesmuseum Darmstadt, Friedensplatz 1, 64283 Darmstadt", "Art & Exhibitions", "Darmstadt",
   "https://www.hlmd.de/de/presse/aktuell/aktuell/ausstellungsuebersicht-2026"))
A(ev("Hesslocher Kuckuckskerb", "2026-10-02", "15:00 - 23:00",
   "Wiesbaden-Kohlheck/Hessloch's quirky 'Cuckoo Kerb' (2-4 October), named for the Hesslocher Kuckuck emblem, with a small fairground, Kerbezelt, live music and the traditional Kerbebaum.",
   "Free entry", "Kerbplatz Hessloch, 65205 Wiesbaden", "Festival & Culture", "Wiesbaden",
   "https://festam.app/de-de/feste-in-wiesbaden/"))
A(ev("Langenhainer Kerb", "2026-10-02", "15:00 - 23:00",
   "Hofheim-Langenhain's parish fair (2-5 October) with rides, Kerbestand, apple wine and the Langenhainer Kerbepaar. Sunday parade and open-air Frühschoppen.",
   "Free entry", "Ortsmitte Langenhain, 65719 Hofheim am Taunus", "Festival & Culture", "Hofheim am Taunus",
   "https://festam.app/de-de/feste-in-hofheim-am-taunus/"))
A(ev("Ray Wilson: The Weight Of Man", "2026-10-02", "20:00 - 22:30",
   "The former Genesis and Stiltskin frontman plays the Stadthalle Friedberg with a band set covering his solo catalogue plus Genesis and Stiltskin classics, including 'The Weight of Man' material.",
   "Tickets from ~35 EUR", "Stadthalle Friedberg, Kaiserstr. 132, 61169 Friedberg (Hessen)", "Music & Opera", "Friedberg (Hessen)",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/oktober/"))
A(ev("Oktoberfest am Mainvorgelände Offenbach", "2026-10-03", "17:00 - 01:00",
   "Offenbach's Oktoberfest on the Mainvorgelände: Bavarian beer tent, live brass and party bands, Wiesn food and a full evening programme with entrance from 17:00. Dirndl and lederhosen welcome but not required.",
   "Tickets from ~18 EUR", "Mainvorgelände, 63067 Offenbach am Main", "Nightlife & Social", "Offenbach am Main",
   "https://festam.app/de-de/feste-in-offenbach-am-main/"))
A(ev("Bauschemer Nachkerb", "2026-10-03", "16:00 - 23:00",
   "The follow-up weekend to Rüsselsheim-Bauschheim's Kerb (3-4 October), a smaller, cosier affair with the Kerbehalle, live music, home-made cakes and the traditional Kerbeborsch gathering.",
   "Free entry", "Ortsmitte Bauschheim, 65428 Rüsselsheim am Main", "Festival & Culture", "Rüsselsheim am Main",
   "https://festam.app/de-de/feste-in-ruesselsheim/"))
A(ev("Stadtfest Dreieich", "2026-10-03", "11:00 - 22:00",
   "Dreieich's city festival in and around the historic Burg Hayn at Dreieichenhain, with market stalls, food trucks, live bands on two stages, a children's programme and evening fireworks over the castle moat.",
   "Free entry", "Burg Hayn, Dreieichenhain, 63303 Dreieich", "Festival & Culture", "Dreieich",
   "https://festam.app/de-de/feste-in-dreieich/"))
A(ev("NATUR PUR in der Hattenheimer Flur", "2026-10-03", "11:00 - 18:00",
   "The Hattenheim vintners (Eltville) set out a walking and tasting trail through their vineyards (3-4 October), from the Pfaffenberg to the Steinberg, with 16 estates pouring wines at stands along the marked route and regional food along the way.",
   "Tasting pass from ~25 EUR", "Weingut Barth / Hattenheimer Flur, 65347 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://festam.app/de-de/feste-in-eltville-am-rhein/"))
A(ev("DenkmalKunst - KunstDenkmal Hann. Münden", "2026-10-03", "11:00 - 18:00",
   "A nine-day art trail (3-11 October) through Hann. Münden's half-timbered old town: commissioned and invited artists exhibit installations, sculpture and photography in historic houses, churches and the Werra Renaissance town hall.",
   "Free, some venues ticketed", "Altstadt Hann. Münden, 34346 Hann. Münden", "Art & Exhibitions", "Hann. Münden",
   "https://festam.app/de-de/feste-in-hann-muenden/"))
A(ev("Juse Ju - In jenen Tagen Tour", "2026-10-03", "20:00 - 22:30",
   "German rap with sharp social commentary: Juse Ju plays the Kulturzentrum Färberei in Kassel, touring the 'In jenen Tagen' record with a live band and his trademark blend of humour and political reflection.",
   "Tickets from ~22 EUR", "Kulturzentrum Färberei, Färberstr. 2, 34117 Kassel", "Music & Opera", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/oktober/"))
A(ev("Gradierwerkfest Bad Orb", "2026-10-03", "11:00 - 19:00",
   "Bad Orb's festival around its historic 180-metre graduation tower (Gradierwerk) in the spa gardens: guided tours of the salt-graduation works, wellness and salt-product market, brass music, coffee and cake in the Kursaal.",
   "Free entry", "Gradierwerk / Kurpark Bad Orb, 63619 Bad Orb", "Festival & Culture", "Bad Orb",
   "https://festam.app/de-de/feste-in-bad-orb/"))
A(ev("Apfelmarkt Wetzlar", "2026-10-04", "11:00 - 18:00",
   "Wetzlar's apple market in the old town celebrates the region's orchards with dozens of apple varieties, fresh juice and cider, apple pancakes, fruit trees for sale and pomology advice. Traditional market on the Eisenmarkt.",
   "Free entry", "Eisenmarkt Wetzlar, 35578 Wetzlar", "Seasonal & Markets", "Wetzlar",
   "https://festam.app/de-de/feste-in-wetzlar/"))
A(ev("'Der Name der Rose' - Open-Air-Kino in der Basilika", "2026-10-04", "19:30 - 22:30",
   "Part of kinoSommer hessen: Umberto Eco's 'The Name of the Rose' is screened in the monumental basilica of Kloster Eberbach, where much of the film was shot. A rare cinema experience at the original location, including a short introduction.",
   "Tickets ~15 EUR", "Kloster Eberbach, Basilika, 65346 Eltville am Rhein", "Film & Cinema", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-10-4"))
A(ev("Riesling Walk Schloss Vollrads", "2026-10-04", "11:00 - 16:00",
   "A guided walk around the Vollrads vineyards in Oestrich-Winkel with tasting stops among the Riesling vines, finishing at the Schloss for a glass and a view over the Rheingau. Around 6 km at a relaxed pace.",
   "From ~35 EUR", "Schloss Vollrads, 65375 Oestrich-Winkel", "Food & Drink", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-10-4"))
A(ev("Erntedankfest Fritzlar", "2026-10-04", "10:00 - 18:00",
   "Fritzlar's harvest-thanksgiving market in the cathedral and imperial city, with decorated harvest carts, regional produce, bread from the town's bakeries, church services and a parade through the medieval centre.",
   "Free entry", "Marktplatz / Domplatz Fritzlar, 34560 Fritzlar", "Seasonal & Markets", "Fritzlar",
   "https://festam.app/de-de/feste-in-fritzlar/"))
A(ev("Heavysaurus - Metal Tour 2026/27", "2026-10-04", "15:00 - 17:00",
   "The world's leading 'dino metal' band for children rocks the Stadthalle Limburg: costumed dinosaurs playing ear-friendly heavy metal with a confetti and laser show, aimed at families with children from around four years up.",
   "Tickets from ~25 EUR (child ~20 EUR)", "Stadthalle Limburg, Hospitalstr. 4, 65549 Limburg an der Lahn", "Family & Education", "Limburg an der Lahn",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/oktober/"))
A(ev("Badmómzjay - Haus im Meer Tour", "2026-10-06", "20:00 - 22:30",
   "One of Germany's most successful young rappers plays the Schlachthof Wiesbaden on her 'Haus im Meer' tour, presenting the more personal material of her 2026 album with full live band and stage production.",
   "Tickets from ~35 EUR", "Schlachthof Wiesbaden, Murnaustr. 1, 65189 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/oktober/"))
A(ev("Glaskunst aus Nancy - Werke von Émile Gallé", "2026-10-06", "15:30 - 16:30",
   "A lecture and guided viewing of Art Nouveau glass by Émile Gallé and the Nancy school, drawing on the Gießen museum's decorative-arts holdings. Part of the city's regular art-history series.",
   "From ~6 EUR", "Museum für Gießen / Altes Schloss, Brandplatz 2, 35390 Gießen", "Art & Exhibitions", "Gießen",
   "https://www.giessen.de/Erleben/Veranstaltungen/"))
A(ev("Marburger Innenstadtkirmes", "2026-10-09", "14:00 - 23:00",
   "Marburg's city-centre fair (9-12 October): rides and showmen's stalls on the Rudolf-Bultmann-Straße and Gutenbergstraße fairground, Kerbezelt with live bands, Bratwurst stands and an evening fireworks show on the Saturday.",
   "Free entry, pay per ride", "Festplatz / Innenstadt Marburg, 35037 Marburg", "Festival & Culture", "Marburg",
   "https://festam.app/de-de/feste-in-marburg/"))
A(ev("Schelmenmarkt Gelnhausen", "2026-10-09", "11:00 - 23:00",
   "Gelnhausen's four-day Volksfest (9-12 October) named after the town's trickster figure: a large Krammarkt through the medieval centre, funfair on the Untermarkt, beer tents and the Schelm parade on the Sunday.",
   "Free entry", "Untermarkt / Altstadt Gelnhausen, 63571 Gelnhausen", "Festival & Culture", "Gelnhausen",
   "https://festam.app/de-de/feste-in-gelnhausen/"))
A(ev("Sven Bensmann - SVENOMENAL", "2026-10-09", "20:00 - 22:00",
   "Comedy in the Erwin-Piscator-Haus Marburg: Sven Bensmann's 'SVENOMENAL' programme mixes observational humour, music and improvisation in a fast, interactive two-hour show.",
   "Tickets from ~25 EUR", "Erwin-Piscator-Haus, Biegenstr. 15, 35037 Marburg", "Literature & Arts", "Marburg",
   "https://www.eventfinder.de/marburg/veranstaltungen/oktober/"))
A(ev("Marburger Elisabethmarkt", "2026-10-10", "10:00 - 18:00",
   "A two-day market festival (10-11 October) around the Elisabethkirche and the Deutschordenshaus, with crafts, regional food, an artisan village, organ music in the church and guided tours of the Gothic Elisabethkirche.",
   "Free entry", "Elisabethkirche / Deutschordensplatz, 35037 Marburg", "Markets & Shopping", "Marburg",
   "https://festam.app/de-de/feste-in-marburg/"))
A(ev("Erntedankmarkt Bad Homburg", "2026-10-10", "10:00 - 18:00",
   "Bad Homburg's harvest market in the upper city centre (10-11 October), with Hessian farm produce, pumpkin and ornamental-gourd displays, rural craft, cider and a children's programme. Shops open on the Sunday.",
   "Free entry", "Innenstadt Bad Homburg, 61348 Bad Homburg vor der Höhe", "Seasonal & Markets", "Bad Homburg vor der Höhe",
   "https://festam.app/de-de/feste-in-bad-homburg/"))
A(ev("Idsteiner Herbstmarkt", "2026-10-10", "10:00 - 18:00",
   "A two-day autumn market (10-11 October) in Idstein's lovingly restored old town: arts and crafts, regional specialities, antiques, a small farm-animal enclosure and live music between the half-timbered houses.",
   "Free entry", "Marktplatz Idstein, 65510 Idstein", "Markets & Shopping", "Idstein",
   "https://festam.app/de-de/feste-in-idstein/"))
A(ev("Mittelalterlicher Markt Korbach", "2026-10-10", "11:00 - 22:00",
   "Korbach's medieval market (10-11 October) in the old town: historical traders, armourers and craftspeople, jugglers and minstrels, medieval food and drink, plus demonstrations of falconry and traditional crafts.",
   "Free entry, pay per item", "Marktplatz / Altstadt Korbach, 34497 Korbach", "Festival & Culture", "Korbach",
   "https://festam.app/de-de/feste-in-korbach/"))
A(ev("Robert Marc Lehmann: Mission Erde Live", "2026-10-11", "19:00 - 21:30",
   "The marine biologist and wildlife photographer presents his 'Mission Erde' live show in Marburg's Erwin-Piscator-Haus, mixing large-format photography, film sequences and first-hand reporting on ocean and rainforest conservation.",
   "Tickets from ~30 EUR", "Erwin-Piscator-Haus, Biegenstr. 15, 35037 Marburg", "Literature & Arts", "Marburg",
   "https://www.eventfinder.de/marburg/veranstaltungen/oktober/"))
A(ev("Musik von Hans Zimmer - Lords of the Sound", "2026-10-11", "19:30 - 22:00",
   "A symphonic tribute to Hans Zimmer's film scores in Fulda's Esperantohalle, with a full orchestra and choir performing themes from Gladiator, Inception, Interstellar, The Lion King and Pirates of the Caribbean.",
   "Tickets from ~40 EUR", "Esperantohalle Fulda, Esperantostr. 2-4, 36037 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/oktober/"))
A(ev("The Dark Tenor - Symphonica", "2026-10-11", "20:00 - 22:00",
   "Classical crossover in the Buderus Arena Wetzlar: The Dark Tenor (Billy Andrews) combines operatic vocals with rock band arrangements and dramatic staging, including material from 'Symphonica'.",
   "Tickets from ~35 EUR", "Buderus Arena Wetzlar, Wolfgang-Kühle-Str. 1, 35576 Wetzlar", "Music & Opera", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/oktober/"))
A(ev("Lullusfest Bad Hersfeld", "2026-10-12", "11:00 - 23:00",
   "Germany's oldest continuously recorded fair (first mentioned 852) runs 12-19 October through Bad Hersfeld's old town: a huge Krammarkt, funfair, festival hall, Lullus fire tradition and the Lullus procession with the Lullusfigur on 16 October.",
   "Free entry, pay per ride", "Innenstadt / Stiftsruine Bad Hersfeld, 36251 Bad Hersfeld", "Festival & Culture", "Bad Hersfeld",
   "https://festam.app/de-de/feste-in-bad-hersfeld/"))
A(ev("Lulluskrammarkt Bad Hersfeld", "2026-10-14", "09:00 - 18:00",
   "The main market day of the Lullusfest: around 250 travelling traders fill Bad Hersfeld's streets with textiles, household goods, sweets, baskets and spices - the classic Krammarkt of one of Germany's oldest fairs.",
   "Free entry", "Innenstadt Bad Hersfeld, 36251 Bad Hersfeld", "Markets & Shopping", "Bad Hersfeld",
   "https://festam.app/de-de/feste-in-bad-hersfeld/"))
A(ev("Deutscher Straßen- und Verkehrskongress 2026", "2026-10-14", "09:00 - 18:00",
   "Germany's central road and transport congress (14-16 October) at the RheinMain CongressCenter, with technical lectures, seminars and a large exhibition of road-building, traffic-technology and infrastructure suppliers.",
   "Congress pass, registration required", "RheinMain CongressCenter (RMCC), Friedrich-Ebert-Allee 1, 65185 Wiesbaden", "Convention & Pop Culture", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Maite Itoiz & John Kelly - Best of 20 Years", "2026-10-14", "20:00 - 22:30",
   "The Spanish-Irish duo celebrates two decades of collaboration in the Stadthallen Wetzlar, blending Celtic, classical and flamenco elements with their own compositions and vocal pieces.",
   "Tickets from ~30 EUR", "Stadthallen Wetzlar, Brühlsbachstr. 4, 35578 Wetzlar", "Music & Opera", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/oktober/"))
A(ev("Oktoberfest Limburg", "2026-10-16", "17:00 - 01:00",
   "Limburg's Oktoberfest on the Festplatz (mid-October, running to about 20 October): a big Bavarian beer tent with brass and party bands, Wiesn food, a midday Wiesn afternoon and evening party sessions.",
   "Tickets from ~15 EUR", "Festplatz Limburg, 65549 Limburg an der Lahn", "Nightlife & Social", "Limburg an der Lahn",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Gallusmarkt Wetzlar", "2026-10-15", "11:00 - 23:00",
   "Wetzlar's historic Gallusmarkt (15-18 October), documented since the 14th century: a large Krammarkt through the old town and an extensive funfair, with a beer tent, live music and the traditional market opening.",
   "Free entry, pay per ride", "Innenstadt / Eisenmarkt Wetzlar, 35578 Wetzlar", "Festival & Culture", "Wetzlar",
   "https://festam.app/de-de/feste-in-wetzlar/"))
A(ev("Das Kriminal Dinner - Louvre", "2026-10-15", "19:00 - 23:00",
   "A murder-mystery dinner in the Weißer Saal of Schloss Philippsruhe Hanau: actors play suspects between courses while guests solve the case, with a four-course menu included in the ticket price.",
   "From ~75 EUR including dinner", "Schloss Philippsruhe, Weißer Saal, Philippsruher Allee 45, 63454 Hanau", "Food & Drink", "Hanau",
   "https://www.eventfinder.de/hanau/veranstaltungen/oktober/"))
A(ev("Waldauer Enten-Kirmes", "2026-10-16", "14:00 - 23:00",
   "Kassel-Waldau's parish fair (16-19 October), famous for its wooden duck-lottery stands alongside a small funfair, Kerbezelt with live music, and the Sunday Kirmes parade through the quarter.",
   "Free entry", "Ortsmitte Waldau, 34123 Kassel", "Festival & Culture", "Kassel",
   "https://festam.app/de-de/feste-in-kassel/"))
A(ev("Tabaluga und Lilli - Das Musical", "2026-10-16", "16:00 - 18:00",
   "Peter Maffay's popular children's musical staged in the Stadthallen Wetzlar, with the dragon Tabaluga, large puppets, songs from the albums and a family-friendly running time of around two hours.",
   "Tickets from ~30 EUR (child ~25 EUR)", "Stadthallen Wetzlar, Brühlsbachstr. 4, 35578 Wetzlar", "Family & Education", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/oktober/"))
A(ev("Escape-Dinner: Knack den Geschmack", "2026-10-16", "19:00 - 22:30",
   "An escape-room-meets-dinner event in Fulda's Propstei Johannesberg: teams of guests solve puzzles between courses to unlock the menu, combining a multi-course dinner with a live puzzle game.",
   "From ~70 EUR per person", "Propstei Johannesberg, Johannesberg 2, 36041 Fulda", "Food & Drink", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/oktober/"))
A(ev("Jassin - Die größere Arsenalplatz Tour", "2026-10-16", "20:00 - 22:00",
   "The East German rapper plays the Schlachthof Wiesbaden: songs about origin, class and society from 'Arsenalplatz' and its successor, delivered with a live band and a loyal, vocal audience.",
   "Tickets from ~28 EUR", "Schlachthof Wiesbaden, Murnaustr. 1, 65189 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/oktober/"))
A(ev("Eure Mütter: Best Of Jubiläum", "2026-10-17", "20:00 - 22:30",
   "The Hessian comedian trio celebrates its anniversary with a best-of programme in the Stadthalle Baunatal, mixing sketch, music and improv from two decades of touring.",
   "Tickets from ~28 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Literature & Arts", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/oktober/"))
A(ev("Tito & Tarantula - Best Of Tour 2026", "2026-10-17", "20:00 - 22:30",
   "The band behind 'After Dark' from From Dusk Till Dawn brings its Latin-tinged desert rock to the Kulturzentrum Kreuz Fulda on a best-of tour.",
   "Tickets from ~32 EUR", "Kulturzentrum Kreuz, Mariahilfstr. 5, 36039 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/oktober/"))
A(ev("Herbstmarkt Hofgeismar", "2026-10-18", "10:00 - 18:00",
   "Hofgeismar's autumn market in the historic town centre: market stalls, harvest produce, sugar-bread and gingerbread stands, plus a small fairground on the Marktplatz. Family afternoon with brass music.",
   "Free entry", "Marktplatz Hofgeismar, 34369 Hofgeismar", "Seasonal & Markets", "Hofgeismar",
   "https://festam.app/de-de/feste-in-hofgeismar/"))
A(ev("Herbstfest mit Handwerkermarkt Lorsch", "2026-10-18", "11:00 - 18:00",
   "Lorsch's autumn festival and craft market in front of the UNESCO-listed abbey gatehouse, with potters, basket-weavers, felt and wood craftspeople demonstrating and selling, plus pumpkin soup, Federweißer and live folk music.",
   "Free entry", "Kloster Lorsch / Lauresham, Nibelungenstraße 32, 64653 Lorsch", "Markets & Shopping", "Lorsch",
   "https://festam.app/de-de/feste-in-lorsch/"))
A(ev("Ein Abend mit Robert Kreis", "2026-10-18", "19:30 - 21:30",
   "The celebrated Berlin cabaret entertainer, singer and pianist brings his Weimar-era repertoire of chansons, jokes and piano virtuosity to the Rheingauer Wein Bühne in Oestrich-Winkel.",
   "Tickets from ~30 EUR", "Rheingauer Wein Bühne, Frauenstein, 65375 Oestrich-Winkel", "Literature & Arts", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-10-18"))
A(ev("Nights on Broadway - Tribute", "2026-10-18", "19:00 - 21:30",
   "A musical-theatre gala in Fulda's Esperantohalle: soloists and orchestra perform songs from The Lion King, Phantom of the Opera, Les Misérables, Mamma Mia and other Broadway and West End hits.",
   "Tickets from ~38 EUR", "Esperantohalle Fulda, Esperantostr. 2-4, 36037 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/oktober/"))
A(ev("One Night of Dire Straits", "2026-10-18", "19:00 - 22:00",
   "A full-band tribute to Dire Straits in the Kongresshalle Gießen, recreating the Brothers in Arms-era sound with authentic guitar work and stage lighting.",
   "Tickets from ~32 EUR", "Kongresshalle Gießen, Berliner Platz 2, 35390 Gießen", "Music & Opera", "Gießen",
   "https://www.eventfinder.de/giessen/veranstaltungen/oktober/"))
A(ev("Yasi Hofer", "2026-10-18", "20:00 - 22:00",
   "The young German electric guitarist - known from the German TV talent show and touring with Helene Fischer - plays an intimate club show at the Theaterstübchen in Kassel, blending rock, funk and pop instrumentals.",
   "Tickets from ~22 EUR", "Theaterstübchen, Jordanstr. 11, 34117 Kassel", "Music & Opera", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/oktober/"))
A(ev("ABBA - Tribute Night auf Burg Gleiberg", "2026-10-18", "19:00 - 22:00",
   "An ABBA tribute concert inside the medieval walls of Burg Gleiberg above Wettenberg, with a live band in period costume, a bar in the castle courtyard and views over the Lahn valley.",
   "Tickets from ~28 EUR", "Burg Gleiberg, 35435 Wettenberg", "Music & Opera", "Wettenberg",
   "https://www.eventfinder.de/giessen/veranstaltungen/oktober/"))
A(ev("STAFFINGpro - HR Services & Staffing Industry Expo", "2026-10-21", "09:00 - 17:00",
   "A trade expo at the RheinMain CongressCenter for staffing firms and HR service providers, with supplier stands, workshops on recruitment technology and compliance sessions. Trade visitors only.",
   "Free with trade registration", "RheinMain CongressCenter (RMCC), Friedrich-Ebert-Allee 1, 65185 Wiesbaden", "Convention & Pop Culture", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("European Youth Circus 2026", "2026-10-22", "10:00 - 22:00",
   "Europe's leading youth circus competition pitches its big top on the Dernsches Gelände in Wiesbaden (22-25 October): two competition shows daily, a gala show with prize-giving on 24 October and an ecumenical service plus second gala on the 25th. Around 150 young artists from a dozen countries.",
   "Tickets from ~15 EUR, family tickets available", "Zeltbau Dernsches Gelände, 65183 Wiesbaden", "Family & Education", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("AzubiTECH 2026", "2026-10-22", "09:00 - 16:00",
   "An expo on training technology and innovation at the RheinMain CongressCenter, aimed at trainers, vocational schools and HR teams, with live demonstrations of digital learning tools.",
   "Free with registration", "RheinMain CongressCenter (RMCC), Friedrich-Ebert-Allee 1, 65185 Wiesbaden", "Convention & Pop Culture", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Kasseler Musiktage 2026", "2026-10-22", "20:00 - 22:00",
   "Kassel's long-running music festival (22 October - 1 November) explores musical movement across chamber, orchestral and choral programmes in the city's museums, churches and concert halls. Opening concert: Treppenhausorchester with purely acoustic beats and melodies.",
   "Tickets from ~20 EUR, festival pass available", "Various venues incl. Kongress Palais, 34117 Kassel", "Music & Opera", "Kassel",
   "https://www.kasseler-musiktage.de/"))
A(ev("Jan Philipp Zymny - Straßentherapie", "2026-10-22", "20:00 - 22:00",
   "Poetry-slam champion turned comedian Jan Philipp Zymny brings his 'Straßentherapie' show to the Stadthalle Baunatal: rapid-fire wordplay, absurd observation and audience interaction.",
   "Tickets from ~25 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Literature & Arts", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/oktober/"))
A(ev("'Die Blauen Reiterinnen' - Sonderausstellung", "2026-10-23", "10:00 - 18:00",
   "The Museum Wiesbaden's 2026 highlight exhibition (23 October 2026 - 21 February 2027) examines the influence of well-known and forgotten women artists in the circle of Der Blaue Reiter, with works by Marianne von Werefkin, Gabriele Münter and others.",
   "Museum admission ~10 EUR", "Museum Wiesbaden, Friedrich-Ebert-Str. 1, 65185 Wiesbaden", "Art & Exhibitions", "Wiesbaden",
   "https://www.wiesbaden.de/kultur/kultur-erleben/museen-ausstellungen/museum-wiesbaden-2026"))
A(ev("Reitsportmesse Gießen", "2026-10-23", "10:00 - 18:00",
   "An equestrian trade fair (23-25 October) at the Gießen Messe grounds: saddlery, riding equipment, stable technology, feed suppliers and daily live riding demonstrations and shows in the indoor arena.",
   "Day ticket from ~10 EUR", "Messe Gießen, An der Hessenhalle 1, 35398 Gießen", "Markets & Shopping", "Gießen",
   "https://festam.app/de-de/feste-in-giessen/"))
A(ev("Das Kriminal Dinner - Der letzte Joint", "2026-10-23", "19:00 - 23:00",
   "A murder-mystery dinner at the Waldgaststätte Hohes Gras above Kassel: actors perform between courses while guests interrogate the case, with a multi-course menu and forest views over the Habichtswald.",
   "From ~70 EUR including dinner", "Waldgaststätte Hohes Gras, 34131 Kassel", "Food & Drink", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/oktober/"))
A(ev("Vinyl Night Smooth Jazz im Loftwerk", "2026-10-24", "19:00 - 01:00",
   "A monthly vinyl session in the WERKLOFT at Wiesbaden's Loftwerk: DJs work through jazz, soul and house from the turntable, with cocktails and a relaxed late-night crowd. Every fourth Saturday of the month.",
   "Free entry", "Loftwerk, Karlstr. 7, 65185 Wiesbaden", "Nightlife & Social", "Wiesbaden",
   "https://www.rheingau.de/veranstaltungen/2026-10-25"))
A(ev("Butzbacher Katharinenmarkt", "2026-10-24", "11:00 - 23:00",
   "Butzbach's Katharinenmarkt (24-27 October) is one of the Wetterau's oldest fairs: Krammarkt through the walled old town, funfair on the Festplatz, beer tent with live bands and the traditional market opening with the mayor.",
   "Free entry, pay per ride", "Innenstadt / Festplatz Butzbach, 61273 Butzbach", "Festival & Culture", "Butzbach",
   "https://festam.app/de-de/feste-in-butzbach/"))
A(ev("760. Kalter Markt Ortenberg", "2026-10-24", "11:00 - 23:00",
   "One of Hessen's oldest fairs, held since 1266 (23-27 October) in Ortenberg's Wetterau old town: a large Krammarkt through the streets, funfair, market hall with regional produce and the traditional Kalter-Markt opening ceremony.",
   "Free entry", "Innenstadt Ortenberg, 63683 Ortenberg", "Festival & Culture", "Ortenberg",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Alsfelder Schokoladenmarkt", "2026-10-25", "11:00 - 19:00",
   "Alsfeld's chocolate market transforms the half-timbered old town into a giant confectioner's shop: artisan chocolatiers, praline tastings, chocolate sculptures, hot chocolate and a children's chocolate workshop.",
   "Free entry, tastings from ~3 EUR", "Marktplatz Alsfeld, 36304 Alsfeld", "Food & Drink", "Alsfeld",
   "https://festam.app/de-de/feste-in-alsfeld/"))
A(ev("WAHNSINN! Die Show", "2026-10-25", "18:00 - 20:30",
   "A large-scale entertainment and variety show in the Esperantohalle Fulda: comedy acts, magic, acrobatics, live music and audience participation hosted by a touring ensemble.",
   "Tickets from ~35 EUR", "Esperantohalle Fulda, Esperantostr. 2-4, 36037 Fulda", "Nightlife & Social", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/oktober/"))
A(ev("PETER KUNZ - HESSKALATION", "2026-10-25", "19:00 - 21:00",
   "Hessian stand-up comedian Peter Kunz brings his 'HESSkalation' programme to the Rheingauer Wein Bühne, with dialect humour, sharp observations on apple wine and regional identity, and plenty of audience banter.",
   "Tickets from ~25 EUR", "Rheingauer Wein Bühne, Frauenstein, 65375 Oestrich-Winkel", "Literature & Arts", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-10-25"))
A(ev("Casseler Herbst-Freyheit", "2026-10-29", "12:00 - 23:00",
   "Kassel's city festival in the pedestrian zone (29 October - 1 November): market and craft stands, food, live music on several stages, an autumn fairground on Friedrichsplatz and a late-season shopping Sunday.",
   "Free entry", "Innenstadt Kassel / Friedrichsplatz, 34117 Kassel", "Festival & Culture", "Kassel",
   "https://festam.app/de-de/feste-in-kassel/"))
A(ev("Oarhelljer Kerb Darmstadt-Arheilgen", "2026-10-29", "15:00 - 23:00",
   "Darmstadt-Arheilgen's parish fair (29 October - 3 November), one of the region's biggest Kerben, with a large fairground, Kerbehalle, live music and the traditional Kerbeumzug with the Kerbeborsch on the first Sunday.",
   "Free entry, pay per ride", "Ortsmitte Arheilgen, 64291 Darmstadt", "Festival & Culture", "Darmstadt",
   "https://festam.app/de-de/feste-in-darmstadt/"))
A(ev("Kappeskerb und Weinlesefest Eltville", "2026-10-30", "16:00 - 23:00",
   "A combined cabbage fair and grape-harvest festival in Eltville (30 October - 2 November): sauerkraut and Kappes specialities, Federweißer and new wine, brass music, and a small funfair on the Rheinufer.",
   "Free entry", "Rheinufer / Altstadt Eltville, 65343 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://festam.app/de-de/feste-in-eltville-am-rhein/"))
A(ev("Kulturnacht Bad Homburg", "2026-10-31", "19:00 - 01:00",
   "Bad Homburg's culture night: museums, galleries, churches, the Kurhaus and the Schloss open late with short performances, installations, readings and music, linked by a shuttle bus and a wristband ticket.",
   "Wristband ~15 EUR", "Various venues, Innenstadt Bad Homburg, 61348 Bad Homburg vor der Höhe", "Festival & Culture", "Bad Homburg vor der Höhe",
   "https://festam.app/de-de/feste-in-bad-homburg/"))
A(ev("Kunsthandwerkermarkt in der documenta-Halle", "2026-10-31", "11:00 - 18:00",
   "A curated applied-arts market in Kassel's documenta-Halle (31 October - 1 November): around 80 selected makers present ceramics, jewellery, textiles, glassware and woodwork, with demonstrations and a café.",
   "Admission ~5 EUR", "documenta-Halle, Du-Ry-Str. 1, 34117 Kassel", "Art & Exhibitions", "Kassel",
   "https://festam.app/de-de/feste-in-kassel/"))
A(ev("Schlitzer Runkelrübenfest", "2026-10-31", "11:00 - 18:00",
   "Schlitz's unusual beetroot festival in the Vogelsberg old town: beetroot dishes both sweet and savoury, beetroot wine and schnapps, a sugar-beet weighing contest, market stalls and live music.",
   "Free entry", "Marktplatz Schlitz, 36110 Schlitz", "Food & Drink", "Schlitz",
   "https://festam.app/de-de/feste-in-schlitz/"))
A(ev("Martinifest Nidda", "2026-10-31", "17:00 - 23:00",
   "Nidda's Martinifest (31 October - 1 November) in the Wetterau old town with lantern-lit streets, a lantern parade for children, market stalls, Martin's goose dishes and live music around the Marktplatz.",
   "Free entry", "Marktplatz Nidda, 63667 Nidda", "Seasonal & Markets", "Nidda",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))

# ---------------- November ----------------
A(ev("Liebigs Suppenfest", "2026-11-01", "11:00 - 16:00",
   "Gießen's soup festival in honour of Justus von Liebig: local restaurants, clubs and the university serve around 30 soups from stalls in the city centre, with a jury prize and a public vote. Family-friendly and inexpensive.",
   "Small charge per bowl (~3-5 EUR)", "Brandplatz / Innenstadt Gießen, 35390 Gießen", "Food & Drink", "Gießen",
   "https://festam.app/de-de/feste-in-giessen/"))
A(ev("Matinée musicale der Hempelstiftung (November)", "2026-11-01", "11:00 - 12:30",
   "The second autumn matinée of the Wiesbaden Hempelstiftung, again in the Loge Plato on Friedrichstraße, presenting young scholarship holders in a mixed programme of chamber music.",
   "Free, donations welcome", "Loge Plato, Großer Saal, Friedrichstraße 35, 65185 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Stefanie Heinzmann - Circles Tour 2026", "2026-11-03", "20:00 - 22:30",
   "The Swiss soul-pop singer and winner of the German talent show 'SSDSDSSWEMUGABRTLAD' plays the Stadthalle Baunatal on her 'Circles' tour, with a live band and songs from her latest album plus her best-known hits.",
   "Tickets from ~35 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Music & Opera", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Clemens Brock - Der Vadda", "2026-11-04", "20:00 - 22:00",
   "Comedy in the Stadthalle Offenbach: Clemens Brock's 'Der Vadda' programme looks at the absurdities of parenthood, family life and middle age with fast-paced storytelling.",
   "Tickets from ~25 EUR", "Stadthalle Offenbach, Berliner Str. 2, 63065 Offenbach am Main", "Literature & Arts", "Offenbach am Main",
   "https://www.eventfinder.de/offenbach/veranstaltungen/november/"))
A(ev("Wintergold Markt Hanau", "2026-11-04", "12:00 - 21:00",
   "Hanau's winter and Christmas market village (4 November - 22 December) in the city centre: wooden huts with craftsmanship, mulled drinks, a covered food court, ice rink and a light installation programme on the Marktplatz.",
   "Free entry", "Marktplatz Hanau, Am Markt 14, 63450 Hanau", "Seasonal & Markets", "Hanau",
   "https://festam.app/de-de/feste-in-hanau/"))
A(ev("Rock The Circus", "2026-11-05", "19:30 - 21:30",
   "Circus and rock music collide in the Parktheater Bensheim: acrobats, aerial artists and hand-to-hand performers are accompanied live by an electric rock band. A full-evening family and adult show.",
   "Tickets from ~30 EUR", "Parktheater Bensheim, Beethovenstr. 4, 64625 Bensheim", "Family & Education", "Bensheim",
   "https://www.eventfinder.de/darmstadt/veranstaltungen/november/"))
A(ev("Yakari - Freunde fürs Leben", "2026-11-05", "16:00 - 17:30",
   "A stage adaptation of the classic children's comic in the Congress Park Hanau: the little Sioux Yakari and his horse Little Thunder in a colourful family musical with songs, puppets and video scenery.",
   "Tickets from ~20 EUR (child ~15 EUR)", "Congress Park Hanau, Schloßplatz 1, 63450 Hanau", "Family & Education", "Hanau",
   "https://www.eventfinder.de/hanau/veranstaltungen/november/"))
A(ev("Martin Rütter - SCHLUSS! AUS!", "2026-11-05", "20:00 - 22:30",
   "Germany's best-known dog trainer brings his new live programme to the Kurhaus Wiesbaden, mixing practical dog-training insight with comedy and film from his television work.",
   "Tickets from ~40 EUR", "Kurhaus Wiesbaden, Friedrich-von-Thiersch-Saal, Kurhausplatz 1, 65189 Wiesbaden", "Literature & Arts", "Wiesbaden",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/november/"))
A(ev("Moving Shadows: On Fire", "2026-11-05", "20:00 - 22:00",
   "A shadow-dance and multimedia show in the Stadthallen Wetzlar: performers work with light, projection and body art to tell a story of fire and transformation, set to live percussion.",
   "Tickets from ~28 EUR", "Stadthallen Wetzlar, Brühlsbachstr. 4, 35578 Wetzlar", "Nightlife & Social", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/november/"))
A(ev("Hochheimer Markt", "2026-11-06", "11:00 - 23:00",
   "One of the largest and oldest Volksfeste in the Rhine-Main region, held annually in the weekend after All Souls (6-10 November, 2026) in Hochheim: a five-day mix of funfair, cattle market, trade fair and Krammarkt across seven hectares, with an opening ceremony and five cannon shots on Friday at noon and a closing fireworks display.",
   "Free entry, pay per ride", "Festplatz Hochheim, 65239 Hochheim am Main", "Festival & Culture", "Hochheim am Main",
   "https://www.hochheim-tourismus.de/veranstaltungen/hochheimer-markt"))
A(ev("Martinimarkt Bad Schwalbach", "2026-11-06", "11:00 - 23:00",
   "Bad Schwalbach's Martinimarkt (6-10 November): a traditional Krammarkt through the spa town's centre with a funfair, sweet stalls, market hall and live music, held since the 18th century.",
   "Free entry", "Innenstadt Bad Schwalbach, 65307 Bad Schwalbach", "Markets & Shopping", "Bad Schwalbach",
   "https://festam.app/de-de/feste-in-bad-schwalbach/"))
A(ev("Kalter Markt Schlüchtern", "2026-11-06", "11:00 - 23:00",
   "Schlüchtern's historic Kalter Markt (6-10 November), an old autumn fair in the Kinzig valley with a large Krammarkt through the old town, funfair, cattle show and market hall with regional produce.",
   "Free entry", "Innenstadt Schlüchtern, 36381 Schlüchtern", "Markets & Shopping", "Schlüchtern",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Viernheimer Kerwe", "2026-11-06", "14:00 - 23:00",
   "Viernheim's town fair (6-11 November) in the Bergstraße municipality: a fairground in the city centre, Kerwe hall with live bands, wine and beer stands, and the traditional Kerweumzug on the Sunday.",
   "Free entry, pay per ride", "Innenstadt Viernheim, 68519 Viernheim", "Festival & Culture", "Viernheim",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Bodo Wartke - Wunderpunkt", "2026-11-06", "20:00 - 22:30",
   "The piano cabaret artist plays the Stadthallen Wetzlar with 'Wunderpunkt': witty German-language songs, wordplay and political satire at the grand piano.",
   "Tickets from ~32 EUR", "Stadthallen Wetzlar, Brühlsbachstr. 4, 35578 Wetzlar", "Literature & Arts", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/november/"))
A(ev("Massenheimer Kerb", "2026-11-07", "15:00 - 23:00",
   "Bad Vilbel-Massenheim's parish fair (7-9 November) with rides, Kerbezelt, apple wine and the Massenheimer Kerbepaar. Sunday service and Kerbeumzug through the village.",
   "Free entry", "Ortsmitte Massenheim, 61118 Bad Vilbel", "Festival & Culture", "Bad Vilbel",
   "https://festam.app/de-de/feste-in-bad-vilbel/"))
A(ev("Puppen- und Bären Festtage Eschwege", "2026-11-07", "10:00 - 18:00",
   "Eschwege's doll and teddy-bear days (7-8 November) in the town centre: collectors' stands, antique dolls and bears, restoration workshops, puppet theatre for children and a doll-doctors' consultation corner.",
   "Admission ~6 EUR", "Innenstadt Eschwege, 37269 Eschwege", "Markets & Shopping", "Eschwege",
   "https://festam.app/de-de/feste-in-eschwege/"))
A(ev("GameChanger by Bastian Bielendorfer", "2026-11-07", "20:00 - 22:00",
   "The comedian and podcaster brings his 'GameChanger' show to the Stadthalle Baunatal: stories from school, gaming, family and the absurdities of adult life.",
   "Tickets from ~28 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Literature & Arts", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Gentleman - Gratitude Tour 2026", "2026-11-07", "20:00 - 23:00",
   "Germany's best-known reggae artist plays the Schlachthof Wiesbaden on his 'Gratitude' tour, with a full band performing roots reggae, dancehall and his classic hits.",
   "Tickets from ~40 EUR", "Schlachthof Wiesbaden, Murnaustr. 1, 65189 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/november/"))
A(ev("William Wahl - wahlweise", "2026-11-07", "20:00 - 22:00",
   "The former 'Basta' vocal acrobat performs solo in the Kongresshalle Gießen: a cappella loops, quirky German songs and dry humour.",
   "Tickets from ~28 EUR", "Kongresshalle Gießen, Berliner Platz 2, 35390 Gießen", "Literature & Arts", "Gießen",
   "https://www.eventfinder.de/giessen/veranstaltungen/november/"))
A(ev("Das Kriminal Dinner im Schlosshotel Weilburg", "2026-11-07", "19:00 - 23:00",
   "A murder-mystery dinner in the baroque Schlosshotel Weilburg above the Lahn: professional actors play the suspects between the courses of a multi-course menu.",
   "From ~75 EUR including dinner", "Schlosshotel Weilburg, Schloßplatz 2, 35781 Weilburg", "Food & Drink", "Weilburg",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/november/"))
A(ev("Riesling Gala im Kloster Eberbach (Glorreiche Rheingau Tage)", "2026-11-08", "12:00 - 20:00",
   "The crowning finale of the Glorreichen Rheingau Tage: 500 guests sit at one long table in the Laiendormitorium of Kloster Eberbach for a full-day gala menu, with the Rheingau VDP estates pouring matching Rieslings. Nearly 40 years of tradition.",
   "From ~350 EUR", "Kloster Eberbach, Laiendormitorium, 65346 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/feste/glorreiche-tage"))
A(ev("St. Martins-Umzug Lorsch", "2026-11-08", "17:00 - 19:30",
   "Lorsch's St Martin's lantern procession through the old town, with hand-made lanterns, brass band, a rider as St Martin on horseback and the traditional sharing of the cloak in front of the Kloster. Mulled drinks and Martin's pastries afterwards.",
   "Free", "Altstadt / Kloster Lorsch, 64653 Lorsch", "Family & Education", "Lorsch",
   "https://festam.app/de-de/feste-in-lorsch/"))
A(ev("Martinimarkt Weilmünster", "2026-11-08", "10:00 - 18:00",
   "Weilmünster's traditional Martinimarkt in the Weil valley: market stalls through the town centre, autumn produce, a funfair and later a St Martin's lantern parade for children.",
   "Free entry", "Innenstadt Weilmünster, 35789 Weilmünster", "Markets & Shopping", "Weilmünster",
   "https://schaustellerverband-schleswig-holstein.de/Bundesweit.html?bundesland=Hessen"))
A(ev("Veljanov - Solo", "2026-11-08", "20:00 - 22:30",
   "Alexander Veljanov, frontman of Deine Lakaien, plays a solo show at the Schlachthof Wiesbaden: dark-wave ballads, art song and material from his solo albums with piano and string accompaniment.",
   "Tickets from ~32 EUR", "Schlachthof Wiesbaden, Murnaustr. 1, 65189 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://www.eventfinder.de/wiesbaden/veranstaltungen/november/"))
A(ev("Herr Schröder", "2026-11-08", "20:00 - 22:00",
   "The award-winning German teacher-comedian performs his schoolroom satire in the Stadthallen Wetzlar, with an interactive 'lesson' format and plenty of audience participation.",
   "Tickets from ~26 EUR", "Stadthallen Wetzlar, Brühlsbachstr. 4, 35578 Wetzlar", "Literature & Arts", "Wetzlar",
   "https://www.eventfinder.de/wetzlar/veranstaltungen/november/"))
A(ev("Nights on Broadway - Tribute (Kassel)", "2026-11-08", "19:00 - 21:30",
   "A musical-theatre gala in the Probonio Arena Kassel with soloists and orchestra performing Broadway and West End repertoire from Phantom, Les Misérables, Wicked and The Lion King.",
   "Tickets from ~40 EUR", "Probonio Arena, Damaschkestr. 55, 34121 Kassel", "Music & Opera", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Sankt Martinsumzug Michelstadt", "2026-11-10", "17:00 - 19:30",
   "Michelstadt's St Martin's procession through the Odenwald old town, with lanterns, a brass band and a rider portraying St Martin at the Marktbrunnen. Warm drinks and Martinsbrezeln on the market square afterwards.",
   "Free", "Altstadt Michelstadt, 64720 Michelstadt", "Family & Education", "Michelstadt",
   "https://festam.app/de-de/feste-in-michelstadt/"))
A(ev("Rheingauer Krimiabend: Birgit Körner im Weingut Georg Breuer", "2026-11-11", "19:00 - 21:30",
   "Part of the 12th season of the Rheingauer Krimiabende held every Wednesday in November: Birgit Körner reads a local crime story in the Rüdesheim cellars of Weingut Georg Breuer, with wines poured alongside. Motto: 'Das Blut tropft - der Wein fließt'.",
   "From ~25 EUR including wine", "Weingut Georg Breuer, Rüdesheim am Rhein, 65385 Rüdesheim am Rhein", "Literature & Arts", "Rüdesheim am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-8"))
A(ev("Martinsumzug Gelnhausen", "2026-11-11", "17:30 - 19:30",
   "Gelnhausen's St Martin's lantern procession through the medieval old town, led by a rider on horseback, with brass band, lanterns made in the town's schools and kindergartens, and Martinsbrezeln at the Obermarkt.",
   "Free", "Obermarkt / Altstadt Gelnhausen, 63571 Gelnhausen", "Family & Education", "Gelnhausen",
   "https://festam.app/de-de/feste-in-gelnhausen/"))
A(ev("Maxi Gstettenbauer - KOMPLETT ABSURD", "2026-11-11", "20:00 - 22:00",
   "Stand-up comedy in the KUZ Kreuz Fulda: Maxi Gstettenbauer's 'KOMPLETT ABSURD' programme about everyday chaos, technology and the absurdity of modern life.",
   "Tickets from ~24 EUR", "KUZ Kreuz, Bahnhofstr. 1, 36037 Fulda", "Literature & Arts", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("Cecile Verny & Johannes Maikranz", "2026-11-12", "20:00 - 22:00",
   "The jazz singer with West African roots and the guitarist Johannes Maikranz interpret German art song and cabaret repertoire - from Knef and Zarah Leander to Schubert - in the Kultur- und Tagungshaus Rauenthal.",
   "Tickets from ~25 EUR", "Kultur- und Tagungshaus Rauenthal, 65345 Eltville am Rhein", "Music & Opera", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-8"))
A(ev("Matze Knop - Spitzenreiter", "2026-11-12", "20:00 - 22:15",
   "The German comedian and impressionist brings 'Spitzenreiter' to the Kongresshalle Gießen, with voices and impressions of German football and showbiz figures alongside his own songs.",
   "Tickets from ~30 EUR", "Kongresshalle Gießen, Berliner Platz 2, 35390 Gießen", "Literature & Arts", "Gießen",
   "https://www.eventfinder.de/giessen/veranstaltungen/november/"))
A(ev("exground filmfest 39", "2026-11-13", "14:00 - 23:00",
   "Wiesbaden's international festival of short and independent film (13-22 November) screens some 200 productions from around the world at the Caligari FilmBühne and other venues, with competitions, retrospectives and filmmaker Q&As.",
   "Single tickets from ~9 EUR, festival pass available", "Caligari FilmBühne, Marktplatz 9, 65183 Wiesbaden", "Film & Cinema", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Hofheimer Eiszauber", "2026-11-13", "14:00 - 21:00",
   "Hofheim's winter ice rink and winter village (13 November - 10 January) on the Kellereiplatz: open-air ice skating under floodlights, curling lanes, Alpine huts with mulled drinks and a small programme for children.",
   "Ice-rink ticket from ~7 EUR incl. skates", "Kellereiplatz Hofheim, 65719 Hofheim am Taunus", "Seasonal & Markets", "Hofheim am Taunus",
   "https://festam.app/de-de/feste-in-hofheim-am-taunus/"))
A(ev("Lichterzauber in Lorsch", "2026-11-13", "17:00 - 22:00",
   "Lorsch's old town is illuminated for one evening with light installations, lanterns and projections on the UNESCO-listed abbey complex, accompanied by street food, live music and late-opening shops.",
   "Free entry", "Altstadt / Kloster Lorsch, 64653 Lorsch", "Festival & Culture", "Lorsch",
   "https://festam.app/de-de/feste-in-lorsch/"))
A(ev("Martinsgans-Menü im Weingut Sohns", "2026-11-13", "19:00 - 22:00",
   "A seasonal three-course St Martin's goose menu at Weingut Sohns in Geisenheim, with red cabbage, braised apple, chestnuts and dumplings, matched to the estate's wines. A vegetarian alternative is offered.",
   "65 EUR per person", "Weingut Sohns, Geisenheim, 65366 Geisenheim", "Food & Drink", "Geisenheim",
   "https://www.rheingau.de/veranstaltungen/2026-11-8"))
A(ev("NightWash Live", "2026-11-13", "20:00 - 22:30",
   "The live touring version of the cult TV comedy show, recorded in the Stadthalle Baunatal: a line-up of stand-up comedians with a host, performed in the round.",
   "Tickets from ~30 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Literature & Arts", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Prison Break vs. Reality", "2026-11-13", "19:30 - 21:30",
   "A true-crime live talk at the Propstei Johannesberg Fulda: former investigators and journalists compare Hollywood prison-break fiction with real cases, with original footage and audience questions.",
   "Tickets from ~25 EUR", "Propstei Johannesberg, Johannesberg 2, 36041 Fulda", "Literature & Arts", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("Mamma Mia - ABBA Konzerttour", "2026-11-14", "20:00 - 22:30",
   "A full ABBA show with live band and vocalists in the S-Club Fulda, performing the complete greatest hits including Mamma Mia, Dancing Queen and Waterloo, with period costume.",
   "Tickets from ~30 EUR", "S-Club Fulda, Am Rosengarten 4, 36037 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("Klang - Geschichten - Raum", "2026-11-14", "15:30 - 17:00",
   "A matinée for families in Wiesbaden's Stadt- und Musikbibliothek with the Theater 3D: sound stories, instruments to try and short scenes built around listening and space, aimed at children and their adults.",
   "Free", "Stadt- und Musikbibliothek, Hochstättenstr. 6-10, 65183 Wiesbaden", "Family & Education", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Sekttage im Wein- und Sektgut F.B. Schönleber", "2026-11-14", "11:00 - 18:00",
   "Nine days of sparkling-wine events (14-22 November) at F.B. Schönleber in Mittelheim: cellar tours, riddling (Rüttel) demonstrations, Sekt seminars and tastings across the range of Rheingau Sekt.",
   "From ~20 EUR per tasting", "Wein- und Sektgut F.B. Schönleber, Mittelheim, 65375 Oestrich-Winkel", "Food & Drink", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("Judit Reigl. Couleur vivante. - Ausstellung", "2026-11-15", "10:00 - 18:00",
   "The Museum Reinhard Ernst opens a major survey of the Hungarian-French painter Judit Reigl (15 November 2026 - April 2027), tracing her abstract 'Couleur vivante' period and its links to the first post-war exhibition of French and German informal painting in Wiesbaden in 1957.",
   "Museum admission ~14 EUR", "Museum Reinhard Ernst, Wilhelmstr. 1, 65185 Wiesbaden", "Art & Exhibitions", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("Themenführung 'Der Name der Rose' im Kloster Eberbach", "2026-11-15", "14:00 - 15:30",
   "A guided tour linking the history of Kloster Eberbach with the shooting of 'The Name of the Rose': original props and film locations in the basilica and monk's dormitory, plus a welcome glass of Rheingau wine.",
   "From ~20 EUR incl. wine", "Kloster Eberbach, 65346 Eltville am Rhein", "Literature & Arts", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("LARS REICHOW: BOOMERLAND", "2026-11-15", "19:00 - 21:00",
   "The Mainz-born cabaret artist takes on the baby-boomer generation in 'BOOMERLAND' at the Rheingauer Wein Bühne: piano, wordplay and pointed social commentary.",
   "Tickets from ~28 EUR", "Rheingauer Wein Bühne, Frauenstein, 65375 Oestrich-Winkel", "Literature & Arts", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("Family Day im Museum", "2026-11-15", "14:00 - 17:00",
   "A hands-on family afternoon at the Museum für Gießen: short guided tours for children, craft stations, a treasure hunt through the collections and a chance to handle original objects with curators.",
   "Free for children, reduced adult ticket", "Museum für Gießen, Brandplatz 2, 35390 Gießen", "Family & Education", "Gießen",
   "https://www.giessen.de/Erleben/Veranstaltungen/"))
A(ev("Santiano - Die große Arena Tour 2026", "2026-11-16", "20:00 - 22:45",
   "Germany's leading shanty-rock band plays the Probonio Arena Kassel on their arena tour, with a large stage set, nautical staging and singalong hits from their albums.",
   "Tickets from ~45 EUR", "Probonio Arena, Damaschkestr. 55, 34121 Kassel", "Music & Opera", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Darmstädter Weihnachtsmarkt", "2026-11-16", "11:00 - 21:00",
   "Darmstadt's Christmas market (16 November - 23 December) spreads across the Marktplatz, Friedensplatz and the Schloss area with around 100 wooden huts, a giant Christmas tree, an ice rink, artisan crafts and a daily stage programme.",
   "Free entry", "Marktplatz / Friedensplatz Darmstadt, 64283 Darmstadt", "Seasonal & Markets", "Darmstadt",
   "https://festam.app/de-de/feste-in-darmstadt/"))
A(ev("Offenbacher Weihnachtsmarkt", "2026-11-16", "11:00 - 21:00",
   "Offenbach's Christmas market (16 November - 29 December) on the Marktplatz and Wilhelmsplatz: wooden huts with crafts and food, a Christmas pyramid, children's carousel and a live programme of choirs and bands.",
   "Free entry", "Marktplatz Offenbach, 63065 Offenbach am Main", "Seasonal & Markets", "Offenbach am Main",
   "https://festam.app/de-de/feste-in-offenbach-am-main/"))
A(ev("Herbstmarkt Bad Hersfeld", "2026-11-18", "09:00 - 18:00",
   "Bad Hersfeld's late-autumn market in the old town: Krammarkt stalls with textiles, household goods and regional food, plus a funfair on the Hattorfer Straße. Held in the tradition of the Lullus market days.",
   "Free entry", "Innenstadt Bad Hersfeld, 36251 Bad Hersfeld", "Markets & Shopping", "Bad Hersfeld",
   "https://festam.app/de-de/feste-in-bad-hersfeld/"))
A(ev("Rheingauer Krimiabend: Carola Christiansen bei den Winzern von Erbach", "2026-11-18", "19:00 - 21:30",
   "Another Wednesday evening in the Rheingauer Krimiabende series: Carola Christiansen reads a crime story among the vintners of Erbach, with Rheingau wines served through the evening.",
   "From ~25 EUR including wine", "Bachmanns Wein + Kultur / Winzer von Erbach, 65346 Eltville am Rhein", "Literature & Arts", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("SALÒ - Hardcore Ist Tot Tour 2026", "2026-11-18", "20:00 - 22:30",
   "The German rap duo plays the Kulturkeller Fulda, touring the 'Hardcore Ist Tot' record with their characteristic blend of punk energy and hip-hop.",
   "Tickets from ~22 EUR", "Kulturkeller Fulda, Karlstr. 8, 36037 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("Weihnachtsmarkt der Nationen Rüdesheim", "2026-11-19", "11:00 - 21:00",
   "Rüdesheim's international Christmas market (19 November - 23 December) turns the narrow alleys of the old town into a romantic Christmas village, with stands from around 20 nations, an Advent calendar window on the town hall and a nativity scene on the market square.",
   "Free entry", "Altstadt Rüdesheim, 65385 Rüdesheim am Rhein", "Seasonal & Markets", "Rüdesheim am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-22"))
A(ev("Weihnachtsstadt Bad Homburg (Winterzauber & Eiswinter)", "2026-11-19", "11:00 - 21:00",
   "Bad Homburg's Christmas town (19 November - 31 December): the Winterzauber market on the Schlossplatz with an ice rink and curling, the 'Eiswinter' sculpture exhibition in the Kurpark, illumination of the Schloss and a daily Advent programme.",
   "Free entry, ice rink from ~7 EUR", "Schlossplatz / Kurpark Bad Homburg, 61348 Bad Homburg vor der Höhe", "Seasonal & Markets", "Bad Homburg vor der Höhe",
   "https://festam.app/de-de/feste-in-bad-homburg/"))
A(ev("Jahreskonzert der Wiesbadener Musik- & Kunstschule", "2026-11-19", "19:00 - 21:00",
   "The annual concert of the Wiesbadener Musik- & Kunstschule e.V. in the Kulturforum Friedrichstraße: ensembles and soloists from all departments perform highlights from the year's work.",
   "From ~12 EUR", "Kulturforum, Friedrichstraße 16, 65183 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("FISCH & WEIN mit Gastkoch Jörg Hansen", "2026-10-25", "19:00 - 22:00",
   "Guest chef Jörg Hansen of Cuxhaven's Hotel Seelust - winner of the Goldene Kochmütze and Koch des Jahres - cooks a fish menu at Weingut Sohns in Geisenheim, matched with the estate's Rieslings.",
   "From ~75 EUR", "Weingut Sohns, Geisenheim, 65366 Geisenheim", "Food & Drink", "Geisenheim",
   "https://www.rheingau.de/veranstaltungen/2026-10-25"))
A(ev("Martinsgans - Weiß- oder Rotwein?", "2026-11-13", "18:30 - 23:00",
   "A five-course St Martin's goose dinner at Weingut Craß in Erbach with ten matched wines and sparkling wines, hosted with a wine commentary, welcome Sekt, water and espresso included.",
   "From ~95 EUR per person", "Weingut Craß, Erbach, 65346 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("Mirja Boes & die HonkeyDonkeys", "2026-11-20", "20:00 - 22:30",
   "Comedy and live music in the Stadthalle Baunatal: Mirja Boes performs her new programme with her band, blending stand-up, songs and improvisation.",
   "Tickets from ~32 EUR", "Stadthalle Baunatal, Marktplatz 1, 34225 Baunatal", "Literature & Arts", "Baunatal",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("FRIDAY BEATS - Masurka", "2026-11-20", "20:00 - 02:00",
   "Live music night in the WERKLOFT of Wiesbaden's Loftwerk: regional acts start the weekend, with Masurka - a versatile newcomer from Heidelberg - moving between R&B, soul, hip-hop, drum & bass and EDM. Drinks and DJ set afterwards.",
   "From ~10 EUR", "Loftwerk, Karlstr. 7, 65185 Wiesbaden", "Nightlife & Social", "Wiesbaden",
   "https://www.rheingau.de/veranstaltungen/2026-11-22"))
A(ev("Serdar Somuncu - HASSIAS", "2026-11-21", "20:00 - 22:30",
   "The writer, satirist and actor performs 'HASSIAS' in the Orangerie of the Maritim Hotel Fulda: a biting, high-tempo reckoning with German society and the phenomenon of hatred.",
   "Tickets from ~35 EUR", "Orangerie, Maritim Hotel Fulda, Paxtonplatz 1, 36037 Fulda", "Literature & Arts", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("Öffentliche Glühweinführung Kloster Eberbach", "2026-11-21", "16:00 - 17:30",
   "A winter guided tour of the Kloster Eberbach cloister with warm clothing and a glass of Glühwein: the Cistercian order, the abbey's economy and its wine history told through the roman-gothic ensemble.",
   "From ~20 EUR incl. Glühwein", "Kloster Eberbach, 65346 Eltville am Rhein", "Food & Drink", "Eltville am Rhein",
   "https://www.rheingau.de/veranstaltungen/2026-11-15"))
A(ev("Konzert zum Instrument des Jahres: Akkordeon", "2026-11-21", "19:00 - 20:30",
   "A concert in the Stadt- und Musikbibliothek Wiesbaden celebrating the accordion as Instrument of the Year, with solo and ensemble performances spanning tango, musette and contemporary repertoire.",
   "Free", "Stadt- und Musikbibliothek, Hochstättenstr. 6-10, 65183 Wiesbaden", "Music & Opera", "Wiesbaden",
   "https://wiesbadenaktuell.de/wp-content/uploads/2025/12/Jahreskalender-2026_Wiesbaden.pdf"))
A(ev("CONNY & Liser - Ælpha Male Club Tour 2026", "2026-11-21", "20:00 - 22:30",
   "Hip-hop in the Kulturzentrum Färberei Kassel: the duo CONNY & Liser perform their 'Ælpha Male Club Tour' set in an intimate club setting with support act.",
   "Tickets from ~20 EUR", "Kulturzentrum Färberei, Färberstr. 2, 34117 Kassel", "Music & Opera", "Kassel",
   "https://www.eventfinder.de/kassel/veranstaltungen/november/"))
A(ev("Loriot - live auf der Bühne", "2026-11-22", "18:00 - 20:00",
   "A staged homage to Loriot in the Esperantohalle Fulda: actors perform his best-known sketches - the potato, the noodle, the Advent poem - as live theatre, with original archive footage between scenes.",
   "Tickets from ~32 EUR", "Esperantohalle Fulda, Esperantostr. 2-4, 36037 Fulda", "Literature & Arts", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("The Music of Queen Live", "2026-11-22", "20:00 - 22:30",
   "A symphonic rock tribute in the Esperantohalle Fulda: a full band with orchestra performs Queen's catalogue, from Bohemian Rhapsody to We Will Rock You, with video staging.",
   "Tickets from ~40 EUR", "Esperantohalle Fulda, Esperantostr. 2-4, 36037 Fulda", "Music & Opera", "Fulda",
   "https://www.eventfinder.de/fulda/veranstaltungen/november/"))
A(ev("GERDA & WALTER: Do sin se widder!", "2026-11-22", "17:00 - 19:00",
   "The cult Hessian comedy duo returns with 'Noch mehr Kabbeleien' at the Rheingauer Wein Bühne: dialect sketches, songs and marital bickering in a warm, very Hessian evening.",
   "Tickets from ~25 EUR", "Rheingauer Wein Bühne, Frauenstein, 65375 Oestrich-Winkel", "Literature & Arts", "Oestrich-Winkel",
   "https://www.rheingau.de/veranstaltungen/2026-11-22"))

# ---- sort, validate, write ----
E.sort(key=lambda e: (e["date"], e["city"]))
CATS = {"Music & Opera", "Festival & Culture", "Literature & Arts", "Art & Exhibitions",
        "Food & Drink", "Film & Cinema", "Seasonal & Markets", "Sports",
        "Nightlife & Social", "Family & Education", "Markets & Shopping",
        "Convention & Pop Culture"}
assert len(E) == len({(e["title"], e["date"]) for e in E}), "duplicate title/date"
for e in E:
    assert set(e) == {"title", "date", "time", "description", "cost_per_person", "location",
                      "category", "city", "latitude", "longitude", "website",
                      "google_maps_link", "distance_from_frankfurt_km"}, e["title"]
    assert e["category"] in CATS, e["category"]
    assert e["city"] in D, e["city"]
    assert e["date"] >= "2026-09-13" and e["date"] <= "2026-11-22", e["date"]

out = {
    "last_updated": "2026-09-13",
    "research_date": "2026-09-13",
    "center": {"city": "Frankfurt am Main", "latitude": 50.1109, "longitude": 8.6821},
    "events": E,
}
path = os.path.expanduser("~/Desktop/PROJECTS/portal/hessen_events.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("events:", len(E))
print("cities:", len({e["city"] for e in E}))
print("categories:", len({e["category"] for e in E}))
print("range:", E[0]["date"], "->", E[-1]["date"])
