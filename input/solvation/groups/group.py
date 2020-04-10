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
        S = -0.025956162881778447,
        B = -0.008596952362180861,
        E = -0.00947188264314363,
        L = -0.1176005138770031,
        A = -0.0037271012397306937,
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
        S = -0.0004012369492458691,
        B = 0.024227109680470513,
        E = -0.023048097123002816,
        L = 0.0779769449902769,
        A = 0.04467305616708157,
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
        S = 0.067820259406802,
        B = 0.025529563112120807,
        E = -0.055744283050034975,
        L = 0.389506371644948,
        A = -0.009215194935829474,
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
        S = 0.1345266890813227,
        B = 0.03235373141943144,
        E = 0.09918651516303485,
        L = 0.6601632871907406,
        A = -0.03487216049183343,
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
        S = -0.12520001241910994,
        B = 0.0008533152082624748,
        E = 0.026109787409853973,
        L = -0.32640463330925856,
        A = 0.006969348498110623,
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
        S = -0.001298942773847638,
        B = -0.027123884457023587,
        E = 0.06070195893698237,
        L = 0.0417010523473993,
        A = -0.034550459510326495,
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
        S = 0.10601053948235757,
        B = 0.060822452873745506,
        E = 0.15189303842119464,
        L = 0.7132515842388399,
        A = 0.14260838012081167,
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
        S = 0.055652051433887406,
        B = -0.002363952274463657,
        E = 0.23057187804413268,
        L = 0.8968064010978979,
        A = -0.008606518778762222,
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
        S = 0.0433453262970215,
        B = -0.04153121085841277,
        E = 0.20620079499358132,
        L = 0.41670490325509857,
        A = 0.014900717925848158,
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
        S = 0.42203114614044535,
        B = 0.24195564164526678,
        E = 0.1086893073938842,
        L = 1.060729971691564,
        A = 0.05937986222611755,
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
        S = 0.27351455914461836,
        B = 0.0681914383744925,
        E = 0.36724315536611823,
        L = 1.5630728165717664,
        A = 0.011012769546031486,
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
        S = 0.22077449132773624,
        B = 0.12155880068224544,
        E = 0.21704782754829394,
        L = 0.9790510172964997,
        A = 0.07323748185810885,
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
        S = 0.0004913242062169707,
        B = 0.03022235728715573,
        E = 0.21623358187470149,
        L = 0.7073615708401083,
        A = -0.009171175206552865,
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
        S = 0.4027599457499263,
        B = 0.1465580304903095,
        E = 0.1272612524389427,
        L = 1.2295105800698594,
        A = 0.027852506001749065,
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
        S = 0.02270711618362876,
        B = 0.031795280057388645,
        E = 0.05515916473257289,
        L = 0.2506193016722922,
        A = 0.04492024526659532,
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
        S = -0.08880389894926427,
        B = 0.012918751918334881,
        E = -0.06210164043137782,
        L = 0.3871741940898732,
        A = -0.03131548574598888,
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
        S = -0.003803805540738954,
        B = 0.00010169864834370231,
        E = -0.0017871856882037264,
        L = 0.5006926869906904,
        A = -0.0005902027089875203,
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
        S = 0.0917845888470962,
        B = 0.002937936483460743,
        E = 0.06603612973360512,
        L = 0.5244993989851621,
        A = 0.00041862894532378316,
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
        S = 0.08892379437625678,
        B = 0.020284657665395486,
        E = 0.10529585970344255,
        L = 0.5057873174457599,
        A = 0.10349325329445866,
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
        S = 0.010713742016326272,
        B = 0.012633003599969253,
        E = 0.026179871904476175,
        L = 0.5169765542470399,
        A = -0.008925534330225492,
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
        S = 0.12402570337854373,
        B = 0.3006717886697003,
        E = 0.1242766748029123,
        L = 0.7221829915472383,
        A = 0.1018503939306512,
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
        S = 0.21245614252468703,
        B = 0.14907646670208397,
        E = 0.1431146563935322,
        L = 0.7134342605349843,
        A = 0.04909423840990805,
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
    index = 1823,
    label = "Oc-N5dc",
    group = 
