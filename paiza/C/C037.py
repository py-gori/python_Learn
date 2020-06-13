t = input()

MM = int(t[:2])
DD = int(t[3:5])
hh = int(t[6:8])
mm = int(t[9:])

if hh >= 24:
    add_DD = hh // 24
    DD += add_DD
    hh %= 24

MM = str(MM).zfill(2)
DD = str(DD).zfill(2)
hh = str(hh).zfill(2)
mm = str(mm).zfill(2)

print(MM+"/"+DD,hh+":"+mm)