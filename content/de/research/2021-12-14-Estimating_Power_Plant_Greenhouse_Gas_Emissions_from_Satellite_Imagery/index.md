---
date: 2021-12-14
title: Abschätzung von Treibhausgasemissionen von Kraftwerken aus Satellitenbildern
summary: |
  Die Überwachung von Treibhausgasemissionen wird in Zukunft zunehmend wichtig sein, da die Stromerzeugung aus fossilen Brennstoffen zurückgefahren werden soll. Für diese Aufgabe sind unabhängige Werkzeuge zur Überwachung von Kraftwerken erforderlich. Wir präsentieren eine Methode, die frei verfügbare Satellitenbilder nutzt, um die Stromerzeugung und die CO2-Emissionsraten auf globaler Ebene zu schätzen.
tags:
- Erdbeobachtung
- Deep Learning
- Multi-Task-Learning
- Kraftwerk
- CO2
- Sentinel-2
thumbnail_image: overview.png

---

Dieses Projekt bildet die logische Erweiterung unseres vorherigen Projekts zur [Charakterisierung industrieller Abgasfahrnen aus Fernerkundungsdaten]({{< ref "2021-12-14-Estimating_Power_Plant_Greenhouse_Gas_Emissions_from_Satellite_Imagery" >}}). Anstatt einfach nur Abgasfahnen zu identifizieren und zu charakterisieren, nutzen wir diese Informationen, um die Treibhausgasemissionen von fossilen Brennstoffkraftwerken zu schätzen.

Die Idee ist recht einfach: Wir wissen, dass wir Abgasfahnen segmentieren und sie robust von natürlichen Wolken unterscheiden können. Für alle europäischen Kraftwerke kennen wir zu jedem gegebenen Zeitpunkt ihre Stromerzeugungsraten. Daher können wir ein Regressionsmodell trainieren, um die Stromerzeugungsrate aus dem Umfang der beobachteten Abgasfahne abzuschätzen. Allerdings ist die scheinbare Größe der Rauchfahne nicht nur eine Funktion des Stromerzeugungsprozesses. Vielmehr handelt es sich um einen hochkomplexen Prozess, der von Umweltvariablen abhängt. Um diese Variablen zu approximieren, stellen wir unserem Regressionsmodell aktuelle Wetterinformationen zur Verfügung, einschließlich Umgebungstemperatur, Luftdruck und Windgeschwindigkeit.

{{< image
src="overview.png"
descr="Unsere Modellarchitektur. Satellitenbilder dienen als Eingabe für ein U-Net-Backbone. Die Ausgangsfeaturemap dient als Eingabe für einen Multi-Task-Learning-Ansatz: Wir verwenden separate Köpfe, um die Abgasfahne zu segmentieren, den Kraftwerkstyp zu klassifizieren und die Stromerzeugungsraten abzuschätzen. Letzteres berücksichtigt auch Wettervariablen. Die Architektur wird auf Ground-Truth-Abgasfahnenmasken, Informationen zum Kraftwerkstyp und Stromerzeugungsraten trainiert. Wir stellen fest, dass die Ergebnisse dieses Multi-Task-Learning-Ansatzes die Modelle übertreffen, die einzeln auf diesen Aufgaben  trainiert wurden." >}}

Um unsere Vorhersagen der Stromerzeugungsraten zu verbessern, nutzen wir einen Multi-Task-Learning-Ansatz: Anstatt einfach ein Modell zu trainieren, das die Stromerzeugung vorhersagt, lernen wir zusätzliche Aufgaben, nämlich ein Klassifikationsmodell für Kraftwerkstypen (siehe [hier]({{< ref "2021-06-16-Power_Plant_Classification_From_Remote_Imaging_With_Deep_Learning" >}})) und ein Segmentierungsmodell für Rauchfahnen (siehe [hier]({{< ref "2020-12-07-Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data" >}})). Durch das Lernen zusätzlicher Aufgaben generiert das Modell reichhaltigere Darstellungen der zugrunde liegenden Daten, was zu einem robusteren Training und einer besseren Leistung führt. Dies spiegelt sich in unseren Ergebnissen wider: Der kombinierte Multi-Task-Learning-Ansatz schneidet bei jeder gelernten Aufgabe besser ab als ein separat trainiertes Modell. Wir können auch zeigen, dass es von Vorteil ist, Wetterdaten in unsere Modelldaten einzubeziehen.

Bisher ist unser Modell in der Lage, die Stromerzeugungsraten (mit einem MAE von 139 MW) zu schätzen – wie erhalten wir CO2-Emissionsraten aus diesem Ergebnis? Unser Modell kann auch die Kraftwerkstypen identifizieren; je nach verwendetem Brennstoff stoßen sie unterschiedliche Mengen CO2 pro MWh in die Atmosphäre aus. Durch die Annäherung dieser Emissionsfaktoren sind wir in der Lage, unsere Schätzungen der Stromerzeugungsraten in Schätzungen der Emissionsraten umzuwandeln.


{{< image
src="results.png"
descr="Vorhersageergebnisse aus unserem Multi-Task-Learning-Ansatz: Stromerzeugungsraten links und CO2-Emissionsraten rechts." >}}

Unser Ansatz ermöglicht die Schätzung der Stromerzeugungsraten und CO2-Emissionsraten von Kraftwerken basierend auf frei verfügbaren Sentinel-2-Satellitenbildern. Die Ergebnisse wurden auf dem Workshop [Tackling Climate Change with Machine Learning bei NeurIPS 2021](https://www.climatechange.ai/papers/neurips2021/27) und in der Zeitschrift IEEE Transactions on Geoscience and Remote Sensing (siehe unten)  veröffentlicht.


# Bibliographie

* Joelle Hanna, Damian Borth, Michael Mommert, "*Physics-Guided Multitask Learning for Estimating Power Generation and CO2 Emissions from Satellite Imagery*", IEEE Transactions on Geoscience and Remote Sensing, [publication](https://ieeexplore.ieee.org/iel7/36/4358825/10153694.pdf), 2023.

* Hanna, J., Mommert, M., Scheibenreif, L. Borth, D., "Multitask Learning for Estimating Power Plant Greenhouse Gas Emissions from Satellite Imagery", NeurIPS 2021 Tackling Climate Change with Machine Learning Workshop; [publication (open access)](https://www.climatechange.ai/papers/neurips2021/27).

* Hanna J. et al. 2021, [code](https://github.com/HSG-AIML/RemoteSensingCO2Estimation)

* Hanna J. et al. 2021, [dataset](https://doi.org/10.5281/zenodo.5644746)

