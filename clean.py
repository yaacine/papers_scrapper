
import csv

partition_start_str = input("Enter the starting partition number:   ")
partition_start_nbr =int(partition_start_str)

partition_end_str = input("Enter the ending partition number:   ")
partition_end_nbr =int(partition_end_str)

csv_columns = ['id','abstract','author','cites','cites_id','journal','number','pages','publisher','title','url','volume','year','citation_link' , 'id_citations']
csv_file = "datasets/cleaned/articles_1_16_clean.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
    writer.writeheader()

    counter = partition_start_nbr
    while counter<= partition_end_nbr:

        print(counter)
        current_file_number= str(counter)
        current_file_name = "datasets/articles_part"+current_file_number+".csv"

        # f1 = csv.reader(open(current_file_name, 'rt' ))

        with open(current_file_name) as f:
            f1= csv.DictReader(f, skipinitialspace=True)
            abstracts = set()
            for row in f1:
                # print(row)
                if row["title"] not in abstracts:
                    writer.writerow(row)
                    abstracts.add( row["title"] )

        counter = counter+1