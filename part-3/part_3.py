from turtle import title


my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book_string):
    book_string = f"My book is {my_book['title']}, written by {my_book['author']}. It was written in {my_book['year']}."
    print(book_string)

book_parser(my_book)



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(book_string):
    book_string = f"My book is {my_book['title']}"
    return book_string

book_title(my_book)

def book_year(book_string):
    book_string = f"My book is {my_book['year']}"
    return book_string

book_year(my_book)

def book_pages(book_string):
    book_string = f"My book is {my_book['pages']}"
    return book_string

book_pages(my_book)

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

