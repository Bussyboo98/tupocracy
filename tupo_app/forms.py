from django import forms
from tupo_app.models import *

   

   
class NominationForm(forms.ModelForm):
    ONE = "Dr."
    TWO = "Doctor"
    THREE = "Mr."
    FOUR = "Mrs."   
    FIVE = "Ms."   
    CHOOSE = ""

    TUPO= [
         (ONE, 'Dr.'),
         (TWO, ' Doctor'),
         (THREE, 'Mr.'),
         (FOUR, 'Mrs.'),
         (FIVE, 'Ms.'  ),
         (CHOOSE, 'Choose Title')
    ]

    ONE = "Yes"
    TWO = "No"
  
    CHOOSE = ""

    TITLE= [
         (ONE, 'Yes'),
         (TWO, ' No'),
         
         (CHOOSE, 'Select')
    ]
    class Meta():
        model = Nomination
        fields = "__all__"
   
        
        widgets = {
            'award_title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Award Title'}),
            'title' :forms.Select(attrs={'class': 'form-control'}),
            'da_ti': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD:MM:YY  h:m'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), 
            'last_name':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LasttName'}),
            'position':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position/Title'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Birthday'}),
            'employer':  forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PhoneNumber'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@gmail.com'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'home': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Home Address'}),
            'member' :forms.Textarea(attrs={'class': 'form-control'}),
            'select_all' :forms.Select(attrs={'class': 'form-control'}),
           
           
            
        }
class PrincipalForm(forms.ModelForm):
    ONE = "Dr."
    TWO = "Doctor"
    THREE = "Mr."
    FOUR = "Mrs."   
    FIVE = "Ms."   
    CHOOSE = ""

    TUPO= [
         (ONE, 'Dr.'),
         (TWO, ' Doctor'),
         (THREE, 'Mr.'),
         (FOUR, 'Mrs.'),
         (FIVE, 'Ms.'  ),
         (CHOOSE, 'Choose Title')
    ]

    ONE = "Yes"
    TWO = "No"
  
    CHOOSE = ""

    TITLE= [
         (ONE, 'Yes'),
         (TWO, ' No'),
         
         (CHOOSE, 'Select')
    ]
    class Meta():
        model = Principal
        fields = "__all__"
   
        
        widgets = {
            'award_title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Award Title'}),
            'title' :forms.Select(attrs={'class': 'form-control'}),
           
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), 
            'last_name':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LasttName'}),
            'position':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position/Title'}),
          
            'employer':  forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PhoneNumber'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@gmail.com'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'home': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Home Address'}),
            'member' :forms.Textarea(attrs={'class': 'form-control'}),
            'select_all' :forms.Select(attrs={'class': 'form-control'}),
            'name1':  forms.TextInput(attrs={'class': 'form-control'}),
            'affilation1': forms.TextInput(attrs={'class': 'form-control'}),
            'name2':  forms.TextInput(attrs={'class': 'form-control'}),
            'affilation2': forms.TextInput(attrs={'class': 'form-control'}),
            'name3':  forms.TextInput(attrs={'class': 'form-control'}),
            'affilation3': forms.TextInput(attrs={'class': 'form-control'}),
            'name4':  forms.TextInput(attrs={'class': 'form-control'}),
            'affilation4': forms.TextInput(attrs={'class': 'form-control'}),
            'name5':  forms.TextInput(attrs={'class': 'form-control'}),
            'affilation5': forms.TextInput(attrs={'class': 'form-control'}),
           
           
            
        }
