#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values" 
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
    index = 1093,
    label = "O",
    group = 
"""
1 * O u0
""",
    solute = SoluteData(
        S = -0.026767150376487737,
        B = -0.008205140556768678,
        E = 0.0019334333594636008,
        L = -0.09063146591294212,
        A = -0.003015303774870977,
    ),
    )


entry(
    index = 1823,
    label = "Oc",
    group = 
"""
1 * O0sc u0 c-1
""",
    solute = SoluteData(
        S = -0.007184312134262608,
        B = 0.02704628124473719,
        E = -0.03407036187504577,
        L = 0.06700748678612983,
        A = 0.045529140601476274,
    ),
    )


entry(
    index = 1094,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    solute = SoluteData(
        S = 0.07179854275048453,
        B = 0.01996588189630844,
        E = -0.0642136922132283,
        L = 0.3508857565821049,
        A = -0.012490916248528163,
    ),
    )


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    solute = SoluteData(
        S = 0.09888442986765955,
        B = 0.044693787641265866,
        E = 0.10322737592833782,
        L = 0.5500491184906087,
        A = -0.03163232803672514,
    ),
    )


entry(
    index = 1922,
    label = "N1dc",
    group = 
"""
1 * N1dc u0 p2 {2,D}
2   R!H  ux {1,D}
""",
    solute = SoluteData(
        S = -0.06782153240746572,
        B = -0.01279261273579943,
        E = 0.037218271653571645,
        L = -0.16422171053431595,
        A = -0.011418782505746627,
    ),
    )


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    solute = SoluteData(
        S = 0.006213734445637208,
        B = -0.02559919415524572,
        E = 0.07768992014968672,
        L = 0.22197473420552583,
        A = -0.033683841589521445,
    ),
    )


entry(
    index = 1,
    label = "C",
    group = 
"""
1 * C u0
""",
    solute = None,
)


entry(
    index = 1099,
    label = "O2s-OsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10302641569093826,
        B = 0.06172634573937962,
        E = 0.15367107926367854,
        L = 0.7146679646852799,
        A = 0.14428927138249695,
    ),
    )


entry(
    index = 1097,
    label = "O2s",
    group = 
"""
1 * O2s u0
""",
    solute = None,
)


entry(
    index = 1152,
    label = "S2s-SsSs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05397686927091243,
        B = -0.002473052023725812,
        E = 0.23131455709074145,
        L = 0.8942899446857496,
        A = -0.007887538677680675,
    ),
    )


entry(
    index = 1152,
    label = "S2s-SS",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   S   ux {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    solute = None,
)


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    solute = None,
)


entry(
    index = 2029,
    label = "S4dd",
    group = 
"""
1 * S4dd u0
""",
    solute = SoluteData(
        S = 0.05462803554161576,
        B = -0.04578773482068887,
        E = 0.21009763830149178,
        L = 0.51722536289567,
        A = 0.01704469531851974,
    ),
    )


entry(
    index = 2024,
    label = "O2d-Sd",
    group = 
"""
1 * O2d u0 {2,D}
2   S   ux {1,D}
""",
    solute = SoluteData(
        S = 0.42369727136245816,
        B = 0.24418445497459992,
        E = 0.11017320464234688,
        L = 1.0401758155815024,
        A = 0.06020432331069315,
    ),
    )


entry(
    index = 1160,
    label = "S2d-C",
    group = 
"""
1 * S2d u0 {2,D}
2   C   u0 {1,D}
""",
    solute = SoluteData(
        S = 0.28357177737948364,
        B = 0.07165471724569172,
        E = 0.37412515331950164,
        L = 1.5435940800129737,
        A = 0.008924923173922123,
    ),
    )


entry(
    index = -1,
    label = "S2d",
    group = 
"""
1 * S2d u0
""",
    solute = None,
)


entry(
    index = 1811,
    label = "N3s-N3sHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.22377391488234147,
        B = 0.12208782506237784,
        E = 0.23038185097601055,
        L = 0.9878748659852842,
        A = 0.07862158994643369,
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    solute = None,
)


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    solute = SoluteData(
        S = 0.016088528542229384,
        B = 0.02096191318950799,
        E = 0.20582083591601893,
        L = 0.7758820652899521,
        A = -0.020284478090134436,
    ),
    )


entry(
    index = 1919,
    label = "N3t",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   R!H u0 {1,T}
""",
    solute = SoluteData(
        S = 0.388833333438237,
        B = 0.1474220362183651,
        E = 0.12223861446865703,
        L = 1.1883784736295908,
        A = 0.02741439986177837,
    ),
    )


entry(
    index = 20,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    solute = SoluteData(
        S = 0.017836879623976048,
        B = 0.037454287064390517,
        E = 0.04694581473796069,
        L = 0.25300044176244113,
        A = 0.05381615610937202,
    ),
    )


entry(
    index = 332,
    label = "Cs-CsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.09248348348916184,
        B = 0.012924420655971552,
        E = -0.0603847414724432,
        L = 0.3824659815180326,
        A = -0.029570272282073463,
    ),
    )


entry(
    index = 331,
    label = "Cs-CHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    solute = None,
)


entry(
    index = 346,
    label = "Cs-CsCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0038247546098641423,
        B = 0.0004868049430158775,
        E = -0.0020439977686122846,
        L = 0.5006807237820096,
        A = -0.0005783725395569428,
    ),
    )


entry(
    index = 345,
    label = "Cs-CCHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 390,
    label = "Cs-CsCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08698575579781374,
        B = 0.005993380900493567,
        E = 0.0623741780672236,
        L = 0.5321446312593636,
        A = -0.003718657243214499,
    ),
    )


entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 520,
    label = "Cs-CsCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08291225537171773,
        B = 0.03234821247655327,
        E = 0.09278155283968995,
        L = 0.49312255037231006,
        A = 0.11279169626681776,
    ),
    )


entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-CrCrHH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.005511011336442456,
        B = 0.013000866663362651,
        E = 0.026822603512832985,
        L = 0.5128177418902625,
        A = -0.00780606465872531,
    ),
    )


entry(
    index = 1823,
    label = "Crs-CCHH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Oc-N5dc",
    group = 
"""
1 * O0sc u0 c-1 {2,S}
2   N5dc u0 c+1 {1,S}
""",
    solute = SoluteData(
        S = 0.2274679320828027,
        B = 0.11521175553320082,
        E = 0.11446239679606587,
        L = 0.7365490269234093,
        A = 0.08647908056982058,
    ),
    )


entry(
    index = 1944,
    label = "O2d-N5dc",
    group = 
"""
1 * O2d  u0 {2,D}
2   N5dc u0 {1,D}
""",
    solute = SoluteData(
        S = 0.06575000056557818,
        B = -0.08781399789869276,
        E = 0.05991311692460502,
        L = 0.22160114192283722,
        A = -0.1359466325949703,
    ),
    )


entry(
    index = 1823,
    label = "N3rs-CrCrCr",
    group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
    solute = SoluteData(
        S = -0.040381979515830294,
        B = -0.07840974638341405,
        E = 0.11314015267067871,
        L = 0.18221779626230122,
        A = -0.07699372133948675,
    ),
    )


entry(
    index = 1823,
    label = "N3rs-CrCrC",
    group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "N3rs-CCC",
    group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1939,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "N5dc-OdOsC",
    group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   C    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.07158385274029574,
        B = 0.07363577895520985,
        E = 0.05343453753823812,
        L = 0.34542407677167064,
        A = 0.024809048235699026,
    ),
    )


entry(
    index = 1823,
    label = "N5dc",
    group = 
"""
1 * N5dc u0 c+1
""",
    solute = None,
)


entry(
    index = 1932,
    label = "Cs-N5dcCsCsCs",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   Cs   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.16446255737607596,
        B = 0.0488484413650573,
        E = 0.04116242551665187,
        L = 0.715958066829623,
        A = 0.013006292197701802,
    ),
    )


entry(
    index = 1930,
    label = "Cs-NCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1802,
    label = "Cs-N3sCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09848045905886983,
        B = 0.18720494861430945,
        E = 0.04552602355008494,
        L = 0.6261551769667318,
        A = 0.012677315583062773,
    ),
    )


entry(
    index = 1921,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    solute = SoluteData(
        S = 0.10014209742742869,
        B = 0.13847349500886644,
        E = 0.1088437566445707,
        L = 0.6126218689959266,
        A = 0.028972873074045214,
    ),
    )


entry(
    index = 1127,
    label = "O2s-Cs(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.003621218015756126,
        B = 0.013709015160130952,
        E = -0.015515646233892271,
        L = 0.21610342368116456,
        A = -0.025370965552787176,
    ),
    )


entry(
    index = 1126,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1095,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO  u0 {1,D}
""",
    solute = SoluteData(
        S = 0.3965740729459134,
        B = 0.2469167196134368,
        E = 0.10169430080481458,
        L = 0.9225996420856096,
        A = 0.035892177540001055,
    ),
    )


entry(
    index = 394,
    label = "Cs-(Cds-Cds)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.05385985146057002,
        B = 0.06845704106332186,
        E = 0.07156434066182045,
        L = 0.5740824142046251,
        A = 0.02454852111955752,
    ),
    )


entry(
    index = 393,
    label = "Cs-(Cds-Cd)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 391,
    label = "Cs-CdsCsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1039,
    label = "Cs-CsCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0856413398130254,
        B = 0.042763696513874475,
        E = 0.008304726847304234,
        L = 0.35448737208434744,
        A = -0.012944912079535109,
    ),
    )


entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 334,
    label = "Cs-(Cds-O2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.07793995702698493,
        B = 0.055797560273061486,
        E = -0.05016535976624457,
        L = 0.30522443071535504,
        A = -0.025107469614137914,
    ),
    )


entry(
    index = 333,
    label = "Cs-CdsHHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 201,
    label = "Cds-CdsCsCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06113538108248526,
        B = -0.008335546065880996,
        E = 0.13112512992873673,
        L = 0.4533660690702717,
        A = -0.004292001977116961,
    ),
    )


entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    solute = None,
)


entry(
    index = 66,
    label = "Cds-OdCsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.019290169963772228,
        B = 0.045428449264884464,
        E = 0.05389595850182804,
        L = 0.30764445755011,
        A = -0.01742209009519838,
    ),
    )


entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = None,
)


entry(
    index = 121,
    label = "Cds-CdsHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.09248947420354546,
        B = 0.009436033831706391,
        E = 0.0072323990486349524,
        L = 0.35515433880155284,
        A = -0.0393402141693587,
    ),
    )


entry(
    index = 120,
    label = "Cds-CdHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 336,
    label = "Cs-(Cds-Cds)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.08152003937489773,
        B = 0.034744653947241404,
        E = -0.03954901852330774,
        L = 0.48607776138103265,
        A = -0.015010075321188605,
    ),
    )


entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 136,
    label = "Cds-CdsCsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0244007563643307,
        B = 0.022853403144824976,
        E = 0.0843472863555744,
        L = 0.5304135997813848,
        A = -0.013828875802386864,
    ),
    )


entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 350,
    label = "Cs-(Cds-Cds)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.0011870270044132489,
        B = 0.021792079356854174,
        E = -0.013171015499729795,
        L = 0.5067146225795655,
        A = 0.006004886670970209,
    ),
    )


entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 347,
    label = "Cs-CdsCsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 524,
    label = "Cs-(Cds-Cds)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.1528286245487465,
        B = 0.04146036339017517,
        E = 0.11512434239067033,
        L = 0.40211359585269923,
        A = 0.06442333772668708,
    ),
    )


entry(
    index = 523,
    label = "Cs-(Cds-Cd)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 521,
    label = "Cs-CdsCsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = None,
)


entry(
    index = 122,
    label = "Cds-CddHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.008986299017361345,
        B = 0.005587778936202772,
        E = 0.04652208410312769,
        L = 0.4564344623953374,
        A = -0.016982796910455504,
    ),
    )


entry(
    index = 49,
    label = "Cdd-CdsCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
    solute = SoluteData(
        S = -0.01192726901181581,
        B = 0.009837025150717719,
        E = 0.0632106367464903,
        L = 0.6297440891430165,
        A = -0.015406829667145894,
    ),
    )


