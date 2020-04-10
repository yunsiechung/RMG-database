name = "Polycyclic Ring Corrections" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
	 index = -1,
	 label = "PolycyclicRing",
	     group = 
"""
1 * R u0
""",
	 solute = None, 
	 shortDesc = u"""""",
	 longDesc = 
u"""
""",
)
entry(
    index = 92,
    label = "s2_5_6_ane",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    solute = SoluteData(
        S = 0.19942981915931557,
        B = 0.0661572278213485,
        E = 0.0893706760166258,
        L = 0.26404532721994356,
        A = -0.036472194215326166,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 165,
    label = "s3_6_6_ane",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
    solute = SoluteData(
        S = -0.013811390856633096,
        B = 0.0018015905215462468,
        E = 0.0313768518111198,
        L = 0.020674752133393544,
        A = -0.016848865679248544,
    ),
    )


entry(
    index = 0,
    label = "s3_6_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 118,
    label = "s2_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {5,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = 0.08807756374369172,
        B = 0.0544704874073458,
        E = 0.04145443596784021,
        L = 0.17813902699645123,
        A = 0.03962044772451053,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 64,
    label = "s2_3_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
""",
    solute = SoluteData(
        S = -0.07801252124892458,
        B = 0.0021453199045756203,
        E = -0.013906893106564044,
        L = -0.057319863120549125,
        A = -0.0032936762383791334,
    ),
    )


entry(
    index = 0,
    label = "s2_3_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 75,
    label = "s2_4_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    solute = SoluteData(
        S = 0.0022646584430432003,
        B = 0.03723118341981192,
        E = 0.0885511326751626,
        L = -0.017057894899937046,
        A = -0.05254838869124103,
    ),
    )


entry(
    index = 0,
    label = "s2_4_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 61,
    label = "s2_3_4_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
""",
    solute = SoluteData(
        S = -0.053750010478910586,
        B = -0.005250665147425808,
        E = -0.06674972442090786,
        L = -0.2756697707355932,
        A = 0.016604742821778914,
    ),
    )


entry(
    index = 0,
    label = "s2_3_4",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 80,
    label = "s2_5_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,S} {6,S}
""",
    solute = SoluteData(
        S = -0.03918826512637675,
        B = -0.013679657777804022,
        E = 0.08330411549749688,
        L = -0.0618845939221756,
        A = -0.0015006798690503803,
    ),
    )


entry(
    index = 0,
    label = "s2_5_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 157,
    label = "s3_5_5_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {6,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7   R!H u0 {2,S} {5,S}
""",
    solute = SoluteData(
        S = -0.10424678092222482,
        B = 1.7287558128153858e-05,
        E = 0.02989423222868996,
        L = -0.30811365332837676,
        A = -0.058921323038027495,
    ),
    )


entry(
    index = 0,
    label = "s3_5_5",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 82,
    label = "s2_5_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3 * R!H u0 {2,S} {7,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,S} {6,S}
""",
    solute = SoluteData(
        S = 0.08641573515186794,
        B = -0.03589806019304251,
        E = -0.13551767267670284,
        L = -0.046719245576176516,
        A = -0.016177678500561274,
    ),
    )


entry(
    index = 0,
    label = "s2_5_5_ene",
    group = 'OR{s2_5_5_ene_0, s2_5_5_ene_1}',
    solute = None,
)


entry(
    index = 158,
    label = "s3_5_5_ene_1",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {2,S} {6,D}
""",
    solute = SoluteData(
        S = 0.014900403911631247,
        B = -0.0071828926279024355,
        E = 0.04568912501700342,
        L = -0.22211510614469035,
        A = -0.004435072752521641,
    ),
    )


entry(
    index = 0,
    label = "s3_5_5_ene",
    group = 'OR{s3_5_5_ene_1, s3_5_5_ene_side}',
    solute = None,
)


entry(
    index = 160,
    label = "s3_5_5_diene_1_4",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {6,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {4,D}
7   R!H u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = -0.00686134333213668,
        B = -0.006918292834673363,
        E = 0.0030427107815164858,
        L = 0.07253269296624318,
        A = -0.0028350898987698513,
    ),
    )


entry(
    index = 0,
    label = "s3_5_5_diene",
    group = 'OR{s3_5_5_diene_1_4}',
    solute = None,
)


entry(
    index = 66,
    label = "s2_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    solute = SoluteData(
        S = 0.048438812584516384,
        B = -0.011115230134277641,
        E = 0.0016361993354880838,
        L = 0.08907333886326274,
        A = 0.0038301560653560673,
    ),
    )


entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 121,
    label = "s2_6_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {6,S} {10,D}
10   R!H u0 {3,S} {9,D}
""",
    solute = SoluteData(
        S = -0.059273474040690985,
        B = 0.07621604016535762,
        E = 0.04262904464263959,
        L = 0.375229625856438,
        A = 0.1463111276830388,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ene",
    group = 'OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}',
    solute = None,
)


entry(
    index = 131,
    label = "s2_6_6_diene_0_8",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {9,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,D} {9,S}
""",
    solute = SoluteData(
        S = 0.09567310145761708,
        B = 0.013297141460243368,
        E = 0.009874296007581114,
        L = 0.19222319171403998,
        A = -0.014514585074627979,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_diene",
    group = 'OR{s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_5, s2_6_6_diene_0_6, s2_6_6_diene_0_8, s2_6_6_diene_1_6, s2_6_6_diene_1_7}',
    solute = None,
)


entry(
    index = 185,
    label = "s2_6_6_ben",
    group = 
"""
1    R!H u0 {2,B} {3,B} {5,S}
2    R!H u0 {1,B} {4,B} {6,S}
3    R!H u0 {1,B} {7,B}
4    R!H u0 {2,B} {9,B}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {3,B} {9,B}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {4,B} {7,B}
10   R!H u0 {5,S} {8,S}
""",
    solute = SoluteData(
        S = 0.033774737483055955,
        B = -0.037309336775970904,
        E = 0.08774497123233298,
        L = 0.03432995808069647,
        A = -0.062057679325775716,
    ),
    )


