name = "Long distance interaction correction for cyclic molecule" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
	 index = -1,
	 label = "R",
	     group = 
"""
1 * R ux
""",
	 solute = None, 
	 shortDesc = u"""""",
	 longDesc = 
u"""
""",
)
entry(
    index = 13,
    label = "o_CH3_C2H5",
    group = 
"""
1     C  u0 {2,S} {4,S} {6,S} {7,S}
2     C  u0 {1,S} {8,S} {9,S} {10,S}
3     C  u0 {5,S} {11,S} {12,S} {13,S}
4  *2 Cb u0 {1,S} {5,B}
5  *1 Cb u0 {3,S} {4,B}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {3,S}
12    H  u0 {3,S}
13    H  u0 {3,S}
""",
    solute = SoluteData(
        S = 0.008795291051148894,
        B = -0.014985162436107948,
        E = 0.04951920354082431,
        L = 0.09638309442105056,
        A = 0.00841781409036314,
    ),
    )


entry(
    index = 12,
    label = "o_CH3",
    group = 
"""
1    C  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cb u0 {1,S} {6,B}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6 *2 Cb u0 {2,B}
""",
    solute = None,
)


entry(
    index = 25,
    label = "aromatic-ortho",
    group = 
"""
1 *1 Cb u0 {2,B}
2 *2 Cb u0 {1,B}
""",
    solute = None,
)


entry(
    index = 14,
    label = "o_C2H5_C2H5",
    group = 
"""
1     C  u0 {3,S} {5,S} {7,S} {8,S}
2     C  u0 {4,S} {6,S} {9,S} {10,S}
3     C  u0 {1,S} {14,S} {15,S} {16,S}
4     C  u0 {2,S} {11,S} {12,S} {13,S}
5  *1 Cb u0 {1,S} {6,B}
6  *2 Cb u0 {2,S} {5,B}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {4,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {3,S}
15    H  u0 {3,S}
16    H  u0 {3,S}
""",
    solute = SoluteData(
        S = 0.018513853190674535,
        B = -0.015226518231621775,
        E = 0.017793967216263418,
        L = 0.08331922207133137,
        A = 0.0067185973660122125,
    ),
    )


entry(
    index = 14,
    label = "o_C2H5",
    group = 
"""
1    C  u0 {2,S} {3,S} {4,S} {5,S}
2    C  u0 {1,S} {6,S} {7,S} {8,S}
3 *1 Cb u0 {1,S} {9,B}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9 *2 Cb u0 {3,B}
""",
    solute = None,
)


entry(
    index = 12,
    label = "o_CH3_CH3",
    group = 
"""
1     C  u0 {3,S} {5,S} {6,S} {7,S}
2     C  u0 {4,S} {8,S} {9,S} {10,S}
3  *1 Cb u0 {1,S} {4,B}
4  *2 Cb u0 {2,S} {3,B}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    solute = SoluteData(
        S = 0.01428564401677473,
        B = 0.00180249125781764,
        E = 0.017273342825236383,
        L = 0.05896248143873155,
        A = 0.00394803876180569,
    ),
    )


entry(
    index = 9,
    label = "o_vinyl_CH3",
    group = 
"""
1     C  u0 {4,S} {6,S} {7,S} {8,S}
2     C  u0 {3,D} {5,S} {9,S}
3     C  u0 {2,D} {10,S} {11,S}
4  *2 Cb u0 {1,S} {5,B}
5  *1 Cb u0 {2,S} {4,B}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
""",
    solute = SoluteData(
        S = 0.005982424762005019,
        B = -0.004763464452955403,
        E = 0.02809345183982578,
        L = 0.048106951118075496,
        A = 0.0030932657770514705,
    ),
    )


entry(
    index = 6,
    label = "o_vinyl",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D} {5,S} {6,S}
3 *1 Cb u0 {1,S} {7,B}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7 *2 Cb u0 {3,B}
""",
    solute = None,
)


entry(
    index = 4,
    label = "o_MeO_MeO",
    group = 
"""
1     C  u0 {3,S} {7,S} {8,S} {9,S}
2     C  u0 {4,S} {10,S} {11,S} {12,S}
3     O  u0 {1,S} {5,S}
4     O  u0 {2,S} {6,S}
5  *1 Cb u0 {3,S} {6,B}
6  *2 Cb u0 {4,S} {5,B}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {1,S}
10    H  u0 {2,S}
11    H  u0 {2,S}
12    H  u0 {2,S}
""",
    solute = SoluteData(
        S = 0.03324094873636534,
        B = 0.02126406157826841,
        E = -0.017384659762868942,
        L = 0.006658443987137541,
        A = 0.012715457149540355,
    ),
    )


