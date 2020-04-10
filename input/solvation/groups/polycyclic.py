#!/usr/bin/env python
# encoding: utf-8

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
        S = 0.1773045427744753,
        B = 0.06985933316588883,
        E = 0.07223689814773378,
        L = 0.26578897650091365,
        A = -0.042188840951440716,
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
        S = -0.024418945119950727,
        B = 0.0005068316684048537,
        E = 0.03373069877333174,
        L = 0.007316759346954611,
        A = -0.01615036181247686,
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
        S = 0.07053781073979348,
        B = 0.058168965594959904,
        E = 0.05349792461004287,
        L = 0.09901377002922314,
        A = 0.03866342887972452,
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
        S = -0.09575310818543571,
        B = 0.004206450095036367,
        E = -0.016034548171340122,
        L = -0.1016881476091187,
        A = -0.004820449565586902,
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
        S = 0.01414494428509762,
        B = 0.014189107131100423,
        E = 0.07721173216187965,
        L = 0.01552326813022314,
        A = -0.013410245944674735,
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
        S = -0.05094214995696632,
        B = -0.0036942986997841078,
        E = -0.05324945478368095,
        L = -0.2703469824915638,
        A = 0.014475155791767166,
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
        S = -0.03499930961930221,
        B = -0.010894737370263096,
        E = 0.06299322900033119,
        L = -0.05640616518904715,
        A = 0.00039693859026335913,
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
        S = -0.09424533171571892,
        B = -0.008893021517347059,
        E = 0.03780658930363941,
        L = -0.3014151048423235,
        A = -0.06110934572531505,
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
        S = 0.08004547616361835,
        B = -0.03737052514422164,
        E = -0.136619767936801,
        L = -0.042147262923960004,
        A = -0.01732537697791453,
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
        S = -0.042810689033230945,
        B = -0.018941831893283734,
        E = 0.03698105867812261,
        L = -0.31275894869232435,
        A = -0.00931146379405188,
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
        S = -0.011572019986951766,
        B = -0.008039197072470429,
        E = 0.0032305814638522593,
        L = 0.04445404601616862,
        A = -0.0037038423348434565,
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
        S = 0.024423339650969867,
        B = -0.005790657747944982,
        E = -0.00854093496583454,
        L = -0.030910055268894936,
        A = 0.005118439363066972,
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
        S = 0.1517771986077044,
        B = 0.046440507801407925,
        E = 0.01138280910180865,
        L = 0.20328625889972599,
        A = -0.008372737081465678,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_diene",
    group = 'OR{s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_5, s2_6_6_diene_0_6, s2_6_6_diene_0_8, s2_6_6_diene_1_6, s2_6_6_diene_1_7}',
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
        S = -0.07042085298717884,
        B = 0.06527254619770584,
        E = 0.0768018720366349,
        L = 0.5723992613434189,
        A = 0.13036767441575542,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ene",
    group = 'OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}',
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
        S = -0.0006499976845751307,
        B = -0.04907190497685619,
        E = 0.07378857829415136,
        L = 0.009126908278371542,
        A = -0.06299936157661265,
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
        S = -0.06716455481828619,
        B = -0.0039156197405117365,
        E = 0.09470213834927439,
        L = 0.2427556908821975,
        A = -0.011343807170496205,
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
        S = 0.2918315922882003,
        B = 0.05467888640381767,
        E = 0.109698708054039,
        L = -0.02627034495499788,
        A = 0.010918918846878886,
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
        S = -0.11240696136463314,
        B = 0.05156466383265287,
        E = 0.04198138795918725,
        L = -0.13190519193322595,
        A = 0.0018547672602050875,
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
        S = 0.005326465620001639,
        B = 0.013100186071658948,
        E = -0.002808176012942216,
        L = -0.07179269836818725,
        A = -0.023457738532259506,
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
        S = 0.12244482919898621,
        B = 0.033608781560070244,
        E = 0.010144101427321809,
        L = 0.07106485490510073,
        A = -0.014128961433313438,
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
        S = 0.012409035244814681,
        B = -0.031854432859437766,
        E = 0.10019061581240575,
        L = 0.3872735468425364,
        A = -0.027501902334123342,
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
        S = 0.00919081110391261,
        B = -0.023535055832812117,
        E = 0.06316618017072112,
        L = -0.08656521157504816,
        A = -0.01775085263294681,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ben_ene",
    group = 'OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}',
    solute = None,
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
        S = 0.13366583974206012,
        B = -0.04424881706024354,
        E = 0.19722385652457036,
        L = 0.2494089902571007,
        A = 0.02050706936655009,
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
        S = 0.02829584649194979,
        B = -0.06382935323318602,
        E = 0.08394150668449506,
        L = 0.016763496202073225,
        A = -0.02696115603825582,
    ),
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
        S = 0.006422880977576711,
        B = -0.02871241311218047,
        E = 0.08169404101793967,
        L = 0.08191191248269623,
        A = -0.011180141494895143,
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
        S = -0.02328619993757255,
        B = 0.007653775825532519,
        E = 0.05677200608470954,
        L = -0.2766772107364752,
        A = -0.00799487374930561,
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
        S = 0.009054035340345866,
        B = -0.07697669427604278,
        E = 0.007311656627027246,
        L = -0.09943737436787789,
        A = -0.04636078730075854,
    ),
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
        S = -0.0431700554452329,
        B = 0.04080948289844194,
        E = 0.13338330817855512,
        L = 0.10646974989320805,
        A = 0.07382183938248585,
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
        S = 0.05754331817681423,
        B = 0.025177382176088125,
        E = 0.08800216145553161,
        L = 0.21410242967315737,
        A = -0.006096262216648545,
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
        S = 0.009062983435954916,
        B = 0.02280063527389013,
        E = -0.03302680740590832,
        L = -0.06827365852981514,
        A = 0.0076451346069397515,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_ene",
    group = 'OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_6}',
    solute = None,
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
        S = 0.008285706705906146,
        B = 0.019855944153813723,
        E = 0.09462401060115751,
        L = 0.23021151731042994,
        A = -0.028374460929934453,
    ),
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
        S = 0.016811604043243767,
        B = 0.029810785179214604,
        E = -0.027052070873335023,
        L = -0.005443548158180859,
        A = 0.04680948018171523,
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
        S = 0.04769083589385515,
        B = -0.06171752229151966,
        E = 0.12576077671026445,
        L = 0.38664228323447725,
        A = 0.004023377047652171,
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
        S = -0.004507062323426117,
        B = -0.02594573258882291,
        E = -0.009333766303545012,
        L = -0.021903137244337786,
        A = -0.019191547546655776,
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
        S = -0.05204915787197058,
        B = 0.037744400187073146,
        E = 0.0023191080605724497,
        L = -0.1564996672008511,
        A = -0.027492949437876796,
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
        S = 0.023539752922026678,
        B = -0.0193833679811604,
        E = 0.12434788201776326,
        L = 0.11547570574462873,
        A = -0.01346124975600726,
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
        S = -0.10046413080392748,
        B = 0.019878243542372304,
        E = 0.21369797762228385,
        L = -0.09162361112487102,
        A = -0.03308520124622262,
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
        S = 0.03674966338905501,
        B = 0.041075104871853556,
        E = 0.07318450241027845,
        L = -0.19817617592490183,
        A = -0.01814581854312421,
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
        S = -0.03279160051131779,
        B = 0.03962487416810407,
        E = 0.02480745598407008,
        L = -0.2487348152540386,
        A = 0.0043335318086950465,
    ),
    )


