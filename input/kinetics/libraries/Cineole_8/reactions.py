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
        A = (1.43e+14, 'cm^3/(mol*s)'),
        n = -0.08,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "Cineole + CH3 <=> CH4 + R1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e-10, 'cm^3/(mol*s)'),
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
        A = (1.517e-09, 'cm^3/(mol*s)'),
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
        A = (1.588e-10, 'cm^3/(mol*s)'),
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
        A = (5.26e-10, 'cm^3/(mol*s)'),
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
        A = (3.914e-09, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (5.401, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "R2 <=> R2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348e+12, 's^-1'), n=0.323, Ea=(32.163, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "R2 <=> R2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.251e+11, 's^-1'), n=0.596, Ea=(28.921, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "R2 <=> R2c",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.497e+12, 's^-1'), n=0.261, Ea=(26.67, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "R4 <=> R4a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+11, 's^-1'), n=0.5, Ea=(25.798, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "R4 <=> R4b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+13, 's^-1'), n=0.071, Ea=(19.363, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "R4b <=> R4b_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.59e+07, 's^-1'), n=1.37, Ea=(3.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "R4b <=> acetone + cycC7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "R5 <=> R5a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+12, 's^-1'), n=0.46, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "R5a <=> R5a_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52, 's^-1'), n=3.81, Ea=(7.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "R5a <=> R5a_bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+11, 's^-1'), n=0.75, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "R2OO <=> Q2OOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00595, 's^-1'), n=4.12, Ea=(22.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "Q2OOH-1 <=> R2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.02e+09, 's^-1'), n=1, Ea=(10.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "R2OO <=> Q2OOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e-10, 's^-1'), n=6.47, Ea=(28.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "R2OO <=> R2ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(174, 's^-1'), n=3.23, Ea=(33.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "R2OO <=> Q2OOH-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0572, 's^-1'), n=4, Ea=(21.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "cycC7H11-1 <=> C7H11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "cycC7H11-2 <=> C7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "cycC7H11O2-1 <=> cycC7H10OOH-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "cycC7H10OOH-1a <=> cycC7H10O-1a + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "cycC7H10OOH-1a <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+09, 's^-1'), n=1.36, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "cycC7H10OOH-1a <=> cycC7H10O-1b + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.15e+06, 's^-1'), n=1.87, Ea=(30.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "cycC7H11O2-1 <=> cycC7H10OOH-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "cycC7H10OOH-1b <=> cycC7H10O-1c + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+08, 's^-1'), n=1.65, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "cycC7H10OOH-1b <=> cycC7H10OOH-1bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(197000, 's^-1'), n=2.58, Ea=(36.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "cycC7H11O2-1 <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "cycC7H11O2-1 <=> exoaddcycC7H11O2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "exoaddcycC7H11O2-1 <=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "OC7H11O-1 <=> bscisOC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "bscisOC7H11O-1 <=> bscisbscisOC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(3.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "bscisbscisOC7H11O-1 <=> C3H4O + C4H7OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+11, 's^-1'), n=0.67, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "cycC7H11O2-2 <=> cycC7H10OOH-2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "cycC7H10OOH-2a <=> cycC7H10O-2a + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "cycC7H10OOH-2a <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+09, 's^-1'), n=1.36, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "cycC7H10OOH-2a <=> cycC7H10O-2b + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.15e+06, 's^-1'), n=1.87, Ea=(30.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "cycC7H11O2-2 <=> cycC7H10OOH-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "cycC7H10OOH-2b <=> cycC7H10O-1c + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+08, 's^-1'), n=1.65, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "cycC7H10OOH-2b <=> cycC7H10OOH-2bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(197000, 's^-1'), n=2.58, Ea=(36.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "cycC7H11O2-2 <=> cycC7H10 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "cycC7H11O2-2 <=> exoaddcycC7H11O2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "exoaddcycC7H11O2-2 <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "OC7H11O-2 <=> bscisOC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "bscisOC7H11O-2 <=> bscisbscisOC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(3.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "bscisbscisOC7H11O-2 <=> VMK + C3H5OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+11, 's^-1'), n=0.67, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
The product, VMK, was originally mislabeled as C4H6O. Fixed now.
""",
)

entry(
    index = 54,
    label = "C7H11OO-2 <=> C7H11OOexo-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+11, 's^-1'), n=0.1, Ea=(14.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "C7H11OOexo-2 <=> C7H11O_Oexo-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.02e+11, 's^-1'), n=0.32, Ea=(14.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "C7H11O_Oexo-2 <=> C4H6O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.85e+13, 's^-1'), n=0, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "C7H11OO-2 <=> C7H11OOexo2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.02e+07, 's^-1'), n=1.25, Ea=(26, 'kcal/mol'), T0=(1, 'K')),
)


entry(
    index = 58,
    label = "cycC7H11-1 <=> fusedcycC7H11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.96e+11, 's^-1'), n=0.270, Ea=(16.768, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation for R2 exocyclic
""",
)

