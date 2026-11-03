import sys, subprocess, numpy as np
f = sys.argv[1]; endc = float(sys.argv[2]) if len(sys.argv) > 2 else 1e9
W, H, fps = 108, 192, 30
raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", f, "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32); n = len(fr)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2)); detail = fr.std(axis=(1, 2))
print(f"{f}: {n} frames, {n/fps:.2f}s"); issues = 0
frozen = d < 0.15; i = 0
while i < len(frozen):
    if frozen[i]:
        j = i
        while j < len(frozen) and frozen[j]: j += 1
        if j - i >= 10 and i / fps < endc: print(f"  FROZEN {i/fps:.2f}-{j/fps:.2f}s ({(j-i)/fps:.2f}s)"); issues += 1
        i = j
    else: i += 1
for k in range(n):
    if detail[k] < 6 and k / fps > 0.3:
        print(f"  EMPTY-ish frame {k/fps:.2f}s (std {detail[k]:.1f})"); issues += 1
        if issues > 40: break
cuts = [k + 1 for k in range(len(d)) if d[k] > 18]
print("  cuts/flashes at:", ", ".join(f"{c/fps:.2f}" for c in cuts) or "none")
print("  OK" if issues == 0 else f"  {issues} issue(s)")
