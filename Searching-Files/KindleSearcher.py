import csv
from Book import Book

file = "Kindle_Book_Dataset.csv"
books = []
go_on = "y"


with open(file) as myFile:
    kindle = csv.reader(myFile)
    for row in kindle:
        books.append(Book(row[0], row[1], row[2], row[3], row[14]))

while go_on == "y" or go_on == "Y" or go_on == "ye" or go_on == "Ye" or "ye" in go_on or "Ye" in go_on or "Yu" in go_on or "Yea" in go_on or "Ya" in go_on or "ya" in go_on:
    same_books= []
    hasbook = False
    results = 0
    actuallyhasbook = False

    user_book = input("\n\nWhat book are you looking for? Please enter the book title or the author. ")

    for book in books:
        if user_book.lower() in book.title.lower() or user_book.lower() in book.author.lower():
            hasbook = True
            same_books.append(book)
            results += 1
            continue
    if not(hasbook):
        print("\nHmmm... We found " + str(results) + " results with the keyword \"" + user_book + "\".")
        print("\nSorry then, either the book \"" + user_book + "\", or the selected author is not available on Amazon Kindle.\n")
        go_on = input("\nWould you like to continue searching for books? ")
        if go_on == "y" or go_on == "Y" or go_on == "ye" or go_on == "Ye" or "ye" in go_on or "Ye" in go_on or "Yu" in go_on or "Yea" in go_on or "Ya" in go_on or "ya" in go_on:
            continue
        else:
            break

    if hasbook:
        if results == 1:
            print("\nHmmm... We found " + str(results) + " result with the keyword \"" + user_book + "\".")
        else:
            print("\nHmmm... We found " + str(results) + " results with the keyword \"" + user_book + "\".")
        for same in same_books:
            if actuallyhasbook:
                break
            isbook = input("\nIs the book \"" + same.title + "\" by " + same.author + " the one you are looking for? ")
            if isbook == "y" or isbook == "Y" or isbook == "ye" or isbook == "Ye" or "ye" in isbook or "Ye" in isbook or "Yu" in isbook or "Yea" in isbook or "Ya" in isbook or "ya" in isbook:
                print("\nOkay, looks like Amazon Kindle has your book!")
                print("\nHere is some basic information about your book: ")
                print("\n\t URL: " + same.url)
                print("\t Title: " + same.title)
                print("\t Author: " + same.author)
                print("\t Price: $" + same.price)
                print("\t Rating: " + same.rating + "/5.0\n")
                actuallyhasbook = True
        if not(actuallyhasbook):
            print("\nSorry, either the book \"" + user_book + "\", or the selected author is not available on Amazon Kindle.\n")
        go_on = input("\nWould you like to continue searching for books? ")

print("\nGoodbye then! Thank you for using our service! Happy reading!\n")