entry(
    index = 0,
    label = "s2_6_7_ben_ene",
    group = 'OR{s2_6_7_ben_ene_1}',
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
        S = -0.011741263728115903,
        B = 0.034190064903869465,
        E = 0.016153221585353667,
        L = -0.021890467370630457,
        A = -0.027015136367280354,
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
        S = 0.23148729517981226,
        B = -0.01763912330559975,
        E = -0.08747225346286436,
        L = 0.5257930999391495,
        A = 0.010815658468701469,
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
        S = -0.0030571296955362076,
        B = 0.012411252796213851,
        E = 0.1290075608847187,
        L = 0.19588315129539746,
        A = -0.0066961605769145305,
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_tetraene",
    group = 'OR{s2_6_6_tetraene_0_2_6_8}',
    solute = None,
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
        S = 0.09207603920265536,
        B = 0.02205966689362221,
        E = 0.09930106986602298,
        L = 0.42035409679479874,
        A = 0.00847855691327285,
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
        S = -0.04602011972095382,
        B = 0.017649353495376854,
        E = -0.08917547006632344,
        L = -0.31815190179485103,
        A = 0.0054431719948942175,
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
        S = 0.12091777595564566,
        B = -0.021498148018500383,
        E = -0.1480498304370044,
        L = 0.4128053681731551,
        A = 0.010500943138290099,
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
        S = 0.023934336617775248,
        B = -0.0022860182600356804,
        E = 0.07118005976348347,
        L = -2.7050872471203373,
        A = -0.0026066637475233374,
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
        S = 0.07511895355814381,
        B = -0.01062056480128661,
        E = 0.18896014917527357,
        L = 0.37504776292119685,
        A = 0.012235438561149458,
    ),
    )


entry(
    index = 98,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    solute = SoluteData(
        S = 0.11280205179235527,
        B = -0.003980899619031473,
        E = 0.0795680061213506,
        L = 0.35521210367765227,
        A = -0.015112862946646174,
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
        S = 0.029767150478908534,
        B = 0.007809211458622885,
        E = 0.013584938482541806,
        L = 0.0716560540322007,
        A = 0.009929057436332954,
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
        S = 0.019791670990195537,
        B = -0.020795784300884686,
        E = 0.06144169933198729,
        L = 0.28801287855670205,
        A = -0.023437774981067867,
    ),
    )


