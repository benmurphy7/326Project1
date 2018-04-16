from django.shortcuts import render, redirect
from django.views import generic
from .models import Mix, Profile, Follows
from django.forms.models import model_to_dict
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.text import slugify
from datetime import timedelta

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.
class MixView(generic.DetailView):
    model = Mix
    template_name = 'mix_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(MixView, self).get_context_data(**kwargs)
        playlist = []
        for member in context['mix'].playlistmembership_set.select_related().prefetch_related().all():
            playlist.append({
                'id': member.track.id,
                'title': member.track.title,
                'extra_info': member.track.extra_info or '',
                'artist': member.track.artist,
                'time': member.time.total_seconds(),
                'time_str': str(member.time),
                'links': [model_to_dict(link, fields=('provider', 'url')) for link in member.track.links.all()]
            })
        context['playlist'] = playlist
        return context

class LogInView(generic.TemplateView):
    template_name = 'login_signup.html'

class EditMixView(generic.DetailView):
    model = Mix
    template_name = 'editor_edit.html'
    
class UploadMixView(generic.TemplateView):
    template_name = 'editor_upload.html'

# New upload views here
from .forms import UploadMixModelForm
class CreateMixView(generic.CreateView):
    model = Mix
    template_name = 'mix_upload.html'
    fields = ('title', 'audio_file')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.uploader = self.request.user.profile
        form.instance.length = timedelta()
        return super(CreateMixView, self).form_valid(form)


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profile_template.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['follows'] = Follows.objects.filter(owner__user=self.kwargs['pk'])
        bfollows = []
        for rel in Follows.objects.filter(follows__user=self.kwargs['pk']):
            bfollows.append(rel.owner)
        context['bfollows'] = bfollows
        context['mixs'] = Mix.objects.filter(uploader__user=self.kwargs['pk'])
        return context
	
class MainPageView(generic.TemplateView):
    #model = Mix
    template_name = 'main_page.html' #fill this
    
    def get_context_data(self, **kwargs):
     
     model = Mix   
     context = super(MainPageView, self).get_context_data(**kwargs)
     context['mixes'] = Mix.objects.all()[:3]
     return context    
	
class ChartsView(generic.ListView):
    model = Mix
    template_name = 'charts_template.html'
    queryset = Mix.objects.order_by('-play_count')

class EditProfileView(generic.TemplateView):
    model = Profile
    template_name = 'edit_profile.html'

def follow(request, profile_id):
    user = request.user.profile
    profile = Profile.objects.get(id=profile_id)
    f = Follows(owner=user, follows=profile)
    f.save()
    return redirect("/profile/"+profile_id)

def unfollow(request, profile_id):
    user = request.user.profile
    profile = Profile.objects.get(id=profile_id)
    Follows.objects.filter(owner=user, follows=profile).delete()
    return redirect("/profile/"+profile_id)