---
date: 2021-11-17
title: Erkennung von LKWs auf Satellitenbildern mit Deep Learning
summary: |
  Können wir Lastwagen aus dem Weltraum identifizieren um das Verkehrsaufkommen abzuschätzen? Ja, das können wir!
tags:
- Erdbeobachtung
- Deep Learning
- Verkehr
- Sentinel-2
thumbnail_image: trucks.png

---

Der LKW-Verkehr ist derzeit für 7% der globalen CO2-Emissionen verantwortlich. Während der Straßenfrachtverkehr das dominierende Transportmittel für Oberflächenfracht bleiben wird, wird sein Beitrag zum Klimawandel voraussichtlich kurzfristig zunehmen. Daher ist die quantitative Überwachung des Verkehrs von Nutzfahrzeugen entscheidend für die Umsetzung gezielter Emissionsvorschriften für Straßen. Allerdings sind Bodenüberwachungsstationen kostspielig, und weniger als die Hälfte aller Länder weltweit erfasst die Aktivitäten im Straßenfrachtverkehr. In dieser Arbeit untersuchen wir die Machbarkeit der Erkennung und Überwachung des Nutzfahrzeugverkehrs in frei verfügbaren Satellitenbildern der Sentinel-2-Satelliten der ESA.

{{< image
src="trucks.png"
descr="Grüne Kästchen kennzeichnen Nutzfahrzeuge auf einem Autobahn-Abschnitt in der Schweiz. Aufgrund einer Verzögerung bei der Bildaufnahme der verschiedenen Kanäle zeigen sich bewegende Objekte in Sentinel-2-Bildern mit einem charakteristischen regenbogenartigen Erscheinungsbild." >}}


{{< image
src="setup.png"
descr="Workflow dieses Projekts. Wir sammeln Satellitenbilder und Ground-Truth-Verkehrszählraten für Nutzfahrzeuge, identifizieren einzelne Fahrzeuge mit einem Objekterkennungsmodell und trainieren schließlich baumbasierte Modelle auf Zählungen, um stündliche Verkehrsraten für die betrachteten Standorte abzuschätzen." >}}

Für diese Aufgabe beziehen wir Sentinel-2 Satellitenbilder für 33 Standorte, die auf Abschnitten der Schweizer Autobahn zentriert sind, um Nutzfahrzeuge mit einem Deep-Learning-Ansatz zu identifizieren. Wir erkennen LKWs mit einem modifizierten Faster R-CNN Objekterkennungsmodell, indem wir ein charakteristisches Merkmal von bewegenden Objekten in den Sentinel-2-Daten ausnutzen: Eine konstante Verzögerung zwischen der Bildaufnahme in den verschiedenen Kanälen führt zu einem charakteristischen "regenbogenartigen" Erscheinungsbild für Objekte, die sich mit ausreichender Geschwindigkeit bewegen, was leicht zu erkennen ist. Nach dem Training unseres Modells finden wir eine durchschnittliche Präzision von 72% für die Erkennung von CVs in unseren Bilddaten. Das Modell zeigt zudem ähnliche Leistungsergebnisse für Autobahnabschnitte außerhalb Europas (siehe Abbildung unten).

{{< image
src="brazil.png"
descr="Wir testen unseren Ansatz zur Objekterkennung an Satellitenbildern, die außerhalb der Schweiz. In diesem Beispiel identifiziert das trainierte Modell korrekt alle Nutzfahrzeuge auf einem Autobahnabschnitt in Brasilien (die extrahierten Erkennungen sind rechts dargestellt)." >}}

Für jeden Autobahnabschnitt, der in diesem Projekt betrachtet wird, sind Ground-Truth-Verkehrszähldaten von ASTRA verfügbar, die es uns ermöglichen, die Snapshot-Zählungen von Nutzfahrzeugen in stündliche Verkehrsrate umzuwandeln. Zu diesem Zweck haben wir gradientenverstärkte baumbasierte Regressionsmodelle trainiert, um die Verkehrsraten aus der Anzahl der pro Autobahnabschnitt gezählten LKWs aus unseren Bilddaten sowie anderen Merkmalen vorherzusagen. Wir stellen fest, dass es möglich ist, stündliche Verkehrsvolumina für jeden Autobahnabschnitt der Welt innerhalb von 65% des tatsächlichen Wertes oder mit einem Root Mean Square Error (RMSE) von etwa 160 Fahrzeugen pro Stunde zu messen. Für Autobahnabschnitte mit verfügbaren, aber begrenzten Ground-Truth-Daten können wir die Verkehrsvolumina bis auf 4% genau vorhersagen und erreichen einen RMSE von etwa 60 Fahrzeugen pro Stunde. Wir finden, dass unsere Modelle am besten auf Satellitenbilder mit geringer Bewölkung und für Autobahnabschnitte über 1 Kilometer Länge angewendet werden.

{{< image
src="covid.png"
descr="Unser kombinierter Modellansatz ermöglicht die Erkennung von Veränderungen in den Verkehrsraten im Jahr 2020 aufgrund der Covid-19-Lockdown-Regelungen in der Schweiz für verschiedene Einreisepunkte. In Übereinstimmung mit den Ground-Truth-Verkehrsraten stellen wir fest, dass die Grenze zu Italien am stärksten von einem Rückgang des Verkehrs betroffen war, während die Grenze zu Deutschland kaum betroffen war." >}}

Darüber hinaus ermöglichen unsere Ergebnisse die Schätzung des relativen Rückgangs des Verkehrs aufgrund von Lockdown-Maßnahmen während der ersten Welle der COVID-19-Pandemie in der Schweiz im Jahr 2020 (siehe Abbildung oben).

Abschließend lässt sich sagen, dass unser Ansatz die Schätzung der Verkehrsraten ausschließlich aus Fernerkundungsdaten ermöglicht, was ihn auf globaler Ebene anwendbar macht. Die hier vorgestellten Methoden stellen ein leistungsstarkes Werkzeug dar, um die LKW-Verkehrsraten in Gebieten zu schätzen, in denen bodengestützte Verkehrsmessungen nicht verfügbar sind.

Dieses Projekt basiert auf den Ergebnissen der Masterarbeit von MBI-Student Moritz Blattner, der dieses Projekt auch auf dem [ICML 2021 Tackling Climate Change with Machine Learning Workshop](https://www.climatechange.ai/papers/icml2021/19) vorgestellt hat.

# Bibliographie

* Blattner, M., Mommert, M., Borth, D., "Commercial Vehicle Traffic Detection from Satellite Imagery with Deep Learning", ICML 2021 Tackling Climate Change with Machine Learning Workshop [publication (open access)](https://www.climatechange.ai/papers/icml2021/19).