entry(
    index = 179,
    label = "s4_6_6_ane",
    group = 
"""
1 * R!H u0 {3,S} {6,S} {8,S}
2   R!H u0 {4,S} {5,S} {7,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.07374868842382518,
        B = -0.008884570780310741,
        E = 0.09136551171880102,
        L = 0.2207716895101786,
        A = -0.011816590510564811,
    ),
    )


entry(
    index = 0,
    label = "s4_6_6",
    group = 
"""
1 * R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 119,
    label = "s2_6_6_ene_0",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {2,D} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {5,S} {9,S}
""",
    solute = SoluteData(
        S = 0.26389927838141025,
        B = 0.06772026529478256,
        E = 0.08085157846823901,
        L = -0.18950174827135507,
        A = 0.04008982834056114,
    ),
    )


entry(
    index = 0,
    label = "s2_6_7",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    solute = SoluteData(
        S = -0.1489389771704655,
        B = 0.05320521107723735,
        E = 0.060324628694283636,
        L = -0.1699849946714791,
        A = -0.0036366997407407163,
    ),
    )


entry(
    index = 51,
    label = "s1_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {11,S}
7    R!H u0 {4,S} {10,S}
8    R!H u0 {2,S} {11,S}
9    R!H u0 {3,S} {10,S}
10 * R!H u0 {7,S} {9,S}
11   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = -0.008008768762510044,
        B = 0.014676428609005468,
        E = -0.00025886632607047315,
        L = -0.09474776638355176,
        A = -0.014855674305296827,
    ),
    )


entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = -1,
    label = "PolycyclicRing",
    group = 
"""
1 * R u0
""",
    solute = SoluteData(
        S = 0.04430901508084168,
        B = 0.04164684973416053,
        E = 0.003303062777666616,
        L = -0.04623759448097044,
        A = -0.017865457851842174,
    ),
    )


entry(
    index = 185,
    label = "s2_6_6_naphthalene",
    group = 
"""
1    R!H u0 {2,B} {3,B} {4,B}
2    R!H u0 {1,B} {5,B} {6,B}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {10,B}
6    R!H u0 {2,B} {7,B}
7  * R!H u0 {6,B} {8,B}
8    R!H u0 {4,B} {7,B}
9    R!H u0 {3,B} {10,B}
10   R!H u0 {5,B} {9,B}
""",
    solute = SoluteData(
        S = 0.013257532803539859,
        B = -0.020779612201391,
        E = 0.10054231626279729,
        L = 0.3816826094247896,
        A = -0.025118433669149266,
    ),
    )


entry(
    index = 117,
    label = "s2_5_6_indene",
    group = 
"""
1 * R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {5,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,B} {8,B}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {2,B} {9,B}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,B} {9,B}
9   R!H u0 {6,B} {8,B}
""",
    solute = SoluteData(
        S = 0.079971956719528,
        B = -0.017661718525762794,
        E = 0.17312261585473065,
        L = 0.12874572713096138,
        A = 0.02402829484229975,
    ),
    )


entry(
    index = 184,
    label = "s2_5_6_ben",
    group = 
"""
1 * R!H u0 {2,B} {3,S} {5,B}
2   R!H u0 {1,B} {4,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,B} {9,B}
6   R!H u0 {2,B} {8,B}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,B} {9,B}
9   R!H u0 {5,B} {8,B}
""",
    solute = SoluteData(
        S = 0.028308753101926452,
        B = -0.0604973793422672,
        E = 0.06687821905764078,
        L = 0.0065612583259373365,
        A = -0.023318995904897565,
    ),
    )


entry(
    index = 0,
    label = "s2_4_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = SoluteData(
        S = -0.02501649526012217,
        B = -0.011095215772975195,
        E = 0.0969586163203423,
        L = -0.2487931453181962,
        A = -0.009760252261843612,
    ),
    )


entry(
    index = 216,
    label = "s2_6_7_ben",
    group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    solute = SoluteData(
        S = -0.0008664038148437644,
        B = -0.08884964242186727,
        E = -0.01137934412528018,
        L = -0.08553735344088385,
        A = -0.03132251681543033,
    ),
    )


entry(
    index = 123,
    label = "s2_6_6_ben_ene_1",
    group = 
"""
1    R!H u0 {2,B} {3,S} {4,B}
2    R!H u0 {1,B} {5,B} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {9,B}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {3,D} {10,S}
8    R!H u0 {4,B} {9,B}
9    R!H u0 {5,B} {8,B}
10   R!H u0 {6,S} {7,S}
""",
    solute = SoluteData(
        S = -0.02403040121690028,
        B = -0.02235981102601452,
        E = 0.05847877624120073,
        L = -0.2273632224448453,
        A = -0.01461880514324521,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ben_ene",
    group = 'OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}',
    solute = None,
)


entry(
    index = 123,
    label = "s2_6_6_ben_ene_2",
    group = 
"""
1    R!H u0 {2,B} {4,B} {5,S}
2    R!H u0 {1,B} {3,S} {6,B}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,B} {10,B}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {2,B} {9,B}
7  * R!H u0 {5,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {6,B} {10,B}
10   R!H u0 {4,B} {9,B}
""",
    solute = SoluteData(
        S = -0.042911524562646505,
        B = 0.05041446350312437,
        E = 0.11535653152953106,
        L = 0.10528272701661143,
        A = 0.08934915691955826,
    ),
    )


entry(
    index = 120,
    label = "s2_6_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,S}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {10,S}
8    R!H u0 {6,S} {9,S}
9    R!H u0 {3,D} {8,S}
10   R!H u0 {5,S} {7,S}
""",
    solute = SoluteData(
        S = 0.06813026569515845,
        B = 0.026238443898390102,
        E = 0.08162021788392289,
        L = 0.24673230397285772,
        A = 1.1591255641008731e-05,
    ),
    )


