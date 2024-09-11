import json
from difflib import get_close_matches

# Load the dictionary from a JSON file
def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The dictionary data file is not found!")
        return {}

# Load the dictionary data
dictionary_data = load_dictionary('data.json')

#Create a function to return the word definition
def get_definition(word):
    word = word.lower()  # Make the search case-insensitive
    if word in dictionary_data:
        return dictionary_data[word]  # Return the definition if the word is found
    else:
        return None  # Return None if the word is not found


def search_word(word):
    definition = get_definition(word)
    if definition:
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"Sorry, the word '{word}' was not found in the dictionary.")
        # If the word is not found, suggest possible close matches using difflib
        suggest_similar_words(word)

# Use difflib to suggest similar words in case of misspelling
def suggest_similar_words(word):
    close_matches = get_close_matches(word, dictionary_data.keys(), n=3, cutoff=0.8)
    if close_matches:
        print(f"Did you mean one of these words? {', '.join(close_matches)}")
    else:
        print("No close matches found.")


def main():
    while True:
        word = input("Enter a word to search its definition (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            search_word(word)

if __name__ == "__main__":
    main()
