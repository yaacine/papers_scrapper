# Author scrapping 

To start scrapping authors based on the keywords available on `scripts/V1.0.2/datasets/keywords.txt`  run the following command

```
python3 scripts/V1.0.2/main.py  author
```
2. To start scrapping authors based on the co-authoring and build the co-authoring relationship changing this variable AUTHORS_CSV_FILE_INPUT_COAUTHORS  in `scripts/V1.0.2/controller/authors.py`
 example:

```
AUTHORS_CSV_FILE_INPUT_COAUTHORS = 'scripts/V1.0.2/datasets/authors/authors2.csv'`
``` 

 , run the following command
```
python3 scripts/V1.0.2/main.py  coauthor
```

# Articles scrapping

1. To start scrapping articles of authors, follow these steps

change the source of authors that you want to use to get articles by changing this variable AUTHORS_CSV_FILE  in `scripts/V1.0.2/controller/publications.py`
 example:

```
AUTHORS_CSV_FILE = 'scripts/V1.0.2/datasets/authors/authors2.csv'`
``` 

**ps: the url should exist and have authors with `got_publications=0`**

run the following command
```
python3 scripts/V1.0.2/main.py  publication
```

2. To start scrapping articles based on the citations relationship follow these steps 

Edit the file link to the file from which you want to get the citation relationship in the by changing this variable `PUBLICATIONS_CSV_FILE_INPUT` in 
`scripts/V1.0.2/controller/publications.py` 
example: 

```
PUBLICATIONS_CSV_FILE_INPUT= 'scripts/V1.0.2/datasets/articles/articles2.csv'
```  

run the following command 
```
python3 scripts/V1.0.2/main.py  citation
```
 