"""
1 * O0sc u0 c-1 {2,S}
2   N5dc u0 c+1 {1,S}
""",
    solute = SoluteData(
        S = 0.2533573022378585,
        B = 0.12441289787035507,
        E = 0.1166032131113445,
        L = 0.79662242999134,
        A = 0.09218517182400673,
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
        S = 0.0356214955807911,
        B = -0.08867015686356589,
        E = 0.05228761884074473,
        L = 0.13564307634554948,
        A = -0.13665052250410184,
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
        S = -0.04376699585028585,
        B = -0.0712830739332929,
        E = 0.1011145889423419,
        L = 0.11956819416534101,
        A = -0.07947482653109235,
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
        S = 0.06829460876495679,
        B = 0.07316285526621803,
        E = 0.05609986410715469,
        L = 0.3494468671000277,
        A = 0.023815534382150876,
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
        S = 0.16828302913455656,
        B = 0.039797563343625095,
        E = 0.04779077786674469,
        L = 0.7280861261072604,
        A = 0.01010660775426197,
    ),
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
        S = 0.09644784897086736,
        B = 0.19349404276640883,
        E = 0.044564539595788336,
        L = 0.6337301865302405,
        A = 0.012533127488892142,
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
        S = 0.09597540354363084,
        B = 0.1486473894943779,
        E = 0.12110374534168805,
        L = 0.6169486458992428,
        A = 0.017463071510668542,
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
        S = 0.005492704435363646,
        B = 0.0070945423553232054,
        E = -0.015934899078963713,
        L = 0.2395285110124638,
        A = -0.022201998416096293,
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
        S = 0.39123335735749243,
        B = 0.2470870976363441,
        E = 0.10873391742073815,
        L = 0.9495507235061129,
        A = 0.028308972798016276,
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
        S = 0.029727532480165027,
        B = 0.05623137279820625,
        E = 0.07304726442983636,
        L = 0.5867463029189092,
        A = 0.02468784092106518,
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
        S = 0.05596804991841053,
        B = 0.04050264745694824,
        E = 0.018856474018728468,
        L = 0.3248303797697628,
        A = -0.0137011141103817,
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
        S = -0.055631518362228495,
        B = 0.060192956760224466,
        E = -0.055257133478352996,
        L = 0.30711050850075705,
        A = -0.02218909492298653,
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
        S = 0.06374898688191025,
        B = 0.005811695818589282,
        E = 0.13554757769882492,
        L = 0.463323006659653,
        A = -0.003424405858415757,
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
        S = 0.016358910532127412,
        B = 0.04907472728129876,
        E = 0.0371055748017801,
        L = 0.2502893010607424,
        A = -0.01706167892407373,
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
        S = -0.08639097011159508,
        B = 0.00658609991797751,
        E = 0.0012650427111776687,
        L = 0.35227467148215524,
        A = -0.04057692538526315,
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
        S = -0.07995298634303855,
        B = 0.027387612125119358,
        E = -0.04392752644175045,
        L = 0.4738615711858426,
        A = -0.01635026659492664,
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
        S = 0.011706871889901833,
        B = 0.019336060829269308,
        E = 0.07796999676303097,
        L = 0.500625296612175,
        A = -0.01670434632722287,
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
        S = 0.01107942143699683,
        B = 0.023720198509892158,
        E = -0.007870741159925027,
        L = 0.5251339695649351,
        A = 0.00800132184867967,
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
        S = 0.16186332500300235,
        B = 0.042558124886825054,
        E = 0.11927663142614038,
        L = 0.3594138980562462,
        A = 0.06892848056760867,
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
        S = -0.006763865330510758,
        B = 0.005271368492575623,
        E = 0.045481946678770965,
        L = 0.45486407195524353,
        A = -0.018004961864800502,
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
        S = -0.009908518314991633,
        B = 0.009545771086739523,
        E = 0.062472268742481664,
        L = 0.6279111535255427,
        A = -0.01633468087505246,
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
        S = -0.020714469676267423,
        B = 0.013941850575281878,
        E = 0.030089507200217306,
        L = 0.41421791388724005,
        A = -0.01460094199050209,
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
        S = -0.010326130731838917,
        B = 0.009957504946474124,
        E = 0.06089727844669836,
        L = 0.5441226172828586,
        A = -0.011755424823038284,
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
        S = -0.002727040567633578,
        B = 0.003862668734429357,
        E = 0.018565312359493786,
        L = 0.2568356178129755,
        A = -0.0029089750622662163,
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
        S = 0.06802584087333856,
        B = 0.041824520827678076,
        E = 0.099861514347553,
        L = 0.5875477455259608,
        A = -0.000683393850384147,
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
        S = 0.16783087633394628,
        B = 0.01640647723529774,
        E = 0.13794235469776686,
        L = 0.6049485321716032,
        A = -0.011266446346230643,
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
        S = 0.004934257809161365,
        B = 0.0037409918400509784,
        E = 0.06793839596546876,
        L = 0.6435759390215676,
        A = -0.002972432957068613,
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
        S = 0.004972362421251926,
        B = 0.07025123466700317,
        E = -0.019547759176166392,
        L = 0.47266347642943846,
        A = 0.027139101073441606,
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
        S = 0.009917388917781432,
        B = 0.025657085536481244,
        E = 0.026559287010521026,
        L = 0.31836958112649627,
        A = 0.005694328059899852,
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
        S = 0.06092510397532681,
        B = 0.039829846962928996,
        E = 0.028034359939953162,
        L = 0.42606988125069417,
        A = 0.02626292593175301,
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
        S = -0.04866392163011233,
        B = -0.003935958969738948,
        E = -0.003783928769001067,
        L = 0.16768763805655074,
        A = -0.0358306635548217,
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
        S = 0.11216113935731292,
        B = 0.07841799070179493,
        E = 0.10918067066320106,
        L = 0.9077720744072152,
        A = 0.02283724729343558,
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
        S = -0.0635049238731882,
        B = -0.013868855444954213,
        E = 0.001276242136331904,
        L = 0.08184062747449711,
        A = -0.014235521716240084,
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
        S = 0.022924622248063582,
        B = 0.01883734206844398,
        E = 0.011300828145505903,
        L = 0.3928899340480831,
        A = 0.005732990705552292,
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
        S = 0.04004371190476962,
        B = 0.012291313021937596,
        E = 0.15796553171781402,
        L = 0.6481521571479352,
        A = -0.003488936786629928,
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
        S = 0.008578717543905767,
        B = 0.006504357554677618,
        E = 0.10527805386430765,
        L = 0.5044570105519329,
        A = 0.0031334136758155193,
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
        S = 0.08428322442618653,
        B = 0.22592041897188278,
        E = 0.1755590202143357,
        L = 0.7775686346270138,
        A = 0.015432396416962924,
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
        S = 0.0009337682026074075,
        B = 0.059416847977374974,
        E = -0.09393195948365742,
        L = 0.3100652916461965,
        A = -0.0454347271241544,
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
        S = 0.05410784513731747,
        B = 0.053549628934817205,
        E = -0.07347254868494099,
        L = 0.30061041983780945,
        A = -0.014706557879837795,
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
        S = 0.15384475060105166,
        B = 0.15154984916083453,
        E = 0.07459088732558548,
        L = 0.019582925464407958,
        A = 0.03228597255998458,
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
        S = -0.015719631351620952,
        B = 0.001365598165347201,
        E = -0.09608676465092156,
        L = 0.04890654350092522,
        A = -0.0370406981748883,
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
        S = 0.018258247454813567,
        B = 0.09551888425808548,
        E = 0.09308585243906063,
        L = 0.49585716138795016,
        A = 0.003017043788134594,
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
        S = 0.04134774094572971,
        B = 0.051181864440266844,
        E = 0.02446272300611082,
        L = 0.21031891664712704,
        A = -0.05447352918901864,
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
        S = 0.046777864952982355,
        B = 0.08664814362346433,
        E = -0.0865574837516407,
        L = 0.3263079298727579,
        A = 0.009308713939252745,
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
        S = 0.0006952852793178682,
        B = -0.0248379901302839,
        E = -0.1363758422972179,
        L = -0.04104923287461795,
        A = -0.03515853724677962,
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
        S = 0.05253090268255619,
        B = 0.03822744991282221,
        E = -0.1227665498630767,
        L = 0.0038489626769228225,
        A = 0.00026030922544146505,
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
        S = 0.025112962165544116,
        B = 0.016845262447668912,
        E = -0.00869500653603811,
        L = 0.11747940231259153,
        A = 0.00361755933723323,
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
        S = -0.008024231460358102,
        B = -0.0420450382130824,
        E = 0.031404757871970106,
        L = 0.43666813932725174,
        A = -0.02922913896573337,
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
        S = 0.07890019657050619,
        B = 0.07012693973290107,
        E = 0.11192450530434331,
        L = 0.5175962412688155,
        A = 0.01955896872473109,
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
        S = 0.07136614333911655,
        B = 0.017704618030973375,
        E = 0.09144732210572068,
        L = 0.55609225695303,
        A = 0.004255253184499972,
    ),
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
        S = -0.14040096978886968,
        B = -0.0634248001820067,
        E = -0.03440101597709724,
        L = -0.14485053352855629,
        A = -0.025340967432902643,
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
        S = 0.03555006794519244,
        B = -0.028508711195648184,
        E = -0.13446270395205676,
        L = -0.04346889595124816,
        A = -0.03814237982361417,
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
        S = 0.05016017354264563,
        B = 0.02881618667146003,
        E = 0.06517128475806773,
        L = 0.05876560710723183,
        A = 0.058178564168635226,
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
        S = 0.08535927079316033,
        B = -0.013513807709238714,
        E = -0.0671440217941041,
        L = 0.04447926391332405,
        A = -0.0067735286139995205,
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
        S = 0.1197398276729932,
        B = 0.13346613380574002,
        E = 0.15882390537232524,
        L = 0.5459483009857421,
        A = 0.06341964380337653,
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
        S = -0.02379688415685149,
        B = 0.057927533585605394,
        E = 0.016351387656502254,
        L = 0.20580954313421332,
        A = -0.0873242263279988,
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
        S = 0.024786298637907402,
        B = 0.06260740316684084,
        E = -0.011914441301253865,
        L = 0.3907795675203491,
        A = 0.0007389800488228148,
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
        S = 0.1218250293791457,
        B = 0.05579930240063843,
        E = 0.060510010196550036,
        L = 0.5235146867217128,
        A = 0.04346946725157431,
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
        S = 0.14426498626470796,
        B = 0.07785840055595826,
        E = 0.1043510478729576,
        L = 0.5271518283465343,
        A = 0.09596278338710335,
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
        S = -0.05275593142398085,
        B = -0.005816154749451625,
        E = 0.012644688034841658,
        L = 0.03539143444298562,
        A = -0.027087936453047412,
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
        S = -0.03472596214903009,
        B = -0.01990263091070592,
        E = 0.020777064366901597,
        L = 0.03308341044831121,
        A = -0.027966452286758214,
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
        S = 0.0303400809459326,
        B = 0.026638386141373416,
        E = 0.07933604586357032,
        L = 0.4019253057454236,
        A = -0.007193754789163,
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
        S = 0.030340080945932595,
        B = 0.026638386141373423,
        E = 0.07933604586357024,
        L = 0.40192530574542396,
        A = -0.007193754789163001,
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
        S = 0.006826050174899671,
        B = 0.07234172697829228,
        E = 0.10268929046771313,
        L = 0.43209258848316706,
        A = -0.021087415256691305,
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
        S = 0.10431937400217176,
        B = -0.0047296968261521955,
        E = 0.0704472801866697,
        L = 0.4344542481022285,
        A = -0.05070105340454789,
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
        S = -0.017751140870365,
        B = 0.09071915345612862,
        E = 0.11830987668295757,
        L = 0.3879533360889567,
        A = 0.00856339830857664,
    ),
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
        S = 0.0058755757671189335,
        B = 0.0031710730533056402,
        E = 0.01802522673307087,
        L = 0.40677895558982013,
        A = 0.027754831939247264,
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
        S = -0.051401586988953155,
        B = 0.004686778910519469,
        E = 0.0814207960247034,
        L = 0.19327643247893248,
        A = -0.05932560092208026,
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
        S = 0.025144638464613407,
        B = 0.01942468879162643,
        E = 0.08497517468646407,
        L = 0.5263332365232548,
        A = 0.012319972428469364,
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
        S = 0.08637942513250713,
        B = 0.0487537470850995,
        E = 0.06110995805731915,
        L = 0.4570764525913874,
        A = -0.07126601447862171,
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
        S = 0.1412326516679848,
        B = 0.046445077344921426,
        E = 0.09304192344152888,
        L = 0.36421355929572957,
        A = -0.04287652277309901,
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
        S = -0.14925854183120604,
        B = 0.032998759668971624,
        E = -0.061168956406393714,
        L = 0.09705579910017519,
        A = 0.038612293479822604,
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
        S = -0.20413104870067308,
        B = -0.05529063936120866,
        E = 0.056227520074277455,
        L = 0.16106536888902975,
        A = 0.027842369234221773,
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
        S = -0.012631303508528464,
        B = -0.0059874560109107215,
        E = 0.04089119769373399,
        L = 0.2853340016604805,
        A = -0.03621904677028311,
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
        S = 0.0930853846629283,
        B = -0.0034578305043528094,
        E = 0.09862641439541243,
        L = 0.8697177252538922,
        A = 0.024223633478999317,
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
        S = 0.019522377882082886,
        B = 0.0358306946999878,
        E = 0.061054621733643254,
        L = 0.46095549201655023,
        A = 0.013783158953066952,
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
        S = 0.01571694307242122,
        B = 0.016240545397735895,
        E = 0.0900251278865878,
        L = 0.19982926455640682,
        A = -0.0490816825967834,
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
        S = 0.21125617957669332,
        B = 0.3176584261130905,
        E = 0.21293584555309342,
        L = 1.003128670747086,
        A = 0.2512288991035964,
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
        S = 0.029185549527691746,
        B = 0.1211369314324244,
        E = 0.13131222452412078,
        L = 0.6552318653167511,
        A = 0.14693856258273455,
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
        S = -0.28727923134388933,
        B = 0.042047461014359154,
        E = -0.046267620057193,
        L = -0.15218755501299722,
        A = 0.10426746300118751,
    ),
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
        S = 0.019468158214182758,
        B = 0.046481241698015464,
        E = 0.14708972523980493,
        L = 0.37705793249803193,
        A = -0.020963582798099484,
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
        S = -0.012546973490622617,
        B = 0.024950605222732417,
        E = 0.01726666925560563,
        L = 0.1912202589139367,
        A = -0.03184222830046195,
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
        S = -0.01366329617640603,
        B = -0.007784751970028413,
        E = -0.037106792142205906,
        L = 0.06050530927259505,
        A = -0.01624902982381564,
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
        S = 0.16571592320825107,
        B = 0.015644459325677013,
        E = 0.053715671482910884,
        L = 0.4839193736856274,
        A = -0.00800785375242903,
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
        S = 0.11715290354591239,
        B = 0.13555612876823675,
        E = -0.016998366288009836,
        L = 0.2620752936655907,
        A = 0.06864725075732041,
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
        S = 0.018486585254417105,
        B = -0.022547083637907608,
        E = 0.02344599774672847,
        L = 0.25751195703685364,
        A = 0.010211704901316343,
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
        S = 0.0018778056713885144,
        B = 0.011308548811611453,
        E = 0.03771395284627482,
        L = 0.10946978462476935,
        A = -0.004004373072387697,
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
        S = -0.02950857938186177,
        B = 0.015764819554386623,
        E = 0.054965318425379,
        L = 0.1307884063423077,
        A = -0.003621651204365403,
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
        S = 0.02848480909159286,
        B = 0.033684408963454496,
        E = 0.02233647670825993,
        L = 0.36599225530652574,
        A = 0.2410667824777641,
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
        S = 0.0284848090915927,
        B = 0.03368440896345446,
        E = 0.022336476708263487,
        L = 0.36599225530654034,
        A = 0.2410667824777616,
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
        S = 0.08979250216905384,
        B = -0.0024691136344607936,
        E = -0.014712774474583459,
        L = 0.4826789986659347,
        A = -0.1345035530854679,
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
        S = -0.006948135510858159,
        B = -0.005831932272268974,
        E = 0.012483267051811886,
        L = 0.13325361167492478,
        A = 0.006503631477663186,
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
    index = 1850,
    label = "Ct-N3tCs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18571299402801672,
        B = 0.09161924651822091,
        E = 0.00045494319118538265,
        L = 0.3373928229608965,
        A = -0.02393394745049289,
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
        S = 0.12746594656726024,
        B = 0.026286434410655476,
        E = -0.003539791324126178,
        L = 0.3174418452731476,
        A = -0.039330272139378265,
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
        S = 0.05176109983361904,
        B = 0.007558681148134128,
        E = 0.0216703401658096,
        L = 0.3043990847122355,
        A = -0.005747437364917244,
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
        S = 0.018167271620712938,
        B = 0.008932424004097014,
        E = 0.0504262901023399,
        L = 0.13242815179041675,
        A = -0.0005011230653704712,
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
        S = 0.03309587685530887,
        B = 0.009307192377410631,
        E = 0.0899625600549583,
        L = 0.39929627690015024,
        A = -0.0016831501944892815,
    ),
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
        S = 0.012293000179138145,
        B = 0.05760375061990242,
        E = 0.03450692107694768,
        L = 0.07273025298010827,
        A = -0.03815987855109568,
    ),
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
        S = 0.007562931025778337,
        B = 0.007004973059572103,
        E = 0.02307908237767874,
        L = 0.19295260658162713,
        A = -0.002573244352386279,
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
        S = -0.0019897827998415357,
        B = 0.011008250822984098,
        E = -0.010343690281830823,
        L = 0.15473945887806617,
        A = -0.0038343217495050573,
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
        S = 0.005955635291676234,
        B = 0.02264901033825076,
        E = 0.022076464190845333,
        L = 0.1257275826725417,
        A = -0.007758680315485539,
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
        S = -0.07617325494687263,
        B = 0.08809015986448718,
        E = 0.03956704924532038,
        L = 0.26960674012318503,
        A = 0.013322342585823715,
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
        S = 0.18559861307487993,
        B = 0.09672215220486312,
        E = 0.055671607530109475,
        L = 0.7289548553376188,
        A = 0.010068301689707548,
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
        S = 0.05709702512161463,
        B = 0.16150236124917486,
        E = -0.004529085626454388,
        L = 0.5863736121854444,
        A = -0.04492486483912137,
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
        S = 0.055600084564876445,
        B = -0.016684279922347216,
        E = 0.023547883774511818,
        L = 0.07958873616371467,
        A = 0.00039961390438012374,
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
        S = 0.007723213745646102,
        B = 0.0035305129810492557,
        E = -0.006584268359790681,
        L = 0.01873774140985562,
        A = 0.008783875499245662,
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
    solute = SoluteData(
        S = 0.022234814893665092,
        B = 0.014547128384762409,
        E = -0.0003499386880861046,
        L = 0.4635281650454389,
        A = -0.005553009836286536,
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
        S = -0.014815412872923829,
        B = -0.005444474692384337,
        E = -0.005599686076671355,
        L = 0.09210442199846548,
        A = -0.008922409986355193,
    ),
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
        S = 0.10729460770187178,
        B = 0.16619924671632827,
        E = 0.07843339095065367,
        L = 0.6002178156849777,
        A = 0.005011211497759072,
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
        S = 0.08906626319589121,
        B = 0.10284901761744603,
        E = 0.08511163089722049,
        L = 0.5591363491908865,
        A = 0.008440246926620092,
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
        S = 0.008370296266011707,
        B = 0.2093393775738819,
        E = 0.07674527732322223,
        L = 0.48953601177653744,
        A = 0.0736228424157101,
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
        S = 0.043745526351771445,
        B = 0.1675761365622076,
        E = 0.1191583554578906,
        L = 0.5032769171617282,
        A = 0.022689882711440682,
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
        S = 0.0867155249149565,
        B = 0.131787205108073,
        E = 0.12522231587435714,
        L = 0.6619043969250213,
        A = 0.08856175739552113,
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
        S = 0.12071235514819333,
        B = -0.025483423035129002,
        E = -0.02680528688717311,
        L = 0.4354090532711095,
        A = 0.050506303196181296,
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
        S = 0.28619374529187086,
        B = 0.022334593907495176,
        E = 0.05686663201144108,
        L = 0.7610056373943463,
        A = 0.19995779724265747,
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
        S = 0.011232976322397958,
        B = 0.20785792771360692,
        E = 0.2237353849650696,
        L = 0.7571759646864289,
        A = 0.18052613279705684,
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
        S = 0.023972230728683944,
        B = 0.2572621479603885,
        E = 0.10808555577469096,
        L = 0.546571288575315,
        A = 0.006872965451723723,
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
        S = 0.14597450802873266,
        B = 0.21431556966500936,
        E = 0.31770666406595033,
        L = 1.0943439508619994,
        A = 0.05949207995471331,
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
        S = 0.09188832484251211,
        B = 0.09084863237973577,
        E = -0.1820131315059096,
        L = 0.28561684388588593,
        A = 0.04271357717984663,
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
        S = 0.015381902387157005,
        B = -0.025665333061448404,
        E = 0.09930242441787365,
        L = 0.3423944147878894,
        A = -0.07203336495636248,
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
        S = 0.00807374859878088,
        B = 0.09269199447032425,
        E = 0.16455390287854035,
        L = 0.5487163066368815,
        A = 0.1577583453830762,
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
        S = 0.08474652877922097,
        B = 0.08829772559461074,
        E = 0.15125636158319386,
        L = 0.5037599763120248,
        A = -0.04283091165487754,
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
        S = 0.15032544299342637,
        B = 0.07223722177689647,
        E = 0.09660542694187488,
        L = 0.7096472861217152,
        A = 0.05167908902106997,
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
        S = 0.09994544762850238,
        B = 0.021039188107992483,
        E = 0.07388158564520676,
        L = 0.6170964223781022,
        A = -0.0036565867682008674,
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
        S = 0.09994544762850241,
        B = 0.021039188107992463,
        E = 0.0738815856452068,
        L = 0.6170964223781036,
        A = -0.0036565867682008717,
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
        S = 0.12367977806837609,
        B = 0.045054150440190746,
        E = -0.021875691425653553,
        L = 0.7820086228108737,
        A = -0.012798181647959149,
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
        S = 0.03838505655208313,
        B = 0.013677008790811344,
        E = 0.008738219672092812,
        L = 0.3436107636322751,
        A = -0.001114496783260321,
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
        S = 0.2768274459021049,
        B = 0.13595069132025334,
        E = 0.09923257108897449,
        L = 0.971895620880841,
        A = 0.2873059320920083,
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
        S = 0.15822232903734665,
        B = 0.024870310489926946,
        E = 0.08944014316748464,
        L = 0.5736958326246208,
        A = 0.026768838203985804,
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
        S = 0.23317068273727365,
        B = 0.09711729487343229,
        E = 0.11117059499263784,
        L = 0.5680603046019361,
        A = 0.04772028154114067,
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
        S = 0.19104008985091908,
        B = -0.01625453718745758,
        E = 0.06314530978958977,
        L = 0.5604820395525594,
        A = -0.03175690842548088,
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
        S = 0.06867387162292825,
        B = 0.10939091597269485,
        E = 0.13968761762287052,
        L = 0.3389992542140959,
        A = 0.07657940045563866,
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
        S = -0.03630003238858848,
        B = 0.038505622469743116,
        E = 0.030986902410650063,
        L = 0.24031664434283068,
        A = -0.00904403562676484,
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
        S = 0.20731997801186197,
        B = 0.01707267124661216,
        E = 0.017437262164231596,
        L = 0.5088174279698647,
        A = 0.005484185561317295,
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
        S = -0.03630003238858838,
        B = 0.03850562246974314,
        E = 0.030986902410650163,
        L = 0.24031664434282948,
        A = -0.009044035626764832,
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
        S = -0.024814935947473287,
        B = 0.018530482435753916,
        E = 0.10101912059255758,
        L = 0.2344059666154256,
        A = 0.05160486620150672,
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
        S = -0.08022709915011919,
        B = 0.07367580152571637,
        E = 0.06972137574319519,
        L = 0.36701645520972737,
        A = 0.1635286275301103,
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
        S = 0.04441753610400187,
        B = -0.007740965293395989,
        E = 0.09163977773086392,
        L = 0.41858175288369126,
        A = -0.11502532145013829,
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
        S = 0.048277023761939306,
        B = -0.031887414977893797,
        E = 0.08797178791865064,
        L = 0.4308745321993218,
        A = 0.0006263566584182064,
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
        S = 0.06879176858152852,
        B = 0.03230287783399098,
        E = 0.11481501227381172,
        L = 0.33083706095727927,
        A = 0.028592040140198647,
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
        S = 0.06232664513685548,
        B = -0.014593847224065676,
        E = -0.1585319166353568,
        L = 0.1986670963676305,
        A = -0.041956016738796766,
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
        S = -0.06023441935780982,
        B = 0.033150010418064355,
        E = -0.2641544939502497,
        L = -0.17294087528774085,
        A = -0.029387612116807158,
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
        S = 0.09113183114743216,
        B = -0.03234754582170231,
        E = -0.029856021817485444,
        L = 0.24151975574403456,
        A = -0.05967037311541579,
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
        S = 0.21061761940543158,
        B = 0.08407410464678057,
        E = 0.046927134524356935,
        L = 0.6427530217591076,
        A = 0.1167697948486663,
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
        S = 0.13416230881585964,
        B = 0.09005874206253184,
        E = 0.2014014824463701,
        L = 1.0422566285340127,
        A = -0.03346874107275619,
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
        S = 0.11600685188321075,
        B = 0.06349764676858895,
        E = 0.1256804914809067,
        L = 0.7328842465319152,
        A = 0.02456247138145457,
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
        S = -0.017577385490837746,
        B = -0.02383482680306825,
        E = 0.020278980079524812,
        L = 0.006871219363539052,
        A = -0.024803242002367346,
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
        S = -0.05951888905756164,
        B = 0.06051412914812995,
        E = 0.15687178022966905,
        L = 0.3167076916612499,
        A = 0.008739311397709256,
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
        S = 0.08010083890631607,
        B = -0.00808133020869421,
        E = -0.05008763183179581,
        L = 0.24064345417770164,
        A = 0.024211893402235365,
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
        S = -0.01911581556484544,
        B = 0.021616556943279117,
        E = -0.07518515435693698,
        L = -0.1164102170638787,
        A = -0.002731505493876089,
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
        S = 0.12326795647361316,
        B = 0.0516731936004169,
        E = -0.0005020886658118611,
        L = 0.2315960742972502,
        A = 0.029574993743244068,
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
        S = 0.2046433824978339,
        B = 0.09606677649323513,
        E = 0.09741367214688518,
        L = 0.6535084950828739,
        A = 0.036193091797284825,
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
        S = -0.05403652185738107,
        B = 0.04062137407816361,
        E = -0.08706281186257872,
        L = 0.13892991637612548,
        A = -0.05649511291146416,
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
    solute = SoluteData(
        S = 0.0019671965661517523,
        B = 0.033338154993320074,
        E = -0.004590730439109812,
        L = 0.14754675302451525,
        A = 0.025223937099716584,
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
        S = 0.20775549204756316,
        B = 0.12263220579390798,
        E = 0.10351992560555373,
        L = 0.7811307513952007,
        A = -0.02817533830479161,
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
        S = 0.1872904607217446,
        B = 0.13393595372748224,
        E = 0.10689133264829048,
        L = 0.8289602563326923,
        A = -0.030048079219424168,
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
        S = 0.265707700181659,
        B = 0.16676663218770194,
        E = 0.128208311118181,
        L = 0.8578184848556228,
        A = -0.022526875918818932,
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
        S = -0.03219500921162151,
        B = -0.06424355724729204,
        E = 0.017997255087478684,
        L = -0.09081348657915132,
        A = -0.03601611242884347,
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
        S = 0.06665981867786296,
        B = 0.037208267694411205,
        E = 0.12983265419352047,
        L = 0.6030539213197603,
        A = -0.0331860212525486,
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
        S = -0.008740366717669418,
        B = 0.0008110740053244182,
        E = -0.03947850557722166,
        L = 0.035363450739379285,
        A = -0.008421902671830319,
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
        S = -0.028942282016873728,
        B = -0.028238298247624832,
        E = 0.049353084937332564,
        L = 0.18048243036346479,
        A = -0.015394796609789088,
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
        S = -0.03310345131081268,
        B = 0.027149062792437183,
        E = -0.03907944564289579,
        L = 0.2157059750975499,
        A = -0.03608409349938604,
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
        S = -0.06382795515503113,
        B = 0.011296487557942776,
        E = -0.12627276491472847,
        L = -0.34982980926790447,
        A = -0.011559029229009147,
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
        S = -0.02496561084227484,
        B = 0.02678236114874691,
        E = 0.1521874090963178,
        L = 0.5155760229834295,
        A = -0.032990147299489556,
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
        S = 0.05464779127495141,
        B = 0.02021792349980855,
        E = 0.1370702656511503,
        L = 0.6815771404248478,
        A = -0.006789999893499426,
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
        S = 0.05464779127495144,
        B = 0.020217923499808558,
        E = 0.13707026565115032,
        L = 0.6815771404248476,
        A = -0.006789999893499436,
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
        S = 0.10745793387830697,
        B = 0.07527750490255027,
        E = 0.14421317976401685,
        L = 0.8361367131945299,
        A = 0.016559956133607757,
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
        S = -0.018387692289226223,
        B = -0.003480212857854162,
        E = 0.11927946427471978,
        L = 0.3316201257280456,
        A = -0.01562685954628989,
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
        S = 0.05625484521252979,
        B = 0.01938454798362144,
        E = 0.09553036475170959,
        L = 0.7747076730702936,
        A = -0.05199072780894785,
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
        S = -0.002548537259699447,
        B = 0.011657607295298852,
        E = 0.06469102368596527,
        L = 0.41500103489928514,
        A = -0.0058570326440961695,
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
        S = 0.07469555644690787,
        B = 0.06515122612093804,
        E = 0.13105955121139448,
        L = 0.8145809503344211,
        A = -0.009498322701793255,
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
        S = 0.08230530764504616,
        B = -0.0050337816198390796,
        E = 0.17005442571952512,
        L = 0.7859383300732485,
        A = -0.009427315733899695,
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
        S = 0.005893486244891804,
        B = 0.01635160387490944,
        E = 0.08539953306886426,
        L = 0.30328066559451605,
        A = -0.02031845592429415,
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
        S = 0.1040465930660961,
        B = 0.16853000367057552,
        E = 0.11148994190188935,
        L = 0.7862844109511923,
        A = -0.0011855395165190805,
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
        S = 0.05112644540716333,
        B = 0.01729802292475422,
        E = 0.00462401266320741,
        L = 0.2803012469791399,
        A = 0.010131593747766426,
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
        S = 0.1781108874497731,
        B = 0.06751383734516703,
        E = -0.03231052722296701,
        L = 0.4156832603382455,
        A = 0.02012608977172538,
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
        S = 0.10733715154853163,
        B = 0.01348682400060583,
        E = -0.0020522583505407518,
        L = 0.5615365912015583,
        A = -0.035873597855176576,
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
        S = 0.12698444204260956,
        B = 0.05021581442041307,
        E = -0.036934539886177016,
        L = 0.13538201335908756,
        A = 0.009994496023958943,
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
        S = 0.13597536625645495,
        B = 0.033379867043188335,
        E = 0.16927517729779798,
        L = 0.6957063839026357,
        A = -0.009283227509544004,
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
        S = -0.05775416261988767,
        B = -0.04016938830890506,
        E = -0.017982957920445863,
        L = 0.4464905299497653,
        A = -0.04454869270350359,
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
        S = 0.09654578784001702,
        B = 0.09973106116027382,
        E = 0.16048776668228856,
        L = 0.6180963698774185,
        A = 0.33534659539107264,
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
        S = -0.11580877383452208,
        B = -0.0803033814734108,
        E = 0.09655071394250517,
        L = 0.27832018956983395,
        A = 0.018600814453273135,
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
    solute = None,
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
    index = 1113,
    label = "O2s-OsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.015843166081658554,
        B = 0.0797830790101984,
        E = 0.00965849373190521,
        L = 0.6182620351612529,
        A = -0.008536013336946341,
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
        S = 0.1014511068212865,
        B = 0.10910990505822285,
        E = 0.06495625637141623,
        L = 0.43796400348967934,
        A = -0.012541401959787474,
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
        S = 0.14945772918805056,
        B = -0.002892217229901303,
        E = 0.15314993805334778,
        L = 0.5624053680932174,
        A = 0.004703588742745024,
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
        S = 0.1115393792135213,
        B = 0.021607759379996375,
        E = 0.20910125245781927,
        L = 0.9351904750336867,
        A = 0.015003614377652942,
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
        S = -0.021335422478657176,
        B = -0.004523315995300513,
        E = 0.0543590257231479,
        L = 0.20696947887218395,
        A = -0.054201998222828014,
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
        S = 0.00457597299954342,
        B = 0.00880499879778836,
        E = 0.07367091632651473,
        L = 0.3804214629442518,
        A = 0.01791995395512864,
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
        S = 0.004575972999543409,
        B = 0.008804998797788365,
        E = 0.07367091632651473,
        L = 0.3804214629442519,
        A = 0.017919953955128683,
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
        S = 0.061528167897414096,
        B = 0.04090585342860861,
        E = 0.05021792356010413,
        L = 0.2650770582220215,
        A = -0.003610258070362646,
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
        S = 0.07063908583298319,
        B = 0.020727671626537297,
        E = 0.16313937007364737,
        L = 0.5622834257127967,
        A = -0.006691269430421432,
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
        S = -0.019707040497942585,
        B = -0.0029628631476949596,
        E = 0.009457952469331251,
        L = 0.41086027656146884,
        A = -0.02864598208465414,
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
        S = -0.03143098023842345,
        B = -0.0017729805591462685,
        E = -0.031131097788974302,
        L = -0.37769082524131625,
        A = -0.00932035724719323,
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
        S = 0.08377247665319257,
        B = 0.022953828835371684,
        E = 0.23388560944357215,
        L = 0.4735560039777697,
        A = -0.01056814734318715,
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
        S = 0.02749017346548457,
        B = -0.009926506503623747,
        E = 0.06498426958493934,
        L = 0.3209711515144961,
        A = -0.028406822602334805,
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
        S = 0.1765101634250321,
        B = 0.04313724006229132,
        E = 0.100347722024917,
        L = 0.4289041869956884,
        A = 0.06064317999253129,
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
        S = 0.15492297854757062,
        B = -0.04824297879760295,
        E = 0.010875166323021981,
        L = 0.6305756494104968,
        A = -0.017788463317838735,
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
        S = -0.010155772779355362,
        B = 0.022289194680354618,
        E = 0.0010524124583524332,
        L = 0.28526575733086224,
        A = -0.00350211658467233,
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
        S = 0.06697696260266507,
        B = 0.012320465371437234,
        E = 0.26732979350770575,
        L = 0.4965709148496105,
        A = -0.005197090168374506,
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
        S = 0.24679787769284012,
        B = 0.14810092439030983,
        E = 0.21048560012720682,
        L = 0.8726686328593857,
        A = 0.09242092760326336,
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
        S = 0.20003388214914813,
        B = 0.10365294170504742,
        E = 0.17803663157051908,
        L = 0.8190605056157064,
        A = 0.039085298387513095,
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
        S = -0.020826217981683225,
        B = -0.02425538919212208,
        E = 0.09203812285207318,
        L = -0.10151060385760245,
        A = -0.004520328597641163,
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
        S = -0.018123919545651478,
        B = -0.005364084174879186,
        E = -0.023815398394368695,
        L = -0.03136175485296396,
        A = -0.01002243597862681,
    ),
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
        S = 0.09945615132455098,
        B = 0.010002552166840654,
        E = 0.13278268295465276,
        L = 0.5767316998499967,
        A = -0.005799082197491015,
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
    index = 1131,
    label = "O2s-CbCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03650488133205619,
        B = -0.05165303870841494,
        E = 0.09674121059698773,
        L = 0.03504202828774207,
        A = -0.07965528367024725,
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
        S = 0.02416601456018503,
        B = 0.0506725710914518,
        E = 0.08093140748770843,
        L = 0.22835270003286107,
        A = -0.003110553563038427,
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
        S = 0.29274006834771943,
        B = 0.19287180451470556,
        E = 0.15126004012211966,
        L = 0.8181135955246925,
        A = 0.17252040659361123,
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
        S = -0.041910838474306,
        B = 0.07334890703335477,
        E = -0.02744188044188719,
        L = 0.3829430341690591,
        A = -0.030470103326700984,
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
        S = -0.024673274112570136,
        B = 0.0440707478335491,
        E = -0.017354248188390268,
        L = 0.19330266673012905,
        A = -0.0066140159569425755,
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
        S = -0.06589424256797931,
        B = -0.04143552231727702,
        E = 0.06913449271551175,
        L = 0.22593080221714637,
        A = -0.016722602854741832,
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
        S = 0.01692106111479363,
        B = -0.006857994032158502,
        E = -0.02779471321289504,
        L = -0.06069948084047518,
        A = 0.029362731173600682,
    ),
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
        S = -0.03618154128425975,
        B = 0.09501365092074947,
        E = 0.01583133963207024,
        L = 0.17593244829635238,
        A = 0.03498253661601274,
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
        S = 0.024973420210470013,
        B = 0.009867403802048345,
        E = 0.024278193415448072,
        L = 0.10342705953505094,
        A = 0.007666196312372147,
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
        S = 0.06814442874411587,
        B = -0.04505133185202152,
        E = 0.08846532543158345,
        L = 0.5320601705234147,
        A = -0.0258198866502129,
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
        S = 0.1842368422842674,
        B = -0.005963817775186424,
        E = 0.11380275148640151,
        L = 0.6746824032906665,
        A = -0.0032528157829217054,
    ),
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
        S = -0.02017400745939875,
        B = 0.040976841475604646,
        E = 0.08434376258214726,
        L = 0.15197678069753137,
        A = -0.009923583701138211,
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
        S = -0.08792489995362443,
        B = 0.06226074295593586,
        E = -0.02344965297136747,
        L = 0.2923180032196633,
        A = 0.009987133998961279,
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
        S = -0.01761274614156063,
        B = 0.01739138719163146,
        E = 0.1340251484544915,
        L = 0.06805821350093025,
        A = -0.038920492675759,
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
        S = -0.0643453257431319,
        B = -0.06295122111988356,
        E = 0.1773445416681305,
        L = 0.24589932943248916,
        A = -0.03123074005667285,
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
        S = -0.053161790764361914,
        B = 0.005693923515220884,
        E = 0.014228018403378851,
        L = -0.7760897265725802,
        A = -0.016323091987604794,
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
        S = -0.028970583144548825,
        B = 0.01595263571016678,
        E = 0.13008407501445562,
        L = 0.15252000362574336,
        A = 0.03505140788452565,
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
        S = -0.05515191419678284,
        B = 0.007273000950631007,
        E = 0.09024780493195422,
        L = 0.38627875800359635,
        A = -0.0002738465962943242,
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
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.013004429136908737,
        B = -0.005087053798822648,
        E = -0.03177643893444799,
        L = 0.033824141071988126,
        A = -0.0699010652780286,
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
        S = -0.03395602141158703,
        B = -0.013195566953516839,
        E = 0.11782253672892438,
        L = 0.08185801032215298,
        A = 0.0017255980281063888,
    ),
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
        S = 0.00057303209141969,
        B = -0.00481563626409813,
        E = 0.19905232586607374,
        L = 0.5348258373626528,
        A = 0.017090266509741853,
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
        S = 0.05056385053919875,
        B = 0.014227180943116943,
        E = 0.08225671954696007,
        L = 0.389421423335545,
        A = 0.030808512347988808,
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
        S = 0.11684914818176265,
        B = 0.03192389986616952,
        E = 0.00893773795961077,
        L = 0.6033757918536242,
        A = 0.024158216887871328,
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
        S = 0.00573439564607736,
        B = 0.007707456252276306,
        E = 0.04039762655087808,
        L = 0.053770413021814616,
        A = -0.005879830363818894,
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
        S = 0.028833921854815456,
        B = 0.07268914756375826,
        E = 0.14134250560257855,
        L = 0.5286201394499499,
        A = -0.0743886450303445,
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
        S = 0.08875648318127578,
        B = 0.045719605069233706,
        E = 0.10488327123371582,
        L = 0.4131166734138343,
        A = -0.015305301058525567,
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
        S = -0.010549006853333223,
        B = 0.030667660428710518,
        E = 0.05249496645409262,
        L = 0.38381225515580353,
        A = -0.03529177964453944,
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
        S = 0.00273544543881715,
        B = 0.014120645226336038,
        E = 0.07820063733592002,
        L = 0.2646967620459769,
        A = -0.0001450767127071446,
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
        S = 0.1197836068679268,
        B = 0.12860531504910402,
        E = 0.12570529326233934,
        L = 0.6449004200502954,
        A = 0.01837533697702327,
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
        S = 0.11897340217742974,
        B = -0.0517021260263951,
        E = 0.1730093740096024,
        L = 0.666862903228974,
        A = 0.03386944148125032,
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
        S = 0.007123617864566192,
        B = 0.013934406805102708,
        E = 0.10090051721465644,
        L = 0.3192056551974949,
        A = 0.01569360140883282,
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
        S = 0.11013285637767292,
        B = -0.026045914351446115,
        E = 0.07302254805221861,
        L = 0.4144635432853129,
        A = 0.006835720670452991,
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
        S = -0.0049420800791388315,
        B = 0.02477786243990826,
        E = -0.0014494653311454813,
        L = -0.17489521117710896,
        A = 0.01180001459007741,
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
        S = 0.12610709575502033,
        B = 0.033707012494430935,
        E = 0.3147731814441802,
        L = 1.1755759375925081,
        A = -0.0065077387041019424,
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
        S = 0.12889774463860387,
        B = 0.11500920361186978,
        E = 0.01982191454919055,
        L = 0.5044461586256127,
        A = -0.0005439076174783028,
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
        S = 0.042708527229082575,
        B = 0.03278708334645303,
        E = 0.048666583447386516,
        L = 0.509322371382869,
        A = 0.23245597439756696,
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
        S = 0.06822168535091103,
        B = 0.0545278178217893,
        E = 0.11498320881383828,
        L = 0.5246620863641587,
        A = -0.004277746332815298,
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
        S = -0.05682395401073259,
        B = 0.03272994195381428,
        E = 0.06881242800757795,
        L = 0.1291214705872889,
        A = 0.01761659629280091,
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
        S = 0.005416615601246928,
        B = 0.15707608544601379,
        E = 0.12380355064318507,
        L = 0.6112699354322753,
        A = 0.10229375174066488,
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
        S = -0.1254194935451041,
        B = 0.08568865242737908,
        E = 0.1044466076920337,
        L = 0.15630665807419508,
        A = 0.09004250164853266,
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
        S = 0.12758256331046322,
        B = 0.04424294341995042,
        E = 0.09535807571697069,
        L = 0.6612161087080953,
        A = 0.21125423326260126,
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
        S = 0.06303678441239079,
        B = 0.07035052358542404,
        E = 0.06071494940064321,
        L = 0.37574230761692223,
        A = 0.03811671489899725,
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
        S = 0.04183587886312241,
        B = 0.046226047744549845,
        E = 0.07621862570084201,
        L = 0.5478507482102597,
        A = 0.011480692949476432,
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
        S = -0.0036514432391306826,
        B = 0.0564029411401827,
        E = -0.11872048810848174,
        L = 0.21204192363943652,
        A = 0.019260378502879982,
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
        S = -0.14535434608999545,
        B = -0.030851342551873127,
        E = 0.11786049756764133,
        L = 0.17084318863350076,
        A = -0.043799841101486964,
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
        S = 0.05526866843912967,
        B = -0.006771350968045204,
        E = 0.1303178724892286,
        L = 0.5813618689926479,
        A = -0.0010130590239997538,
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
        S = 0.05010401140059449,
        B = 0.02344651461041122,
        E = 0.09128536727329446,
        L = 0.41387763910932224,
        A = 0.009000934148108992,
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
        S = 0.08806696236772697,
        B = 0.10657991556561593,
        E = 0.2142909882641327,
        L = 0.8224868830038768,
        A = 0.008012906307849678,
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
        S = 0.0648246978213492,
        B = 0.08720650744345707,
        E = 0.09382269327009503,
        L = 0.41512205689465903,
        A = -0.009009873897987917,
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
        S = -0.04091736510577727,
        B = 0.017317587489321776,
        E = -0.1015877649754743,
        L = -0.21426455010192832,
        A = -0.01009206415556258,
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
        S = 0.05224947479268917,
        B = -0.013003289182077353,
        E = 0.09672322133275124,
        L = 0.42465560068850383,
        A = 0.08204398168025145,
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
        S = -0.03732668313335821,
        B = 0.10842123625580265,
        E = 0.004022674895088321,
        L = 0.3824166705356927,
        A = 0.022122545445644588,
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
        S = 0.1501050124209989,
        B = 0.0730531824035475,
        E = 0.06674862038826047,
        L = 0.5992155334287428,
        A = 0.01046127552235594,
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
        S = -0.02728650104849885,
        B = 0.015804153535001846,
        E = -0.05055632262338384,
        L = -0.024483108771239333,
        A = -0.02933153423202549,
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
        S = 0.002424616495209683,
        B = -0.003023748261892601,
        E = 0.14495922856297078,
        L = 0.519618159446386,
        A = -0.018571959239902288,
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
        S = 0.029210512064034168,
        B = 0.012285622311464697,
        E = 0.12791694508270296,
        L = 0.7799644310601831,
        A = -0.009973540186429312,
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
        S = 0.01616419567468841,
        B = 0.013680700807983476,
        E = 0.052113949180311786,
        L = 0.28536245174854896,
        A = -0.02057487830701948,
    ),
    )


