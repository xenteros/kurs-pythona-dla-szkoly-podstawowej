# Lista zadań – rozumienie kodu + wyszukiwanie informacji

## Założenia
- Zadania są krótkie i proste.
- Priorytet: **czytanie i rozumienie gotowego kodu**.
- Dopuszczalne: uzupełnianie pojedynczych luk (`___`) albo jednej linijki.
- Część zadań wymaga **sprawdzenia informacji w internecie** i podania źródła.

---

## A. Rozumienie kodu (bez pisania od zera)

1. Przeczytaj kod:
   ```python
   x = 3
   y = 5
   print(x + y)
   ```
   Zaznacz poprawną odpowiedź: co zostanie wypisane?

2. Przeczytaj kod:
   ```python
   imie = "Ola"
   print("Cześć,", imie)
   ```
   Napisz dokładnie, jaki tekst pojawi się w konsoli.

3. W kodzie:
   ```python
   a = 10
   a = a + 2
   print(a)
   ```
   wyjaśnij, co robi druga linijka.

4. Kod:
   ```python
   for i in range(3):
       print(i)
   ```
   Uzupełnij: pętla wykona się `___` razy.

5. Kod:
   ```python
   for i in range(1, 4):
       print(i)
   ```
   Wypisz wszystkie liczby, które pojawią się na ekranie.

6. Kod:
   ```python
   liczby = [2, 4, 6]
   print(liczby[0])
   ```
   Odpowiedz: dlaczego wypisze się pierwsza liczba z listy?

7. Kod:
   ```python
   liczby = [2, 4, 6]
   print(len(liczby))
   ```
   Co robi funkcja `len`?

8. Kod:
   ```python
   haslo = "python"
   if haslo == "python":
       print("OK")
   else:
       print("BŁĄD")
   ```
   Kiedy zostanie wypisane `BŁĄD`?

9. Kod:
   ```python
   temperatura = 19
   if temperatura > 20:
       print("Ciepło")
   else:
       print("Chłodno")
   ```
   Zaznacz, który napis pojawi się na ekranie.

10. Kod:
    ```python
    tekst = "Ala"
    print(tekst.lower())
    ```
    Co zrobi metoda `lower()`?

11. Kod:
    ```python
    n = 7
    if n % 2 == 0:
        print("parzysta")
    else:
        print("nieparzysta")
    ```
    Wyjaśnij, do czego służy operator `%`.

12. Kod:
    ```python
    suma = 0
    for i in range(1, 4):
        suma += i
    print(suma)
    ```
    Podaj końcową wartość zmiennej `suma`.

13. Kod:
    ```python
    owoce = ["jabłko", "banan", "gruszka"]
    for owoc in owoce:
        print(owoc)
    ```
    Co oznacza nazwa `owoc` w pętli?

14. Kod:
    ```python
    def przywitaj():
        print("Hej!")

    przywitaj()
    ```
    Zaznacz poprawne zdanie: kiedy funkcja się wykona?

15. Kod:
    ```python
    def dodaj(a, b):
        return a + b

    wynik = dodaj(2, 3)
    print(wynik)
    ```
    Co oznacza słowo `return`?

---

## B. Uzupełnianie bardzo prostych luk

16. Uzupełnij brakującą liczbę:
    ```python
    for i in range(___):
        print("Hej")
    ```
    aby napis wypisał się 5 razy.

17. Uzupełnij operator porównania:
    ```python
    if 7 ___ 3:
        print("tak")
    ```
    aby warunek był prawdziwy.

18. Uzupełnij nazwę funkcji:
    ```python
    liczby = [1, 2, 3, 4]
    print(___(liczby))
    ```
    aby wypisać liczbę elementów listy.

19. Uzupełnij metodę napisu:
    ```python
    imie = "ola"
    print(imie.___())
    ```
    aby wynik to było `Ola`.
    Wybierz jedną opcję: `capitalize`, `upper`, `lower`, `title`.

20. Uzupełnij jedną linijkę:
    ```python
    def pole_kwadratu(a):
        ___
    ```
    aby funkcja zwracała pole kwadratu.

21. Uzupełnij wartość logiczną:
    ```python
    czy_pada = ___
    if czy_pada:
        print("Weź parasol")
    ```
    tak, aby komunikat się pojawił.

22. Uzupełnij brakujący argument:
    ```python
    print("Python", ___)
    ```
    aby wypisać `Python jest super`.

23. Uzupełnij indeks:
    ```python
    kolory = ["czerwony", "zielony", "niebieski"]
    print(kolory[___])
    ```
    aby wypisać `zielony`.

