import json,glob,os,re,sys
pre=sys.argv[1] if len(sys.argv)>1 else 'base'
tot_bad=0
for f in sorted(glob.glob(f'/root/htf-motion/pacing/{pre}_*.json')):
    J=json.load(open(f)); rows=J['rows'] if isinstance(J,dict) else J; dur=J.get('dur',0) if isinstance(J,dict) else 0
    rows=[r for r in rows if not (r['dwell']<=0.25 and re.search(r'\d',r['tx']))]  # counter frames mid-count
    rows=[r for r in rows if not r['tx'].startswith(('Halcyon offers','Rewards are paid'))]
    
    for r in rows: r['need']=round(max(1.0,0.6+0.32*r['words']),2); r['ok']=r['dwell']>=r['need']
    bad=[r for r in rows if not r['ok']]; tot_bad+=len(bad)
    print(f"== {os.path.basename(f)[len(pre)+1:-5]} ({dur:.1f}s): {len(rows)} text blocks, {len(bad)} below reading time")
    for r in bad: print(f"   {r['dwell']:5.2f}s / need {r['need']:.2f}  @{r['from']:5.2f}  {r['tx'][:62]}")
print("TOTAL below:", tot_bad)
