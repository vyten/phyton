# common

Kod som delas av flera program i repot. Filerna är fristående och kan också kopieras till andra projekt.

## Filer

| Fil | Innehåll | Används av |
|---|---|---|
| `terminal_colors.py` | Färger i terminalen, samma koder som i bash | `learning_python/urban.py`, `learning_python/urban_functions.py`, `dft/dft.py` |
| `__init__.py` | Tom fil som talar om för Python att katalogen är ett paket | – |

Kör `python3 terminal_colors.py` för att se alla färger.

## Använda i ett program

Python letar bara efter moduler i skriptets egen katalog. Därför behöver programmet tala om var roten på repot ligger innan det importerar från `common/`:

```python
import sys
from os import path
# the root directory of the repo, so that common/ can be found
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), '..'))
from common.terminal_colors import COL_YELLOW_BLUE, COL_STANDARD
```

Raden fungerar för program som ligger en katalog ner från roten, till exempel `dft/` och `learning_python/`.

När en ny fil läggs till eller ett nytt program börjar använda en fil uppdateras tabellen ovan. Med `grep -r terminal_colors --include=*.py` syns vilka program som använder den.
