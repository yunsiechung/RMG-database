#!/usr/bin/env python
# encoding: utf-8

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
        S = -0.019210180568089597,
        B = -0.0013718471622547446,
        E = 0.0012983765111619398,
        L = -0.017690538552214564,
        A = 0.012484281438863888,
    ),
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
        S = -0.025722222422190723,
        B = -0.02290965817519166,
        E = 0.01893162615226219,
        L = -0.030242000204771458,
        A = -0.025635166498791887,
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
        S = -0.06266688584244531,
        B = -0.02173327842634227,
        E = 0.016274858346373548,
        L = 0.031905497424796134,
        A = 0.0056754602502876285,
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
        S = 0.008101186963055817,
        B = -0.007486576367143617,
        E = 0.003608990378498489,
        L = -0.0835866366105008,
        A = 0.008910441867079214,
    ),
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
        S = -0.013418809185821815,
        B = 0.004302057075499487,
        E = 0.006176547662998522,
        L = -0.032658257005578395,
        A = 0.006976124102735123,
    ),
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
        S = -0.031237301888106923,
        B = -0.012657889486222615,
        E = 0.016378468036094582,
        L = 0.04778412101791641,
        A = -0.005957763871491428,
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
        S = -0.010353365105690855,
        B = -0.02374840267107539,
        E = 0.0250682525518633,
        L = 0.015017287224781269,
        A = -0.014874379132134281,
    ),
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
        S = 0.019930737888599316,
        B = 0.06224825405374003,
        E = -0.030584509317761667,
        L = -0.048146133962393624,
        A = 0.01301313843871556,
    ),
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
        S = -0.040412571447463574,
        B = -0.0025416952891898228,
        E = -0.027780784015045586,
        L = 0.1514195075463361,
        A = 0.0023940218128495824,
    ),
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
        S = -0.002943244604833988,
        B = -0.025645988647577708,
        E = -0.014980784490995845,
        L = -0.09699644252617191,
        A = 0.0018269375178330785,
    ),
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
        S = -0.001371991100968279,
        B = -0.00047004147745950957,
        E = 0.002306007932551771,
        L = 0.046441058941177726,
        A = -0.001624705490922527,
    ),
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
        S = 0.019626475933178626,
        B = -0.005760292597594357,
        E = -0.006921128971666045,
        L = 0.04687958565375387,
        A = -0.008709859216974739,
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
        S = -0.0006068562741274098,
        B = 0.005289569336622016,
        E = 0.02253674982375654,
        L = -0.09292404526961788,
        A = 0.010872534371186137,
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
        S = -0.012724457947324441,
        B = -0.00236835867415218,
        E = -0.04249538703080918,
        L = -0.05728688998784159,
        A = 0.0005856302302300942,
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
        S = 0.034769555646506835,
        B = 0.00539369654668091,
        E = -0.02492683785824779,
        L = -0.004641064500949273,
        A = 0.01811015457386952,
    ),
)

tree(
"""
L1: R
	L2: int14_gauche
		L3: CsCs
			L4: CsCs-S
				L5: CsCs-ST
				L5: CsCs-SQ
			L4: CsCs-T
				L5: CsCs-TT
					L6: CsCs-T(TTP)
					L6: CsCs-T(TTS)
				L5: CsCs-TQ
			L4: CsCs-Q
				L5: CsCs-QQ
		L3: OsCs
			L4: OsCs-S
				L5: OsCs-ST
				L5: OsCs-SQ
		L3: CdCs
			L4: CdCs-S
				L5: CdCs-ST
				L5: CdCs-SQ
	L2: int15
		L3: CsCsCs
			L4: CsCsCs-TQ
			L4: CsCsCs-QQ
		L3: CsOsCs
			L4: CsOsCs-TQ
		L3: CsSsCs
			L4: CsSsCs-QQ
"""
)

