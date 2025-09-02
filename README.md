# Szyfr Cezara

Ten projekt to implementacja algorytmu szyfru Cezara w języku Python. Program umożliwia szyfrowanie i deszyfrowanie tekstu za pomocą podanego klucza, a także kryptoanalizę, czyli łamanie szyfru bez znajomości klucza, bazując na analizie częstotliwości liter. Jest to idealny projekt do nauki podstawowych operacji kryptograficznych i analizy tekstu.

### Główne funkcjonalności

* **Szyfrowanie**: Szyfruje tekst z pliku `plain.txt` za pomocą klucza (przesunięcia) i zapisuje wynik w `crypto.txt`.
* **Deszyfrowanie**: Deszyfruje tekst z pliku `crypto.txt` za pomocą klucza i zapisuje wynik w `decrypt.txt`.
* **Kryptoanaliza**: Próbuje znaleźć klucz i odszyfrować tekst z pliku `crypto.txt` bez znajomości klucza. Złamanie szyfru opiera się na analizie częstotliwości liter, co jest jedną z najprostszych metod kryptoanalizy. Odnaleziony klucz jest zapisywany w `key-found.txt`, a odszyfrowany tekst w `decrypt.txt`.
* **Przygotowanie tekstu**: Przygotowuje tekst jawny, usuwając znaki inne niż litery i zmieniając wielkość liter na małe, a następnie zapisuje go w `plain.txt`.

### Użycie z linii komend

Program uruchamia się z jednym z następujących argumentów:

* `-p`: Przygotowanie tekstu jawnego.
* `-e <klucz>`: Szyfrowanie tekstu za pomocą podanego klucza (liczba od 1 do 25).
* `-d <klucz>`: Deszyfrowanie tekstu za pomocą podanego klucza (liczba od 1 do 25).
* `-k`: Kryptoanaliza.

**Przykłady użycia:**
`python caesar-cipher.py -e 3`
`python caesar-cipher.py -k`

### Pliki

* `orig.txt`: Plik z oryginalnym tekstem jawnym (używany z opcją `-p`).
* `plain.txt`: Plik z przygotowanym tekstem jawnym.
* `crypto.txt`: Plik z zaszyfrowanym tekstem.
* `decrypt.txt`: Plik z odszyfrowanym tekstem.
* `key-found.txt`: Plik z kluczem znalezionym przez kryptoanalizę.
