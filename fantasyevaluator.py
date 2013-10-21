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
12. 	(168) 	Louis Williams (Atl - PG,SG)
13. 	(169) 	Alex Len (Pho - C)"""
fw = """Fungal Wang
1. 	(7) 	Stephen Curry (GS - PG,SG)
2. 	(22) 	Larry Sanders (Mil - PF,C)
3. 	(35) 	Josh Smith (Det - SF,PF)
4. 	(50) 	Jeff Teague (Atl - PG)
5. 	(63) 	Jonas Valanciunas (Tor - C)
6. 	(78) 	Amir Johnson (Tor - PF,C)
7. 	(91) 	Jameer Nelson (Orl - PG)
8. 	(106) 	DeAndre Jordan (LAC - C)
9. 	(119) 	Jamal Crawford (LAC - PG,SG)
10. 	(134) 	Arron Afflalo (Orl - SG,SF)
11. 	(147) 	Bismack Biyombo (Cha - C)
12. 	(162) 	Randy Foye (Den - PG,SG)
13. 	(175) 	Mario Chalmers (Mia - PG)"""
my="""My Team
1. 	(8) 	Kyrie Irving (Cle - PG)
2. 	(21) 	Dwyane Wade (Mia - PG,SG)
3. 	(36) 	Chris Bosh (Mia - PF,C)
4. 	(49) 	Tim Duncan (SA - PF,C)
5. 	(64) 	David West (Ind - PF)
6. 	(77) 	Ersan Ilyasova (Mil - SF,PF)
7. 	(92) 	Goran Dragic (Pho - PG)
8. 	(105) 	Danny Granger (Ind - SF)
9. 	(120) 	Andrew Bogut (GS - C)
10. 	(133) 	Gerald Wallace (Bos - SF,PF)
11. 	(148) 	Amar'e Stoudemire (NY - PF,C)
12. 	(161) 	Michael Carter-Williams (Phi - PG)
13. 	(176) 	Patrick Beverley (Hou - PG)"""
r = fp.ranker()
r.get_yahoo_ranks_from_espn(fp.yahoo,fp.espn)

def parselineup(lineup):
    """from string (from
    http://basketball.fantasysports.yahoo.com/nba/46428/draftresults?drafttab=team
    to list of the player names."""
    lulist = []
    for line in lineup.split('\n'):
        try:
            lulist.append(fp.alphanumeric(line.split(')',1)[1].split('(')[0].strip()))
        except:
            print line + " not a player"
    return lulist
for i in r.yahooranks:
    pass
    #print i

def excel_it_up(lineup):
    """takes a list of player names and prints out, line-by-line, the row in excel
    in which they show up.  The +1 is because I use the first row in excel as column
    labels."""
    for player in parselineup(lineup):
        try:
            print r.aggregate[player]+1
            #print r.yahooranks[r.aggregate[player]]
        except:
            print player

excel_it_up(my)
