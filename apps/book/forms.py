from django import forms
from apps.core.constants import BOOK_CATEGORY, BOOK_FORMAT, LANGUAGES
from apps.book.models import Tag, Author

class PostBookForm(forms.Form):
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "isbn-input",
                "placeholder": "Enter isbn"
            }
        )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter text"
            }
        )
    )
    pages= forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "pages-input",
                "placeholder": "Enter page count"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "description-textarea",
                "placeholder": "Enter description"
            }
        )
    )
    category = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-cat",
            }
        ),
        choices=BOOK_CATEGORY,
        initial='pr'
    )
    published_year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "published-year-input",
                "placeholder": "Enter published year"
            }
        )
    )
    publisher = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "publisher-input",
                "placeholder": "Enter publisher"
            }
        )
    )
    edition = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "edition-input",
                "placeholder": "Enter book edition"
            }
        )
    )
    book_format = forms.ChoiceField(
        required=True,
    widget=forms.RadioSelect(
        attrs={
            "class": "form-format",
        }
    ),
    choices=BOOK_FORMAT
)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "tags-select"
            }
        )
)
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "authors-select",
            }
        )
)
    language = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "language-select"
            }
    ),
    choices=LANGUAGES,
    initial='en'
)
