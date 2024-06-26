from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import DecimalValidator
from django.utils import timezone
import re

def my_view(request):
    timezone.activate('UTC')

def validate_username(value):
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,20}$', value):
        raise ValidationError(
            'Username must be between 6-20 characters and contain at least 1 letter and 1 number.'
        )

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username ', max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    userPass = forms.CharField(label='Password ', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput())

class PersonalInfoForm(forms.Form):
    fName = forms.CharField(label='First Name ', max_length=50, widget=forms.TextInput(attrs={'class': 'name-field', 'autocomplete': 'off'}))
    lName = forms.CharField(label='Last Name ', max_length=50, widget=forms.TextInput(attrs={'class': 'name-field', 'autocomplete': 'off'}))
    date_of_birth = forms.DateField(label='Date of Birth ', widget=forms.DateInput(attrs={'class': 'dob-phoneNo-field', 'autocomplete': 'off'}))
    gender = forms.ChoiceField(label='Gender ', choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'gender-field'}))
    phoneNo = forms.CharField(label='Phone Number ', max_length=20, widget=forms.TextInput(attrs={'class': 'dob-phoneNo-field', 'autocomplete': 'off'}))
    email = forms.EmailField(label='Email ', widget=forms.EmailInput(attrs={'class': 'email-field', 'autocomplete': 'off'}))
    address = forms.CharField(label='Address ', widget=forms.Textarea(attrs={'class': 'address-field', 'autocomplete': 'off'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username ', max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    userPass = forms.CharField(label='Password ', widget=forms.PasswordInput())

class ForgotPassForm(forms.Form):
    username = forms.CharField(label='Username ', max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email = forms.EmailField(label='Email ')

class ResetPassForm(forms.Form):
    userPass = forms.CharField(label='New Password ', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput())

class EditProfileForm(forms.Form):
    fName = forms.CharField(label='First Name ', max_length=50, widget=forms.TextInput(attrs={'class': 'name-field', 'autocomplete': 'off'}))
    lName = forms.CharField(label='Last Name ', max_length=50, widget=forms.TextInput(attrs={'class': 'name-field', 'autocomplete': 'off'}))
    date_of_birth = forms.DateField(label='Date of Birth ', widget=forms.DateInput(attrs={'class': 'dob-phoneNo-field', 'autocomplete': 'off'}))
    gender = forms.ChoiceField(label='Gender ', choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'gender-field'}))
    phoneNo = forms.CharField(label='Phone Number ', max_length=20, widget=forms.TextInput(attrs={'class': 'dob-phoneNo-field', 'autocomplete': 'off'}))
    email = forms.EmailField(label='Email ', widget=forms.EmailInput(attrs={'class': 'email-field', 'autocomplete': 'off'}))
    address = forms.CharField(label='Address ', widget=forms.Textarea(attrs={'class': 'address-field', 'autocomplete': 'off'}))

class CreateAuctionForm(forms.Form):
    item_name = forms.CharField(label='Item Name ', required=True, max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'item-name-field'}))
    item_desc = forms.CharField(label='Item Description ', required=True, max_length=200, widget=forms.Textarea(attrs={'autocomplete': 'off', 'class': 'item-desc-field'}))
    item_cat = forms.ChoiceField(label='Item Category ', required=True, choices=[('Apparel & Accessories', 'Apparel & Accessories'), ('Animal & Pet Supplies', 'Animal & Pet Supplies'),
                                                                                ('Arts & Entertainment', 'Arts & Entertainment'), ('Baby & Toddler', 'Baby & Toddler'),
                                                                                ('Camera & Optics', 'Camera & Optics'), ('Electronics', 'Electronics'), ('Food & Beverages', 'Food & Beverages'),
                                                                                ('Furniture', 'Furniture'), ('Hardware', 'Hardware'), ('Home & Garden', 'Home & Garden'), 
                                                                                ('Health & Beauty', 'Health & Beauty'), ('Luggage & Bags', 'Luggage & Bags'), ('Office Supplies', 'Office Supplies'),
                                                                                ('Religious', 'Religious'), ('Sporting Goods', 'Sporting Goods'), ('Toys & Games', 'Toys & Games'),
                                                                                ('Vehicle & Parts', 'Vehicle & Parts'), ('Others', 'Others')
                                                                                ], widget=forms.Select(attrs={'class': 'item-cat-field'}))
    start_bid = forms.DecimalField(label='Starting Bid ', required=True, max_digits=10, decimal_places=2, min_value=1,
                                    widget=forms.NumberInput(attrs={'class': 'start-bid-field', 'autocomplete': 'off', 'step':'0.10', 'placeholder': 'Minimum RM 1.00'}))
    auction_end_time = forms.DateTimeField(label='End Time ', required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'auction-end-time-field'}))
    picture1 = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture2 = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture3 = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture4 = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture5 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture6 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture7 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))

    def clean_start_bid(self):
        start_bid = self.cleaned_data['start_bid']
        try:
            DecimalValidator(max_digits=10, decimal_places=2)(start_bid)
        except ValidationError:
            raise ValidationError('Starting bid must be a valid decimal number.')
        return start_bid
    
    def clean_auction_end_time(self):
        auction_end_time = self.cleaned_data.get('auction_end_time')
        if auction_end_time <= timezone.now():
            raise forms.ValidationError("Auction end time must be in the future.")
        return auction_end_time

