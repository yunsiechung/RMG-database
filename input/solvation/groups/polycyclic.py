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
        S = -0.126743253203669,
        B = 0.007136825638097918,
        E = 0.005662447956420098,
        L = -0.21760452632725003,
        A = -0.020849604985479334,
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
        S = -0.037857554046788866,
        B = -0.0062598263208623085,
        E = 0.004375652913677875,
        L = -0.053424842455987664,
        A = -0.007744143162675481,
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
    index = -1,
    label = "PolycyclicRing",
    group = 
"""
1 * R u0
""",
    solute = SoluteData(
        S = 0.14454439831137686,
        B = -0.015991748428448027,
        E = 0.031103237746109076,
        L = 0.061782597429881736,
        A = -0.0033183852377923046,
    ),
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
        S = 0.18562082746743153,
        B = 0.04721449232084406,
        E = 0.08949445142799436,
        L = 0.21693855214948904,
        A = -0.03790232890765992,
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
        S = 0.008675734485345723,
        B = 0.0015943361995622697,
        E = 0.040678554011921275,
        L = 0.015195302502804976,
        A = -0.0116520520129552,
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
        S = 0.1180212565605515,
        B = 0.08775860460420218,
        E = 0.05568697475795268,
        L = 0.2016815577476462,
        A = 0.0029601407811171297,
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
        S = -0.12806097199831207,
        B = 0.015990976946081408,
        E = 0.20909291303181632,
        L = -0.12443996526698298,
        A = -0.09093262844756156,
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
        S = -0.029615360353623783,
        B = -0.007898692835079137,
        E = -0.09531273410799841,
        L = -0.19354593740012943,
        A = 0.014658545625941518,
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
        S = 0.007260652161790062,
        B = -0.019608298352048255,
        E = 0.08716594394733002,
        L = -0.03946903406605129,
        A = -0.012569303869677462,
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
        S = -0.15545191669249764,
        B = 0.015723482595002072,
        E = 0.016107577793424574,
        L = -0.4312654105293372,
        A = -0.05319284187641501,
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
        S = -0.07358009220414996,
        B = 0.025412694033294696,
        E = -0.27736877782186964,
        L = -0.08685131245280023,
        A = -0.03309135594988068,
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
        S = -0.0026112231250797714,
        B = -0.010342990798979887,
        E = -0.04226435270267846,
        L = -0.11456869584117083,
        A = -0.006626527736911,
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
        S = -0.044814000969530574,
        B = -0.0316015177548259,
        E = -0.014740608474173186,
        L = -0.2401473336579794,
        A = -0.028194151476050228,
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
        S = -0.002857074404458967,
        B = -0.005842048823449559,
        E = -0.008457349089571636,
        L = 0.040885926421141215,
        A = -0.003337867864941886,
    ),
    )


