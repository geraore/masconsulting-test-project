from django import forms

class SearchEmployeeForm(forms.Form):
    search_field = forms.CharField(label='Writhe down you employee ID',
                                   max_length=100,
                                   widget=forms.TextInput(attrs={'class': "form-control",
                                                                 'placeholder': 'Search employee ID'}),
                                   required=False)


