import requests

def get_lyrics_ovh(artist, title):
    base_url = "https://api.lyrics.ovh/v1/"
    query = f"{artist}/{title}"

    try:
        response = requests.get(base_url + query)
        response.raise_for_status()
        data = response.json()

        if "lyrics" in data:
            full_lyrics =  data["lyrics"]

            starting_phrase = f"Paroles de la chanson {title} par {artist}"

            # Check if the starting phrase is present
            if full_lyrics.startswith(starting_phrase):
                # Remove the starting phrase and any leading whitespace
                lyrics = full_lyrics[len(starting_phrase):].lstrip()
            else:
                lyrics = full_lyrics

            return lyrics
        else:
            return "Lyrics not found for the given song."

    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"

    except requests.exceptions.ConnectionError as errc:
        return f"Error connecting: {errc}"

    except requests.exceptions.RequestException as err:
        return f"Error: {err}"

    except Exception as e:
        return f"An error occurred: {e}"


def get_song_genius(lyrics):
    api_key = 'xBNaFrlPzGYJXnoL4aDMiKROqYkqHaWez6kq-UpRyxSTsdPiA4xYHpsxOzlwrxn3'

    url = 'https://api.genius.com/search'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    # Define the parameters for the search query
    params = {
        'q': lyrics
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()
        if 'response' in data and 'hits' in data['response']:
            # Get the song name and artist from the first result
            song_name = data['response']['hits'][0]['result']['title']
            artist_name = data['response']['hits'][0]['result']['primary_artist']['name']

            # Build the result string
            result_string = f'\nSong Name: {song_name},  \n Artist Name: {artist_name}'

            return result_string
        else:
            return 'No results found for the provided lyrics.'
    else:
        return f'Error making the API request. Status Code: {response.status_code}'
