name = "Ring Corrections" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
	 index = -1,
	 label = "Ring",
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
    index = 102,
    label = "EightMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {8,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {1,[S,D]} {7,[S,D]}
""",
    solute = SoluteData(
        S = -0.01335865196884263,
        B = 0.0024540947536931595,
        E = -0.018109134965161422,
        L = 0.07770246142178591,
        A = -0.016614632898217463,
    ),
    )


entry(
    index = 1,
    label = "Cyclopropane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = -0.007119578893032176,
        B = -0.022067622738819515,
        E = 0.06746458207783353,
        L = -0.04968309005735139,
        A = -0.04811083456076326,
    ),
    )


entry(
    index = 97,
    label = "ThreeMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
    solute = None,
)


entry(
    index = 13,
    label = "Cyclobutane",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    solute = SoluteData(
        S = -0.06499410927216324,
        B = -0.013708944219213492,
        E = -0.004448120964611959,
        L = -0.219265359653151,
        A = -0.004610669238551399,
    ),
    )


entry(
    index = 98,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    solute = None,
)


entry(
    index = 21,
    label = "Cyclopentane",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.09764110530166971,
        B = -0.004142229486524085,
        E = 0.003985623299180309,
        L = 0.014039144062112475,
        A = -0.020390471366663106,
    ),
    )


entry(
    index = 99,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    solute = None,
)


entry(
    index = 32,
    label = "Cyclohexane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.027288828812461238,
        B = -0.0031956905343921162,
        E = 0.02209755154340436,
        L = -0.006654294583613077,
        A = 0.009073770752712597,
    ),
    )


entry(
    index = 105,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,O2s,N,S2s] u0 {2,S} {6,S}
2   [Cs,O2s,N,S2s] u0 {1,S} {3,S}
3   [Cs,O2s,N,S2s] u0 {2,S} {4,S}
4   [Cs,O2s,N,S2s] u0 {3,S} {5,S}
5   [Cs,O2s,N,S2s] u0 {4,S} {6,S}
6   [Cs,O2s,N,S2s] u0 {1,S} {5,S}
""",
    solute = None,
)


entry(
    index = 100,
    label = "SixMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
    solute = None,
)


entry(
    index = 55,
    label = "Cycloheptane",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    solute = SoluteData(
        S = 0.030328638488405495,
        B = 0.01157544798348561,
        E = -0.0008112231522440007,
        L = 0.04927241544373834,
        A = 0.007820302740457431,
    ),
    )


entry(
    index = 101,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    solute = None,
)


entry(
    index = 59,
    label = "Cyclooctane",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.05487386666124693,
        B = -0.014871737227115767,
        E = 0.03742612321231271,
        L = 0.05264131235356486,
        A = 0.019261877659860278,
    ),
    )


entry(
    index = 64,
    label = "Cyclononane",
    group = 
"""
1 * Cs u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    solute = SoluteData(
        S = -0.028690074383234607,
        B = -0.017668122472032383,
        E = 0.03608341805848467,
        L = 0.02904334931912421,
        A = 0.00013419156830453375,
    ),
    )


entry(
    index = 103,
    label = "NineMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
    solute = None,
)


entry(
    index = 67,
    label = "Cyclodecane",
    group = 
"""
1  * Cs u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    solute = SoluteData(
        S = -0.032973379018412706,
        B = -0.013881582728826117,
        E = 0.033115851030777396,
        L = 0.04957645190991994,
        A = 0.0052942652974353405,
    ),
    )


entry(
    index = 104,
    label = "TenMember",
    group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    solute = SoluteData(
        S = -0.016602381768583068,
        B = -0.004081541569866634,
        E = 0.017328537701886856,
        L = 0.10254030020347132,
        A = 0.005621647197801833,
    ),
    )


entry(
    index = 105,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,O2s,N,S2s] u0 {2,S} {6,S}
