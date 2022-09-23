### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def create_my_book():
#     title = input("What is the title of your book?: ")
#     author = input("Who is the author of your book?: ")
#     year = input("What year was your book published?: ")
#     rating = input("What rating out of 5 would you give your book?: ")
#     pages = input("How many pages are in your book?: ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_my_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_my_book():
#     title = input("What is the title of your book?: ")
#     author = input("Who is the author of your book?: ")
#     year = int(input("What year was your book published?: "))
#     rating = float(input("What rating out of 5 would you give your book?: "))
#     pages = int(input("How many pages are in your book?: "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_my_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_my_book():
    title = input("What is the title of your book?: ")
    author = input("Who is the author of your book?: ")
    try:
        year = int(input("What year was your book published?: "))
    except:
        year = int(input("Please type a whole number for the year?: "))
    try:
        rating = float(input("What rating out of 5 would you give your book?: "))
    except:
        rating = float(input("Please give a number 1-5?: "))
    try:
        pages = int(input("How many pages are in your book?: "))
    except:
        pages = int(input("Please give a whole number for the pages in the book?: "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

print(create_my_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# book_list = []
# def create_my_book():
#     title = input("What is the title of your book?: ")
#     author = input("Who is the author of your book?: ")
#     try:
#         year = int(input("What year was your book published?: "))
#     except:
#         year = int(input("Please type a whole number for the year?: "))
#     try:
#         rating = float(input("What rating out of 5 would you give your book?: "))
#     except:
#         rating = float(input("Please give a number 1-5?: "))
#     try:
#         pages = int(input("How many pages are in your book?: "))
#     except:
#         pages = int(input("Please give a whole number for the pages in the book?: "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
    
#     return book_dictionary

# print(create_my_book())


# def print_all_books(list_of_books):

#     print("\nHere are all your books...\n")

#     for book in list_of_books:
#         title = book["title"]
#         author = book["author"]
#         year = book["year"]
#         rating = book["rating"]
#         pages = book["pages"]

#         print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


# def menu_select():
#     selection = input("Would like like to add a book, or view all books?: ")
#     if selection == "add":
#         book_list.append(create_my_book())
#     elif selection == "view":
#         print_all_books()










### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

book_list = []
def create_my_book():
    title = input("What is the title of your book?: ")
    author = input("Who is the author of your book?: ")
    try:
        year = int(input("What year was your book published?: "))
    except:
        year = int(input("Please type a whole number for the year?: "))
    try:
        rating = float(input("What rating out of 5 would you give your book?: "))
    except:
        rating = float(input("Please give a number 1-5?: "))
    try:
        pages = int(input("How many pages are in your book?: "))
    except:
        pages = int(input("Please give a whole number for the pages in the book?: "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    
    return book_dictionary

print(create_my_book())


def print_all_books(list_of_books):

    print("\nHere are all your books...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


def main_menu(books_source):

    active = True

    while active:
        choice = input("\n 'Add' to add a book...\n'View' to view your books...\n'Count' to see how many books you have...\n'Pages' to view the number of pages in your books...\n'Exit' to exit.\nType here: ")

        if choice == "Add":
            books_source.append(create_my_book())
        elif choice == "View":
            print_all_books(books_source)
        elif choice == "Count":
            print(f"\nYou have a total of {len(books_source)} books.\n")
        elif choice == "Pages":
            print(f"\nYou books page count totals {sum([x['pages'] for x in books_source])} pages!\n")
        elif choice == "Exit":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please type a number for one of the options.\n")

main_menu(book_list)