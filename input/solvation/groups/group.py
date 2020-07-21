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
	index = 1,
	label = "C",
	group =
"""
1 * C u0
""",
	solute = None,
)

entry(
	index = 1919,
	label = "CJ2_singlet",
	group =
"""
1 * C u0 p1
""",
	solute = SoluteData(
        S = -0.004101196085712347,
        B = -0.0046931793100941175,
        E = 0.018713120420726127,
        L = 0.24301090653628293,
        A = -0.007291466310344371,
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
        S = -0.011027754526197722,
        B = -8.431631893951206e-05,
        E = 0.04398570954755759,
        L = -0.010336741921530045,
        A = 0.0013877589478878685,
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
        S = 0.09114198868888591,
        B = 0.02631257672336653,
        E = 0.2327193407178169,
        L = 0.4263480411783276,
        A = -0.009322860733174076,
    ),
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
        S = 0.07468609606262853,
        B = 0.017025802032585195,
        E = 0.2601785385173265,
        L = 0.4656278614381717,
        A = -0.00874106247579314,
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
        S = -0.019112903522767982,
        B = -0.0288473493866609,
        E = 0.13143947913662604,
        L = -0.04728998275306219,
        A = -0.006272367371429882,
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
        S = 0.13753868301010005,
        B = -0.024574684522455693,
        E = 0.0979618516051097,
        L = 0.5553982066642091,
        A = -0.02061559507831537,
    ),
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
        S = 0.06589407054930686,
        B = 0.01708317251707696,
        E = 0.0881191505620861,
        L = 0.5486152530273577,
        A = 0.003170004687835929,
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
        S = 0.15685157770218175,
        B = 0.06953012045595583,
        E = 0.09223106746916061,
        L = 0.6720287322852526,
        A = 0.054994908345387915,
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
        S = 0.07953363251102569,
        B = 0.09321123744805035,
        E = 0.11402080549637782,
        L = 0.4973682531043682,
        A = -0.0293828030142241,
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
        S = 0.13041057251657975,
        B = 0.03254677336263464,
        E = 0.30075734776154645,
        L = 1.0455726684346096,
        A = -0.005623623804104935,
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
        S = 0.132452762387606,
        B = 0.042052496009188006,
        E = 0.18095268224619307,
        L = 0.7975254750387398,
        A = -0.011705741122066075,
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
        S = 0.18040230431731585,
        B = 0.10193739227258884,
        E = 0.163343884967269,
        L = 0.8095699848630813,
        A = 0.046875406456166294,
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
	index = 10,
	label = "Cb-Cs",
	group =
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
	solute = SoluteData(
        S = 0.09481768670628245,
        B = 0.06998648302659786,
        E = 0.1261464532625522,
        L = 0.580019911027289,
        A = 0.01564111947329492,
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
        S = 0.04413798568990581,
        B = 0.08545922080908636,
        E = 0.16555076231956692,
        L = 0.6370003544519173,
        A = -0.002136465185683829,
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
        S = 0.07460749728065873,
        B = -0.04335524383234772,
        E = 0.06510017887480714,
        L = 0.4561487612964493,
        A = -0.020833243553298336,
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
        S = -0.131214465943977,
        B = -0.09036382453881746,
        E = 0.09654497728839265,
        L = 0.30806636029980056,
        A = 0.01565044131861426,
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
	index = 14,
	label = "Cb-(Cds-Cds)",
	group =
"""
1   Cd u0 {2,S} {3,D}
2 * Cb u0 {1,S}
3   Cd u0 {1,D}
""",
	solute = SoluteData(
        S = 0.10787602981158491,
        B = 0.03865373990980079,
        E = 0.2186361000569264,
        L = 0.9505848934146636,
        A = 0.012364312713172664,
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
        S = 0.006325165179927589,
        B = 0.009123589430498803,
        E = 0.11192739118416115,
        L = 0.39887342644946505,
        A = 0.014098425496912245,
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
        S = 0.10129454565640963,
        B = 0.007730208887546361,
        E = 0.09156964632319217,
        L = 0.45891301959710956,
        A = 0.004193410648624497,
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
        S = 0.09483507671058623,
        B = 0.020997297710478133,
        E = 0.18685611542572106,
        L = 0.5644860478033983,
        A = -0.007824165015698348,
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
        S = 0.05520328057168425,
        B = 0.02229226191484593,
        E = 0.057996018664336776,
        L = 0.4548869341506125,
        A = 0.051442667026443165,
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
        S = -0.03049833421090494,
        B = 0.05926535166556298,
        E = -0.013492467268101773,
        L = 0.3702230633731511,
        A = 0.04949137226897531,
    ),
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
        S = 0.07164556288035841,
        B = 0.032252355089362444,
        E = 0.0327287350923734,
        L = 0.4674956916878003,
        A = 0.03009196740271683,
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
	solute = SoluteData(
        S = 0.11080547644434266,
        B = -0.02652635597972385,
        E = 0.09137999266982605,
        L = 0.26486653180276387,
        A = -0.017047953349032252,
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
        S = 0.2352374800732635,
        B = 0.08972043837272288,
        E = 0.08196628877368993,
        L = 0.5504367289056579,
        A = -0.02437615583942166,
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
        S = -0.03268823308361274,
        B = 0.02493148845026722,
        E = 0.0847676623552514,
        L = -0.015388095654790043,
        A = -0.047319444988749564,
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
	index = 24,
	label = "Ct-CtCs",
	group =
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
        S = 0.14394270958298236,
        B = 0.08823954605590043,
        E = 0.07119704046096054,
        L = 0.8679962049289116,
        A = 0.013321795589410632,
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
        S = 0.023368796310631188,
        B = 0.02097256931121871,
        E = 0.06286861541932144,
        L = 0.5168985159963218,
        A = 0.022405027879330453,
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
        S = 0.049576280891685684,
        B = 0.014765388277102475,
        E = 0.15535246541911651,
        L = 0.5740266983528469,
        A = -0.0035126579450073156,
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
        S = 0.006325165179927582,
        B = 0.009123589430498812,
        E = 0.1119273911841611,
        L = 0.39887342644946494,
        A = 0.014098425496912252,
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
        S = 0.06865862747807813,
        B = -0.03625851523572177,
        E = 0.1005847246028105,
        L = 0.41177547916901247,
        A = -0.005993888784107847,
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
	index = 37,
	label = "Cdd-CdsOd",
	group =
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   O2d u0 {1,D}
""",
	solute = SoluteData(
        S = 0.03047465575328211,
        B = 0.025722517065783903,
        E = 0.08169053072068296,
        L = 0.461225633286627,
        A = -0.0066329918065191375,
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
	index = 49,
	label = "Cdd-CdsCds",
	group =
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
	solute = SoluteData(
        S = -0.00858558050478316,
        B = 0.003959084992249304,
        E = 0.05944187242417156,
        L = 0.6153710525518452,
        A = -0.014353425808392198,
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
        S = 0.12401248598906227,
        B = 0.11948896058618921,
        E = 0.15841041364469816,
        L = 0.6333168689267706,
        A = 0.05988026397774544,
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
        S = 0.04968050742336032,
        B = 0.09343943178680748,
        E = 0.17436113176838963,
        L = 0.4593242837635654,
        A = 0.043028808954221426,
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
        S = 0.08965543137405468,
        B = 0.062104351347143955,
        E = 0.1553970879773959,
        L = 0.4919549616705036,
        A = 0.03814112706992401,
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
        S = 0.23367177547473378,
        B = 0.08754576723422325,
        E = 0.129835720768172,
        L = 0.6044523984625416,
        A = 0.025964795101770067,
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
        S = 0.17828638657817836,
        B = 0.005766936876871923,
        E = 0.10024408775020037,
        L = 0.6246944551754013,
        A = 0.009217457037200305,
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
        S = 0.045638150062565566,
        B = -0.008481382678650354,
        E = 0.26718870316361903,
        L = 0.2606370394330534,
        A = -0.009313219369598712,
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
        S = -0.062086616467258195,
        B = 0.007113913367895253,
        E = 0.13547990517635694,
        L = 0.18394457992943522,
        A = 0.032184503086704244,
    ),
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
        S = -0.06859370777036132,
        B = -0.04183579086981738,
        E = 0.034696730568952595,
        L = 0.21008075952622302,
        A = 0.030203994200013854,
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
        S = 0.014540653464890285,
        B = 0.07692623387437812,
        E = 0.11877481942179524,
        L = 0.5546716275127066,
        A = 0.032626377778040755,
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
        S = 0.05863212348501301,
        B = 0.056543579364371696,
        E = 0.12644646526544245,
        L = 0.795993686142176,
        A = 0.05192868375207076,
    ),
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
        S = -0.017770241587473486,
        B = 0.027842988019061713,
        E = 0.035447992565700956,
        L = 0.3459070130943013,
        A = -0.02282151676034499,
    ),
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
        S = 0.04774792439020181,
        B = 0.03999317923923623,
        E = 0.11483917537966515,
        L = 0.37652279718735004,
        A = -0.06595753544475247,
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
        S = 0.05909313292722206,
        B = 0.030225373530166882,
        E = 0.12641376564929918,
        L = 0.47892644857999317,
        A = -0.009130299181067125,
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
	solute = SoluteData(
        S = -0.054152395567942685,
        B = 0.004890336864411901,
        E = 0.15404082154941295,
        L = 0.4112536733021197,
        A = -0.05380943109239908,
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
        S = 0.005941987954444543,
        B = 0.046938284944830905,
        E = 0.05411241049049556,
        L = 0.3231762223060821,
        A = -0.07949042212827219,
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
        S = -0.055749325295320666,
        B = -0.004624536794711968,
        E = 0.042181580154811875,
        L = 0.13625747796761647,
        A = -0.020079820393904307,
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
        S = 0.11318621748666792,
        B = 0.009898526612360186,
        E = 0.10538753156990342,
        L = 0.5600354545383466,
        A = -0.040933867447690515,
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
        S = 0.035154068649431415,
        B = 0.03994516049072787,
        E = 0.0433582087736406,
        L = 0.4264228999206281,
        A = 0.24839688774121113,
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
	solute = SoluteData(
        S = -0.00029893310833647416,
        B = 0.0126141583257971,
        E = 0.07955509183760186,
        L = 0.18593748040391234,
        A = 0.0054311491580075295,
    ),
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
        S = 0.02087324424455349,
        B = 0.05182221502732242,
        E = 0.055719641020393604,
        L = 0.39269525547088463,
        A = -0.008247462570102481,
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
        S = 0.034076447585444425,
        B = -0.0008484848589340817,
        E = -0.026034339908916064,
        L = 0.2111111842296517,
        A = -0.011637249219353928,
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
        S = -0.029529075792499977,
        B = 0.01895579247828775,
        E = 0.06118247385479256,
        L = 0.2535784510224454,
        A = 0.0014377787343838344,
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
        S = 0.01876280415745965,
        B = -0.007518933110412887,
        E = 0.04262737203259852,
        L = 0.4054798842589065,
        A = 0.005221197398506534,
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
        S = 0.1139161421285303,
        B = 0.11763305518606551,
        E = 0.09466913819653906,
        L = 0.5759341891281956,
        A = -0.005973062552936668,
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
        S = -0.018505944003211105,
        B = 0.044673252913864474,
        E = 0.1806737045181774,
        L = 0.37294645002564786,
        A = 0.016084930986218868,
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
        S = 0.12655346094499842,
        B = 0.05261277670717228,
        E = 0.11183752683519321,
        L = 0.5565723446397127,
        A = -0.05222542078190362,
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
        S = -0.03193940755164068,
        B = -0.02450077804342024,
        E = 0.10563636392985072,
        L = -0.019795375260568588,
        A = -0.01653442629362746,
    ),
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
        S = -0.029971277185185264,
        B = -0.008935916207224243,
        E = 0.058844872891036966,
        L = 0.1131717728983009,
        A = -0.03363845353042541,
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
        S = 0.15444245462578873,
        B = 0.07797222753455268,
        E = 0.12118811943209058,
        L = 0.4316795496506483,
        A = -0.009399806107746099,
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
        S = -0.10864633969066514,
        B = -0.03937083902404059,
        E = -0.00536628139478641,
        L = -0.5234444149466773,
        A = -0.023044606341901194,
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
        S = 0.07023911384471068,
        B = 0.0028896355573357984,
        E = 0.10436685046897874,
        L = 0.4852249856219089,
        A = -0.021959341025490527,
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
        S = -0.05981593288958346,
        B = 0.023306073094914902,
        E = 0.24502243288360062,
        L = 0.4294766445790159,
        A = -0.04745603541267447,
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
        S = -0.08099113642709224,
        B = 0.00729047925172681,
        E = 0.0012083853136037426,
        L = 0.3595114428693104,
        A = -0.028323138828987165,
    ),
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
        S = -0.00453612464097346,
        B = 0.00842051921595281,
        E = 0.04175129351120858,
        L = 0.4496572007567839,
        A = -0.01437262430489218,
    ),
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
        S = 0.030474655753282127,
        B = 0.025722517065783906,
        E = 0.08169053072068273,
        L = 0.4612256332866251,
        A = -0.0066329918065191435,
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
        S = 0.008448966355755158,
        B = 0.07760658084720407,
        E = 0.041953443314880275,
        L = 0.422681014686011,
        A = -0.01056543639660007,
    ),
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
        S = 0.02258716202385683,
        B = 0.023458392369838467,
        E = 0.06124313507485185,
        L = 0.5160899811406763,
        A = 0.003541420419734967,
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
        S = 0.0012097082178004954,
        B = 0.0038682714075933275,
        E = 0.08017537537881865,
        L = 0.6436904920681734,
        A = -0.012393893917125842,
    ),
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
        S = 2.158219665440649e-05,
        B = 0.016800438861568946,
        E = 0.0672112701307535,
        L = 0.48829564589043806,
        A = -0.013164668113452528,
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
        S = 0.1237385507337973,
        B = 0.06202948878951369,
        E = 0.02959826035206302,
        L = 0.5181530680282794,
        A = -0.0022049661083804995,
    ),
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
        S = 0.02785155612232175,
        B = 0.06354244203136547,
        E = 0.09979667516590703,
        L = 0.43919979855673996,
        A = -0.013023812941574616,
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
        S = 0.032682590213873514,
        B = 0.03145468730203127,
        E = 0.08827085626053022,
        L = 0.5398049119534342,
        A = -0.008947135646148881,
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
        S = 0.02221283569349954,
        B = 0.019858457878355995,
        E = 0.017322127662414664,
        L = 0.4629084352535398,
        A = 0.00481396972254759,
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
        S = 0.08173971514365447,
        B = 0.016364977849856816,
        E = 0.1888854104476327,
        L = 0.8191600383460912,
        A = 0.0007775408034978203,
    ),
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
        S = -0.004418402898254931,
        B = -0.018391456670802043,
        E = 0.056165699037086965,
        L = 0.2390832713417014,
        A = -0.03777892783013778,
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
        S = -0.0038326111938612184,
        B = -0.031466932117658275,
        E = 0.05204982549054335,
        L = 0.20731862342163937,
        A = -0.040033272608436005,
    ),
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
        S = -0.009619057289083984,
        B = 0.0016832082211477436,
        E = 0.14146924355554386,
        L = 0.3555597602170567,
        A = -0.05798245707081932,
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
        S = 0.053274712645394774,
        B = 0.08334805748780953,
        E = 0.20702972978759482,
        L = 0.45737529501156954,
        A = 0.004563220475851591,
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
        S = 0.06299716496044383,
        B = 0.04770347229674434,
        E = 0.2298373498679398,
        L = 0.9090268750108935,
        A = 0.08959014692642439,
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
        S = -0.06620458642305813,
        B = -0.010452667792969897,
        E = 0.08314803868517355,
        L = 0.06751063796486236,
        A = -0.04355583559837447,
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
        S = 0.10323816430237634,
        B = 0.0189162085840029,
        E = 0.09984441091022388,
        L = 0.4043897494758535,
        A = -0.02181719978960337,
    ),
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
        S = 0.025084524806129375,
        B = 0.02191482271909999,
        E = 0.09910626149241411,
        L = 0.40930697762176527,
        A = -0.022534453793335327,
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
        S = 0.056432711337079576,
        B = 0.027447274736940922,
        E = 0.07583942791710356,
        L = 0.6253219991445461,
        A = -0.002321125269545872,
    ),
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
        S = 0.029674059038227795,
        B = 0.00788535534568729,
        E = 0.11859045530105586,
        L = 0.38038386273331265,
        A = -0.009719885371440565,
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
	solute = SoluteData(
        S = 0.10146659261064989,
        B = -0.0004414532016699722,
        E = 0.10000649319001624,
        L = 0.4639561003508131,
        A = 0.005634874453035421,
    ),
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
        S = -0.03162210803023215,
        B = 0.07664020728705619,
        E = 0.10753862401749668,
        L = 0.30469005776269287,
        A = 0.007913082851931952,
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
        S = 0.1485526309199529,
        B = 0.010516045573000232,
        E = 0.1301330951148226,
        L = 0.5597797653972243,
        A = -0.013109353546444711,
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
        S = -0.06435962722676579,
        B = -0.055653682579936976,
        E = 0.19663332042739343,
        L = 0.2825865478319233,
        A = -0.045880716766919086,
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
        S = -0.08526109919385289,
        B = -0.02225864931921813,
        E = 0.08826289106688018,
        L = 0.28972684211609573,
        A = -0.008742593676645512,
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
        S = 0.14395718275046002,
        B = -0.01599103111380019,
        E = 0.18181915536866244,
        L = 0.6967964511877794,
        A = -0.001518205804747376,
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
        S = 0.016179921314761578,
        B = 0.00829659450488635,
        E = 0.03664635442357659,
        L = 0.3205272545305269,
        A = -0.002528588927307978,
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
        S = -0.002587146292846639,
        B = 0.019555178308081338,
        E = 0.08970986246721972,
        L = 0.38359184337659014,
        A = -0.020675238539415868,
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
        S = 0.03828229184956405,
        B = -0.002174289897684322,
        E = 0.0446105422287201,
        L = 0.3784220829932893,
        A = -0.001808249815521261,
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
        S = 0.013444817129334246,
        B = -0.008171538922883798,
        E = 0.0672788269272626,
        L = 0.26094155454598694,
        A = -0.010078647503326202,
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
        S = -0.039920181804616026,
        B = 0.03134866519535,
        E = 0.1736528237763072,
        L = 0.20934121528145358,
        A = 0.05254865777699663,
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
        S = -0.003989779955650588,
        B = 0.02146630375969185,
        E = 0.027983196821631764,
        L = 0.2554117228313428,
        A = 0.0022132696880723095,
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
        S = 0.0090113955065426,
        B = 0.028544296341002515,
        E = 0.030400823633030295,
        L = -0.09945847048372485,
        A = 0.019956493969888,
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
        S = 0.08667962916530374,
        B = 0.12230987752366045,
        E = 0.013714926359092399,
        L = 0.4891126350619062,
        A = -0.005212166034739433,
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
        S = 0.13640500467114364,
        B = 0.11536547018327352,
        E = 0.05064047898714162,
        L = 0.599896860876509,
        A = 0.02443894197292142,
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
        S = 0.0858508749651425,
        B = 0.04894149858375247,
        E = 0.07915338167583733,
        L = 0.4064065840027144,
        A = -0.023842519498591543,
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
        S = 0.1665218540092053,
        B = 0.1870436447374351,
        E = 0.06570165583402018,
        L = 0.6691727784621381,
        A = 0.04185159735730441,
    ),
)

entry(
	index = 329,
	label = "Cs",
	group =
"""
1 * Cs u0
""",
	solute = SoluteData(
        S = 0.0332414455573995,
        B = 0.13382470907439817,
        E = 0.08212129906187167,
        L = 0.5471172162575723,
        A = 0.024257772356472706,
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
        S = 0.022272329413342094,
        B = 0.012968013494282905,
        E = 0.01561024806035448,
        L = 0.42321208390621573,
        A = -0.005907529433431764,
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
        S = 0.05568920250554059,
        B = 0.15470279619153177,
        E = -0.03267112383678068,
        L = 0.5390993421637139,
        A = -0.0445079761587393,
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
        S = 0.0347448323821717,
        B = 0.017067994985180825,
        E = -0.15526559173974966,
        L = 0.39156251164070477,
        A = -0.014090334147104071,
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
        S = 0.17563204691404719,
        B = 0.09833948543763403,
        E = 0.033660436090143096,
        L = 0.6848887427367323,
        A = 0.0028243838295255825,
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
        S = 0.0802908228817134,
        B = 0.18907125883282022,
        E = 0.02997145528603334,
        L = 0.5755640063041649,
        A = 0.0056571852510162585,
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
        S = 0.15103983020043105,
        B = 0.0012741849086939671,
        E = -0.10862521535081612,
        L = 0.5386079612305862,
        A = -0.004878972546539951,
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
        S = 0.10013374254656345,
        B = 0.022497151672851788,
        E = 0.07620062665791039,
        L = 0.6218013069815848,
        A = -0.0035590244717434816,
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
        S = 0.03910089530367503,
        B = 0.13586907859114422,
        E = -0.26296835505008387,
        L = 0.3936265485698976,
        A = 0.053565636128990804,
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
        S = 0.16518967933328305,
        B = 0.057408316144121646,
        E = -0.04342355029643704,
        L = 0.7045895386184363,
        A = -0.023558186814236454,
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
        S = 0.13407732187843258,
        B = 0.22140385687866154,
        E = 0.12329035526880387,
        L = 0.6758480695943261,
        A = 0.029976594107290984,
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
        S = -0.02983791857384878,
        B = 0.1007192174707088,
        E = 0.06970236446748582,
        L = 0.4744046267299676,
        A = -0.009748589630867692,
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
        S = 0.06270465580437186,
        B = 0.1888293419283702,
        E = 0.07871110120442114,
        L = 0.5480008337990431,
        A = -0.0037370768825059773,
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
        S = 0.1802899057458388,
        B = 0.17682175024124994,
        E = 0.10457678075654084,
        L = 0.6437993156475997,
        A = 0.04036537664319463,
    ),
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
        S = 0.1721438400552021,
        B = 0.04836672414867764,
        E = 0.033989200877442845,
        L = 0.6550660533639839,
        A = 0.005807613449301496,
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
        S = -0.07818611960970048,
        B = 0.0075722910989238735,
        E = -0.07088159208463864,
        L = 0.39112917444846856,
        A = -0.026375121629508336,
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
        S = -0.03090381797405773,
        B = 0.05223178714787238,
        E = -0.05982466694667943,
        L = 0.35210519069707047,
        A = -0.018289250325859867,
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
	solute = SoluteData(
        S = -0.03293913670291486,
        B = 0.008126714722409011,
        E = 0.004366911372741741,
        L = 0.3131097827910774,
        A = -0.015435656362564297,
    ),
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
        S = -0.057301239687652925,
        B = 0.02815719822311473,
        E = -0.04236635936386797,
        L = 0.5283591687356811,
        A = -0.009085033077403593,
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
        S = -0.07377858659452068,
        B = 0.06421283145102845,
        E = -0.01571082535520052,
        L = 0.320019783621583,
        A = -0.026713626995637313,
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
        S = -0.07302979310840821,
        B = -0.012937533317734623,
        E = 0.02101076250085377,
        L = 0.1797818757663577,
        A = -0.034059783806051555,
    ),
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
        S = -0.06824334101320213,
        B = -0.039412695097402466,
        E = -0.02809273532757504,
        L = 0.4034932061555509,
        A = -0.03517574704433412,
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
        S = 0.05545070420818659,
        B = 0.034036399084486434,
        E = 0.024292716781588394,
        L = 0.40687044967704034,
        A = 0.006241519153564101,
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
        S = 0.01494912737216766,
        B = 0.05766322570461193,
        E = -0.09990467608609556,
        L = 0.358735440724109,
        A = -0.04119514733275048,
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
        S = 0.06565112518501205,
        B = 0.01337179809346539,
        E = 0.04759909599227211,
        L = 0.7637140463207992,
        A = -0.04319539801248974,
    ),
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
        S = 0.19019171230165333,
        B = 0.1393850966228007,
        E = 0.09716257350519934,
        L = 0.8969913699030132,
        A = -0.02258645228460084,
    ),
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
        S = 0.13176857771610637,
        B = 0.02597055272667083,
        E = 0.021379425851106207,
        L = 0.6889532601911144,
        A = -0.033354999306307684,
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
        S = 0.07714755333482914,
        B = 0.012695672494346747,
        E = 0.13000129683808243,
        L = 0.49341765018229783,
        A = -0.019162237004149308,
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
        S = -0.0031745902010184438,
        B = 0.00044911238449079,
        E = -0.0018242905179063562,
        L = 0.5019240194739002,
        A = -0.0004349411052366079,
    ),
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
        S = -0.013123826086474239,
        B = 0.0695109282549194,
        E = -0.01330865087855886,
        L = 0.3857755043192536,
        A = 0.0013231209034258661,
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
	solute = SoluteData(
        S = 0.007700162041292686,
        B = 0.00781898748606295,
        E = 0.06972261592271257,
        L = 0.6053695338345625,
        A = -0.0035636311845813552,
    ),
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
        S = 0.01380535792317722,
        B = 0.022460353462945434,
        E = 0.010046096211342517,
        L = 0.5357017295829305,
        A = 0.006901327858459534,
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
        S = -0.04667774074867878,
        B = 0.08894644885734676,
        E = 0.026906942810084763,
        L = 0.27584998989367265,
        A = 0.006669765600775624,
    ),
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
        S = -0.25751470644373264,
        B = -0.05588695723573798,
        E = 0.01739775890962204,
        L = 0.15354972284751575,
        A = 0.023582677699726603,
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
        S = -0.0010173794122155463,
        B = 0.013207410748845594,
        E = 0.013117166248617885,
        L = 0.41105502305214214,
        A = 0.010465654753782376,
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
        S = 0.06246265476282281,
        B = 0.07788856031485314,
        E = 0.025007714187730488,
        L = 0.543264622000834,
        A = 0.02454034739540399,
    ),
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
        S = -0.06690076049930986,
        B = -0.027201808099531447,
        E = 0.03874652625171541,
        L = 0.12442354946534856,
        A = -0.015978469226078984,
    ),
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
        S = 0.13987166217064395,
        B = 0.018241735783269614,
        E = -0.0007965181683291095,
        L = 0.31363154159262824,
        A = -0.03906149071137759,
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
        S = -0.00498092250740735,
        B = -0.009608487277615903,
        E = 0.011010540433164791,
        L = 0.13221834635751467,
        A = 0.008310924371744252,
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
        S = 0.001157327220108552,
        B = 0.009802758999349093,
        E = -0.006241773532953319,
        L = 0.16514660367292305,
        A = -0.004243466573969697,
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
        S = 0.010790058789258565,
        B = 0.0005657806326143238,
        E = -0.0056337095172087626,
        L = 0.019918180948565425,
        A = 0.009859053181135932,
    ),
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
        S = -0.021286088747558746,
        B = -0.032798134370492546,
        E = 0.03061860236283267,
        L = 0.397253413952637,
        A = -0.024790404771556925,
    ),
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
        S = 0.0643719456335884,
        B = 0.024464806064243713,
        E = 0.05106827829767368,
        L = 0.5886222052618169,
        A = 0.0392449006610956,
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
        S = -0.11520315832192184,
        B = 0.05736199557005814,
        E = -0.029954050588961292,
        L = 0.28088889696291647,
        A = 0.015545580085833548,
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
        S = -0.01325548128236435,
        B = 0.011087570793283437,
        E = -0.00989704873346254,
        L = 0.4883766970107785,
        A = -0.024853427517585912,
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
        S = -0.023735798758295564,
        B = 0.001564585755939747,
        E = -0.00820836927508299,
        L = 0.1202842412211,
        A = 0.002622486705177009,
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
        S = 0.1701142690074311,
        B = -0.04309219288631602,
        E = 0.021634751589059326,
        L = 0.673742473152982,
        A = -0.028776758977967342,
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
        S = -0.23438494411772556,
        B = -0.01679611108849003,
        E = 0.13944279055948222,
        L = 0.12105100023175493,
        A = -0.006221347011697671,
    ),
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
        S = 0.09368073666417466,
        B = 0.0086637770115185,
        E = 0.06736080812367082,
        L = 0.542773174938132,
        A = 0.005560248613163528,
    ),
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
        S = 0.0822127925104954,
        B = 0.06461900390245445,
        E = 0.075314342352213,
        L = 0.5066324863138876,
        A = 0.04225502506813657,
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
        S = 0.060505468158070334,
        B = 0.06779494167391033,
        E = 0.09779430824666255,
        L = 0.6034574332863797,
        A = 0.013509400986594228,
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
        S = -0.015940069784450252,
        B = 0.037690127379592694,
        E = 0.18412458453609165,
        L = 0.25898564872910934,
        A = 0.007106486995233711,
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
        S = 0.05636573598989752,
        B = 0.008697285009550602,
        E = 0.0428202953096295,
        L = 0.3335568920113306,
        A = -0.010656922667924259,
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
        S = 0.0354860036738375,
        B = -0.02177337408715477,
        E = 0.09185340722907205,
        L = 0.380096614883641,
        A = 0.0006736697068282018,
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
        S = -0.10765981912788737,
        B = -0.013478276415607022,
        E = 0.06855618836835141,
        L = 0.14193371238919242,
        A = -0.03681391495316959,
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
        S = 0.021226611381081843,
        B = 0.026743348173501755,
        E = 0.055487380344153285,
        L = 0.38607522591413834,
        A = 0.005521602887078235,
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
        S = 0.06245343262592868,
        B = 0.04889341761804775,
        E = 0.025133873195637348,
        L = 0.44948499333764097,
        A = 0.025258535309363384,
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
        S = -0.021868121484945758,
        B = 0.0420859331257354,
        E = 0.027590419616383227,
        L = 0.25984081765235195,
        A = 0.015114785771100613,
    ),
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
        S = 0.05229153537432181,
        B = 0.002641760338789057,
        E = 0.08180465846125146,
        L = 0.2925064511180811,
        A = -0.02955280457416353,
    ),
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
        S = 0.012099653059310902,
        B = -0.006310005240476706,
        E = 0.0645751112906756,
        L = -0.26046542771136133,
        A = -0.002400644469922984,
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
        S = 0.01371971059993573,
        B = 0.011193032518179881,
        E = 0.02723449275914107,
        L = 0.5232593420817452,
        A = -0.006449450310693584,
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
        S = 0.18673272160540513,
        B = 0.05321065419018941,
        E = 0.10687643784997411,
        L = 0.4385372413902415,
        A = 0.05371024292428021,
    ),
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
        S = 0.11749335532254353,
        B = 0.015141642787581367,
        E = 0.12773597612014045,
        L = 0.5892296388664754,
        A = 0.07671951308448037,
    ),
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
        S = 0.09918825096145004,
        B = 0.08099549979808046,
        E = 0.11507650802362267,
        L = 0.4655331305081367,
        A = 0.09208848459577998,
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
        S = 0.15310002171593978,
        B = 0.04673949738826772,
        E = 0.13873991492933968,
        L = 0.5028401147480075,
        A = 0.05934371906179595,
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
        S = -0.0011753618570689015,
        B = 0.006541990178162352,
        E = 0.12704684735650593,
        L = 0.30454431837763485,
        A = 0.008036096206979247,
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
        S = 0.017847218547259906,
        B = 0.009018581255396698,
        E = 0.062290442316183345,
        L = 0.13435638638009773,
        A = -0.0008218703970528579,
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
        S = 0.11023719034268162,
        B = 0.012561498869405193,
        E = 0.15997698757346504,
        L = 0.5223580562582995,
        A = -0.0036196628228355593,
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
        S = -0.07446901805367394,
        B = 0.07134022367596987,
        E = 0.11792914393307848,
        L = 0.32779621999914094,
        A = -0.008882913327798411,
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
        S = 0.03582848874363877,
        B = 0.05584001339083286,
        E = 0.08147384263478955,
        L = 0.27691646488692057,
        A = 0.0030398697584293256,
    ),
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
        S = 0.01794454104238315,
        B = -0.01791471268615584,
        E = -0.12537850773389586,
        L = 0.052781361867994404,
        A = -0.03450989980340529,
    ),
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
        S = 0.055314616481795274,
        B = -0.03575301920073961,
        E = -0.12337779695775099,
        L = 0.0029293976741740025,
        A = -0.03658490192803714,
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
        S = 0.2646455388572495,
        B = 0.1115856664392152,
        E = 0.1190195861014129,
        L = 0.7223402295634406,
        A = 0.05322261016258456,
    ),
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
        S = 0.19535808062891383,
        B = 0.14769468833863006,
        E = 0.0951786332879227,
        L = 0.1563693831118337,
        A = 0.017303496371455975,
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
        S = 0.09431493126845683,
        B = -0.0064709799981786725,
        E = -0.026170878657258194,
        L = 0.28470942864402915,
        A = -0.09847296600362514,
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
        S = 0.16495633916832939,
        B = 0.05039717848903462,
        E = 0.023306380623189647,
        L = 0.2038165957683611,
        A = 0.03304938674622018,
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
        S = -0.0026147192833931355,
        B = 0.07232375353174222,
        E = 0.10462486896697384,
        L = 0.11708699591881443,
        A = -0.010173013370732929,
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
        S = 0.0319171516399007,
        B = 0.01705539373638326,
        E = 0.014192735704726438,
        L = 0.22254492365805015,
        A = -0.0018143532293044232,
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
        S = 0.05406528274404945,
        B = 0.039066480503925215,
        E = -0.07287358455944018,
        L = 0.0659338993972759,
        A = 0.001988806788425274,
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
        S = 0.052031802993052774,
        B = 0.008018971237598194,
        E = 0.027770026192697715,
        L = 0.13617488703880987,
        A = 0.013880475999175997,
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
        S = -0.039395654540194114,
        B = -0.016944003627282198,
        E = 0.08385079123474971,
        L = 0.1719437115355478,
        A = 0.12900247925567057,
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
        S = 0.07194873068722621,
        B = -0.01121451601268989,
        E = -0.029725692764168372,
        L = 0.094902211310836,
        A = -0.020141076217254347,
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
        S = -0.07107372648272763,
        B = -0.05503703579738821,
        E = -0.0432348813063833,
        L = -0.072716181839841,
        A = -0.02208178450109087,
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
        S = 0.004192525118111532,
        B = 0.06061705535344181,
        E = 0.005892512173479447,
        L = 0.14239910350487517,
        A = 0.03339990488726123,
    ),
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
        S = 0.09119562000267134,
        B = 0.049803902335579735,
        E = 0.022958842475522052,
        L = 0.3805696760799154,
        A = -0.015527150265070922,
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
        S = -0.20852143493409084,
        B = 0.055380905867674,
        E = -0.005839259482172238,
        L = -0.1011598942752668,
        A = 0.14919555684321714,
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
        S = 0.11113032222214903,
        B = 0.15028299932842187,
        E = 0.013934710534993034,
        L = 0.26157252305962764,
        A = 0.041181936628941096,
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
        S = -0.036256658937167674,
        B = 0.12255358447206048,
        E = 0.04633903035439149,
        L = 0.2570933420337249,
        A = 0.016861839208697205,
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
        S = 0.022705978328276453,
        B = 0.043611511357716425,
        E = -0.04292450196986186,
        L = 0.26111788058469865,
        A = -0.004893635313372493,
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
        S = 0.06500982632814269,
        B = 0.05654227540738327,
        E = -0.06666987580551952,
        L = 0.3478794492982239,
        A = -0.015333853419648737,
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
        S = -0.010153601147445832,
        B = 0.03979247311782816,
        E = -0.14285180291772015,
        L = 0.21019451826252544,
        A = -0.014498465988517248,
    ),
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
        S = -0.1654294501537048,
        B = 0.04321864080977844,
        E = -0.06840749937665055,
        L = 0.14066307968767466,
        A = 0.03825615643842937,
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
        S = 0.08322517138004833,
        B = 0.08918960573702751,
        E = -0.075683289069982,
        L = 0.4029992238815315,
        A = -0.0019483460205159608,
    ),
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
        S = -0.05153245349282287,
        B = 0.02871013466605751,
        E = -0.03609769013275091,
        L = -0.08995933472099917,
        A = -0.002433286353467825,
    ),
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
        S = 0.06769575874265697,
        B = 0.13297628907666592,
        E = 0.2501082355601123,
        L = 0.6312811428243295,
        A = -0.024403512287077347,
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
        S = -0.1806208822879332,
        B = -0.0035001622265976176,
        E = -0.21441508236572676,
        L = -0.25676471989328714,
        A = -0.000623260172367494,
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
        S = 0.07521716219990958,
        B = 0.053086540947522326,
        E = 0.14469963120568516,
        L = 0.6244416683465527,
        A = -0.03139727756889353,
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
        S = 0.1811970884406012,
        B = 0.01056609426388237,
        E = 0.1783771750572251,
        L = 0.4732690283221581,
        A = 0.013536861177351705,
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
        S = 0.13692740515755647,
        B = 0.08130185380913195,
        E = 0.1407198089152997,
        L = 0.7060504747778723,
        A = -0.0030281032949890127,
    ),
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
        S = 0.1414395273167519,
        B = 0.07078499166418278,
        E = 0.08532813125106782,
        L = 0.8060990148768655,
        A = 0.022801529270738845,
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
        S = 0.09993489622621479,
        B = 0.06340322731722713,
        E = 0.08689703959037699,
        L = 0.8261523243084758,
        A = -0.005689933252803495,
    ),
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
        S = 0.2926641910006172,
        B = 0.1710691361924526,
        E = 0.12138992595466773,
        L = 0.8975517762464219,
        A = -0.011069584903415194,
    ),
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
        S = 0.12148156916725872,
        B = 0.07732539699829742,
        E = 0.15262390913449064,
        L = 0.45413894207651156,
        A = -0.013694326339616977,
    ),
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
        S = 0.14173737594517835,
        B = 0.07977649988370568,
        E = 0.07596622381492694,
        L = 0.8510150735182709,
        A = 0.022370935889283933,
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
        S = -0.02891114107164928,
        B = 0.005902739106102253,
        E = -0.007435472643423692,
        L = -0.16938932574287285,
        A = 0.006089597620322089,
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
        S = 0.0404303689881986,
        B = 0.00761015430738872,
        E = 0.11121936674080686,
        L = 0.7784420737795293,
        A = -0.006445869917493694,
    ),
)

entry(
	index = 1093,
	label = "O",
	group =
"""
1 * O u0
""",
	solute = SoluteData(
        S = -0.02481845784370715,
        B = -0.010907432102261756,
        E = 0.028813412054519014,
        L = -0.028248096431014363,
        A = -0.0032407633816651502,
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
        S = 0.08913557466028313,
        B = 0.03894874246410729,
        E = -0.06993195637072966,
        L = 0.24068733045417637,
        A = -0.0051855618264784,
    ),
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
        S = 0.4052682176146764,
        B = 0.24482150379009565,
        E = 0.0700515367501216,
        L = 0.8423784765901882,
        A = 0.01646343654178804,
    ),
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
        S = 0.18231717790242907,
        B = 0.059546613609583986,
        E = -0.029961710419803958,
        L = 0.2926557442940245,
        A = -0.0030439807717776188,
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
        S = 0.06498291982120173,
        B = -0.09508334845344647,
        E = 0.05880512956448261,
        L = 0.11210332096467146,
        A = -0.13092248505725732,
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
        S = 0.4277634766357593,
        B = 0.24505020442056874,
        E = 0.09467019197053637,
        L = 0.9697494164450546,
        A = 0.03379434836181867,
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
	index = 1945,
	label = "O2s-N",
	group =
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
	solute = SoluteData(
        S = 0.03447652383132647,
        B = 0.1909180502363115,
        E = 0.053493176119315027,
        L = 0.4977838584873667,
        A = 0.13901796106805522,
    ),
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
        S = 0.06688743402155103,
        B = -0.016839244973145418,
        E = 0.010988128069419557,
        L = 0.3541099085027164,
        A = -0.05004649798086718,
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
        S = -0.017192213178214427,
        B = 0.02930951806184003,
        E = 0.0602042035195823,
        L = 0.11549952239406928,
        A = -0.0019929576508964223,
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
        S = -0.03563017932444973,
        B = 0.029488059196765178,
        E = 0.05880281759330619,
        L = 0.3146473990281309,
        A = -0.012050462149060397,
    ),
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
        S = 0.10864800578452649,
        B = 0.061506324736415506,
        E = 0.16620007774835882,
        L = 0.7149189442854184,
        A = 0.1483122662284209,
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
        S = 0.035154068649430784,
        B = 0.03994516049072823,
        E = 0.043358208773646593,
        L = 0.42642289992059235,
        A = 0.24839688774120974,
    ),
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
        S = 0.026444805209357006,
        B = 0.1569535722220822,
        E = 0.08354928672481589,
        L = 0.5798501106063766,
        A = 0.140386069081905,
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
        S = 0.18396868712694828,
        B = 0.2985614797029683,
        E = 0.21145293848267896,
        L = 0.9599599348600216,
        A = 0.2494979112553731,
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
        S = 0.09374185929857792,
        B = 0.10130986339960801,
        E = 0.17169478186387255,
        L = 0.679537457440111,
        A = 0.35010181731786116,
    ),
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
        S = 0.08244008165205187,
        B = -0.00579025181003274,
        E = -0.031224345045908333,
        L = 0.22863712949931533,
        A = 0.029759101705301286,
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
        S = -0.05860792499075252,
        B = 0.10105371359661852,
        E = 0.04194006815285143,
        L = 0.5112810982441615,
        A = -0.029700126715651802,
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
        S = 0.01930042886948969,
        B = -0.02719970100117187,
        E = -0.01651063608570024,
        L = 0.0702654082092352,
        A = -0.06525047052731285,
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
        S = -0.021920439006922483,
        B = -0.022498543905189464,
        E = -0.021548822811708238,
        L = -0.056272595119733766,
        A = -0.03010295428291197,
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
        S = -0.0006585748166697022,
        B = -0.0039489298880391495,
        E = 0.0024124201511142944,
        L = 0.05754321433632132,
        A = -0.011479779501856382,
    ),
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
        S = 0.07443777425582974,
        B = -0.032629529996254104,
        E = -0.010841684737355807,
        L = 0.3640379598245171,
        A = 0.019788533587954543,
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
        S = -0.0005928655296673558,
        B = -0.08125387629868773,
        E = 0.0858742606108667,
        L = 0.26763826649166506,
        A = -0.059949058021946985,
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
        S = -0.01479849227702181,
        B = 0.0054485406550546225,
        E = 0.005455998770254124,
        L = 0.173155848931191,
        A = -0.01966243609333313,
    ),
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
        S = 0.04740742468866109,
        B = 0.09095173867649659,
        E = 0.06619403634890779,
        L = 0.22470652891625612,
        A = -0.04366266343732936,
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
        S = 0.06965921209602143,
        B = 0.22860428773580826,
        E = 0.15476618784549273,
        L = 0.6880797052717293,
        A = 0.023468705752352582,
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
        S = 0.06629277182298912,
        B = 0.08392022988428272,
        E = 0.16687238735590754,
        L = 0.5137115036827165,
        A = -0.05164208952213159,
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
        S = -0.049333545851973686,
        B = -0.03891338950885982,
        E = 0.0908785441262268,
        L = 0.16410529672078492,
        A = -0.08947830006004517,
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
	index = 2025,
	label = "O2s-CS6",
	group =
"""
1 * O2s                     u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   C                       ux {1,S}
""",
	solute = SoluteData(
        S = -0.08677577107748724,
        B = -0.01960451875625655,
        E = 0.03886483804920188,
        L = 0.07365420200407939,
        A = -0.027297667075140614,
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
	index = 2026,
	label = "O2s-S_DeH",
	group =
"""
1 * O2s            u0 {2,S} {3,S}
2   [S4d,S6d,S6dd] ux {1,S}
3   H              ux {1,S}
""",
	solute = SoluteData(
        S = 0.16146370499077653,
        B = 0.10911963502500092,
        E = -0.018074005047185045,
        L = 0.49687711129289747,
        A = 0.054950846423763564,
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
        S = -0.011301094679836001,
        B = 0.03865195791428607,
        E = -0.08331724105780783,
        L = 0.07717309272191611,
        A = 0.053188570732866425,
    ),
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
        S = 0.2501254625214213,
        B = 0.1245116009256774,
        E = 0.1505056985821648,
        L = 0.8310285473816114,
        A = 0.08936159310488465,
    ),
)

entry(
	index = 1400,
	label = "S",
	group =
"""
1 * S ux
""",
	solute = SoluteData(
        S = 0.07299686511534582,
        B = 0.04615427473068231,
        E = 0.20848926596570289,
        L = 0.7730082871044683,
        A = -0.029172846606828038,
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
	index = 1160,
	label = "S2d-C",
	group =
"""
1 * S2d u0 {2,D}
2   C   u0 {1,D}
""",
	solute = SoluteData(
        S = 0.3071095270111656,
        B = 0.06318846210251323,
        E = 0.3410825166302148,
        L = 1.438641433484408,
        A = 0.011454475464163193,
    ),
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
	index = 1133,
	label = "S2s-CsH",
	group =
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
	solute = SoluteData(
        S = 0.11108325158643846,
        B = 0.08505842930920123,
        E = 0.24124581665652614,
        L = 1.025526881848979,
        A = -0.03051322980867016,
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
        S = 0.044425406113517495,
        B = 0.047218910557620286,
        E = 0.266111699543138,
        L = 0.974937901901399,
        A = 0.01681996578943104,
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
        S = 0.040079443012301,
        B = 0.01688873066674022,
        E = 0.2529235761493422,
        L = 0.8639958816744723,
        A = 0.051287149079251124,
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
        S = 0.0752435602117132,
        B = -0.007547805087960857,
        E = 0.16175054005687534,
        L = 0.7316044687510697,
        A = 0.003431851724921581,
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
	index = 1152,
	label = "S2s-SsSs",
	group =
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
	solute = SoluteData(
        S = 0.04925274883758288,
        B = 0.007022641181965108,
        E = 0.21212302557177026,
        L = 0.8935814281902871,
        A = -0.010998037996415138,
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
	index = 1148,
	label = "S2s-S2sCs",
	group =
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs  u0 {1,S}
""",
	solute = SoluteData(
        S = 0.11556370082437917,
        B = 0.05430353551717703,
        E = 0.2527118885094951,
        L = 0.9112356390404488,
        A = 0.0022183205149645135,
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
        S = 0.09322997253535917,
        B = 0.004988442795008619,
        E = 0.307305801751119,
        L = 1.0863439495207752,
        A = 0.0011353635615300138,
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
	index = 1137,
	label = "S2s-CsCs",
	group =
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
	solute = SoluteData(
        S = 0.04516975434701249,
        B = 0.18847674667987202,
        E = 0.20952981182454655,
        L = 0.7756295592269741,
        A = -0.004494791170589967,
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
        S = 0.037945997117167285,
        B = -0.02556504645000953,
        E = 0.1989595799845435,
        L = 0.7325824831617079,
        A = -0.0885746378900196,
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
        S = 0.02495337066069845,
        B = 0.01606774881598842,
        E = 0.1691465695573235,
        L = 0.3471313638456714,
        A = -0.01806063341507347,
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
        S = 0.009682548965262132,
        B = 0.025944311655639627,
        E = 0.20509334623153339,
        L = 0.31810154554784853,
        A = -0.05534749379063163,
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
        S = 0.026559579492315195,
        B = 0.033455828526167256,
        E = 0.1819478528734099,
        L = 0.5595234911378933,
        A = 0.0016956669190434862,
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
        S = 0.12612277183705034,
        B = 0.02290774499161327,
        E = 0.13015583556407737,
        L = 0.8781162001544601,
        A = 0.01805037452760744,
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
        S = -0.013636205583306473,
        B = -0.012056553359523993,
        E = 0.04947279606402822,
        L = 0.42385200723795113,
        A = -0.05393561458640937,
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
        S = 0.004199073344826797,
        B = 0.014577561845692094,
        E = 0.06076828939989757,
        L = 0.09008495163397692,
        A = 0.010081638598926523,
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
        S = 0.07748674004705942,
        B = -0.000257438803159867,
        E = 0.21617940541274475,
        L = 0.8211911341045122,
        A = -0.009960772417376775,
    ),
)

entry(
	index = 2029,
	label = "S4dd",
	group =
"""
1 * S4dd u0
""",
	solute = SoluteData(
        S = 0.015056058223832039,
        B = -0.03768795634613316,
        E = 0.18317462852905902,
        L = 0.5135347688725795,
        A = 0.01748865325885605,
    ),
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
        S = 0.10912512717969441,
        B = 0.1109685158037024,
        E = 0.24376921629439136,
        L = 0.8490729366503852,
        A = 0.009393757813924406,
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
        S = 0.2729441215149173,
        B = 0.12318218356612484,
        E = 0.14244291532582404,
        L = 0.8026499732671566,
        A = -0.029396541467535838,
    ),
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
	index = 2044,
	label = "S6dd-OdOd",
	group =
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
	solute = SoluteData(
        S = -0.02094808827252855,
        B = -0.013004018386583445,
        E = -0.04452361462704899,
        L = 0.14570737166447972,
        A = -0.025108545173211486,
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
        S = -0.027425408224331982,
        B = 0.009795507500356243,
        E = -0.02182652743437831,
        L = -0.17287271099675758,
        A = 0.003768535699339192,
    ),
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
        S = -0.0002880213118446414,
        B = 0.02359821422152404,
        E = 0.05122424249214496,
        L = 0.39562852634496476,
        A = -0.041966991284609824,
    ),
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
        S = -0.007332029586489829,
        B = -0.0786064277153443,
        E = 0.028123121619020527,
        L = -0.017559454985701498,
        A = -0.010783550993919045,
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
        S = 0.13749273349252905,
        B = 0.03465906280487495,
        E = -0.039858016436748925,
        L = 0.1799784757912805,
        A = 0.008582793906119204,
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
        S = -0.027975093546835722,
        B = 0.0780901652934739,
        E = -0.020119912851879175,
        L = -0.03109810480116496,
        A = 0.017478769773317495,
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
        S = -0.004362532796393078,
        B = -0.015897527995517347,
        E = -0.04642015308220934,
        L = 0.14242047883876988,
        A = 0.08099948299152103,
    ),
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
        S = 0.00026888889443513577,
        B = -0.0007817159531213255,
        E = -0.012982853514602459,
        L = 0.19904305598378458,
        A = -0.0024784506160260684,
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
        S = 0.1373907892998341,
        B = 0.038664835910526156,
        E = 0.08369430468788414,
        L = 0.5728017317975199,
        A = -0.027499058599480722,
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
        S = 0.0635461263938259,
        B = 0.0007726056915601632,
        E = 0.09611823894472332,
        L = 0.22849653136562795,
        A = 0.04967727703235391,
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
        S = -0.044637717878835526,
        B = 0.074507628792188,
        E = 0.2768416941326066,
        L = 0.5376196915265219,
        A = 0.11984098216432995,
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
        S = 0.12434502371215954,
        B = 0.13460359695558263,
        E = 0.13741578608262198,
        L = 0.7170908982649541,
        A = 0.11051697473583741,
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
        S = 0.16398090649602456,
        B = 0.30896698811109874,
        E = 0.15038171877427253,
        L = 0.7994250805519827,
        A = 0.12251653654915515,
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
        S = 0.25024821347974235,
        B = 0.15920293016216247,
        E = 0.23991748563272947,
        L = 0.8838650403010251,
        A = 0.11169276826874511,
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
        S = 0.25804545734278117,
        B = 0.15938227840159125,
        E = 0.1322001736911229,
        L = 1.0385345821193217,
        A = 0.30663975590062953,
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
        S = 0.042349137637249935,
        B = 0.24899551195049952,
        E = 0.25422663698619324,
        L = 0.76923535941029,
        A = 0.209207506351838,
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
        S = 0.0460123227328491,
        B = 0.09056142501054432,
        E = 0.19164020344013186,
        L = 0.6257582508455725,
        A = 0.167876684683321,
    ),
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
        S = 0.0200191442070353,
        B = 0.20966688067609746,
        E = 0.09750701502179973,
        L = 0.5461999136906203,
        A = 0.07393058758790512,
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
        S = 0.057880063249960305,
        B = 0.0036870201755125134,
        E = 0.24826274814829913,
        L = 0.6017542443049472,
        A = 0.045725798252776735,
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
        S = 0.14982372030395963,
        B = -0.04981929375693672,
        E = 0.12437982621774545,
        L = 0.9639787209681032,
        A = 0.0587380352130338,
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
        S = 0.28191658565752686,
        B = 0.06962277741184209,
        E = 0.12563131082454249,
        L = 0.9014471492687044,
        A = 0.2398176564707254,
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
        S = 0.06365978622278745,
        B = 0.04013075586399394,
        E = 0.09614401743482988,
        L = 0.5887347202023286,
        A = 0.26012410014435533,
    ),
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
        S = -0.10701656682805724,
        B = 0.0917173880806053,
        E = 0.14237948361804662,
        L = 0.38327367397213097,
        A = 0.17818143043051013,
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
        S = 0.12859128744154255,
        B = 0.09625526771805734,
        E = 0.08922187950602377,
        L = 0.8637653942668794,
        A = 0.09999361844207084,
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
        S = 0.05077939843182383,
        B = -0.019614598707964385,
        E = 0.20576490902905883,
        L = 0.5579075143396102,
        A = -0.07626337090263356,
    ),
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
        S = -0.08864158576040324,
        B = 0.09414171230836198,
        E = 0.09148031652378188,
        L = 0.3847544882115542,
        A = 0.01131271164561286,
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
        S = -0.009937628613100172,
        B = -0.08691742491541264,
        E = 0.2858283446904712,
        L = 0.299509093446071,
        A = -0.04437079651085808,
    ),
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
        S = 0.21423535393461374,
        B = 0.015097123037514584,
        E = 0.12612877527633126,
        L = 0.7395930893701895,
        A = -0.008272207296548836,
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
        S = 0.036839591222840355,
        B = -0.021100235037779292,
        E = 0.2291075437509359,
        L = 0.5998296436037377,
        A = 0.05337914214176565,
    ),
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
        S = 0.0602640679050227,
        B = -0.024325283042112386,
        E = 0.11927225622703193,
        L = 0.4241222311028623,
        A = -0.059673674676018376,
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
        S = -0.0945900807250906,
        B = -0.09970454554251579,
        E = 0.16644500607895796,
        L = 0.20194013168008673,
        A = -0.08252201741134609,
    ),
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
        S = 0.2348385220043769,
        B = 0.1219849044751088,
        E = 0.2113507037206339,
        L = 0.9998136762394643,
        A = 0.08120926217338631,
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
        S = 0.09276094890521165,
        B = 0.06100828866974193,
        E = 0.07649808911968832,
        L = 0.6369536474580955,
        A = 0.22408759511889986,
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
        S = 0.052486570986744294,
        B = 0.046705791212001635,
        E = 0.13274016517342027,
        L = 0.6158172071583903,
        A = 0.017527650417767316,
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
        S = 0.016089642371232834,
        B = 0.05381718284351396,
        E = 0.22604697851198582,
        L = 0.5541786632873571,
        A = 0.03210855628592552,
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
        S = 0.012482059807316306,
        B = 0.05965218194779756,
        E = 0.13958867654742407,
        L = 0.4660317875127705,
        A = -0.015041432272506674,
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
        S = 0.20918645997759328,
        B = 0.0638271891290988,
        E = 0.03203793536888045,
        L = 0.4307356803142477,
        A = 0.007001082263932166,
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
        S = 0.08676239803633307,
        B = 0.08061948284228848,
        E = 0.20731521211685267,
        L = 0.35308182162658364,
        A = -0.08507059105258208,
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
        S = -0.14569777727115496,
        B = 0.10093324365009261,
        E = 0.24319082665715638,
        L = 0.3331312118631573,
        A = -0.03589279398887656,
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
	index = 1906,
	label = "N3d-CdH",
	group =
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   H        u0 {1,S}
""",
	solute = SoluteData(
        S = -0.05403143802058963,
        B = 0.16760324069063476,
        E = -0.00796054645852705,
        L = 0.23919469635811738,
        A = -0.018123178810367235,
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
        S = 0.20077991221083463,
        B = -0.0080180334853898,
        E = 0.2028447335552664,
        L = 0.8451533245009137,
        A = 0.05471203860425725,
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
        S = -0.03563017932444956,
        B = 0.0294880591967652,
        E = 0.05880281759330635,
        L = 0.31464739902813127,
        A = -0.012050462149060394,
    ),
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
        S = 0.2635317295375031,
        B = -0.004066412945029752,
        E = 0.28913446066670345,
        L = 1.0754815156346873,
        A = -0.005288089123116344,
    ),
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
        S = -0.07112221800144729,
        B = 0.1829125677154705,
        E = 0.24181788049774205,
        L = 0.4835806017147018,
        A = -0.03734047719000979,
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
        S = 0.10013374254656329,
        B = 0.022497151672851778,
        E = 0.07620062665791044,
        L = 0.6218013069815858,
        A = -0.003559024471743491,
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
        S = -0.03091461724910122,
        B = 0.08187031288492888,
        E = 0.11967569463706561,
        L = 0.5144268029777509,
        A = -0.06109265680534165,
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
        S = 0.34783291843564934,
        B = 0.16597724177465573,
        E = 0.04123723863917814,
        L = 1.0298272053028052,
        A = 0.027760631590819946,
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
        S = 0.1896458668028035,
        B = 0.0778491674392543,
        E = -0.020726829732987482,
        L = 0.4823020343045072,
        A = 0.10882569168673216,
    ),
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
        S = 0.07399695888248674,
        B = 0.09622182350297075,
        E = 0.027136668776722522,
        L = 0.4541477022293843,
        A = 0.03767884305396266,
    ),
)

tree(
"""
L1: R
	L2: C
		L3: CJ2_singlet
		L3: Cbf
			L4: Cbf-CbCbCbf
			L4: Cbf-CbCbfCbf
			L4: Cbf-CbfCbfCbf
		L3: Cb
			L4: Cb-H
			L4: Cb-O2s
			L4: Cb-S
				L5: Cb-S2s
				L5: Cb-S6dd
			L4: Cb-N3s
			L4: Cb-C
				L5: Cb-Cs
				L5: Cb-Cds
					L6: Cb-(Cds-O2d)
						L7: Cb-(Cds-O2dOs)
					L6: Cb-(Cds-Cd)
						L7: Cb-(Cds-Cds)
				L5: Cb-Ct
					L6: Cb-(CtN3t)
				L5: Cb-Cb
		L3: Ct
			L4: Ct-N3tN3s
			L4: Ct-CtH
			L4: Ct-N3tC
				L5: Ct-N3tCs
				L5: Ct-N3tCd
			L4: Ct-CtC
				L5: Ct-CtCs
				L5: Ct-CtCds
					L6: Ct-Ct(Cds-Cd)
						L7: Ct-Ct(Cds-Cds)
				L5: Ct-CtCb
		L3: Cdd
			L4: Cdd-CdOd
				L5: Cdd-CdsOd
			L4: Cdd-CdCd
				L5: Cdd-CdsCds
		L3: Cds
			L4: Cds-OdN3sC
				L5: Crds-OdN3rsCr
				L5: Cds-OdN3sCs
			L4: Cds-OdN3sH
			L4: Cds-OdN3sN
				L5: Cds-OdN3sN3s
					L6: Crds-OdN3rsN3rs
			L4: Cd-N3dCsCs
			L4: Cd-N3dCsH
			L4: Cds-OdOsH
			L4: Cds-OdOsOs
			L4: CO-CsSs
			L4: Cds-OdCH
				L5: Cds-OdCsH
				L5: Cds-OdCdsH
					L6: Cds-O2d(Cds-O2d)H
					L6: Cds-O2d(Cds-Cd)H
						L7: Cds-O2d(Cds-Cds)H
			L4: Cds-Od(OsH)
			L4: Cds-OdCOs
				L5: Cds-OdCsOs
				L5: Cds-OdCdsOs
					L6: Cds-O2d(Cds-O2d)O2s
					L6: Cds-O2d(Cds-Cd)O2s
						L7: Cds-O2d(Cds-Cds)O2s
				L5: Cds-OdCbOs
			L4: Cds-OdCC
				L5: Cds-OdCsCs
				L5: Cds-OdCdsCs
					L6: Cds-O2d(Cds-O2d)Cs
					L6: Cds-O2d(Cds-Cd)Cs
						L7: Cds-O2d(Cds-Cds)Cs
				L5: Cds-OdCdsCds
					L6: Cds-O2d(Cds-Cd)(Cds-Cd)
						L7: Cds-O2d(Cds-Cds)(Cds-Cds)
				L5: Cds-OdCbCb
			L4: Cds-CdHH
				L5: Cds-CdsHH
				L5: Cds-CddHH
					L6: Cds-(Cdd-O2d)HH
			L4: Cds-CdOsH
				L5: Cds-CdsOsH
			L4: Cds-CdSH
				L5: Cds-CdsSH
					L6: Cds-CdsS2H
			L4: Cds-CdCH
				L5: Cds-CdsCsH
				L5: Cds-CdsCdsH
					L6: Cd-Cd(CO)H
					L6: Cds-Cds(Cds-Cd)H
						L7: Cds-Cds(Cds-Cds)H
				L5: Cds-CdsCtH
					L6: Cds-CdsH(CtN3t)
				L5: Cds-CdsCbH
					L6: Cds-(Cds-Os)CbH
			L4: Cds-CdCO
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-O2d)O2s
					L6: Cds-Cds(Cds-Cd)O2s
						L7: Cds-Cds(Cds-Cds)O2s
				L5: Cds-CdsCbOs
				L5: Cd-CdCsOs
					L6: Cds-CdsCsOs
			L4: Cds-CdCS
				L5: Cds-CdsCsSs
					L6: Cds-CdsCsS2
			L4: Cds-CdCC
				L5: Cds-CdsCsCs
				L5: Cds-CdsCdsCs
					L6: Cd-CdCs(CO)
					L6: Cds-Cds(Cds-Cd)Cs
						L7: Cds-Cds(Cds-Cds)Cs
				L5: Cds-CdsCdsCds
					L6: Cds-Cds(Cds-O2d)(Cds-Cd)
						L7: Cds-Cds(Cds-O2d)(Cds-Cds)
					L6: Cds-Cds(Cds-Cd)(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)(Cds-Cds)
				L5: Cds-CdsCtCs
					L6: Cd-CdCs(CtN3t)
				L5: Cds-CdsCtCds
					L6: Cds-CdsCt(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)Ct
				L5: Cds-CdsCbCs
				L5: Cds-CdsCbCds
					L6: Cds-Cds(Cds-Cd)Cb
						L7: Cds-Cds(Cds-Cds)Cb
				L5: Cds-CdsCbCb
			L4: Cds-CNH
				L5: Cd-CdHN3s
			L4: Cds-CCN
				L5: Cd-CdCsN3s
		L3: Cs
			L4: Cs-NHHH
				L5: Cs-N3sHHH
				L5: Cs-N3dHHH
					L6: Cs-(N3dCd)HHH
			L4: Cs-NCsHH
				L5: Cs-N3sCsHH
				L5: Cs-N3dCHH
					L6: Cs-(N3dN3d)CsHH
					L6: Cs-(N3dCd)CsHH
				L5: Cs-N5dcCsHH
			L4: Crs-NCCH
				L5: Crs-CrN3rsCH
				L5: Crs-CrCrN3sH
			L4: Cs-NCsCsH
				L5: Cs-N3sCsCsH
			L4: Cs-NCsCsCs
				L5: Cs-N3sCsCsCs
				L5: Cs-N5dcCsCsCs
			L4: Cs-CHHH
				L5: Cs-CsHHH
				L5: Cs-CdsHHH
					L6: Cs-(Cds-O2d)HHH
					L6: Cs-(Cds-Cd)HHH
						L7: Cs-(Cds-Cds)HHH
					L6: Cs-(CdN3d)HHH
				L5: Cs-CtHHH
				L5: Cs-CbHHH
				L5: Cs-C=SHHH
			L4: Cs-OsHHH
			L4: Cs-SsHHH
				L5: Cs-S2sHHH
				L5: Cs-S4HHH
				L5: Cs-S6HHH
			L4: Cs-SsSsHH
			L4: Cs-CCHH
				L5: Cs-CsCsHH
				L5: Cs-CdsCsHH
					L6: Cs-(Cds-O2d)CsHH
					L6: Cs-(Cds-Cd)CsHH
						L7: Cs-(Cds-Cds)CsHH
					L6: Cs-(CdN3d)CsHH
				L5: Cs-CdsCdsHH
					L6: Cs-(Cds-O2d)(Cds-O2d)HH
					L6: Cs-(Cds-O2d)(Cds-Cd)HH
						L7: Cs-(Cds-O2d)(Cds-Cds)HH
					L6: Cs-(Cds-Cd)(Cds-Cd)HH
						L7: Cs-(Cds-Cds)(Cds-Cds)HH
				L5: Cs-CtCsHH
					L6: Cs-(CtN3t)CsHH
				L5: Cs-CtCdsHH
					L6: Cs-(Cds-O2d)CtHH
					L6: Cs-(Cds-Cd)CtHH
						L7: Cs-(Cds-Cds)CtHH
				L5: Cs-CtCtHH
				L5: Cs-CbCsHH
				L5: Cs-CbCdsHH
					L6: Cs-(Cds-O2d)CbHH
					L6: Cs-(Cds-Cd)CbHH
						L7: Cs-(Cds-Cds)CbHH
				L5: Cs-CbCtHH
				L5: Cs-CbCbHH
			L4: Cs-CCCH
				L5: Cs-CsCsCsH
				L5: Cs-CdsCsCsH
					L6: Cs-(Cds-O2d)CsCsH
					L6: Cs-(Cds-Cd)CsCsH
						L7: Cs-(Cds-Cds)CsCsH
					L6: Cs-(CdN3d)CsCsH
				L5: Cs-CtCsCsH
					L6: Cs-(CtN3t)CsCsH
				L5: Cs-CbCsCsH
				L5: Cs-CdsCdsCsH
					L6: Cs-(Cds-Cd)(Cds-Cd)CsH
						L7: Cs-(Cds-Cds)(Cds-Cds)CsH
				L5: Cs-CbCdsCsH
					L6: Cs-(Cds-Cd)CbCsH
						L7: Cs-(Cds-Cds)CbCsH
				L5: Cs-CbCbCsH
				L5: Cs-CbCbCbH
			L4: Crs-CCHH
				L5: Crs-CrCrHH
			L4: Cs-CCCC
				L5: Cs-CsCsCsCs
				L5: Cs-CdsCsCsCs
					L6: Cs-(Cds-O2d)CsCsCs
					L6: Cs-(Cds-Cd)CsCsCs
						L7: Cs-(Cds-Cds)CsCsCs
				L5: Cs-CtCsCsCs
					L6: Cs-(CtN3t)CsCsCs
				L5: Cs-CbCsCsCs
				L5: Cs-CdsCdsCsCs
					L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
				L5: Cs-CbCtCsCs
			L4: Crs-OsOsHH
				L5: Crs-OrsOrsHH
			L4: Cs-CCCOs
				L5: Cs-CsCsCsOs
				L5: Cs-CdsCsCsOs
					L6: Cs-(Cds-O2d)CsCsOs
					L6: Cs-(Cds-Cd)CsCsOs
						L7: Cs-(Cds-Cds)CsCsOs
				L5: Cs-CbCsCsOs
			L4: Cs-CCOsOs
				L5: Cs-CsCsOsOs
			L4: Cs-COsOsH
				L5: Cs-CsOsOsH
			L4: Crs-CCOsOs
				L5: Crs-OrsOrsCC
				L5: Crs-CrOrsOsC
			L4: Crs-COsOsH
				L5: Crs-OrsOrsCH
				L5: Crs-CrOrsOsH
			L4: Cs-CCOsH
				L5: Cs-CsCsOsH
				L5: Cs-CdsCsOsH
					L6: Cs-(Cds-O2d)CsOsH
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
				L5: Cs-CbCsOsH
			L4: Cs-COsHH
				L5: Cs-CsOsHH
				L5: Cs-CdsOsHH
					L6: Cs-(Cds-O2d)OsHH
					L6: Cs-(Cds-Cd)OsHH
						L7: Cs-(Cds-Cds)OsHH
				L5: Cs-CtOsHH
			L4: Cs-CCCS
				L5: Cs-CsCsCsS
					L6: Cs-CsCsCsS2
			L4: Cs-CCSS
				L5: Cs-CsCsSS
			L4: Crs-CSHH
				L5: Crs-CrSrHH
			L4: Cs-CCSH
				L5: Cs-CsCsSH
					L6: Cs-CsCsS2H
			L4: Cs-CSHH
				L5: Cs-CsSHH
					L6: Cs-CsS2HH
					L6: Cs-CsS4HH
					L6: Cs-CsS6HH
				L5: Cs-CdsSsHH
				L5: Cs-CtSsHH
				L5: Cs-CbSsHH
	L2: O
		L3: O2d
			L4: O2d-Cd
			L4: O2d-N3d
			L4: O2d-N5dc
			L4: O2d-Sd
		L3: O2s
			L4: O2s-N
				L5: O2s-CN
					L6: O2s-CsN3s
					L6: O2s-CsN3d
						L7: O2s-Cs(N3dOd)
			L4: O2s-OsH
			L4: O2s-CH
				L5: O2s-CdsH
					L6: O2s-(Cds-O2d)H
					L6: O2s-(Cds-Cd)H
				L5: O2s-CsH
				L5: O2s-CbH
			L4: O2s-OsC
				L5: O2s-OsCds
					L6: O2s-O2s(Cds-O2d)
				L5: O2s-OsCs
			L4: O2s-CC
				L5: O2s-CdsCds
					L6: O2s-(Cds-O2d)(Cds-O2d)
					L6: O2s-(Cds-O2d)(Cds-Cd)
					L6: O2s-(Cds-Cd)(Cds-Cd)
				L5: O2s-CdsCs
					L6: O2s-Cs(Cds-O2d)
					L6: O2s-Cs(Cds-Cd)
				L5: O2s-CsCs
				L5: O2s-CsCb
				L5: O2s-CbCb
			L4: O2s-CS
				L5: O2s-CS6
			L4: O2s-SH
				L5: O2s-S_DeH
		L3: Oc
			L4: Oc-N5dc
	L2: S
		L3: S2d
			L4: S2d-C
		L3: S2s
			L4: S2s-CH
				L5: S2s-CsH
				L5: S2s-CdH
				L5: S2s-CtH
				L5: S2s-CbH
			L4: S2s-SS
				L5: S2s-SsSs
			L4: S2s-SC
				L5: S2s-S2sC
					L6: S2s-S2sCs
					L6: S2s-S2sCd
			L4: S2s-CC
				L5: S2s-CsCs
				L5: S2s-CsCd
				L5: S2s-Cs(C=O)
				L5: S2s-CsCt
				L5: S2s-CsCb
				L5: S2s-CdCd
				L5: S2s-CdCb
				L5: S2s-CbCb
				L5: S2s-(C=S2d)Cs
		L3: S4dd
		L3: S4d
			L4: S4d-Od
				L5: S4d-OdCC
					L6: S4d-OdCsCs
		L3: S6dd
			L4: S6dd-OdOd
				L5: S6dd-OdOdCC
					L6: S6dd-OdOdCsCs
					L6: S6rdd-CCOdOd
				L5: S6dd-OdOdCO
					L6: S6dd-OdOdCsOs
				L5: S6dd-OdOdN3sC
				L5: S6dd-OdOdOO
	L2: N
		L3: N1dc
		L3: N3s
			L4: N3s-CHH
				L5: N3s-CsHH
				L5: N3s-CbHH
				L5: N3s-(CO)HH
				L5: N3s-CdHH
			L4: N3s-CCH
				L5: N3s-CsCsH
				L5: N3s-CbCsH
				L5: N3s-CbCbH
				L5: N3s-(CO)CsH
				L5: N3s-(CO)CbH
				L5: N3s-(CO)(CO)H
				L5: N3s-(CdCd)CsH
			L4: N3s-CCC
				L5: N3s-CsCsCs
				L5: N3s-CbCsCs
				L5: N3s-(CO)CsCs
				L5: N3s-(CdCd)CsCs
				L5: N3rs-CCC
					L6: N3rs-CrCrC
						L7: N3rs-CrCrCr
			L4: N3s-N3sHH
			L4: N3s-NCH
				L5: N3s-N3sCsH
				L5: N3s-N3sCbH
			L4: N3s-NCC
				L5: N3s-NCsCs
					L6: N3s-CsCs(N3dOd)
				L5: N3s-NCdCs
				L5: N3s-NrCrC
		L3: N3d
			L4: N3d-CdH
			L4: N3d-N3dN3s
			L4: N3d-OdOs
			L4: N3d-OdN3s
			L4: N3d-CsR
				L5: N3d-N3dCs
			L4: N3d-CbR
		L3: N3t
		L3: N5dc
			L4: N5dc-OdOsC
"""
)

