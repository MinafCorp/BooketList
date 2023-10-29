from django import forms

class WishlistSearchForm(forms.Form):
    bookTitleSearch = forms.CharField(label='Search for a book', max_length=100, required=False)
    yearFilter = forms.ChoiceField(
        label='Year Filter',
        choices=[
            ('all', 'All Years'),
            ('<1990', 'Before 1990'),
            ('1990-2000', '1990 - 2000'),
            ('>2000', 'After 2000'),
        ],
        required=False
    )
