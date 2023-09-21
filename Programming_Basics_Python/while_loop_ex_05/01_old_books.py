needed_book = input()
book_counter = 0
current_book = input()
no_more_books = False
while current_book != needed_book:

    if current_book == 'No More Books':
        no_more_books = True

        break

    book_counter += 1
    current_book = input()

if no_more_books:
    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')
else:
    print(f'You checked {book_counter} books and found it.')