class PlaceBidForm(forms.Form):
    bid_amount = forms.DecimalField(label='Bid Amount', min_value=0, max_digits=10, decimal_places=2, required=True)

class EditAuctionForm(forms.Form):
    item_name = forms.CharField(required=True, label='Item Name ', max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'item-name-field'}))
    item_desc = forms.CharField(required=True, label='Item Description ', max_length=200, widget=forms.Textarea(attrs={ 'class': 'item-desc-field'}))
    item_cat = forms.ChoiceField(required=True, label='Item Category ', choices=[('Apparel & Accessories', 'Apparel & Accessories'), ('Animal & Pet Supplies', 'Animal & Pet Supplies'),
                                                                                ('Arts & Entertainment', 'Arts & Entertainment'), ('Baby & Toddler', 'Baby & Toddler'),
                                                                                ('Camera & Optics', 'Camera & Optics'), ('Electronics', 'Electronics'), ('Food & Beverages', 'Food & Beverages'),
                                                                                ('Furniture', 'Furniture'), ('Hardware', 'Hardware'), ('Home & Garden', 'Home & Garden'), 
                                                                                ('Health & Beauty', 'Health & Beauty'), ('Luggage & Bags', 'Luggage & Bags'), ('Office Supplies', 'Office Supplies'),
                                                                                ('Religious', 'Religious'), ('Sporting Goods', 'Sporting Goods'), ('Toys & Games', 'Toys & Games'),
                                                                                ('Vehicle & Parts', 'Vehicle & Parts'), ('Others', 'Others')
                                                                                ], widget=forms.Select(attrs={ 'class': 'item-cat-field'}))
    start_bid = forms.DecimalField(required=True, label='Starting Bid ', max_digits=10, decimal_places=2, min_value=1,
                                   widget=forms.NumberInput(attrs={'class': 'start-bid-field', 'autocomplete': 'off', 'step':'0.10', 'placeholder': 'Minimum RM 1.00'}))
    auction_end_time = forms.DateTimeField(required=True, label='End Time ', widget=forms.DateTimeInput(attrs={'type': 'datetime-local',  'class': 'auction-end-time-field'}))
    picture1 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture4 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture5 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture6 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))
    picture7 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'picture-field'}))

    def clean_start_bid(self):
        start_bid = self.cleaned_data['start_bid']
        try:
            DecimalValidator(max_digits=10, decimal_places=2)(start_bid)
        except ValidationError:
            raise ValidationError('Starting bid must be a valid decimal number.')
        return start_bid
    
    def clean_auction_end_time(self):
        auction_end_time = self.cleaned_data.get('auction_end_time')
        if auction_end_time <= timezone.now():
            raise forms.ValidationError("Auction end time must be in the future.")
        return auction_end_time

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class CheckoutForm(forms.Form):
    buyer_name = forms.CharField(max_length=100, required=True ,label='Buyer Name', widget=forms.TextInput(attrs={'class': 'name-field'}))
    buyer_phone = forms.CharField(max_length=15, required=True, label='Buyer Phone Number', widget=forms.TextInput(attrs={'class': 'phoneNo-field'}))
    buyer_address = forms.CharField(required=True, label='Buyer Shipping Address', widget=forms.Textarea(attrs={'class': 'address-field'}))

class ReceiveForm(forms.Form):
    comment = forms.CharField(max_length=50, label='Comment', required=True, widget=forms.Textarea(attrs={'class': 'comment-field', 'autocomplete': 'off'}))
    ratings = forms.IntegerField(label='Ratings', min_value=1, max_value=5, required=True, widget=forms.NumberInput(attrs={'class': 'rating-field'}))

class ReportForm(forms.Form):
    category = forms.ChoiceField(label='Report Category ', required=True, choices=[('Fraud & Scam', 'Fraud & Scam'), ('Bugs Report', 'Bugs Report'),('Other', 'Other'),], widget=forms.Select(attrs={}))
    title = forms.CharField(label='Report Title ', required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'title-field', 'autocomplete': 'off'}))
    content = forms.CharField(label='Report Content ', required=True, widget=forms.Textarea(attrs={'class': 'content-field', 'autocomplete': 'off'}))