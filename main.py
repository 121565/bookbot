def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()


        print(f"--- Begin report of {path_to_file} ---")
        print(f"{count_words(file_contents)} words found in document")
        print()



        letters_as_dict = count_letters(file_contents)
        letters_as_dict = dict(sorted(letters_as_dict.items(), key=lambda item: item[1], reverse=True))
        for i in letters_as_dict:
            print(f"The '{i}' character was found {letters_as_dict[i]} times")


def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letter_count = {}
    for letter in book_text:
        lowered_letter = letter.lower()
        if lowered_letter.isalpha() == True:
            if lowered_letter in letter_count:
                letter_count[lowered_letter.lower()] += 1
            else:
                letter_count[lowered_letter.lower()] = 1
    return letter_count


def sort_on(dict):
    return dict["num"]

if __name__ == '__main__':
    main()
