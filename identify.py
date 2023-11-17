#!/usr/bin/python3


prefix_names = {
    "Music_Prison_01": "Center Perks 2.0",
    "Music_Prison_02": "K.A.P.O.W Camp",
    "Music_Prison_03": "Rattlesnake Springs",
    "Music_Prison_04": "U.S.S Anomaly",
    "Music_Prison_05": "Fort Tundra",
    "Music_Prison_06": "The Glorious Regime",
    "Music_Prison_07": "H.M.P Offshore",
    "Music_Prison_08": "Area 17",
    "Music_Prison_DLC_05": "Dungeons & Duct Tape",
    "Music_Static_Transport_Boat": "H.M.S Orca",
    "Music_Static_Transport_Plane": "Air Force Con",
    "Music_Transport_Train": "Cougar Creek Railroad",
    "Prison_DLC_01": "Wicked Ward",
    "Prison_DLC_03": "Santa's Shakedown",
    "Prison_DLC_04": "Big Top Breakout",
    "Prison_Music_Tutorial": "Precinct 17",
    "Xmas_DLC": "Snow Way Out",

    # alt names
    "Area17": "Area 17",
    "Boat": "H.M.S Orca",
    "CenterPerks": "Center Perks 2.0",
    "Centre_Perks": "Center Perks 2.0",
    "DLC_03": "Santa's Shakedown",
    "DLC_04": "Big Top Breakout",
    "DLC_05": "Dungeons & Duct Tape",
    "Dictator": "The Glorious Regime",
    "Gulag": "Fort Tundra",
    "OilRig": "H.M.P Offshore",
    "Oil_Rig": "H.M.P Offshore",
    "OldWest": "Rattlesnake Springs",
    "Old_West": "Rattlesnake Springs",
    "POW": "K.A.P.O.W Camp",
    "Plane": "Air Force Con",
    "Space": "U.S.S Anomaly",
    "Train": "Cougar Creek Railroad",
}

# escape methods
sp_escapes = {
}
mp_escapes = {
}

# events & cutscenes
ecs = {
    "Showtime": "Big Top Breakout - Show Time",
}

routines = {
    "A": "Lights Out",
    "B": "Roll Call",
    "C": "Dining Time",
    "D": "Exercise Time",
    "E": "Shower Time",
    "F": "Job Time",
    "G": "Free Time",
    "H": "Show Time",
    "Amb": "Ambience",
    "Lockdown": "Lockdown",
    "Intro": "Introduction",
    "Part": "Part"
}

dines = {
    "Precinct 17": "Lunch Time",
    "Center Perks 2.0": "Breakfast,Lunch,Dinner",
    "Rattlesnake Springs": "Breakfast,Lunch,Dinner",
    "K.A.P.O.W Camp": "Breakfast,Dinner",
    "H.M.P Offshore": "Breakfast,Lunch",
    "Fort Tundra": "Breakfast,Dinner",
    "Area 17": "Breakfast Time",
    "U.S.S Anomaly": "Breakfast,Lunch,Dinner",
    "The Glorious Regime": "Breakfast,Lunch,Dinner",
    "Wicked Ward": "Breakfast,Dinner",
    "Big Top Breakout": "Breakfast,Dinner",
    "Santa's Shakedown": "Breakfast,Dinner",
    "Dungeons & Duct Tape": "Breakfast,Dinner",
    "Snow Way Out": "Breakfast,Dinner",
}


def identify_routine(strid):
    name = ""

    # Prison name
    for prefix, pname in prefix_names.items():
        if strid.startswith(prefix):
            name = pname
            strid = strid.removeprefix(prefix)
            strid = strid.lstrip("_")
            break
    else:
        return ""

    # Routine
    strid = strid.removeprefix("Routine")
    strid = strid.lstrip("_")
    for routine, rname in routines.items():
        if strid == routine or strid.startswith(routine + "_"):
            if routine == "C":
                rname = dines.get(pname, rname)
            name += " - " + rname
            strid = strid.removeprefix(routine)
            strid = strid.lstrip("_")
            strid = strid.removeprefix("Alt")
            strid = strid.lstrip("_")
            if routine == "Intro":
                return name
            elif routine == "Part":
                name += " " + strid
                return name
            else:
                break

    # Security level
    strid = strid.removeprefix("Level")
    strid = strid.lstrip("_")
    try:
        lvl = int(strid)
    except ValueError:
        lvl = None
    if lvl is not None:
        if lvl == 1:
            name += " (1 Star)"
        else:
            name += f" ({lvl} Stars)"
    return name


def identify_cutscene(strid):
    return ""


def identify_misc(strid):
    return ""


def identify(numid, strid):
    if strid == "?":
        return f"Unknown - {numid}"

    name = identify_routine(strid)
    if name != "":
        return name

    name = identify_cutscene(strid)
    if name != "":
        return name

    name = identify_misc(strid)
    if name != "":
        return name

    return "?"