entry(
    index = 41,
    label = "Cdd-CdCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   C   u0 {1,D}
""",
    solute = None,
)


entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = SoluteData(
        S = -0.022496628147921464,
        B = 0.01416452726246279,
        E = 0.030851832141054667,
        L = 0.4141259065663956,
        A = -0.013776151409836455,
    ),
    )


entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.011784820897168008,
        B = 0.01017702060116505,
        E = 0.061325975640391335,
        L = 0.5456537424550978,
        A = -0.011086481717167276,
    ),
    )


entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.003083418109102099,
        B = 0.0039092507640676386,
        E = 0.018573213749462657,
        L = 0.2573999734356026,
        A = -0.002744380706668932,
    ),
    )


entry(
    index = 140,
    label = "Cds-Cds(Cds-Cds)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.05976841315193485,
        B = 0.03368466261075186,
        E = 0.09850337348950662,
        L = 0.5771868629549023,
        A = 0.0012340108544195239,
    ),
    )


entry(
    index = 139,
    label = "Cds-Cds(Cds-Cd)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.004544971032549316,
        B = 0.003830994866837529,
        E = 0.06762057099826185,
        L = 0.646327782759908,
        A = -0.0027990917206686767,
    ),
    )


entry(
    index = 362,
    label = "Cs-(Cds-Cds)(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = -0.013130255517208745,
        B = 0.06643563156854317,
        E = -0.030438751137629963,
        L = 0.4028400847312419,
        A = 0.02366752669473744,
    ),
    )


entry(
    index = 361,
    label = "Cs-(Cds-Cd)(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = None,
)


entry(
    index = 354,
    label = "Cs-CdsCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 408,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 0.007176879768780591,
        B = 0.02538615278555102,
        E = 0.01495495038390905,
        L = 0.2911250392471071,
        A = 0.0068668581904590825,
    ),
    )


entry(
    index = 407,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = None,
)


entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 21,
    label = "Ct-CtH",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0835395871738788,
        B = 0.037337375415834886,
        E = 0.04079743696109471,
        L = 0.47655663723835257,
        A = 0.029955495525550338,
    ),
    )


entry(
    index = 340,
    label = "Cs-CtHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.06123894531280705,
        B = -0.006407052647446825,
        E = 0.02041023690103549,
        L = 0.18355177193030042,
        A = -0.03404308393943715,
    ),
    )


entry(
    index = 24,
    label = "Ct-CtCs",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.11940454653736629,
        B = 0.0876370400044183,
        E = 0.0842161490918245,
        L = 0.8700880114983374,
        A = 0.020064616500530374,
    ),
    )


entry(
    index = 23,
    label = "Ct-CtC",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   C  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 370,
    label = "Cs-CtCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.06314195455559304,
        B = -0.008839556160051379,
        E = 0.013041120784240738,
        L = 0.12152203467208236,
        A = -0.009307894320762471,
    ),
    )


entry(
    index = 144,
    label = "Cds-CdsCtH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.024982462176627963,
        B = 0.01698485064462393,
        E = -0.007050547458303967,
        L = 0.41241621604868,
        A = 0.007554876614755026,
    ),
    )


entry(
    index = 28,
    label = "Ct-Ct(Cds-Cds)",
    group = 
"""
1 * Ct u0 {2,S} {3,T}
2   Cd u0 {1,S} {4,D}
3   Ct u0 {1,T}
4   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.041174198741995016,
        B = 0.013316334283159937,
        E = 0.17615849921415525,
        L = 0.6264789010285234,
        A = -0.0053056362884132445,
    ),
    )


entry(
    index = 27,
    label = "Ct-Ct(Cds-Cd)",
    group = 
"""
1 * Ct u0 {2,S} {3,T}
2   Cd u0 {1,S} {4,D}
3   Ct u0 {1,T}
4   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct         u0 {2,T} {3,S}
2   Ct         u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 32,
    label = "Ct-CtCt",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0004423431610141778,
        B = 0.007440123740702923,
        E = 0.0963951754833858,
        L = 0.46580681482625574,
        A = 0.0028512702540381667,
    ),
    )


entry(
    index = 1129,
    label = "O2s-CsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06906319277393101,
        B = 0.22753325368034313,
        E = 0.19405411945934614,
        L = 0.7623322392929929,
        A = 0.020409672358617084,
    ),
    )


entry(
    index = 342,
    label = "Cs-OsHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.005425788221483999,
        B = 0.056674978747674215,
        E = -0.10219304132983469,
        L = 0.3198583697177304,
        A = -0.044288186558876834,
    ),
    )


entry(
    index = 1083,
    label = "Cs-CsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05980077331312201,
        B = 0.05323111318350809,
        E = -0.08347219081040608,
        L = 0.30477704640920106,
        A = -0.016983524768482094,
    ),
    )


entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 841,
    label = "Cs-CsCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.16097312038536876,
        B = 0.15189860153956944,
        E = 0.058007504347486506,
        L = 0.023268626682416443,
        A = 0.02609770869578392,
    ),
    )


entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1125,
    label = "O2s-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.026886130569581758,
        B = -0.012547018121274194,
        E = -0.08410116770470709,
        L = 0.1196200892014563,
        A = -0.02001123047541935,
    ),
    )


entry(
    index = 1122,
    label = "O2s-CdsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 126,
    label = "Cds-CdsOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02666570236217047,
        B = 0.07292647561170189,
        E = 0.08606497161398488,
        L = 0.4667831795852722,
        A = -0.0007184559787612065,
    ),
    )


entry(
    index = 125,
    label = "Cds-CdOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1128,
    label = "O2s-Cs(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   C   u0 {2,D}
""",
    solute = SoluteData(
        S = 0.03931671251465907,
        B = 0.07335677356684628,
        E = 0.027802608148640953,
        L = 0.23296754077843773,
        A = -0.04663360280363737,
    ),
    )


entry(
    index = 1087,
    label = "Cs-(Cds-Cds)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.05180250054428104,
        B = 0.0901592255104548,
        E = -0.11033732087474458,
        L = 0.29179097296155193,
        A = 0.014545194206771878,
    ),
    )


entry(
    index = 1086,
    label = "Cs-(Cds-Cd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 343,
    label = "Crs-OsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.00466014076866264,
        B = -0.023681198033219792,
        E = -0.15082143731353115,
        L = -0.02717402172346904,
        A = -0.036826390088469496,
    ),
    )


entry(
    index = 1028,
    label = "Cs-CsOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.049168178750908245,
        B = 0.03880742035321998,
        E = -0.13914500966152166,
        L = 0.007767963889692235,
        A = -0.001192732830312942,
    ),
    )


entry(
    index = 1027,
    label = "Cs-COsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 972,
    label = "Cs-CsCsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.029627157520251454,
        B = 0.01934738586555139,
        E = -0.019098212820323906,
        L = 0.11142561737805237,
        A = 0.0047781497587781885,
    ),
    )


entry(
    index = 971,
    label = "Cs-CCOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = None,
)


entry(
    index = 379,
    label = "Cs-CbCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.018806609328038855,
        B = -0.044277366516844455,
        E = 0.024533630912834146,
        L = 0.4269125755966495,
        A = -0.03170383678750355,
    ),
    )


entry(
    index = 10,
    label = "Cb-Cs",
    group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08661269004774153,
        B = 0.07337186494841612,
        E = 0.119294626862824,
        L = 0.5368543076362701,
        A = 0.016844532222036194,
    ),
    )


entry(
    index = 9,
    label = "Cb-C",
    group = 
"""
1 * Cb u0 {2,S}
2   C  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    solute = None,
)


entry(
    index = 7,
    label = "Cb-H",
    group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06535257462702555,
        B = 0.01832028096519729,
        E = 0.08874229878094986,
        L = 0.5515342996104056,
        A = 0.005165758583888552,
    ),
    )


entry(
    index = 1043,
    label = "Cs-(Cds-Cds)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.1007636914455226,
        B = 0.14323635235685903,
        E = -0.033755269058848195,
        L = 0.21509927113275693,
        A = 0.05770803918755595,
    ),
    )


entry(
    index = 1042,
    label = "Cs-(Cds-Cd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1040,
    label = "Cs-CdsCsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.015049786869828557,
        B = 0.04493731085030024,
        E = -0.01968268562971211,
        L = 0.1240947734983759,
        A = 0.023534746672368285,
    ),
    )


entry(
    index = 1850,
    label = "Ct-N3tCs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.20211341440665506,
        B = 0.0927446772213558,
        E = 0.008173563102801781,
        L = 0.38826373620580545,
        A = -0.030949025791636373,
    ),
    )


entry(
    index = 1942,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-CrOrsOsH",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.14894097710498572,
        B = -0.05561476015060267,
        E = -0.06700599640146575,
        L = -0.13217567215241524,
        A = -0.035698374237232544,
    ),
    )


entry(
    index = 1823,
    label = "Crs-COsOsH",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-OrsOrsHH",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.00323733182306908,
        B = -0.01687387570248556,
        E = -0.1573310500383246,
        L = -0.10835763768617844,
        A = -0.03357777068602005,
    ),
    )


entry(
    index = 1823,
    label = "Crs-CrOrsOsC",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04601843970149694,
        B = -0.0139804482791599,
        E = 0.055122316751941305,
        L = 0.15955462308817514,
        A = 0.12247518580771692,
    ),
    )


entry(
    index = 1823,
    label = "Crs-CCOsOs",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-OrsOrsCH",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09582292189986041,
        B = -0.019199081661575378,
        E = -0.07058562949632832,
        L = 0.09154668273634091,
        A = -0.014636074194955636,
    ),
    )


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    solute = SoluteData(
        S = 0.15690389154703718,
        B = 0.11454724110975333,
        E = 0.1720419247083608,
        L = 0.6417423035705887,
        A = 0.06109930110675582,
    ),
    )


entry(
    index = 55,
    label = "Cds-OdCsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.024596027938960242,
        B = 0.05284466530892,
        E = 0.025004549993265086,
        L = 0.22987585164368546,
        A = -0.08974948497288542,
    ),
    )


entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 348,
    label = "Cs-(Cds-O2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.012620003349672126,
        B = 0.06283255068194554,
        E = -0.011589667187273198,
        L = 0.39033898087570834,
        A = -0.0010742194900543746,
    ),
    )


entry(
    index = 392,
    label = "Cs-(Cds-O2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.12106554389801587,
        B = 0.053859613504232406,
        E = 0.06049003152494803,
        L = 0.5386665865540476,
        A = 0.04220994765515438,
    ),
    )


entry(
    index = 522,
    label = "Cs-(Cds-O2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.13222057851012564,
        B = 0.0810998324341867,
        E = 0.10351358571856557,
        L = 0.5269541496543336,
        A = 0.09793778002981957,
    ),
    )


entry(
    index = 57,
    label = "Cds-O2d(Cds-O2d)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.05648534217767513,
        B = -0.005977648185299922,
        E = 0.018517671693825753,
        L = 0.053196485777006385,
        A = -0.02916244392185217,
    ),
    )


entry(
    index = 56,
    label = "Cds-OdCdsH",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 79,
    label = "Cds-O2d(Cds-O2d)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.02369761855879738,
        B = -0.007366304124413684,
        E = 0.0326419626663608,
        L = 0.10288973673598742,
        A = -0.023199288309984363,
    ),
    )


entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = None,
)


entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 123,
    label = "Cds-(Cdd-O2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.029031419477030983,
        B = 0.02723247792669016,
        E = 0.08326550161462663,
        L = 0.4162481849867496,
        A = -0.006469933410175373,
    ),
    )


entry(
    index = 37,
    label = "Cdd-CdsOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.029031419477030997,
        B = 0.027232477926690136,
        E = 0.08326550161462681,
        L = 0.4162481849867498,
        A = -0.006469933410175367,
    ),
    )


entry(
    index = 36,
    label = "Cdd-CdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   O2d u0 {1,D}
""",
    solute = None,
)


entry(
    index = 1999,
    label = "Cd-Cd(CO)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.009929651071749798,
        B = 0.0777168572388299,
        E = 0.09673267628240816,
        L = 0.43102090761763634,
        A = -0.015051637767913028,
    ),
    )


entry(
    index = 59,
    label = "Cds-O2d(Cds-Cds)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.09988829923937834,
        B = -0.005491682930203324,
        E = 0.08771233216589712,
        L = 0.4689499245956553,
        A = -0.05464035840332288,
    ),
    )


entry(
    index = 58,
    label = "Cds-O2d(Cds-Cd)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1996,
    label = "Cd-CdCs(CO)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.023190148808702758,
        B = 0.08554660961034723,
        E = 0.11801665972142068,
        L = 0.3897738897259974,
        A = 0.005052307279451151,
    ),
    )


entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = None,
)


entry(
    index = 357,
    label = "Cs-(Cds-O2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.0075144008136488775,
        B = 0.0005238437247634811,
        E = 0.012042997679717149,
        L = 0.38153218303654585,
        A = 0.026570307017750365,
    ),
    )


entry(
    index = 356,
    label = "Cs-(Cds-O2d)(Cds-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    solute = None,
)


entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.05055524256372229,
        B = -0.01330283076713921,
        E = 0.09103968720534762,
        L = 0.19475091011653983,
        A = -0.06173660012757256,
    ),
    )


entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct         u0 {2,T} {3,S}
2   Ct         u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.020390476449984263,
        B = 0.01964006139063981,
        E = 0.08778472099784522,
        L = 0.5348550610518134,
        A = 0.012009947690506886,
    ),
    )


entry(
    index = 77,
    label = "Cds-OdCsCs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.11223658863530125,
        B = 0.04871384817935903,
        E = 0.0655798002917072,
        L = 0.5040140059103194,
        A = -0.06919083506769519,
    ),
    )


entry(
    index = 81,
    label = "Cds-O2d(Cds-Cds)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.14154911744099322,
        B = 0.043220652243818374,
        E = 0.09354929026113405,
        L = 0.35005784449593685,
        A = -0.04297386834189341,
    ),
    )


