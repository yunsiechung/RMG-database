#!/usr/bin/env python
# encoding: utf-8

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
        S = -0.02678115184720035,
        B = -0.011243521250034354,
        E = -0.006950862186513421,
        L = -0.06985512715255904,
        A = -0.03257806787105071,
    ),
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
        S = -0.04965613522261422,
        B = 0.008393692811456006,
        E = -0.04700457916980601,
        L = -0.1269996191667133,
        A = -0.13138814618030012,
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
        S = -0.012238033664136666,
        B = 0.01146968036371983,
        E = -0.015163516643679795,
        L = 0.1205905757570004,
        A = 0.008469706274404387,
    ),
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
        S = -0.013677178172325206,
        B = 0.007257576952284303,
        E = 0.018750286461340027,
        L = 0.07143036456514641,
        A = -0.0007492035582228443,
    ),
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
        S = -0.0089962529943208,
        B = -0.01218789474289042,
        E = 0.05907577477989655,
        L = 0.09398704845638405,
        A = 0.005734925675685355,
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
        S = 0.006976324256955572,
        B = -0.005011417657232979,
        E = 0.033144436648075516,
        L = 0.03225063073572207,
        A = -3.666035419034662e-05,
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
        S = 0.023223169175430908,
        B = 0.017671377873057576,
        E = -0.019790203041333203,
        L = -0.013951387605037458,
        A = 0.011920672935943632,
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
        S = 0.014780476072956066,
        B = 0.0015698310636721021,
        E = 0.013734351133301969,
        L = 0.06662498795605573,
        A = 0.0021979153169533736,
    ),
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
        S = 0.010002529195170187,
        B = -0.018139846562919573,
        E = 0.030010127060326932,
        L = 0.12296684213905616,
        A = 0.007717966868743846,
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
        S = 0.00956238840607638,
        B = -0.0192475818540464,
        E = 0.012094358886379544,
        L = 0.08154807733117815,
        A = 0.008347546517170793,
    ),
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
        S = 0.027468144337867144,
        B = -0.005496938902807853,
        E = 0.0019888193414746434,
        L = -0.05446205829820941,
        A = -0.07983921641389058,
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
        S = 0.038010210443479124,
        B = -0.028464440952301332,
        E = -0.016855401977514277,
        L = -0.044483556060582866,
        A = -0.02267519373000539,
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
        S = 0.011384135949332113,
        B = -0.018245103025160365,
        E = -0.014457614846908903,
        L = 0.004193269001707425,
        A = 0.006074340466525844,
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
        S = 0.03240653980149021,
        B = -0.03135831091858667,
        E = -0.0009747892965889078,
        L = -0.03181004245942251,
        A = -0.0016379622274380918,
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
        S = 0.01975897101886766,
        B = -0.021557163850406555,
        E = 0.04417536557553183,
        L = 0.0378752660352623,
        A = -0.0038841882291138774,
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
        S = -0.026613507719163914,
        B = 0.004023169206518073,
        E = 0.0004620237742506726,
        L = -0.06638512510530889,
        A = -0.002890071473293455,
    ),
)

tree(
"""
L1: R
	L2: aromatic-ortho
		L3: o_OH
			L4: o_OH_OH
			L4: o_OH_MeO
		L3: o_CHO
			L4: o_CHO_CHO
			L4: o_CHO_CH3
			L4: o_CHO_MeO
		L3: o_vinyl
			L4: o_vinyl_CH3
		L3: o_MeO
			L4: o_MeO_MeO
		L3: o_CH3
			L4: o_CH3_CH3
			L4: o_CH3_C2H5
		L3: o_C2H5
			L4: o_C2H5_C2H5
	L2: aromatic-para
		L3: p_OH
			L4: p_OH_OH
			L4: p_OH_MeO
			L4: p_OH_CHO
		L3: p_MeO
			L4: p_MeO_MeO
			L4: p_MeO_CHO
		L3: p_CHO
			L4: p_CHO_CHO
"""
)

