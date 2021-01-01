import os.path


def get_next_keyword():
    keywords_file = open(os.path.dirname(__file__) +'/keywords.txt', 'r') 
    lines = keywords_file.readlines()
    i =0
    stop = False
    while i< len(lines) and not stop:
        if lines[i][0]!="#": 
            stop = True
        else: i+=1
    # check if all the keywords are done
    if i == len(lines) -1:
        print ('ERROR: all keywords are done. Add some keywords to the keyword.txt file')
        keywords_file.close()
        raise EOFError
    else:
        return (i, lines[i])
    keywords_file.close()



def mark_line_as_done(line_index):
    keywords_file = open(os.path.dirname(__file__) +'/keywords.txt', 'r') 
    lines = keywords_file.readlines()
    keywords_file.close()
    keywords_file = open(os.path.dirname(__file__) +'/keywords.txt', 'w') 
    lines[line_index] = "#"+ lines[line_index] 
    keywords_file.writelines(lines) 
    keywords_file.close()

""" 
    A code example below

    (index, word ) = get_next_keyword()
    print (index)
    print(word)

    mark_line_as_done(index)
"""