entry(
    index = 80,
    label = "Cds-O2d(Cds-Cd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1085,
    label = "Cs-(Cds-O2d)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.153528284536588,
        B = 0.04226972613758036,
        E = -0.07203574684271777,
        L = 0.06985893352736527,
        A = 0.03973044327498149,
    ),
    )


entry(
    index = 355,
    label = "Cs-(Cds-O2d)(Cds-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.2277030145370596,
        B = -0.054019884906281596,
        E = 0.053503408581236644,
        L = 0.13015129331381622,
        A = 0.013192726669523177,
    ),
    )


entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0094005606999664,
        B = -0.006519994952177289,
        E = 0.033932647806479865,
        L = 0.28700901044985944,
        A = -0.03521624582367401,
    ),
    )


entry(
    index = 12,
    label = "Cb-(Cds-O2d)",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * Cb  u0 {1,S}
3   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.060331200436193964,
        B = -0.03831436616921612,
        E = 0.08497405352069914,
        L = 0.5600545900043522,
        A = -0.03147730488458525,
    ),
    )


entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.016941833686915812,
        B = 0.03425039075013175,
        E = 0.10382223289747738,
        L = 0.1702701615173817,
        A = -0.017714029666120734,
    ),
    )


entry(
    index = 1141,
    label = "S2s-CdCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08989050818553125,
        B = 0.012628033167615975,
        E = 0.07854247213743117,
        L = 0.8453184672242997,
        A = 0.028222907999959385,
    ),
    )


entry(
    index = -1,
    label = "S2s-CC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1180,
    label = "Cds-CdsS2H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.012680561359817093,
        B = 0.036694004091799556,
        E = 0.06973886153202326,
        L = 0.4679956772362668,
        A = 0.007869034702179157,
    ),
    )


entry(
    index = 1180,
    label = "Cds-CdsSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Cds-CdSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 53,
    label = "Cds-OdOsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04401695421118792,
        B = 0.013640225871818606,
        E = 0.13115828256314024,
        L = 0.2810167568858371,
        A = -0.05450525067705078,
    ),
    )


entry(
    index = 1106,
    label = "O2s-CsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19839433758116246,
        B = 0.3053896407209747,
        E = 0.22873988429219694,
        L = 1.000538392641614,
        A = 0.25633506363920544,
    ),
    )


entry(
    index = 1101,
    label = "O2s-CH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1105,
    label = "O2s-(Cds-Cd)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    solute = SoluteData(
        S = 0.020090348537328113,
        B = 0.12239122264910193,
        E = 0.12220623760896326,
        L = 0.5976118269222527,
        A = 0.14298492027037601,
    ),
    )


entry(
    index = 1103,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1041,
    label = "Cs-(Cds-O2d)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.2802045906545474,
        B = 0.03487335064641779,
        E = -0.06409476252654135,
        L = -0.14083084920922467,
        A = 0.12064255659091076,
    ),
    )


entry(
    index = 171,
    label = "Cds-Cds(Cds-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.044005186290509236,
        B = 0.06709385735713279,
        E = 0.17524169923965796,
        L = 0.45231327933128795,
        A = -0.00020149225579566864,
    ),
    )


entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = None,
)


entry(
    index = 168,
    label = "Cds-CdCO",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = None,
)


entry(
    index = 52,
    label = "Cds-OdOsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.022233105199946892,
        B = 0.019486743679759673,
        E = 0.031714532348410096,
        L = 0.2350216820801229,
        A = -0.030346380604868006,
    ),
    )


entry(
    index = 1124,
    label = "O2s-(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {4,D}
4   C   u0 {3,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.008007562306622473,
        B = 0.000343480172701479,
        E = -0.05049561264098544,
        L = 0.07941055225608383,
        A = -0.012917851491033595,
    ),
    )


entry(
    index = 169,
    label = "Cds-CdsCsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09117471579555489,
        B = 0.024165337127385805,
        E = 0.09475400267127326,
        L = 0.3773025796333499,
        A = -0.016408082747565965,
    ),
    )


entry(
    index = 1995,
    label = "Cd-CdCsOs",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,D}
""",
    solute = None,
)


entry(
    index = 70,
    label = "Cds-O2d(Cds-Cds)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.005812667640875963,
        B = -0.03471475691391445,
        E = 0.04165562823715865,
        L = 0.28909583828500385,
        A = 0.007459059842357948,
    ),
    )


entry(
    index = 69,
    label = "Cds-O2d(Cds-Cd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = None,
)


entry(
    index = 205,
    label = "Cds-Cds(Cds-Cds)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.17835585964454695,
        B = 0.00923267472113068,
        E = 0.13972745174037934,
        L = 0.6143312966100225,
        A = -0.010962852452338735,
    ),
    )


entry(
    index = 204,
    label = "Cds-Cds(Cds-Cd)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.00016901601624547303,
        B = 0.009693865706847464,
        E = 0.05153597164696753,
        L = 0.12904780798577792,
        A = -0.004347674778954581,
    ),
    )


entry(
    index = 68,
    label = "Cds-O2d(Cds-O2d)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.03510179633198374,
        B = 0.013927474418288985,
        E = 0.06967798982288569,
        L = 0.1733879032728192,
        A = -0.004517901674583988,
    ),
    )


entry(
    index = 1104,
    label = "O2s-(Cds-O2d)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.025698351806233647,
        B = 0.035370931848208456,
        E = 0.025878796161603698,
        L = 0.37697644113173934,
        A = 0.23666899278194656,
    ),
    )


entry(
    index = 52,
    label = "Cds-Od(OsH)",
    group = 
"""
1 * CO  u0 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   H   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.025698351806233425,
        B = 0.03537093184820829,
        E = 0.025878796161606706,
        L = 0.37697644113173717,
        A = 0.23666899278194514,
    ),
    )


entry(
    index = 843,
    label = "Cs-(Cds-O2d)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.11049838372305848,
        B = -0.00012177988153904828,
        E = -0.026087874123448974,
        L = 0.4159796482388067,
        A = -0.14133030799505722,
    ),
    )


entry(
    index = 842,
    label = "Cs-CdsCsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    solute = None,
)


entry(
    index = 372,
    label = "Cs-(Cds-O2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.0013953047803001517,
        B = -0.0018134227925267093,
        E = 0.015414005861857425,
        L = 0.1523932530450613,
        A = -0.005712270221345674,
    ),
    )


entry(
    index = 371,
    label = "Cs-CtCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1832,
    label = "Cs-(CtN3t)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.13320812443006413,
        B = 0.023646908195826537,
        E = -0.0063877670150096644,
        L = 0.3210390251008419,
        A = -0.028288274395350782,
    ),
    )


entry(
    index = 1834,
    label = "Cs-(CtN3t)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.017879934463404624,
        B = 0.00889233105535951,
        E = 0.04816242973826188,
        L = 0.13679507857643072,
        A = 0.0001923023277677964,
    ),
    )


entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1858,
    label = "Cd-CdCs(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   N3t u0 {3,T}
""",
    solute = SoluteData(
        S = 0.013364435322442683,
        B = 0.0064987235787400234,
        E = 0.03286332965936551,
        L = 0.30676342909457627,
        A = -0.002984172220934297,
    ),
    )


entry(
    index = 225,
    label = "Cds-CdsCtCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1851,
    label = "Ct-N3tCd",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.04165703193180645,
        B = 0.05366693365313681,
        E = 0.012934158317937965,
        L = -0.12450712045897633,
        A = -0.030368333111586418,
    ),
    )


entry(
    index = 374,
    label = "Cs-(Cds-Cds)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.0038802230482563984,
        B = 0.010390860600030695,
        E = -0.01620452517250739,
        L = 0.13571008156200945,
        A = -0.0030387637517299147,
    ),
    )


entry(
    index = 373,
    label = "Cs-(Cds-Cd)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1837,
    label = "Cds-Cd(CtN3t)(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Ct  u0 {1,S} {5,T}
3   Ct  u0 {1,S} {6,T}
4   Cd  u0 {1,D}
5   N3t u0 {2,T}
6   N3t u0 {3,T}
""",
    solute = SoluteData(
        S = 0.043067195778447705,
        B = 0.02462853393294026,
        E = 0.06595668859370966,
        L = 0.5088579595439598,
        A = -0.011187769167342931,
    ),
    )


entry(
    index = 233,
    label = "Cds-CdsCtCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1810,
    label = "N3s-CsCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0930439887509633,
        B = 0.09221559539299137,
        E = 0.046461472171031235,
        L = 0.29594871568572884,
        A = 0.011468278155648024,
    ),
    )


entry(
    index = 1921,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15957882869296622,
        B = 0.09438752181654077,
        E = 0.05363438936027049,
        L = 0.6812397659257032,
        A = 0.0036699412305205925,
    ),
    )


entry(
    index = 1800,
    label = "Cs-N3sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05026206585147421,
        B = 0.16477893148268613,
        E = -0.009456141694989052,
        L = 0.5799339638337544,
        A = -0.04608638421116902,
    ),
    )


entry(
    index = 1919,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1942,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08057183926932852,
        B = -0.01781660040196903,
        E = 0.028466103430817746,
        L = 0.12178330982131379,
        A = -0.011288543862331494,
    ),
    )


entry(
    index = 378,
    label = "Cs-CtCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0062074618895520736,
        B = 0.003311108194286228,
        E = -0.007620771256132022,
        L = 0.011172945935781319,
        A = 0.010630830426280304,
    ),
    )


entry(
    index = 1833,
    label = "Cs-(CtN3t)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.04194383585945775,
        B = -5.78130597878028e-05,
        E = 0.011787481871900282,
        L = 0.2910800807353392,
        A = -0.00223854055399414,
    ),
    )


entry(
    index = 398,
    label = "Cs-CtCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1919,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.021607738814098845,
        B = 0.01474758101559332,
        E = 0.0006583758472467068,
        L = 0.4592132451964153,
        A = -0.004643065219452231,
    ),
    )


entry(
    index = 1919,
    label = "CJ2_singlet",
    group = 
"""
1 * C u0 p1
""",
    solute = SoluteData(
        S = -0.002627928075808337,
        B = -0.009187062384924043,
        E = -0.008846929467681841,
        L = 0.2019975233869321,
        A = -0.008252619881662784,
    ),
    )


entry(
    index = 1808,
    label = "N3s-CsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.135726711805429,
        B = 0.2914982388441256,
        E = 0.12300307206420617,
        L = 0.7414806550980918,
        A = 0.10681159226414365,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1803,
    label = "Cs-N3sCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09395060943901265,
        B = 0.16963018952313327,
        E = 0.07564572617994834,
        L = 0.5985429730962835,
        A = 0.001171688531355665,
    ),
    )


entry(
    index = 1927,
    label = "Cs-NCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1804,
    label = "Cs-N3sCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.21956205949011154,
        B = 0.1543479337239354,
        E = 0.1291919302126533,
        L = 0.7222927108551196,
        A = 0.04679410224757537,
    ),
    )


entry(
    index = 1823,
    label = "Crs-CrCrN3sH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   N  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06993330502325618,
        B = 0.10544429891377999,
        E = 0.08253261752343902,
        L = 0.5449842178021209,
        A = 0.008437508586553573,
    ),
    )


entry(
    index = 1823,
    label = "Crs-NCCH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1809,
    label = "N3s-CsCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.008886015779636092,
        B = 0.2091844956139176,
        E = 0.07632107973697042,
        L = 0.4994758675905717,
        A = 0.07559392558085923,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-CrN3rsCH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   N  u0 r1 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04170106120572301,
        B = 0.1577941871085031,
        E = 0.11465122774556936,
        L = 0.5167573235561554,
        A = 0.03288530780707586,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0745388426714902,
        B = 0.1349208710827761,
        E = 0.12202813309091147,
        L = 0.6299302529280528,
        A = 0.0906667160607813,
    ),
    )


entry(
    index = 1853,
    label = "Ct-N3tN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1210745763865604,
        B = -0.025692598079187355,
        E = -0.02579141751330087,
        L = 0.45704600179348437,
        A = 0.05201112379537392,
    ),
    )


entry(
    index = 1826,
    label = "N3s-(CO)CsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.2785201306422956,
        B = 0.024979152444055172,
        E = 0.06645566249436222,
        L = 0.7685636785682785,
        A = 0.19902721311226196,
    ),
    )


entry(
    index = 1889,
    label = "N3s-CdHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.004254652790667806,
        B = 0.21142320749283536,
        E = 0.20207649569318442,
        L = 0.7354424074274784,
        A = 0.19224906275924264,
    ),
    )


entry(
    index = 1906,
    label = "N3d-CdH",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   H        u0 {1,S}
""",
    solute = SoluteData(
        S = 0.003112565764733259,
        B = 0.2705328975363719,
        E = 0.14364524011694801,
        L = 0.5108612995490222,
        A = -0.01682800943537383,
    ),
    )


entry(
    index = 1904,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    solute = None,
)


entry(
    index = 1911,
    label = "N3d-CsR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cs  u0 {1,S}
3   R!H u0 {1,D}
""",
    solute = SoluteData(
        S = 0.16048068510423877,
        B = 0.22065861378868754,
        E = 0.31903935490199614,
        L = 1.059161718401159,
        A = 0.06401361732509883,
    ),
    )


