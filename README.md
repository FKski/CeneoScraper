# CeneoScraper

## Struktura opinii w serwisie [ceneo.pl]("https://www.ceneo.pl/91714422#tab=reviews")

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|||
|identyfikator opinii|"div.js_product-review\[data-entry-id\]"|||
|autor opinii|span.user-post__author-name|||
|rekomendacja|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|div.review-feature_positives ~ div.review-feature-item|||
|lista wad|div.review-feature_negatives ~ div.review-feature-item|||
|dla ilu osób jest przydatna|span[id^="votes-yes"]|||
|dla ilu osób jest nieprzydatna|span[id^="votes-no"]|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|||