# usage: bash mux2.sh video.mp4 music.mp3 offset_seconds out.mp4
set -e
in="$1"; mu="$2"; off="$3"; out="$4"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$in"); F=$(python3 -I -c "print(max(0,$D-1.2))")
ffmpeg -nostdin -v error -y -i "$in" -ss "$off" -i "$mu" -filter_complex "[1:a]atrim=0:$D,afade=t=in:st=0:d=0.05,afade=t=out:st=$F:d=1.2,loudnorm=I=-14:TP=-1.5:LRA=11,asetpts=PTS-STARTPTS[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$out"
echo "$out ($D s)"
