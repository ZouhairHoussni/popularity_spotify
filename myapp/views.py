import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
from .forms import MyForm
from django.contrib.auth.decorators import login_required

client_id = '120557cf599b4583ba030aeebcd698f0'
client_secret = '11ddae906f5540eebd84044d3f2975bb'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@login_required
def my_view(request):
    
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            

            text = form.cleaned_data['chanson'].capitalize()
            my_model = form.save(commit=False) 
            my_model.user = request.user 
            username = request.user 
            my_model.save()
            results = sp.search(q=f'track:{text}',type='track', limit=1)['tracks']['items'][0]['album']['artists'][0]['name']
            print(username)

            return render(request, 'popularity.html', {'text':text,'results': results,'username':username})
    else:
        username = str(request.user).capitalize()
        form = MyForm(request.POST)
    return render(request, 'welcome.html', {'form': form,'username':username})