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
        S = -0.02354439046758264,
        B = -0.007696391750790957,
        E = 0.0003402076749553634,
        L = -0.010914834793816731,
        A = 0.015971748294885634,
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
        S = -0.004640102106442788,
        B = -0.036951444613928894,
        E = 0.018385224581845057,
        L = 0.0014567506492487094,
        A = -0.03166762085372862,
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
        S = -0.0359037465188237,
        B = -0.027251881061653063,
        E = 0.006915468064768619,
        L = 0.06035974299823418,
        A = 0.011359783252537484,
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
        S = -0.014016412349378502,
        B = -0.04822858405685972,
        E = 0.023709942406299766,
        L = 0.0904320800196394,
        A = -0.014092538410584502,
    ),
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
        S = 0.02240741113743785,
        B = -0.0137510165451375,
        E = 0.006772708838081518,
        L = -0.04873811409381724,
        A = -0.009220538238623923,
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
        S = -0.013712005088455772,
        B = -0.01530515918391837,
        E = 0.001052173560211691,
        L = -0.008577330792456457,
        A = 0.005912775653785716,
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
        S = 0.009133108783256783,
        B = -0.03210372378875687,
        E = 0.024881314788992928,
        L = 0.08003900916910014,
        A = -0.02188998505275806,
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
        S = -0.007182478855857883,
        B = -0.00801698814395739,
        E = 0.0009118837521834707,
        L = -0.039433686686794686,
        A = 0.0030971681996020436,
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
        S = 0.007137292207812729,
        B = -0.012727205636097614,
        E = 0.011719485698627968,
        L = -0.05317747953550033,
        A = -0.0072440571574750616,
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
        S = 0.007584599152979874,
        B = -0.021538795936753195,
        E = -0.01701567903363368,
        L = -0.10844649232713201,
        A = 0.0025165053690828693,
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
    index = 22,
    label = "CdCs-SQ",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd u0 {1,S} {6,D} {7,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
7    Cs u0 {2,S}
""",
    solute = SoluteData(
        S = -0.001905038893135751,
        B = -0.001446326517719455,
        E = -0.005296474779792259,
        L = 0.09894327961384472,
        A = -0.0009246070815292765,
    ),
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
        S = 0.03307501007372643,
        B = 0.06085227926068653,
        E = -0.04543842378324319,
        L = -0.03474933967860297,
        A = 0.012383633568590943,
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
        S = -0.001486814804074525,
        B = 0.01218320338892705,
        E = -0.05047004975003435,
        L = 0.22250687072271091,
        A = 0.0008660426305559414,
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
        S = -0.009069408610089652,
        B = -0.005491996456577414,
        E = -0.04016292566390439,
        L = -0.0526640762367282,
        A = 0.0012518404780405606,
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
        S = 0.019392227527024058,
        B = 0.003731600215710478,
        E = 0.007957364889238249,
        L = 0.008646041755925787,
        A = 0.015696363605763958,
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
				L5: CdCs-SQ
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