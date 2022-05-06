# CeneoScraper

## Struktura opinii w serwisie [ceneo.pl]("https://www.ceneo.pl/91714422#tab=reviews")

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\[data-entry-id\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature_positives ~ div.review-feature-item|pros|list|
|lista wad|div.review-feature_negatives ~ div.review-feature-item|cons|list|
|dla ilu osób jest przydatna|span[id^="votes-yes"]|useful|int|
|dla ilu osób jest nieprzydatna|span[id^="votes-no"]|useless|int|
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||


## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedyńczych opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie mozliwości podania kodu produktu przez uzytkownikow
7. Optymalizacja kodu:
    a. utworzenie funkcji do ekstrakcji elementow strony 
    b. utworzenie slownika selektorow
    c. uzycie dictionary comprehension do pobrania skladowych pojedynczej opinii na podstawie slownika selektorow
8.