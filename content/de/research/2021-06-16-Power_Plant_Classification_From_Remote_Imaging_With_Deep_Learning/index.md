---
date: 2021-06-16
title: Klassifizierung von Kraftwerken aus Satellitenbildern mit Deep Learning
summary: |
  Wir haben ein Deep-Learning-Modell entwickelt, das in der Lage ist, zwischen 10 verschiedenen Arten von Kraftwerken zu unterscheiden. Die Ziel ist es unterchiedliche industrielle Standorte in Satellitenbildern automatisch zu identifizieren und zu charakterisieren. Diese Arbeit wird uns in Zukunft helfen, die Treibhausgasemissionsraten für einzelne Industrieanlagen zu schätzen.
tags:
- Erdbeobachtung
- Deep Learning
- Klassifizierung
- Kraftwerk
- Sentinel-2
thumbnail_image: example_activations.png
---


Die industriellen und energieerzeugenden Wirtschaftssektoren stoßen mehr als die Hälfte der jährlich und global freigesetzten Treibhausgasemissionen aus und tragen somit erheblich zu den globalen Erwärmungseffekten bei. In unserer jüngsten Arbeit ([Mommert et al. 2020]({{< ref "2021-06-16-Power_Plant_Classification_From_Remote_Imaging_With_Deep_Learning" >}})) haben wir die Grundlage für die Schätzung von Treibhausgasemissionen aus Industrieanlagen gelegt, indem wir industrielle Rauchfahnen ausschließlich aus Daten der Fernbildgebung charakterisiert haben. Diese Arbeit ist Teil eines größeren Vorhabens zur Schätzung der Treibhausgasemissionsraten aus Satellitenbildern für einzelne Industrieanlagen. In dieser Arbeit haben wir einen weiteren Schritt in Richtung dieses Ziels gemacht.

Verschiedene Industrieanlagen tragen sehr unterschiedlich zu den Emissionsinventaren bei. Beispielsweise produzieren leichte Industrieanlagen typischerweise weniger Treibhausgasemissionen als kohlebetriebene Kraftwerke. Es ist ratsam, die Art der Industrieanlagen zu berücksichtigen, wenn man versucht, ihr Emissionsbudget zu schätzen.

In dieser Arbeit untersuchen wir die Möglichkeit, verschiedene Arten von Kraftwerken aus Sentinel-2-Satellitenbildern zu identifizieren. Wir unterscheiden zwischen 10 verschiedenen Kraftwerkstypen: fossil befeuerte Kraftwerke, die Braunkohle, Gas oder Steinkohle nutzen, Kernkraftwerke und Kraftwerke, die regenerative Energiequellen nutzen, darunter Wasser (Laufwasserkraftwerke, Speicher- und Pumpspeicherkraftwerke), Solar- und Windenergie.

{{< image
src="example_activations.png"
descr="Beispielbilder und Klassenaktivierungskarten für zwei Kohlekraftwerke aus unserer Stichprobe, die korrekt identifiziert wurden. Die Heatmap-Diagramme heben die Bereiche hervor, auf denen das trainierte Modell seine Klassenvorhersage stützt. In diesem Fall konzentriert sich das Modell auf das Vorhandensein von Kohlehaufen, die tatsächlich ein Indikator für kohlebetriebene Kraftwerke sind." >}}

Mit einem ResNet-50-Modell sind wir in der Lage, eine durchschnittliche Genauigkeit von 90,0% bei der Unterscheidung von 10 verschiedenen Kraftwerkstypen und einer Hintergrundklasse, die zufällige Satellitenbildausschnitte enthält, zu erreichen. Wir stellen auch fest, dass wir die Kühlmechanismen, die in thermischen Kraftwerken verwendet werden, mit einer durchschnittlichen Genauigkeit von 87,5% identifizieren können. Eine Konfusionsmatrix (siehe unten) zeigt die Einschränkungen unseres Ansatzes: Der Grad der Verwirrung ist am höchsten bei Kraftwerken, die ähnliche Energiequellen nutzen (z. B. Wasserkraftwerke) oder sich in ähnlichen geografischen Umgebungen befinden. Dieses Manko kann wahrscheinlich mit einem größeren Trainingsdatensatz behoben werden – diese Studie basiert auf 4.154 Bildern von 450 verschiedenen Kraftwerken, die in 10 verschiedene Kraftwerkstypen gruppiert sind. Schließlich nutzen wir Klassenaktivierungskarten, um die Interpretierbarkeit unserer Ergebnisse zu verbessern, und stellen fest, dass unser trainiertes Modell von einzigartigen Merkmalen der verschiedenen Kraftwerkstypen profitiert: Öltanks, Kohlehaufen, Windturbinen oder Dämme.

{{< image
src="confusion_matrix_11classes_mod.png"
descr="Konfusionsmatrix für die Klassifizierung von Kraftwerkstypen. Verwirrung ist möglich zwischen Anlagen, die ähnliche Energiequellen nutzen, wie z. B. Wasserkraftwerke." >}}

Unsere Ergebnisse ermöglichen es uns, den Energiemix qualitativ aus Sentinel-2-Bilddaten zu untersuchen und beweisen die Machbarkeit, industrielle Standorte weltweit aus frei verfügbaren Satellitenbildern zu klassifizieren. Motiviert durch den Erfolg dieser Arbeit werden wir sie in Zukunft erweitern, um eine vielfältigere Gruppe von Industrieanlagen zu klassifizieren. Neben sozioökonomischen Anwendungen wird uns ein solcher Klassifikator helfen, die Treibhausgasemissionen für jeden Industriestandort auf der Erde aus Daten der Fernbildgebung zu schätzen.

Dieser Arbeit wurde beim [IEEE International Geoscience and
Remote Sensing Symposion (IGARSS) 2021](https://igarss2021.com/) vorgestellt.

# Bibliographie

* Mommert, M., Scheibenreif, L., Hanna, J., Borth, D., "Power Plant Classification from Remote Imaging With Deep Learning", IEEE International Geoscience and Remote Sensing Symposium 2021 ([IGARSS 2021](https://igarss2021.com/)); [publication](https://ieeexplore.ieee.org/iel7/9553015/9553016/09553219.pdf), [arxiv](https://arxiv.org/abs/2107.10894).