entry(
    index = 59,
    label = "cycC7H11-2 <=> fusedcycC7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+12, 's^-1'), n=0.160, Ea=(16.630, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation for R4 exocyclic
""",
)

entry(
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
    label = "R2bfused <=> R2bfused_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 's^-1'), n=0.297, Ea=(30.732, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (7) by Ratkiewicz (2011). Reaction 3: CC.CC -> CH3 + C=CC
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 67,
    label = "cyc5_C7H11-1a <=> cyc5_C6H8-1a_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.090e+12, 's^-1'), n=0.736, Ea=(30.634, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3 calculation of beta-scission of alkyl radical on 5-membered ring
""",
)

entry(
    index = 68,
    label = "cycC7H11-1 <=> cycC7H10-1a_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 20. C7H9-11 <=> C7H8-7 + H
""",
)

entry(
    index = 69,
    label = "cycC7H11-1 <=> cycC7H10-1b_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, 27. C7H9-18 <=> C7H8-10 + H
""",
)

entry(
    index = 70,
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
    index = 71,
    label = "R3a <=> R3a_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.014e+10, 's^-1'), n=1.472, Ea=(14.854, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation for alkoxy radical beta-scission to produce cyclohexanone
""",
)

entry(
    index = 72,
    label = "R3 <=> R3a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=-0.058, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, Table 3
""",
)

entry(
    index = 73,
    label = "R3 <=> R3b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0.310, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, Table 3
""",
)

entry(
    index = 74,
    label = "R3a <=> R3a_habs",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52, 's^-1'), n=3.81, Ea=(7.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
from R5a <=> R5a_habs
""",
)

entry(
    index = 75,
    label = "R3a <=> R3a_bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+11, 's^-1'), n=0.75, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
from R5a <=> R5a_bscis
""",
)

entry(
    index = 76,
    label = "Q3OOH-1 <=> R3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.02e+09, 's^-1'), n=1, Ea=(10.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
from Q2OOH-1 <=> R2O + OH
""",
)

entry(
    index = 77,
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
    index = 78,
    label = "cyc5_C7H11-2a <=> cyc5_C6H8-2a_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.090e+12, 's^-1'), n=0.736, Ea=(30.634, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3 calculation of beta-scission of alkyl radical on 5-membered ring
""",
)

entry(
    index = 79,
    label = "cyc5_C7H11-2b <=> cyc5_C7H10-2b_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.99e+10, 's^-1'), n=1.00, Ea=(32.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 35. C6H9-4 <=> C6H8-2 + H
""",
)

entry(
    index = 80,
    label = "cycC7H11-2a <=> cycC7H10-1a_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 20. C7H9-11 <=> C7H8-7 + H
""",
)

entry(
    index = 81,
    label = "cycC7H11-2 <=> cycC7H10-1b_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, 27. C7H9-18 <=> C7H8-10 + H
""",
)

entry(
    index = 82,
    label = "cycC7H11-2 <=> cycC7H10-1a_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 20. C7H9-11 <=> C7H8-7 + H
""",
)

entry(
    index = 83,
    label = "cycC7H11-2b <=> cycC7H11-2b_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+9, 's^-1'), n=1.23, Ea=(28.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 19. C7H9-10 <=> C7H8-6 + H
""",
)

