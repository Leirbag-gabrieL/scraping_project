# 🕷️ scraping_project 🕷️

Projet de scraping de site web ( https://www.zenithwakfu.com/builder en l'occurence ).

Objectifs :

- Se familiariser avec la lib Scrapy 👷
- Ne pas se faire ban de zenithwakfu 🛑
- S'amuser 🎉


Pour lancer le projet :

1) Faire un `source` sur `bin/activate` afin d'activer le virtual environment
2) Lancer la commande `scrapy crawl build_spider -a request=<mon url à scrap>` depuis `/src/item_scraper`
3) Si tout ce passe bien, un fichier out.csv sera généré

NB: vous pouvez tester si l'url fonctionne correctement en ajoutant l'option `-a display=true`