from stats import count_words, count_chars, count_dict
import sys

def get_book_text(filepath):
    file_content=""
    with open(filepath) as f:
        file_content = f.read()
    return file_content



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    all_chars= count_chars(sys.argv[1])
    report = count_dict(all_chars)
    for dictionary in report:
        print(f"{dictionary["char"]}: {dictionary["num"]} ")
    print("============= END ===============")
if __name__ == "__main__":
    main()