entry(
    index = 84,
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
    index = 85,
    label = "R5a <=> R5a_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.014e+10, 's^-1'), n=1.472, Ea=(14.854, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation for alkoxy radical beta-scission to produce cyclohexanone
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
    label = "cycC10H17O-5 <=> cycC9H14O-5_ene + CH3",
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
    label = "R5a_habs <=> R5a_habs_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 27. C7H9-18 <=> C7H8-10 + H
""",
)

entry(
    index = 89,
    label = "R4b <=> R4b_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.014e+10, 's^-1'), n=1.472, Ea=(14.854, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation for alkoxy radical beta-scission to produce cyclohexanone
""",
)

entry(
    index = 90,
    label = "R1 <=> R1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 's^-1'), n=0.080, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "R1 <=> R1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+11, 's^-1'), n=0.446, Ea=(26.0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "R1a <=> acetone + R1cycC7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Using the kinetic parameters for "R4b <=> acetone + cycC7H11-2" reactions
""",
)

entry(
    index = 93,
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
    index = 94,
    label = "R1cycC7H11O2 <=> R1cycQOOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib, cycC7H11O2-2 <=> cycC7H10OOH-2b
H migration to meta position
""",
)

entry(
    index = 95,
    label = "R1cycC7H11O2 <=>  R1cycQOOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22., 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib, cycC7H11O2-2 <=> cycC7H10OOH-2a
H migration to ortho position
""",
)

entry(
    index = 96,
    label = "R1cycC7H11O2 <=>  R1cycC7H10_ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.75e+06, 's^-1'), n=1.95, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
cycC7H11O2-2 <=> cycC7H10 + OOH
""",
)

entry(
    index = 97,
    label = "R1cycQOOH-2 <=>  R1tricycC7H10O-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
cycC7H10OOH-2a <=> cycC7H10O-2a + OH
""",
)

entry(
    index = 98,
    label = "R1cycQOOH-2 <=>  R1cycC7H10_ene + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
cycC7H10OOH-2a <=> cycC7H10 + OOH
""",
)

entry(
    index = 99,
    label = "R1cycC7H11 <=> R1C7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+12, 's^-1'), n=0.51, Ea=(29.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
cycC7H11-2 <=> C7H11-2
""",
)

entry(
    index = 100,
    label = "R1cycC7H11_fused <=> R1cycC7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+11, 's^-1'), n=0.446, Ea=(26.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
R1 <=> R1b
""",
)

entry(
    index = 101,
    label = "R1cycC7H11_fused <=> R1cyc5C7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+11, 's^-1'), n=0.446, Ea=(26.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Cineole kinetic lib,
R1 <=> R1b
""",
)

entry(
    index = 102,
    label = "R1cyc5C7H11 <=> R1cyc5C7H11-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.343e+10, 's^-1'), n=0.419, Ea=(28.998, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My ccpvtz calc
""",
)

entry(
    index = 103,
    label = "R1cycC7H11 <=> R1cycC7H10_ene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.01, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 24. C7H9-15 <=> C7H8-9 + H
""",
)

entry(
    index = 104,
    label = "cyc5_C7H11-1b <=> cyc5_C7H11-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.343e+10, 's^-1'), n=0.419, Ea=(28.998, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My ccpvtz calc
""",
)

entry(
    index = 105,
    label = "cycC7H11-2 <=> cycC7H11-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1866, 's^-1'), n=3.273, Ea=(20, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Ea temporarily set to 20 kcal until my ccpvtz calc is done
My ccpvtz calc
""",
)

entry(
    index = 106,
    label = "cyc7-1 <=> cyc7-1_ene + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.090e+12, 's^-1'), n=0.736, Ea=(30.634, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3 calculation of beta-scission of alkyl radical on 5-membered ring.
Since the ring-strain of 5-membered ring and 7-membered ring are similar, this rate is used
""",
)

entry(
    index = 107,
    label = "R5cyc5-1 <=> R5cyc5-1_ene + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.63e-4, 's^-1'), n=2.89, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From RMG training reaction, R_addition_multiplebond, 23. C6H6-3 + CH3 <=> C7H9-14
""",
)

entry(
    index = 109,
    label = "R1b-2 <=> R1b-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.1866, 's^-1'), n=3.273, Ea=(20, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Ea temporarily set to 20 kcal until my ccpvtz calc is done
My ccpvtz calc
""",
)

entry(
    index = 110,
    label = "C7H11-2 + O2 <=> C7H11OO-2",
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
    index = 111,
    label = "cycC7H11O2-2 <=> exoaddcycC7H11O2-2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3 calculation by Aaron
""",
)

entry(
    index = 112,
    label = "exoaddcycC7H11O2-2a <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Same rate as exoaddcycC7H11O2-2 <=> OC7H11O-2
""",
)