entry(
    index = 96,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
    solute = SoluteData(
        S = 0.010423376777966203,
        B = 0.016215226979904563,
        E = -0.0018731380235340624,
        L = 0.08249193363868723,
        A = 0.006977282679636465,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_ene",
    group = 'OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2}',
    solute = None,
)


entry(
    index = 78,
    label = "s2_4_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,D}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,D} {7,S}
""",
    solute = SoluteData(
        S = 0.019738318712094263,
        B = 0.027251744154002812,
        E = -0.01830830038933057,
        L = 0.00025256936734563586,
        A = 0.04969819511397978,
    ),
    )


entry(
    index = 0,
    label = "s2_4_6_ene",
    group = 'OR{s2_4_6_ene_1}',
    solute = None,
)


entry(
    index = 101,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = 0.061621844991111716,
        B = -0.051961712804067944,
        E = 0.12710509543294649,
        L = 0.3727425021742327,
        A = 0.007277634671513737,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_diene",
    group = 'OR{s2_5_6_diene_m_7, s2_5_6_diene_1_3}',
    solute = None,
)


entry(
    index = 39,
    label = "s1_5_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {3,S} {7,S}
7    R!H u0 {2,S} {6,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    solute = SoluteData(
        S = 0.006025037015761302,
        B = -0.04042532952431697,
        E = -0.04197317534133328,
        L = -0.044862118372333455,
        A = -0.011698188795574911,
    ),
    )


entry(
    index = 0,
    label = "s1_5_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 161,
    label = "s3_5_6_ane",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    solute = SoluteData(
        S = -0.048158964656590676,
        B = 0.060034609453589356,
        E = 0.005486503311583176,
        L = -0.11188957819659574,
        A = -0.01521166543505934,
    ),
    )


entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_8",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,D}
2   R!H u0 {1,S} {3,S} {4,D}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {9,D}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {5,D} {8,S}
""",
    solute = SoluteData(
        S = 0.03075252599922566,
        B = -0.023077406404061005,
        E = 0.13395772205931783,
        L = 0.1254246506831839,
        A = -0.012760508254045885,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_tetraene",
    group = 'OR{s2_5_6_tetraene_1_3_5_7, s2_5_6_tetraene_1_3_5_8}',
    solute = None,
)


entry(
    index = 95,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * R!H u0 {2,D} {5,S} {6,S}
2   R!H u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = -0.1004959557531029,
        B = 0.011647446931991108,
        E = 0.20367618376763694,
        L = -0.06311689376094501,
        A = -0.029385139664581866,
    ),
    )


entry(
    index = 94,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = 0.06021174266616158,
        B = 0.01967301073374336,
        E = 0.13026172747680212,
        L = 0.1419766459577796,
        A = -0.016997472896147215,
    ),
    )


entry(
    index = 217,
    label = "s2_6_7_ben_ene_1",
    group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,D}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,D} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    solute = SoluteData(
        S = 0.000703497835608686,
        B = 0.040023294485000194,
        E = 0.05807519317311166,
        L = -0.06588109795323611,
        A = -0.008319048753896127,
    ),
    )


entry(
    index = 0,
    label = "s2_6_7_ben_ene",
    group = 'OR{s2_6_7_ben_ene_1}',
    solute = None,
)


entry(
    index = 0,
    label = "s2_5_7",
    group = 
"""
1  * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    solute = SoluteData(
        S = 0.006897864471001265,
        B = -0.010341042626488462,
        E = 0.050782374610824965,
        L = 0.014033284457203527,
        A = -0.001130995555547616,
    ),
    )


entry(
    index = 134,
    label = "s2_6_6_diene_1_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {5,D} {9,S}
9    R!H u0 {6,S} {8,S}
10   R!H u0 {3,S} {7,D}
""",
    solute = SoluteData(
        S = 0.03038750758380869,
        B = 0.013547233962915125,
        E = 0.062395801043291316,
        L = 0.258627699601419,
        A = -0.004274266244296437,
    ),
    )


