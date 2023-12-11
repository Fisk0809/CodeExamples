import spotipy
import spotipy.util as util
import Python.handledata as hd
import Python.readplaylist as rp
import Python.spotipyglobals as sg
import Python.modifyplaylist as mp
from spotipy.exceptions import SpotifyException

ACID = hd.ACID()
ACSE = hd.ACSE()
USERNAME = hd.USERNAME()
token = util.prompt_for_user_token(USERNAME, scope="playlist-read-private playlist-read-collaborative user-library-read playlist-modify-private playlist-modify-public user-modify-playback-state user-read-playback-state user-read-currently-playing", client_id=f"{ACID}", client_secret=f"{ACSE}", redirect_uri="http://localhost:8080")
SP = spotipy.Spotify(auth=token)

def loadpl(): 
    global pl_dict
    pl_dict = {}
    pl_dict["uk"] = hd.uk_pl()
    pl_dict["us"] = hd.us_pl()
    pl_dict["all"] = hd.uk_pl() + hd.us_pl() + ["ALL", "UK", "US"]
    
def jsync_pluri():
    for pl in pl_dict["all"]:
        hd.pl_uri(pl)
    
def addpl(name, group):
    if group.lower() == "uk":
        hd.add_ukpl(name)
        loadpl()   
    elif group.lower() == "us":
        hd.add_uspl(name)
        loadpl()

def jsync_all():   
    jsonsync("ALL")
    jsonsync("UK")
    jsonsync("US")
    pl_jsonsync("UK")
    pl_jsonsync("US")

def jsonsync(r):
    pl_tracks = rp.get_tracks(hd.pl_uri(r))
    hd.sync(r, pl_tracks)

def pl_jsonsync(r):
    pl_tracks_dict = {}
    r_pl = pl_dict[r.lower()]
    for pl in r_pl:
        pl_tracks = rp.get_tracks(hd.pl_uri(pl))
        pl_tracks_dict[pl] = pl_tracks   
    hd.sync_pl(r, pl_tracks_dict)
 
def all_sync():
    for r in ["UK", "US"]:
        add_tracks = []
        for track in hd.check_missing("ALL", r):
            add_tracks.append(track)
        mp.add_tracks_to_playlist("ALL", add_tracks)
         
def region_sync(r):
    for pl in pl_dict[r.lower()]:
        add_tracks = []
        for track in hd.check_missing(r.upper(),f"{r.upper()}/{pl}"):
            add_tracks.append(track)
        mp.add_tracks_to_playlist(r.upper(), add_tracks)

def artist_sync(r):
    for pl in pl_dict[r.lower()]:
        add_tracks = []
        for track in hd.check_missing_artist(r.upper(), f"{r.upper()}/{pl}"):
            add_tracks.append(track)
        mp.add_tracks_to_playlist(pl, add_tracks)
        for track in hd.check_missing_artist("ALL", f"{r.upper()}/{pl}"):
            add_tracks.append(track)
        mp.add_tracks_to_playlist(pl, add_tracks)
        # delete_tracks = []
        # for track in hd.get_tracks(f"{r.upper()}/{pl}"):
        #     if pl not in track["artists"]:
        #         delete_tracks.append(track["uri"])
        # if delete_tracks != []:
        #     SP.playlist_remove_all_occurrences_of_items(hd.pl_uri(pl), delete_tracks)
        #     pl_jsonsync(r.upper())
            
def newartist():
    q = input("What artist do you want to add? ")
    q2 = input("What group do you want to add them to? ")
    addpl(q, q2)
    SP.user_playlist_create(USERNAME, q, public=True)
    a_uri = rp.get_artist_uri(q)
    albums = SP.artist_albums(a_uri)
    add_tracks = []
    for item in albums["items"]:
        for track in rp.get_album_tracks(item["uri"])["tracks"]:
            if q in track["artists"]:
                add_tracks.append(track)
    for pl in [q, q2.upper(), "ALL"]:
        mp.add_tracks_to_playlist(pl, add_tracks)
        
def delete_duplicates():
    for pl in ["ALL", "UK", "US"]:
        add_tracks = []
        track_uris = []
        dupes = hd.check_duplicates(pl)
        if dupes != 0:
            for track in dupes:
                add_tracks.append(track)
                track_uris.append(track["uri"])
            SP.playlist_remove_all_occurrences_of_items(hd.pl_uri(pl), track_uris)
            mp.add_tracks_to_playlist(pl, add_tracks, bypass=True)
    for r in ["us", "uk"]:
        for pl in pl_dict[r]:
            add_tracks = []
            track_uris = []
            dupes = hd.check_duplicates(f"{r.upper()}/{pl}")
            if dupes != 0:
                for track in dupes:
                    add_tracks.append(track)
                    track_uris.append(track["uri"])
                SP.playlist_remove_all_occurrences_of_items(hd.pl_uri(pl), track_uris)
                mp.add_tracks_to_playlist(pl, add_tracks, bypass=True)

def refresh_artist(a):
    a_uri = rp.get_artist_uri(a)
    albums = SP.artist_albums(a_uri)
    add_tracks = []
    for item in albums["items"]:
        for track in rp.get_album_tracks(item["uri"])["tracks"]:
            if a in track["artists"]:
                add_tracks.append(track)
    mp.add_tracks_to_playlist(a, add_tracks)
    if a in pl_dict["uk"]:
        mp.add_tracks_to_playlist("UK", add_tracks)
    if a in pl_dict["us"]:
        mp.add_tracks_to_playlist("US", add_tracks)
    mp.add_tracks_to_playlist("ALL", add_tracks)
    
def main():
    loadpl()
    jsync_all()
    artist_sync("uk")
    artist_sync("us")
    region_sync("uk")
    region_sync("us")
    all_sync()
    # delete_duplicates()
    # newartist()
    # refresh_artist(input("What artist do you want to refresh? "))
        
if __name__ == '__main__':
    main()