entry(
    index = 113,
    label = "bscisOC7H11O-2 <=> bscisbscisOC7H11O-2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Barrier height made arbitrarily larger so that entry 52 rxn becomes the dominant step.
Supported by the paper by Nonhebel (1993)

""",
)

entry(
    index = 114,
    label = "R5bsics_3474 <=> CH3 + R5bsics_7838_ene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 115,
    label = "S_1502 <=> S_1508",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.26e+08, 's^-1'), n=0.96, Ea=(17.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Using cycC7H11O2-2 <=> cycC7H10OOH-2b
""",
)

entry(
    index = 116,
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
    index = 117,
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
    index = 118,
    label = "S_3435 <=> S_3533",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(30.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Instead of forbidding the rxn, I just increased the Ea
""",
)

entry(
    index = 119,
    label = "OC7H11O-2 <=> bscisOC7H11O-2a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Using OC7H11O-2 <=> bscisOC7H11O-2
""",
)

entry(
    index = 120,
    label = "cycR4O2OOH <=> cycR4O2OOH_ene + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 121,
    label = "S_1003 <=> S_10587",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(30.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Instead of forbidding the rxn, I just increased the Ea
""",
)

entry(
    index = 122,
    label = "S_857 <=> S_882",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+10, 's^-1'), n=0.08, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
According to the paper by Vereecken, the five-membered ring formation from peroxy radical
has a barrier height of 30 kcal/mol
Vereecken, L., Peeters, J. J. Phys. Chem. A 2004, 108, 5197-5204
""",
)

entry(
    index = 123,
    label = "S_857 <=> S_892",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+06, 's^-1'), n=1.02, Ea=(17.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
According to the paper by Vereecken, the six-membered ring formation from peroxy radical
has a barrier height of 17.6 kcal/mol
Vereecken, L., Peeters, J. J. Phys. Chem. A 2004, 108, 5197-5204
""",
)

entry(
    index = 124,
    label = "S_1787 <=> S_1881",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Barrier height made arbitrarily larger so that the C-O bond breaking rather than C-C bond breaking
in epoxide becomes more dominant step.
Supported by the paper by Nonhebel (1993)

""",
)

entry(
    index = 125,
    label = "OC7H11O-1 <=> bscisOC7H11O-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "S_2820 <=> S_2884",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Barrier height made arbitrarily larger so that the C-O bond breaking rather than C-C bond breaking
in epoxide becomes more dominant step.
Supported by the paper by Nonhebel (1993)

""",
)

entry(
    index = 127,
    label = "bscisOC7H11O-1 <=> bscisbscisOC7H11O-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+12, 's^-1'), n=0.07, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Barrier height made arbitrarily larger so that the C-O bond breaking rather than C-C bond breaking
in epoxide becomes more dominant step.
Supported by the paper by Nonhebel (1993)

""",
)

entry(
    index = 128,
    label = "exoaddcycC7H11O2-1a <=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "R1b-1 <=> S_203",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+10, 's^-1'), n=0.07, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Instead of forbidding the intra H migration, make the barrier really high

""",
)

entry(
    index = 130,
    label = "Q2OO-1419 <=> Q2OOene_16423 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.610e+12, 's^-1'), n=0.37, Ea=(30.730, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From eqn. (8) by Ratkiewicz (2011). Reaction 3: CC(C)C. -> CH3 + CC=C
Phys. Chem. Chem. Phys., 2011, 13, 15037–15046
""",
)

entry(
    index = 131,
    label = "S_1505 <=> S_6520",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.23e+10, 's^-1'), n=0.07, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Instead of forbidding C-C bond breaking in the three membered ring containing O,
make the barrier really high

""",
)

entry(
    index = 132,
    label = "cycC7H11O2-1 <=> exoaddcycC7H11O2-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3 calculation by Aaron
""",
)

entry(
    index = 133,
    label = "bsicbsicORO-2a <=> bsicbsicORO-2a_ene + CH3CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.014e+10, 's^-1'), n=1.47, Ea=(14.85, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
My CBS-QB3 calculation. matches with the NIST values
""",
)

