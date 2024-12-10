# ASCII Art Converter

## Popis projektu

Tento program převádí obrázky do ASCII artu, což je textová reprezentace obrázku pomocí ASCII znaků. ASCII art umožňuje zobrazit obrázek v textovém formátu, přičemž tmavší znaky reprezentují intenzivnější pixely.

### Klíčové funkce:
1. **Změna velikosti obrázku** při zachování poměru stran.
2. **Převod obrázku na odstíny šedi** pro snazší práci s intenzitou pixelů.
3. **Mapování pixelů na ASCII znaky** podle úrovně jejich intenzity.
4. **Generování ASCII artu** jako textového výstupu.
5. **Uložení výsledného ASCII artu** do textového souboru `ascii_art.txt`.

---

## Jak program používat

### Požadavky
1. **Python 3.x**:
   - Ujistěte se, že máte Python nainstalován. Stáhněte jej z [oficiálních stránek Pythonu](https://www.python.org/).
2. **Knihovna Pillow**:
   - Pillow je potřeba pro práci s obrázky. Nainstalujte ji příkazem:
     ```bash
     pip install pillow
     ```

### Použití programu

1. **Spuštění programu**:
   - Otevřete terminál a přejděte do složky, kde máte soubor uložený.
   - Spusťte skript příkazem:
     ```bash
     python main.py
     ```
2. **Interakce s programem**:
   - Po spuštění budete vyzváni k zadání cesty k obrázku.
   - Následně zadejte šířku ASCII artu v textu (např. 100):

3. **Výstup programu**:
   - ASCII art se zobrazí přímo v terminálu.
   - ASCII art bude také uložen do souboru `ascii_art.txt` ve stejné složce, kde je program uložen.



