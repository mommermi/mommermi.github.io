---
date: 2021-11-18
title: Bestimmung von NO2-Konzentrationen an der Erdoberfläche aus Fernerkundungsdaten
summary: |
  Luftverschmutzung ist ein großes Gesundheitsproblem und trägt in den meisten Fällen auch zum Klimawandel bei. Die Messung der Luftverschmutzung ist kostspielig und daher nur in einigen Ländern verfügbar. Wir haben untersucht, ob frei verfügbare Erdbeobachtungsdaten genutzt werden können, um die Luftverschmutzung an der Erdoberfläche zu abschätzen.
tags:
- Erdbeobachtung
- Deep Learning
- Luftverschmutzung
- NO2
- Sentinel-2
thumbnail_image: figure2.png

---

Luftverschmutzung hat nachweislich negative Auswirkungen auf die Gesundheit. Ein bedeutendes Luftschadstoff ist NO2, das auf der Erdoberfläche direkt die menschliche Gesundheit beeinflusst und in höheren Lagen zur Bildung von saurem Regen beiträgt und als Vorläufer von Treibhausgasen fungiert. Während die NO2-Säulendichten in der Atmosphäre mit Satellitenbeobachtungen, wie sie von Sentinel-5P bereitgestellt werden, gemessen werden können, sind In-situ-Messungen von Bodenstationen erforderlich, um die NO2-Konzentrationen auf der Oberfläche zu messen, die für die menschliche Exposition relevant sind.

Unser Student Linus Scheibenreif untersuchte, ob es möglich wäre, das NO2-Niveau an der Oberfläche ausschließlich aus Fernerkundungsbeobachtungen zu approximieren, um ein damit abschätzen zu können wieviel NO2 Menschen ausgesetzt sind. In seinen beiden Veröffentlichungen zeigte Linus, dass

* es möglich ist, die Exposition gegenüber NO2 auf der Oberfläche basierend auf Messungen der EEA Bodenstationen anhand verschiedener Merkmale zu interpolieren (Scheibenreif et al. 2021a), und
* wir können Satellitenbilder mit Messungen der Säulendichte von atmosphärischen Spurengasen kombinieren, um die NO2-Konzentrationen auf der Oberfläche mit hoher räumlicher Auflösung und mittlerer zeitlicher Auflösung zu schätzen (Scheibenreif et al. 2021b).

{{<  image
src="figure2.png"
descr="Beispielhafte NO2-Vorhersagen basierend auf Sentinel-2- und Sentinel-5P-Eingabedaten aus Scheibenreif et al. 2021b." >}}

Erfahren Sie mehr über Linus' Projekte in diesen Blogartikeln (english): [A Novel Dataset for the Prediction of Surface NO2 Concentrations from Remote Sensing Data](https://hsg-aiml.github.io/2021/04/07/A_Novel_Dataset_for_the_Estimation_of_Surface_NO2_Concentrations_from_Remote_Sensing_Data.html) und [Estimation of Air Pollution with Remote Sensing Data: Revealing Greenhouse Gas Emissions from Space](https://hsg-aiml.github.io/2021/07/23/Estimation_of_Air_Pollution_with_Remote_Sensing_Data.html). 
Seine Ergebnisse wurden auch in einem Artikel der IEEE Transactions on Geoscience and Remote Sensing zusammengefasst (siehe unten).


# Bibliographie

* Scheibenreif, L., Mommert, M., Borth, D., "Towards Global Estimation of Ground-Level NO2 Pollution with Deep Learning and Remote Sensing", IEEE Transactions on Geoscience and Remote Sensing, 2022, [publication](https://doi.org/10.1109/TGRS.2022.3160827), [open access](http://www.alexandria.unisg.ch/266586/1/Toward_Global_Estimation_of_Ground-Level_NO2_Pollution_With_Deep_Learning_and_Remote_Sensing.pdf).

* Scheibenreif et al. 2022 Dataset: [zenodo](https://doi.org/10.5281/zenodo.5764262)

* Scheibenreif et al. 2022 Code: [GitHub](https://github.com/HSG-AIML/Global-NO2-Estimation)

* Scheibenreif, L, Mommert, M., Borth, D., "Estimation of Air Pollution with Remote Sensing Data: Revealing Greenhouse Gas Emissions from Space", ICML 2021 Tackling Climate Change with Machine Learning Workshop;
[publication (open access)](https://www.climatechange.ai/papers/icml2021/23).

* Scheibenreif, L. , Mommert, M., Borth, D., "A Novel Dataset and Benchmark for Surface NO2 Prediction from Remote Sensing Data Including COVID Lockdown Measures", IEEE International Geoscience and Remote Sensing Symposium 2021 ([IGARSS 2021](https://igarss2021.com/)); [publication](https://ieeexplore.ieee.org/iel7/9553015/9553016/09554037.pdf).
