---
date: 2024-07-12
title: Multimodale Diffusion für selbstüberwachtes Vortraining
summary: |
  Deep-Learning-Modelle, die auf Diffusionsprozessen basieren, zeigen ein großes Potenzial in einer Vielzahl von generativen Aufgaben, wie z.B. der Bildgenerierung. Für Anwendungen in der Fernerkundung sind generative Modelle jedoch nicht so verbreitet. Die Frage, die wir zu beantworten versucht haben, ist, ob Diffusionsprozesse verwendet werden können, um Modelle für diskriminative Aufgaben effizient vorzutrainieren?
tags:
- Erdbeobachtung
- Deep Learning
- Diffusion
- Multimodal
- Selbstüberwachtes Lernen
thumbnail_image: diffusion_qualitative_sample.png
---

Diffusionsprozesse sind am besten dafür bekannt, Modelle zu trainieren, die Bilder aus Text generieren. Die Idee hinter Diffusionsprozessen ist recht einfach: Man nimmt ein Bild und zerstört die Informationen schrittweise, indem man Gaußsches Rauschen anwendet. Ein Diffusionsmodell lernt nun, die ursprünglichen Informationen zwischen zwei Schritten wiederherzustellen (d.h. das Rauschen zu entfernen). Vollständig trainiert sind diese Modelle dazu in der Lage, fotorealistische Bilder aus Rauschen zu erzeugen.

Um ein Bild aus Text zu erstellen, muss der Diffusionsprozess mit einem Textprompt konditioniert werden. Dies ist eine Möglichkeit, zusätzliche Informationen bereitzustellen, um den generativen Prozess zu steuern.

Während generative Modelle in der Erdbeobachtung nicht so verbreitet sind, fragten wir uns, ob wir einen Diffusionsprozess nutzen könnten, um unsere Modelle auf selbstüberwachter Basis vorzutrainieren.

Dazu haben wir ein Diffusionsmodell auf unserem [ben-ge Datensatz]({{< ref "2023-07-21-Ben-Ge_Extending_Bigearthnet_with_Geographical_and_Environmental_Data" >}}) trainiert. Wir geben Sentinel-1- und Sentinel-2-Rasterdaten als verschiedene Bänder in das Modell ein und experimentieren mit anderen Datenmodalitäten als Eingabe für den Konditionierungsmechanismus.

Hat es funktioniert?

{{< image
src="diffusion_qualitative_sample.png"
descr="Synthetische Bilder, die mit unserer Methode generiert wurden. Die Spalten zeigen synthetisch erzeugte Datenmodalitäten zu verschiedenen Zeitpunkten (von oben nach unten) des Diffusionsprozesses. Im letzten Zeitpunkt entstehen realistische und konsistente Szenen (über die Datenmodalitäten hinweg) aus dem Rauschen." >}}

Wie die obige Abbildung zeigt, ist das Modell dazu in der Lage, realistisch aussehende Sentinel-2-Szenen zu generieren. Noch wichtiger ist jedoch, dass die Sentinel-1 SAR-Daten, die es für dasselbe Bild  generiert, sehr konsistent mit den Sentinel-2-Daten sind. Dadurch glauben wir, dass das Modell nützliche Informationen lernt. Aber sind die gelernten Repräsentationen nützlich für darauf folgende diskriminative Aufgaben wie die Klassifizierung und Segmentierung von Landnutzung/Landbedeckung?

Die Antwort scheint klar: Das Vortraining mit Diffusion funktioniert gut für die Segmentierungsaufgabe, jedoch nicht so sehr für die Klassifizierungsaufgaben. Darüber hinaus scheint die Konditionierung des Modells die Ergebnisse zu verbessern.

Weitere Details gibt es in unserem Beitrag zu IGARSS 2024 (siehe unten).

# Bibliographie

* Alexander Lontke, Michael Mommert, Damian Borth, "*Multi-Modal Diffusion for Self-Supervised Pretraining*", [IEEE International Geoscience and Remote Sensing Symposium 2024](https://ieeexplore.ieee.org/abstract/document/10640509), 2024.