24. Uzupełnij warunek:
    ```python
    punkty = 85
    if punkty ___ 50:
        print("zdane")
    ```
    aby dla tej wartości wypisało `zdane`.

25. Uzupełnij kod, dodając odpowiedni operator:
    ```python
    licznik = 0
    licznik ___ 1
    print(licznik)
    ```
    Wybierz jedną opcję: `=`, `+=`, `-`, `-=`.
    aby wynik był `1`.

---

## C. Wyszukiwanie informacji w internecie (z podaniem źródła)

> Przy każdym zadaniu uczeń podaje: nazwę strony, link i 1–2 zdania własnego podsumowania.

26. Sprawdź, czym jest Python i kto go stworzył.

27. Znajdź, do czego służy funkcja `print()` w Pythonie.

28. Znajdź różnicę między `=` i `==`.

29. Wyszukaj, czym jest pętla `for` i podaj prosty przykład.

30. Sprawdź, czym różni się `list` od `tuple` (na bardzo podstawowym poziomie).

31. Znajdź, co robi funkcja `input()` i jak zamienić jej wynik na liczbę.

32. Wyszukaj, co robi funkcja `len()` i podaj 2 przykłady użycia.

33. Znajdź, jak działają `and`, `or`, `not` w warunkach.

34. Sprawdź, co to jest `SyntaxError` i kiedy może się pojawić.

35. Znajdź aktualną cenę euro (EUR/PLN) i podaj źródło oraz datę odczytu.

36. Sprawdź, czym jest licencja open source (w 1–2 prostych zdaniach).

37. Znajdź, czym jest GitHub i do czego używa się go w programowaniu.

38. Wyszukaj, co oznacza skrót AI i podaj 2 przykłady zastosowań w życiu codziennym.

39. Sprawdź, czym jest phishing i jak go rozpoznać.

40. Znajdź różnicę między stroną HTTP a HTTPS.

---

## D. Krótkie zadania mieszane (kod + internet)

41. Odczytaj kod, który wypisuje temperaturę, a potem wyszukaj w internecie, jak zapisać symbol stopni Celsjusza (`°C`) w tekście.

42. Przeczytaj kod z listą zakupów i wyszukaj 2 inne metody list w Pythonie (np. `append`, `remove`) – tylko opisz, bez pisania programu od zera.

43. Odczytaj warunek `if/else`, a następnie znajdź w internecie, jak działa `elif` i kiedy go używamy.

44. Przeczytaj funkcję z `return`, a potem wyszukaj różnicę między `print()` i `return`.

45. Odczytaj kod z pętlą `for`, a następnie znajdź, do czego służy `range(start, stop, step)`.

---

## Proponowane dodatkowe tematy

1. **Higiena cyfrowa i ergonomia pracy** – przerwy od ekranu, postawa, ochrona wzroku.
2. **Wiarygodność źródeł** – jak odróżniać rzetelne treści od niepewnych.
3. **Podstawy prawa autorskiego** – co wolno kopiować z internetu, a czego nie.
4. **Bezpieczeństwo kont** – silne hasła, 2FA, menedżery haseł.
5. **Netiquette** – kultura wypowiedzi online i odpowiedzialna komunikacja.
6. **Fake news i dezinformacja** – podstawowe techniki rozpoznawania.
7. **Wprowadzenie do algorytmiki bez kodowania** – schematy blokowe, kolejność kroków.
8. **Debugowanie krok po kroku** – czytanie komunikatów błędów i poprawianie drobnych pomyłek.
9. **Praca projektowa w parach** – podział ról, komunikacja, prosta recenzja kodu.
10. **Podstawy danych i wykresów** – interpretacja prostych tabel i wykresów.
11. **Narzędzia AI w nauce** – jak zadawać pytania i jak sprawdzać odpowiedzi modelu.
12. **Mini-projekty interdyscyplinarne** – łączenie informatyki z matematyką, polskim i przyrodą.

---

## Szybka propozycja organizacji pracy
- 50% czasu: rozumienie gotowego kodu.
- 30% czasu: zadania internetowe z weryfikacją źródła.
- 20% czasu: krótkie uzupełnianie luk.

Dobrą praktyką jest ocenianie nie tylko „czy odpowiedź jest poprawna”, ale też:
- czy uczeń umie uzasadnić odpowiedź,
- czy potrafi wskazać, **w której linijce kodu** znalazł wskazówkę,
- czy podaje wiarygodne źródło internetowe.
