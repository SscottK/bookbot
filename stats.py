#this is where we split the book and return the number of words
def get_num_words(text):
    words = text.split()
    return len(words)

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
        print(f"{i["letter"]}: {i["count"]}")