entry(
    index = 1871,
    label = "Cs-(N3dCd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.12934556840233566,
        B = 0.09074346818086844,
        E = -0.18354644518792268,
        L = 0.3764141164598575,
        A = 0.0544694084105616,
    ),
    )


entry(
    index = 1925,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1823,
    label = "N3rs-CrCrC",
    group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.018546198331403675,
        B = -0.018168198512020815,
        E = 0.09826230280451574,
        L = 0.3602485715395137,
        A = -0.07699670924588681,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0194889222419191,
        B = 0.09555412132496181,
        E = 0.15427085525449039,
        L = 0.5683894069699231,
        A = 0.16359040989928522,
    ),
    )


entry(
    index = 1130,
    label = "O2s-CsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09816483400391088,
        B = 0.07999028099503938,
        E = 0.15468317600494152,
        L = 0.5356701174442234,
        A = -0.048393200530684084,
    ),
    )


entry(
    index = 8,
    label = "Cb-O2s",
    group = 
"""
1 * Cb  u0 {2,S}
2   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13491614766593055,
        B = 0.07644466250787195,
        E = 0.10604178616091765,
        L = 0.6745607970238386,
        A = 0.05203617462105567,
    ),
    )


entry(
    index = 1907,
    label = "N3d-N3dCs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09946028260590924,
        B = 0.021211863967183036,
        E = 0.073856065683453,
        L = 0.6201551885569544,
        A = -0.0034432858451650763,
    ),
    )


entry(
    index = 1805,
    label = "Cs-(N3dN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.09946028260590888,
        B = 0.021211863967183008,
        E = 0.07385606568345321,
        L = 0.6201551885569516,
        A = -0.00344328584516508,
    ),
    )


entry(
    index = 1926,
    label = "Cs-N5dcCsHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10184656355643913,
        B = 0.04048638532831856,
        E = -0.023394801741148375,
        L = 0.7446467647175061,
        A = -0.008457143681458683,
    ),
    )


entry(
    index = 1929,
    label = "Cs-N5dcCsCsH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   H    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.037303705278591344,
        B = 0.014533930828629915,
        E = 0.0072711221583148826,
        L = 0.3395620514441868,
        A = -0.0005755517106395547,
    ),
    )


entry(
    index = 1825,
    label = "N3s-(CO)HH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.25323400857277467,
        B = 0.14369791028017329,
        E = 0.11251439020684725,
        L = 0.9455371748078899,
        A = 0.27221398128696866,
    ),
    )


entry(
    index = 1823,
    label = "Cds-OdN3sH",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.15636862147237182,
        B = 0.032318501428094684,
        E = 0.0874880872495025,
        L = 0.6076096026507085,
        A = 0.013444263771218157,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sCs",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.26735751141473735,
        B = 0.09040171723826045,
        E = 0.10961674385160926,
        L = 0.631084545175373,
        A = 0.058597834157579375,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sC",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   C   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = None,
)


entry(
    index = 1827,
    label = "N3s-(CO)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.1971566754269369,
        B = -0.01965215996033951,
        E = 0.08090273932190006,
        L = 0.5791744288071827,
        A = -0.027953295560245076,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sC",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   C   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.0741744637781046,
        B = 0.12017728416581254,
        E = 0.13915111017615847,
        L = 0.3554991541180295,
        A = 0.06973502864717207,
    ),
    )


entry(
    index = 1847,
    label = "O2s-Cs(N3dOd)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d u0 {2,D}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03133081250149045,
        B = 0.03248555217486804,
        E = 0.06877594443722092,
        L = 0.3274325666877775,
        A = -0.0027710353306661436,
    ),
    )


entry(
    index = 1875,
    label = "O2s-CsN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3d u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1935,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1943,
    label = "O2d-N3d",
    group = 
"""
1 * O2d u0 {2,D}
2   N3d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.17299798943162933,
        B = 0.041087092310573274,
        E = -0.05281016647313091,
        L = 0.31905472249533473,
        A = -0.013521765778107576,
    ),
    )


entry(
    index = 1909,
    label = "N3d-OdOs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03133081250149043,
        B = 0.03248555217486807,
        E = 0.06877594443722097,
        L = 0.32743256668777915,
        A = -0.0027710353306661262,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sN3s",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N3s u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.024079529436163122,
        B = 0.013398548915472914,
        E = 0.07999145832617123,
        L = 0.24093885526219166,
        A = 0.055095732268941246,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sN",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = None,
)


entry(
    index = 1829,
    label = "N3s-(CO)(CO)H",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.045233010954798425,
        B = 0.053970918625564426,
        E = 0.08291789574427705,
        L = 0.4901766079524447,
        A = 0.15327981732242202,
    ),
    )


entry(
    index = 1939,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.023230697809213875,
        B = -0.027898176984276216,
        E = 0.14452837251842793,
        L = 0.4454718943469411,
        A = -0.10745204686529136,
    ),
    )


entry(
    index = 399,
    label = "Cs-CbCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03789418622655731,
        B = -0.03411940041329466,
        E = 0.0800566513963274,
        L = 0.403801119312832,
        A = -0.0023344183490949942,
    ),
    )


entry(
    index = 1824,
    label = "Crds-OdN3rsCr",
    group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.07120894305167806,
        B = 0.03188650625316485,
        E = 0.12224098586286737,
        L = 0.32431325599948496,
        A = 0.02966948555980882,
    ),
    )


entry(
    index = 1925,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06156286876956741,
        B = -0.020525696661719852,
        E = -0.16658736058454066,
        L = 0.08052317726263955,
        A = -0.04561021999653492,
    ),
    )


entry(
    index = 1870,
    label = "Cs-(N3dCd)HHH",
    group = 
"""
1 * Cs       u0 {2,S} {3,S} {4,S} {5,S}
2   N3d      u0 {1,S} {6,D}
3   H        u0 {1,S}
4   H        u0 {1,S}
5   H        u0 {1,S}
6   [Cd,Cdd] u0 {2,D}
""",
    solute = SoluteData(
        S = -0.06232296730267416,
        B = 0.027334236882678692,
        E = -0.2714053702603613,
        L = -0.19993093337640402,
        A = -0.026934185660206875,
    ),
    )


entry(
    index = 1920,
    label = "Cs-N3dHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1935,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10141624219283858,
        B = -0.015643346083503196,
        E = 0.002197619034119442,
        L = 0.3040096000793857,
        A = -0.04591780885181115,
    ),
    )


entry(
    index = 1823,
    label = "N5dc",
    group = 
"""
1 * N5dc u0 c+1
""",
    solute = SoluteData(
        S = 0.17546691758476465,
        B = 0.0768273983794934,
        E = 0.02502406402339125,
        L = 0.54876390285092,
        A = 0.11021447671046551,
    ),
    )


entry(
    index = 1133,
    label = "S2s-CsH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13056749799008727,
        B = 0.0851629217786123,
        E = 0.20956469635529168,
        L = 1.0587891326178016,
        A = -0.02982036238564184,
    ),
    )


entry(
    index = -1,
    label = "S2s-CH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Cs-CSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1624898673617473,
        B = 0.06152921934422281,
        E = 0.11794526099924203,
        L = 0.8243078487600561,
        A = 0.03329478981012989,
    ),
    )


entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.09745074506394383,
        B = 0.058310232208190024,
        E = 0.04221379078885406,
        L = 0.10737547939323559,
        A = 0.01365415251070609,
    ),
    )


entry(
    index = 1123,
    label = "O2s-(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.015966971551242142,
        B = -0.019641457527673722,
        E = 0.002548896288561337,
        L = -0.022724265411766562,
        A = -0.026137120546595033,
    ),
    )


entry(
    index = 531,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.08184386379438942,
        B = 0.06715083910199363,
        E = 0.1629248598456894,
        L = 0.2890191362900773,
        A = 0.010948354405736833,
    ),
    )


entry(
    index = 530,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1111,
    label = "O2s-O2s(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.08044333931063496,
        B = -0.005149426321008761,
        E = -0.06152385111612311,
        L = 0.21503644522099605,
        A = 0.023287309405323208,
    ),
    )


entry(
    index = 1110,
    label = "O2s-OsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   O2s     u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1108,
    label = "O2s-OsC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1091,
    label = "Cs-CtOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.04731128892906555,
        B = 0.01723115448399599,
        E = -0.06076217879318071,
        L = -0.15216760391429185,
        A = -0.009692256165275288,
    ),
    )


entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.17882123517686668,
        B = 0.09340530585678267,
        E = 0.09502794365014222,
        L = 0.6100932649783573,
        A = 0.03391709011119565,
    ),
    )


entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0036404138864381554,
        B = 0.03268096746474734,
        E = -0.09244371638106635,
        L = 0.17999723141630772,
        A = -0.06012589313511387,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCsCs",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
""",
    solute = SoluteData(
        S = 0.20267975565910967,
        B = 0.12057935102032824,
        E = 0.09457277638201661,
        L = 0.7610240410923427,
        A = -0.026674745309871337,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    solute = None,
)


entry(
    index = 2041,
    label = "S4d-Od",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   O2d ux {1,D}
""",
    solute = None,
)


entry(
    index = 2030,
    label = "S4d",
    group = 
"""
1 * S4d u0
""",
    solute = None,
)


entry(
    index = 1162,
    label = "Cs-S4HHH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   [S4s,S4d,S4b,S4t] u0 {1,S}
3   H                 u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    solute = SoluteData(
        S = 0.20317440161355846,
        B = 0.1401892143137371,
        E = 0.1162152731556778,
        L = 0.886438582712276,
        A = -0.03176085368952831,
    ),
    )


entry(
    index = 1162,
    label = "Cs-SsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1163,
    label = "Cs-CsS4HH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2591776512102947,
        B = 0.16636645752191825,
        E = 0.12930908686338063,
        L = 0.8699000924821685,
        A = -0.022926561311606686,
    ),
    )


entry(
    index = 1163,
    label = "Cs-CsSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 2013,
    label = "S6rdd-CCOdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux r1 {1,S}
5   C    ux r1 {1,S}
""",
    solute = SoluteData(
        S = -0.029792161448719563,
        B = -0.06056302223357579,
        E = 0.01547314870004919,
        L = -0.07322123699906562,
        A = -0.041194885639265565,
    ),
    )


entry(
    index = 2013,
    label = "S6dd-OdOdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    solute = None,
)


entry(
    index = 2044,
    label = "S6dd-OdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    solute = None,
)


entry(
    index = 2031,
    label = "S6dd",
    group = 
"""
1 * S6dd u0
""",
    solute = None,
)


entry(
    index = 1823,
    label = "Crs-CrSrHH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   S  u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03589108424673295,
        B = 0.0375407416658656,
        E = 0.14124419738435892,
        L = 0.5382359639060035,
        A = -0.03862482050953252,
    ),
    )


entry(
    index = 1823,
    label = "Crs-CSHH",
    group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 2020,
    label = "S6dd-OdOdOO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   O    ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = -0.005192762612414898,
        B = -0.0002498032464246232,
        E = -0.005677525424930036,
        L = 0.16099662836703407,
        A = -0.006973267221242531,
    ),
    )


entry(
    index = 2025,
    label = "O2s-CS6",
    group = 
"""
1 * O2s                     u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   C                       ux {1,S}
""",
    solute = SoluteData(
        S = -0.06047507697823226,
        B = -0.02110770735864377,
        E = 0.02398876842774392,
        L = 0.06778434210491079,
        A = -0.022628225620298637,
    ),
    )


entry(
    index = 2028,
    label = "O2s-CS",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    solute = None,
)


entry(
    index = 2013,
    label = "S6dd-OdOdCsCs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    solute = SoluteData(
        S = -0.0025359110024577524,
        B = 0.020739239050266613,
        E = -0.02295137705059708,
        L = 0.2627903732112546,
        A = -0.030885646648968892,
    ),
    )


entry(
    index = 1202,
    label = "Cs-CsCsSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.04627914171963524,
        B = 0.007967249403165417,
        E = -0.10830229163088961,
        L = -0.29354670856052456,
        A = -0.008706779075037878,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1163,
    label = "Cs-CsS6HH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.004731402951286665,
        B = 0.019600946479476668,
        E = 0.14446814865700514,
        L = 0.5552878969213842,
        A = -0.027560229080878577,
    ),
    )


entry(
    index = 2003,
    label = "S4d-OdCS",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux {1,S}
4   S   ux {1,S}
""",
    solute = SoluteData(
        S = 0.051007643294460114,
        B = 0.018376574488881758,
        E = 0.13734602993872214,
        L = 0.6609190867741546,
        A = -0.0069271134128634495,
    ),
    )


