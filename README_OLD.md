# Paper Extractor

## Description


This projects extracts papers information from google scholar and stores them in csv files

The resulted csv files are stored in `./datasets/` folder and partitionned over different files of 1000 papers max for a file

***


## Requirements
-  Scholarly package 

```
pip3 install scholarly
```

## How to use it

### FEATURE 1 : Data scrapping

#### 1. Enter the author names 

In the `extract.py` file you will find an array called authors

```
authors = [
    # 'Byung Kyu Kim' done 
    # 'Andrea Toldy', not found
    # 'Ahmad Reza Bahramian', not found
    # 'Jens Gaitzsch', not found
    # 'Jan Feijen',  done
    #'PWM Blom', done
    #'Katharina Landfester', not found
    # 'Kurt Kremer', done partition 3
    # 'Qiang Fu' done partition 5
    'Carlo Dallapiccola',
    # 'Francisco Matorras',
    # 'Haijun Yang',
    # 'Martin Grunewald'
]
```

You can add other names to the list but make sure to uncomment one or two authors at a time and comment the name of the author once his papers are extracted and mention which partition contains his papers.
 

#### 2. Start the extraction
to start the extraction run 
```
python3 extract.py
```
You will be prompted to enter the partition number. To avoid conflicts, yacine starts from 1 to 999 and Mehdi starts from 1000 to 2000


A csv file will be created based on the partition number chosen , for example if you choose `partition = 1001 ` the file `datasets/articles_part1001.csv` will be created and the index will start at `1001000`


### FEATURE 2 : Clean the scrapped data

This feature allows to gather a number of partitions together and eliminate the duplicates. To do this follow these steps

1. Run the script
```
python3 clean.py
```
2. You will be promted to enter the number of start and the number of end of the papers you want to group
for example 

```
Enter the starting partition number: 1
```  
```
Enter the ending partition number: 12
```  
will gather the files from `datasets/articles_part1.csv` to `datasets/articles_part12.csv`

The result will be stored in the followinf file 
```
datasets/cleaned/articles_1_12_clean.csv
```


### FEATURE 3 : Topic extraction from cleaned data

