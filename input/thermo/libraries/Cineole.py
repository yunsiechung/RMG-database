#!/usr/bin/env python
# encoding: utf-8

name = "cineole"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Cineole",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
9  C u0 p0 c0 {3,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,S} {24,S} {25,S} {26,S}
11 C u0 p0 c0 {1,S} {27,S} {28,S} {29,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([48.2171,64.0191,78.0525,89.8684,108.382,122.006,141.903],'cal/(mol*K)'),
        H298 = (-82.5066,'kcal/mol'),
        S298 = (99.9589,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "R4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
10 C u1 p0 c0 {3,S} {6,S} {28,S}
11 O u0 p2 c0 {1,S} {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.205,64.3926,77.377,88.47,106.178,119.052,137.525],'cal/(mol*K)'),
        H298 = (-35.6969,'kcal/mol'),
        S298 = (102.558,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "R2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {9,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
4  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
9  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
10 C u1 p0 c0 {3,S} {6,S} {28,S}
11 O u0 p2 c0 {1,S} {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.4169,64.3427,77.3028,88.4804,106.268,119.144,137.515],'cal/(mol*K)'),
        H298 = (-36.843,'kcal/mol'),
        S298 = (102.491,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
2  C u0 p0 c0 {8,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
9  C u0 p0 c0 {2,S} {23,S} {24,S} {25,S}
10 C u1 p0 c0 {2,S} {5,S} {6,S}
11 O u0 p2 c0 {1,S} {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([48.1901,63.5372,76.7894,87.9282,105.696,118.666,137.37],'cal/(mol*K)'),
        H298 = (-30.8595,'kcal/mol'),
        S298 = (100.491,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {12,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
8  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {3,S} {21,S} {22,S} {23,S}
10 C u1 p0 c0 {3,S} {27,S} {28,S}
11 O u0 p2 c0 {1,S} {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.3467,64.5597,77.7307,88.7598,106.291,119.103,137.606],'cal/(mol*K)'),
        H298 = (-31.608,'kcal/mol'),
        S298 = (104.563,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {12,S}
3  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
8  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
9  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
10 C u1 p0 c0 {3,S} {27,S} {28,S}
11 O u0 p2 c0 {1,S} {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.2188,64.4313,77.6729,88.7409,106.239,119.047,137.581],'cal/(mol*K)'),
        H298 = (-30.7633,'kcal/mol'),
        S298 = (103.895,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R4c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {10,S} {15,S} {16,S} {17,S}
4  O u0 p2 c0 {9,S} {10,S}
5  C u0 p0 c0 {7,S} {9,D} {18,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {19,S}
7  C u0 p0 c0 {5,S} {6,S} {20,S} {21,S}
8  C u0 p0 c0 {10,S} {22,S} {23,S} {24,S}
9  C u0 p0 c0 {1,S} {4,S} {5,D}
10 C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.2539,54.7845,66.2833,75.9965,91.3278,102.295,117.694],'cal/(mol*K)'),
        H298 = (3.45925,'kcal/mol'),
        S298 = (91.5012,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R4a",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {10,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,D} {11,S}
9  C u0 p0 c0 {3,S} {8,D} {26,S}
10 C u1 p0 c0 {4,S} {27,S} {28,S}
11 O u0 p2 c0 {1,S} {8,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([52.0677,66.1759,78.8331,89.8104,106.829,119.098,137.624],'cal/(mol*K)'),
        H298 = (-20.4648,'kcal/mol'),
        S298 = (111.128,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R4b",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {9,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {8,S} {10,D}
10 C u0 p0 c0 {5,S} {9,D} {28,S}
11 O u1 p2 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([50.0675,64.5736,77.6332,88.8775,106.159,118.761,137.547],'cal/(mol*K)'),
        H298 = (-17.4258,'kcal/mol'),
        S298 = (108.695,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R2d",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
9  C u0 p0 c0 {2,S} {10,D} {27,S}
10 C u0 p0 c0 {3,S} {9,D} {26,S}
11 O u0 p2 c0 {1,S} {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([47.1683,62.0622,74.6021,85.3633,102.479,114.863,132.547],'cal/(mol*K)'),
        H298 = (-52.2043,'kcal/mol'),
        S298 = (97.6728,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R2a",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {4,S} {7,S} {11,S}
9  C u0 p0 c0 {2,S} {10,D} {26,S}
10 C u0 p0 c0 {9,D} {27,S} {28,S}
11 O u0 p2 c0 {1,S} {8,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([50.9621,65.011,77.7607,88.9351,106.379,118.736,137.487],'cal/(mol*K)'),
        H298 = (-15.4441,'kcal/mol'),
        S298 = (109.389,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R2b",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {6,S} {7,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {9,D} {26,S}
9  C u0 p0 c0 {3,S} {8,D} {25,S}
10 C u1 p0 c0 {4,S} {27,S} {28,S}
11 O u0 p2 c0 {1,S} {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([51.0725,65.2444,77.5613,88.2163,105.258,117.691,135.69],'cal/(mol*K)'),
        H298 = (-15.1904,'kcal/mol'),
        S298 = (105.788,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R2c",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {8,S} {24,S} {25,S} {26,S}
8  C u1 p0 c0 {6,S} {7,S} {11,S}
9  C u0 p0 c0 {3,S} {10,D} {27,S}
10 C u0 p0 c0 {4,S} {9,D} {28,S}
11 O u0 p2 c0 {1,S} {8,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([50.8597,64.754,77.4686,88.7409,106.596,118.972,137.579],'cal/(mol*K)'),
        H298 = (-17.0066,'kcal/mol'),
        S298 = (112.263,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R2e",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {2,S} {5,S} {10,D}
10 C u0 p0 c0 {4,S} {9,D} {27,S}
11 O u0 p2 c0 {1,S} {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([47.6198,62.5532,75.0535,85.7632,102.793,115.112,132.697],'cal/(mol*K)'),
        H298 = (-5.09509,'kcal/mol'),
        S298 = (97.7364,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation by Jorge Aguilera Iparraguirre""",
    longDesc = 
u"""

""",
)

