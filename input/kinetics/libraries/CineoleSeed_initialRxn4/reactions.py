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
    label = "R1a <=> acetone + R1cycC7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Using the kinetic parameters for "R4b <=> acetone + cycC7H11-2" reactions
""",
)

entry(
    index = 14,
    label = "R1cycC7H11 + O2 <=> R1cycC7H11O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate-rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate-rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 15,
    label = "R1cycC7H11O2 <=> R1cycQOOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.193e+09, 's^-1'), n=0.781, Ea=(25.387, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3 by Oscar Wu
""",
)

entry(
    index = 16,
    label = "R1cycQOOH-1 <=> R1cycQO-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.31e+013, 's^-1'), n=0.248, Ea=(20.44, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Sirjean et al. (2009).
Journal of Physical Chemistry A, 113(25), 6924–6935. https://doi.org/10.1021/jp901492e.
Rxn 4 -> 8 on page 8
""",
)

entry(
    index =17,
    label = "R1cycC7H11O2 <=>  R1cycQOOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+08, 's^-1'), n=1.401, Ea=(31.74, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Sirjean et al. (2009).
Journal of Physical Chemistry A, 113(25), 6924–6935. https://doi.org/10.1021/jp901492e.
Rxn 1 -> 3 on page 8
""",
)

entry(
    index = 18,
    label = "R1cycQOOH-2 <=>  R1tricycC7H10O-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+11, 's^-1'), n=0.564, Ea=(10.25, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From Sirjean et al. (2009).
Journal of Physical Chemistry A, 113(25), 6924–6935. https://doi.org/10.1021/jp901492e.
Rxn 3 -> 7 on page 8
""",
)

entry(
    index = 19,
    label = "R2 + O2 <=> R2OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate-rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate-rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 20,
    label = "R2OO <=> Q2OOH-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00595, 's^-1'), n=4.12, Ea=(22.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "Q2OOH-1 <=> R2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.02e+09, 's^-1'), n=1, Ea=(10.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "R2 <=> R2c",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.497e+12, 's^-1'), n=0.261, Ea=(26.67, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "R2c <=> acetone + cycC7H11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.095e+12, 's^-1'), n=0.248, Ea=(13.83, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 24,
    label = "cycC7H11-1 + O2 <=> cycC7H11O2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.756e+11, 'cm^3/(mol*s)'), n=0.325, Ea=(-0.417, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate-rules (doi:10.1021/jp112152n)
O2 + R_tert = ROO_tert 9.756e+11 0.325 -0.417 0.0 0.0 0.0 ! Miyoshi (2011) rate-rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 25,
    label = "cycC7H11O2-1 <=> cycC7H10OOH-1a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+06, 's^-1'), n=1.63, Ea=(22, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> cycQOOH-a
""",
)

entry(
    index = 26,
    label = "cycC7H10OOH-1a <=> cycC7H10O-1a + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.87e+11, 's^-1'), n=0.59, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycQOOH-a <=> cycQO-a + OH
""",
)

entry(
    index = 27,
    label = "cycC7H11O2-1 <=> fusedcycC7H11O2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> fusedcyc-a
""",
)

entry(
    index = 28,
    label = "fusedcycC7H11O2-1<=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from fusedcyc-a <=> cycORO
""",
)

entry(
    index = 29,
    label = "cycC7H11O2-1 <=> fusedcycC7H11O2-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> fusedcyc-b
""",
)

entry(
    index = 30,
    label = "fusedcycC7H11O2-1b <=> OC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from fusedcyc-a <=> cycORO
""",
)

entry(
    index = 31,
    label = "OC7H11O-1 <=> bscisOC7H11O-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycORO -> bscisORO
""",
)

entry(
    index = 32,
    label = "OC7H11O-1 <=> bscisOC7H11O-1b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycORO -> bscisORO
""",
)

entry(
    index = 33,
    label = "R3 + O2 <=> R3OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.865e+16, 'cm^3/(mol*s)'), n=-1.627, Ea=(0.199, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate-rules (doi:10.1021/jp112152n)
O2 + R_pri = ROO_pri 6.865e+16 -1.627 0.199 0.0 0.0 0.0 ! Miyoshi (2011) rate-rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 34,
    label = "R3OO <=> Q3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.90e+06, 's^-1'), n=1.55, Ea=(19.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G
""",
)

entry(
    index = 35,
    label = "Q3OOH <=> R3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.33e+10, 's^-1'), n=0.287, Ea=(16.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G
""",
)

entry(
    index = 36,
    label = "R3OO <=> Q3OOH-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+09, 's^-1'), n=0.844, Ea=(23.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G(2d,d,p)
Using the rate for: R3OO <=> Q3OOH-2
""",
)

entry(
    index = 37,
    label = "Q3OOH-2 <=> R2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.30e+11, 's^-1'), n=0.235, Ea=(10.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From BMK/6-311G
Using the rate for: Q3OOH-2 <=> R2O + OH
""",
)

entry(
    index = 38,
    label = "R4 <=> R4b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+13, 's^-1'), n=0.071, Ea=(19.363, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 39,
    label = "R4b <=> acetone + cycC7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.22e+11, 's^-1'), n=0.63, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 40,
    label = "cycC7H11-2 + O2 <=> cycC7H11O2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.487e+14, 'cm^3/(mol*s)'), n=-0.816, Ea=(-0.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Peroxy chemistry from Miyoshi (2011) rate-rules (doi:10.1021/jp112152n)
O2 + R_sec = ROO_sec 3.487e+14 -0.816 -0.536 0.0 0.0 0.0 ! Miyoshi (2011) rate-rules
(doi:10.1021/jp112152n)
""",
)

entry(
    index = 41,
    label = "cycC7H11O2-2 <=> fusedcycC7H11O2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+10, 's^-1'), n=0.46, Ea=(19, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> fusedcyc-a
""",
)

entry(
    index = 42,
    label = "fusedcycC7H11O2-2 <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from fusedcyc-a <=> cycORO
""",
)

entry(
    index = 43,
    label = "cycC7H11O2-2 <=> fusedcycC7H11O2-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.40e+11, 's^-1'), n=0.26, Ea=(21.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from cycROO <=> fusedcyc-b
""",
)

entry(
    index = 44,
    label = "fusedcycC7H11O2-2b <=> OC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 's^-1'), n=0.77, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
CBS-QB3, from fusedcyc-a <=> cycORO
""",
)

entry(
    index = 45,
    label = "OC7H11O-2 <=> bscisOC7H11O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3, cycORO <=> bscisORO
""",
)

entry(
    index = 46,
    label = "OC7H11O-2 <=> bscisOC7H11O-2b",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+12, 's^-1'), n=0.58, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From CBS-QB3. cycORO -> bscisORO
""",
)

entry(
    index = 47,
    label = "R5 <=> R5a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+12, 's^-1'), n=0.46, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "R5a <=> R5a_bscis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+11, 's^-1'), n=0.75, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
)

