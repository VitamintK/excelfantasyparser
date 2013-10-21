import re
yahoo ="""1. Kevin Durant
    2. LeBron James
    3. James Harden
    4. Chris Paul
    5. Stephen Curry
    6. Kyrie Irving
    7. Kevin Love
    8. Paul George
    9. Carmelo Anthony
    10. Marc Gasol
    11. LaMarcus Aldridge
    12. Al Jefferson
    13. Deron Williams
    14. Derrick Rose
    15. Anthony Davis
    16. Al Horford
    17. Serge Ibaka
    18. Nicolas Batum
    19. John Wall
    20. Ricky Rubio
    21. Dwyane Wade
    22. Dirk Nowitzki
    23. Kawhi Leonard
    24. Larry Sanders
    25. Nikola Vucevic
    26. Rudy Gay
    27. Mike Conley
    28. Pau Gasol
    29. Joakim Noah
    30. Tim Duncan
    31. Chris Bosh
    32. Brook Lopez
    33. Ty Lawson
    34. Tony Parker
    35. Russell Westbrook
    36. Paul Millsap
    37. Damian Lillard
    38. Josh Smith
    39. Kemba Walker
    40. Monta Ellis
    41. Brandon Jennings
    42. DeMarcus Cousins
    43. Dwight Howard
    44. Kobe Bryant
    45. Ersan Ilyasova
    46. Eric Bledsoe
    47. Roy Hibbert
    48. David Lee
    49. Blake Griffin
    50. David West
    51. Nikola Pekovic
    52. Klay Thompson
    53. Andrew Bynum
    54. Thaddeus Young
    55. Jeff Teague
    56. Jose Calderon
    57. Chandler Parsons
    58. Ryan Anderson
    59. George Hill
    60. Derrick Favors
    61. Jrue Holiday
    62. Goran Dragic
    63. Rajon Rondo
    64. Jeff Green
    65. Kyle Lowry
    66. Bradley Beal
    67. Wesley Matthews
    68. Tyson Chandler
    69. Enes Kanter
    70. Andre Iguodala
    71. Greg Monroe
    72. Kevin Garnett
    73. Jonas Valanciunas
    74. Amir Johnson
    75. Marcin Gortat
    76. Jeremy Lin
    77. Steve Nash
    78. Tyreke Evans
    79. Eric Gordon
    80. Luol Deng
    81. Raymond Felton
    82. Zach Randolph
    83. J.R. Smith
    84. Kevin Martin
    85. O.J. Mayo
    86. Kenneth Faried
    87. Paul Pierce
    88. Jameer Nelson
    89. Tobias Harris
    90. Carlos Boozer
    91. Gerald Henderson
    92. Greivis Vasquez
    93. Gordon Hayward
    94. Jimmy Butler
    95. Andre Drummond
    96. JaVale McGee
    97. Danny Green
    98. DeMar DeRozan
    99. Trey Burke
    100. Joe Johnson
    101. Evan Turner
    102. Manu Ginobili
    103. Marcus Thornton
    104. Andrew Bogut
    105. Wilson Chandler
    106. Dion Waiters
    107. Amar'e Stoudemire
    108. Kyle Korver
    109. Tiago Splitter
    110. Danny Granger
    111. Nene Hilario
    112. Andrei Kirilenko
    113. Jamal Crawford
    114. Harrison Barnes
    115. Robin Lopez
    116. Gerald Wallace
    117. Avery Bradley
    118. Arron Afflalo
    119. Anderson Varejao
    120. Spencer Hawes
    121. Michael Carter-Williams
    122. Ben McLemore
    123. J.J. Redick
    124. Omer Asik
    125. Brandon Knight
    126. Maurice Harkless
    127. Shawn Marion
    128. Lou Williams
    129. Anthony Bennett
    130. Cody Zeller
    131. Otto Porter Jr.
    132. Ray Allen
    133. Victor Oladipo
    134. Alex Len
    135. Emeka Okafor
    136. Kelly Olynyk
    137. Rodney Stuckey
    138. Samuel Dalembert
    139. Chris Kaman
    140. Mario Chalmers
    141. Jared Dudley
    142. DeAndre Jordan
    143. Michael Kidd-Gilchrist
    144. Tristan Thompson
    145. Kris Humphries
    146. Andrea Bargnani
    147. Randy Foye
    148. Tony Allen
    149. Lance Stephenson
    150. Kentavious Caldwell-Pope"""

