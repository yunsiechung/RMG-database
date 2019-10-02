#!/usr/bin/env python
# encoding: utf-8

name = "yunsie_thermo_large"
shortDesc = u""
longDesc = u"""
ARC v1.1.0
ARC project yunsie_thermo_large

Levels of theory used:

Conformers:       b3lyp/6-31g(d,p) empiricaldispersion=gd3bj
TS guesses:       b3lyp/6-31g(d,p) empiricaldispersion=gd3bj
Optimization:     bmk/6-311g(2d,d,p) (using a fine grid)
Frequencies:      bmk/6-311g(2d,d,p)
Single point:     bmk/6-311g(2d,d,p)
Rotor scans:      wb97xd/def2tzvp
NOT using bond additivity corrections for thermo

Using the following ESS settings: {'onedmin': ['local'], 'molpro': ['local'], 'qchem': ['local'], 'gaussian': ['local']}

Considered the following species and TSs:
Species reactant (run time: 2:33:50)
Species product (Failed!) (run time: None)

Overall time since project initiation: 07:57:47
"""
entry(
    index = 0,
    label = "reactant",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {7,S} {11,S} {39,S} {40,S}
3  C u0 p0 c0 {1,S} {11,D} {12,S}
4  C u0 p0 c0 {1,S} {14,B} {15,B}
5  C u0 p0 c0 {1,S} {16,B} {17,B}
6  C u0 p0 c0 {1,S} {18,B} {19,B}
7  C u0 p0 c0 {2,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  C u0 p0 c0 {8,S} {20,B} {21,B}
10 C u0 p0 c0 {8,S} {22,B} {23,B}
11 C u0 p0 c0 {2,S} {3,D} {41,S}
12 C u0 p0 c0 {3,S} {13,D} {42,S}
13 C u0 p0 c0 {7,S} {12,D} {43,S}
14 C u0 p0 c0 {4,B} {30,B} {54,S}
15 C u0 p0 c0 {4,B} {32,B} {58,S}
16 C u0 p0 c0 {5,B} {33,B} {59,S}
17 C u0 p0 c0 {5,B} {35,B} {63,S}
18 C u0 p0 c0 {6,B} {36,B} {64,S}
19 C u0 p0 c0 {6,B} {38,B} {68,S}
20 C u0 p0 c0 {9,B} {24,B} {44,S}
21 C u0 p0 c0 {9,B} {26,B} {48,S}
22 C u0 p0 c0 {10,B} {27,B} {49,S}
23 C u0 p0 c0 {10,B} {29,B} {53,S}
24 C u0 p0 c0 {20,B} {25,B} {45,S}
25 C u0 p0 c0 {24,B} {26,B} {46,S}
26 C u0 p0 c0 {21,B} {25,B} {47,S}
27 C u0 p0 c0 {22,B} {28,B} {50,S}
28 C u0 p0 c0 {27,B} {29,B} {51,S}
29 C u0 p0 c0 {23,B} {28,B} {52,S}
30 C u0 p0 c0 {14,B} {31,B} {55,S}
31 C u0 p0 c0 {30,B} {32,B} {56,S}
32 C u0 p0 c0 {15,B} {31,B} {57,S}
33 C u0 p0 c0 {16,B} {34,B} {60,S}
34 C u0 p0 c0 {33,B} {35,B} {61,S}
35 C u0 p0 c0 {17,B} {34,B} {62,S}
36 C u0 p0 c0 {18,B} {37,B} {65,S}
37 C u0 p0 c0 {36,B} {38,B} {66,S}
38 C u0 p0 c0 {19,B} {37,B} {67,S}
39 H u0 p0 c0 {2,S}
40 H u0 p0 c0 {2,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {12,S}
43 H u0 p0 c0 {13,S}
44 H u0 p0 c0 {20,S}
45 H u0 p0 c0 {24,S}
46 H u0 p0 c0 {25,S}
47 H u0 p0 c0 {26,S}
48 H u0 p0 c0 {21,S}
49 H u0 p0 c0 {22,S}
50 H u0 p0 c0 {27,S}
51 H u0 p0 c0 {28,S}
52 H u0 p0 c0 {29,S}
53 H u0 p0 c0 {23,S}
54 H u0 p0 c0 {14,S}
55 H u0 p0 c0 {30,S}
56 H u0 p0 c0 {31,S}
57 H u0 p0 c0 {32,S}
58 H u0 p0 c0 {15,S}
59 H u0 p0 c0 {16,S}
60 H u0 p0 c0 {33,S}
61 H u0 p0 c0 {34,S}
62 H u0 p0 c0 {35,S}
63 H u0 p0 c0 {17,S}
64 H u0 p0 c0 {18,S}
65 H u0 p0 c0 {36,S}
66 H u0 p0 c0 {37,S}
67 H u0 p0 c0 {38,S}
68 H u0 p0 c0 {19,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[2.93469, 0.187261, 0.000146966, -3.12015e-07, 1.29486e-10, 108658, 24.7386],
                Tmin=(10, 'K'),
                Tmax=(929.244, 'K'),
            ),
            NASAPolynomial(
                coeffs=[21.8207, 0.233201, -0.000132576, 3.58853e-08, -3.75348e-12, 99655, -94.5478],
                Tmin=(929.244, 'K'),
                Tmax=(3000, 'K'),
            ),
        ],
        Tmin=(10, 'K'),
        Tmax=(3000, 'K'),
        E0=(903.799, 'kJ/mol'),
        Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(1679.52, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C=C': 18, 'C-C': 25, 'C-H': 30}

External symmetry: 1, optical isomers: 2

Geometry:
{u'symbols': ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), u'isotopes': (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), u'coords': ((-2.482631, -0.021831, -0.022314), (1.14485, 1.484666, 0.566157), (-0.9672, 0.171323, 0.251516), (-2.727641, -1.003096, -1.202257), (-3.163244, 1.311562, -0.446124), (-3.057957, -0.568415, 1.319288), (1.93012, 0.178958, 0.574771), (3.270031, 0.111973, 0.342464), (4.007046, -1.190429, 0.265026), (4.118231, 1.326598, 0.12835), (-0.310919, 1.33753, 0.169688), (-0.220586, -1.006787, 0.746511), (1.120008, -1.008057, 0.878987), (-1.695013, -1.60914, -1.924949), (-4.050441, -1.241453, -1.618563), (-4.180078, 1.937003, 0.282886), (-2.777993, 1.895539, -1.667991), (-3.727937, -1.790503, 1.442983), (-2.833073, 0.176824, 2.491816), (3.576714, -2.234667, -0.56988), (5.186885, -1.373959, 1.007122), (4.997718, 1.379925, -0.968075), (4.094618, 2.416315, 1.013511), (4.291035, -3.432154, -0.644669), (5.449133, -3.607814, 0.114084), (5.894744, -2.572809, 0.94074), (5.80094, 2.497083, -1.188165), (5.760178, 3.578199, -0.303234), (4.909305, 3.530517, 0.801811), (-1.97379, -2.449692, -3.01051), (-3.288336, -2.694936, -3.395418), (-4.330456, -2.080261, -2.693156), (-4.774849, 3.118819, -0.178363), (-4.366029, 3.696929, -1.375857), (-3.361455, 3.073922, -2.123688), (-4.18132, -2.240376, 2.689548), (-3.971148, -1.480511, 3.836341), (-3.288688, -0.264744, 3.73089), (1.155292, 1.923962, 1.578396), (1.63438, 2.220598, -0.078494), (-0.820211, 2.248769, -0.122616), (-0.783553, -1.90228, 0.989735), (1.623281, -1.909488, 1.21093), (2.683648, -2.097229, -1.170896), (3.944507, -4.224693, -1.300911), (6.004057, -4.538934, 0.056859), (6.796899, -2.698892, 1.531464), (5.543951, -0.568127, 1.641367), (5.043752, 0.536278, -1.650036), (6.463152, 2.523159, -2.048104), (6.391073, 4.445524, -0.470218), (4.881367, 4.358207, 1.50393), (3.448329, 2.380677, 1.884413), (-0.661564, -1.423855, -1.660059), (-1.152362, -2.905127, -3.555227), (-3.503028, -3.345416, -4.237395), (-5.361339, -2.24622, -2.990635), (-4.866618, -0.750415, -1.097077), (-4.534063, 1.510272, 1.212262), (-5.564781, 3.578691, 0.40771), (-4.827322, 4.61291, -1.731296), (-3.039272, 3.501566, -3.068204), (-2.016042, 1.409657, -2.269201), (-3.895055, -2.414553, 0.574516), (-4.695751, -3.194354, 2.754133), (-4.322648, -1.831337, 4.80147), (-3.10303, 0.335586, 4.616291), (-2.287814, 1.113012, 2.42561))}
""",
)


entry(
    index = 1,
    label = "product",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {19,S} {20,S}
2  C u0 p0 c0 {1,D} {3,S} {21,S}
3  C u0 p0 c0 {2,S} {4,D} {22,S}
4  C u0 p0 c0 {3,D} {5,S} {18,S}
5  C u1 p0 c0 {4,S} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {6,D} {8,S} {23,S}
8  C u0 p0 c0 {7,S} {9,D} {24,S}
9  C u0 p0 c0 {8,D} {10,S} {25,S}
10 C u0 p0 c0 {9,S} {11,D} {26,S}
11 C u0 p0 c0 {6,S} {10,D} {27,S}
12 C u0 p0 c0 {5,S} {13,D} {17,S}
13 C u0 p0 c0 {12,D} {14,S} {28,S}
14 C u0 p0 c0 {13,S} {15,D} {29,S}
15 C u0 p0 c0 {14,D} {16,S} {30,S}
16 C u0 p0 c0 {15,S} {17,D} {31,S}
17 C u0 p0 c0 {12,S} {16,D} {32,S}
18 C u0 p0 c0 {4,S} {19,D} {33,S}
19 C u0 p0 c0 {1,S} {18,D} {34,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}
30 H u0 p0 c0 {15,S}
31 H u0 p0 c0 {16,S}
32 H u0 p0 c0 {17,S}
33 H u0 p0 c0 {18,S}
34 H u0 p0 c0 {19,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[3.66847, 0.021459, 0.000512413, -1.09118e-06, 7.21203e-10, 56166.8, 18.6647],
                Tmin=(10, 'K'),
                Tmax=(479.272, 'K'),
            ),
            NASAPolynomial(
                coeffs=[-5.24296, 0.157055, -0.000103574, 3.21786e-08, -3.79558e-12, 56317.9, 47.7676],
                Tmin=(479.272, 'K'),
                Tmax=(3000, 'K'),
            ),
        ],
        Tmin=(10, 'K'),
        Tmax=(3000, 'K'),
        E0=(466.923, 'kJ/mol'),
        Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(831.447, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
""",
)
