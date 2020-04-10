#!/usr/bin/env python
# encoding: utf-8

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
        S = -0.00585894976738981,
        B = 0.0036580047613729823,
        E = -0.02164307614623355,
        L = 0.10663295850268012,
        A = -0.016136445628371035,
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
        S = -0.0068804004876612925,
        B = -0.01468510494521807,
        E = 0.0668790578609087,
        L = -0.042563146937604636,
        A = -0.042546977447944966,
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
        S = -0.06893118333626157,
        B = -0.017756789351894363,
        E = -0.0031596958580152276,
        L = -0.2259723622162769,
        A = -0.010140300249222365,
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
        S = -0.08083524010804069,
        B = -0.012031831439095982,
        E = 0.0065287089243462266,
        L = 0.01636814186029074,
        A = -0.016456249562403335,
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
        S = 0.05490233871612049,
        B = -0.0002647610039621247,
        E = 0.027458666261373405,
        L = 0.016226318198056533,
        A = 0.009139831073956472,
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
        S = 0.01864659702251954,
        B = 0.014361505061337976,
        E = -0.004360685860670934,
        L = 0.0411891557646868,
        A = 0.003022601822882242,
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
        S = 0.0041577458391997045,
        B = -0.013866511633607187,
        E = 0.030659292416503427,
        L = 0.1648995987182199,
        A = 0.025770793096977333,
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
        S = -0.02558951870752523,
        B = -0.017199406687466702,
        E = 0.03557404430551765,
        L = 0.029862923528031843,
        A = -0.0017326961586703756,
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
        S = -0.024846010160162,
        B = -0.012809606735708632,
        E = 0.02925726421103057,
        L = 0.07287708166589331,
        A = 0.003781263518863984,
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
        S = -0.031105455580986475,
        B = -0.01198583812237864,
        E = 0.012361118814742954,
        L = 0.07742145459047826,
        A = 0.0005074587894802334,
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
        S = -0.014551967206873347,
        B = -0.032083009084349016,
        E = 0.042614741877825144,
        L = 0.006102901080143915,
        A = 0.04636151915943987,
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
        S = -0.12467869978635478,
        B = -0.00144051990072771,
        E = -0.07004989527096588,
        L = -0.31038049061271944,
        A = -0.014483492195240323,
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
        S = 0.004063641379865396,
        B = 0.0025258177372563238,
        E = 0.01556025380172038,
        L = 0.03276484342585733,
        A = 0.010065341769578228,
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
        S = 0.06953858867147984,
        B = -0.006397702856682141,
        E = 0.05456798410313314,
        L = 0.46911237821650864,
        A = -0.005670665508252615,
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
        S = -0.011536962692337891,
        B = -0.006410190362706529,
        E = 0.024361896896326167,
        L = 0.0689332149840449,
        A = -0.0009238887379625765,
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
        S = 0.0019591389404226196,
        B = -5.99753535850462e-05,
        E = 0.007774230091344884,
        L = 0.041670214318144924,
        A = -0.0017456804221485994,
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
    index = 57,
    label = "1,3-Cycloheptadiene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    solute = SoluteData(
        S = -0.012245072415181982,
        B = -0.005029374044059264,
        E = 0.037206841200996155,
        L = 0.025488080199497058,
        A = -0.003774744845320188,
    ),
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
        S = 0.012890937511263767,
        B = 0.0036342217699008076,
        E = -0.028377749039785755,
        L = -0.03877249498738909,
        A = 0.0034072467260613305,
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
        S = -0.03254288443096569,
        B = -0.012065607624493086,
        E = -0.03922208764269992,
        L = -0.26093229604843204,
        A = -0.009091109455089898,
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
        S = 0.1240486729272476,
        B = -0.03375711021500378,
        E = 0.04185130351868527,
        L = 0.2606203453702727,
        A = 0.04789718932156259,
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
        S = -0.005445515001340903,
        B = -0.00125207924447562,
        E = 0.025222801528657312,
        L = 0.009322241757959943,
        A = 0.0006687316059684962,
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
        S = 0.02767489446792444,
        B = 0.01848098713178364,
        E = 0.02556485663190248,
        L = 0.07808983532529391,
        A = 0.009750780460823867,
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
        S = 0.1515786441307879,
        B = 0.048433959080585905,
        E = 0.07377940266744346,
        L = 0.43160900064188934,
        A = 0.014216702290225437,
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
    index = 69,
    label = "Ethylene_oxide",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    solute = SoluteData(
        S = 0.1562601084169403,
        B = -0.06310744955162252,
        E = 0.03827312921168844,
        L = 0.13852350194444338,
        A = -0.027443650472086342,
    ),
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
        S = -0.06269597345155108,
        B = 0.017246581969431712,
        E = -0.013154063176149035,
        L = -0.09684662831567885,
        A = -0.06321425142947094,
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
        S = 0.04322021403881139,
        B = 0.004755128052116532,
        E = 0.10030292212443503,
        L = 0.21322538929606955,
        A = -0.009333474256166171,
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
        S = -0.08536373211056905,
        B = -0.006761724400185822,
        E = -0.06459551832792286,
        L = -0.1634249587742107,
        A = 0.017143710049582452,
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
        S = 0.10910385064017454,
        B = -0.007267112048899812,
        E = 0.07357504926952518,
        L = 0.3738292257123264,
        A = -0.026841417064780528,
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
        S = -0.050929923932386614,
        B = -0.05245272059337519,
        E = 0.05145877752602408,
        L = 0.019108964048631695,
        A = 0.043398098089958446,
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
        S = 0.0017245099316080912,
        B = 0.003489647107543948,
        E = 0.06259746514859663,
        L = 0.27352673060376825,
        A = 0.0003314974090987025,
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
        S = 0.004978536633886725,
        B = -0.028287241317062287,
        E = 0.043782911491139886,
        L = 0.05890065913407966,
        A = -0.009416320122866004,
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
        S = 0.0710715846786579,
        B = 0.050021933710143344,
        E = -0.03127471666633233,
        L = -0.08957964691250983,
        A = -0.015112418702695892,
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
        S = -0.008272438440793619,
        B = 0.038490416167491256,
        E = -0.0037667153647401473,
        L = -0.06303775031512683,
        A = -0.0029060396925663294,
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
        S = -0.001063741193182989,
        B = 0.013010895385783457,
        E = 0.006686545228566827,
        L = 0.03505510610242533,
        A = -0.0009086428809624099,
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
        S = -0.0015647422237686874,
        B = 0.011828998416386865,
        E = 0.012275243472150445,
        L = 0.08114623515729504,
        A = -0.00019900063926011366,
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
        S = -0.002065743254354439,
        B = 0.010647101446990211,
        E = 0.006863941715734011,
        L = 0.10273736421216448,
        A = 0.000510641602442164,
    ),
    )