espn = """Kevin Durant, OKC SF [Recent News] 
LeBron James, Mia SF
James Harden, Hou SG [Recent News] 
Chris Paul, LAC PG [Recent News] 
Stephen Curry, GS PG, SG
Kevin Love, Min PF
Kyrie Irving, Cle PG [Recent News] 
Marc Gasol, Mem C
Paul George, Ind SF, SG  DTD [Breaking News] 
Carmelo Anthony, NY SF [Breaking News] 
Deron Williams*, Bkn PG  O [Breaking News] 
Serge Ibaka, OKC PF, C [Recent News] 
Nicolas Batum, Por SF, SG [Breaking News] 
Dirk Nowitzki, Dal PF [Recent News] 
Dwyane Wade, Mia SG [Recent News] 
LaMarcus Aldridge, Por PF, C  DTD [Breaking News] 
Al Jefferson*, Cha C  O [Recent News] 
Derrick Rose, Chi PG [Breaking News] 
John Wall, Wsh PG [Breaking News] 
Ricky Rubio, Min PG
Josh Smith, Det SF, PF [Breaking News] 
Damian Lillard, Por PG [Breaking News] 
Joakim Noah*, Chi C  O [Breaking News] 
Al Horford, Atl C [Breaking News] 
Ty Lawson, Den PG [Breaking News] 
Anthony Davis, Nor C, PF [Recent News] 
Brandon Jennings*, Det PG  O [Recent News] 
Jrue Holiday, Nor PG [Breaking News] 
David Lee, GS PF, C [Recent News] 
Tony Parker, SA PG [Recent News] 
Dwight Howard, Hou C [Recent News] 
Blake Griffin, LAC PF [Breaking News] 
Mike Conley, Mem PG [Recent News] 
Rudy Gay, Tor SF
Ersan Ilyasova*, Mil PF, SF  O [Breaking News] 
Kemba Walker, Cha PG [Breaking News] 
Larry Sanders, Mil C, PF  DTD [Breaking News] 
Brook Lopez, Bkn C [Breaking News] 
Greg Monroe, Det PF, C [Breaking News] 
Klay Thompson, GS SG, SF [Breaking News] 
Monta Ellis, Dal PG, SG [Recent News] 
DeMarcus Cousins, Sac C, PF [Breaking News] 
Chris Bosh, Mia C, PF [Breaking News] 
J.R. Smith*, NY SG  O [Breaking News] 
Roy Hibbert, Ind C [Breaking News] 
Tim Duncan, SA PF, C
Paul Pierce, Bkn SF [Breaking News] 
Kobe Bryant*, LAL SG, SF  O [Recent News] 
Nikola Vucevic, Orl C, PF [Breaking News] 
Ryan Anderson, Nor PF
Kawhi Leonard, SA SF, SG [Recent News] 
Thaddeus Young, Phi SF
Paul Millsap, Atl PF [Breaking News] 
David West, Ind PF [Breaking News] 
Goran Dragic, Pho PG [Breaking News] 
Tyreke Evans, Nor SF, SG  DTD [Breaking News] 
Jeff Teague, Atl PG [Breaking News] 
Jeff Green, Bos SF
Zach Randolph, Mem PF [Recent News] 
Pau Gasol, LAL PF, C [Breaking News] 
Derrick Favors, Uta PF, C [Breaking News] 
Bradley Beal, Wsh SG [Breaking News] 
George Hill, Ind PG  DTD [Breaking News] 
Luol Deng, Chi SF [Breaking News] 
Andre Iguodala, GS SF, SG [Breaking News] 
Russell Westbrook*, OKC PG  O
Tobias Harris*, Orl PF, SF  O [Breaking News] 
Kenneth Faried*, Den PF  O [Breaking News] 
Andre Drummond, Det C, PF [Breaking News] 
Wesley Matthews*, Por SG, SF  O [Breaking News] 
JaVale McGee, Den C [Recent News] 
Danny Granger, Ind SG, SF  DTD [Breaking News] 
Jose Calderon, Dal PG  DTD [Recent News] 
Steve Nash, LAL PG [Recent News] 
Greivis Vasquez, Sac PG [Breaking News] 
Eric Bledsoe, Pho PG, SG [Breaking News] 
Jeremy Lin*, Hou PG  O [Breaking News] 
O.J. Mayo, Mil SG
Isaiah Thomas, Sac PG [Recent News] 
Jonas Valanciunas, Tor C [Recent News] 
Nikola Pekovic, Min C
Jameer Nelson, Orl PG [Recent News] 
Kevin Garnett, Bkn PF [Recent News] 
Danny Green, SA SG, SF [Breaking News] 
Rajon Rondo*, Bos PG  O
Victor Oladipo, Orl SG, PG
Kyle Lowry, Tor PG
Chandler Parsons, Hou SF [Recent News] 
Maurice Harkless, Orl SF [Recent News] 
Jamal Crawford, LAC SG, PG [Breaking News] 
Gordon Hayward, Uta SG, SF [Breaking News] 
Trey Burke, Uta PG
Omer Asik, Hou C  DTD [Breaking News] 
Andrew Bogut, GS C  DTD [Breaking News] 
Gerald Wallace, Bos SF [Recent News] 
Evan Turner, Phi SG [Recent News] 
Joe Johnson, Bkn SG
Raymond Felton, NY PG
Tyson Chandler, NY C
Louis Williams*, Atl PG  O
Cody Zeller, Cha PF, C
Eric Gordon, Nor SG [Breaking News] 
Marcin Gortat, Pho C [Recent News] 
Jimmy Butler*, Chi SG  O [Breaking News] 
Amar'e Stoudemire*, NY PF  O [Breaking News] 
Ben McLemore, Sac SG
Wilson Chandler, Den SF, SG  DTD [Recent News] 
Carlos Boozer, Chi PF
Tristan Thompson, Cle PF
Anderson Varejao, Cle C [Recent News] 
Harrison Barnes, GS SF  DTD [Breaking News] 
Gerald Henderson, Cha SG [Recent News] 
Andrei Kirilenko*, Bkn SF  O [Breaking News] 
Kevin Martin, Min SG  DTD [Breaking News] 
Jarrett Jack*, Cle PG  O [Recent News] 
Jarrett Jack*, Cle PG  O [Recent News] 
Danilo Gallinari*, Den SF, PF  O
Nate Robinson, Den PG, SG  DTD [Breaking News] 
DeMar DeRozan, Tor SG
Derrick Williams, Min PF, SF
Markieff Morris, Pho PF [Breaking News] 
Nene Hilario , Wsh PF, C  DTD [Breaking News] 
J.J. Redick*, LAC SG  O
Brandon Knight, Mil PG [Recent News] 
Spencer Hawes, Phi C
Shawn Marion, Dal SF, PF [Recent News] 
Michael Carter-Williams, Phi PG
J.J. Hickson, Den PF, C [Recent News] 
Iman Shumpert, NY SG, PG  DTD [Breaking News] 
Dion Waiters, Cle SG  DTD [Breaking News] 
Amir Johnson, Tor PF
Arron Afflalo, Orl SG [Recent News] 
Emeka Okafor*, Wsh C  O
Manu Ginobili, SA SG [Breaking News] 
Andrew Bynum*, Cle C  O [Breaking News] 
Kris Humphries, Bos PF  DTD [Breaking News] 
Andrea Bargnani, NY PF [Breaking News] 
Mario Chalmers, Mia PG [Breaking News] 
Andre Miller, Den PG
Jordan Crawford, Bos SG [Recent News] 
Reggie Jackson, OKC PG [Breaking News] 
Carlos Delfino*, Mil SF  O
Michael Kidd-Gilchrist, Cha SF
Brandan Wright*, Dal PF, C  O [Recent News] 
Chris Kaman, LAL C  DTD
Tiago Splitter, SA PF, C [Recent News] 
Vince Carter, Dal SG, SF [Recent News] 
Patrick Beverley, Hou PG
Alex Len, Pho C
Jerryd Bayless, Mem PG, SG
Anthony Bennett, Cle PF
Otto Porter Jr., Wsh SF
Glen Davis*, Orl PF  O
Nick Young, LAL SG
Alec Burks, Uta SG [Recent News] 
Steve Blake, LAL PG [Recent News] 
Mo Williams, Por PG, SG
Trevor Ariza, Wsh SF
Caron Butler, Mil SF
Matt Barnes, LAC SF  DTD [Breaking News]"""

def alphanumeric(word):
    """cleans everything except letters and numbers and commas and single quotes."""
    return re.sub(r'[^a-zA-Z0-9,\']', '', word)

aggregate = {}
yahooranks = []
i=0
for line in yahoo.split('\n'):
    i+=1
    aggregate[alphanumeric(line.split('.',1)[1])] = i

i=0
for line in espn.split('\n'):
    i+=1
    try:
        yahooranks.append(aggregate[alphanumeric(line.split(',')[0])])
    except:
        yahooranks.append(0)
        #print alphanumeric(line.split(',')[0])
        print i
    
#for i in yahooranks: print i
for i in range(0,160):
    if i not in yahooranks:
        print i