entry(
    index = 0,
    label = "s3_5_5_diene",
    group = 'OR{s3_5_5_diene_1_4}',
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
        S = -0.07729428947114099,
        B = -0.005367591679971025,
        E = 0.031398578620052214,
        L = -0.2630169305410398,
        A = -0.04135863674125002,
    ),
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
        S = 0.15106922959119704,
        B = 0.06899946104010037,
        E = 0.036258884869996795,
        L = 0.23504333068162395,
        A = -0.004147959795363535,
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
        S = -0.04531685291468504,
        B = 0.024729007428776054,
        E = 0.03210005828823307,
        L = 0.3458080470319716,
        A = 0.08835719286194355,
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
        S = -0.01686007902840032,
        B = -0.03327676910348611,
        E = 0.035851861645979755,
        L = -0.06700898525939296,
        A = -0.05573942879717143,
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
        S = -0.08263624910476483,
        B = 0.0022423058480392113,
        E = 0.08574770054208154,
        L = 0.2319544284465204,
        A = 0.011940636137465403,
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
        S = 0.28293731687178486,
        B = 0.02960863203254666,
        E = 0.11157387817603491,
        L = -0.02529598673864424,
        A = 0.025611325616424898,
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
        S = -0.1420747403518126,
        B = 0.03691740327221985,
        E = 0.08984316338386662,
        L = -0.16882379694198132,
        A = 0.014795446253527203,
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
        S = 0.014870398011771965,
        B = -0.026572789910686,
        E = 0.09905856015890203,
        L = 0.48000700536347274,
        A = -0.024256487929465984,
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
        S = -0.0017083835045384032,
        B = -0.031074863303531028,
        E = 0.08911874783872187,
        L = -0.0871603204888662,
        A = -0.06655987216915925,
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
        S = -0.03156361528202194,
        B = 0.04345864412350675,
        E = 0.09409907242457756,
        L = 0.10462003428794035,
        A = 0.05928514719046707,
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
        S = 0.03328855611701749,
        B = 0.0008496559544225721,
        E = 0.07117202742303842,
        L = -2.821166508819387,
        A = 0.004783891592536567,
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
        S = 0.11538648389532127,
        B = -0.018134318682193087,
        E = 0.14198921090001967,
        L = 0.11039964073189097,
        A = 0.02456217695666499,
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
        S = -2.2541249376173692e-05,
        B = -0.05283796247099433,
        E = 0.0589189670771469,
        L = 0.000729589636318413,
        A = -0.026970099650886654,
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
        S = 0.0050778346051960676,
        B = -0.020606320736720852,
        E = 0.07783921267193675,
        L = 0.14403205018160664,
        A = 0.007103916206511477,
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
        S = -0.007998400950869393,
        B = 0.012405896560834493,
        E = 0.06726077266629926,
        L = -0.2889634003749843,
        A = -0.0014418692709662127,
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
        S = -0.0139465890658432,
        B = -0.0531274865934961,
        E = 0.006736832165237199,
        L = -0.08029624548626975,
        A = -0.038592351052484805,
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
        S = 0.05755809215491203,
        B = -0.0034971508395671962,
        E = 0.035978185219713084,
        L = 0.04610411020386498,
        A = -0.025353854065273,
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
        S = 0.0946652627573544,
        B = 0.013960140801514377,
        E = -0.14385505865898623,
        L = 0.31285311422162754,
        A = 0.006095005776213093,
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_ene",
    group = 'OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_6}',
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
        S = -0.0012811229282714445,
        B = 0.06355676711497259,
        E = 0.22389899913258335,
        L = 0.30624978128345764,
        A = 0.04848115510086404,
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
        S = 0.010223949128683161,
        B = -0.040182311867867485,
        E = 0.2650203802366783,
        L = 0.3031867844375546,
        A = 0.03374564466172028,
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
        S = -0.03978143902654026,
        B = 0.0023617626777887677,
        E = -0.021239630604342082,
        L = -0.21767464817287036,
        A = -0.018721352251303756,
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
        S = -0.11368422566617918,
        B = 0.055881276427358774,
        E = -0.013289346190129933,
        L = -0.20144289814578495,
        A = -0.03153745959016955,
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
        S = 0.041289156262379195,
        B = -0.03413403815378354,
        E = 0.24580037191780757,
        L = 0.2403891819475176,
        A = 0.015581518086810435,
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
        S = -0.07657097053555584,
        B = 0.011283414566732944,
        E = 0.09792144208037977,
        L = -0.026952046689295878,
        A = -0.02028723701365103,
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
        S = 0.05164894897122314,
        B = 0.04196439904755128,
        E = 0.07728224806984757,
        L = -0.19276457285223228,
        A = -0.018573169082267953,
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
        S = -0.047701132485804945,
        B = 0.04673065854323917,
        E = -0.02056122522595262,
        L = -0.2806489606213609,
        A = 0.0017589920061044115,
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
        S = 0.06613826230473964,
        B = 0.02069038884317458,
        E = 0.1685698229657316,
        L = -0.11141594543198557,
        A = -0.025892144401782356,
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
        S = 0.019510453946335788,
        B = 0.02163502467281505,
        E = 0.0940248401595669,
        L = 0.08000223370015866,
        A = -0.004435026567036603,
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
        S = 0.248502474355874,
        B = -0.020076304446844644,
        E = -0.09255169944511885,
        L = 0.539538258208057,
        A = 0.005425701516089068,
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
        S = -0.003358665543016624,
        B = 0.010553380730018201,
        E = 0.14042461663349867,
        L = 0.09699993660934572,
        A = -0.006849903698115256,
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
        S = 0.10861680991284886,
        B = 0.012177023560395005,
        E = 0.04788026471439062,
        L = 0.3930529512618549,
        A = 0.019309685410801827,
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
        S = -0.06016022185089723,
        B = 0.013389072326093931,
        E = -0.014983964196839247,
        L = -0.27470936248066347,
        A = 0.021576115850889206,
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
        S = 0.1263206878868315,
        B = -0.02422902570674891,
        E = -0.14552907522702097,
        L = 0.456379461467586,
        A = 0.005850039355147004,
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
        S = 0.19892341552372989,
        B = -0.02080111657200259,
        E = 0.20330523015645213,
        L = 0.4500873958712777,
        A = 0.018672705943755915,
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
        S = 0.14249207852326473,
        B = -0.006752393359664945,
        E = 0.10153631311473453,
        L = 0.3173388210648216,
        A = -0.009299971219513845,
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
        S = 0.04625998088612571,
        B = 0.002727432762634594,
        E = -0.09758439790676807,
        L = 0.13228544502595282,
        A = 0.016053249441006123,
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
        S = 0.02498308249487674,
        B = -0.032009383653474104,
        E = 0.1294919593858194,
        L = 0.4053203560756859,
        A = -0.028477418979276466,
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
        S = -0.0726496581719444,
        B = 0.003161250671974572,
        E = -0.02679729121616261,
        L = -0.30323332980948975,
        A = -0.014433711889675719,
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
        S = -0.09706970130093596,
        B = 0.004491888732756192,
        E = 0.004892744567505933,
        L = -0.4610812919518422,
        A = -0.047665672980663695,
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
        S = -0.1584938810036697,
        B = -0.0021608621474047897,
        E = 0.025367605569924102,
        L = -0.15956147222954387,
        A = -0.029112915815176426,
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
        S = -0.03315012986157415,
        B = -0.008380116853960512,
        E = 0.007421341521114411,
        L = -0.18162829977259562,
        A = -0.025743762035480594,
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
        S = -0.02031681531626593,
        B = -0.0022930808383348246,
        E = 0.03427043800344526,
        L = 0.0003862655757375884,
        A = -0.006818431215710443,
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
        S = -0.028010088513867718,
        B = -0.0036260909733364533,
        E = 0.045788646908549745,
        L = -0.17182279563028352,
        A = -0.010663093128209677,
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
        S = -0.07828880572651581,
        B = 0.0014556210076759593,
        E = 0.006759399654392161,
        L = -0.3645110188525485,
        A = -0.016306422449773265,
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
        S = -0.03918076806608165,
        B = 0.0023750412160446314,
        E = 0.11151378260496697,
        L = -0.032408036996998214,
        A = 0.0030270010641847873,
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
        S = -0.007882229466012495,
        B = 0.010623675585595137,
        E = 0.10825296751317542,
        L = 0.20464068286900214,
        A = 0.003419897387841737,
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
        S = -0.05479000035751257,
        B = -0.00881258920826138,
        E = -0.02369696268580656,
        L = -0.2889420464434734,
        A = -0.017732553645463608,
    ),
    )