2   [Cs,O2s,N,S2s] u0 {1,S} {3,S}
3   [Cs,O2s,N,S2s] u0 {2,S} {4,S}
4   [Cs,O2s,N,S2s] u0 {3,S} {5,S}
5   [Cs,O2s,N,S2s] u0 {4,S} {6,S}
6   [Cs,O2s,N,S2s] u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.018751897201134807,
        B = -0.026506640516814492,
        E = 0.037738221470788,
        L = 0.03585685365975823,
        A = 0.06782832897818354,
    ),
    )


entry(
    index = 22,
    label = "Cyclopentene",
    group = 
"""
1   [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5 * [Cs,N] u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.09738870716205313,
        B = -0.009377863948246877,
        E = -0.07370898157837545,
        L = -0.2578315577412831,
        A = -0.012287718519082067,
    ),
    )


entry(
    index = 33,
    label = "Cyclohexene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.0041331247472203275,
        B = 0.004484474626323767,
        E = 0.0392226772972743,
        L = 0.06930219406501865,
        A = 0.018906826231869792,
    ),
    )


entry(
    index = 114,
    label = "six-inringonedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = None,
)


entry(
    index = 56,
    label = "Cycloheptene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    solute = SoluteData(
        S = 0.022959476182268002,
        B = 0.002175976949881221,
        E = 0.03778751459926372,
        L = 0.21235623748559676,
        A = -0.006810139210570291,
    ),
    )


entry(
    index = 60,
    label = "cis-Cyclooctene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.025306588240708867,
        B = -0.011035261667828736,
        E = 0.03494640156048936,
        L = 0.11659515303864955,
        A = -0.001173865117821211,
    ),
    )


entry(
    index = 23,
    label = "Cyclopentadiene",
    group = 
"""
1 * [Cs,N]     u0 {2,S} {5,S}
2   [Cd,N,O,S] u0 {1,S} {3,D}
3   [Cd,N,O,S] u0 {2,D} {4,S}
4   [Cd,N,O,S] u0 {3,S} {5,D}
5   [Cd,N,O,S] u0 {1,S} {4,D}
""",
    solute = SoluteData(
        S = 0.1371123850456413,
        B = -0.054600510049082084,
        E = 0.05214551241843895,
        L = 0.2528978796030423,
        A = 0.04041635981104165,
    ),
    )


entry(
    index = 35,
    label = "1,4-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = 0.008420128342404316,
        B = 0.0002293444870447383,
        E = 0.026325542787426305,
        L = 0.14210143516580587,
        A = 0.00049915994627824,
    ),
    )


entry(
    index = 116,
    label = "six-inringtwodouble-14",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    solute = None,
)


entry(
    index = 58,
    label = "1,3,5-Cycloheptatriene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {1,S} {6,D}
""",
    solute = SoluteData(
        S = 0.01832219032615376,
        B = 0.004750856110395294,
        E = -0.017583465372945285,
        L = 0.015366679570776668,
        A = 0.004670247900531803,
    ),
    )


entry(
    index = 63,
    label = "Cyclooctatetraene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    solute = SoluteData(
        S = -0.03748231783897405,
        B = -0.01812781543752933,
        E = -0.04631413011987422,
        L = -0.30454983766323485,
        A = -0.00818846378206476,
    ),
    )


entry(
    index = 128,
    label = "1,5-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.004723589287714447,
        B = -0.001855686830657391,
        E = 0.031182135441279773,
        L = 0.030878161488860453,
        A = 0.0011927202251133574,
    ),
    )


