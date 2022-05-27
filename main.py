# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
     
    my_file = open(filename, "r") 

  
# reading the file 

    data = my_file.read() 
    
    

    data_into_list = data.replace('\n', ' ').split(" ")
    dictionary = { data_into_list[i] : i  for i in range(0, len(data_into_list) ) }
    
# printing the data 

    print(dictionary) 
    my_file.close() 
    

    return "Hello World"

def count_words():
    text = read_file_content("Reading-Text-Files\story.txt")
    

    return {"as": 10, "would": 20}


count_words()    