entry(
    index = 91,
    label = "Cyclodecanone",
    group = 
"""
1  * CO u0 {2,S} {10,S}
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
        S = -0.0025667442849400877,
        B = 0.009465204477593612,
        E = 0.011952639959317562,
        L = 0.10932849326703342,
        A = 0.0012202838441444741,
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
        S = 0.12669496851983109,
        B = 0.06878848589653581,
        E = 0.016491795448031383,
        L = 0.17887547548769187,
        A = 0.005019455881983166,
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
        S = 0.024309864685182293,
        B = -0.024141816181299784,
        E = 0.15269448997694726,
        L = 0.07716101746310898,
        A = -0.06994973147107365,
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
        S = -0.021494940782256052,
        B = -0.009275956617249689,
        E = 2.0512801554405386e-05,
        L = -0.37420683770245283,
        A = 0.004078403215591987,
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
        S = 0.019137291633332505,
        B = -0.0051371804747683825,
        E = -0.01712790180686106,
        L = -0.1979339760052769,
        A = 0.0006992233199688455,
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
        S = 0.09561663156574648,
        B = 0.001373491856349697,
        E = 0.08897446584189479,
        L = 0.47706656421961086,
        A = -0.007612303306479575,
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
        S = 0.37263941394129296,
        B = 0.07873995774280362,
        E = 0.0884003446763937,
        L = 0.5772848822498761,
        A = -0.015531208166647438,
    ),
    )


entry(
    index = 160,
    label = "oxepane",
    group = 
"""
1 * C   u0 {2,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   O2s u0 {1,S} {6,S}
""",
    solute = SoluteData(
        S = 0.09172506539857767,
        B = -0.000837851717820618,
        E = 0.09841430432163317,
        L = 0.38141388238802587,
        A = -0.018091035894975356,
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
        S = 0.07399334720810588,
        B = -0.028932600900171475,
        E = 0.06622630295466161,
        L = 0.21987335064305538,
        A = -0.004399588981431198,
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
        S = 0.0147624210502887,
        B = -0.011960978487422383,
        E = 0.07038654266151752,
        L = 0.03484387137990465,
        A = 0.0024320929085981597,
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
        S = -0.010771839571907216,
        B = -0.0021309604847672926,
        E = 0.08493435284666438,
        L = 0.027960900488809073,
        A = -0.010962926895720844,
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
        S = -0.008419138208157331,
        B = -0.003620481768760694,
        E = -0.013378243674472282,
        L = -0.0700624792174514,
        A = -0.006284962528238764,
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
        S = 0.010580226902248848,
        B = 0.02309019090544839,
        E = 0.00954290403381408,
        L = 0.028922511059724928,
        A = 0.04259018975854242,
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
        S = -0.024937924693547348,
        B = 0.06129986290749771,
        E = 0.027029232427304636,
        L = 0.07459466686395386,
        A = -0.04217105448546599,
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
        S = 0.0771245757338662,
        B = -0.00031615215947463217,
        E = 0.011271164600812662,
        L = 0.23222868950903278,
        A = -0.008896635688215167,
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
        S = 0.010652931240003383,
        B = 0.02620037214331787,
        E = -0.005616352025885097,
        L = -0.14358539673635934,
        A = -0.046915477064519,
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
        S = 0.034093650618474226,
        B = 0.037808905156947334,
        E = 0.016327675833106677,
        L = 0.052514450593553884,
        A = 0.015760099069953487,
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
        S = -0.03259687339354364,
        B = 0.044013590923487556,
        E = -0.005295632071280384,
        L = -0.09273854586236366,
        A = -0.039365657674119967,
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
        S = -0.0031188865451276973,
        B = 0.010094487569686662,
        E = 0.015309224426294041,
        L = 0.024305727677806897,
        A = 0.052700717766639656,
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
        S = 0.007296878029788029,
        B = 0.019842248362900092,
        E = 0.01838971262631788,
        L = -0.046271193120457216,
        A = -0.014085037624619186,
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
        S = 0.07392868792451665,
        B = 0.021676797076405165,
        E = 0.009282614328622008,
        L = 0.09569110970899516,
        A = 0.05276966831139314,
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
        S = 0.0008540466910701845,
        B = 0.010907327974712555,
        E = 0.0009764452366976701,
        L = 0.03884739363755285,
        A = -0.0004673770656546224,
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
        S = 0.030477481187015456,
        B = 0.049786361595254354,
        E = -0.003194399014380893,
        L = 0.028134354710905172,
        A = -0.004952160760874844,
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
        S = 0.020503035673264874,
        B = 0.0380118415160336,
        E = -0.0152922454496415,
        L = 0.07945430756642419,
        A = 0.023970034832406624,
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
        S = -0.022306612695325082,
        B = 0.005542380128807892,
        E = 0.08353449642241388,
        L = 0.781053082720213,
        A = -0.00479646522626692,
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
        S = -0.12011590942493429,
        B = -0.010468754616651662,
        E = -0.07688274127879426,
        L = -0.32333857587438597,
        A = -0.025516437859555218,
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
        S = 0.11259904527743693,
        B = -0.05782369473100547,
        E = 0.09558834810110274,
        L = 0.12648608404056305,
        A = 0.012190888959131702,
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
        S = -0.07972302649205393,
        B = -0.038078981658035777,
        E = 0.01232123806790217,
        L = -0.08683458308588134,
        A = 0.017488844611064654,
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
        S = 0.038373320496119544,
        B = 0.08391501234958292,
        E = -0.011959784151994347,
        L = 0.1804090093358138,
        A = 0.03558789971334729,
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
        S = -0.03600780264276884,
        B = 0.008926273689883604,
        E = 0.019320536331862554,
        L = -0.043208268535665166,
        A = -0.05175057871813027,
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
        S = -0.0724191096363383,
        B = -0.05758833441225486,
        E = 0.07234519553552987,
        L = -0.47275108979170044,
        A = -0.02511293072820368,
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
        S = 0.005895632830903977,
        B = 0.012260661450698901,
        E = 0.049869382262792965,
        L = 0.0994993565021327,
        A = -0.028100295813956944,
    ),
    )


entry(
    index = 118,
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4 * [Cd,CO]  u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    solute = SoluteData(
        S = 0.08534326271912504,
        B = 0.021658884441457648,
        E = 0.15179972341101475,
        L = 0.4903821337218834,
        A = 0.029403832969740074,
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
        S = 0.025847779931935027,
        B = 0.009640741195246272,
        E = 0.0298280339822292,
        L = -0.03206780970147771,
        A = -0.019303688991323946,
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
        S = 0.015724334810997224,
        B = -0.0015472873643298266,
        E = -0.07383421642053614,
        L = -0.05370219954988005,
        A = -0.001703644983217867,
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
        S = 0.0195828382422249,
        B = 0.03525142180150611,
        E = -0.036003795234506746,
        L = 0.15763895269907596,
        A = 0.048544444376347286,
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
        S = -0.06237813616217646,
        B = 0.024267462556881756,
        E = 0.283010672821388,
        L = 0.1930101479352944,
        A = 0.05094227279699145,
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
        S = 0.014397037133666857,
        B = -0.005437251807039876,
        E = 0.014277594890571397,
        L = -0.15216448850202127,
        A = 0.013727373570454232,
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
        S = 0.0014158185323260599,
        B = 0.010001822902467396,
        E = 0.02975690274058802,
        L = 0.06678857622189165,
        A = -0.002728937033269323,
    ),
    )


tree(
"""
L1: Ring
	L2: TenMember
	L2: NineMember
	L2: SevenMember
	L2: SixMember
		L3: six-oneside-twoindoubles-25
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
			L4: 1,2,3,4-Benzene
			L4: 1,2,4,5-Benzene
			L4: 1,2,3-Benzene
			L4: meta-Benzene
			L4: ortho-Benzene
		L3: Benzene
			L4: para-Benzene
			L4: R-Benzene
	L2: TenMember
		L3: Cyclodecanone
		L3: Cyclodecane
	L2: NineMember
		L3: Cyclononanone
		L3: Cyclononane
	L2: SevenMember
		L3: oxepane
		L3: Cycloheptanone
		L3: 1,3,5-Cycloheptatriene
		L3: 1,3-Cycloheptadiene
		L3: Cycloheptene
		L3: Cycloheptane
	L2: SixMember
		L3: six-sidedoubles
			L4: sixmembd-allsingles-twosidedoubles-para
			L4: sixmembd-allsingles-twosidedoubles-meta
			L4: six-onesidedouble
				L5: Cyclohexanone
		L3: six-inringtwodouble-14
			L4: 1,4-Cyclohexadiene
		L3: six-inringonedouble
			L4: 3,4-Dihydro-2H-pyran
			L4: Cyclohexene
		L3: sixnosidedouble
			L4: 1,3,5-Trioxane
			L4: Piperidine
			L4: 124trioxane
			L4: 1,4-Dioxane
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