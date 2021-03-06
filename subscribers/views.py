from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, UpdateProfileForm, PasswordChangingForm
from blog.models import UserProfile


# View for changing user password

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

# View for creating a Userprofile if none exists

class CreateProfilePageView(CreateView):
    model = UserProfile
    fields = ('bio', 'website_url', 'instagram_url', 'twitter_url', 'linkedin_url')
    template_name = "registration/create_user_profile_page.html"
    success_url = reverse_lazy('home')
        #grab user when form is filled out and make this available to the form itself
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
# View for updating the User Profile ( Bio, Website etc)

class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'avatar', 'website_url', 'instagram_url', 'twitter_url', 'linkedin_url']
    success_url = reverse_lazy('home')


# View for ProfilePage

class ProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

 
class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')



# This class is for updating the user profile

class UserUpdateView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
