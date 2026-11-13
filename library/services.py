from .models import BookRequest

def create_book_request(book, cleaned_data):
    req = BookRequest(
        book=book,
        reader_name=cleaned_data.get('reader_name'),
        phone=cleaned_data.get('phone')
    )
    req.save()
    return req