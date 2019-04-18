#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Cineole + Cl <=> HCl + R1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-1.1, 'kcal/mol'),
        T0 = (1, 'K'),
    )
)

entry(
    index = 2,
    label = "Cineole + Cl <=> HCl + R2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+15, 'cm^3/(mol*s)'),
        n = -0.33,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "Cineole + Cl <=> HCl + R3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+09, 'cm^3/(mol*s)'),
        n = 1.19,
        Ea = (-1.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "Cineole + Cl <=> HCl + R4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+16, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "Cineole + Cl <=> HCl + R5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.0e+13, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "Cineole + CH3 <=> CH4 + R1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e-4, 'cm^3/(mol*s)'),
        n = 4.898,
        Ea = (7.638, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "Cineole + CH3 <=> CH4 + R2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.517e-3, 'cm^3/(mol*s)'),
        n = 4.623,
        Ea = (5.304, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "Cineole + CH3 <=> CH4 + R3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.588e-4, 'cm^3/(mol*s)'),
        n = 4.913,
        Ea = (7.398, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "Cineole + CH3 <=> CH4 + R4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.26e-4, 'cm^3/(mol*s)'),
        n = 4.661,
        Ea = (5.155, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "Cineole + CH3 <=> CH4 + R5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.914e-3, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (5.401, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "R1 <=> R1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 's^-1'), n=0.080, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "R1 <=> R1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+11, 's^-1'), n=0.446, Ea=(26.0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "R1 + O2 <=> R1OO",
    degeneracy = 1,
     kinetics = Arrhenius(A=(6.865e+16, 'cm^3/(mol*s)'), n=-1.627, Ea=(0.199, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_pri = ROO_pri 6.865e+16 -1.627 0.199 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 14,
    label = "R1a <=> acetone + R1cycC7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Using the kinetic parameters for "R4b <=> acetone + cycC7H11-2" reactions
""",
)

entry(
    index = 15,
    label = "R1cycC7H11 + O2 <=> R1cycC7H11O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 16,
    label = "R1cycC7H11O2 <=> R1cycQOOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> cycQOOH-b
H migration to meta position
""",
)

entry(
    index =17,
    label = "R1cycC7H11O2 <=>  R1cycQOOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22., 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> cycQOOH-a
H migration to ortho position
""",
)

entry(
    index = 18,
    label = "R1cycC7H11O2 <=>  R1cycC7H10_ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> cycRene + OOH
""",
)

entry(
    index = 19,
    label = "R1cycQOOH-2 <=>  R1tricycC7H10O-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-a <=> cycQO-a + OH
""",
)

entry(
    index = 20,
    label = "R1cycQOOH-2 <=>  R1cycC7H10_ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+09, 's^-1'), n=1.36, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-a <=> cycQ + OOH
""",
)

entry(
    index = 21,
    label = "R1cycC7H11 <=> R1C7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycC7H11-2 <=> C7H11-2
""",
)

entry(
    index = 22,
    label = "R2 <=> R2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348e+12, 's^-1'), n=0.323, Ea=(32.163, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "R2 <=> R2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.251e+11, 's^-1'), n=0.596, Ea=(28.921, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "R2 <=> R2c",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.497e+12, 's^-1'), n=0.261, Ea=(26.67, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "R2 + O2 <=> R2OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 26,
    label = "R2OO <=> Q2OOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00595, 's^-1'), n=4.12, Ea=(22.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "Q2OOH-1 <=> R2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.02e+09, 's^-1'), n=1, Ea=(10.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "R2OO <=> Q2OOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e-10, 's^-1'), n=6.47, Ea=(28.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "R2OO <=> R2ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(174, 's^-1'), n=3.23, Ea=(33.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "R2OO <=> Q2OOH-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0572, 's^-1'), n=4, Ea=(21.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "R2c <=> acetone + cycC7H11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.095e+12, 's^-1'), n=0.248, Ea=(13.83, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3
""",
)

entry(
    index = 32,
    label = "cycC7H11-1 <=> C7H11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycC7H11-2 -> C7H11-2
""",
)

entry(
    index = 33,
    label = "cycC7H11-1 + O2 <=> cycC7H11O2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.756e+11, 'cm^3/(mol*s)'), n=0.325, Ea=(-0.417, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_tert = ROO_tert 9.756e+11 0.325 -0.417 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 34,
    label = "cycC7H11O2-1 <=> cycC7H10OOH-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycROO -> cycQOOH-a
""",
)

entry(
    index = 35,
    label = "cycC7H10OOH-1a <=> cycC7H10O-1a + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycQOOH-a -> cycQO-a + OH
""",
)

entry(
    index = 36,
    label = "cycC7H10OOH-1a <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+09, 's^-1'), n=1.36, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycQOOH-a -> cycQ + OOH
""",
)

entry(
    index = 37,
    label = "cycC7H10OOH-1a <=> cycC7H10O-1b + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.15e+06, 's^-1'), n=1.87, Ea=(30.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycQOOH-a -> cycQO-b + OH
""",
)

entry(
    index = 38,
    label = "cycC7H11O2-1 <=> cycC7H10OOH-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycROO -> cycQOOH-b
""",
)

entry(
    index = 39,
    label = "cycC7H10OOH-1b <=> cycC7H10O-1c + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+08, 's^-1'), n=1.65, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycQOOH-b -> cycQO-c + OH
""",
)

entry(
    index = 40,
    label = "cycC7H10OOH-1b <=> cycC7H10OOH-1bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(197000, 's^-1'), n=2.58, Ea=(36.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycCQOOH-b -> QOOH-b
""",
)

entry(
    index = 41,
    label = "cycC7H11O2-1 <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycROO -> cycRene + OOH
""",
)

entry(
    index = 42,
    label = "cycC7H11O2-1 <=> fusedcycC7H11O2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycROO -> fusedcyc-a
""",
)

entry(
    index = 43,
    label = "cycC7H11O2-1 <=> fusedcycC7H11O2-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> fusedcyc-b
""",
)

entry(
    index = 44,
    label = "fusedcycC7H11O2-1 <=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. fusedcyc-a -> cycORO
""",
)

entry(
    index = 45,
    label = "fusedcycC7H11O2-1b <=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from fusedcyc-a <=> cycORO
""",
)

entry(
    index = 46,
    label = "OC7H11O-1 <=> bscisOC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycORO -> bscisORO
""",
)

entry(
    index = 47,
    label = "bscisOC7H11O-1 <=> bscisbscisOC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(3.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. bscisORO -> bscisbscisORO
""",
)

entry(
    index = 48,
    label = "bscisbscisOC7H11O-1 <=> C3H4O + C4H7OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+11, 's^-1'), n=0.67, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. bscisbscisORO-> C3H5OJ + C3H4O
""",
)

entry(
    index = 49,
    label = "bscisOC7H11O-1 <=> bscisbscisOC7H11O-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.36e+12, 's^-1'), n=0.12, Ea=(12.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. bscisORO -> bscisbscisORO-b
""",
)

entry(
    index = 50,
    label = "R3 <=> R3a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=-0.058, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 51,
    label = "R3 <=> R3b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0.310, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 52,
    label = "R3a <=> R3a_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52, 's^-1'), n=3.81, Ea=(7.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, R5a <=> R5a_habs
""",
)

entry(
    index = 53,
    label = "R3a <=> R3a_bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+11, 's^-1'), n=0.75, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, R5a <=> R5a_bscis
""",
)

entry(
    index = 54,
    label = "R3 + O2 <=> R3OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.865e+16, 'cm^3/(mol*s)'), n=-1.627, Ea=(0.199, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_pri = ROO_pri 6.865e+16 -1.627 0.199 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 55,
    label = "R3OO <=> Q3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.90e+06, 's^-1'), n=1.55, Ea=(19.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G
""",
)

entry(
    index = 56,
    label = "Q3OOH <=> R3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.33e+10, 's^-1'), n=0.287, Ea=(16.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G
""",
)

entry(
    index = 57,
    label = "R4 <=> R4a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+11, 's^-1'), n=0.5, Ea=(25.798, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "R4 <=> R4b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+13, 's^-1'), n=0.071, Ea=(19.363, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "R4 + O2 <=> R4OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 60,
    label = "R4b <=> R4b_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.59e+07, 's^-1'), n=1.37, Ea=(3.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "R4b <=> acetone + cycC7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "cycC7H11-2 <=> C7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "cycC7H11-2 + O2 <=> cycC7H11O2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 64,
    label = "cycC7H11O2-2 <=> cycC7H10OOH-2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> cycQOOH-a
""",
)

entry(
    index = 65,
    label = "cycC7H10OOH-2a <=> cycC7H10O-2a + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-a <=> cycQO-a + OH
""",
)

entry(
    index = 66,
    label = "cycC7H10OOH-2a <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+09, 's^-1'), n=1.36, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-a <=> cycQ + OOH
""",
)

entry(
    index = 67,
    label = "cycC7H10OOH-2a <=> cycC7H10O-2b + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.15e+06, 's^-1'), n=1.87, Ea=(30.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-a <=> cycQO-b + OH
""",
)

entry(
    index = 68,
    label = "cycC7H11O2-2 <=> cycC7H10OOH-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> cycQOOH-b
""",
)

entry(
    index = 69,
    label = "cycC7H10OOH-2b <=> cycC7H10O-1c + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+08, 's^-1'), n=1.65, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-b <=> cycQO-c + OH
""",
)

entry(
    index = 70,
    label = "cycC7H10OOH-2b <=> cycC7H10OOH-2bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(197000, 's^-1'), n=2.58, Ea=(36.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycQOOH-b <=> QOOH-b
""",
)

entry(
    index = 71,
    label = "cycC7H11O2-2 <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO + cycRene + OOH
""",
)

entry(
    index = 72,
    label = "cycC7H11O2-2 <=> fusedcycC7H11O2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> fusedcyc-a
""",
)

entry(
    index = 73,
    label = "cycC7H11O2-2 <=> fusedcycC7H11O2-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycROO <=> fusedcyc-b
""",
)

entry(
    index = 74,
    label = "fusedcycC7H11O2-2 <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, fusedcyc-a <=> cycORO
""",
)

entry(
    index = 75,
    label = "fusedcycC7H11O2-2b <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, fusedcyc-a <=> cycORO
""",
)

entry(
    index = 76,
    label = "OC7H11O-2 <=> bscisOC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycORO <=> bscisORO
""",
)

entry(
    index = 77,
    label = "bscisOC7H11O-2 <=> bscisbscisOC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(3.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, bscisORO <=> bscisbscisORO
""",
)

entry(
    index = 78,
    label = "bscisbscisOC7H11O-2 <=> VMK + C3H5OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+11, 's^-1'), n=0.67, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, bscisbscisORO <=> C3H5OJ + C3H4O
""",
)

entry(
    index = 79,
    label = "bscisOC7H11O-2 <=> bscisbscisOC7H11O-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.36e+12, 's^-1'), n=0.12, Ea=(12.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. bscisORO -> bscisbscisORO-b
""",
)

entry(
    index = 80,
    label = "R5 <=> R5a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+12, 's^-1'), n=0.46, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "R5a <=> R5a_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52, 's^-1'), n=3.81, Ea=(7.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "R5a <=> R5a_bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+11, 's^-1'), n=0.75, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "R5 + O2 <=> R5OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.756e+11, 'cm^3/(mol*s)'), n=0.325, Ea=(-0.417, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate rules (doi:10.1021/jp112152n)
O2 + R_tert = ROO_tert 9.756e+11 0.325 -0.417 0.0 0.0 0.0 ! Miyoshi (2011) rate rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 84,
    label = "R3 <=> R3ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 85,
    label = "R4 <=> R4ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 86,
    label = "R5 <=> R5_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 87,
    label = "R4OO-1a <=> CH3 + R4OO-1a_ene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 88,
    label = "R5OO-1a <=> R5OO-1a_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 89,
    label = "R2bfused <=> R2bfused_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 's^-1'), n=0.297, Ea=(30.732, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (7) by Ratkiewicz (2011). Reaction 3: CC.CC -> CH3 + C=CC
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

