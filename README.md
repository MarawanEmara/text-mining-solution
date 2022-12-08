# text-mining-solution

### Ergebnisaufbereitung
![min_bounty](https://github.com/MarawanEmara/text-mining-solution/blobmain/min_bounty.png?raw=true)
![max_bounty](https://github.com/MarawanEmara/text-mining-solution/blobmain/max_bounty.png?raw=true)

### Planung weiterer Schritte

Wir könnten neue Funktionen einführen, um die .csv-Liste in Abhängigkeit von Schlüsselwörtern aufzuteilen. Ausschließende Schlüsselwörter wären solche, die auf bestimmte unerwünschte Merkmale hinweisen. Wenn ein solches Schlüsselwort beim Durchgehen der Programmliste entdeckt wird, könnten wir es aus der Liste entfernen und einer neuen Liste hinzufügen. Alternativ könnten wir eine Spalte in der Liste erstellen, die angibt, welche Programme ein- oder ausgeschlossen werden sollen.

### Zusätzlicher Kommentar

Dies war eine äußerst interessante Herausforderung, da ich noch nie Web-Scraping gemacht habe. Nichtsdestotrotz habe ich versucht, so viel wie möglich mit der Zeit, die ich heute (08.12.) habe, umzusetzen. Wenn ich darüber nachdenke, hätte ich diese Herausforderung auch anders angehen können, z. B. indem ich versucht hätte, asynchrone Methoden zu implementieren, anstatt einfache synchrone Methoden zu verwenden, um die Details zu erhalten. Das könnte zusammen mit den Multiprozessing-Fähigkeiten von Python die Zeiten für die Verarbeitung dieser Informationen beschleunigen. Ich möchte auch hinzufügen, dass meine Datenextraktionsmethoden definitiv nicht großartig sind, da sie einige der Informationen, die benötigt werden könnten, nicht erfassen, wie zum Beispiel die Belohnungselemente, die als Kinder von "scope and rewards" eingebettet sind. Das hätte die Gesamtheit der verfügbaren Daten definitiv verbessert.
