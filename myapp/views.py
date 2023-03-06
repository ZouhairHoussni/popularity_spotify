import spotipy,requests,json
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
from .forms import MyForm
from django.contrib.auth.decorators import login_required
import pandas as pd


client_id = '120557cf599b4583ba030aeebcd698f0'
client_secret = '11ddae906f5540eebd84044d3f2975bb'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


audio_features = [
  'duration_ms',
  'danceability',
  'energy',
  'loudness',
  'speechiness',
  'acousticness',
  'instrumentalness',
  'liveness',
  'valence',
  'tempo'
  
  ]

feature = ['artist']

def get_audio_features(query):
    results = sp.search(q = query, type = 'track')
    track_uri = results['tracks']['items'][0]['uri']
   
   
    track_features = sp.audio_features(track_uri)
 
    df = pd.DataFrame(track_features, columns = audio_features)

   
  
    return df

@login_required
def my_view(request):
    
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            

            text = form.cleaned_data['chanson'].capitalize()

            carac = get_audio_features(text)
            carac = carac.to_dict()
            carac = list(carac.values())
            valeurs = [value for d in carac for value in d.values()]
            artist = sp.search(q=f'track:{text}',type='track', limit=1)['tracks']['items'][0]['album']['artists'][0]['name']
            response = requests.get(f"https://spotifast.onrender.com/predict/?duration_ms={valeurs[0]}&danceability={valeurs[1]}&energy={valeurs[2]}&loudness={valeurs[3]}&speechiness={valeurs[4]}&acousticness={valeurs[5]}&instrumentalness={valeurs[6]}&liveness={valeurs[7]}&valence={valeurs[8]}&tempo={valeurs[9]}")
            results = json.loads(response.text)
            results = int(results['Class'])
            
            my_model = form.save(commit=False) 
            my_model.user = request.user 
            username = request.user 
            my_model.save()
            

            return render(request, 'popularity.html', {'text':text,'results': results,'username':username,'artist':artist})
    else:
        username = str(request.user).capitalize()
        form = MyForm(request.POST)
    return render(request, 'welcome.html', {'form': form,'username':username})