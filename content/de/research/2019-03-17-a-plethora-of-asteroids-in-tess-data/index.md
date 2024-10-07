---
date: 2019-03-17
title: Eine Fülle von Asteroiden in TESS-Daten
summary: |
  TESS ist ein Satellit, der helle Sterne beobachtet, um Helligkeitsmodulationen zu finden, die Exoplanetentransite offenbaren – aber er beobachtet auch viele Asteroiden über einen langen Zeitraum, was ihn zu einem einzigartigen Instrument zur Ableitung langer Rotationsperioden von Asteroiden macht.
tags:
- Astronomie
- Asteroid
- physikalische Eigenschaften von Asteroiden
- TESS
featured_image: /research/12893.png
thumbnail_image: https://upload.wikimedia.org/wikipedia/commons/c/c2/Transiting_Exoplanet_Survey_Satellite_artist_concept_%28transparent_background%29.png
---

TESS ist der [Transiting Exoplanet Survey Satellite](https://tess.mit.edu/), der 2018 von der NASA ins All gestartet wurde, um schwache Helligkeitsvariationen in Sternen zu identifizieren, die charakteristisch für Planeten sind, die um diese Sterne kreisen und vor ihnen transitiert.
{{< image
src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Transiting_Exoplanet_Survey_Satellite_artist_concept_%28transparent_background%29.png"
descr="Eine Darstellung des TESS-Raumschiffs. Das Instrument besteht aus vier Bildkameras, die jeweils 24° x 24° des Himmels abdecken." >}}

Im Laufe seiner nominalen zweijährigen Mission wird TESS mehr als 200.000 Sterne mit der photometrischen Genauigkeit überwachen, die notwendig ist, um Exoplanet-Transite zu identifizieren. Um diese riesige Anzahl von Sternen zu beobachten, richtet TESS seine Beobachtungen auf verschiedene "Sektoren" am Himmel, die insgesamt 85 % des gesamten Himmels ausmachen. Jeder Sektor, der 24° x 96° umfasst, wird über einen Zeitraum von etwa einem Monat beobachtet.

Die TESS-Daten sind öffentlich über [MAST](https://archive.stsci.edu/tess/) verfügbar – einschließlich kalibrierter Full Frame Images, die über einen Zeitraum von jeweils 30 Minuten gestapelt werden. Angesichts des riesigen Sichtfelds der TESS-Kameras sollte es zu jedem Zeitpunkt eine enorme Anzahl von Asteroiden in jedem Bild geben. Also machte ich mich auf eine Asteroiden-Fischfang-Expedition...


# Extraktion von Asteroiden aus TESS-Daten

Die Idee ist konzeptionell einfach:

- TESS Full Frame-Bilder herunterladen und vorverarbeiten für die weitere Analyse;
- Eine Hintergrundsubtraktion durchführen, um Sterne und andere feste Quellen zu entfernen, um die Erkennung beweglicher Objekte zu verbessern;
- Die Positionen aller bekannten ~800.000 Asteroiden zum Zeitpunkt der Beobachtungen vorhersagen, um sie in den Bildern identifizieren zu können;
- Photometrie durchführen und ihre Helligkeit messen.

Wenn wir all diese Teile zusammenfügen, können wir Helligkeitsvariationen einer großen Anzahl von Asteroiden über einen Zeitraum von bis zu fast einem Monat messen – dies ist ein einzigartiger Datensatz, der die genaue Messung von Rotationsperioden über einen kontinuierlichen Zeitraum ermöglicht, der vom Boden aus nicht zugänglich ist: Bedenken Sie, dass bodengestützte Beobachtungen auf Nachtbeobachtungen beschränkt sind, während TESS in der Lage ist, 24/7 zu beobachten.

Dieses Projekt ist hauptsächlich ein rechnerisches Problem: Das Betreiben einer von vier Kameras pro Sektor auf einem Desktop-Computer dauert etwa einen Tag. Multithreading wurde dort implementiert, wo es möglich ist, um die Verarbeitung zu beschleunigen.

# Erste Ergebnisse

Ein erstes cooles Ergebnis ist in diesem kurzen Videoausschnitt zu sehen:

<iframe src="https://player.vimeo.com/video/323253379?h=a5dbce3ca8" width="640" height="320" frameborder="0" allow="autoplay; fullscreen"
allowfullscreen></iframe>

Dieses Video zeigt die Rotationslichtkurve des Asteroiden 1693 Hertzsprung. Das linke Diagramm zeigt ein Thumbnail-Bild, das auf den Asteroiden zentriert ist, und das rechte Diagramm zeigt die Helligkeit des Ziels. Mit fortschreitender Zeit wird die Variation in der Helligkeit, die durch die unregelmäßige Form und Rotation des Asteroiden verursacht wird, offensichtlich. Dieser spezifische Asteroid hat eine Rotationsperiode von etwa 9 Stunden. Lücken erscheinen in der Lichtkurve, wenn der Asteroid zu nah an Bereichen kommt, die von Bildartefakten betroffen sind, die im linken Diagramm mit roten Überlagerungen hervorgehoben sind.

# Momentaner Stand

Die Analyse des vollständigen TESS-Datensatzes wird nun durch ein NASA-Stipendium finanziert, und unsere erste Veröffentlichung ist verfügbar: [McNeill et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJS..245...29M/abstract). 

... und ein zweites Paper ist nun auch verfügbar: [McNeill et al. (2023)](https://iopscience.iop.org/article/10.3847/1538-3881/acf194/pdf).

# Bibliographie

* McNeill, A., Mommert, M., Trilling, D. E., Llama, J., & Skiff, B. (2019), "*Asteroid Photometry from the Transiting Exoplanet Survey Satellite: A Pilot Study*", The Astrophysical Journal Supplement Series, 245, 29., [publication](http://doi.org/10.3847/1538-4365/ab5223), [arxiv](http://arxiv.org/abs/1911.01495)

* McNeill, A., Gowanlock, M., Mommert, M., Trilling, D. E., Llama, J., & Paddock, N. (2023), "*An Untargeted Survey of the Rotational Properties of Main-belt Asteroids using the
Transiting Exoplanet Survey Satellite (TESS)*", The Astronomical Journal, 166, 152, [publication](https://iopscience.iop.org/article/10.3847/1538-3881/acf194/pdf).
