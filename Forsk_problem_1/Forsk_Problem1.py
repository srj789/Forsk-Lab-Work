file2 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/robinson_crusoe_defoe.txt","r",encoding="utf8")
file1 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/james_joyce_ulysses.txt","r",encoding="utf8")

file3 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/metamorphosis_kafka.txt","r",encoding="utf8")
file4 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/the_way_of_all_flash_butler.txt","r",encoding="utf8")


file5 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/moby_dick_melville.txt","r",encoding="utf8")
file6 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/sons_and_lovers_lawrence.txt","r",encoding="utf8")
file7 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/to_the_lighthouse_woolf.txt","r",encoding="utf8")

def count_word(fname):
    num_words=0
    for line in fname:
         words = line.split()
         num_words += len(words)
    print("Number of words:")
    print(num_words) 
count_word(file1)
count_word(file2)
count_word(file3)
count_word(file4)
count_word(file5)
count_word(file6)
count_word(file7)

def count_unique_word(fname):
    read_File = fname.read()
    words = read_File.split()
    unique_words = set(words)
    print("Number of unique words:")
    print(len(unique_words))
    return unique_words

file2 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/robinson_crusoe_defoe.txt","r",encoding="utf8") 
s2=count_unique_word(file2)
file1 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/james_joyce_ulysses.txt","r",encoding="utf8")
s1=count_unique_word(file1)
file3 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/metamorphosis_kafka.txt","r",encoding="utf8")
s3=count_unique_word(file3)
file4 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/the_way_of_all_flash_butler.txt","r",encoding="utf8")
s4=count_unique_word(file4)

file5 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/moby_dick_melville.txt","r",encoding="utf8")
s5=count_unique_word(file5)
file6 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/sons_and_lovers_lawrence.txt","r",encoding="utf8")
s6=count_unique_word(file6)
file7 = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/to_the_lighthouse_woolf.txt","r",encoding="utf8")
s7=count_unique_word(file7)

print("Special Words in Ulysses novel by comparing with others, words which are only used in Ulysses: ")

print(len(list(s1-s2-s3-s4-s5-s6-s7)))
#print(list(s1-s2-s3-s4-s5-s6-s7))
file = open("C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Final_common_Words.txt","w",encoding="utf8")
file.write(str(set(s1-s2-s3-s4-s5-s6-s7)))

print("Number of common words which occur in every book")
sets=[s1,s2,s3,s4,s5,s6,s7]
final=set.intersection(*sets)
print(len(final))
#print(final)


