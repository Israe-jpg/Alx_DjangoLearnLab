# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: Book instance created with title "1984", author "George Orwell", and publication year 1949.

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# Output: 1984 George Orwell 1949

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
# Output: Book title updated to "Nineteen Eighty-Four".

retrieved_book.delete()
# Output: Book instance deleted.
