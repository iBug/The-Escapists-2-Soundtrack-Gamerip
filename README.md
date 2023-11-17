# The-Escapists-2-Soundtrack-Gamerip

Scripts and some intermediate files for ripping soundtrack from The Escapists 2 (2017).

This is intended for research purposes only. To download the actual soundtrack, please head over to [Video Game Music](https://downloads.khinsider.com/game-soundtracks/album/the-escapists-2-gamerip) website.

## Description

I ripped and converted this album from the Windows (Steam) version of the game.

All the game resources used in ripping come from `The Escapists 2\TheEscapists2_Data\StreamingAssets\Audio\GeneratedSoundBanks\Windows` (hereinafter referred to as the "assets directory). The entire assets directory is copied onto a Linux machine, and the whole work is done under Linux environment.

Directories `assets/`, `mp3/`, `wav/`, `The Escapists 2/` should be created in advance. `Cover.jpg` should be fetched beforehand. Details are given below.

-   `db.txt` is a mapping from the numeric file names to a sort of in-game string IDs. It is gathered from `.txt` files from the assets directory:

    ```shell
    awk '{print $1, $2}' assets/*.txt | sort | uniq > db.txt
    ```

    Then I manually removed header-like lines and kept only lines with a number followed by a string ID.

    These `.txt`, `.json` and `.xml` files do not seem to be used by the game, but rather left over by the music composer (Oli Wood). Thanks Oli, these files are *essential* for sorting out the tracks.

-   `ref.csv` comes from a previous attempt to sort things out. It is produced with a previous version of `identify.py`, with every single line manually reviewed and fixed. Some manual interventions include:

    -   `Music_Prison_01_Routine_E` has three copies for each level ([Security Level](https://theescapists.fandom.com/wiki/Security_Level)). It seems like Routine F and Routine G are mis-tagged as Routine E in the game files.
    -   Various escape methods are uniquely named, and writing code to process them requires quite some effort, so I'd rather review them manually.
    -   Many tags aren't named consistently. There's no one-scheme-fits-all identifying method.

-   `list.csv` and `list.json` are produced by `python3 sort.py` (requires Python 3.9+).
-   `.wem` files from the assets directory is processed by [`vgmstream-cli`](https://github.com/vgmstream/vgmstream), and the output is written in the `wav/` directory.
-   `Cover.jpg` is downloaded from Spotify: <https://i.scdn.co/image/ab67616d0000b273934b320729ac82f6c91ba4e0>
-   `ffmpeg.sh` reads `list.json` and converts eacv `.wav` file into `.mp3` inside the `mp3/` directory. It also adds some metadata, including `Cover.jpg` as the album cover.

    The original `.wem` files are already lossy-compressed with Vorbis to around 250 kbps, so it makes little sense to produce 320 kbps MP3. I opted for 256 kbps instead.

-   `rename.py` create symlinks in `The Escapists 2/` that links back to files in `mp3/` directory. I don't like moving files around so I chose symlinking.
-   Finally, `zip -9r 'The Escapists 2.zip' 'The Escapists 2' Cover.jpg` packs the selected subset of properly identified soundtracks into a package that you can distribute. Since `zip` follows symlinks by default, it will pack up the actual MP3 files.

This is about as far as I've got to restore the soundtrack to a reasonably consumable state, with all files well-named and well-tagged. The final archive includes 656 tracks, all of which can be categorized as "music" rather than "ambient sound" or "SFX".

The rest of the tracks are really messy. For example, if you sort `db.txt` by the second column, a lot of ambient sounds and SFXs are duplicated. There are 60 tracks tagged as `Volume_Down`, and over 200 untagged tracks. Among the untagged tracks, most are duplicate versions of tracks from Center Perks 2.0, Couger Creek Railroad, H.M.S Orca and Air Force Con.

Most of these should be of no interest to music collectors, so I decided not to waste my effort on them. There *might* be a small number of tracks that are noteworthy. For example, tracks 40263129, 527107076, 996158410, 544524851, 884059560 and 485943432 (all 2:18 in length) appear to compose into an unused or cut routine in Rattlesnake Springs (or a cut map), being the 0-star to 5-star music for this routine, respectively. See `ref.csv` for an incomplete attempt to make sense of these unlabeled tracks.

I left this repository here in case someone in the future may be interested.