entry(
    index = 1145,
    label = "S2s-CtCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.007054001118048695,
        B = -0.010324555072609671,
        E = 0.06784594746621499,
        L = 0.12540850698626593,
        A = -0.011028419711041793,
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
        S = -0.0250730808894755,
        B = -0.0005629292475627068,
        E = 0.07595538617544792,
        L = 0.16831990600844113,
        A = 0.0265303178403128,
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
        S = 0.011288343736264219,
        B = -0.04978903181227603,
        E = 0.05608839121731028,
        L = 0.3115382013613964,
        A = -0.04641617768718504,
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
        S = -0.021693647623409452,
        B = 0.09076912406314501,
        E = 0.1822132110539383,
        L = 0.357343040504222,
        A = -0.019677482465488075,
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
    index = 1138,
    label = "S2s-CsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09309908116638088,
        B = -0.03650466867284033,
        E = 0.1707143000453437,
        L = 0.8087744043536172,
        A = -0.05397939361216977,
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
        S = 0.0551609046263674,
        B = 0.12117163629646947,
        E = 0.18014487996159967,
        L = 0.42763000972981385,
        A = -0.06409411905082085,
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
        S = 0.06415239787236407,
        B = 0.039111300200621875,
        E = 0.17528229171501625,
        L = 0.5890611863671907,
        A = 0.048413502130298464,
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
        S = -0.005816607220438114,
        B = -0.005572317888647983,
        E = -0.004732085909468315,
        L = -0.1953248894999691,
        A = 0.0012980377071675029,
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
        S = 0.03201556822329179,
        B = 0.001852238264779324,
        E = -0.006233301821440339,
        L = 0.08882332112119715,
        A = 0.022619035948738354,
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
        S = -0.02399832862890046,
        B = 0.01878762018641962,
        E = 0.10141624728220551,
        L = 0.27290043126430674,
        A = -0.0141950277598657,
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
        S = 0.15916836883142052,
        B = 0.057326699114436254,
        E = -0.03865029589181766,
        L = 0.3014310508163805,
        A = 0.00646045998106329,
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
        S = 0.21410177559149085,
        B = 0.02051168772843903,
        E = 0.2586875312583209,
        L = 0.85464189653835,
        A = -0.010906928230390307,
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
        S = 0.19927319368274107,
        B = 0.039079867414062476,
        E = 0.06536272164476405,
        L = 0.9382314533471228,
        A = 0.07407398797128918,
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
        S = 0.014082927986904296,
        B = -0.045884931182346114,
        E = 0.04462847022681604,
        L = 0.20737833201787118,
        A = -0.05969250405609899,
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
    solute = SoluteData(
        S = -0.06493138043163336,
        B = 0.018109155283983158,
        E = 0.18687109781669525,
        L = 0.07411089494629483,
        A = 0.0201247822698415,
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
        S = 0.0939600041015297,
        B = 0.04390797380042265,
        E = 0.24016979942897831,
        L = 1.0229699071452782,
        A = 0.06810634458944201,
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
        S = -0.019198308780779518,
        B = 0.017719893529184058,
        E = 0.18011175821966735,
        L = 0.4494831970514303,
        A = 0.04193952243291989,
    ),
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
        S = 0.04360791341123629,
        B = 0.018322924877716362,
        E = 0.212491663601368,
        L = 0.9012401960598632,
        A = 0.053906396464006225,
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
        S = 0.016230074632457275,
        B = 0.005764047395916302,
        E = 0.01965328332085552,
        L = 0.1449836898048271,
        A = 0.0058733313469178285,
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
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = None,
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
        S = -0.001084846642202214,
        B = 0.025088178596574418,
        E = 0.20499046526549547,
        L = 0.44188287405245447,
        A = -0.019682161740804983,
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
        S = 0.11246621934915711,
        B = 0.1315132400590221,
        E = 0.23524517150197782,
        L = 0.6066688045004737,
        A = -0.008168171826840372,
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
        S = 0.011390340534338225,
        B = 0.010735986763069359,
        E = 0.1194661049898391,
        L = 0.3504524328643809,
        A = -0.03554531144288429,
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
        S = 0.023617935997902413,
        B = 0.01571735803271118,
        E = 0.045163609699727665,
        L = 0.518558834516495,
        A = 0.027763916328688125,
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
        S = 0.010222939550291046,
        B = 0.01185065883516669,
        E = 0.2675131722175264,
        L = 0.7580335914327793,
        A = -0.0003619918608381504,
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
        S = 0.07472346126568259,
        B = 0.0347764765034308,
        E = 0.15293804927717392,
        L = 0.6101568850892288,
        A = 0.01700444293747525,
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
        S = 0.10402870855166133,
        B = 0.06663547103273995,
        E = 0.16087363298956084,
        L = 0.6841984906735569,
        A = 0.004453893511178804,
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
        S = -0.0058044912707697,
        B = -0.046508835405488,
        E = 0.10989648405974739,
        L = 0.234941246469635,
        A = 0.0680195049540561,
    ),
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
        S = 0.00138277412433893,
        B = 0.005563397576782402,
        E = 0.0991492256825968,
        L = 0.13032293939925033,
        A = -0.022926884491510466,
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
        S = 0.023032410675202102,
        B = 0.03223283074600383,
        E = 0.20826056309713986,
        L = 0.8347905637446317,
        A = 0.011441852562096903,
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
        S = 0.018959230321065865,
        B = -0.022486555789409318,
        E = -0.019859860336498322,
        L = 0.262729277188082,
        A = -0.04215716987416117,
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
        S = -0.0033803039047192738,
        B = -0.0038149083473380395,
        E = 0.04951140760969151,
        L = 0.02241499139948114,
        A = -0.009823966539580713,
    ),
    )