entry(
    index = 31,
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {3,S} {6,D}
2   [Cs,N] u0 {1,S} {4,S}
3   [Cs,N] u0 {1,S} {5,S}
4   [Cs,N] u0 {2,S} {5,S}
5   [Cs,N] u0 {3,S} {4,S}
6   [Cd,N] u0 {1,D}
""",
    solute = SoluteData(
        S = -0.009836339523556956,
        B = 0.0028941444042333638,
        E = 0.01683398375630612,
        L = -0.004552628419048577,
        A = -0.0017601301180144068,
    ),
    )


entry(
    index = 107,
    label = "six-onesidedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.07813941946213493,
        B = 0.027545961262341986,
        E = 0.06548523040645933,
        L = 0.27585608873534023,
        A = 0.006177670698041886,
    ),
    )


entry(
    index = 106,
    label = "six-sidedoubles",
    group = 
"""
1   [C,O]   u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [C,O]   u0 {2,S} {4,S}
4   [C,O]   u0 {3,S} {5,S}
5   [C,O]   u0 {4,S} {6,S}
6   [C,O]   u0 {1,S} {5,S}
""",
    solute = None,
)


entry(
    index = 200,
    label = "R-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    H   u0 {2,S}
9    H   u0 {3,S}
10   H   u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = -0.0840976559247017,
        B = 0.018176889410312567,
        E = -0.027858249536055174,
        L = -0.12370182919112598,
        A = -0.061768914071068,
    ),
    )


entry(
    index = 96,
    label = "Benzene",
    group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
    solute = None,
)


entry(
    index = 96,
    label = "Aromatic",
    group = 
"""
1 * Cb u0
""",
    solute = None,
)


entry(
    index = 69,
    label = "Ethylene_oxide",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = 0.10720778149076038,
        B = -0.04209269385349724,
        E = 0.03532645834284126,
        L = 0.14182823174653927,
        A = -0.019102016383247412,
    ),
    )


entry(
    index = 70,
    label = "Oxetane",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    solute = SoluteData(
        S = 0.0453600701874885,
        B = 0.0049336051911471265,
        E = 0.0979042457703992,
        L = 0.20987945554708767,
        A = -0.009579829624096821,
    ),
    )


entry(
    index = 71,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.08004557650116775,
        B = 0.002129565982358379,
        E = -0.04589990618583582,
        L = -0.15154369656518435,
        A = -0.006733518147352993,
    ),
    )


entry(
    index = 73,
    label = "1,3-Dioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2 * Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.10361344009741091,
        B = -0.006561713053851673,
        E = 0.06762504645875252,
        L = 0.3619455475180014,
        A = -0.020587747690194263,
    ),
    )


entry(
    index = 111,
    label = "Oxane",
    group = 
"""
1 * Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.006485421890560056,
        B = -0.06315424768621636,
        E = 0.04642385086205223,
        L = 0.15124576327022388,
        A = 0.06148633080527645,
    ),
    )


entry(
    index = 79,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = 0.0040957310270525165,
        B = 0.0036670682860204373,
        E = 0.05792904360422972,
        L = 0.28095869295103715,
        A = 0.00047074598751000043,
    ),
    )


entry(
    index = 75,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.03431556629930008,
        B = -0.013152568271203006,
        E = -0.02956710455734975,
        L = 0.06653302794817209,
        A = -0.004581725063545074,
    ),
    )


entry(
    index = 86,
    label = "Cyclopentanone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   [Cs,N]  u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = 0.028423007733245922,
        B = 0.0582057077130887,
        E = -0.03826266100594667,
        L = -0.17880914576147428,
        A = -0.01428812053534057,
    ),
    )


entry(
    index = 87,
    label = "Cyclohexanone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.0038544522450796787,
        B = 0.03872892257332809,
        E = -0.006731050899050283,
        L = -0.06140340760529021,
        A = -0.0006399305136530105,
    ),
    )


entry(
    index = 88,
    label = "Cycloheptanone",
    group = 
"""
1 * CO u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    solute = SoluteData(
        S = 5.451063669873029e-07,
        B = 0.013050120953394808,
        E = 0.005670373817880305,
        L = 0.030397893650743853,
        A = 8.818138692480056e-05,
    ),
    )


entry(
    index = 89,
    label = "Cyclooctanone",
    group = 
"""
1 * CO u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.0009734314405717683,
        B = 0.011901666080670328,
        E = 0.011580437865642177,
        L = 0.07440961652722514,
        A = 0.000899593598763476,
    ),
    )


