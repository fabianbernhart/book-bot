from stats import get_num_words, get_characters

import sys
import os



def get_book_text(path: str) -> str | FileNotFoundError:
   
   if not os.path.isfile(path):
      raise FileNotFoundError(f"No such file: '{path}'")
   
   with open(path) as f:
      
       return f.read()
   

def display(file_name: str, book_wods_count: int, charakters_dict: dict) -> str:
   output = []
   output.append(format("BOOKBOT", "=^33"))
   output.append(f"Analyzing book found at {file_name}")
   output.append(format(" Word Count ", "-^33"))
   output.append(f"Found {book_wods_count} total words")
   output.append(format(" Character Count ", "-^33"))
   
   for char, count in sorted(charakters_dict.items()):
      if char.isalpha():
         output.append(f"{char}: {count}")
   
   output.append(format(" END ", "=^33"))
   
   return "\n".join(output)
   

def main(args: list[str]):
   
   if len(args) < 2:
      print("Usage: python main.py <path_to_book>")
      return
   
   file_name: str = args[1]
   
   
   try:
      book_content: str = get_book_text(file_name)
   except FileNotFoundError as e:
      print(e)
      return
   
   book_wods_count: int = len(get_num_words(book_content))
   charakters_dict: dict = get_characters(book_content)
   
   display_content: str = display(book_wods_count=book_wods_count, charakters_dict=charakters_dict, file_name=file_name)
   
   print(display_content)


if __name__ == "__main__":
   main(sys.argv)
   
   