entry(
    index = -1,
    label = "S2s-S46C",
    group = 
"""
1 * S2s                                 u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   C                                   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05100764329446013,
        B = 0.01837657448888177,
        E = 0.13734602993872222,
        L = 0.6609190867741541,
        A = -0.006927113412863461,
    ),
    )


entry(
    index = -1,
    label = "S2s-SC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    solute = None,
)


entry(
    index = 1164,
    label = "Cs-CdsSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.07807415389555902,
        B = 0.08594417487812381,
        E = 0.12826688636447856,
        L = 0.7662535097124589,
        A = 0.0058343106063969375,
    ),
    )


entry(
    index = 1463,
    label = "S2s-Cs(C=O)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.02123820381691292,
        B = -0.0014513741148009349,
        E = 0.11366081971062443,
        L = 0.31262548864796996,
        A = -0.015933346065617582,
    ),
    )


entry(
    index = 1162,
    label = "Cs-S2sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03308667570597221,
        B = 0.026039211379484548,
        E = 0.09383848522573236,
        L = 0.7479944250671409,
        A = -0.05708812864605547,
    ),
    )


entry(
    index = 1455,
    label = "CO-CsSs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0014662560447614179,
        B = 0.01056917200673195,
        E = 0.07513344146766779,
        L = 0.47115999406724063,
        A = -0.005016842100456493,
    ),
    )


entry(
    index = 1163,
    label = "Cs-CsS2HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06310934171410527,
        B = 0.07474551036567557,
        E = 0.12478508226870867,
        L = 0.7851598559395426,
        A = -0.016987057230602745,
    ),
    )


entry(
    index = 1154,
    label = "S2s-(C=S2d)Cs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   S2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.08050379373377015,
        B = -0.00450353772826058,
        E = 0.16469550566052996,
        L = 0.7785220311298051,
        A = -0.006568297737028515,
    ),
    )


entry(
    index = 1139,
    label = "S2s-CsCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.010274849407864352,
        B = 0.014170787088878093,
        E = 0.09851931360869107,
        L = 0.3522941765919763,
        A = -0.019922990677069548,
    ),
    )


entry(
    index = 1137,
    label = "S2s-CsCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.12281940412580429,
        B = 0.15165408175771758,
        E = 0.12358061238075932,
        L = 0.8545812312865595,
        A = 0.017137831214394956,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCsOs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = 0.007735900391689804,
        B = 0.02475681285705898,
        E = -0.059347065726366645,
        L = -0.019145571332609967,
        A = -0.00015649603129987396,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    solute = None,
)


entry(
    index = 2026,
    label = "O2s-S_DeH",
    group = 
"""
1 * O2s            u0 {2,S} {3,S}
2   [S4d,S6d,S6dd] ux {1,S}
3   H              ux {1,S}
""",
    solute = SoluteData(
        S = 0.1665902296195626,
        B = 0.06778338246386939,
        E = -0.0073735848772332364,
        L = 0.5774796983010657,
        A = 0.05222384658855958,
    ),
    )


entry(
    index = 2027,
    label = "O2s-SH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   H   ux {1,S}
""",
    solute = None,
)


entry(
    index = 1162,
    label = "Cs-S6HHH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
3   H                       u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09681702132598373,
        B = 0.023159684299264075,
        E = 0.007558636605494792,
        L = 0.6012083917487011,
        A = -0.041021325490125625,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = 0.11042644137829263,
        B = 0.05251469971914981,
        E = -0.04177200222129842,
        L = 0.15374353663887846,
        A = 0.04338232547447496,
    ),
    )


entry(
    index = 1197,
    label = "Cb-S6dd",
    group = 
"""
1 * Cb   u0 {2,S}
2   S6dd u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15093514093335028,
        B = 0.025080189379137984,
        E = 0.1675766763655408,
        L = 0.7292536541169025,
        A = -0.011060599956055524,
    ),
    )


entry(
    index = 1197,
    label = "Cb-S",
    group = 
"""
1 * Cb u0 {2,S}
2   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 341,
    label = "Cs-CbHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.06269546720394074,
        B = -0.04472018502372714,
        E = -0.021889366449775693,
        L = 0.43407772370767506,
        A = -0.043525673931537466,
    ),
    )


entry(
    index = 1113,
    label = "O2s-OsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0010944184362831632,
        B = 0.07781232728040959,
        E = 0.019699101158602496,
        L = 0.6365507861704699,
        A = -0.01871792351916027,
    ),
    )


entry(
    index = 12,
    label = "Cb-(Cds-O2dOs)",
    group = 
"""
1   CO  u0 {2,S} {3,D} {4,S}
2 * Cb  u0 {1,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.10815984333754375,
        B = -0.09036715327075323,
        E = 0.1000709551730179,
        L = 0.2987104584909943,
        A = 0.023044253397029753,
    ),
    )


entry(
    index = 75,
    label = "Cds-OdCbOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09092661993167755,
        B = 0.1095313789509286,
        E = 0.08308113819876577,
        L = 0.47546818165487265,
        A = -0.022272016286011158,
    ),
    )


entry(
    index = 529,
    label = "Cs-CbCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.14154613923518222,
        B = -0.004609213156447775,
        E = 0.13813006106242728,
        L = 0.5789692785878092,
        A = 0.0031706976499941996,
    ),
    )


entry(
    index = 14,
    label = "Cb-(Cds-Cds)",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * Cb u0 {1,S}
3   Cd u0 {1,D}
""",
    solute = SoluteData(
        S = 0.12170316051448277,
        B = 0.03220622556059443,
        E = 0.20504987455686438,
        L = 0.9351365772201914,
        A = 0.011313435066969177,
    ),
    )


entry(
    index = 13,
    label = "Cb-(Cds-Cd)",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * Cb u0 {1,S}
3   C  u0 {1,D}
""",
    solute = None,
)


entry(
    index = 145,
    label = "Cds-CdsCbH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.036799871187599795,
        B = -0.009713625330472207,
        E = 0.053681613258272656,
        L = 0.1889392695831582,
        A = -0.05141630496416275,
    ),
    )


entry(
    index = 234,
    label = "Cds-CdsCbCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03839486630612241,
        B = 0.008728799571347454,
        E = 0.05477333781481709,
        L = 0.23307459993517773,
        A = -0.0002465315888324997,
    ),
    )


entry(
    index = 18,
    label = "Cb-Ct",
    group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S}
""",
    solute = SoluteData(
        S = 0.002879750957165524,
        B = 0.008655660023286833,
        E = 0.07140334254342827,
        L = 0.3697293321945487,
        A = 0.01809393402563152,
    ),
    )


entry(
    index = 33,
    label = "Ct-CtCb",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = 0.002879750957165516,
        B = 0.008655660023286826,
        E = 0.07140334254342826,
        L = 0.3697293321945482,
        A = 0.018093934025631492,
    ),
    )


entry(
    index = 19,
    label = "Cb-Cb",
    group = 
"""
1 * Cb u0 {2,S}
2   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08092475183376689,
        B = 0.02160042905472576,
        E = 0.16732444345563882,
        L = 0.5637808254649919,
        A = -0.011327448421572954,
    ),
    )


entry(
    index = 383,
    label = "Cs-(Cds-Cds)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.02544325880330746,
        B = 0.0021109430370527143,
        E = -0.00485689089895823,
        L = 0.3957766999253172,
        A = -0.014007046324029689,
    ),
    )


entry(
    index = 382,
    label = "Cs-(Cds-Cd)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 518,
    label = "Cs-CbCbCbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.027813535416242076,
        B = -0.0033090046475859015,
        E = -0.027699335464657818,
        L = -0.41109792908978726,
        A = -0.007522433673556442,
    ),
    )


entry(
    index = 3,
    label = "Cbf-CbCbCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cb  u0 {1,B}
4   Cbf u0 {1,B}
""",
    solute = SoluteData(
        S = 0.09225391327688633,
        B = 0.026748060273399744,
        E = 0.23585489761987233,
        L = 0.4684735397006549,
        A = -0.009806358048227954,
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    solute = None,
)


entry(
    index = 432,
    label = "Cs-CbCbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03527407656415149,
        B = -0.013521329606433942,
        E = 0.06704252824598574,
        L = 0.3296230383272161,
        A = -0.029380596654917546,
    ),
    )


entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.17230590736556065,
        B = 0.04105173037828887,
        E = 0.064828645275576,
        L = 0.33707072329263854,
        A = 0.06228818571509615,
    ),
    )


entry(
    index = 388,
    label = "Cs-CbCbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10145354830040004,
        B = -0.0489803384299793,
        E = 0.015639843192487044,
        L = 0.5133202912735024,
        A = -0.01888786766518403,
    ),
    )


entry(
    index = 426,
    label = "Cs-(Cds-Cds)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.017891182933054178,
        B = 0.028195363484491316,
        E = -0.01966023532540896,
        L = 0.18005525129745137,
        A = 0.0001812769654421241,
    ),
    )


entry(
    index = 425,
    label = "Cs-(Cds-Cd)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = None,
)


entry(
    index = 217,
    label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 0.11006731244302416,
        B = -0.008584284040182348,
        E = 0.16380981671032702,
        L = 0.6159961408411053,
        A = -0.011617545167361932,
    ),
    )


entry(
    index = 216,
    label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   C  u0 {2,D}
6   C  u0 {3,D}
""",
    solute = None,
)


entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 4,
    label = "Cbf-CbCbfCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
    solute = SoluteData(
        S = 0.07755125031675836,
        B = 0.01261140317366554,
        E = 0.2728204898724892,
        L = 0.5038778499122495,
        A = -0.006878670398700457,
    ),
    )


entry(
    index = 1817,
    label = "N3s-CbHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2350221984991501,
        B = 0.15184751994102857,
        E = 0.23102890749611962,
        L = 0.8830554068291961,
        A = 0.08622445639410055,
    ),
    )


entry(
    index = 1821,
    label = "Cb-N3s",
    group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18323587982605025,
        B = 0.10178849313059254,
        E = 0.16417214750515294,
        L = 0.778730110416433,
        A = 0.04225943319549152,
    ),
    )


entry(
    index = 5,
    label = "Cbf-CbfCbfCbf",
    group = 
"""
1  * Cbf u0 p0 c0 {2,B} {3,B} {6,B}
2    Cbf u0 p0 c0 {1,B} {4,B} {5,B}
3    Cbf u0 p0 c0 {1,B} {7,B} {11,B}
4    Cbf u0 p0 c0 {2,B} {8,B} {12,B}
5    Cbf u0 p0 c0 {2,B} {9,B} {13,B}
6    Cbf u0 p0 c0 {1,B} {10,B} {14,B}
7    C   u0 p0 c0 {3,B} {8,B}
8    C   u0 p0 c0 {4,B} {7,B}
9    C   u0 p0 c0 {5,B} {10,B}
10   C   u0 p0 c0 {6,B} {9,B}
11   C   u0 p0 c0 {3,B} {15,B}
12   C   u0 p0 c0 {4,B} {16,B}
13   C   u0 p0 c0 {5,B} {16,B}
14   C   u0 p0 c0 {6,B} {15,B}
15   C   u0 p0 c0 {11,B} {14,B}
16   C   u0 p0 c0 {12,B} {13,B}
""",
    solute = SoluteData(
        S = -0.025433799159650248,
        B = -0.031126347457771954,
        E = 0.09397061585666808,
        L = -0.09098076700386189,
        A = -0.005361402920687464,
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    solute = SoluteData(
        S = -0.019672652788129737,
        B = -0.007315980464491938,
        E = -0.019544258467003826,
        L = -0.017295256751593914,
        A = -0.01057063335431274,
    ),
    )


entry(
    index = 1131,
    label = "O2s-CbCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.018952978884026563,
        B = -0.049614959028072364,
        E = 0.06795736181562356,
        L = 0.11500728996216146,
        A = -0.08181084125614219,
    ),
    )


entry(
    index = 561,
    label = "Cs-CbCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03658858019972152,
        B = 0.048232583527564765,
        E = 0.08824101973047016,
        L = 0.2818063052784417,
        A = -0.0063637720559518805,
    ),
    )


entry(
    index = 1103,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2466497694102891,
        B = 0.21720410496620993,
        E = 0.1394496837648158,
        L = 0.7264509898797464,
        A = 0.15569817562235258,
    ),
    )


entry(
    index = 1862,
    label = "Cs-(CdN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.03796738649603144,
        B = 0.060187499101047474,
        E = -0.028326930494056164,
        L = 0.42460695012327565,
        A = -0.03103666019065207,
    ),
    )


entry(
    index = 238,
    label = "Cds-Cds(Cds-Cds)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.03325490091540492,
        B = 0.0217801255306473,
        E = -0.03049825098268345,
        L = 0.16467828390206657,
        A = -0.021034475048505023,
    ),
    )


entry(
    index = 237,
    label = "Cds-Cds(Cds-Cd)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 93,
    label = "Cds-O2d(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   Cd  u0 {2,D}
6   Cd  u0 {3,D}
""",
    solute = SoluteData(
        S = -0.030516632812311442,
        B = -0.026717661018716327,
        E = 0.09922126610003716,
        L = 0.3537173691867897,
        A = -0.015770239963616806,
    ),
    )


entry(
    index = 92,
    label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    solute = None,
)


