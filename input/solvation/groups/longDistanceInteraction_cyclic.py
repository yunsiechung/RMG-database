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
        S = 0.015440962288059495,
        B = 0.0017673724900045588,
        E = 0.016913657357833154,
        L = 0.06281025878470489,
        A = 0.005580397877205374,
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
        S = 0.014327466066772898,
        B = -0.017084689536760577,
        E = 0.05353187759023954,
        L = 0.11425568850016546,
        A = 0.00859175325538136,
    ),
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
        S = 0.023541354532276536,
        B = -0.01680517365104264,
        E = 0.018428267120987055,
        L = 0.08683049451451008,
        A = 0.009405797809626307,
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
        S = 0.022651222030594394,
        B = 0.02542021536457931,
        E = -0.022761172383594347,
        L = -0.019358376135697155,
        A = 0.022343576309042414,
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
        S = -0.008636581058722741,
        B = 0.010078754824088747,
        E = 0.025584168810317106,
        L = 0.06821099648346107,
        A = -0.0018662753656116177,
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
        S = -0.010685535461736197,
        B = -0.012066314619410561,
        E = 0.07533165549670978,
        L = 0.046803629255660006,
        A = 0.0013495705917818436,
    ),
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
        S = 0.02290407294995593,
        B = -0.026482381884464598,
        E = 0.07379148484017568,
        L = 0.09483832296276379,
        A = -0.01124824127181048,
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
        S = -0.011619701468067338,
        B = 0.01412312241116447,
        E = -0.003802733393435431,
        L = 0.1085685498200328,
        A = 0.006173708730320979,
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
        S = -0.02493071579603772,
        B = 0.005683608128027184,
        E = 0.006261852164526933,
        L = -0.06289587294880168,
        A = -0.005534269474345078,
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
        S = 0.036550365467080875,
        B = -0.03559211470531718,
        E = 0.00035423109475214406,
        L = 0.03212035246193948,
        A = -0.004158245691501002,
    ),
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
        S = 0.013283065960741814,
        B = 0.0018772394397332539,
        E = 0.014288711697301396,
        L = -0.05973728427616988,
        A = -0.0738536703505799,
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
        S = -0.021497436132290486,
        B = -0.013803003990339385,
        E = 0.004539730604714861,
        L = -0.05468919387156761,
        A = -0.03526768908962064,
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
        S = -0.007903046481252554,
        B = 0.0011784109804519572,
        E = -0.03362293344737387,
        L = -0.18011242820764145,
        A = -0.11705671433438028,
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
        S = 0.034150185230807484,
        B = -0.03001033415590222,
        E = -0.011241404257405779,
        L = -0.03956787369990046,
        A = -0.018654434136894174,
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
        S = 0.013529593372838671,
        B = -0.015836470617223857,
        E = -0.008682530619556268,
        L = 0.04081958607616159,
        A = 0.01884375994890057,
    ),
    )


tree(
"""
L1: R
	L2: aromatic-para
		L3: p_OH
			L4: p_OH_CHO
			L4: p_OH_MeO
			L4: p_OH_OH
		L3: p_CHO
			L4: p_CHO_CHO
		L3: p_MeO
			L4: p_MeO_MeO
			L4: p_MeO_CHO
	L2: aromatic-ortho
		L3: o_OH
			L4: o_OH_MeO
			L4: o_OH_OH
		L3: o_CHO
			L4: o_CHO_CHO
			L4: o_CHO_MeO
			L4: o_CHO_CH3
		L3: o_MeO
			L4: o_MeO_MeO
		L3: o_C2H5
			L4: o_C2H5_C2H5
		L3: o_CH3
			L4: o_CH3_C2H5
			L4: o_CH3_CH3
""",
)