entry(
    index = 0,
    label = "s3_5_6_ene",
    group = 'OR{s3_5_6_ene_1}',
    solute = None,
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
        S = -0.01730939909471693,
        B = -0.0016763610944611949,
        E = 0.03551185419696384,
        L = -0.05054370868482905,
        A = -0.005365796291005066,
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
        S = -0.01730939909471693,
        B = -0.001676361094461195,
        E = 0.03551185419696381,
        L = -0.05054370868482906,
        A = -0.005365796291005064,
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
        S = -0.009433759876769032,
        B = -0.0030431886461141622,
        E = 0.030590673452772936,
        L = -0.009103423277042265,
        A = -0.004697216064816465,
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
        S = -0.030745814684344744,
        B = -0.002974252265386702,
        E = 0.0391481756105842,
        L = 0.025158512815335897,
        A = -0.009704883874974897,
    ),
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
        S = -0.01743417285044962,
        B = -0.0007826231509490012,
        E = -0.0202646928416699,
        L = -0.283344872348416,
        A = -0.020022948664404065,
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
	L2: s2_6_7
		L3: s2_6_7_ben
			L4: s2_6_7_ben_ene
				L5: s2_6_7_ben_ene_1
	L2: s4_6_6
		L3: s4_6_6_ane
	L2: s1_6_6
		L3: s1_6_6_ane
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
	L2: s2_6_6
		L3: s2_6_6_tetraene
			L4: s2_6_6_tetraene_0_2_6_8
		L3: s2_6_6_ben_ene
			L4: s2_6_6_ben_ene_2
			L4: s2_6_6_ben_ene_1
		L3: s2_6_6_naphthalene
		L3: s2_6_6_ben
		L3: s2_6_6_ene
			L4: s2_6_6_ene_1
			L4: s2_6_6_ene_m
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
	L2: s2_3_6
		L3: s2_3_6_ene
			L4: s2_3_6_ene_2
			L4: s2_3_6_ene_1
		L3: s2_3_6_ane
	L2: s2_3_5
		L3: s2_3_5_ene
			L4: s2_3_5_ene_1
		L3: s2_3_5_ane
""",
)