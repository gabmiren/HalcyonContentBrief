from PIL import Image, ImageDraw
import glob,os,sys
pref=sys.argv[1].split(','); out=sys.argv[2]
ns=[n for n in sorted(glob.glob('img/*.png')) if os.path.basename(n).split('_')[0].rstrip('.png')[:2] in pref or os.path.basename(n)[:3] in pref]
W=432;H=540;cols=6;rows=(len(ns)+cols-1)//cols
sh=Image.new('RGB',(W*cols,(H+22)*rows),'#444');d=ImageDraw.Draw(sh)
for i,n in enumerate(ns):
    im=Image.open(n).convert('RGB'); im=im.resize((int(im.width*H/im.height),H))
    x=(i%cols)*W;y=(i//cols)*(H+22); sh.paste(im,(x,y)); d.text((x+4,y+H+4),os.path.basename(n),fill='white')
sh.save(out,quality=84); print(len(ns))
