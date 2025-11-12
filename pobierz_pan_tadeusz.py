"""Pobiera tekst "Pan Tadeusz" z Wolnych Lektur.

Uruchom skrypt poleceniem:
    python pobierz_pan_tadeusz.py

Plik zostanie zapisany w bieżącym katalogu jako "pan-tadeusz.txt".
"""

from pathlib import Path
from urllib.request import urlretrieve

URL = "https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt"
OUTPUT = Path("pan-tadeusz.txt")


def main() -> None:
    """Pobierz plik z utworem i zapisz go lokalnie."""
    print(f"Pobieram plik z {URL}...")
    urlretrieve(URL, OUTPUT)
    print(f"Zapisano jako {OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
