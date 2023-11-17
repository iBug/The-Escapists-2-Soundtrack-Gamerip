#!/bin/sh

cd "$(dirname "$0")"

SRC=wav
DST=mp3

for f in "$SRC"/*.wav; do
  id="$(basename -s .wav "$f")"
  #if [ "$id" -ne 984559894 ]; then continue; fi
  title="$(jq -r --arg id "$id" '.[] | select(.number == $id) | if .id == "?" or .name == "?" then ("Unidentified " + .number) else .name end' list.json)"
  echo "$id: $title"
  out="$DST/$id.mp3"
  ffmpeg -loglevel warning \
    -channel_layout stereo \
    -i "$f" \
    -i Cover.jpg \
    -map 0:0 \
    -map 1:0 \
    -c:a libmp3lame \
    -c:v copy \
    -id3v2_version 3 \
    -ab 256k \
    -metadata title="$title" \
    -metadata album="The Escapists 2" \
    -metadata artist="Team17" \
    -metadata album_artist="Team17" \
    -metadata date="2017" \
    -metadata track="$id" \
    -metadata:s:v title="Album cover" \
    -metadata:s:v comment="Cover (front)" \
    -y "$out"
done
