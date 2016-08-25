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
    label = "bscisbscisOC7H11O-2 <=> C4H6O + C3H5OJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+11, 's^-1'), n=0.67, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
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

