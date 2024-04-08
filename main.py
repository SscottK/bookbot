def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()
    lowered_text = text.lower()
    counts = letter_count(lowered_text)
    letter_report(counts)
    print("--- End report ---")
   
    

#this is where we split the book and return the number of words
def get_num_words(text):
    words = text.split()
    return len(words)

#here we are opening the file to be read
def get_book_text(path):
    with open(path) as f:
        return f.read()

#here we add the letter to a the dictionary if it doesn't exist and update the count
def letter_count(lowered_text):
    counts_dict = {}    
    for i in range(len(lowered_text)):
        if not lowered_text[i] in counts_dict.keys():
            counts_dict[lowered_text[i]]= 1
        else:
            counts_dict[lowered_text[i]] =  counts_dict[lowered_text[i]] + 1   
    return counts_dict

def letter_report(counts):
    characters = []
    for key, value in counts.items():
        if key.isalpha():
            characters.append({"letter": key, "count": value})

    def sort_on(dict):
        return dict["count"]
    

    characters.sort(reverse=True, key=sort_on)
    for i in characters:
        print(f"The {i["letter"]} character was found {i["count"]} times") 

main()