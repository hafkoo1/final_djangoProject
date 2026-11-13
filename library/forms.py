from django import forms
from datetime import datetime
import re
from .models import Book, BookRequest

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year', 'pages', 'description', 'is_available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        current_year = datetime.now().year
        if year < 1000 or year > current_year:
            raise forms.ValidationError(f"Рік має бути в межах від 1000 до {current_year}.")
        return year

    def clean_pages(self):
        pages = self.cleaned_data.get('pages')
        if pages is not None and pages <= 0:
            raise forms.ValidationError("Кількість сторінок має бути більшою за 0.")
        return pages


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['reader_name', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        cleaned = re.sub(r'[\s\(\)\-]', '', phone)
        if not re.match(r'^\+?\d{10,13}$', cleaned):
            raise forms.ValidationError("Невірний формат телефону. Введіть від 10 до 13 цифр (допускається '+' на початку).")
        return cleaned