from django.shortcuts import render
import requests

def index(request):
  if request.method == 'POST':
    
    song_title = request.POST.get('song_title')
    
    api_key = 'Your Key'
    api_url = f'https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track={song_title}&apikey={api_key}'
    
    response = requests.get(api_url)
    print(response.json())
        # try:
        #     lyrics = data['message']['body']['lyrics']['lyrics_body']
        #     context = {
        #         'lyrics':lyrics
        #     }
        #     return render(request, 'index.html', context)
        # except KeyError as e:
        #     return render(request, 'error.html', {'error': f'{e} not found'})
  else:
    return render(request, 'index.html')
  return render(request, 'index.html')
