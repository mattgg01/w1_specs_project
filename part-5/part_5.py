### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_my_book(source):
    title = input("\nWhat is the title of your book?: ")
    author = input("Who is the author of your book?: ")
    try:
        year = int(input("What year was your book published?: "))
    except:
        year = int(input("You must use a whole number: "))
    try:
        rating = float(input("What rating out of 5 would you give your book?: "))
    except:
        rating = float(input("You must use a number 1-5: "))
    try:
        pages = int(input("How many pages does your book have?: "))
    except:
        pages = int(input("You must use a whole number: "))
    with open(source, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def book_view_first(source):
    print("\nThese are your books\n")
    with open(source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

#RANKED RATINGS
def get_rating_ranked(source):
    print("\nThese are all of your books by book rating descending\n")
    list = get_dictionaries(source)
    list =  sorted(list, key=lambda x: int(x["rating"]), reverse = True)
    for book in list:
        get_book_printed(book)


def get_dictionaries(source):
    books_list = []
    with open(source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

#PRINT BOOKS
def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")


#BEST RATING
def best_rating(source):
    list = get_dictionaries(source)
    return max(list, key=lambda x: int(x["rating"]))


# MAIN MENU
def main_menu(source):
    active = True
    while active:
        choice = input("""
Type 'add' to add a book...
Type 'view' to view all of your books
Type 'count' to see a count of your books
Type 'pages' to see a count of the pages in the book
Type 'best' to see the your highest book rating
Type 'worst' to see your lowest book rating
Type 'ranks' to see your books ranked by rating descending
Type 'exit' to exit
Type here: """)
        if choice == "add":
            create_my_book(source)
        elif choice == "view":
            view_books(source)
        elif choice == "count":
            print(f"\nYou have a total of {len(get_dictionaries(source))} books.\n")
        elif choice == "pages":
            print(f"\nYou books page count totals {sum([x['pages'] for x in get_dictionaries(source)])} pages!\n")
        elif choice == "best":
            print("\nHere is your highest rated book...\n")
            get_book_printed(best_rating(source))
        elif choice == "worst":
            print("\nHere is your lowest rated book...\n")
            get_book_printed(worst_rating(source))
        elif choice == "ranks":
            get_rating_ranked(source)
        elif choice == "exit":
            print("\nGoodbye")
            active = False
        else:
            print("\nPlease select a menu option from the list of options\n")

def worst_rating(source):
    list = get_dictionaries(source)
    return min(list, key=lambda x: int(x["rating"]))

def view_books(source):
    print("\nThese all of your books\n")
    for book in get_dictionaries(source):
        get_book_printed(book)


# if __name__ == “__main__”:
#     main_menu("library.txt")