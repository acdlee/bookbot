#!/usr/bin/python3
import sys
from stats import count_words, count_characters, sort_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(word_count, chars_data):
    report = "============ BOOKBOT ============\n----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n--------- Character Count -------\n"
    
    for datum in chars_data:
        if datum["char"].isalpha():
            report += f"{datum["char"]}: {datum["num"]}\n"
    
    report += "============= END ===============\n"
    
    print(report)
        
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)
    sorted_chars_list = sort_chars_dict(chars_dict)
    
    print_report(num_words, sorted_chars_list)
    
    
    
main()