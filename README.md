# Multiplikationstabellen

Mitt första Python-skript: ett litet program för att öva på multiplikationstabellen i terminalen.

Du väljer vilken tabell du vill öva på och mellan vilka tal (start och stopp). Programmet ställer en fråga i taget, rättar svaret direkt och visar på slutet hur många du hade rätt.

## Kör

```bash
cd learning_python
python3 urban.py
```

Felaktig inmatning loggas till `PythonLogException.log` i samma katalog som skriptet. Namnet ändras i variabeln `log_file_name` i `urban.py`.

## Filer

| Fil | Innehåll |
|---|---|
| `learning_python/urban.py` | Huvudskriptet: välkomsttext, inmatning, frågeloop och resultat |
| `learning_python/urban_functions.py` | Funktionerna `check_integer()` och `result()`: kontroll av heltal och rättning |
| `template.py` | Mall för header och sektioner i nya skript |

## Fler program

- [DFT – Distans Fart Tid](dft/README.md): räknar ut distans, fart eller tid till sjöss.

## Utvärdering

Synpunkter från en kodgranskning av skriptet.

### Övergripande

- **Koden är uppdelad i två filer.** Logiken ligger i `urban_functions.py` och flödet i `urban.py`, och du importerar din egen modul. Det är rätt tänkt.
- **Skriptet är dokumenterat** med header, syfte och historik.

### urban.py

- **Användaren får vänliga meddelanden:** en välkomsttext med exempel, rättning efter varje svar och en sammanfattning på slutet.
- **Felen loggas** till fil med tidsstämpel och nivå, och nivån är satt till `ERROR` så att det inte blir onödigt brus.

### urban_functions.py

- **Inmatningen kontrolleras.** `check_integer()` fångar felaktig inmatning i stället för att krascha. Du använder dessutom `try/except/else`, där `else` körs bara när inget fel uppstod. Det är en del av Python som många inte känner till ens efter flera år.