entry(
    index = 1155,
    label = "S2s-(C=S2d)Cmb",
    group = 
"""
1 * S2s           u0 {2,S} {3,S}
2   CS            u0 {1,S} {4,D}
3   [Cd,Cb,Ct,CO] u0 {1,S}
4   S2d           u0 {2,D}
""",
    solute = SoluteData(
        S = 0.004605344634458186,
        B = 0.00028723483426731797,
        E = 0.04808278521423434,
        L = 0.14198906767028013,
        A = 0.0150899465768379,
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
        S = -0.01672964601351561,
        B = 0.0037783373290045707,
        E = -0.038151189969726516,
        L = 0.04319710215014767,
        A = 0.00920722187256406,
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
        S = -0.04306046879392984,
        B = 0.027728498991043113,
        E = -0.1386470234430957,
        L = -0.14566756529430275,
        A = 0.011572985444080572,
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
        S = 0.05419227493677363,
        B = 0.06259263981446792,
        E = 0.06334947674521392,
        L = 0.49001470827058713,
        A = 0.060230381469457965,
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
        S = 0.12800815223372064,
        B = 0.04925513271748059,
        E = 0.2108048112769247,
        L = 0.9113121722223849,
        A = 0.0043047597068183365,
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
    index = 1149,
    label = "S2s-S2sCd",
    group = 
"""
1 * S2s        u0 {2,S} {3,S}
2   S2s        u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09942594068976487,
        B = -0.009756313672006772,
        E = 0.34279943237776783,
        L = 1.0697836102073435,
        A = 0.008682142403437412,
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
        S = 0.019029876618126922,
        B = 0.00812553015780202,
        E = 0.10905178029075853,
        L = 0.46247909367233414,
        A = 9.247484681749768e-05,
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
					L6: S2s-S2sCs
				L5: S2s-S46C
			L4: S2s-CH
				L5: S2s-CdH
				L5: S2s-CtH
				L5: S2s-CbH
				L5: S2s-CsH
			L4: S2s-CC
				L5: S2s-(C=S2d)Cmb
				L5: S2s-CdCb
				L5: S2s-CsCd
				L5: S2s-CtCb
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
			L4: Cds-OdCC
				L5: Cds-OdCdsCs
				L5: Cds-OdCdsCds
				L5: Cds-OdCbCb
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
			L4: Cds-OdCH
			L4: Cds-OdCC
				L5: Cds-OdCdsCds
					L6: Cds-O2d(Cds-Cd)(Cds-Cd)
						L7: Cds-O2d(Cds-Cds)(Cds-Cds)
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
					L6: Cb-(Cds-O2d)
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
				L5: Cds-CdsCtCds
					L6: Cds-CdsCt(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)Ct
				L5: Cds-CdsCdsCds
				L5: Cds-CdsCdsCs
				L5: Cds-CdsCbCds
				L5: Cds-CdsCbCb
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
					L6: Cd-CdCs(CO)
					L6: Cds-Cds(Cds-Cd)Cs
						L7: Cds-Cds(Cds-Cds)Cs
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
			L4: Cs-CCCH
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
			L4: Cs-CCOsH
				L5: Cs-CbCsOsH
			L4: Cs-COsHH
				L5: Cs-CdsOsHH
			L4: Cs-CCCOs
				L5: Cs-CbCsCsOs
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
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
					L6: Cs-(Cds-O2d)CsOsH
				L5: Cs-CsCsOsH
		L3: Cs
			L4: Cs-NCsHH
				L5: Cs-N3sCsHH
			L4: Cs-NCsCsCs
				L5: Cs-N5dcCsCsCs
				L5: Cs-N3sCsCsCs
			L4: Crs-CCHH
				L5: Crs-CrCrHH
			L4: Cs-CCCC
				L5: Cs-CbCsCsCs
				L5: Cs-CdsCdsCsCs
					L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
				L5: Cs-CtCsCsCs
					L6: Cs-(CtN3t)CsCsCs
				L5: Cs-CdsCsCsCs
					L6: Cs-(Cds-O2d)CsCsCs
					L6: Cs-(Cds-Cd)CsCsCs
						L7: Cs-(Cds-Cds)CsCsCs
				L5: Cs-CsCsCsCs
			L4: Cs-CCCH
				L5: Cs-CbCdsCsH
				L5: Cs-CbCdsCsH
					L6: Cs-(Cds-Cd)CbCsH
						L7: Cs-(Cds-Cds)CbCsH
				L5: Cs-CbCbCsH
				L5: Cs-CbCbCbH
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
				L5: Cs-CbCtHH
				L5: Cs-CbCdsHH
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
			L4: N3s-CCC
				L5: N3s-(CO)CsCs
				L5: N3s-CsCsCs
				L5: N3rs-CCC
					L6: N3rs-CrCrC
					L6: N3rs-CrCrC
						L7: N3rs-CrCrCr
			L4: N3s-CHH
				L5: N3s-CsHH
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
				L5: O2s-CdsH
				L5: O2s-CbH
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