def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    lowered_text = text.lower()
    counts = letter_count(lowered_text)
    print(counts)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def letter_count(lowered_text):
    amount = 0
    lowers = []
    
    for i in range(len(lowered_text)):
        if not lowered_text[i] in lowers:
            lowers.append(lowered_text[i])
            amount += 1
        else:
            amount += 1
    
        
        
    return lowers, amount
    


main()