entry(
    index = 125,
    label = "s2_6_6_diene_0_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,D} {7,S}
7  * R!H u0 {6,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    solute = SoluteData(
        S = 0.22136323521366752,
        B = -0.015971238137455785,
        E = -0.08658241148751569,
        L = 0.501868852258479,
        A = 0.018227874603491432,
    ),
    )


entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_6_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,D} {5,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {9,D}
8    R!H u0 {3,D} {10,S}
9    R!H u0 {6,S} {7,D}
10   R!H u0 {5,D} {8,S}
""",
    solute = SoluteData(
        S = -0.0036322634739003774,
        B = 0.014231146815328388,
        E = 0.13405604740703062,
        L = 0.1662763476653788,
        A = -0.004880482493393607,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_tetraene",
    group = 'OR{s2_6_6_tetraene_0_2_6_8}',
    solute = None,
)


entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_7",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,D}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    solute = SoluteData(
        S = -0.00857458544755043,
        B = 0.0319291455976977,
        E = 0.038943623470273345,
        L = -0.04558450927960763,
        A = -0.014041151842823603,
    ),
    )


entry(
    index = 99,
    label = "s2_5_6_triene_m_1_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,D}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    solute = SoluteData(
        S = -0.038300066976499084,
        B = 0.015417342097481938,
        E = -0.07506044929385873,
        L = -0.27291312980423854,
        A = 0.006984794047446373,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_triene",
    group = 'OR{s2_5_6_triene_m_1_7}',
    solute = None,
)


entry(
    index = 108,
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {9,D}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,D}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {5,D} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    solute = SoluteData(
        S = 0.11439659366343752,
        B = -0.020910153270096227,
        E = -0.15856968900866597,
        L = 0.3888607894105422,
        A = 0.013307287219345107,
    ),
    )


entry(
    index = 122,
    label = "s2_6_6_ene_m",
    group = 
"""
1    R!H u0 {2,D} {5,S} {6,S}
2    R!H u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {2,S} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {3,S} {9,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {6,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    solute = SoluteData(
        S = 0.028861858501621266,
        B = -0.0006830125315827366,
        E = 0.05691221608656849,
        L = -2.6544397712209147,
        A = -0.004002153038396352,
    ),
    )


entry(
    index = 126,
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,D} {8,S}
7  * R!H u0 {5,D} {8,S}
8    R!H u0 {6,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    solute = SoluteData(
        S = 0.09526086137317621,
        B = -0.00046464882887898976,
        E = 0.16841525349840036,
        L = 0.3483486138643468,
        A = 0.02174696354943282,
    ),
    )


entry(
    index = 128,
    label = "s2_6_6_diene_0_5",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,D}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {1,D} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    solute = SoluteData(
        S = 0.0317377806275546,
        B = 0.018448448252476816,
        E = -0.05984589890730713,
        L = 0.024383500764024374,
        A = 0.004768576322839505,
    ),
    )


entry(
    index = 137,
    label = "s3_4_4_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = 0.030194036119874396,
        B = 0.002958406452029409,
        E = -0.006538304989385972,
        L = 0.11793227459165098,
        A = 0.014489103551988491,
    ),
    )


entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 87,
    label = "s2_5_5_diene_0_4",
    group = 
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,D} {7,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {5,S}
""",
    solute = SoluteData(
        S = 0.03162586094662277,
        B = -0.028207099589021723,
        E = 0.0883318835293873,
        L = 0.3865496370878467,
        A = -0.024235663704317473,
    ),
    )


entry(
    index = 0,
    label = "s2_5_5_diene",
    group = 'OR{s2_5_5_diene_0_4}',
    solute = None,
)


entry(
    index = 150,
    label = "s3_4_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    solute = SoluteData(
        S = -0.03954565116578552,
        B = -0.01465852826269401,
        E = 0.014570427049757445,
        L = -0.23814393661147817,
        A = -0.04114918674140837,
    ),
    )


entry(
    index = 0,
    label = "s3_4_6_ene",
    group = 'OR{s3_4_6_ene_1}',
    solute = None,
)


entry(
    index = 0,
    label = "s3_4_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 159,
    label = "s3_5_5_ene_side",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {4,S} {5,S} {7,S}
3 * R!H u0 {1,S} {5,S} {8,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {3,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {2,S} {6,S}
8   R!H ux {3,D}
""",
    solute = SoluteData(
        S = -0.07820936543555389,
        B = -0.009484285003517204,
        E = 0.05337230763214238,
        L = -0.23602299528455825,
        A = -0.03508237560931502,
    ),
    )


