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
        S = 0.07100636480497688,
        B = -0.0829300040477686,
        E = 0.1317596254463221,
        L = 0.139969121009264,
        A = 0.01621048455127699,
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
        S = -0.031924599935710174,
        B = -0.023224564365879257,
        E = 0.07086322875673744,
        L = -0.030314897035930582,
        A = -0.03276951078779055,
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
        S = -0.038114706196091176,
        B = -0.01839763977060502,
        E = -0.0413005800404785,
        L = -0.1855711239061292,
        A = 0.001257601188018095,
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
        S = -0.06601953687034905,
        B = 0.0013569412812337086,
        E = -0.014760488408513002,
        L = 0.028875870954723038,
        A = -0.009323833318260564,
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
        S = -0.006336958324235078,
        B = 0.0009522036511194473,
        E = -0.00587997461558223,
        L = -0.05343040875766081,
        A = -0.0027970828020240615,
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
        S = -0.03488939261217882,
        B = 0.03192122582651745,
        E = 0.004192870447095582,
        L = -0.004467321247808921,
        A = 0.005303024665659601,
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
        S = -0.023073389663346443,
        B = 0.00463231776962889,
        E = 0.011018900179805464,
        L = 0.06455515542685543,
        A = 0.03471530961556678,
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
        S = -0.047273271185332526,
        B = -0.016790388359318023,
        E = 0.06039746964010128,
        L = -0.015035927135967997,
        A = -0.004954063434938111,
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
        S = -0.033652394072929866,
        B = -0.008667767916070412,
        E = 0.018074364589743347,
        L = 0.018672235654250777,
        A = 0.002503473134315867,
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
        S = -0.047979551067225255,
        B = 0.01484263648573846,
        E = -0.00022308911698693928,
        L = 0.05821604394727398,
        A = -0.016578761173346446,
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
        S = -0.004138054775536826,
        B = -0.0349815769989829,
        E = 0.04866590836587756,
        L = 0.050482078362438225,
        A = 0.05138276585261091,
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
        S = -0.015456969229179121,
        B = -0.04227377997371097,
        E = 0.022994136337798454,
        L = -0.019434439129907714,
        A = 0.015980158587481533,
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
        S = -0.03608424375268822,
        B = 0.017406373699200357,
        E = 0.025199077307342298,
        L = 0.048750272545743205,
        A = 0.008098397331342442,
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
        S = 0.038178379305373114,
        B = 0.0033750312339823705,
        E = 0.0718629063840403,
        L = 0.45416584427593143,
        A = -0.009437892518026606,
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
        S = -0.02061760047836928,
        B = -0.00879353048872004,
        E = 0.041869150714498524,
        L = 0.13266212883562362,
        A = -0.00282255004099095,
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
        S = 0.01001979446148447,
        B = 0.0036077689245103397,
        E = 0.049008324807348916,
        L = 0.05066122557229059,
        A = 0.011094551891312178,
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
        S = 0.14897690478222214,
        B = -0.05039195585786758,
        E = 0.08457891946483886,
        L = 0.18536109119688776,
        A = 0.03532840168646344,
    ),
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
        S = 0.09400263566095797,
        B = -0.05058607068440475,
        E = 0.08271492325290113,
        L = 0.10280413157337946,
        A = 0.039524465337898315,
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
        S = 0.012116053052211837,
        B = 0.0018996415398872797,
        E = 0.03268590020905524,
        L = 0.27995836700351995,
        A = 0.0023281931127530544,
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
        S = 0.09251546269199773,
        B = -0.005171699506061968,
        E = 0.015340680304750642,
        L = 0.194140119079366,
        A = -0.010909040019551439,
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
        S = -0.015116624363942269,
        B = 0.10285848473186633,
        E = -0.0038241376214407383,
        L = -0.0366525890575809,
        A = 0.006063267172364051,
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
        S = 0.017658005934498528,
        B = 0.0150728738681358,
        E = 0.050510875204045895,
        L = 0.11782373713527723,
        A = 0.009222284332069038,
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
        S = -0.00969357072830181,
        B = -0.010365322832976063,
        E = -0.0035136071464606316,
        L = -0.09903753265670572,
        A = -0.001200398030501535,
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
        S = 0.00041917255989776773,
        B = 0.0027338245045475298,
        E = 0.07556250561687042,
        L = 0.11513126189784723,
        A = -0.00011412324545533105,
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
        S = 0.02851668591182645,
        B = 0.020719514598282026,
        E = 0.03397714754192124,
        L = 0.050113014986014975,
        A = 0.008687015878544093,
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
        S = 0.11827940357011,
        B = 0.05611911737985376,
        E = 0.05414434081297767,
        L = 0.2972195469130637,
        A = 0.024526375520060543,
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
        S = 0.17882056641789637,
        B = -0.06944310260248106,
        E = 0.04988600213681555,
        L = 0.18161002218970607,
        A = -0.02945775740174633,
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
        S = -0.06421042235862301,
        B = 0.01936958406857114,
        E = -0.035811065705793406,
        L = -0.12620484300414736,
        A = -0.05416182929062461,
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
        S = 0.0445721718858353,
        B = 0.004053352861866543,
        E = 0.10107009579968176,
        L = 0.2175710558327077,
        A = -0.009641467144934064,
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
        S = 0.17284740936834422,
        B = 0.0015210794041036375,
        E = -0.022915029739734385,
        L = 0.20356484332863972,
        A = -0.015730838377829105,
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
        S = -0.04167091559992665,
        B = -0.043382547491247245,
        E = -0.041879376654615254,
        L = -0.09504937737399197,
        A = 0.019701393825104888,
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
        S = 0.10676149670324303,
        B = -0.003861575062259526,
        E = 0.05857081391423358,
        L = 0.3910310652515731,
        A = -0.030943008263821938,
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
        S = 0.09518507012420355,
        B = -0.05284267720283278,
        E = 0.0677666827306521,
        L = 0.15103140216406855,
        A = 0.07604941297053258,
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
        S = 0.006045838448234819,
        B = 0.002121077129500084,
        E = 0.05999088814200742,
        L = 0.3011414536798188,
        A = 0.0009858234985190657,
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
        S = 0.00901112770435753,
        B = -0.030712110610822428,
        E = 0.0706960377319954,
        L = 0.0966072255363736,
        A = -0.00917242816711104,
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
        S = 0.04120632767877079,
        B = -0.011516841630358564,
        E = -0.03245420335688114,
        L = 0.16412262623244694,
        A = -0.005089321849927606,
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
        S = 0.02353079764292566,
        B = 0.0031042973666228903,
        E = 0.0435442325666808,
        L = 0.06614763087293483,
        A = 0.0029615297802360213,
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
        S = 0.0495997165579794,
        B = 0.047144455151022086,
        E = -0.017405582021460836,
        L = -0.11433565003564326,
        A = -0.011993109997129738,
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
        S = -0.03462514668788239,
        B = 0.04718238806487367,
        E = -0.027203226474013173,
        L = -0.11804208588086343,
        A = -0.004307246994731013,
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
        S = -0.004482590769056571,
        B = 0.013911497422469676,
        E = -0.007078192174421174,
        L = 0.02992867829684595,
        A = -0.0009384343091300438,
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
        S = -0.005729837187232538,
        B = 0.012893949011726023,
        E = -0.0016954385539917425,
        L = 0.07079900725597468,
        A = -0.0003521206445215349,
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
        S = -0.006977083605408572,
        B = 0.011876400600982386,
        E = -0.007312684933562347,
        L = 0.08716933621510022,
        A = 0.00023419302008697586,
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
        S = -0.004834065077146571,
        B = 0.05095231232183471,
        E = 0.09860372913389669,
        L = 0.07433017761088136,
        A = -0.03196595295888145,
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
        S = 0.05608239659142608,
        B = 0.006431177407722173,
        E = 0.15584413929967947,
        L = 0.1299171855707051,
        A = -0.038631143936779626,
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
        S = 0.00457225509082455,
        B = -0.0020990169626676288,
        E = -0.06968945087041874,
        L = -0.2889382501505592,
        A = 0.012984061858734361,
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
        S = 0.015119022198234078,
        B = -0.004729249437612912,
        E = -0.03778823120793733,
        L = -0.17878739023635698,
        A = 0.0011400278380271204,
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
        S = 0.09929318335949461,
        B = 0.002062403473653053,
        E = 0.08064951946581786,
        L = 0.4860574382178343,
        A = -0.006377914735875455,
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
        S = 0.3999871741573585,
        B = 0.08905943873418923,
        E = 0.0759150778380406,
        L = 0.5771223734372971,
        A = -0.01227590271121391,
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
        S = 0.07357174400594947,
        B = -0.0341904826101011,
        E = 0.061314037498924515,
        L = 0.19988645676386607,
        A = -0.0014997608680047967,
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
        S = -0.06220358728771552,
        B = 0.02010105556190715,
        E = 0.019779548772365544,
        L = -0.016649971472266163,
        A = -0.018103092718326438,
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
        S = 0.01610307688180253,
        B = 0.018410879095260242,
        E = -0.006877100241334493,
        L = 0.009304208590397415,
        A = 0.03912749426482192,
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
        S = -0.014273933916575107,
        B = -0.003779321296672075,
        E = 0.11936864535288676,
        L = 0.012760253311066172,
        A = -0.006545468292657782,
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
        S = 0.04217277364930928,
        B = 0.033734553259933096,
        E = 0.012643634280150761,
        L = 0.008906273994978954,
        A = 0.015157305000102091,
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
        S = -0.03177771410470916,
        B = -0.0155660760733807,
        E = -0.07313099873534583,
        L = -0.13884690071808084,
        A = 0.007288792142201116,
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
        S = -0.050096659117671846,
        B = 0.05065129951021585,
        E = 0.04063574070507641,
        L = -0.17370262490560906,
        A = -0.06419545865775793,
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
        S = -0.03452524150338822,
        B = 0.046285300994847976,
        E = -0.007813249196508366,
        L = -0.15113504356537416,
        A = -0.040390949969063034,
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
        S = 0.007061818397588077,
        B = 0.014105006070993072,
        E = 0.00030429895790532753,
        L = -0.008037578535062082,
        A = 0.04305103445734647,
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
        S = 0.04346312423458493,
        B = 0.049729307467470944,
        E = -0.0004126199486568758,
        L = -0.04424241199261519,
        A = -0.009093473265642681,
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
        S = 0.0916987773407488,
        B = 0.022914663591740745,
        E = 0.014500088438210502,
        L = 0.07426917164329538,
        A = 0.030151255553192233,
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
        S = -0.0411855539911082,
        B = 0.0009802741781195922,
        E = -0.030053229733980568,
        L = -0.21114328872896937,
        A = -0.019064729593865168,
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
        S = 0.026062909483694836,
        B = 0.03466694712020661,
        E = 0.023627652670762465,
        L = -0.005059638162958289,
        A = -0.0045571988917545315,
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
        S = 0.041622011987404055,
        B = 0.0419493265788949,
        E = -0.004821053831949349,
        L = 0.04529309044514919,
        A = 0.028878411866536478,
    ),
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
        S = -0.23655360903948675,
        B = -0.01219297370400275,
        E = -0.04646962401864361,
        L = -0.44910775770792805,
        A = -0.01679040781392345,
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
        S = -0.06671678070008194,
        B = -0.02545759290443443,
        E = -0.023084490198885633,
        L = -0.045636953023652026,
        A = 0.028021872251140036,
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
        S = 0.022052371604137855,
        B = 0.010617469328844133,
        E = 0.04805839109195159,
        L = -0.061192317671966874,
        A = -0.03140351973230931,
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
        S = 0.01917738394230565,
        B = 0.010358656969319925,
        E = 0.0389213201187799,
        L = -0.009237778853971576,
        A = -0.02036802373871918,
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
    solute = SoluteData(
        S = 0.005910686452021038,
        B = -0.005984537165008176,
        E = 0.03566046235091732,
        L = 0.06591678523701393,
        A = -0.002882272846909861,
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
        S = 0.0012442172131439677,
        B = 0.00390628351623612,
        E = -0.017905820838057192,
        L = 0.21998822930272688,
        A = -0.003081523919754846,
    ),
    )