entry(
    index = 85,
    label = "Cds-OdCdsCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1072,
    label = "Cs-CbCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.019681236435676184,
        B = 0.11706471897288274,
        E = 0.00588519669667045,
        L = 0.1720870644613815,
        A = 0.01992273534876497,
    ),
    )


entry(
    index = 850,
    label = "Cs-CbCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.017177285703109398,
        B = 0.038384413811114244,
        E = 0.037356380829700706,
        L = -0.0131671110930529,
        A = 0.006335853367232056,
    ),
    )


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    solute = SoluteData(
        S = 0.16769548493487382,
        B = -0.0007182781863627302,
        E = 0.11497686491951192,
        L = 0.6507855883871563,
        A = -0.001026474670093378,
    ),
    )


entry(
    index = 381,
    label = "Cs-(Cds-O2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.09428765366374235,
        B = 0.056614881139042665,
        E = -0.020546596778285083,
        L = 0.30284281137141983,
        A = 0.005237420710620457,
    ),
    )


entry(
    index = 76,
    label = "Cds-OdCbCb",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.07264219037931384,
        B = 0.005560727136030759,
        E = 0.10299200405508306,
        L = -0.00010178611899381947,
        A = -0.027912091188336725,
    ),
    )


entry(
    index = 1819,
    label = "N3s-CbCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.037519569304104064,
        B = -0.06583247119007674,
        E = 0.21159120698599448,
        L = 0.3342007022422182,
        A = -0.04073283485562148,
    ),
    )


entry(
    index = 85,
    label = "Cds-OdCdsCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.059871352173240695,
        B = 0.005001640698879304,
        E = 0.03402371890954585,
        L = -0.7877717735590415,
        A = -0.01658879579436389,
    ),
    )


entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.010838067665916537,
        B = 0.027322498010668973,
        E = 0.13482032800333776,
        L = 0.18653009032739432,
        A = 0.044570516565456714,
    ),
    )


entry(
    index = 1107,
    label = "O2s-CbH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10650630172596165,
        B = 0.08896765372231864,
        E = 0.15264439975658084,
        L = 0.6530652747554069,
        A = 0.3402326460823583,
    ),
    )


entry(
    index = 212,
    label = "Cds-Cds(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cd  u0 {3,D}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.04575184813072249,
        B = -0.007829197783635658,
        E = 0.10893615433836605,
        L = 0.4235865096683531,
        A = 0.000942497367883873,
    ),
    )


entry(
    index = 211,
    label = "Cds-Cds(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   C   u0 {3,D}
6   O2d u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1818,
    label = "N3s-CbCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0035631978695343956,
        B = 0.0024090045344076112,
        E = 0.20313625781408973,
        L = 0.5508154185568919,
        A = 0.007142800127602793,
    ),
    )


entry(
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.004528983168395375,
        B = -0.003677772872090449,
        E = -0.05627580351244058,
        L = 0.032281962141527905,
        A = -0.0683184830918916,
    ),
    )


entry(
    index = 178,
    label = "Cds-CdsCbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.000290938080784612,
        B = -0.02099995731094524,
        E = 0.11356608621490191,
        L = 0.11040163213304975,
        A = -0.0015157385119623453,
    ),
    )


entry(
    index = 1839,
    label = "Cb-(CtN3t)",
    group = 
"""
1   Ct  u0 {2,S} {3,T}
2 * Cb  u0 {1,S}
3   N3t u0 {1,T}
""",
    solute = SoluteData(
        S = 0.08229879305738319,
        B = 0.012674450521271613,
        E = 0.08011934976741517,
        L = 0.427169820540209,
        A = 0.013187821971573685,
    ),
    )


entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10089242960859669,
        B = 0.03574339399351117,
        E = 0.002936976276344556,
        L = 0.5521021259982722,
        A = 0.017871112971667436,
    ),
    )


entry(
    index = 387,
    label = "Cs-CbCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.036719673429192995,
        B = 0.006160278804679156,
        E = -0.0352801205981714,
        L = 0.044373342021194716,
        A = 0.0029148142491156287,
    ),
    )


entry(
    index = 1836,
    label = "Cds-CdsH(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.025820825996178763,
        B = 0.0058478236472315846,
        E = 0.13356056065016053,
        L = 0.4604291209160157,
        A = -0.0008807141376002509,
    ),
    )


entry(
    index = 1852,
    label = "Ct-N3tOs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.00889365568351978,
        B = 0.00706533676063866,
        E = 0.05151039239245936,
        L = 0.09279210450551743,
        A = -0.005806977277413354,
    ),
    )


entry(
    index = 1912,
    label = "N3d-CbR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cb  u0 {1,S}
3   R!H u0 {1,D}
""",
    solute = SoluteData(
        S = -0.03524412336192379,
        B = 0.08808508468283398,
        E = 0.13819960486879856,
        L = 0.39169399379984693,
        A = -0.05374652635572354,
    ),
    )


entry(
    index = 1924,
    label = "Cds-CCN",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   N  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0911554985474876,
        B = 0.049671961439127624,
        E = 0.10887622960487824,
        L = 0.43491725541412535,
        A = -0.012780739259666437,
    ),
    )


entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.014621355846234323,
        B = 0.03510944354262727,
        E = 0.045897859235294616,
        L = 0.4029468549897859,
        A = -0.03911496150089679,
    ),
    )


entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0091173413090973,
        B = 0.012560512460975507,
        E = 0.09170020563326338,
        L = 0.3253291980537414,
        A = 0.0010439743969913582,
    ),
    )


entry(
    index = 1859,
    label = "Cd-CdCsN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1405997530526527,
        B = 0.1249834796836434,
        E = 0.1376310776660782,
        L = 0.6284652974628967,
        A = 0.02287362890540481,
    ),
    )


entry(
    index = 1820,
    label = "N3s-CbCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.11444695970709769,
        B = -0.03823158079347691,
        E = 0.14146463256256725,
        L = 0.7785093790364094,
        A = 0.04954579679682774,
    ),
    )


entry(
    index = 1814,
    label = "N3s-N3sCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.009349261132939553,
        B = 0.05233310842382249,
        E = 0.18945311595786393,
        L = 0.5328735279796373,
        A = 0.032441212340956815,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0981651803010435,
        B = -0.024983130231607312,
        E = 0.058382916967171065,
        L = 0.3913974007705658,
        A = 0.008273693863824936,
    ),
    )


entry(
    index = 1146,
    label = "S2s-CbCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.01331280593470535,
        B = 0.007129924863174224,
        E = -0.03401789212971357,
        L = -0.25463510682171936,
        A = 0.023996556407119285,
    ),
    )


entry(
    index = 1197,
    label = "Cb-S2s",
    group = 
"""
1 * Cb  u0 {2,S}
2   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10551559193986314,
        B = 0.038586652783128915,
        E = 0.3178582715504392,
        L = 1.1703740679736583,
        A = -0.003929574242093504,
    ),
    )


entry(
    index = 1923,
    label = "Cds-CNH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13403834657342656,
        B = 0.13726409893074762,
        E = 0.019356408336322517,
        L = 0.51510342134663,
        A = 0.008674103770125612,
    ),
    )


entry(
    index = 1828,
    label = "N3s-(CO)CbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.04096721872255178,
        B = 0.046490186543880596,
        E = 0.06135755971485019,
        L = 0.5253120750309525,
        A = 0.21597514517634472,
    ),
    )


entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02523040177411776,
        B = 0.07194912452874343,
        E = 0.08891829663522642,
        L = 0.48433683122314475,
        A = -0.0074984244111798385,
    ),
    )


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0270896083816773,
        B = 0.16456538881587648,
        E = 0.13394066441421168,
        L = 0.6493475203414993,
        A = 0.10768049043690747,
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    solute = SoluteData(
        S = -0.12456884350281124,
        B = 0.08128759552018144,
        E = 0.11845690532836607,
        L = 0.16370439638922815,
        A = 0.08048446834570429,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10108406219773142,
        B = 0.03787309303263909,
        E = 0.08209827727483628,
        L = 0.6295958505575666,
        A = 0.2073908999657379,
    ),
    )


entry(
    index = 1855,
    label = "Cd-N3dCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04787866361226671,
        B = 0.08260658537055043,
        E = 0.07646440362139559,
        L = 0.41842407040108154,
        A = 0.04184449247805312,
    ),
    )


entry(
    index = 1812,
    label = "N3s-N3sCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04750593156429622,
        B = 0.044419877771728546,
        E = 0.0737233070645776,
        L = 0.5867177578285245,
        A = 0.013595790342596191,
    ),
    )


entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0013582314046520184,
        B = 0.05821116212265593,
        E = -0.12137905179934447,
        L = 0.24404453461699163,
        A = 0.022140907420075146,
    ),
    )


entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.12790781753237995,
        B = -0.0399421999133451,
        E = 0.11169323496253294,
        L = 0.2132245508277543,
        A = -0.05487633732817889,
    ),
    )


entry(
    index = 1898,
    label = "N3s-(CdCd)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.017219920897868272,
        B = -0.04294416836039491,
        E = 0.1938450004828945,
        L = 0.42308593846483894,
        A = 0.038183475096024946,
    ),
    )


entry(
    index = 1136,
    label = "S2s-CbH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.07490689841407816,
        B = -0.011110315213817924,
        E = 0.1348627220006173,
        L = 0.5779102660243717,
        A = -0.00318239826904365,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    solute = SoluteData(
        S = 0.100059394317912,
        B = 0.11211495755909065,
        E = 0.21984536560299767,
        L = 0.8155436078658403,
        A = 0.0004978560406408388,
    ),
    )


entry(
    index = 1197,
    label = "Cb-S",
    group = 
"""
1 * Cb u0 {2,S}
2   S  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.07760683127935733,
        B = 0.09282072569529397,
        E = 0.09705551382224872,
        L = 0.4465625780508779,
        A = -0.011821571629838533,
    ),
    )


entry(
    index = 2013,
    label = "S6dd-OdOdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    solute = SoluteData(
        S = -0.025837327781767935,
        B = 0.0204376091394172,
        E = -0.07727813074122696,
        L = -0.16288838248251392,
        A = -0.015618103243795941,
    ),
    )


entry(
    index = 2020,
    label = "S6dd-OdOdN3sC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   N3s  ux {1,S}
5   C    ux {1,S}
""",
    solute = SoluteData(
        S = 0.050723050930672406,
        B = -0.019497236933070487,
        E = 0.08016418760278117,
        L = 0.41380798883222186,
        A = 0.0698222477250217,
    ),
    )


entry(
    index = 1864,
    label = "Cs-(CdN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = -0.018866903234047452,
        B = 0.11993666598890217,
        E = -0.023562255241942495,
        L = 0.3847428272033014,
        A = 0.03424568407082628,
    ),
    )


entry(
    index = 1860,
    label = "Cd-CdHN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10248846543401673,
        B = 0.09313760309032412,
        E = 0.06622926005311779,
        L = 0.5214969826791073,
        A = 0.008517208134918623,
    ),
    )


entry(
    index = 1098,
    label = "O2s-HH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03984664308000864,
        B = 0.028797843279354883,
        E = -0.044407128621314865,
        L = -0.04826236712520768,
        A = -0.04241780531583567,
    ),
    )


entry(
    index = 1126,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.015401879600061676,
        B = -0.04459420860554332,
        E = 0.04634410214798493,
        L = 0.313897927395998,
        A = -0.049176214517854575,
    ),
    )


entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = SoluteData(
        S = 0.008594037074884488,
        B = 0.0024289923501405165,
        E = 0.12921331634882718,
        L = 0.5513528257789645,
        A = -0.030813289099288665,
    ),
    )


entry(
    index = 1166,
    label = "Cs-CbSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02543392738271217,
        B = 0.014292537589421393,
        E = 0.11561852168627114,
        L = 0.7417184691816483,
        A = -0.01145427761100644,
    ),
    )


entry(
    index = 1140,
    label = "S2s-CsCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.013346312736023616,
        B = 0.027793672739407187,
        E = 0.15826155924435276,
        L = 0.3978207471606258,
        A = -0.001152593073325278,
    ),
    )


entry(
    index = 1176,
    label = "Cs-C=SHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.01208256416334446,
        B = 0.014942096128197482,
        E = 0.055207650557273016,
        L = 0.25767477041803866,
        A = -0.020783520548732615,
    ),
    )


entry(
    index = 2044,
    label = "S6dd-OdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    solute = SoluteData(
        S = -0.013367290630636021,
        B = -0.002998956588486079,
        E = 0.0954545161763444,
        L = 0.28720788620503457,
        A = 0.02303633449252286,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NrCrC",
    group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.048371509961567964,
        B = 0.09784054694450477,
        E = 0.20471522223100225,
        L = 0.40073676394369523,
        A = -0.032142127979828045,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1824,
    label = "Cds-OdN3sN",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.003693242750220046,
        B = 0.0071245399717639315,
        E = 0.2731844339863134,
        L = 0.22881514288895421,
        A = 0.015551143198029712,
    ),
    )


