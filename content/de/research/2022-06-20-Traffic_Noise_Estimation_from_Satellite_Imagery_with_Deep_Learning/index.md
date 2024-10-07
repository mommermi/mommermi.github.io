---
date: 2022-06-20
title: Schätzung des Verkehrslärms aus Satellitenbildern mit Deep Learning
summary: |
  Straßenverkehrslärm ist ein globales Problem, das zu schweren gesundheitlichen Auswirkungen führen kann. Trotz der Allgegenwart von Verkehrslärm ist dessen Quantifizierung oder Schätzung kompliziert, und detaillierte Straßenverkehrskarten sind nur für ausgewählte Länder oder Regionen verfügbar. Wir untersuchen, ob es möglich ist, ein Regressionsmodell zu trainieren, um Straßenverkehrslärm aus Satellitenbildern zu schätzen.

tags:
- Erdbeobachtung
- Deep Learning
- Segmentierung
- Verkehrslärm
- Sentinel-2
thumbnail_image: stein.png

---

Straßenverkehrslärm stellt ein globales Gesundheitsproblem dar. Trotz seiner Bedeutung sind Lärmdaten in vielen Regionen der Welt nicht verfügbar. Solche Daten werden typischerweise durch Punktmessungen und komplexe physikalische Modelle abgeleitet, um die Ausbreitung von Lärm zu simulieren.

Da dieser Prozess in vielen Gebieten der Welt nicht durchführbar ist, schlagen wir vor, Lärmdaten aus Satellitenbildern in einem End-to-End-Deep-Learning-Ansatz zu approximieren. Wir trainieren ein U-Net-Segmentierungsmodell, um Verkehrslärm basierend auf frei verfügbaren Sentinel-2-Satellitenbildern und bestehenden Schätzungen des Straßenverkehrslärms für die Schweiz zu schätzen.

{{< image
src="stein.png"
descr="Ergebnisse unseres Ansatzes für das Dorf Stein (AR). Das obere linke Diagramm zeigt das True-Color (RGB)-Bild des Sentinel-2-Satellitenbildes, das als Eingabe für das Modell verwendet wurde. Das obere rechte Diagramm zeigt die Ground-Truth-Karte des Straßenverkehrslärms für dieselbe Szene, zusammen mit einigen Statistiken zur Lärmausbreitung. Die Vorhersage unseres Modells ist im unteren linken Diagramm mit den entsprechenden Lärmstatisiken dargestellt. Das untere rechte Diagramm zeigt das Histogramm beider Lärmausbreitungen." >}}

Unser Modell zeigt vielversprechende Ergebnisse: Es erreicht einen RMSE von 8,8 dB(A) für den Verkehrslärm tagsüber und 7,6 dB(A) für den Verkehrslärm nachts bei einer räumlichen Auflösung von 10m. Neben der Identifizierung wichtiger Straßennetze gelingt es unserem Modell, die räumliche Ausbreitung von Lärm mit einigen Einschränkungen vorherzusagen. Darüber hinaus stellen wir fest, dass unser Modell in ländlichen Gebieten besser abschneidet als in überfüllten städtischen Gebieten, was auf die begrenzte räumliche Auflösung der verwendeten Satellitenbilder zurückzuführen ist. Dennoch deuten unsere Ergebnisse darauf hin, dass dieser Ansatz einen Weg zur Schätzung des Straßenverkehrslärms für Gebiete bietet, für die keine solchen Maßnahmen verfügbar sind.

Diese Arbeit war das Bachelorarbeit-Projekt von Leonardo Eicher, der seine Ergebnisse auch auf der IGARSS 2022 präsentiert hat (siehe unten).

# Bibliographie

* Eicher, L., Mommert, M., Borth, D., "*Traffic Noise Estimation from Satellite Imagery with Deep Learning*", [IEEE International Geoscience and Remote Sensing Symposium 2022](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9883463)) ([open access](http://www.alexandria.unisg.ch/267269/1/IGARSS_traffic_noise.pdf)), 2022.