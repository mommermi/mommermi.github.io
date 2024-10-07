---
date: 2020-12-07
title: Charakterisierung industrieller Abgasfahnen aus Fernerkundungsdaten
summary: |
  Treibhausgasemissionen aus dem industriellen Wirtschaftssektor sind ein wesentlicher Treiber des derzeit beobachteten Klimawandels. Wir haben einen Ansatz des maschinellen Lernens entwickelt, um industrielle Rauchfahnen zu identifizieren und zu charakterisieren. In Zukunft werden wir diesen Ansatz nutzen, um Treibhausgasemissionen aus Fernerkundungsdaten im globalen Maßstab zu schätzen.
tags:
- Eardbeobachtung
- Deep Learning
- Segmentierung
- Abgasfahne
- Sentinel-2
thumbnail_image: example_panel.png
---

Der Haupttreiber der globalen Erwärmung ist Freisetzung von Treibhausgasemissionen (THG) aus industriellen Aktivitäten. Die quantitative Überwachung dieser Emissionen ist notwendig, um ihre Auswirkungen auf das Klima der Erde vollständig zu verstehen und Emissionsvorschriften im großen Maßstab durchzusetzen. In dieser Arbeit untersuchen wir die Möglichkeit, industrielle Rauchfahnen aus global und kostenlos verfügbaren Multiband-Bilddaten der Sentinel-2-Satelliten der ESA zu erkennen und zu quantifizieren.

{{< image
src="example_panel.png"
descr="Beispielbilder aus unserem Satz von 21.350 Bildern industrieller Standorte. Jede Spalte entspricht einem der 624 Standorte. Die oberste Reihe zeigt den Standort während der Aktivität (eine Abgasfahne ist vorhanden) und die untere Reihe während der Inaktivität (Abgasfahne ist nicht vorhanden). Die Ursprungsregion der Abgasfahne ist durch rote Kreise markiert." >}}


### Klassifizierung der Abgasfahnen

Mit einem modifizierten ResNet-50 können wir Abgasfahnen unterschiedlicher Größen mit einer Genauigkeit von 94,3% erkennen. Das Modell ignoriert korrekt natürliche Wolken und konzentriert sich auf die Bildkanäle, die mit der spektralen Absorption von Aerosolen und Wasserdampf in Zusammenhang stehen, was die Lokalisierung von Rauch ermöglicht.


{{< image
src="activation_example.png"
descr="Beispieleaus unserem Klassifizierungsmodell. Für verschiedene Beispiele aus unserem Testdatensatz (Spalten) zeigen wir das echte Farbbild (oberste Reihe), ein Falschfarbbild (mittlere Reihe) und die Aktivierungen einiger versteckter Schichten in unserer ResNet-Implementierung (unterste Reihe, die über die gesamte Reihe dasselbe Scaling verwendet). Wir stellen fest, dass der Standort der Fahne in den meisten Fällen mit signifikanten Aerosol- und Wasserdampfsignalen korreliert und dass die Aktivierungen der versteckten Schichten auf der Grundlage dieser Signale feuern, was zu einer guten Lokalisierung des Rauchs führt." >}}

### Segmentierung der Abgasfahnen 

Wir nutzen diese Lokalisierungsfähigkeit und trainieren ein U-Net-Segmentierungsmodell auf einer annotierten Teilstichprobe unserer Daten, was zu einem Intersection-over-Union (IoU)-Wert von 0,608 und einer Gesamtgenauigkeit von 94,0 % bei der Erkennung von Rauchfahnen führt; im Durchschnitt kann unser Modell die von einer Fahne bedeckte Fläche auf 5,6% genau reproduzieren. Die Leistung unseres Modells wird hauptsächlich durch gelegentliche Verwechslungen mit Oberflächenobjekten, die Unfähigkeit, halbtransparenten Rauch zu identifizieren, und menschliche Einschränkungen bei der korrekten Identifizierung von Fahrend basierend auf RGB-Bildern begrenzt. Dennoch ermöglichen uns unsere Ergebnisse, Aktivität zuverlässig zu erkennen und qualitativ den Grad der Aktivität zu schätzen, um Industrieanlagen weltweit zu überwachen. Unser Datensatz und unsere Codebasis sind öffentlich verfügbar.

{{< image
src="segmentation_example.png"
descr="Beispiele für die Leistung unseres Segmentierungsmodells. Für verschiedene Bilder aus unserer Teststichprobe (Spalten) zeigen wir das RGB-Bild (oberste Reihe), ein Falschfarbenbild (mittlere Reihe) und die Footprints der Ground-Truth-Labels (rote Bereiche) sowie der vorhergesagten Labels (grüne Bereiche). Im Allgemeinen identifiziert das Segmentierungsmodell Abgasfahnen zuverlässig mit wenigen Einschränkungen." >}}


Diese Arbeit wurde auf dem [``Tackling Climate Change with Machine Learning'' Workshop bei NeurIPS 2020](https://www.climatechange.ai/papers/neurips2020/9) und der  [2021 NVIDIA GTC](https://www.nvidia.com/en-us/gtc/) präsentiert.
Der [Code](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection) und der [Datensatz](https://zenodo.org/record/4250706) sind online verfügbar.


Diese Arbeit wurde von unserer Doktorandin Joelle erweitert. Schauen Sie sich ihre Updates [hier]({{< ref 2021-12-14-Estimating_Power_Plant_Greenhouse_Gas_Emissions_from_Satellite_Imagery  >}}) an.


# Bibliographie

* Mommert, M., Sigel, M., Neuhausler, M., Scheibenreif, L., Borth, D., "Characterization of Industrial Smoke Plumes from Remote Sensing Data", [Tackling Climate Change with Machine Learning Workshop,
NeurIPS 2020](https://www.climatechange.ai/papers/neurips2020/9). 

* Mommert, M. et al. 2020: [dataset](https://zenodo.org/record/4250706)

* Mommert, M. et al. 2020: [code](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection)


* Mommert, M., "Characterizing Industrial Smoke Plumes from Remote Sensing Data with Deep Learning", oral presentation at [NVIDIA GTC21](https://www.nvidia.com/en-us/gtc/). 
