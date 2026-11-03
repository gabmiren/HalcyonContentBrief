import cv2,numpy as np,subprocess,sys
SRC='/mnt/user-data/uploads/2f5b26bb-output.mp4'
tex=cv2.imread('/tmp/gj/screen.png').astype(np.float32)
TW,TH=tex.shape[1],tex.shape[0]
H,W=1280,720
XL,XR=242.0,716.0
xs,ys=np.meshgrid(np.arange(W,dtype=np.float32),np.arange(H,dtype=np.float32))
yt=356.0+(xs-280)*0.006; yb=589.0+(xs-400)*0.067
u=(xs-XL)/(XR-XL)*TW; v=(ys-yt)/(yb-yt)*TH
# anti-aliased polygon coverage (1px ramps)
cov=np.clip(xs-XL+0.5,0,1)*np.clip(ys-yt+0.5,0,1)*np.clip(yb-ys+0.5,0,1)
# screen look: soft focus, glow, lifted blacks, like a lit monitor filmed on a phone
warp=cv2.remap(tex,u,v,cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT,borderValue=(0,0,0))
warp=cv2.GaussianBlur(warp,(0,0),1.0)
glow=cv2.GaussianBlur(warp,(0,0),6)
warp=np.clip(warp*0.88+glow*0.28+10,0,255)
rng=np.random.default_rng(3)
out=subprocess.Popen(['ffmpeg','-nostdin','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','24','-i','-','-i',SRC,'-map','0:v','-map','1:a?','-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-c:a','copy','-shortest','-movflags','+faststart',sys.argv[1]],stdin=subprocess.PIPE)
cap=cv2.VideoCapture(SRC);i=0
while True:
  ok,f=cap.read()
  if not ok:break
  m=np.zeros((H,W),np.float32);mt=cv2.imread(f'/tmp/gj/mattes/{i:04d}.png',0)
  if mt is not None:m[200:760,100:720]=mt.astype(np.float32)/255
  m=cv2.GaussianBlur(m,(0,0),0.8)
  a=(cov*(1-m))[...,None]
  n=rng.normal(0,2.2,(H,W,1)).astype(np.float32)
  o=f.astype(np.float32)*(1-a)+(warp+n)*a
  out.stdin.write(np.clip(o,0,255).astype(np.uint8).tobytes());i+=1
out.stdin.close();out.wait();print('frames',i)