tree(
"""
L1: Ring
	L2: SixMember
		L3: six-sidedoubles
		L3: six-twoin14-twoout
			L4: pbenzoquinone
	L2: FourMember
		L3: Beta-Propiolactone
	L2: FiveMember
		L3: 1,3-Dioxolane
		L3: Furan
		L3: Pyrrolidine
		L3: thiolane
		L3: 2,5-Furandione
		L3: butyrolactone
		L3: thiophene
		L3: Cyclopentanone
		L3: Tetrahydrofuran
	L2: Aromatic
		L3: Benzene
			L4: 1,2,3,4,5-Benzene
			L4: 1,2,3-Benzene
			L4: 1,2,3,4-Benzene
			L4: 1,2,4,5-Benzene
			L4: 1,2,4-Benzene
			L4: meta-Benzene
			L4: ortho-Benzene
		L3: Benzene
			L4: para-Benzene
			L4: R-Benzene
	L2: NineMember
		L3: Cyclononanone
	L2: SevenMember
		L3: Cycloheptanone
		L3: 1,3,5-Cycloheptatriene
	L2: TenMember
	L2: TenMember
		L3: Cyclodecane
	L2: NineMember
		L3: Cyclononane
	L2: SevenMember
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
		L3: six-inringtwodouble-13
			L4: 1,3-Cyclohexadiene
		L3: six-inringonedouble
			L4: 3,4-Dihydro-2H-pyran
			L4: Cyclohexene
		L3: sixnosidedouble
			L4: 124trioxane
			L4: Piperidine
			L4: 1,3,5-Trioxane
			L4: 1,4-Dioxane
			L4: Oxane
			L4: 1,3-Dioxane
		L3: sixnosidedouble
			L4: Cyclohexane
	L2: FiveMember
		L3: methylenecyclopentane
		L3: Cyclopentadiene
		L3: Cyclopentene
		L3: Cyclopentane
	L2: FourMember
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