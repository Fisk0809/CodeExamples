import spotipy
import spotipy.util as util
import math
import Python.readplaylist as rp
import Python.spotipyglobals as sg
import Python.handledata as hd

ACID = hd.ACID()
ACSE = hd.ACSE()
USERNAME = hd.USERNAME()
token = util.prompt_for_user_token(USERNAME, scope="playlist-read-private playlist-read-collaborative user-library-read playlist-modify-private playlist-modify-public user-modify-playback-state user-read-playback-state user-read-currently-playing", client_id=f"{ACID}", client_secret=f"{ACSE}", redirect_uri="http://localhost:8080")
SP = spotipy.Spotify(auth=token)

def add_tracks_to_playlist(add_playlist, tracks, bypass=False):
    if bypass == False:
        add_songs = []
        pl_uri = hd.pl_uri(add_playlist)
        # Checks for existing tracks in the json file
        if add_playlist in hd.uk_pl():
            pljson = f"UK/{add_playlist}"
        elif add_playlist in hd.us_pl():
            pljson = f"US/{add_playlist}"
        else:
            pljson = add_playlist
        c_tracks = hd.check_if_exists(pljson, tracks)
        track_amount = len(c_tracks)
        # After checking for json position and checking if tracks exist, add the tracks to the json file
        hd.json_add(pljson, c_tracks)
        # Then adds the tracks to the playlist using a method that bypasses the 100 track limit
        if track_amount > 100:
            for i in range(track_amount):
                i+=1
                track = c_tracks.pop()
                add_songs.append(track["uri"])
                if len(add_songs) == 100:
                    SP.playlist_add_items(pl_uri, add_songs)
                    add_songs = []
            SP.playlist_add_items(pl_uri, add_songs)
        elif track_amount != 0:
            for track in c_tracks:
                add_songs.append(track["uri"])
            SP.playlist_add_items(pl_uri, add_songs)
    elif bypass == True:
        add_songs = []
        c_tracks = tracks
        pl_uri = hd.pl_uri(add_playlist)
        track_amount = len(c_tracks)
        if track_amount > 100:
            for i in range(track_amount):
                i+=1
                track = c_tracks.pop()
                add_songs.append(track["uri"])
                if len(add_songs) == 100:
                    SP.playlist_add_items(pl_uri, add_songs)
                    add_songs = []
            SP.playlist_add_items(pl_uri, add_songs)
        elif track_amount != 0:
            for track in c_tracks:
                add_songs.append(track["uri"])
            SP.playlist_add_items(pl_uri, add_songs)
        