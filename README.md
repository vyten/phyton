# Multiplikationstabellen

Mitt första Python-skript: ett litet program för att öva på multiplikationstabellen i terminalen.

Du väljer vilken tabell du vill öva på och mellan vilka tal (start och stopp). Programmet ställer en fråga i taget, rättar svaret direkt och visar på slutet hur många du hade rätt.

## Kör

```bash
cd learning_python
python3 urban.py
```

Felaktig inmatning loggas till `PhytonLogExeption.log` i katalogen där skriptet körs.

## Filer

| Fil | Innehåll |
|---|---|
| `learning_python/urban.py` | Huvudskriptet: välkomsttext, inmatning, frågeloop och resultat |
| `learning_python/urbanClasses.py` | Klassen `Calculate`: kontroll av heltal, rättning och räknare |
| `template.py` | Mall för header och sektioner i nya skript |

## Utvärdering

Synpunkter från en kodgranskning av skriptet.

### Övergripande

- **Koden är uppdelad i två filer.** Logiken ligger i `urbanClasses.py` och flödet i `urban.py`, och du importerar din egen modul. Det är rätt tänkt.
- **Skriptet är dokumenterat** med header, syfte och historik.

### urban.py

- **Användaren får vänliga meddelanden:** en välkomsttext med exempel, rättning efter varje svar och en sammanfattning på slutet.
- **Felen loggas** till fil med tidsstämpel och nivå, och nivån är satt till `ERROR` så att det inte blir onödigt brus.

### urbanClasses.py

- **Inmatningen kontrolleras.** `checkInteger()` fångar felaktig inmatning i stället för att krascha. Du använder dessutom `try/except/else`, där `else` körs bara när inget fel uppstod. Det är en del av Python som många inte känner till ens efter flera år.
