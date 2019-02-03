from django.contrib.auth.forms import UserCreationForm


class SignupFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email')

