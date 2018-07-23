# carandclassic
Collect car data at https://www.carandclassic.co.uk/

## Tech
python3, urllib, BeautifulSoup

## Demo
```bash 
# demo of cclassic_scrape_V1.py 
$ git clone https://github.com/yennanliu/web_scraping
$ cd web_scraping/carandclassic
$ python cclassic_scrape_V1.py

# output 
['/car/C1018332', '/car/C983211', '/car/C1018314', '/car/C1018313', '/car/C1018311', '/car/C901161', '/car/C305537', '/car/C1018308', '/car/C994875', '/car/C990970', '/car/C1018297', '/car/C1018296', '/car/C1018294', '/car/C998769', '/car/C1009081', '/car/C1018284', '/car/C1018283', '/car/C1018281', '/car/C887797', '/car/C1018280', '/car/C1018279', '/car/C1005573', '/car/C1018274', '/car/C1018272', '/car/C1018269', '/car/C1018268', '/car/C1018266', '/car/C387007', '/car/C1018263', '/car/C1018262', '/car/C1018257', '/car/C1018251', '/car/C1018249', '/car/C1018247', '/car/C1018236', '/car/C1018220']
url_ :  https://www.carandclassic.co.uk/car/C1018332
k_next £3999 As stated
k_next Classic Cars
k_next Austin Healey
k_next Sprite
k_next 1968
k_next UK
k_next 07043 229662
k_next 23-Jul-2018
k_next C1018332
...
      Price      Category           Make                   Model  Year  \
0     £3999  Classic Cars  Austin Healey                  Sprite  1968   
1    £27950  Classic Cars           Audi                 Quattro  1984   
2     £3495  Classic Cars         Morris                   Minor  1968   
3     £6500  Classic Cars     Volkswagen                  Beetle  1971   
4    £12500  Classic Cars             MG            MGB Roadster  1973   
5    £40000  Classic Cars          Buick   redfern saloon tourer  1937   
 ...
   Country     Telephone         Date       Ref  
0       UK  07043 229662  23-Jul-2018  C1018332  
1       UK  07043 216048  23-Jul-2018   C983211  
2       UK  07043 225499  22-Jul-2018  C1018314  
3       UK  07043 217556  22-Jul-2018  C1018313  
4       UK  07043 215436  22-Jul-2018  C1018311  
5       UK  07043 228310  22-Jul-2018   C901161  
....




```