entry(
    index = 0,
    label = "s2_5_5_diene",
    group = 'OR{s2_5_5_diene_0_4}',
    solute = None,
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
        S = -0.06346755225362202,
        B = -0.011307479836043976,
        E = -0.009874309708476059,
        L = -0.21414703530814774,
        A = -0.016068988979489083,
    ),
    )


entry(
    index = 0,
    label = "s2_3_5_ene",
    group = 'OR{s2_3_5_ene_1}',
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
        S = -0.05233280798331564,
        B = -0.021992787079358825,
        E = 0.03473978072056691,
        L = -0.2263056059996148,
        A = -0.04554584942665112,
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
        S = -0.07604051818404674,
        B = -0.013366660311412154,
        E = 0.0612589405008375,
        L = -0.22841937099344364,
        A = -0.03723723778530784,
    ),
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
        S = -0.028872156940652958,
        B = -0.018847815203861213,
        E = 0.020043802204312063,
        L = -0.14485588734669874,
        A = -0.04020323351344303,
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
        S = -0.017889031296269745,
        B = -0.0044265857205275354,
        E = 0.03562689090736616,
        L = 0.02939681080101306,
        A = -0.007963715633521063,
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
        S = -0.08474381667436702,
        B = -0.0013943107743084491,
        E = 0.011891165569386603,
        L = -0.032575064561514835,
        A = -0.01808661602368976,
    ),
    )


entry(
    index = 41,
    label = "s1_5_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {5,S} {7,S}
10   R!H u0 {6,S} {8,D}
""",
    solute = SoluteData(
        S = -0.010890529538568684,
        B = -0.00300722037598323,
        E = 0.06620127837756527,
        L = -0.05986478737442136,
        A = -0.00576162156088518,
    ),
    )


entry(
    index = 0,
    label = "s1_5_6_ene",
    group = 'OR{s1_5_6_ene_1, s1_5_6_ene_2, s1_5_6_ene_7}',
    solute = None,
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
        S = -0.029349866664182295,
        B = 0.004040957412581224,
        E = 0.024956566545802344,
        L = -0.1447217831532042,
        A = -0.003715534025867267,
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
        S = -0.03018565020279171,
        B = 0.0007463849557595607,
        E = 0.094107101371297,
        L = -0.04494921903857799,
        A = 0.0028384666363981946,
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
        S = -0.009346974010817057,
        B = 0.012199483783908508,
        E = 0.09886696795534083,
        L = 0.1916728747125625,
        A = 0.005230015881863677,
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
        S = -0.012310948749649046,
        B = -0.002908180466218302,
        E = 0.050337312936505806,
        L = 0.06836468234228345,
        A = -0.004939979761739631,
    ),
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
        S = -0.012310948749649043,
        B = -0.0029081804662183025,
        E = 0.050337312936505806,
        L = 0.06836468234228345,
        A = -0.004939979761739631,
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
        S = -0.011856387158585422,
        B = 0.00036602244387012444,
        E = 0.014955877350604094,
        L = 0.04494240285004922,
        A = -0.005257177137810383,
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
        S = -0.0262645146681743,
        B = 0.0006780436152615786,
        E = 0.04379591332843504,
        L = 0.08343280582596889,
        A = -0.010832089849728494,
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
        S = -0.03218032556966854,
        B = -0.006438014017145915,
        E = -0.03575205415339473,
        L = -0.09458424156785931,
        A = -0.014091715118805725,
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
        S = -0.015394028642545913,
        B = -0.009616986415384172,
        E = -0.01897601481151254,
        L = -0.2865676133501634,
        A = -0.03263675183163699,
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
	L2: s3_5_6
		L3: s3_5_6_ene
			L4: s3_5_6_ene_1
		L3: s3_5_6_ane
	L2: s1_5_6
		L3: s1_5_6_ene
			L4: s1_5_6_ene_1
			L4: s1_5_6_ene_7
			L4: s1_5_6_ene_2
		L3: s1_5_6_ane
	L2: s2_4_6
		L3: s2_4_6_ene
			L4: s2_4_6_ene_1
	L2: s2_5_7
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
		L3: s2_6_6_ene
			L4: s2_6_6_ene_m
			L4: s2_6_6_ene_1
			L4: s2_6_6_ene_0
			L4: s2_6_6_ene_2
		L3: s2_6_6_diene
			L4: s2_6_6_diene_0_6
			L4: s2_6_6_diene_1_6
			L4: s2_6_6_diene_0_3
			L4: s2_6_6_diene_0_5
			L4: s2_6_6_diene_0_2
			L4: s2_6_6_diene_1_7
			L4: s2_6_6_diene_0_8
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
			L4: s2_5_6_ene_6
			L4: s2_5_6_ene_1
			L4: s2_5_6_ene_m
			L4: s2_5_6_ene_2
		L3: s2_5_6_ben
		L3: s2_5_6_indene
		L3: s2_5_6_ane
""",
)