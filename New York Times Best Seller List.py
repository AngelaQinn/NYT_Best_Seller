import requests

"""
Example Calls to get best seller list
https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=yourkey
https://api.nytimes.com/svc/books/v3/lists/2025-05-04/hardcover-fiction.json?api-key=yourkey
"""

API_url = 'https://api.nytimes.com/svc/books/v3/lists/2025-06-18/hardcover-fiction.json'
API_key = 'azQNIZ85Hq48qokNZWWGhqRQOStfNFDC'

def get_list():
    params = {'api-key': API_key}
    book_lst = requests.get(API_url, params)
    return book_lst.json()

def display_results(book_lst):
    books = book_lst['results']['books']
    for book in books:
        title = book['title']
        author = book['author']
        isbn = book['primary_isbn13']
        publisher = book['publisher']
        print('Title: ', title)
        print('Author: ', author)
        print('ISBN-13: ', isbn)
        print('Publisher: ', publisher)
        print('')

while True:
    book_lst = get_list()
    display_results(book_lst)
