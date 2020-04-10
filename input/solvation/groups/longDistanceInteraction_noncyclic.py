name = "Long distance interaction correction for non-cyclic molecule" 
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
    index = 7,
    label = "CsCs-ST",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    solute = SoluteData(
        S = -0.01735025315636698,
        B = -0.008902245704012208,
        E = 0.0008088976103491292,
        L = -0.012639399151936364,
        A = 0.015630254805286393,
    ),
    )


entry(
    index = 2,
    label = "CsCs-S",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    Cs                          u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1,
    label = "CsCs",
    group = 
"""
1 *1 Cs u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 0,
    label = "int14_gauche",
    group = 
"""
1 *1 [Cs,O2s,Cd,S2s] u0 {2,S}
2 *2 Cs              u0 {1,S}
""",
    solute = None,
)


entry(
    index = 8,
    label = "CsCs-SQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
""",
    solute = SoluteData(
        S = -0.009378543887737458,
        B = -0.040985476007635864,
        E = 0.02217751344561246,
        L = 0.00858330811821799,
        A = -0.039983156067219104,
    ),
    )


entry(
    index = 9,
    label = "CsCs-TT",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    solute = SoluteData(
        S = -0.02994702757581017,
        B = -0.030044192466379776,
        E = 0.008876261919761444,
        L = 0.05848587433690633,
        A = 0.012565000242507781,
    ),
    )


entry(
    index = 2,
    label = "CsCs-T",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
""",
    solute = None,
)


entry(
    index = 10,
    label = "CsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
""",
    solute = SoluteData(
        S = 0.0068953543163717,
        B = -0.035599069529216966,
        E = 0.01953382542352557,
        L = 0.14579974163624695,
        A = -0.014917005629350822,
    ),
    )


entry(
    index = 9,
    label = "CsCs-T(TTP)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
13    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
14    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    solute = SoluteData(
        S = -0.010510046789982928,
        B = -0.012742845171331675,
        E = 0.0017184720488613097,
        L = 0.002157083053427908,
        A = 0.00637674071525182,
    ),
    )