entry(
    index = 90,
    label = "Cyclononanone",
    group = 
"""
1 * CO u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    solute = SoluteData(
        S = -0.0019474079875105277,
        B = 0.010753211207945857,
        E = 0.006490501913403951,
        L = 0.09392133940370495,
        A = 0.0017110058106021566,
    ),
    )


entry(
    index = 99,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    solute = SoluteData(
        S = 0.15265223742579895,
        B = 0.07232698307175663,
        E = -0.004039798836271783,
        L = 0.15000004884837922,
        A = 0.021792454567051048,
    ),
    )


entry(
    index = 144,
    label = "thiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
""",
    solute = SoluteData(
        S = 0.017710710776710947,
        B = -0.023327798799923923,
        E = 0.1462508841652999,
        L = 0.06556011000285221,
        A = -0.05960686647155923,
    ),
    )


entry(
    index = 108,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cd,CO]  u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.023983699792062812,
        B = -0.005183955184923791,
        E = -0.020071692016671826,
        L = -0.1884391401509676,
        A = 0.0023705425705752062,
    ),
    )


entry(
    index = 83,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [CO,CS]  u0 {1,S} {3,S}
""",
    solute = SoluteData(
        S = 0.10041108639390868,
        B = 0.0018025519634360726,
        E = 0.08769216469429283,
        L = 0.48575313480409216,
        A = -0.007633072444217004,
    ),
    )


entry(
    index = 25,
    label = "butyrolactone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   O2s     u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = 0.38864909927352875,
        B = 0.08128159101525899,
        E = 0.08566541992704096,
        L = 0.5913560623916568,
        A = -0.012847844962537254,
    ),
    )


entry(
    index = 92,
    label = "Ethyleneimine",
    group = 
"""
1 * N        u0 {2,S} {3,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = 0.07606472455573772,
        B = -0.031606281525860765,
        E = 0.06376227354034215,
        L = 0.21895029445568095,
        A = -0.003941664089593284,
    ),
    )


entry(
    index = 98,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    solute = SoluteData(
        S = 0.014985365293937122,
        B = -0.02174966806935848,
        E = 0.07984446714078497,
        L = 0.03495638856903472,
        A = 0.0014449930201570246,
    ),
    )


entry(
    index = 82,
    label = "2,5-Furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cd,N]  u0 {2,S} {4,D}
4   [Cd,N]  u0 {3,D} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.010328488120435068,
        B = -0.003158041667435154,
        E = 0.07962323159539615,
        L = 0.014550265732707244,
        A = -0.009600321389881908,
    ),
    )


entry(
    index = 141,
    label = "thiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.041682603060918436,
        B = -0.012763163438672946,
        E = -0.0016879244517805105,
        L = -0.15481212930827062,
        A = -0.00549934869079244,
    ),
    )


entry(
    index = 200,
    label = "para-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {6,B} {7,S}
2    Cb  u0 {1,B} {3,B} {8,S}
3    Cb  u0 {2,B} {4,B} {9,S}
4    Cb  u0 {3,B} {5,B} {10,S}
5    Cb  u0 {4,B} {6,B} {11,S}
6    Cb  u0 {1,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    H   u0 {2,S}
9    H   u0 {3,S}
10   R!H u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.0006954254955938976,
        B = 0.020353263234384827,
        E = 0.003178660343007953,
        L = 0.025163988780219044,
        A = 0.03363841477520795,
    ),
    )


entry(
    index = 96,
    label = "Benzene",
    group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
    solute = SoluteData(
        S = 0.03083383566240373,
        B = 0.028529895712052777,
        E = 0.015184275816141356,
        L = 0.05430348923375068,
        A = 0.013328194121458754,
    ),
    )


