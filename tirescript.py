#This is a simple depreciation calculator for use in racing simulations
#Users will note their tire % after 1 lap of testing, this lets us anticipate
#how much any given tire will degrade in one lap.
#From there the depreciation is calculated. 



sst=100     #Set tire life to 100%
st=100
mt=100
ht=100


print("when entering degredation use X.XX format")  

#Have the user enter their degredation figures after test laps

laps = int(input("How many laps to show?"))
ss = float(input("What is the degredation on SuperSoft tires?"))
s = float(input("on Softs?"))
m = float(input("on Medium?"))
h = float(input("on Hards?"))

laps += 1

print("Here's your expected tire life after each lap")

lapcount = 1

while laps > 1:
    ssdeg = sst * ss
    sst = sst - ssdeg

    sdeg = st * s
    st = st - sdeg

    mdeg = mt * m
    mt = mt - mdeg

    hdeg = ht * h
    ht = ht - hdeg


    

    

    print("AFTER LAP: {:<5}   SST:{:<5}   ST:{:<5}   MT:{:<5}   HT:{:<5}".format(lapcount, round(sst, 1), round(st, 1), round(mt, 1),  round(ht, 1)))
    laps -= 1
    lapcount += 1