entry(
    index = 11,
    label = "CsCs-QQ",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs u0 {1,S} {6,S} {7,S} {8,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {2,S}
7    Cs u0 {2,S}
8    Cs u0 {2,S}
""",
    solute = SoluteData(
        S = 0.014634136870042887,
        B = -0.03671955474222926,
        E = 0.03211617686552552,
        L = 0.10420324699529607,
        A = -0.02622469149076431,
    ),
    )


entry(
    index = 2,
    label = "CsCs-Q",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 0,
    label = "CsCsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {3,S} {4,S} {5,S} {9,S}
2 *2 Cs                          u0 {3,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S} {2,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
9    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.028754780553908475,
        B = -0.014234763890025407,
        E = 0.009648500020947888,
        L = -0.025892286617562894,
        A = -0.00934167596534359,
    ),
    )


entry(
    index = 0,
    label = "CsCsCs",
    group = 
"""
1 *2 Cs u0 {3,S} {4,S} {5,S} {6,S}
2 *1 Cs u0 {3,S} {7,S} {8,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {1,S}
7    Cs u0 {2,S}
8    Cs u0 {2,S}
""",
    solute = None,
)


entry(
    index = 0,
    label = "int15",
    group = 
"""
1 *2 Cs           u0 {3,S} {4,S} {5,S} {6,S}
2 *1 Cs           u0 {3,S} {7,S} {8,S}
3    [Cs,O2s,S2s] u0 {1,S} {2,S}
4    Cs           u0 {1,S}
5    Cs           u0 {1,S}
6    Cs           u0 {1,S}
7    Cs           u0 {2,S}
8    Cs           u0 {2,S}
""",
    solute = None,
)


entry(
    index = 9,
    label = "CsCs-T(TTS)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    Cs                          u0 {4,S}
13    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
14    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    solute = SoluteData(
        S = -0.006756458650703445,
        B = -0.008191829038713325,
        E = 0.0015466248439754537,
        L = -0.03525862525191313,
        A = 0.0040993333169476,
    ),
    )


entry(
    index = 0,
    label = "CsCsCs-QQ",
    group = 
"""
1 *1 Cs u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs u0 {3,S} {7,S} {8,S} {9,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {1,S}
7    Cs u0 {2,S}
8    Cs u0 {2,S}
9    Cs u0 {2,S}
""",
    solute = SoluteData(
        S = 0.011690544150247437,
        B = -0.01485759782858449,
        E = 0.016006850665327848,
        L = -0.035703207331562584,
        A = -0.008249598762547475,
    ),
    )


entry(
    index = 21,
    label = "CdCs-ST",
    group = 
"""
1 *2 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd                          u0 {1,S} {6,D} {7,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cd                          u0 {2,D}
7    Cs                          u0 {2,S}
""",
    solute = SoluteData(
        S = 1.2688975700995156e-05,
        B = -0.024572625647447575,
        E = -0.022075178319082855,
        L = -0.10268276001288183,
        A = 0.0024937848715071383,
    ),
    )


entry(
    index = 19,
    label = "CdCs-S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3    Cs u0 {1,S}
4 *2 Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 18,
    label = "CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Cd u0 {1,D}
3 *2 Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 16,
    label = "OsCs-ST",
    group = 
"""
1 *2 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s                         u0 {1,S} {6,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
""",
    solute = SoluteData(
        S = 0.03617696040483294,
        B = 0.054666094464068615,
        E = -0.048767004485083434,
        L = -0.01759020896636364,
        A = 0.007099640678590457,
    ),
    )


entry(
    index = 14,
    label = "OsCs-S",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cs  u0 {1,S}
3    Cs  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 12,
    label = "OsCs",
    group = 
"""
1 *1 O2s u0 {2,S}
2 *2 Cs  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 17,
    label = "OsCs-SQ",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {2,S}
""",
    solute = SoluteData(
        S = 0.0006503458681820411,
        B = 0.007798077764915644,
        E = -0.038449236113098945,
        L = 0.23065275234761218,
        A = 0.002533248684971774,
    ),
    )


entry(
    index = 0,
    label = "CsOsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {3,S} {4,S} {5,S} {9,S}
2 *2 Cs                          u0 {3,S} {6,S} {7,S} {8,S}
3    O2s                         u0 {1,S} {2,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
9    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.010901087756788504,
        B = -0.004775110020549038,
        E = -0.04282179503154271,
        L = -0.06042518874440663,
        A = 0.0013205350819369625,
    ),
    )


entry(
    index = 0,
    label = "CsOsCs",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 {3,S} {7,S} {8,S}
3    O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    Cs  u0 {2,S}
8    Cs  u0 {2,S}
""",
    solute = None,
)


entry(
    index = 0,
    label = "CsSsCs-QQ",
    group = 
"""
1 *1 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3    S2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    Cs  u0 {2,S}
8    Cs  u0 {2,S}
9    Cs  u0 {2,S}
""",
    solute = SoluteData(
        S = 0.009429691461671897,
        B = 0.009914630823588321,
        E = 0.014704031437822193,
        L = -0.03341795249433326,
        A = 0.0069714629145603765,
    ),
    )


entry(
    index = 0,
    label = "CsSsCs",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 {3,S} {7,S} {8,S}
3    S2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    Cs  u0 {2,S}
8    Cs  u0 {2,S}
""",
    solute = None,
)


tree(
"""
L1: R
	L2: int15
		L3: CsSsCs
			L4: CsSsCs-QQ
		L3: CsOsCs
			L4: CsOsCs-TQ
		L3: CsCsCs
			L4: CsCsCs-QQ
			L4: CsCsCs-TQ
	L2: int14_gauche
		L3: OsCs
			L4: OsCs-S
				L5: OsCs-SQ
				L5: OsCs-ST
		L3: CdCs
			L4: CdCs-S
				L5: CdCs-ST
		L3: CsCs
			L4: CsCs-Q
				L5: CsCs-QQ
			L4: CsCs-T
				L5: CsCs-TQ
				L5: CsCs-TT
					L6: CsCs-T(TTS)
					L6: CsCs-T(TTP)
			L4: CsCs-S
				L5: CsCs-SQ
				L5: CsCs-ST
""",
)