entry(
    index = 100,
    label = "SixMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
    solute = SoluteData(
        S = -0.021771864102994573,
        B = 0.05816937315217664,
        E = 0.040656466024209796,
        L = 0.05594416417803537,
        A = -0.03569505403618275,
    ),
    )


entry(
    index = 101,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    solute = SoluteData(
        S = 0.08043465221882602,
        B = -0.008199178018507633,
        E = 0.007439244228057989,
        L = 0.17919473455587556,
        A = -0.02069344418466212,
    ),
    )


entry(
    index = 42,
    label = "124trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.01601753752502005,
        B = 0.029352857218010966,
        E = -0.0005177326521410163,
        L = -0.18949553276710238,
        A = -0.02971134861059365,
    ),
    )


entry(
    index = 200,
    label = "ortho-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    H   u0 {3,S}
10   H   u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = -0.044329035554415835,
        B = 0.043141738940548374,
        E = -0.008379205837901435,
        L = -0.09982203777366283,
        A = -0.04182215548214091,
    ),
    )


entry(
    index = 200,
    label = "meta-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {6,B} {7,S}
2    Cb  u0 {1,B} {3,B} {8,S}
3    Cb  u0 {2,B} {4,B} {9,S}
4    Cb  u0 {3,B} {5,B} {10,S}
5    Cb  u0 {4,B} {6,B} {11,S}
6    Cb  u0 {1,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    H   u0 {2,S}
9    R!H u0 {3,S}
10   H   u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = -0.02125528098762494,
        B = 0.01103100060356316,
        E = 0.003804886295313901,
        L = 0.003971184425525185,
        A = 0.04740227400116556,
    ),
    )


entry(
    index = 200,
    label = "1,2,4,5-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    H   u0 {3,S}
10   R!H u0 {4,S}
11   R!H u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.0696333379861665,
        B = 0.011263939572777432,
        E = 0.014266868081609985,
        L = 0.07069760365402883,
        A = 0.04187796669781262,
    ),
    )


entry(
    index = 200,
    label = "1,2,3,4-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    R!H u0 {3,S}
10   R!H u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.003144330989608639,
        B = 0.008784685156296362,
        E = 0.0028064139993920533,
        L = 0.05734713086915309,
        A = -0.000283297730967996,
    ),
    )


entry(
    index = 200,
    label = "1,2,3-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    R!H u0 {3,S}
10   H   u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.044964140102365116,
        B = 0.03245271057389952,
        E = 0.023423727460365536,
        L = 0.1284564086527703,
        A = -0.005222688153914884,
    ),
    )


entry(
    index = 200,
    label = "1,2,4-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    H   u0 {3,S}
10   R!H u0 {4,S}
11   H   u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.0067292139878415815,
        B = 0.03289190131883684,
        E = -0.0007216183270381281,
        L = -0.01179629215620756,
        A = -0.012563590845200092,
    ),
    )


entry(
    index = 200,
    label = "1,2,3,4,5-Benzene",
    group = 
"""
1  * Cb  u0 {2,B} {3,B} {7,S}
2    Cb  u0 {1,B} {4,B} {8,S}
3    Cb  u0 {1,B} {5,B} {9,S}
4    Cb  u0 {2,B} {6,B} {10,S}
5    Cb  u0 {3,B} {6,B} {11,S}
6    Cb  u0 {4,B} {5,B} {12,S}
7    R!H u0 {1,S}
8    R!H u0 {2,S}
9    R!H u0 {3,S}
10   R!H u0 {4,S}
11   R!H u0 {5,S}
12   H   u0 {6,S}
""",
    solute = SoluteData(
        S = 0.025342442654360493,
        B = 0.031037831505395835,
        E = -0.0062410597974910656,
        L = 0.11572529027917543,
        A = 0.023623810204510775,
    ),
    )


