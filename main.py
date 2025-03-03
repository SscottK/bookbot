import sys
from stats import get_num_words, letter_count, letter_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")    
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    # print(text)
    lowered_text = text.lower()
    counts = letter_count(lowered_text)
    letters = letter_count(lowered_text)
    # print(letters)
    letter_report(counts)
    print("--- End report ---")
   
    



#here we are opening the file to be read
def get_book_text(path):
    with open(path) as f:
        return f.read()



 
    
main()