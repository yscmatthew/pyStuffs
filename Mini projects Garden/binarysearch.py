def binary_search(num, lo, hi):
 trial = 1
 lo=1
 hi=100
 while(lo<=hi):
    ges = int((hi+lo)/2)
    if ges == num :
        return (ges, trial)
    elif (ges < num ):
        lo = ges + 1
    else:
        hi = ges - 1
    trial=trial+1
 print(trial, ges)
 return(-2, trial)

input=int()