entry(
    index = 74,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3 * O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.010442672748240418,
        B = -0.024315534870727257,
        E = -0.06085439686561671,
        L = -0.12039444198338087,
        A = -0.004806609815820023,
    ),
    )


entry(
    index = 54,
    label = "obenzoquinone",
    group = 
"""
1 * CO u0 {5,S} {6,S}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   CO u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = -0.022319909956657804,
        B = 0.004612881176589585,
        E = 0.07998726117374252,
        L = 0.7216873875920096,
        A = -0.0040500672668167155,
    ),
    )


entry(
    index = 120,
    label = "six-twoin13-twoout",
    group = 
"""
1   [CO,Cd] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6 * [Cd,CO] u0 {1,S} {5,S}
""",
    solute = None,
)


entry(
    index = 53,
    label = "pbenzoquinone",
    group = 
"""
1 * CO u0 {4,S} {5,S}
2   Cd u0 {5,D} {6,S}
3   Cd u0 {4,D} {6,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   CO u0 {2,S} {3,S}
""",
    solute = SoluteData(
        S = -0.10880122983038681,
        B = 0.003969192182030195,
        E = -0.05845244860744231,
        L = -0.19294490974813,
        A = -0.018270858833282538,
    ),
    )


entry(
    index = 121,
    label = "six-twoin14-twoout",
    group = 
"""
1   [Cd,CO] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    solute = None,
)


entry(
    index = 34,
    label = "1,3-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = 0.1312280676361811,
        B = -0.08367761835911545,
        E = 0.11066754108897121,
        L = 0.1272897846072415,
        A = -0.0005794113178737208,
    ),
    )


entry(
    index = 115,
    label = "six-inringtwodouble-13",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = None,
)


entry(
    index = 94,
    label = "Pyrrolidine",
    group = 
"""
1 * N      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = -0.04110592697375113,
        B = -0.05138714938124944,
        E = 0.0012231383243815667,
        L = -0.007897547196846811,
        A = 0.020818452275189293,
    ),
    )


entry(
    index = 103,
    label = "NineMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
    solute = SoluteData(
        S = 0.05347105731066512,
        B = 0.07236373215336443,
        E = 0.0019649622797300323,
        L = 0.18039759508938474,
        A = 0.030855977849380507,
    ),
    )


entry(
    index = 95,
    label = "Piperidine",
    group = 
"""
1 * N  u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.06755290006327812,
        B = 0.023360475002148797,
        E = 0.0009002857565009101,
        L = -0.0854509346574268,
        A = -0.04202863835134385,
    ),
    )


entry(
    index = 121,
    label = "six-twoin14-twoout",
    group = 
"""
1   [Cd,CO] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = -0.06619047367124678,
        B = -0.05720211968542835,
        E = 0.06373335213177043,
        L = -0.4304311503353814,
        A = -0.024831668155538025,
    ),
    )


entry(
    index = 78,
    label = "Furan",
    group = 
"""
1   [Cd,N] u0 {2,D} {5,S}
2   [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5 * O      u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = 0.0061105239567261415,
        B = 0.03961631383935185,
        E = 0.10860421530110408,
        L = 0.1211858938437148,
        A = -0.01705992486757964,
    ),
    )


entry(
    index = 77,
    label = "1,3-Dioxolane",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   O      u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O      u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = 0.020923285107646506,
        B = 0.012074632900834412,
        E = 0.03178515082603169,
        L = -0.0587927778925511,
        A = -0.01860023151384586,
    ),
    )


entry(
    index = 142,
    label = "2,3-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [C,N]  u0 {3,S} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    solute = SoluteData(
        S = 0.025554925932532488,
        B = 0.03282406204265123,
        E = -0.013576214479858392,
        L = 0.1955774588672879,
        A = 0.048400157406812305,
    ),
    )


