## 03.13
A node-os alkalmazáshoz a Dockerfile-t és a docker-compose.yml-t ezen videók alapján csináltam:
  https://www.youtube.com/watch?v=CsWoMpK3EtE&t=409s
  https://www.youtube.com/watch?v=Qw9zlE3t8Ko
  
Miután ez megvolt, és működött is az alkalmazás a 3030-as porton, elkezdtem dolgozni a cypress docker-esítésén.
Eőször is létrehoztam a cypress mappán belül egy Dockerfile-t. Ezt a gitrepo-t használtam alapként: https://github.com/cypress-io/cypress-example-docker-compose
Utánna kiegészítettem a docker-compose file-t.
Megpróbáltam tesztelni, hogy működik-e az egész projekt, de a cypress-es résznél elhasalt.
A tutorialban 'npx install cypress' command volt, én lecseréltem 'npm run cypress'-re, majd 'npm run cypress:all'-ra, hogy az összes tesztesetet lefuttassa.
Ekkor azt a hibaüzenetet kaptam, hogy a cypress nincsen telepítve, először telepítsem a csomagot 'cypress install'-al.
Átírtam a commandot a következőre: bysh -c "npm install cypress && nmp run cypress:all"
Ez egy újabb dependeciát dobott ki ami nincs telepítve. (talán Xvfb volt a neve) Itt abbahagytam a command piszkálását, nem hiszem hogy itt lenne  hiba.
Jelenleg itt tartok. :)

## 04.10
Orchestrátor komponens + Prométeusz komponens a projekthez adva
#### Orchestrátor:
- XML fájl beolvasás és megjelenítés flash-alapú python script segítségével
- Cypress konténer futtatása egy oldal felkeresésével (http://localhost:5000/results)
- Ezek mind lokálisan működnek
- Dockerfile is kész, de az alábbi problémába ütközök amikor build-elni szeretnék.
![](docker_error.png)
- Valamiért nem "találja" az xml fájlokat a mappában. Első sorban arra gyanakodtam, hogy nincsen futtatási/olvasási jog a fájlokhoz, de a jog hozzáadása se oldotta meg a problémát

##### Todo:
- Path megtalálásának megfixálása (ebben szeretnék segítséget kérni :) )
- XMl fájlok contentjének kiírátasának átformálása megfelelő struktúrára
- Oldal felkeresés helyett időzített cypress futtatás (cron)

#### Prometheus
- Docker image a yaml filehoz adva, megfelelő porton fut is az alkalmazás

##### Todo:
- Adatok bekötése
- Összekötés Grafanával