entry(
    index = 4,
    label = "o_MeO",
    group = 
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 Cb u0 {2,S} {7,B}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7 *2 Cb u0 {3,B}
""",
    solute = None,
)


entry(
    index = 24,
    label = "p_MeO_MeO",
    group = 
"""
1     C  u0 {3,S} {12,S} {13,S} {14,S}
2     C  u0 {4,S} {9,S} {10,S} {11,S}
3     O  u0 {1,S} {5,S}
4     O  u0 {2,S} {6,S}
5  *1 Cb u0 {3,S} {7,B}
6  *2 Cb u0 {4,S} {8,B}
7     Cb u0 {5,B} {8,B}
8     Cb u0 {6,B} {7,B}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {2,S}
12    H  u0 {1,S}
13    H  u0 {1,S}
14    H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.020555452271681752,
        B = -0.03777778933516083,
        E = 0.007375160087121149,
        L = 0.016212454430167673,
        A = -0.0096466516402212,
    ),
    )


entry(
    index = 24,
    label = "p_MeO",
    group = 
"""
1    C  u0 {2,S} {6,S} {7,S} {8,S}
2    O  u0 {1,S} {3,S}
3 *1 Cb u0 {2,S} {4,B}
4    Cb u0 {3,B} {5,B}
5    Cb u0 {4,B} {9,B}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9 *2 Cb u0 {5,B}
""",
    solute = None,
)


entry(
    index = 0,
    label = "aromatic-para",
    group = 
"""
1    Cb u0 {2,B} {3,B}
2    Cb u0 {1,B} {4,B}
3 *1 Cb u0 {1,B}
4 *2 Cb u0 {2,B}
""",
    solute = None,
)


entry(
    index = 7,
    label = "o_CHO_CH3",
    group = 
"""
1    C  u0 {3,S} {5,S} {6,S} {7,S}
2    C  u0 {4,S} {8,S} {9,D}
3 *2 Cb u0 {1,S} {4,B}
4 *1 Cb u0 {2,S} {3,B}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    O  u0 {2,D}
""",
    solute = SoluteData(
        S = -0.007213326986550839,
        B = 0.008456395843763351,
        E = 0.022548855270734487,
        L = 0.07670106046747646,
        A = -0.0019985744863452145,
    ),
    )


entry(
    index = 3,
    label = "o_CHO",
    group = 
"""
1    C  u0 {2,S} {3,S} {4,D}
2 *1 Cb u0 {1,S} {5,B}
3    H  u0 {1,S}
4    O  u0 {1,D}
5 *2 Cb u0 {2,B}
""",
    solute = None,
)


entry(
    index = 27,
    label = "p_MeO_CHO",
    group = 
"""
1     C  u0 {3,S} {8,S} {9,S} {10,S}
2     C  u0 {4,S} {11,D} {12,S}
3     O  u0 {1,S} {5,S}
4  *2 Cb u0 {2,S} {6,B}
5  *1 Cb u0 {3,S} {7,B}
6     Cb u0 {4,B} {7,B}
7     Cb u0 {5,B} {6,B}
8     H  u0 {1,S}
9     H  u0 {1,S}
10    H  u0 {1,S}
11    O  u0 {2,D}
12    H  u0 {2,S}
""",
    solute = SoluteData(
        S = 0.01867977488231437,
        B = -0.028567757386123008,
        E = 0.06400118203186271,
        L = 0.06085087611764407,
        A = -0.007694347038382608,
    ),
    )


entry(
    index = 3,
    label = "o_CHO_CHO",
    group = 
"""
1    C  u0 {3,S} {5,S} {8,D}
2    C  u0 {4,S} {6,S} {7,D}
3 *1 Cb u0 {1,S} {4,B}
4 *2 Cb u0 {2,S} {3,B}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    O  u0 {2,D}
8    O  u0 {1,D}
""",
    solute = SoluteData(
        S = -0.012169529324195195,
        B = 0.011112128050639514,
        E = -0.008954522319342111,
        L = 0.10438425833033933,
        A = 0.006133417126701416,
    ),
    )


entry(
    index = 25,
    label = "p_CHO_CHO",
    group = 
"""
1     C  u0 {3,S} {7,S} {10,D}
2     C  u0 {4,S} {8,D} {9,S}
3  *1 Cb u0 {1,S} {5,B}
4  *2 Cb u0 {2,S} {6,B}
5     Cb u0 {3,B} {6,B}
6     Cb u0 {4,B} {5,B}
7     H  u0 {1,S}
8     O  u0 {2,D}
9     H  u0 {2,S}
10    O  u0 {1,D}
""",
    solute = SoluteData(
        S = -0.02574445233133944,
        B = 0.002939053151520029,
        E = 0.0024223312082940303,
        L = -0.06841015229121433,
        A = -0.004646664338634138,
    ),
    )


entry(
    index = 25,
    label = "p_CHO",
    group = 
"""
1    C  u0 {2,S} {5,S} {6,D}
2 *1 Cb u0 {1,S} {3,B}
3    Cb u0 {2,B} {4,B}
4    Cb u0 {3,B} {7,B}
5    H  u0 {1,S}
6    O  u0 {1,D}
7 *2 Cb u0 {4,B}
""",
    solute = None,
)


