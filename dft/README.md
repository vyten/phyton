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

## Utvärdering

Synpunkter från en kodgranskning av programmet.

### Övergripande

- **Uträkningarna är skilda från användargränssnittet.** `dft_functions.py` räknar bara och skriver aldrig ut något, och `dft.py` sköter frågor och svar. Därför kan ett GUI senare använda samma funktioner utan ändringar.
- **Funktionerna är små och gör en sak var.** `to_minutes()` och `to_hours_and_minutes()` används av de andra i stället för att samma uträkning upprepas.
- **Felet med 60 minuter från C#-versionen är borta.** `divmod(round(...), 60)` ger alltid minuter mellan 0 och 59.

### dft.py

- **Inmatningen tål både punkt och komma** som decimaltecken, och negativa tal stoppas. `nan` och `inf`, som `float()` också godtar, stoppas med `math.isfinite()`.
- **Division med noll fångas** innan uträkningen, med ett eget felmeddelande för tid 0 och fart 0.
- **Ctrl+C och Ctrl+D avslutar lugnt** med hej då på valt språk, i stället för en lång Python-felutskrift.
- **Språken ligger i en tabell** (`LANGUAGES`). Ett nytt språk kräver bara en ny språkfil och en rad.
- **Språket sparas** i `dft_lang.txt`, och en trasig eller saknad fil leder till språkvalet i stället för en krasch.

### Språkfilerna

- **Alla tre filerna har samma nycklar**, och tal formateras i själva texten (`{distance:.1f}`), så varje språk kan placera talet där det passar.

### Att förbättra

- **`terminal_colors.py` finns i två kopior**, här och i `learning_python/`. Ändras den ena måste den andra ändras för hand.
- **Provuträkningarna i `dft_functions.py` skrivs bara ut** och måste läsas av med ögonen. Med `assert` eller modulen `unittest` kontrollerar Python själv att svaren stämmer.
- **Distansenheten skiljer sig mellan språken:** `M` på svenska och `nm` på engelska och tjeckiska.
- **Nio rader i `lang_cz.py` är fortfarande på svenska** och väntar på översättning.
