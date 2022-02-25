#Question 1

'''
Here we have 3 pegs namely A, B, C and we want all the disk to be transferred to disk C from A.
n is the number of disk.
Here A is starting point, B is auxillary and C is the final peg.
'''

def towerofhanoi(n,start,extra,end):
    if n>0:
        towerofhanoi (n-1,start,end,extra)
        print("Transfer disk from",start,"to",end)
        towerofhanoi (n-1,extra,start,end)
        
towerofhanoi(3,"A","B","C")
