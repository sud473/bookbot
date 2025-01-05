from typing import Dict


def char_counter(text: str) -> Dict[str, int]:
    freq = {}

    for char in text:
        if char.lower() in freq:
            freq[char.lower()] += 1
        else:
            freq[char.lower()] = 1
    return freq

def word_counter(text: str) -> int:
    return len(text.split())

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f'{word_counter(file_contents)} words found in the document\n')

    for char, freq in char_counter(file_contents).items():
        if char.isalpha():
            print(f"The '{char}' character was found {freq} times")
            
    print("--- End report ---")
    
if __name__ == '__main__':
    main()