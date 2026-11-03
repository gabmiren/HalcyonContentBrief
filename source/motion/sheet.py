import sys, subprocess, numpy as np
from PIL import Image, ImageDraw
v, out = sys.argv[1], sys.argv[2]; args = sys.argv[3:]
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",v],capture_output=True,text=True).stdout)
if args and args[0] == "--around": ts = sorted({round(c+k/10,2) for c in map(float,args[1:]) for k in range(-5,6) if 0 <= c+k/10 < dur}); cols = 11
else:
    fps = float(args[0]) if args else 2; cols = int(args[1]) if len(args) > 1 else 10
    ts = [round(i/fps,2) for i in range(int(dur*fps))]
w, h = 216, 384; rows = (len(ts)+cols-1)//cols; sh = Image.new("RGB",(cols*w,rows*(h+20)),"#05080A"); d = ImageDraw.Draw(sh)
for i,t in enumerate(ts):
    raw = subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",str(t),"-i",v,"-frames:v","1","-vf",f"scale={w}:{h}","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    if len(raw) == w*h*3:
        x, y = (i%cols)*w, (i//cols)*(h+20); sh.paste(Image.fromarray(np.frombuffer(raw,np.uint8).reshape(h,w,3)),(x,y+20)); d.text((x+4,y+4),f"{t:.2f}",fill="#E4E6E6")
sh.save(out, quality=85); print(out, len(ts), "frames")
