# app.py

from flask import Flask, render_template, request
from SongFinder import get_lyrics_ovh, get_song_genius

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_form():
    if request.method == 'POST':
        artist = request.form.get('artist')
        title = request.form.get('title')
        lyric = request.form.get('lyric')

        if artist and title:
            # Use the function to get lyrics
            lyrics = get_lyrics_ovh(artist, title)
            return render_template("index.html", artist=artist, title=title, lyrics=lyrics)

        elif lyric:
            # Use the function to get song info
            info = get_song_genius(lyric)
            return render_template("index.html", info=info)

    # If no valid form data, render the template without results
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
