from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustmUser
        fields = ('email' )