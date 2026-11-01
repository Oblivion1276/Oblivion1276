"""Independent assertions for modular survivor enumeration."""
import sys,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from track_residues import test_residue,track

def direct(n,depth):
    x=n
    for _ in range(depth):
        x=(3*x+1)//2 if (x&1) else x//2
        if x<n:return False
    return True

def run():
    for t in range(1,11):
        m=1<<t
        for r in range(m):
            result,_,_=test_residue(r,t)
            assert result==direct(m+r,t)
            # Test uniform certificate across later members of same residue class.
            if not result:
                for j in [2,3,8,99]:assert not direct(r+j*m,t), (t,r,j)
    rows,edges,front=track(18,16)
    assert [r['unresolved_classes'] for r in rows]==[2114,4228,7495]
    assert all(x['max_residue_survives'] for x in rows)
    assert len(front)==7495
    # No fixed finite parity observation determines an ultimate result:
    # n=2^k-1 has first k odd operations (hence no first drop in k).
    for k in range(2,50):
        n=2**k-1;x=n
        for i in range(k):
            assert x&1
            x=(3*x+1)//2
            assert x>n
    print('PASS: brute-force equivalence, uniform certificates, 16-18 counts, long odd run')
if __name__=='__main__':run()