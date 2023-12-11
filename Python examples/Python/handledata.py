import json, time
json_path = "json/"

def ACID():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        cfg.close()
        acid = data["acid"]
        return acid      
    except:
        try:
            file = open(json_path + "config.json", "r")
            data = json.load(file)
            print(data)
            print("Error: ACID not found in config.json")
            acid = input("Write ACID here: ")
            file.close()
            file = open(json_path + "config.json", "w")
            data["acid"] = acid
            json.dump(data, file, indent=4)
            file.close()
            ACID() 
        except:
            print("Error: ACID not found in config.json")
            acid = input("Write ACID here: ")
            newData = f'"acid": "{acid}"'
            newData = '{' + newData + '}'
            file = open(json_path + "config.json", "w")
            file.write(newData)
            file.close()
            ACID()

def ACSE():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        cfg.close()
        acse = data["acse"]
        return acse
        
    except:
        try:
            file = open(json_path + "config.json", "r")
            data = json.load(file)
            print(data)
            print("Error: ACSE not found in config.json")
            acse = input("Write ACSE here: ")
            file.close()
            file = open(json_path + "config.json", "w")
            data["acse"] = acse
            json.dump(data, file, indent=4)
            file.close()
            ACSE() 
        except:
            print("Error: ACSE not found in config.json")
            acse = input("Write acse here: ")
            newData = f'"acse": "{acse}"'
            newData = '{' + newData + '}'
            file = open(json_path + "config.json", "w")
            file.write(newData)
            file.close()
            ACSE()

def n_playlists():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        cfg.close()
        npl = data["npl"]
        return npl
        
    except:
        try:
            file = open(json_path + "config.json", "r")
            data = json.load(file)
            print(data)
            print("Error: NPL not found in config.json")
            npl = input("Write NPL here: ")
            file.close()
            file = open(json_path + "config.json", "w")
            data["npl"] = npl
            json.dump(data, file, indent=4)
            file.close()
            n_playlists() 
        except:
            print("Error: NPL not found in config.json")
            npl = input("Write NPL here: ")
            newData = f'"npl": "{npl}"'
            newData = '{' + newData + '}'
            file = open(json_path + "config.json", "w")
            file.write(newData)
            file.close()
            n_playlists()
    
def USERNAME():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        cfg.close()
        username = data["username"]
        return username
        
    except:
        try:
            file = open(json_path + "config.json", "r")
            data = json.load(file)
            print(data)
            print("Error: Username not found in config.json")
            username = input("Write Username here: ")
            file.close()
            file = open(json_path + "config.json", "w")
            data["username"] = username
            json.dump(data, file, indent=4)
            file.close()
            USERNAME() 
        except:
            print("Error: Username not found in config.json")
            username = input("Write username here: ")
            newData = f'"username": "{username}"'
            newData = '{' + newData + '}'
            file = open(json_path + "config.json", "w")
            data.append(newData)
            file.write(data)
            file.close()
            USERNAME()

def uk_pl():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        uklists = data["uk_playlists"]
        return uklists
    except:
        print("Error: UK playlists not found in config.json")
        uklists = input("Write UK playlists here: ")
        uklists = uklists.split(", ")
        file = open(json_path + "config.json", "r")
        data = json.load(file)
        file.close()
        data["uk_playlists"] = uklists
        file = open(json_path + "config.json", "w")
        json.dump(data, file, indent=4)
        file.close()
        uk_pl()
        
def us_pl():
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        uslists = data["us_playlists"]
        return uslists
    except:
        print("Error: US playlists not found in config.json")
        uslists = input("Write US playlists here: ")
        uslists = uslists.split(", ")
        file = open(json_path + "config.json", "r")
        data = json.load(file)
        file.close()
        data["us_playlists"] = uslists
        file = open(json_path + "config.json", "w")
        json.dump(data, file, indent=4)
        file.close()
        us_pl()        

