import spotipy
import spotipy.util as util
import math
import Python.spotipyglobals as sg
import Python.handledata as hd

ACID = hd.ACID()
ACSE = hd.ACSE()
USERNAME = hd.USERNAME()
token = util.prompt_for_user_token(USERNAME, scope="playlist-read-private playlist-read-collaborative user-library-read playlist-modify-private playlist-modify-public user-modify-playback-state user-read-playback-state user-read-currently-playing", client_id=f"{ACID}", client_secret=f"{ACSE}", redirect_uri="http://localhost:8080")
SP = spotipy.Spotify(auth=token)

def get_artist_uri(name):
    result = SP.search(q=f"artist:{name}", type="artist")        
    for artist in result["artists"]["items"]:
        if artist["name"].lower() == f"{name.lower()}":
            if artist["followers"]["total"] > 10000:
                return artist["uri"]

def get_tracks(playlist):
    global track_name
    global i
    i = 0
    full_track_info = []
    while True:
        offset_number = i * 100
        i += 1
        for track in SP.playlist_tracks(playlist, None, 100, offset_number)["items"]:
            track_artists = []
            for artist in track["track"]["artists"]:
                track_artists.append(artist["name"])
            track_uri = track["track"]["uri"]
            track_name = track["track"]["name"]
            track_info = {"uri": track_uri, "name": track_name, "artists": track_artists}
            full_track_info.append(track_info)
        if len(SP.playlist_tracks(playlist, None, 100, offset_number)["items"]) < 100:
            tracks = {'tracks': full_track_info}
            return tracks


def get_album_tracks(playlist):
    global track_name
    global i
    i = 0
    full_track_info = []
    while True:
        offset_number = i * 50
        i += 1
        for track in SP.album_tracks(playlist, 50, offset_number)["items"]:
            track_artists = []
            for artist in track["artists"]:
                track_artists.append(artist["name"])
            track_uri = track["uri"]
            track_name = track["name"]
            track_info = {"uri": track_uri, "name": track_name, "artists": track_artists}
            full_track_info.append(track_info)
        if len(SP.album_tracks(playlist, 50, offset_number)["items"]) < 50:
            tracks = {'tracks': full_track_info}
            return tracks


def get_artist_tracks(artist_name, target_playlist):
    all_tracks = get_tracks(target_playlist)["tracks"]
    artist_tracks = []
    for track in all_tracks:
        if artist_name in track["artists"]:
            artist_tracks.append(track)
    return artist_tracks

def get_track_uri(tracks):
    track_uris = []
    all_tracks = tracks["tracks"]
    for track in all_tracks:
        track_uris.append(track["uri"])
    return track_uris
        
def check_if_exists(track_uris, og_playlist):
    playlist_tracks = get_tracks(og_playlist)["tracks"]
    playlist_tracks_uri = []
    unique_tracks = []
    for track in playlist_tracks:
        playlist_tracks_uri.append(track["uri"])
    for element in track_uris:
        if element not in playlist_tracks_uri:
            unique_tracks.append(element)
    return unique_tracks
            
     
    