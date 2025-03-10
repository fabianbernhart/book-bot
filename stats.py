def get_num_words(book_text: str):
   return book_text.split()

def get_characters(book_text: str) -> dict[str, int]:

    characters = {}
    for char in book_text:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1


    return characters

   
   