entry(
    index = 1138,
    label = "S2s-CsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0940034943478049,
        B = -0.031489536658843104,
        E = 0.15419033524495027,
        L = 0.8198764742694953,
        A = -0.05090559042523884,
    ),
    )


entry(
    index = 1941,
    label = "N3s-NCdCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08126482275357244,
        B = 0.11893311241966191,
        E = 0.16173633960782613,
        L = 0.456170640527648,
        A = -0.0600342864309706,
    ),
    )


entry(
    index = 1822,
    label = "N3d-N3dN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0845005787416505,
        B = 0.038533992407837385,
        E = 0.181953302300014,
        L = 0.6854933390877003,
        A = 0.04405090866945204,
    ),
    )


entry(
    index = 1165,
    label = "Cs-CtSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.002771234198981536,
        B = -0.0054406366222915946,
        E = 0.008951724361171656,
        L = -0.1630825008572585,
        A = -0.0017349641946321282,
    ),
    )


entry(
    index = 1823,
    label = "Crs-OrsOrsCC",
    group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.044133282027163025,
        B = 0.0029121136763810207,
        E = -0.015153629802357346,
        L = 0.10785897395581859,
        A = 0.017232322197547917,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.008501818038624856,
        B = 0.04311554889317187,
        E = 0.13038404971463038,
        L = 0.3383027046883771,
        A = -0.009521283232368087,
    ),
    )


entry(
    index = 1896,
    label = "N3s-CsCs(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.17183930751634163,
        B = 0.052937249571405554,
        E = -0.02380706592542234,
        L = 0.33879486308506845,
        A = 0.01491678999803047,
    ),
    )


entry(
    index = 1893,
    label = "N3s-NCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1910,
    label = "N3d-OdN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.23844343667115467,
        B = 0.005118693275620352,
        E = 0.3180023852773945,
        L = 1.0288311306207978,
        A = -0.0007350825799285601,
    ),
    )


entry(
    index = 1899,
    label = "N3s-(CdCd)CsH",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.133183361045915,
        B = 0.042615378842031856,
        E = 0.059650695707809724,
        L = 0.7773330649174944,
        A = 0.08149823478055752,
    ),
    )


entry(
    index = 1932,
    label = "Cds-(Cds-Os)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    solute = SoluteData(
        S = -0.007677772197843762,
        B = -0.0310801960256749,
        E = 0.03386087790352901,
        L = 0.1217540319276076,
        A = -0.0560128457477335,
    ),
    )


entry(
    index = 243,
    label = "Cds-CdsCbCb",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = -0.00019316788308978275,
        B = 0.014175024324692384,
        E = 0.06612155013504595,
        L = 0.013951055437145575,
        A = 0.02380250551979378,
    ),
    )


entry(
    index = 173,
    label = "Cds-Cds(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.07290937024963932,
        B = 0.04421168156373076,
        E = 0.25256986548187527,
        L = 0.9548437996707678,
        A = 0.06522267361862978,
    ),
    )


entry(
    index = 172,
    label = "Cds-Cds(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.011741331491292853,
        B = 0.007242914990868393,
        E = 0.06227619941486267,
        L = 0.212790175435891,
        A = -0.03186249849665013,
    ),
    )


entry(
    index = 229,
    label = "Cds-Cds(Cds-Cds)Ct",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.02778259212928794,
        B = 6.581121112172661e-05,
        E = 0.052149548848914325,
        L = 0.31933588300893695,
        A = 0.0025953002854094383,
    ),
    )


entry(
    index = 228,
    label = "Cds-CdsCt(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   C  u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1135,
    label = "S2s-CtH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.041581002804568105,
        B = 0.0164820789384381,
        E = 0.22008188804091844,
        L = 0.9001095549713981,
        A = 0.05332028935668461,
    ),
    )


entry(
    index = 1874,
    label = "O2s-CsN3s",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.00629369255479236,
        B = 0.026131239139406588,
        E = 0.1908870632060619,
        L = 0.4790380395556685,
        A = -0.013689955559158962,
    ),
    )


entry(
    index = 1175,
    label = "Cs-CsCsCsS2",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.14312461652616043,
        B = 0.11907629777896263,
        E = 0.21727528524499795,
        L = 0.6413990361917125,
        A = 0.010676722452745252,
    ),
    )


entry(
    index = 1175,
    label = "Cs-CsCsCsS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Cs-CCCS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1181,
    label = "Cds-CdsCsS2",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02107688488411232,
        B = 0.017868992118415875,
        E = 0.12003318318403733,
        L = 0.36193852742173266,
        A = -0.023345518640511213,
    ),
    )


entry(
    index = 1181,
    label = "Cds-CdsCsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Cds-CdCS",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.013483300656662067,
        B = 0.01363268819428633,
        E = 0.05019080223730575,
        L = 0.4646383423897871,
        A = 0.023217474166327915,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.01967074944656005,
        B = 0.010950189186618477,
        E = 0.2469639776294025,
        L = 0.7638268598483573,
        A = -0.002866699883542118,
    ),
    )


entry(
    index = 1865,
    label = "Cs-(CdN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.022864058601181524,
        B = 0.03469119481714954,
        E = 0.14268636646254582,
        L = 0.40438824102433074,
        A = 0.02378338707228911,
    ),
    )


entry(
    index = 1169,
    label = "Cs-CsCsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10150861465190637,
        B = 0.06945252144868698,
        E = 0.15175429244775626,
        L = 0.6734015242121983,
        A = -0.0006932271059701869,
    ),
    )


entry(
    index = 1169,
    label = "Cs-CsCsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1824,
    label = "Crds-OdN3rsN3rs",
    group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   N3s u0 r1 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.054864923436484844,
        B = -0.031003188896859702,
        E = 0.09840255258435017,
        L = 0.12127668263915051,
        A = 0.065822338420049,
    ),
    )


entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = SoluteData(
        S = 0.011978235742647558,
        B = 0.02820173525193563,
        E = -0.05442728689121103,
        L = 0.13788959555348837,
        A = 0.0024995643698690006,
    ),
    )


entry(
    index = 1134,
    label = "S2s-CdH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02359220765863853,
        B = 0.03188705757223141,
        E = 0.1943813463877902,
        L = 0.8298050227264194,
        A = 0.014459449709523956,
    ),
    )


entry(
    index = 1143,
    label = "S2s-CdCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0005420920876900635,
        B = -0.008340317020162706,
        E = -0.006730788663980297,
        L = 0.269820293983292,
        A = -0.046516259761622165,
    ),
    )


entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = -0.003196921969338703,
        B = -0.006149455602708236,
        E = 0.04622616948633017,
        L = 0.04371811670494071,
        A = -0.00956346483342884,
    ),
    )


entry(
    index = 845,
    label = "Cs-(Cds-Cds)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.14817306796033866,
        B = 0.04903057453446034,
        E = -0.019602321794030663,
        L = 0.20430209087280643,
        A = 0.0211834405904248,
    ),
    )


entry(
    index = 844,
    label = "Cs-(Cds-Cd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1866,
    label = "Cs-(CdN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.02556665403547449,
        B = 0.006727036352096275,
        E = 0.0118722463652812,
        L = 0.2823507827167008,
        A = 0.0003680659889412255,
    ),
    )


entry(
    index = 1856,
    label = "Cd-N3dCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0566715697022523,
        B = 0.05664637491249194,
        E = 0.06660142546523833,
        L = 0.5867818390865267,
        A = 0.056636303454378596,
    ),
    )


entry(
    index = 1148,
    label = "S2s-S2sCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13474005760912713,
        B = 0.04470645026895408,
        E = 0.21685493958818183,
        L = 0.9368931571018478,
        A = 0.008633562285459176,
    ),
    )


entry(
    index = -1,
    label = "S2s-S2sC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1151,
    label = "S2s-S2sCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.04443008474685384,
        B = 0.015983762551356494,
        E = 0.0995005632290296,
        L = 0.4340929744489299,
        A = -0.0010714359523412843,
    ),
    )


