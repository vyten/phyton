# DFT – Distans Fart Tid

Räknar ut distans, fart eller tid till sjöss i terminalen. Du väljer vad du vill räkna ut, skriver in de två andra värdena och får svaret direkt.

Det här är fjärde versionen av programmet. De tidigare är skrivna i VB6, C# (Windows Forms) och PHP (webbsida med TinyMVC).

## Formler

Tiden räknas i minuter, därav 60.

| Räkna ut | Formel | Enhet |
|---|---|---|
| Distans | (Fart × Tid) / 60 | M (distansminuter) |
| Fart | (Distans / Tid) × 60 | knop |
| Tid | (Distans / Fart) × 60 | h och minuter |

## Kör

```bash
cd dft
python3 dft.py
```

Första gången väljer du språk: 1 = Svenska, 2 = English, 3 = český. Språket sparas i `dft_lang.txt` bredvid skriptet, och nästa gång kommer du direkt till menyn. I menyn väljer du 1 = Distans, 2 = Fart, 3 = Tid, 4 = Byt språk eller 0 = Avsluta. När du byter språk står det nuvarande inom hakparenteser, till exempel `[2]`, och Enter behåller det. Decimaltal kan skrivas med punkt eller komma, till exempel `5.5` eller `5,5`. Ctrl+C avslutar också.

Felaktig inmatning loggas till `dft.log` i samma katalog som skriptet. Namnet ändras i konstanten `LOG_FILE_NAME` i `dft.py`.

## Filer

| Fil | Innehåll |
|---|---|
| `dft.py` | Huvudskriptet: meny, inmatning och utskrift |
| `dft_functions.py` | Uträkningarna: `calculate_distance()`, `calculate_speed()`, `calculate_time()` och hjälpfunktionerna `to_minutes()` och `to_hours_and_minutes()` |
| `terminal_colors.py` | Färger i terminalen, kopia av `learning_python/terminal_colors.py` |
| `lang_se.py` | Svenska texter |
| `lang_en.py` | Engelska texter |
| `lang_cz.py` | Tjeckiska texter (rader märkta TODO är fortfarande på svenska) |

Kör `python3 dft_functions.py` för att se några provuträkningar.