entry(
    index = 65,
    label = "s2_3_5_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,D} {5,S}
""",
    solute = SoluteData(
        S = -0.034069319739677195,
        B = -0.005619933733742466,
        E = -0.035269718403809776,
        L = -0.1881628471351312,
        A = -0.013407672016342357,
    ),
    )


entry(
    index = 0,
    label = "s2_3_5_ene",
    group = 'OR{s2_3_5_ene_1}',
    solute = None,
)


entry(
    index = 67,
    label = "s2_3_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,D}
5   R!H u0 {2,S} {7,S}
6 * R!H u0 {4,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    solute = SoluteData(
        S = -0.026462838893460794,
        B = -0.01362457312785812,
        E = 0.013601369721196828,
        L = -0.12139196656364185,
        A = -0.03814751175148305,
    ),
    )


entry(
    index = 0,
    label = "s2_3_6_ene",
    group = 'OR{s2_3_6_ene_1, s2_3_6_ene_2}',
    solute = None,
)


entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
    solute = SoluteData(
        S = -0.019083118170486663,
        B = -0.003146292148481859,
        E = 0.029574612201859685,
        L = 0.0356924011668138,
        A = -0.007537245877990693,
    ),
    )


entry(
    index = 148,
    label = "s3_4_6_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    solute = SoluteData(
        S = -0.08658717083352827,
        B = 0.004077923195908762,
        E = 0.00905335408590849,
        L = -0.06168940608838665,
        A = -0.019291523032696954,
    ),
    )


entry(
    index = 70,
    label = "s2_3_7_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8   R!H u0 {6,S} {7,S}
""",
    solute = SoluteData(
        S = -0.03317420385764077,
        B = 0.004909268105701113,
        E = 0.02728893664031006,
        L = -0.13329055236231993,
        A = -0.005312294889542425,
    ),
    )


entry(
    index = 0,
    label = "s2_3_7",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = None,
)


entry(
    index = 133,
    label = "s2_6_6_diene_1_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {8,D}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,D}
7  * R!H u0 {6,D} {10,S}
8    R!H u0 {4,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    solute = SoluteData(
        S = -0.02277703081742101,
        B = 0.004674054343789176,
        E = 0.09705375688193842,
        L = -0.02640460984209162,
        A = 0.0027687366508702227,
    ),
    )


entry(
    index = 129,
    label = "s2_6_6_diene_0_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,D}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {1,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {5,S} {9,S}
9    R!H u0 {4,D} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    solute = SoluteData(
        S = -0.011807305988210249,
        B = 0.01052194068485241,
        E = 0.09167921216589496,
        L = 0.18267092282683406,
        A = 0.0050853970498972705,
    ),
    )


entry(
    index = 42,
    label = "s1_5_6_ene_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {4,S} {10,S}
7    R!H u0 {2,S} {10,S}
8  * R!H u0 {3,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {6,S} {7,S}
""",
    solute = SoluteData(
        S = -0.01593809322185231,
        B = -0.004814963476009696,
        E = 0.04533211339464724,
        L = 0.04383520795276282,
        A = -0.00568416269912967,
    ),
    )


entry(
    index = 0,
    label = "s1_5_6_ene",
    group = 'OR{s1_5_6_ene_1, s1_5_6_ene_7}',
    solute = None,
)


entry(
    index = 81,
    label = "s2_5_5_ene_0",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {6,S}
""",
    solute = SoluteData(
        S = -0.015938093221852304,
        B = -0.004814963476009699,
        E = 0.04533211339464723,
        L = 0.04383520795276281,
        A = -0.005684162699129672,
    ),
    )


entry(
    index = 93,
    label = "s2_5_6_ene_0",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,D} {8,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {5,S} {8,S}
""",
    solute = SoluteData(
        S = -0.011569110953392931,
        B = -0.0016629352329247398,
        E = 0.010489298721781814,
        L = 0.04527641264821109,
        A = -0.005086396241584141,
    ),
    )


entry(
    index = 40,
    label = "s1_5_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {2,S} {9,S}
7    R!H u0 {3,D} {10,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {6,S}
10   R!H u0 {7,S} {8,S}
""",
    solute = SoluteData(
        S = -0.025420438767644982,
        B = -0.0010614450841806662,
        E = 0.02630147642473224,
        L = 0.11382027131398681,
        A = -0.010544930763154188,
    ),
    )


entry(
    index = 162,
    label = "s3_5_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    solute = SoluteData(
        S = -0.033648481421738194,
        B = -0.005763848400593,
        E = -0.061033333654415,
        L = -0.13151581553857833,
        A = -0.014585187415028714,
    ),
    )


entry(
    index = 0,
    label = "s3_5_6_ene",
    group = 'OR{s3_5_6_ene_1}',
    solute = None,
)


entry(
    index = 9,
    label = "s1_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    solute = SoluteData(
        S = -0.014323398431964571,
        B = -0.006196765445839329,
        E = -0.021935350265095604,
        L = -0.2319218315271576,
        A = -0.031244371263267498,
    ),
    )


