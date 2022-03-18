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
