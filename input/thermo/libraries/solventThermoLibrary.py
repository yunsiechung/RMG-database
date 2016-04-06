#!/usr/bin/env python
# encoding: utf-8

name = "solventThermoLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "water",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([298,300,335,370,400,450,500],'K'),
        Cpdata = ([18.02,18.01,18.01,18.15,18.34,18.91,20.00],'cal/(mol*K)'),
        H298 = (-68.315,'kcal/mol','+|-',0.0096),
        S298 = (16.718,'cal/(mol*K)','+|-',0.0072),
    ),
    shortDesc = u"""library value for liquid water""",
    longDesc =
u"""
from NIST
""",
)

'''
entry(
    index = 2,
    label = "1-octanol",
    molecule =
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {25,S} {26,S}
9  O u0 p2 c0 {8,S} {27,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([],'K'),
        Cpdata = ([],'cal/(mol*K)'),
        H298 = (-101.96,'kcal/mol','+|-',0.14),
        S298 = ([],'cal/(mol*K)','+|-',0.0072),
    ),
    shortDesc = u"""library value for liquid water""",
    longDesc =
u"""
H298 from NIST, Mosselman and Dekker, 1975
""",
)
'''

'''
entry(
    index = 3,
    label = "benzene",
    molecule =
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([],'K'),
        Cpdata = ([],'cal/(mol*K)'),
        H298 = (11.7,'kcal/mol','+|-',0.22),
        S298 = (41.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""library value for liquid water""",
    longDesc =
u"""
H298 from NIST, Roux, Temprado, et al., 2008
S298 from NIST, Oliver, Eaton, et al., 1948
""",
)
'''