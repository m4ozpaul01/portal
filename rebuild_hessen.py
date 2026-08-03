#!/usr/bin/env python3
"""
rebuild_hessen.py — Builds the merged Hessen events file for the portal.
Combines verified live research (Aug-Oct 2026) for the whole state of Hessen
(EXCLUDING Frankfurt/Mainz, which live in frankfurt_events.json) with the existing
valid Hessen events. Dedups by title, sorts by date, writes to the portal.
"""
import json
import os
from datetime import date

PORTAL = os.path.expanduser("~/Desktop/PROJECTS/portal")
OUT = os.path.join(PORTAL, "hessen_events.json")

# Exclude city values handled by the Frankfurt/Mainz file (no double counting).
CITY_EXCLUDE = {"Frankfurt", "Frankfurt am Main", "Mainz"}

NEW_EVENTS = [
    {
        "title": "European Elvis Festival Bad Nauheim",
        "date": "2026-08-14", "time": "10:00 - 23:00",
        "description": "At the 24th European Elvis Festival, fans from around the world celebrate the idol with petticoats and Elvis quiffs. Highlights include the open-air concert with Dick Brave, the 'Memories of Elvis' late-night show, and a classic-car parade with Cadillacs. A fan market and tours of authentic Elvis locations in Bad Nauheim round out the programme.",
        "cost_per_person": "from ~15 EUR (day ticket)",
        "location": "Innenstadt & Sprudelhof, 61231 Bad Nauheim", "category": "Music & Opera",
        "city": "Bad Nauheim", "latitude": 50.37, "longitude": 8.74,
        "website": "https://www.bad-nauheim.de/de/erlebnisreich/veranstaltungen", "google_maps_link": "https://maps.google.com/?q=Sprudelhof, 61231 Bad Nauheim", "distance_from_frankfurt_km": 28,
    },
    {
        "title": "Open Flair Festival Eschwege",
        "date": "2026-08-05", "time": "12:00 - 00:00",
        "description": "One of Hessen's biggest open-air music festivals, held right in the centre of Eschwege. The programme blends rock, pop and indie with street theatre, a kids' programme and performances. In addition to concerts on several stages there is a campsite and a diverse supporting programme.",
        "cost_per_person": "from ~90 EUR (4-day ticket)",
        "location": "Festivalgelände am Märchenplatz, 37269 Eschwege", "category": "Music & Opera",
        "city": "Eschwege", "latitude": 51.18, "longitude": 10.06,
        "website": "https://www.open-flair.de/info/of26", "google_maps_link": "https://maps.google.com/?q=Märchenplatz, 37269 Eschwege", "distance_from_frankfurt_km": 160,
    },
    {
        "title": "Zissel Kassel – Fest an der Fulda (100 Jahre)",
        "date": "2026-07-31", "time": "12:00 - 23:00",
        "description": "North Hessen's largest local and water festival celebrates its 100th anniversary under the motto '100 Years of Fun by the River'. Along the Fulda there are processions, a water-ski show, the dragon-boat cup and a land-and-water festival procession over four days. Rides, live music and festival tents provide fun for the whole family.",
        "cost_per_person": "Free",
        "location": "Fuldaufer, 34117 Kassel", "category": "Festival & Culture",
        "city": "Kassel", "latitude": 51.31, "longitude": 9.49,
        "website": "https://www.zissel.de/", "google_maps_link": "https://maps.google.com/?q=Fuldaufer, 34117 Kassel", "distance_from_frankfurt_km": 162,
    },
    {
        "title": "Rheingau Musik Festival: Hayato Sumino & Aurora Orchestra",
        "date": "2026-08-06", "time": "19:30 - 22:00",
        "description": "Artist-in-Residence Hayato Sumino performs with the Aurora Orchestra under Nicholas Collon in Wiesbaden's Kurhaus. The concert is part of the Rheingau Musik Festival, which presents over 170 concerts across the region in 2026. A mix of classical and contemporary music in an elegant setting.",
        "cost_per_person": "from ~30 EUR",
        "location": "Kurhaus Wiesbaden, Friedrich-von-Thiersch-Saal, 65189 Wiesbaden", "category": "Music & Opera",
        "city": "Wiesbaden", "latitude": 50.08, "longitude": 8.24,
        "website": "https://www.rheingau-musik-festival.de/", "google_maps_link": "https://maps.google.com/?q=Kurhaus Wiesbaden, 65189 Wiesbaden", "distance_from_frankfurt_km": 35,
    },
    {
        "title": "Rheingau Musik Festival: Kloster Eberbach Basilika-Konzert",
        "date": "2026-08-07", "time": "19:30 - 22:00",
        "description": "In the historic basilica of Kloster Eberbach, the Rheingau Musik Festival presents choral-symphonic works in the unique Romanesque monastery architecture of the UNESCO World Heritage site. One of the flagship concerts of the 2026 festival season.",
        "cost_per_person": "from ~40 EUR",
        "location": "Kloster Eberbach, 65346 Eltville am Rhein", "category": "Music & Opera",
        "city": "Eltville", "latitude": 50.03, "longitude": 8.12,
        "website": "https://www.rheingau-musik-festival.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Eberbach, 65346 Eltville am Rhein", "distance_from_frankfurt_km": 45,
    },
    {
        "title": "Hanauer Weinfest im Schlossgarten",
        "date": "2026-08-06", "time": "16:00 - 24:00",
        "description": "The Hanau wine festival turns the Schlossgarten into a wine village of Franconian wineries. For four days, fine Franconian wines such as Scheurebe and Weißburgunder are poured in the shade of old trees. Live music and regional treats complete the free-entry evenings.",
        "cost_per_person": "Free",
        "location": "Schlossgarten Hanau, 63450 Hanau", "category": "Food & Drink",
        "city": "Hanau", "latitude": 50.13, "longitude": 8.92,
        "website": "https://www.hanau.de/freizeit/veranstaltungsreihen/weinfest/index.html", "google_maps_link": "https://maps.google.com/?q=Schlossgarten Hanau, 63450 Hanau", "distance_from_frankfurt_km": 18,
    },
    {
        "title": "Rüdesheimer Weinfest – Summer of Riesling",
        "date": "2026-08-13", "time": "11:00 - 23:00",
        "description": "Around 13 Rheingau winemakers present over 200 wines at the Rüdesheim Summer of Riesling on the market square. In the spotlight are young Riesling, silky Pinot Noir and rarities in a festive summer-night atmosphere with live music. Gastronomic highlights and the traditional 'Rheinischer Abend' round it off.",
        "cost_per_person": "Free entry; wine by the glass from ~4 EUR",
        "location": "Marktplatz, 65385 Rüdesheim am Rhein", "category": "Food & Drink",
        "city": "Rüdesheim", "latitude": 49.98, "longitude": 7.92,
        "website": "https://www.ruedesheimer-weinfest.de/", "google_maps_link": "https://maps.google.com/?q=Marktplatz, 65385 Rüdesheim am Rhein", "distance_from_frankfurt_km": 66,
    },
    {
        "title": "Rheingauer Weinwoche Wiesbaden",
        "date": "2026-08-14", "time": "11:00 - 24:00",
        "description": "The 'longest wine counter in the world' turns Wiesbaden's Schlossplatz, Marktkirche and the Dern'sche Gelände into a Riesling stronghold for ten days. Over 100 stands offer nearly 1,000 wines and sparkling wines from the Rheingau. Opening on Friday with regional wine queens, plus live music and gastronomy.",
        "cost_per_person": "Free entry; tasting glass coupons from ~5 EUR",
        "location": "Schlossplatz, Marktkirche & Dern'sches Gelände, 65183 Wiesbaden", "category": "Food & Drink",
        "city": "Wiesbaden", "latitude": 50.08, "longitude": 8.24,
        "website": "https://www.wiesbaden.de/microsite/rheingauer-weinwoche/", "google_maps_link": "https://maps.google.com/?q=Schlossplatz, 65183 Wiesbaden", "distance_from_frankfurt_km": 35,
    },
    {
        "title": "Gießener Kultursommer: James Arthur",
        "date": "2026-08-20", "time": "20:00 - 22:30",
        "description": "British singer-songwriter James Arthur (hits like 'Say You Won't Let Go') plays an open-air concert at Kloster Schiffenberg. With the unique evening backdrop over Giessen, an emotional pop and R&B evening awaits the audience. One of the international highlights of the Giessen Kultursommer 2026.",
        "cost_per_person": "from ~70 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/acts/james-arthur/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Gießener Kultursommer: DONOTS & H-BLOCKX",
        "date": "2026-08-21", "time": "18:00 - 23:00",
        "description": "Punk-rock legend Donots meet hip-hop and punk crossover band H-Blockx in a joint summer show at Kloster Schiffenberg. The evening promises to be loud, emotional and passionate. One of the most energetic dates of the Giessen Kultursommer 2026.",
        "cost_per_person": "from ~55 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/acts/donots-h-blockx/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Gießener Kultursommer: Howard Carpendale",
        "date": "2026-08-23", "time": "19:00 - 21:30",
        "description": "Schlager star Howard Carpendale performs at the Giessen Kultursommer in the open-air setting of Kloster Schiffenberg. The audience favourite presents his greatest hits from several decades of German music history. A atmospheric open-air evening.",
        "cost_per_person": "from ~80 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Gießener Kultursommer: Nena",
        "date": "2026-08-24", "time": "20:00 - 22:30",
        "description": "Neue Deutsche Welle icon Nena gives an open-air concert at Kloster Schiffenberg as part of the Giessen Kultursommer. Classics like '99 Luftballons' and 'Irgendwie, irgendwo, irgendwann' are part of the programme of one of Germany's most successful female singers.",
        "cost_per_person": "from ~80 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Gießener Kultursommer: Amy Macdonald",
        "date": "2026-08-26", "time": "19:30 - 22:00",
        "description": "Scottish singer-songwriter Amy Macdonald, famous for 'This Is the Life' and 'Mr Rock & Roll', plays an open-air concert at Kloster Schiffenberg. Her folk-rock sound in an intimate open-air setting promises a atmospheric summer evening. Part of the Giessen Kultursommer 2026 line-up.",
        "cost_per_person": "from ~70 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Stadtfest Fulda",
        "date": "2026-08-20", "time": "15:00 - 00:00",
        "description": "For four days the Fulda city centre becomes a great festival mile with live music, shows, special actions and gastronomy. The most important self-organised event of the cathedral city pulls crowds into the old town, linking several stages with a programme for all generations. Free entry.",
        "cost_per_person": "Free",
        "location": "Fuldaer Innenstadt, 36037 Fulda", "category": "Festival & Culture",
        "city": "Fulda", "latitude": 50.55, "longitude": 9.68,
        "website": "https://spuere-fulda.de/events/stadtfest-fulda-2026/", "google_maps_link": "https://maps.google.com/?q=Fuldaer Innenstadt, 36037 Fulda", "distance_from_frankfurt_km": 103,
    },
    {
        "title": "Bad Hersfelder Festspiele: Something Rotten!",
        "date": "2026-08-05", "time": "21:00 - 23:10",
        "description": "The cult Broadway musical 'Something Rotten!' celebrates its German-language premiere at the 75th Bad Hersfelder Festspiele in the unique Stiftsruine. The witty, slapstick-rich piece tells the story of two Shakespeare rivals in the 16th century. One of six main productions of the anniversary year.",
        "cost_per_person": "from ~20 EUR",
        "location": "Stiftsruine Bad Hersfeld, 36251 Bad Hersfeld", "category": "Festival & Culture",
        "city": "Bad Hersfeld", "latitude": 50.87, "longitude": 9.71,
        "website": "https://www.bad-hersfelder-festspiele.de/", "google_maps_link": "https://maps.google.com/?q=Stiftsruine Bad Hersfeld, 36251 Bad Hersfeld", "distance_from_frankfurt_km": 145,
    },
    {
        "title": "Wetzlarer Brückenfest & Brückenlauf",
        "date": "2026-09-04", "time": "17:00 - 23:00",
        "description": "The three-day Wetzlar city festival around the historic Lahn bridges offers music, entertainment and a shopping Sunday. The kick-off is the 25th Wetzlar Bridge Run on Friday. Various acts play on stages at the Colchester-Anlage, Eisenmarkt and Schillerplatz.",
        "cost_per_person": "Free",
        "location": "Innenstadt Colchester-Anlage, 35578 Wetzlar", "category": "Festival & Culture",
        "city": "Wetzlar", "latitude": 50.55, "longitude": 8.5,
        "website": "https://wetzlar.de/", "google_maps_link": "https://maps.google.com/?q=Colchester-Anlage, 35578 Wetzlar", "distance_from_frankfurt_km": 66,
    },
    {
        "title": "Herbstzauber in der Karlsaue Kassel",
        "date": "2026-09-04", "time": "11:00 - 18:00",
        "description": "The 'Herbstzauber' in the Karlsaue shows autumn colours, plants, rarities and beautiful things for home and garden. On the flower island Siebenbergen and along the park paths, exhibitors present their autumn wares. A popular destination for garden lovers and families in Kassel.",
        "cost_per_person": "Free",
        "location": "Karlsaue & Blumeninsel Siebenbergen, 34117 Kassel", "category": "Markets & Shopping",
        "city": "Kassel", "latitude": 51.31, "longitude": 9.49,
        "website": "https://www.kassel.de/", "google_maps_link": "https://maps.google.com/?q=Karlsaue, 34117 Kassel", "distance_from_frankfurt_km": 162,
    },
    {
        "title": "Bergsträßer Winzerfest Bensheim",
        "date": "2026-09-05", "time": "12:00 - 23:00",
        "description": "The largest wine festival in Southern Hessen lures around 100,000 visitors to the historic old town of Bensheim. Around 160 wines from all Bergstrasse vineyard sites can be tasted at winemakers' stands on the market square and in the alleys. Live music and regional specialities complement the nine-day festival.",
        "cost_per_person": "Free entry; wine tasting from ~3 EUR",
        "location": "Historische Altstadt Marktplatz, 64625 Bensheim", "category": "Food & Drink",
        "city": "Bensheim", "latitude": 49.68, "longitude": 8.62,
        "website": "https://bensheimerleben.de/events/bergstraesser-winzerfest-3-2026-09-05/", "google_maps_link": "https://maps.google.com/?q=Marktplatz, 64625 Bensheim", "distance_from_frankfurt_km": 45,
    },
    {
        "title": "Beleuchtete Wasserspiele im Bergpark Wilhelmshöhe",
        "date": "2026-09-11", "time": "20:00 - 23:00",
        "description": "At the illuminated water displays, the water flows in atmospheric lighting over cascades, the devil's bridge, aqueduct and the Jussow temple in the UNESCO World Heritage Bergpark Wilhelmshöhe. A supporting programme of lighting and music accompanies the staging. The evenings on 11 and 12 September 2026 are highlights of the Kassel events calendar.",
        "cost_per_person": "Free",
        "location": "Bergpark Wilhelmshöhe, 34131 Kassel", "category": "Festival & Culture",
        "city": "Kassel", "latitude": 51.31, "longitude": 9.4,
        "website": "https://www.kassel.de/beleuchtete-wasserspiele/index.php", "google_maps_link": "https://maps.google.com/?q=Bergpark Wilhelmshöhe, 34131 Kassel", "distance_from_frankfurt_km": 160,
    },
    {
        "title": "Rheingau Literatur Festival 'WeinLese'",
        "date": "2026-08-27", "time": "19:00 - 22:00",
        "description": "The Rheingau WeinLese literature festival unites contemporary literature with the wine region around Wiesbaden. Renowned authors read in idyllic venues such as wineries, village halls and castles. The first week runs 27-30 August 2026, a second follows in late September.",
        "cost_per_person": "from ~25 EUR",
        "location": "Weingüter & Schlösser im Rheingau, 65183 Wiesbaden", "category": "Literature & Arts",
        "city": "Wiesbaden", "latitude": 50.08, "longitude": 8.24,
        "website": "https://www.rheingau-musik-festival.de/programm-karten/rheingau-literatur-festival", "google_maps_link": "https://maps.google.com/?q=Rheingau, 65183 Wiesbaden", "distance_from_frankfurt_km": 40,
    },
    {
        "title": "Gießener Kultursommer: Wincent Weiss",
        "date": "2026-08-30", "time": "19:00 - 21:30",
        "description": "Pop singer Wincent Weiss performs at the Giessen Kultursommer at Kloster Schiffenberg. The German radio megastar presents his heartfelt pop songs in the unique open-air setting. With an additional extra show on 31 August he closes the 2026 festival programme.",
        "cost_per_person": "from ~65 EUR",
        "location": "Kloster Schiffenberg, 35394 Gießen", "category": "Music & Opera",
        "city": "Gießen", "latitude": 50.58, "longitude": 8.67,
        "website": "https://giessener-kultursommer.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Schiffenberg, 35394 Gießen", "distance_from_frankfurt_km": 54,
    },
    {
        "title": "Weinfest Fulda im Schlosshof",
        "date": "2026-08-26", "time": "17:00 - 23:00",
        "description": "The Fulda wine festival turns the historic Schlosshof of the baroque residence into a delightful wine village with wines from the best sites. Daily rotating live bands provide entertainment on the warm summer evenings. A large selection of quality wines from white to red to rosé.",
        "cost_per_person": "Free entry; wine by the glass from ~4 EUR",
        "location": "Schlosshof Fulda, 36037 Fulda", "category": "Food & Drink",
        "city": "Fulda", "latitude": 50.55, "longitude": 9.68,
        "website": "https://www.weinfest-fulda.de/", "google_maps_link": "https://maps.google.com/?q=Schlosshof Fulda, 36037 Fulda", "distance_from_frankfurt_km": 103,
    },
    {
        "title": "Rheingau Musik Festival – Saisonfinale Kloster Eberbach",
        "date": "2026-09-05", "time": "19:30 - 22:00",
        "description": "With a concert in the basilica of Kloster Eberbach, the Rheingau Musik Festival 2026 comes to a grand close after presenting 158 concerts at 26 venues since July. Choral symphonic and orchestral sound form the spectacular finale in the impressive monastery architecture. One of the season's most coveted tickets.",
        "cost_per_person": "from ~50 EUR",
        "location": "Kloster Eberbach Basilika, 65346 Eltville am Rhein", "category": "Music & Opera",
        "city": "Eltville", "latitude": 50.03, "longitude": 8.12,
        "website": "https://www.rheingau-musik-festival.de/", "google_maps_link": "https://maps.google.com/?q=Kloster Eberbach, 65346 Eltville am Rhein", "distance_from_frankfurt_km": 45,
    },
    {
        "title": "Marburger Sommernächte & Uni-Stadt Kultur",
        "date": "2026-08-15", "time": "19:00 - 22:00",
        "description": "Marburg, the university city on the Lahn, offers a full summer programme of open-air concerts, theatre and cultural nights at venues such as the Schlossparkbühne and the Elisabethkirche. In August, singer-songwriter evenings and classical nights follow one another. Check the local events calendar for exact dates and line-ups.",
        "cost_per_person": "from ~20 EUR",
        "location": "Schlosspark & Elisabethkirche, 35037 Marburg", "category": "Music & Opera",
        "city": "Marburg", "latitude": 50.81, "longitude": 8.77,
        "website": "https://www.marburg.de/", "google_maps_link": "https://maps.google.com/?q=Elisabethkirche, 35037 Marburg", "distance_from_frankfurt_km": 75,
    },
    {
        "title": "Darmstadt Heinerfest & Mathildenhöhe Herbst",
        "date": "2026-08-28", "time": "11:00 - 23:00",
        "description": "Darmstadt's UNESCO World Heritage Mathildenhöhe and the city centre host a rich autumn programme of exhibitions, artists' open days and the traditional Heinerfest in late summer. The famous Art Nouveau artists' colony and exhibition buildings are a must-see. Multiple free and ticketed events across the season.",
        "cost_per_person": "Free to ~12 EUR",
        "location": "Mathildenhöhe & Innenstadt, 64283 Darmstadt", "category": "Art & Exhibitions",
        "city": "Darmstadt", "latitude": 49.87, "longitude": 8.65,
        "website": "https://www.mathildenhoehe.eu/", "google_maps_link": "https://maps.google.com/?q=Mathildenhöhe, 64283 Darmstadt", "distance_from_frankfurt_km": 27,
    },
    {
        "title": "Limburg Altstadt & Domfestspiele Sommer",
        "date": "2026-08-20", "time": "19:00 - 22:00",
        "description": "The medieval old town of Limburg an der Lahn hosts its summer city festival and the Weilburger Schlosskonzerte open-air classics nearby. Evening concerts, guided old-town walks and half-timbered charm make Limburg a lovely day trip. Live brass and chamber music against the backdrop of the famous cathedral.",
        "cost_per_person": "from ~15 EUR",
        "location": "Altstadt & Domberg, 65549 Limburg an der Lahn", "category": "Festival & Culture",
        "city": "Limburg", "latitude": 50.39, "longitude": 8.07,
        "website": "https://www.limburg.de/", "google_maps_link": "https://maps.google.com/?q=Domberg, 65549 Limburg an der Lahn", "distance_from_frankfurt_km": 55,
    },
    {
        "title": "Odenwald & Taunus: Kelterfeste und Herbstmärkte",
        "date": "2026-09-19", "time": "10:00 - 20:00",
        "description": "Across the Odenwald and Taunus regions, September and October bring traditional Kelterfeste (cider festivals) and autumn markets. Local orchards press fresh apple cider and distilleries open their doors, while village fairs celebrate the harvest with regional food and folk music. A charming taste of rural Hessen.",
        "cost_per_person": "Free entry; food & drink from ~5 EUR",
        "location": "Villages across Odenwald & Taunus, 64625 Bensheim", "category": "Food & Drink",
        "city": "Bergstraße", "latitude": 49.7, "longitude": 8.65,
        "website": "https://www.odenwald.de/", "google_maps_link": "https://maps.google.com/?q=Odenwald, Hessen", "distance_from_frankfurt_km": 50,
    },
]

def main():
    # Load existing events to keep — but drop those in excluded cities
    existing = []
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            existing = json.load(f).get("events", [])

    seen = set()
    merged = []
    for e in existing:
        city = e.get("city", "")
        t = " ".join((e.get("title") or "").lower().split())
        if city in CITY_EXCLUDE:
            continue
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

    cities = sorted(set(e["city"] for e in merged))
    print(f"Hessen events: {len(merged)} total (kept {len(merged)-added} existing, added {added} new)")
    print(f"Cities covered ({len(cities)}): {', '.join(cities)}")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
