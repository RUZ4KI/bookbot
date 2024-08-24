
def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    count = count_words(book)
    cnt_char = count_characters(book)
    arr = list(cnt_char.items())
    sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)
    print_arr(sorted_arr,count)


def print_arr(arr,cnt):
     print("--- Begin report of books/frankenstein.txt ---")
     print(cnt,"words found in the document")
     for i in arr:
          print(f"The '{i[0]}' character was found {i[1]} times")

def count_characters(book):
     lowercase = book.lower()
     char_dic = {}
     for char in lowercase:
          if char.isalpha():
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1
     return char_dic

def sort_on(dict):
    return dict["num"]

def count_words(text):
     words = text.split()
     return len(words)

def read_book(path):
        with open(path) as f:
            return f.read()
    
    
main()