import cv2,numpy as np,subprocess,sys,os
from PIL import Image
SRC='/mnt/user-data/uploads/02685a37-snaptik_7651965178908560662_v3.mp4'
N=int(sys.argv[2]) if len(sys.argv)>2 else 1395
frames=[int(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else None
S=1080/576
cap=cv2.VideoCapture(SRC);last=None
_c=cv2.VideoCapture(SRC);[_c.read() for _ in range(11)];CLEAN11=_c.read()[1]
def key_caption(f):
    band=f[282:328,:].copy();band[:,:50]=0;band[:,526:]=0;hsv=cv2.cvtColor(band,cv2.COLOR_BGR2HSV)
    m=((hsv[...,2]>228)&(hsv[...,1]<45)).astype(np.uint8)*255
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(m)
    keep=np.zeros_like(m)
    for k in range(1,n):
        x,y,w,h,a=st[k]
        if h>=9 and w<=80 and a>=12: keep[lab==k]=255
    m=keep
    m=cv2.resize(m,(1080,int(46*S)),interpolation=cv2.INTER_LINEAR)
    return m
def build(i,f):
    out=np.zeros((1920,1080,3),np.uint8)
    chart=f[356:1024,:];chart=cv2.resize(chart,(1080,1920-668),interpolation=cv2.INTER_CUBIC)
    out[668:]=chart
    m=key_caption(f).astype(np.float32)/255;h=m.shape[0];y0=668-h//2
    st=cv2.dilate(m,np.ones((9,9),np.uint8));st=cv2.GaussianBlur(st,(0,0),2)
    reg=out[y0:y0+h].astype(np.float32)
    reg=reg*(1-st[...,None]*0.9)
    reg=reg*(1-m[...,None])+255*m[...,None]
    ui_path=f'/root/htf-motion/live/ui/{i:05d}.png'
    ui=cv2.imread(ui_path,cv2.IMREAD_UNCHANGED)
    o=out.astype(np.float32)
    if ui is not None:
        a=ui[...,3:4].astype(np.float32)/255;o=o*(1-a)+ui[...,:3].astype(np.float32)*a
    o[y0:y0+h]=o[y0:y0+h]*0+0  # placeholder replaced below
    # caption drawn on top of UI so it sits over the seam
    base=o[y0:y0+h]
    return o,y0,h,m,st
i=0
pipe=None
if not frames:
    pipe=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r','30','-i','-','-i',SRC,'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-af','apad','-t',str(N/30),'-movflags','+faststart',sys.argv[1]],stdin=subprocess.PIPE)
while i<N:
    ok,f=cap.read()
    if ok: last=f
    else: f=last
    if frames is None or i in frames:
        out=np.zeros((1920,1080,3),np.float32)
        src=(CLEAN11 if i<11 else f)[356:1024,:];lab=cv2.cvtColor(src,cv2.COLOR_BGR2LAB);lab[...,0]=(18+(255-lab[...,0].astype(np.float32))*0.86).astype(np.uint8);src=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
        z=1.03+0.025*np.sin(i/30*0.35);H0,W0=src.shape[:2];cw,ch=int(W0/z),int(H0/z);x0=int((W0-cw)*(0.5+0.3*np.sin(i/30*0.21)));y0c=(H0-ch)//2;src=src[y0c:y0c+ch,x0:x0+cw]
        chart=cv2.resize(src,(1080,1252),interpolation=cv2.INTER_CUBIC).astype(np.float32);out[668:]=chart
        import os
        pth=f'/root/htf-motion/live/ui/{i:05d}.png'
        ui=np.array(Image.open(pth).convert('RGBA'))[...,[2,1,0,3]] if os.path.exists(pth) else None
        if ui is not None:
            a=ui[...,3:4].astype(np.float32)/255;out=out*(1-a)+ui[...,:3].astype(np.float32)*a
        if ok and i>=78:
            m=key_caption(f).astype(np.float32)/255;h=m.shape[0];y0=598-h//2
            st=cv2.GaussianBlur(cv2.dilate(m,np.ones((9,9),np.uint8)),(0,0),2)
            r=out[y0:y0+h];r=r*(1-st[...,None]*0.85);r=r*(1-m[...,None])+255*m[...,None];out[y0:y0+h]=r
        o=np.clip(out,0,255).astype(np.uint8)
        if pipe: pipe.stdin.write(o.tobytes())
        else: cv2.imwrite(f'/tmp/lc/test_{i}.jpg',o)
    i+=1
if pipe: pipe.stdin.close();pipe.wait()
print('done')
