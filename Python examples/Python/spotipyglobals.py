import spotipy
import spotipy.util as util
import math
import Python.handledata as hd

ACID = hd.ACID()
ACSE = hd.ACSE()
USERNAME = hd.USERNAME()
token = util.prompt_for_user_token(USERNAME, scope="playlist-read-private playlist-read-collaborative user-library-read playlist-modify-private playlist-modify-public user-modify-playback-state user-read-playback-state user-read-currently-playing", client_id=f"{ACID}", client_secret=f"{ACSE}", redirect_uri="http://localhost:8080")
SP = spotipy.Spotify(auth=token)


def get_playlist_uri(playlist_name):
    npl = int(hd.n_playlists())
    if npl > 50:
        for n in range(math.ceil(npl/50)):
            playlists = SP.current_user_playlists(limit=50, offset=n*50)["items"]
            for playlist in playlists:
                if playlist["name"] == playlist_name:
                    return playlist["id"]
    else:    
        playlists = SP.current_user_playlists(limit=50, offset=0)["items"]
        for playlist in playlists:
            if playlist["name"] == playlist_name:
                return playlist["id"]


def get_playlist_uri_from_url(playlist_url):
    if "https://open.spotify.com/playlist/" in playlist_url:
        playlist_id = playlist_url.replace("https://open.spotify.com/playlist/", "")
        playlist_id = playlist_id.split("?")[0]
        return playlist_id
    elif "https://open.spotify.com/album/" in playlist_url:
        album_id = playlist_url.replace("https://open.spotify.com/album/", "")
        album_id = album_id.split("?")[0]
        return album_id
def user_display_name():
    user = SP.current_user()
    return user["display_name"]