entry(
    index = 11,
    label = "o_CHO_MeO",
    group = 
"""
1     C  u0 {3,S} {6,S} {7,S} {8,S}
2     C  u0 {4,S} {9,S} {10,D}
3     O  u0 {1,S} {5,S}
4  *1 Cb u0 {2,S} {5,B}
5  *2 Cb u0 {3,S} {4,B}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    O  u0 {2,D}
""",
    solute = SoluteData(
        S = -0.0021864195419016323,
        B = -0.01591213218671146,
        E = 0.06235590779893017,
        L = -0.011323307130873775,
        A = 0.0013208934142660905,
    ),
    )


entry(
    index = 15,
    label = "o_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O  u0 {1,S} {5,S}
4    O  u0 {2,S} {6,S}
5    H  u0 {3,S}
6    H  u0 {4,S}
""",
    solute = SoluteData(
        S = -0.024137881362416954,
        B = -0.01611786733864515,
        E = 0.0035635569755891696,
        L = -0.05416762386299009,
        A = -0.037349697186156106,
    ),
    )


entry(
    index = 15,
    label = "o_OH",
    group = 
"""
1 *1 Cb u0 {2,S} {3,B}
2    O  u0 {1,S} {4,S}
3 *2 Cb u0 {1,B}
4    H  u0 {2,S}
""",
    solute = None,
)


entry(
    index = 22,
    label = "p_OH_OH",
    group = 
"""
1    Cb u0 {2,B} {3,B}
2    Cb u0 {1,B} {4,B}
3 *1 Cb u0 {1,B} {5,S}
4 *2 Cb u0 {2,B} {6,S}
5    O  u0 {3,S} {7,S}
6    O  u0 {4,S} {8,S}
7    H  u0 {5,S}
8    H  u0 {6,S}
""",
    solute = SoluteData(
        S = 0.01005589644602817,
        B = 0.007677975639728849,
        E = -0.021670697277802194,
        L = -0.10867049098997612,
        A = -0.0660755444901218,
    ),
    )


entry(
    index = 22,
    label = "p_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {5,B}
4    O  u0 {1,S} {6,S}
5 *2 Cb u0 {3,B}
6    H  u0 {4,S}
""",
    solute = None,
)


entry(
    index = 16,
    label = "o_OH_MeO",
    group = 
"""
1    C  u0 {2,S} {6,S} {7,S} {8,S}
2    O  u0 {1,S} {3,S}
3 *2 Cb u0 {2,S} {4,B}
4 *1 Cb u0 {3,B} {5,S}
5    O  u0 {4,S} {9,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {5,S}
""",
    solute = SoluteData(
        S = 0.003853620867281946,
        B = 0.004655751483219834,
        E = -0.03216133942648203,
        L = -0.15490528156705524,
        A = -0.10568036920076383,
    ),
    )


entry(
    index = 26,
    label = "p_OH_CHO",
    group = 
"""
1    C  u0 {2,S} {7,D} {8,S}
2 *2 Cb u0 {1,S} {3,B}
3    Cb u0 {2,B} {4,B}
4    Cb u0 {3,B} {5,B}
5 *1 Cb u0 {4,B} {6,S}
6    O  u0 {5,S} {9,S}
7    O  u0 {1,D}
8    H  u0 {1,S}
9    H  u0 {6,S}
""",
    solute = SoluteData(
        S = 0.014866006093048367,
        B = -0.011352448080751214,
        E = -0.003597963834579326,
        L = 0.03733131900381534,
        A = -0.005831787796221804,
    ),
    )


entry(
    index = 23,
    label = "p_OH_MeO",
    group = 
"""
1     C  u0 {2,S} {8,S} {9,S} {10,S}
2     O  u0 {1,S} {3,S}
3  *2 Cb u0 {2,S} {5,B}
4     Cb u0 {5,B} {6,B}
5     Cb u0 {3,B} {4,B}
6  *1 Cb u0 {4,B} {7,S}
7     O  u0 {6,S} {11,S}
8     H  u0 {1,S}
9     H  u0 {1,S}
10    H  u0 {1,S}
11    H  u0 {7,S}
""",
    solute = SoluteData(
        S = 0.024888136706494552,
        B = -0.031169055050149615,
        E = -0.025187078431260647,
        L = -0.051289182777304404,
        A = -0.024875158193170686,
    ),
    )


tree(
"""
L1: R
	L2: aromatic-para
		L3: p_OH
			L4: p_OH_MeO
			L4: p_OH_CHO
			L4: p_OH_OH
		L3: p_CHO
			L4: p_CHO_CHO
		L3: p_MeO
			L4: p_MeO_CHO
			L4: p_MeO_MeO
	L2: aromatic-ortho
		L3: o_OH
			L4: o_OH_MeO
			L4: o_OH_OH
		L3: o_CHO
			L4: o_CHO_MeO
			L4: o_CHO_CHO
			L4: o_CHO_CH3
		L3: o_MeO
			L4: o_MeO_MeO
		L3: o_vinyl
			L4: o_vinyl_CH3
		L3: o_C2H5
			L4: o_C2H5_C2H5
		L3: o_CH3
			L4: o_CH3_CH3
			L4: o_CH3_C2H5
""",
)