entry(
    index = 1149,
    label = "S2s-S2sCd",
    group = 
"""
1 * S2s        u0 {2,S} {3,S}
2   S2s        u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09125356296065043,
        B = 0.004232939599018403,
        E = 0.2814507132910011,
        L = 1.0086116486969137,
        A = 0.00747105068494808,
    ),
    )


entry(
    index = 1167,
    label = "Cs-SsSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.01924570051989579,
        B = 0.00941911017836322,
        E = 0.10030767531103277,
        L = 0.43163695795890705,
        A = -0.000941710514894095,
    ),
    )


tree(
"""
L1: R
	L2: S
		L3: S6dd
			L4: S6dd-OdOd
			L4: S6dd-OdOd
				L5: S6dd-OdOdN3sC
				L5: S6dd-OdOdCC
				L5: S6dd-OdOdCO
				L5: S6dd-OdOdCO
					L6: S6dd-OdOdCsOs
				L5: S6dd-OdOdOO
				L5: S6dd-OdOdCC
					L6: S6dd-OdOdCsCs
					L6: S6rdd-CCOdOd
		L3: S4d
			L4: S4d-Od
				L5: S4d-OdCC
				L5: S4d-OdCS
				L5: S4d-OdCC
					L6: S4d-OdCsCs
	L2: S
		L3: S2d
			L4: S2d-C
		L3: S4dd
		L3: S2s
			L4: S2s-SC
				L5: S2s-S2sC
					L6: S2s-S2sCd
					L6: S2s-S2sCb
					L6: S2s-S2sCs
				L5: S2s-S46C
			L4: S2s-CH
				L5: S2s-CdH
				L5: S2s-CtH
				L5: S2s-CbH
				L5: S2s-CsH
			L4: S2s-CC
				L5: S2s-CdCb
				L5: S2s-CsCd
				L5: S2s-CsCb
				L5: S2s-CbCb
				L5: S2s-CsCs
				L5: S2s-CsCt
				L5: S2s-(C=S2d)Cs
				L5: S2s-Cs(C=O)
				L5: S2s-CdCd
			L4: S2s-SS
				L5: S2s-SsSs
	L2: C
		L3: Cb
			L4: Cb-S
		L3: Cbf
		L3: Cbf
			L4: Cbf-CbfCbfCbf
			L4: Cbf-CbCbfCbf
			L4: Cbf-CbCbCbf
		L3: CJ2_singlet
		L3: Cds
			L4: Cd-N3dCsH
			L4: Cds-CdCS
				L5: Cds-CdsCsSs
					L6: Cds-CdsCsS2
			L4: Cds-OdN3sN
			L4: Cd-N3dCsCs
			L4: Cds-CNH
				L5: Cd-CdHN3s
			L4: Cds-CCN
				L5: Cd-CdCsN3s
			L4: CO-CsSs
			L4: Cds-OdN3sN
				L5: Cds-OdN3sN3s
					L6: Crds-OdN3rsN3rs
			L4: Cds-OdN3sC
				L5: Crds-OdN3rsCr
			L4: Cds-OdN3sC
				L5: Cds-OdN3sCs
			L4: Cds-OdN3sH
			L4: Cds-Od(OsH)
			L4: Cds-OdCOs
				L5: Cds-OdCdsOs
				L5: Cds-OdCbOs
			L4: Cds-OdOsH
			L4: Cds-CdCO
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-Cd)O2s
						L7: Cds-Cds(Cds-Cds)O2s
				L5: Cds-CdsCbOs
				L5: Cd-CdCsOs
					L6: Cds-CdsCsOs
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-O2d)O2s
			L4: Cds-OdOsOs
			L4: Cds-CdSH
				L5: Cds-CdsSH
					L6: Cds-CdsS2H
			L4: Cds-OdCC
				L5: Cds-OdCdsCs
				L5: Cds-OdCdsCds
				L5: Cds-OdCbCb
				L5: Cds-OdCdsCds
					L6: Cds-O2d(Cds-Cd)(Cds-Cd)
						L7: Cds-O2d(Cds-Cds)(Cds-Cds)
			L4: Cds-OdCH
			L4: Cds-OdCC
				L5: Cds-OdCsCs
				L5: Cds-OdCdsCs
					L6: Cds-O2d(Cds-Cd)Cs
						L7: Cds-O2d(Cds-Cds)Cs
					L6: Cds-O2d(Cds-O2d)Cs
			L4: Cds-OdCH
				L5: Cds-OdCdsH
					L6: Cds-O2d(Cds-Cd)H
						L7: Cds-O2d(Cds-Cds)H
					L6: Cds-O2d(Cds-O2d)H
				L5: Cds-OdCsH
		L3: Cb
			L4: Cb-N3s
			L4: Cb-S
				L5: Cb-S2s
				L5: Cb-S6dd
			L4: Cb-O2s
			L4: Cb-H
			L4: Cb-C
				L5: Cb-Cds
				L5: Cb-Cb
				L5: Cb-Ct
					L6: Cb-(CtN3t)
				L5: Cb-Cds
					L6: Cb-(Cds-Cd)
						L7: Cb-(Cds-Cds)
					L6: Cb-(Cds-O2d)
						L7: Cb-(Cds-O2dOs)
				L5: Cb-Cs
		L3: Cds
			L4: Cds-CdOsH
				L5: Cds-CdsOsH
			L4: Cds-CdCC
				L5: Cds-CdsCtCds
					L6: Cds-CdsCt(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)Ct
				L5: Cds-CdsCbCb
				L5: Cds-CdsCdsCds
				L5: Cds-CdsCdsCs
				L5: Cds-CdsCbCds
				L5: Cds-CdsCbCds
					L6: Cds-Cds(Cds-Cd)Cb
						L7: Cds-Cds(Cds-Cds)Cb
				L5: Cds-CdsCdsCds
					L6: Cds-Cds(Cds-O2d)(Cds-Cd)
						L7: Cds-Cds(Cds-O2d)(Cds-Cds)
					L6: Cds-Cds(Cds-Cd)(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)(Cds-Cds)
				L5: Cds-CdsCbCs
				L5: Cds-CdsCtCt
					L6: Cds-Cd(CtN3t)(CtN3t)
				L5: Cds-CdsCtCs
					L6: Cd-CdCs(CtN3t)
				L5: Cds-CdsCdsCs
					L6: Cds-Cds(Cds-Cd)Cs
						L7: Cds-Cds(Cds-Cds)Cs
					L6: Cd-CdCs(CO)
			L4: Cds-CdCH
				L5: Cds-CdsCdsH
				L5: Cds-CdsCbH
					L6: Cds-(Cds-Os)CbH
				L5: Cds-CdsCtH
					L6: Cds-CdsH(CtN3t)
				L5: Cds-CdsCdsH
					L6: Cd-Cd(CO)H
					L6: Cds-Cds(Cds-Cd)H
						L7: Cds-Cds(Cds-Cds)H
			L4: Cds-CdCH
				L5: Cds-CdsCsH
			L4: Cds-CdHH
				L5: Cds-CddHH
					L6: Cds-(Cdd-O2d)HH
				L5: Cds-CdsHH
			L4: Cds-OdCOs
				L5: Cds-OdCdsOs
					L6: Cds-O2d(Cds-O2d)O2s
					L6: Cds-O2d(Cds-Cd)O2s
						L7: Cds-O2d(Cds-Cds)O2s
				L5: Cds-OdCsOs
			L4: Cds-CdCC
				L5: Cds-CdsCsCs
		L3: Cs
			L4: Cs-SsSsHH
			L4: Cs-CCSH
				L5: Cs-CsCsSH
					L6: Cs-CsCsS2H
			L4: Cs-CCCS
				L5: Cs-CsCsCsS
					L6: Cs-CsCsCsS2
			L4: Cs-CCCC
				L5: Cs-CtCsCsCs
				L5: Cs-CbCtCsCs
			L4: Cs-CCSS
				L5: Cs-CsCsSS
			L4: Crs-CSHH
				L5: Crs-CrSrHH
			L4: Cs-SsHHH
				L5: Cs-S6HHH
				L5: Cs-S2sHHH
				L5: Cs-S4HHH
			L4: Cs-COsHH
				L5: Cs-CdsOsHH
			L4: Cs-CCCOs
				L5: Cs-CbCsCsOs
			L4: Cs-CCCH
				L5: Cs-CbCdsCsH
				L5: Cs-CbCdsCsH
					L6: Cs-(Cds-Cd)CbCsH
						L7: Cs-(Cds-Cds)CbCsH
				L5: Cs-CbCbCsH
				L5: Cs-CbCbCbH
			L4: Cs-CSHH
				L5: Cs-CtSsHH
				L5: Cs-CbSsHH
				L5: Cs-CdsSsHH
				L5: Cs-CsSHH
					L6: Cs-CsS2HH
					L6: Cs-CsS6HH
					L6: Cs-CsS4HH
			L4: Crs-NCCH
				L5: Crs-CrN3rsCH
				L5: Crs-CrCrN3sH
			L4: Cs-NCsCsH
				L5: Cs-N5dcCsCsH
				L5: Cs-N3sCsCsH
			L4: Cs-NHHH
				L5: Cs-N3dHHH
					L6: Cs-(N3dCd)HHH
			L4: Cs-NHHH
				L5: Cs-N3sHHH
			L4: Cs-NCsHH
				L5: Cs-N3dCHH
				L5: Cs-N5dcCsHH
				L5: Cs-N3dCHH
					L6: Cs-(N3dN3d)CsHH
					L6: Cs-(N3dCd)CsHH
			L4: Crs-CCOsOs
				L5: Crs-OrsOrsCC
				L5: Crs-CrOrsOsC
			L4: Crs-COsOsH
				L5: Crs-OrsOrsCH
				L5: Crs-CrOrsOsH
			L4: Cs-CCOsH
				L5: Cs-CbCsOsH
			L4: Cs-CCOsOs
				L5: Cs-CsCsOsOs
			L4: Cs-COsOsH
				L5: Cs-CsOsOsH
			L4: Crs-OsOsHH
				L5: Crs-OrsOrsHH
			L4: Cs-CCCOs
				L5: Cs-CdsCsCsOs
					L6: Cs-(Cds-Cd)CsCsOs
						L7: Cs-(Cds-Cds)CsCsOs
					L6: Cs-(Cds-O2d)CsCsOs
				L5: Cs-CsCsCsOs
			L4: Cs-COsHH
				L5: Cs-CtOsHH
				L5: Cs-CdsOsHH
					L6: Cs-(Cds-O2d)OsHH
					L6: Cs-(Cds-Cd)OsHH
						L7: Cs-(Cds-Cds)OsHH
				L5: Cs-CsOsHH
			L4: Cs-OsHHH
			L4: Cs-CCOsH
				L5: Cs-CdsCsOsH
					L6: Cs-(Cds-O2d)CsOsH
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
				L5: Cs-CsCsOsH
		L3: Cs
			L4: Cs-NCsHH
				L5: Cs-N3sCsHH
			L4: Cs-NCsCsCs
				L5: Cs-N3sCsCsCs
				L5: Cs-N5dcCsCsCs
			L4: Crs-CCHH
				L5: Crs-CrCrHH
			L4: Cs-CCCC
				L5: Cs-CbCsCsCs
				L5: Cs-CdsCdsCsCs
					L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
				L5: Cs-CtCsCsCs
					L6: Cs-(CtN3t)CsCsCs
				L5: Cs-CdsCsCsCs
					L6: Cs-(CdN3d)CsCsCs
					L6: Cs-(Cds-O2d)CsCsCs
					L6: Cs-(Cds-Cd)CsCsCs
						L7: Cs-(Cds-Cds)CsCsCs
				L5: Cs-CsCsCsCs
			L4: Cs-CCCH
				L5: Cs-CbCsCsH
				L5: Cs-CtCsCsH
					L6: Cs-(CtN3t)CsCsH
				L5: Cs-CdsCdsCsH
				L5: Cs-CdsCdsCsH
					L6: Cs-(Cds-Cd)(Cds-Cd)CsH
						L7: Cs-(Cds-Cds)(Cds-Cds)CsH
				L5: Cs-CdsCsCsH
					L6: Cs-(CdN3d)CsCsH
					L6: Cs-(Cds-O2d)CsCsH
					L6: Cs-(Cds-Cd)CsCsH
						L7: Cs-(Cds-Cds)CsCsH
				L5: Cs-CsCsCsH
			L4: Cs-CCHH
				L5: Cs-CbCdsHH
				L5: Cs-CbCtHH
				L5: Cs-CbCbHH
				L5: Cs-CbCdsHH
					L6: Cs-(Cds-O2d)CbHH
					L6: Cs-(Cds-Cd)CbHH
						L7: Cs-(Cds-Cds)CbHH
				L5: Cs-CtCtHH
				L5: Cs-CtCdsHH
					L6: Cs-(Cds-Cd)CtHH
						L7: Cs-(Cds-Cds)CtHH
					L6: Cs-(Cds-O2d)CtHH
				L5: Cs-CbCsHH
				L5: Cs-CtCsHH
					L6: Cs-(CtN3t)CsHH
				L5: Cs-CdsCdsHH
					L6: Cs-(Cds-O2d)(Cds-O2d)HH
					L6: Cs-(Cds-O2d)(Cds-Cd)HH
						L7: Cs-(Cds-O2d)(Cds-Cds)HH
					L6: Cs-(Cds-Cd)(Cds-Cd)HH
						L7: Cs-(Cds-Cds)(Cds-Cds)HH
				L5: Cs-CdsCsHH
					L6: Cs-(CdN3d)CsHH
					L6: Cs-(Cds-O2d)CsHH
					L6: Cs-(Cds-Cd)CsHH
					L6: Cs-(Cds-Cd)CsHH
						L7: Cs-(Cds-Cds)CsHH
				L5: Cs-CsCsHH
			L4: Cs-CHHH
				L5: Cs-C=SHHH
				L5: Cs-CbHHH
				L5: Cs-CtHHH
				L5: Cs-CdsHHH
					L6: Cs-(CdN3d)HHH
					L6: Cs-(Cds-Cd)HHH
					L6: Cs-(Cds-Cd)HHH
						L7: Cs-(Cds-Cds)HHH
					L6: Cs-(Cds-O2d)HHH
				L5: Cs-CsHHH
		L3: Ct
			L4: Ct-N3tOs
			L4: Ct-N3tN3s
			L4: Ct-N3tC
			L4: Ct-N3tC
				L5: Ct-N3tCd
				L5: Ct-N3tCs
			L4: Ct-CtC
				L5: Ct-CtCb
				L5: Ct-CtCds
				L5: Ct-CtCt
				L5: Ct-CtCds
					L6: Ct-Ct(Cds-Cd)
						L7: Ct-Ct(Cds-Cds)
				L5: Ct-CtCs
			L4: Ct-CtH
		L3: Cdd
			L4: Cdd-CdOd
				L5: Cdd-CdsOd
			L4: Cdd-CdCd
				L5: Cdd-CdsCds
	L2: N
		L3: N3s
			L4: N3s-NCC
				L5: N3s-NCsCs
					L6: N3s-CsCs(N3dOd)
			L4: N3s-NCC
				L5: N3s-NCdCs
				L5: N3s-NrCrC
			L4: N3s-NCH
				L5: N3s-N3sCsH
		L3: N5dc
		L3: N3d
			L4: N3d-OdN3s
			L4: N3d-N3dN3s
			L4: N3d-CbR
			L4: N3d-OdOs
			L4: N3d-CsR
				L5: N3d-N3dCs
			L4: N3d-CdH
		L3: N5dc
			L4: N5dc-OdOsC
		L3: N3t
		L3: N3s
			L4: N3s-NCH
				L5: N3s-N3sCbH
			L4: N3s-CCC
				L5: N3s-(CdCd)CsCs
				L5: N3s-CbCsCs
			L4: N3s-CCH
				L5: N3s-(CdCd)CsH
				L5: N3s-(CO)CbH
				L5: N3s-CbCbH
				L5: N3s-CbCsH
				L5: N3s-(CO)(CO)H
			L4: N3s-CHH
				L5: N3s-CbHH
				L5: N3s-(CO)HH
				L5: N3s-CdHH
			L4: N3s-CCH
				L5: N3s-(CO)CsH
				L5: N3s-CsCsH
			L4: N3s-CHH
				L5: N3s-CsHH
			L4: N3s-CCC
				L5: N3s-(CO)CsCs
				L5: N3s-CsCsCs
				L5: N3rs-CCC
					L6: N3rs-CrCrC
					L6: N3rs-CrCrC
						L7: N3rs-CrCrCr
			L4: N3s-N3sHH
		L3: N1dc
	L2: O
		L3: O2s
			L4: O2s-HH
			L4: O2s-N
			L4: O2s-CC
				L5: O2s-CdsCs
			L4: O2s-SH
				L5: O2s-S_DeH
			L4: O2s-CS
				L5: O2s-CS6
			L4: O2s-OsC
				L5: O2s-OsCs
				L5: O2s-OsCds
					L6: O2s-O2s(Cds-O2d)
			L4: O2s-N
				L5: O2s-CN
					L6: O2s-CsN3s
				L5: O2s-CN
					L6: O2s-CsN3d
						L7: O2s-Cs(N3dOd)
			L4: O2s-CH
				L5: O2s-CbH
				L5: O2s-CdsH
				L5: O2s-CdsH
					L6: O2s-(Cds-O2d)H
					L6: O2s-(Cds-Cd)H
				L5: O2s-CsH
			L4: O2s-CC
				L5: O2s-CbCb
				L5: O2s-CsCb
				L5: O2s-CdsCds
					L6: O2s-(Cds-O2d)(Cds-O2d)
					L6: O2s-(Cds-O2d)(Cds-Cd)
					L6: O2s-(Cds-Cd)(Cds-Cd)
				L5: O2s-CsCs
				L5: O2s-CdsCs
					L6: O2s-Cs(Cds-Cd)
					L6: O2s-Cs(Cds-O2d)
			L4: O2s-OsH
		L3: O2d
			L4: O2d-N3d
			L4: O2d-Cd
			L4: O2d-N5dc
			L4: O2d-Sd
		L3: Oc
			L4: Oc-N5dc
""",
)