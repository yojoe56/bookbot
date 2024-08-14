def sort_on(dict):
    return dict["nums"]

def main():
    book = "books/frankenstien.txt"
    with open(book) as f:
        file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    print("--- Begin report of "+book+" ---")
    print(num_words,"words found in the document\n")
    dict1 = {}
    letters = file_contents.lower()
    for char in letters:
        if char in dict1:
            dict1[char] +=1
        else:
            dict1[char] =1
    sort_chars = []
    for entry in dict1:
        if entry.isalpha():
            sort_chars.append({"char": entry,  "nums": dict1[entry]})
    sort_chars.sort(reverse = True, key = sort_on)
    for n in sort_chars:
        print("The \'%c\' character was found %d times"%(n["char"],n["nums"]))
    print("--- End report ---")
    
    

main()