def add_ukpl(name):
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        uklists = data[f"uk_playlists"]
        uklistslower = [list.lower() for list in uklists]
        npl = data["npl"]
        npl = int(npl) + 1
        data["npl"] = npl
        newpl = name
        if newpl.lower() in uklistslower:
            print("Error: Playlist already in UK playlists")
        else:
            uklists.append(newpl)
            cfg = open(json_path + "config.json", "w")
            data["uk_playlists"] = uklists
            json.dump(data, cfg, indent=4)
            cfg.close()
            file = open(json_path + f"UK/" + f"{name}.json", "x")
            file.close()
    except:
        print("Error: UK playlists not found in config.json")
        uklists = input("Write UK playlists here: ")
        uklists = uklists.split(", ")
        file = open(json_path + "config.json", "r")
        data = json.load(file)
        file.close()
        data["uk_playlists"] = uklists
        file = open(json_path + "config.json", "w")
        json.dump(data, file, indent=4)
        file.close()
        uk_pl()

def add_uspl(name):
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        cfg.close()
        uslists = data["us_playlists"]
        uslistslower = [list.lower() for list in uslists]
        npl = data["npl"]
        npl = int(npl) + 1
        data["npl"] = npl
        newpl = name
        if newpl.lower() in uslistslower:
            print("Error: Playlist already in US playlists")
        else:
            uslists.append(newpl)
            cfg = open(json_path + "config.json", "w")
            data["us_playlists"] = uslists
            json.dump(data, cfg, indent=4)
            cfg.close()
            file = open(json_path + f"US/" + f"{name}.json", "x")
            file.close()
    except:
        print("Error: US playlists not found in config.json")
        uslists = input("Write US playlists here: ")
        uslists = uslists.split(", ")
        file = open(json_path + "config.json", "r")
        data = json.load(file)
        file.close()
        data["us_playlists"] = uslists
        file = open(json_path + "config.json", "w")
        json.dump(data, file, indent=4)
        file.close()
        us_pl()

def add_pl(*args):
    try:
        cfg = open(json_path + "config.json")
        data = json.load(cfg)
        uslists = data["us_playlists"]
        uslistslower = [list.lower() for list in uslists]
        newpl = input("Write new US playlist here: ")
        if newpl.lower() in uslistslower:
            print("Error: Playlist already in US playlists")
        else:
            uslists.append(newpl)
    except:
        print("Error: US playlists not found in config.json")
        uslists = input("Write US playlists here: ")
        uslists = uslists.split(", ")
        file = open(json_path + "config.json", "r")
        data = json.load(file)
        file.close()
        data["us_playlists"] = uslists
        file = open(json_path + "config.json", "w")
        json.dump(data, file, indent=4)
        file.close()
        us_pl()
        
def get_tracks(pl):
    file = open(json_path + f"{pl}.json", "r")
    data = json.load(file)["tracks"]
    file.close()
    return data
       
def sync_all(tracks_info):
    try:
        file = open(json_path + "ALL.json", "w")
        json.dump(tracks_info, file, indent=4)
        file.close()
    except:
        file = open(json_path + "ALL.json", "x")
        file.close()
        file = open(json_path + "ALL.json", "w")
        json.dump([], file, indent=4)
        file.close()
    
def sync_uk(tracks_info):
    try:
        file = open(json_path + "UK.json", "w")
        json.dump(tracks_info, file, indent=4)
        file.close()
    except:
        file = open(json_path + "UK.json", "x")
        file.close()
        file = open(json_path + "UK.json", "w")
        json.dump([], file, indent=4)
        file.close()
    
def sync_us(tracks_info):
    try:
        file = open(json_path + "US.json", "w")
        json.dump(tracks_info, file, indent=4)
        file.close()
    except:
        file = open(json_path + "US.json", "x")
        file.close()
        file = open(json_path + "US.json", "w")
        json.dump([], file, indent=4)
        file.close()    
    
