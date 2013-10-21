import fantasytopplayersparser as fp
han = """HAN FURY
1. 	(1) 	Kevin Durant (OKC - SF)
2. 	(28) 	Damian Lillard (Por - PG)
3. 	(29) 	DeMarcus Cousins (Sac - PF,C)
4. 	(56) 	Andre Drummond (Det - PF,C)
5. 	(57) 	Greivis Vasquez (Sac - PG,SG)
6. 	(84) 	Victor Oladipo (Orl - SG)
7. 	(85) 	Jimmy Butler (Chi - SG,SF)
8. 	(112) 	Vince Carter (Dal - SG,SF)
9. 	(113) 	Brandon Knight (Mil - PG,SG)
10. 	(140) 	Jarrett Jack (Cle - PG,SG)
11. 	(141) 	Jason Thompson (Sac - PF,C)
12. 	(168) 	Lou Williams (Atl - PG,SG)
13. 	(169) 	Alex Len (Pho - C)"""

def parselineup(lineup):
    lulist = []
    for line in lineup.split('\n'):
        try:
            lulist.append(fp.alphanumeric(line.split(')',1)[1].split('(')[0].strip()))
        except:
            print line + " not a player"
    return lulist
for i in fp.yahooranks:
    pass

for player in parselineup(han):
    try:
        print fp.aggregate[player]+1
        #print fp.yahooranks[fp.aggregate[player]]
    except:
        print player