entry(
    index = 0,
    label = "s1_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    solute = None,
)


tree(
"""
L1: PolycyclicRing
	L2: s1_3_6
		L3: s1_3_6_ane
	L2: s2_3_7
		L3: s2_3_7_ane
	L2: s3_4_6
		L3: s3_4_6_ane
		L3: s3_4_6_ene
			L4: s3_4_6_ene_1
	L2: s3_4_4
		L3: s3_4_4_ane
	L2: s2_5_7
	L2: s3_5_6
		L3: s3_5_6_ene
			L4: s3_5_6_ene_1
		L3: s3_5_6_ane
	L2: s1_5_6
		L3: s1_5_6_ene
			L4: s1_5_6_ene_1
			L4: s1_5_6_ene_7
		L3: s1_5_6_ane
	L2: s2_4_6
		L3: s2_4_6_ene
			L4: s2_4_6_ene_1
	L2: s1_6_6
		L3: s1_6_6_ane
	L2: s2_6_7
		L3: s2_6_7_ben
			L4: s2_6_7_ben_ene
				L5: s2_6_7_ben_ene_1
	L2: s4_6_6
		L3: s4_6_6_ane
	L2: s2_3_6
		L3: s2_3_6_ene
			L4: s2_3_6_ene_2
			L4: s2_3_6_ene_1
		L3: s2_3_6_ane
	L2: s3_5_5
		L3: s3_5_5_diene
			L4: s3_5_5_diene_1_4
		L3: s3_5_5_ene
			L4: s3_5_5_ene_side
			L4: s3_5_5_ene_1
		L3: s3_5_5_ane
	L2: s2_5_5
		L3: s2_5_5_diene
			L4: s2_5_5_diene_0_4
		L3: s2_5_5_ene
			L4: s2_5_5_ene_0
			L4: s2_5_5_ene_1
		L3: s2_5_5_ane
	L2: s2_3_4
		L3: s2_3_4_ane
	L2: s2_4_5
		L3: s2_4_5_ane
	L2: s2_3_5
		L3: s2_3_5_ene
			L4: s2_3_5_ene_1
		L3: s2_3_5_ane
	L2: s2_6_6
		L3: s2_6_6_tetraene
			L4: s2_6_6_tetraene_0_2_6_8
		L3: s2_6_6_ben_ene
			L4: s2_6_6_ben_ene_2
			L4: s2_6_6_ben_ene_1
		L3: s2_6_6_naphthalene
		L3: s2_6_6_ben
		L3: s2_6_6_diene
			L4: s2_6_6_diene_0_6
			L4: s2_6_6_diene_1_6
			L4: s2_6_6_diene_0_5
			L4: s2_6_6_diene_0_3
			L4: s2_6_6_diene_0_2
			L4: s2_6_6_diene_1_7
			L4: s2_6_6_diene_0_8
		L3: s2_6_6_ene
			L4: s2_6_6_ene_m
			L4: s2_6_6_ene_1
			L4: s2_6_6_ene_0
			L4: s2_6_6_ene_2
		L3: s2_6_6_ane
	L2: s3_6_6
		L3: s3_6_6_ane
	L2: s2_5_6
		L3: s2_5_6_triene
			L4: s2_5_6_triene_m_1_7
		L3: s2_5_6_tetraene
			L4: s2_5_6_tetraene_1_3_5_7
			L4: s2_5_6_tetraene_1_3_5_8
		L3: s2_5_6_diene
			L4: s2_5_6_diene_1_3
			L4: s2_5_6_diene_m_7
		L3: s2_5_6_ene
			L4: s2_5_6_ene_0
			L4: s2_5_6_ene_1
			L4: s2_5_6_ene_m
			L4: s2_5_6_ene_2
		L3: s2_5_6_ben
		L3: s2_5_6_indene
		L3: s2_5_6_ane
""",
)