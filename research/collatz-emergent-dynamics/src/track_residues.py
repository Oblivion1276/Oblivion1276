#!/usr/bin/env python3
"""Exact integer enumeration of 'no first drop within k' residue classes.
One representative n=2**k+r suffices for all n>=2**k in class r mod 2**k.
"""
from pathlib import Path
import csv,json,math,argparse,random

def test_residue(r,k):
    n=(1<<k)+r; x=n; a=0; B=0; first_drop=None
    for j in range(1,k+1):
        if x&1:
            x=(3*x+1)//2
            B=3*B+(1<<(j-1));a+=1
        else:x//=2
        assert (3**a*n+B)==(1<<j)*x
        if x<n:
            assert 3**a<(1<<j)
            assert (3**a-(1<<j))*n+B<0
            first_drop=j
            break
    return first_drop is None,a,B

def track(max_depth=32,base_depth=16):
    frontier=[]
    for r in range(1<<base_depth):
        still,_,_=test_residue(r,base_depth)
        if still:frontier.append(r)
    assert len(frontier)==2114, f'expected 2114 at depth16, got {len(frontier)}'
    rows=[];transition=[]
    for t in range(base_depth,max_depth+1):
        modulus=1<<t
        # Due to inheritance of certificates, candidates are exactly children of previous frontiers.
        if t>base_depth:
            prev=frontier;delta=modulus//2
            next_frontier=[];children=[0,0,0]
            for r in prev:
                s0,_,_=test_residue(r,t)
                s1,_,_=test_residue(r+delta,t)
                nchild=int(s0)+int(s1);children[nchild]+=1
                if s0:next_frontier.append(r)
                if s1:next_frontier.append(r+delta)
            frontier=next_frontier
            transition.append({'depth':t,'previous_frontier':len(prev),'zero_children':children[0],'one_child':children[1],'two_children':children[2],'next_frontier':len(frontier)})
        a_list=[test_residue(r,t)[1] for r in frontier] if t<=20 else []
        rows.append({'depth':t,'modulus':modulus,'unresolved_classes':len(frontier),'certified_classes':modulus-len(frontier),'unresolved_fraction':len(frontier)/modulus,'survivors_odd':sum(r&1 for r in frontier),'survivors_mod3_0':sum(r%3==0 for r in frontier),'survivors_mod3_1':sum(r%3==1 for r in frontier),'survivors_mod3_2':sum(r%3==2 for r in frontier),'min_a':min(a_list) if a_list else None,'max_a':max(a_list) if a_list else None,'mean_a':sum(a_list)/len(a_list) if a_list else None,'max_residue_survives':int(modulus-1 in frontier)})
        print('level',t,'unresolved',len(frontier),'share',f'{len(frontier)/modulus:.10f}',flush=True)
    return rows,transition,frontier

if __name__=='__main__':
    arg=argparse.ArgumentParser();arg.add_argument('--max-depth',type=int,default=24);arg.add_argument('--out',default=str(Path(__file__).resolve().parents[1]/'data'));opts=arg.parse_args()
    target=Path(opts.out);target.mkdir(exist_ok=True,parents=True)
    rows,trans,front=track(opts.max_depth)
    for name,records in [('residue_levels.csv',rows),('residue_transitions.csv',trans)]:
        with (target/name).open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    (target/'residue_frontier_sample.json').write_text(json.dumps({'max_depth':opts.max_depth,'count':len(front),'first_100':front[:100],'last_100':front[-100:]},indent=2))