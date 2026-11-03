set -e
f="$1"; dur="$2"; w="${3:-4}"
n=$(python3 -I -c "print(int($dur*30))"); d="fr_$(basename "${f%.html}")"; q=$(( (n+w-1)/w ))
rm -rf "./$d"; mkdir "./$d"
for ((k=0;k<w;k++)); do a=$((k*q)); b=$(( (k+1)*q<n ? (k+1)*q : n )); if [ $a -lt $b ]; then node rend.js "$f" "$d" $a $b & fi; done; wait
c=$(ls "./$d" | wc -l); [ "$c" -eq "$n" ] || { echo "ERROR: rendered $c of $n frames"; exit 1; }
ffmpeg -nostdin -v error -y -framerate 30 -i "$d/%05d.jpg" -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -movflags +faststart "${f%.html}.mp4"
rm -rf "./$d"; echo "${f%.html}.mp4: $n frames"