entry(
    index = 50,
    label = "fg6",
    group = 
"""
1   Cd u0 {2,S} {3,S} {7,D}
2 * CO u0 {1,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D} {6,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   Cd u0 {1,D}
""",
    solute = SoluteData(
        S = -0.0549947079688971,
        B = 0.012538563079532999,
        E = 0.31951535628380767,
        L = 0.36106760749571554,
        A = 0.05447928257920179,
    ),
    )


entry(
    index = 110,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cd,CO]  u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = -0.033704122220925885,
        B = 0.010653259747783984,
        E = 0.021173797995293165,
        L = -0.31851213828753244,
        A = -0.0053394383017644305,
    ),
    )


entry(
    index = 104,
    label = "TenMember",
    group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
    solute = SoluteData(
        S = 0.023327415637703748,
        B = -0.0007088761684759607,
        E = 0.01439877901464298,
        L = -0.04367172349206463,
        A = 0.0099420012864308,
    ),
    )


entry(
    index = 133,
    label = "thiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = -0.0014059090603480687,
        B = 0.00838578706810943,
        E = 0.04555430212587228,
        L = 0.03394501764525247,
        A = -0.0025438791258335747,
    ),
    )


tree(
"""
L1: Ring
	L2: TenMember
	L2: NineMember
	L2: SevenMember
	L2: SixMember
		L3: six-twoin14-twoout
		L3: six-inringtwodouble-13
			L4: 1,3-Cyclohexadiene
		L3: six-twoin14-twoout
			L4: pbenzoquinone
		L3: six-twoin13-twoout
			L4: fg6
			L4: obenzoquinone
	L2: FourMember
	L2: FiveMember
		L3: 2,3-dihydrothiophene
		L3: 1,3-Dioxolane
		L3: Furan
		L3: Pyrrolidine
		L3: thiolane
		L3: 2,5-Furandione
		L3: butyrolactone
		L3: thiophene
	L2: Aromatic
		L3: Benzene
			L4: 1,2,3,4,5-Benzene
			L4: 1,2,4-Benzene
			L4: 1,2,3-Benzene
			L4: 1,2,3,4-Benzene
			L4: 1,2,4,5-Benzene
			L4: meta-Benzene
			L4: ortho-Benzene
		L3: Benzene
			L4: para-Benzene
			L4: R-Benzene
	L2: TenMember
		L3: Cyclodecane
	L2: NineMember
		L3: Cyclononanone
		L3: Cyclononane
	L2: SevenMember
		L3: Cycloheptanone
		L3: 1,3,5-Cycloheptatriene
		L3: Cycloheptene
		L3: Cycloheptane
	L2: SixMember
		L3: six-sidedoubles
			L4: sixmembd-allsingles-twosidedoubles-meta
			L4: sixmembd-allsingles-twosidedoubles-para
			L4: six-onesidedouble
				L5: Cyclohexanone
		L3: six-inringtwodouble-14
			L4: 1,4-Cyclohexadiene
		L3: six-inringonedouble
			L4: 3,4-Dihydro-2H-pyran
			L4: Cyclohexene
		L3: sixnosidedouble
			L4: Piperidine
			L4: 1,4-Dioxane
			L4: 124trioxane
			L4: 1,3,5-Trioxane
			L4: Oxane
			L4: 1,3-Dioxane
		L3: sixnosidedouble
			L4: Cyclohexane
	L2: FiveMember
		L3: Cyclopentanone
		L3: Tetrahydrofuran
		L3: methylenecyclopentane
		L3: Cyclopentadiene
		L3: Cyclopentene
		L3: Cyclopentane
	L2: FourMember
		L3: Beta-Propiolactone
		L3: Oxetane
		L3: Cyclobutane
	L2: ThreeMember
		L3: thiirane
		L3: Ethyleneimine
		L3: Ethylene_oxide
		L3: Cyclopropane
	L2: EightMember
		L3: Cyclooctanone
		L3: 1,5-cyclooctadiene
		L3: Cyclooctatetraene
		L3: cis-Cyclooctene
		L3: Cyclooctane
""",
)