def sync(r ,tracks_info):
    try:    
        file = open(json_path + f"{r}.json", "w")
        json.dump(tracks_info, file, indent=4)
        file.close()
    except:
        file = open(json_path + f"{r}.json", "x")
        file.close()
        file = open(json_path + f"{r}.json", "w")
        json.dump([], file, indent=4)
        file.close()
    
def sync_pl(r, tracks_info):
    for pl in tracks_info:
        try:
            file = open(json_path + f"{r}/" + f"{pl}.json", "w")
            json.dump(tracks_info[pl], file, indent=4)
            file.close()
        except:
            file = open(json_path + f"{r}/" + f"{pl}.json", "x")
            file.close()
            file = open(json_path + f"{r}/" + f"{pl}.json", "w")
            json.dump([], file, indent=4)
            file.close()
    
def check_missing(pl1, pl2):
    missing_tracks = []
    pl1_file = open(json_path + f"{pl1}.json", "r")
    pl2_file = open(json_path + f"{pl2}.json", "r")
    pl1_tracks = json.load(pl1_file)["tracks"]
    pl2_tracks = json.load(pl2_file)["tracks"]
    for track in pl2_tracks:
        if track not in pl1_tracks:
            missing_tracks.append(track)
    return missing_tracks

def check_missing_artist(pl1, pl2):
    missing_tracks = []
    artist_name = str(pl2).split("/")[1]
    pl1_file = open(json_path + f"{pl1}.json", "r")
    pl2_file = open(json_path + f"{pl2}.json", "r")
    pl1_tracks = json.load(pl1_file)["tracks"]
    pl2_tracks = json.load(pl2_file)["tracks"]
    for track in pl1_tracks:
        if artist_name in track["artists"]:
            if track not in pl2_tracks:
                missing_tracks.append(track)
    return missing_tracks

def json_add(pl, tracks):
    try: 
        file = open(json_path + f"{pl}.json", "r")
        data = json.load(file)["tracks"]
        data.extend(tracks)
        data = {"tracks": data}
        file.close()
        file = open(json_path + f"{pl}.json", "w")
        json.dump(data, file, indent=4)
        file.close()
    except:
        file = open(json_path + f"{pl}.json", "w")
        json.dump(tracks, file, indent=4)
        file.close()

def check_duplicates(pl):
    duplicates = []
    file = open(json_path + f"{pl}.json", "r")
    data = json.load(file)
    pl_tracks = data["tracks"]
    file.close()
    for track in pl_tracks:
        if pl_tracks.count(track) > 1:
            if track not in duplicates:
                duplicates.append(track)
                pl_tracks.remove(track)
    file = open(json_path + f"{pl}.json", "w")
    data["tracks"] = pl_tracks
    json.dump(data, file, indent=4)
    return duplicates

def check_if_exists(pl, tracks):
    try:
        missing_tracks = []
        file = open(json_path + f"{pl}.json", "r")
        pl_tracks = json.load(file)["tracks"]
        file.close()
        for track in tracks:
            if track not in pl_tracks:
                missing_tracks.append(track)
        return missing_tracks
    except:
        return tracks

def pl_uri(pl): 
    import Python.spotipyglobals as sg
    try:
        file = open(json_path + f"pl_uri.json", "r")
        data = json.load(file)
        file.close()
        uri = data[pl]
        return uri
    except:
        try:
            file = open(json_path + f"pl_uri.json", "r")
            data = json.load(file)
            file.close()
            uri = sg.get_playlist_uri(pl)
            data[pl] = uri
            file = open(json_path + f"pl_uri.json", "w")
            json.dump(data, file, indent=4)
            file.close()
            return uri
        except:
            print("Error: File not found")
            file = open(json_path + "pl_uri.json", "x")
            uri = sg.get_playlist_uri(pl)
            newData = f'"{pl}": "{uri}"'
            newData = '{' + newData + '}'
            file = open(json_path + "pl_uri.json", "w")
            file.write(newData)
            file.close()
            return uri      