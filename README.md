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
|dla ilu osób jest przydatna|span[id^="votes-yes"]|useful||
|dla ilu osób jest nieprzydatna|span[id^="votes-no"]|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||