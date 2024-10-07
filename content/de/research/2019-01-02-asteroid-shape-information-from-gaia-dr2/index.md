---
date: 2019-01-02
title: Informationen über die Form von Asteroiden aus Gaia DR2
summary: |
  Die Gaia-Mission erstellt eine einzigartige Erhebung der Sterne in unserer Milchstraße – sie beobachtet jedoch auch Asteroiden, die ihr Sichtfeld durchqueren. Wir leiten Informationen über die Formverteilungen verschiedener Asteroidpopulationen aus der ersten Charge von Asteroidendaten von Gaia ab.
tags:
- Astronomie
- Asteroid
- Physikalische Eigenschaften von Asteroiden
- Gaia
featured_image: /research/12893.png
thumbnail_image: gaia.png
---

Die ESA-Mission [Gaia](http://sci.esa.int/gaia/)Gaia beobachtet nicht nur einen großen Teil der Sterne in der Milchstraße, sondern auch eine enorme Anzahl von Asteroiden. Der Gaia-Datenrelease 2 (DR2) ist der erste Datenrelease, der eine Reihe von Asteroidbeobachtungen enthält, beschränkt auf G-Helligkeiten (ohne Farbinformationen) und eine vorab ausgewählte Stichprobe von 14.099 Asteroiden aus verschiedenen Populationen. Für jeden Asteroiden enthält DR2 eine mediane Anzahl von 9 Beobachtungen über die ersten 9 Monate der Mission. Während dieser begrenzte Datensatz nicht zulässt, die Rotationsperioden der Ziele abzuleiten oder ihre taxonomischen Typen einzugrenzen, ist er nützlich, um einen Blick auf die Formverteilung der Asteroiden zu werfen.

In dieser Studie haben wir untere Grenzwerte für die Lichtkurvenamplituden aller Hauptgürtel-Asteroiden in der DR2-Stichprobe extrahiert, um die Formverteilung der Population zu untersuchen und sie mit anderen Populationen zu vergleichen.

Um die unteren Grenzwerte für die Lichtkurvenamplituden abzuleiten, subtrahierten wir erwartete Helligkeitsvariationen aufgrund des sich ändernden Sonnenphasenwinkels basierend auf Literaturdaten. Die Amplituden (Peak-to-Peak) wurden dann aus der resultierenden Streuung der berichteten Helligkeiten abgeleitet. Diese Amplituden stellen aufgrund der unvollständigen Abdeckung der Lichtkurven nur untere Grenzwerte dar. Für jedes Hauptgürtelobjekt übersetzen wir diese Lichtkurvenamplitude in ein Seitenverhältnis, wobei wir ein triaxiales ellipsoides Formmodell annehmen. Das folgende Diagramm (Abbildung 2 im Paper) zeigt die Verteilung dieser Seitenverhältnisse in Abhängigkeit von anderen Ziel-Eigenschaften:

{{< image
src="gaia.png"
descr="Seitenverhältnisse für verschiedene Ziel-Eigenschaften (Panels) und verschiedene Asteroidpopulationen (farbige Balken)." >}}


Während eine signifikante Variation in den Verteilungen über verschiedene Teilsamples (getrennt durch gestrichelte vertikale Linien) offensichtlich ist, unterscheiden sich die korrigierten (debiased) Durchschnitte (farbige Symbole) nur geringfügig in Bezug auf ihre Fehlerbalken. Das Debiasing wurde mithilfe einer Monte-Carlo-Simulation erreicht, die Mängel im Sampling-Prozess und in der Genauigkeit der aus der Literatur entnommenen photometrischen Phasenparameter berücksichtigt.

Der signifikanteste Effekt in beiden gemessenen und debiased Formverteilungen wird in Abhängigkeit von der Größe beobachtet: Die DR2-Daten zeigen, dass große Hauptgürtel-Asteroiden dazu neigen, runder zu sein als kleinere Hauptgürtel-Asteroiden, was das Ergebnis ist, dass größere und massereichere Körper stärker von der Selbstgravitation betroffen sind.

Während die gemessenen Formverteilungen klare Variationen für verschiedene Teilsamples zeigen (z. B. in Abhängigkeit von der großen Halbachse), schränkt die kleine Stichprobengröße das Vertrauen in irgendwelche Schlussfolgerungen strikt ein. Diese Studie zeigt jedoch eindeutig, dass zukünftige Gaia-Datenfreigaben für kleine Körper (die hoffentlich viele weitere photometrische Datenpunkte für viele weitere Asteroiden enthalten werden) einen Schatz für Studien wie die hier präsentierte bieten werden.

# Bibliographie

* Mommert, M., McNeill, A., Trilling, D. E., Moskovitz, N., Delbo', M. (2018), "*The Main Belt Asteroid Shape Distribution from Gaia Data Release 2*", The Astronomical Journal, 156, 139., [publication](http://doi.org/10.3847/1538-3881/aad338), [arxiv](http://arxiv.org/abs/1808.08988)
