# Citation
def cite():
    print(r"""
______      _
| ___ \    | |
| |_/ /___ | |_ ___  _ __
|    // _ \| __/ _ \| '__|
| |\ \ (_) | || (_) | |
\_|_\_\___/ \__\___/|_|   _
|  ___|              | | (_)
| |_ _   _ _ __   ___| |_ _  ___  _ __  ___
|  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
| | | |_| | | | | (__| |_| | (_) | | | \__ \
\_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

""")
    print('Please cite:https://arxiv.org/abs/2404.11247')
    print('Colin M. Hylton-Farrington, R. C. R., Dynamic Local Symmetry Fluctuations of Electron Density in Halide Perovskites. arXiv 2024.')
cite()
# If you use this code in your research or project, please cite the associated paper:
#
# Colin M. Hylton-Farrington, R. C. R., Dynamic Local Symmetry Fluctuations of Electron Density in Halide Perovskites. arXiv 2024.
#
#
# ```bibtex
# @article{hylton-farrington2024,
#    author = {Colin M. Hylton-Farrington, Richard C. Remsing},
#    title = {Dynamic Local Symmetry Fluctuations of Electron Density in Halide Perovskites},
#    journal = {arXiv},
#    DOI = {doi.org/10.48550/arXiv.2404.11247},
#    year = {2024},
#    type = {arXiv}
# }


#Libaries
import numpy as np
from scipy.special import sph_harm
import argparse

# Number of Functions for Oh for a given ell and irrep
symmetry_data = {
0: {
"A1g": 1, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
1: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 1, "T2u": 0
},
2: {
"A1g": 0, "A2g": 0, "Eg": 1, "T1g": 0, "T2g": 1,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
3: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 1, "Eu": 0, "T1u": 1, "T2u": 1
},
4: {
"A1g": 1, "A2g": 0, "Eg": 1, "T1g": 1, "T2g": 1,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
5: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 0, "Eu": 1, "T1u": 2, "T2u": 1
},
6: {
"A1g": 1, "A2g": 1, "Eg": 1, "T1g": 1, "T2g": 2,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
7: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 1, "Eu": 1, "T1u": 2, "T2u": 2
},
8: {
"A1g": 1, "A2g": 0, "Eg": 2, "T1g": 2, "T2g": 2,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
9: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 1, "A2u": 1, "Eu": 1, "T1u": 3, "T2u": 2
},
10: {
"A1g": 1, "A2g": 1, "Eg": 2, "T1g": 2, "T2g": 3,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
11: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 0, "A2u": 1, "Eu": 2, "T1u": 3, "T2u": 3
},
12: {
"A1g": 2, "A2g": 1, "Eg": 2, "T1g": 3, "T2g": 3,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
13: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 1, "A2u": 1, "Eu": 2, "T1u": 4, "T2u": 3
},
14: {
"A1g": 1, "A2g": 1, "Eg": 3, "T1g": 3, "T2g": 4,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
15: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 1, "A2u": 2, "Eu": 2, "T1u": 4, "T2u": 4
},
16: {
"A1g": 2, "A2g": 1, "Eg": 3, "T1g": 4, "T2g": 4,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
},
17: {
"A1g": 0, "A2g": 0, "Eg": 0, "T1g": 0, "T2g": 0,
"A1u": 1, "A2u": 1, "Eu": 3, "T1u": 5, "T2u": 4
},
18: {
"A1g": 2, "A2g": 2, "Eg": 3, "T1g": 4, "T2g": 5,
"A1u": 0, "A2u": 0, "Eu": 0, "T1u": 0, "T2u": 0
}
}

# Coefficients of real spherical harmonics for a given cubic harmonic given by:
# Simon L. Altmann and Peter Herzig. Point-group Theory Tables. 2nd edition, 2011.
Oh_sym = {
'A1g':{
0:[
((0,),((1,),)),
],
4:[
((0,4),((0.763762615826,0.645497224368),)),
],
6:[
((0,4),((0.353553390593,-0.935414346693),)),
],
8:[
((0,4,8),((0.718070330817,0.381881307913,0.581843335157),)),
],
10:[
((0,4,8),((0.411425367878,-0.586301969978,-0.697838926019),)),
],
12:[
((0,4,8,12),((0.695502665943,0.314125566803,0.348449537593,0.544227975850),)),
((4,8,12),((0.558979374200,-0.806267508183,0.193583998482),)),
],
14:[
((0,4,8,12),((0.440096461964,-0.457681828621,-0.491132301422,-0.596348480686),)),
],
16:[
((0,4,8,12,16),((0.681361683315,0.275868022760,0.290489869847,0.327569746984,0.517645425853),)),
((4,8,12,16),((0.637048214634,-0.329990348811,-0.647980748513,0.255728159340),)),
],
18:[
((0,4,8,12,16),((0.457915144210,-0.386455976323,-0.402094634007,-0.437465928526,-0.536571491741),)),
((4,8,12,16),((0.148727527118,-0.637746007755,0.723341669444,-0.218945156413),)),
],
},
'A2g':{
6:[
((2,6),((0.829156197589,-0.559016994375),)),
],
10:[
((2,6,10),((0.829156197589,0.157288217401,-0.576221528581),)),
],
12:[
((2,6,10),((0.210406352883,-0.826797284708,0.521666001065),)),
],
14:[
((2,6,10,14),((0.777543289926,0.248530839384,0.020171788261,-0.577279787560),)),
],
16:[
((2,6,10,14),((0.278048912813,-0.719994393786,-0.280380600702,0.570686948992),)),
],
18:[
((2,6,10,14,18),((0.759120166861,0.265186489844,0.147854721474,-0.058999411988,-0.572774605402),)),
((6,10,14,18),((0.386921004710,-0.782089226470,0.483084960929,-0.072508609678),)),
],
},
'A1u':{
9:[
((-4,-8),((0.841625411530,-0.540061724867),)),
],
13:[
((-4,-8,-12),((0.786441087007,0.228217732294,-0.573957388081),)),
],
15:[
((-4,-8,-12),((0.299739470207,-0.810092587301,0.503891109269),)),
],
17:[
((-4,-8,-12,-16),((0.736753683115,0.350316077517,0.038273277231,-0.577068291019),)),
],
},
'A2u':{
3:[
((-2,),((1,),)),
],
7:[
((-2,-6),((0.735980072194,0.677003200386),)),
],
9:[
((-2,-6),((0.433012701892,-0.901387818866),)),
],
11:[
((-2,-6,-10),((0.665363309278,0.459279326772,0.588518620493),)),
],
13:[
((-2,-6,-10),((0.497389016096,-0.493446636764,-0.713522657898),)),
],
15:[
((-2,-6,-10,-14),((0.634946889183,0.318161585237,0.483018535151,0.512160861739),)),
((-6,-10,-14),((0.648649259562,-0.712102682285,0.268633408111),)),
],
17:[
((-2,-6,-10,-14),((0.524544072862,-0.323629924644,-0.504294706537,-0.604817357934),)),
],
},
'Eg':{
2:[
((0,2),((0.707106781187,0),(0,0.707106781187),)),
],
4:[
((0,2,4),((0.456435464588,0,-0.540061724867),(0,0.707106781187,0),)),
],
6:[
((0,2,4,6),((0.661437827766,0,0.25,0),(0,-0.395284707521,0,-0.586301969978),))
],
8:[
((0,2,4,6,8),((0.492125492126,0,-0.278605397905,0,-0.424489731629),(0,0.460101671793,0,0.536941758120,0,))),
((2,4,6,8),((0,0.591153419673,0,-0.387991796832),(0.536941758120,0,-0.460101671793,0),))
],
10:[
((0,2,4,6,8,10),((0.644487845761,0,0.187140459880,0,0.222741700053,0),(0,-0.314647791600,0,-0.343798977702,0,-0.531788520159),)),
((2,4,6,8,10),((0,-0.541390292004,0,0.454858826147),(0.281748440826,0,-0.607809568257,0,0.226241784000),))
],
12:[
((0,2,4,6,8,10,12),((0.508072849927,0,-0.215003782611,0,-0.238496883249,0,-0.372497770879),(0,0.364873518395,0,0.386893033360,0,0.466026926595,0),)),
((2,4,6,8,10,12),((0,0.498203740666,0,0.239535068790,0,-0.440926279106),(0.587138739062,0,-0.092287083266,0,-0.383081186376),))
],
},
'Eu':{
5:[
((-2,-4),((0.707106781187,0),(0,0.707106781187)))
],
7:[
((-2,-4,-6),((0.478713553878,0,-0.520416499867),(0,0.707106781187,0)))
],
9:[
((-2,-4,-6,-8),((0.637377439199,0,0.306186217848,0),(0,-0.381881307913,0,-0.595119035712)))
],
11:[
((-2,-4,-6,-8,-10),((0.527869144138,0,-0.289453945298,0,-0.370905082492),(0,0.350233566926,0,0.614277175710,0))),
((-4,-6,-8,-10),((0,0.557447453624,0,-0.435031420071),(0.614277175710,0,-0.350233566926,0)))
],
},
'T1g':{
4:[
((-1,-3,-4),((0.935414346693,-0.353553390593,0),(0,0,-1),(0.935414346693,0.353553390593,0)))
],
6:[
((-1,-3,-4,-5),((0.433012701892,0.684653196881,0,-0.586301969978),(0,0,1,0),(0.433012701892,-0.684653196881,0,-0.586301969978)))
],
8:[
((-1,-3,-4,-5,-7),((0.274217637106,0.605153647845,0,0.338020432075,-0.666585281491),(0,0,-1,0,0),(0.274217637106,-0.605153647845,0,0.338020432075,0.666585281491))),
((-1,-3,-5,-7,-8),((0.835608872320,-0.516334738808,0.184877493222,-0.03125,0),(0,0,0,0,-1),(0.835608872320,0.516334738808,0.184877493222,0.03125,0)))
],
},
'T2g':{
2:[
((-1,-2),((1,0),(0,-1),(-1,0)))
],
4:[
((-1,-2,-3),((0.353553390593,0,0.935414346693),(0,1,0),(-0.353553390593,0,0.935414346693)))
],
6:[
((-1,-2,-3,-5),((0.197642353761,0,0.5625,0.802827036167),(0,-1,0,0),(-0.197642353761,0,0.5625,-0.802827036167))),
((-1,-3,-5,-6),((0.879452954967,-0.463512405443,0.108253175473,0),(0,0,0,-1),(-0.879452954967,-0.463512405443,-0.108253175473,0)))
],
8:[
((-1,-2,-3,-5,-7),((0.130728129146,0,0.380814300217,0.590864700037,0.699120541287),(0,1,0,0,0),(-0.130728129146,0,0.380814300217,-0.590864700037,0.699120541287))),
((-1,-3,-5,-6,-7),((0.457681828621,0.471346972781,-0.708831013888,0,0.256744948831),(0,0,0,1,0),(-0.457681828621,0.471346972781,0.708831013888,0,0.256744948831)))
],
},
'T1u':{
1:[
((0,1),((0,1),(1,0),(0,1)))
],
3:[
((0,1,3),((0,0.612372435696,0.790569415042),(-1,0,0),(0,0.612372435696,-0.790569415042)))
],
5:[
((0,1,3,5),((0,0.484122918276,0.522912516584,0.701560760020),(1,0,0,0),(0,0.484122918276,-0.522912516584,0.701560760020))),
((1,3,4,5),((0.572821961869,-0.795495128835,0,0.197642353761),(0,0,1,0),(0.572821961869,0.795495128835,0,0.197642353761)))
],
7:[
((0,1,3,5,7),((0,0.413398642354,0.429616471402,0.474958879799,0.647259849288),(-1,0,0,0,0),(0,0.413398642354,-0.429616471402,0.474958879799,-0.647259849288))),
((1,3,4,5,7),((0.538552748113,-0.103644524699,0,-0.78125,0.298106000443),(0,0,-1,0,0),(0.538552748113,0.103644524699,0,-0.78125,-0.298106000443)))
],
9:[
((0,1,3,5,7,9),((0,0.366854902559,0.375487963772,0.396364090436,0.443148525028,0.609049392176),(1,0,0,0,0,0),(0,0.366854902559,-0.375487963772,0.396364090436,-0.443148525028,0.609049392176))),
((1,3,4,5,7,9),((0.494352875611,0.137996263536,0,-0.392184387438,-0.672329061686,0.361576139544),(0,0,1,0,0,0),(0.494352875611,-0.137996263536,0,-0.392184387438,0.672329061686,0.361576139544))),
((1,3,5,7,8,9),((0.385196657363,-0.752680755907,0.509312687906,-0.159440090875,0,0.016572815184),(0,0,0,0,1,0),(0.385196657363,0.752680755907,0.509312687906,0.159440090875,0,0.016572815184)))
],

},
'T2u':{
3:[
((1,2,3),((0.790569415042,0,-0.612372435696),(0,1,0),(-0.790569415042,0,-0.612372435696)))
],
5:[
((1,2,3,5),((0.661437827766,0,0.306186217848,-0.684653196881),(0,-1,0,0),(-0.661437827766,0,0.306186217848,0.684653196881)))
],
7:[
((1,2,3,5,7),((0.574099158465,0,0.419844651330,0.073287746247,-0.699120541287),(0,1,0,0,0),(-0.574099158465,0,0.419844651330,-0.073287746247,-0.699120541287))),
((1,3,5,6,7),((0.457681828621,-0.792728180873,0.398360899499,0,-0.058463396668),(0,0,0,1,0),(-0.457681828621,-0.792728180873,-0.398360899499,0,-0.058463396668)))
],
9:[
((1,2,3,5,7,9),((0.513014223731,0,0.429616471402,0.251945554634,-0.056336738679,-0.696846972531),(0,-1,0,0,0,0),(-0.513014223731,0,0.429616471402,-0.251945554634,-0.056336738679,0.696846972531))),
((1,3,5,6,7,9),((0.457681828621,-0.298106000443,-0.605153647845,0,0.568329171234,-0.111584819196),(0,0,0,-1,0,0),(-0.457681828621,-0.298106000443,0.605153647845,0,0.568329171234,0.111584819196)))
],
11:[
((1,2,3,5,7,9,11),((0.467650076701,0,0.416551701262,0.310141244521,0.136899991476,-0.135949285588,-0.688750084186),(0,1,0,0,0,0,0),(-0.467650076701,0,0.416551701262,-0.310141244521,0.136899991476,0.135949285588,0.688750084186))),
((1,3,5,6,7,9,11),((0.435529357832,-0.047641839522,-0.522728282943,0,-0.324256986638,0.636036888060,-0.158474160191),(0,0,0,1,0,0,0),(-0.435529357832,-0.047641839522,0.522728282943,0,-0.324256986638,-0.636036888060,-0.158474160191))),
((1,3,5,7,9,10,11),((0.334851305401,-0.706413209675,0.568716664438,-0.249300933011,0.056959635045,0,-0.004580484140),(0,0,0,0,0,1,0),(-0.334851305401,-0.706413209675,-0.568716664438,-0.249300933011,-0.056959635045,0,-0.004580484140)))
]
},
}

# Convert Cartessian Coordinates to Spherical Coordinates
def cart2sph(x, y, z,calc_r = False):
    """
    Converts Cartesian to Spherical Coordinates

    Parameters
    ----------
    x : numpy.ndarray
        array of coordinates taken to be along [1,0,0] axis
    y : numpy.ndarray
        array of coordinates taken to be along [0,1,0] axis
    z : numpy.ndarray
        array of coordinates taken to be along [0,0,1] axis
    calc_r : boolean
        if True will calculate distance numpy.ndarray

    Returns
    -------
    r : numpy.ndarray
        Distance
    phi : numpy.ndarray
        Polar angle
    theta : numpy.ndarray
        Azimuthal angle


    Examples
    --------
    >>> import numpy as np
    # build cartesian coordinates
    ... x = np.array([0,0.5,1,0,0.5,1])
    ... y = np.array([0,0.5,0,1,0.5,0])
    ... z = np.array([0,0,0,1,0.5,1])
    ... r, phi, theta = cart2sph(x,y,z,True)
    ... print(r)
     [[0.        , 0.70710678, 1.        , 1.41421356, 0.8660254 ,
       1.41421356]]
    ... print(phi)
     [[0.        , 1.57079633, 1.57079633, 0.78539816, 0.95531662,
       0.78539816]]
    ... print(theta)
     [[0.        , 0.78539816, 0.        , 1.57079633, 0.78539816,
       0.        ]]


    """
    xy = np.sqrt(x**2 + y**2) # sqrt(x² + y²)

    if calc_r:
        x_2 = x**2
        y_2 = y**2
        z_2 = z**2
        r = np.sqrt(x_2 + y_2 + z_2) # r = sqrt(x² + y² + z²)
    else:
        r = None

    theta = np.arctan2(y, x)

    phi = np.arctan2(xy, z)
    return r, phi,theta

# Determines irrep label and returns coefficients for cubic harmonics
def finding_sym(sym,el,m):
    """
    Finds ith irrep label of symmetry adapted function

    Parameters
    ----------
    sym : str
        Point group in Schoenflies notation
    el : int, 0 >= el
        angular momentum quantum number
    m : int, 0 >= m <= 2*el
        index of symmetry adapted function for given el

    Returns
    -------
    If cubic point group_element
    ---
    m_sym : tuple
        (irrep, ms, coefs)
        irrep : str
            irrep name
        ms : tuple, (int,)
            tuple of real spherical harmonics that tranfsorm into this cubic harmonic. add el to get index of non-cubic symmetry adapted function
        coefs: tuple, (float,)
            tuple of the coeffiecients of the real spherical harmonics that tranfsorm into this cubic harmonic
    num : int, 0 > num
        index of irrep for given el, 0 > num

    If non-cubic point group
    ---
    m_sym : tuple
        (irrep, m_1, m_2, ....)
        irrep : str
            irrep name
        m_1, m_2, ...: int
            degenerate indexes with m_n + el being the index of symmetry adpated function
    num : int, 0 > num
        index of irrep for given el, 0 > num


    Examples
    --------
    >>> import numpy as np
    ... m_sym,num = finding_sym('D4h',3,2)
    ... print(m_sym)
     ('Eu', -1, 1)
    ... print(num)
     2

    ... # S^{3,2}_Z for D4h is the second Eu irrep that transforms in S^{3,2} and S^{3,4}

    ... m_sym,num = finding_sym('Oh',3,4)
    ... r, phi, theta = cart2sph(x,y,z,True)
    ... print(m_sym)
     (('T2u', ((-1, -2, -3), (0.790569415042, 0, -0.612372435696))
    ... print(num)
     1

    ... # S^{3,4}_K for Oh is the first T2u irrep that is a linear combination of non-cubic symmetry adapted functions l,m: 0.790569415042*S^{3,2}_Z + 0*S^{3,1}_Z - 0.612372435696*S^{3,0}_Z


    """
    def first_label(m_el):
        nonlocal el,sym
        if sym == 'C1':
            return 'A'
        elif sym == 'C2':
            if m_el % 2 == 0:
                return 'A'
            elif m_el % 2 == 1:
                return 'B'
        elif sym == 'C3':
            if m_el % 3 == 0:
                return 'A'
            elif m_el % 3 == 1:
                return '1_E'
            elif m_el % 3 == 2:
                return '2_E'
        elif sym == 'C4':
            if m_el % 4 == 0:
                return 'A'
            elif m_el % 4 == 2:
                return 'B'
            elif m_el % 4 == 1:
                return '1_E'
            elif m_el % 4 == 3:
                return '2_E'
        elif sym == 'C6':
            if m_el % 6 == 0:
                return 'A'
            elif m_el % 6 == 3:
                return 'B'
            elif m_el % 6 == 1:
                return '1_E1'
            elif m_el % 6 == 5:
                return '2_E1'
            elif m_el % 6 == 4:
                return '1_E2'
            elif m_el % 6 == 2:
                return '2_E2'
        elif sym == 'Ci':
            if el % 2 == 0:
                return 'Ag'
            if el % 2 == 1:
                return 'Au'
        elif sym == 'Cs':
            if (el % 2 == 0 and m_el % 2 == 0) or (el % 2 == 1 and m_el % 2 == 1):
                return 'A^'
            elif (el % 2 == 1 and m_el % 2 == 0) or (el % 2 == 0 and m_el % 2 == 1):
                return 'A^^'
        elif sym == 'S4':
            if (el % 2 == 0 and m_el % 4 == 0) or (el % 2 == 1 and m_el % 4 == 2):
                return 'A'
            elif (el % 2 == 0 and m_el % 4 == 2) or (el % 2 == 1 and m_el % 4 == 0):
                return 'B'
            elif (el % 2 == 0 and m_el % 4 == 1) or (el % 2 == 1 and m_el % 4 == 3):
                return '1_E'
            elif (el % 2 == 0 and m_el % 4 == 3) or (el % 2 == 1 and m_el % 4 == 1):
                return '2_E'
        elif sym == 'S6':
            if el % 2 == 0 and m_el % 3 == 0:
                return 'Ag'
            elif el % 2 == 0 and m_el % 3 == 1:
                return '1_Eg'
            elif el % 2 == 0 and m_el % 3 == 2:
                return '2_Eg'
            if el % 2 == 1 and m_el % 3 == 0:
                return 'Au'
            elif el % 2 == 1 and m_el % 3 == 1:
                return '1_Eu'
            elif el % 2 == 1 and m_el % 3 == 2:
                return '2_Eu'
        elif sym == 'D2':
            if (el % 2 == 0 and m_el >= 0 and m_el % 2 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 2 == 0):
                return 'A'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 2 == 0) or (el % 2 == 0 and m_el < 0 and m_el % 2 == 0):
                return 'B1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 2 == 1) or (el % 2 == 0 and m_el < 0 and m_el % 2 == 1):
                return 'B2'
            elif (el % 2 == 0 and m_el >= 0 and m_el % 2 == 1) or (el % 2 == 1 and m_el < 0 and m_el % 2 == 1):
                return 'B3'
        elif sym == 'D3':

            if (el % 2 == 0 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el > 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 3) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 0):
                return 'A1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el > 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 0):
                return 'A2'
            elif (el % 2 == 1 and m_el % 3 == 2) or (el % 2 == 0 and  m_el % 3 == 1):
                return 'E',m_el,-m_el
            elif (el % 2 == 1 and m_el % 3 == 1) or (el % 2 == 0 and  m_el % 3 == 2):
                return 'E',-m_el,m_el
        elif sym == 'D4':
            if (el % 2 == 0 and m_el >= 0 and m_el % 4 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 4 == 0):
                return 'A1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 4 == 0) or (el % 2 == 0 and m_el < 0 and m_el % 4 == 0):
                return 'A2'
            elif (el % 2 == 0 and m_el >= 0 and m_el % 4 == 2) or (el % 2 == 1 and m_el < 0 and m_el % 4 == 2):
                return 'B1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 4 == 2) or (el % 2 == 0 and m_el < 0 and m_el % 4 == 2):
                return 'B2'
            elif m_el % 4 == 3:
                return 'E',m_el,-m_el
            elif m_el % 4 == 1:
                return 'E',-m_el,m_el
        elif sym == 'D6':
            if (el % 2 == 0 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 0):
                return 'A1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 0):
                return 'A2'
            elif (el % 2 == 0 and m_el >= 0 and m_el % 6 == 3) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 3):
                return 'B1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 3):
                return 'B2'
            elif m_el % 6 == 5:
                return 'E1',m_el,-m_el
            elif m_el % 6 == 1:
                return 'E1',-m_el,m_el
            elif m_el % 6 == 4:
                return 'E2',m_el,-m_el
            elif m_el % 6 == 2:
                return 'E2',-m_el,m_el
        elif sym == 'D2h':
            if el % 2 == 0 and m_el >= 0 and m_el % 2 == 0:
                return 'Ag'
            elif el % 2 == 0 and m_el < 0 and m_el % 2 == 0:
                return 'B1g'
            elif el % 2 == 0 and m_el < 0 and m_el % 2 == 1:
                return 'B2g'
            elif el % 2 == 0 and m_el >= 0 and m_el % 2 == 1:
                return 'B3g'
            if el % 2 == 1 and m_el < 0 and m_el % 2 == 0:
                return 'Au'
            elif el % 2 == 1 and m_el >= 0 and m_el % 2 == 0:
                return 'B1u'
            elif el % 2 == 1 and m_el >= 0 and m_el % 2 == 1:
                return 'B2u'
            elif el % 2 == 1 and m_el < 0 and m_el % 2 == 1:
                return 'B3u'
        elif sym == 'D3h':
            if (el % 2 == 0 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el > 0 and m_el % 6 == 3):
                return 'A1^'
            if (el % 2 == 1 and m_el < 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 0):
                return 'A2^'
            if (el % 2 == 1 and  m_el % 6 == 5) or (el % 2 == 0  and m_el % 6 == 4):
                return 'E^',m_el,-m_el
            if (el % 2 == 1  and m_el % 6 == 1) or (el % 2 == 0  and m_el % 6 == 2):
                return 'E^',-m_el,m_el
            if (el % 2 == 0 and m_el < 0 and m_el % 6 == 3) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 0):
                return 'A1^^'
            if (el % 2 == 1 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 0 and m_el > 0 and m_el % 6 == 3):
                return 'A2^^'
            if (el % 2 == 1 and  m_el % 6 == 4) or (el % 2 == 0  and m_el % 6 == 5):
                return 'E^^',m_el,-m_el
            if (el % 2 == 1 and m_el % 6 == 2) or (el % 2 == 0 and m_el % 6 == 1):
                return 'E^^',-m_el,m_el
        elif sym == 'D4h':
            if el % 2 == 0 and m_el >= 0 and m_el % 4 == 0:
                return 'A1g'
            elif el % 2 == 0 and m_el < 0 and m_el % 4 == 0:
                return 'A2g'
            elif el % 2 == 0 and m_el >= 0 and m_el % 4 == 2:
                return 'B1g'
            elif el % 2 == 0 and m_el < 0 and m_el % 4 == 2:
                return 'B2g'
            elif el % 2 == 0 and m_el % 4 == 3:
                return 'Eg',m_el,-m_el
            elif el % 2 == 0 and m_el % 4 == 1:
                return 'Eg',-m_el,m_el
            if el % 2 == 1 and m_el < 0 and m_el % 4 == 0:
                return 'A1u'
            elif el % 2 == 1 and m_el >= 0 and m_el % 4 == 0:
                return 'A2u'
            elif el % 2 == 1 and m_el < 0 and m_el % 4 == 2:
                return 'B1u'
            elif el % 2 == 1 and m_el >= 0 and m_el % 4 == 2:
                return 'B2u'
            elif el % 2 == 1 and m_el % 4 == 3:
                return 'Eu',m_el,-m_el
            elif el % 2 == 1 and m_el % 4 == 1:
                return 'Eu',-m_el,m_el
        elif sym == 'D6h':
            if el % 2 == 0 and m_el >= 0 and m_el % 6 == 0:
                return 'A1g'
            elif el % 2 == 0 and m_el < 0 and m_el % 6 == 0:
                return 'A2g'
            elif el % 2 == 0 and m_el >= 0 and m_el % 6 == 3:
                return 'B1g'
            elif el % 2 == 0 and m_el < 0 and m_el % 6 == 3:
                return 'B2g'
            elif el % 2 == 0 and m_el % 6 == 5:
                return 'E1g',m_el,-m_el
            elif el % 2 == 0 and m_el % 6 == 1:
                return 'E1g',-m_el,m_el
            elif el % 2 == 0 and m_el % 6 == 4:
                return 'E2g',m_el,-m_el
            elif el % 2 == 0 and m_el % 6 == 2:
                return 'E2g',-m_el,m_el
            elif el % 2 == 1 and m_el < 0 and m_el % 6 == 0:
                return 'A1u'
            elif el % 2 == 1 and m_el >= 0 and m_el % 6 == 0:
                return 'A2u'
            elif el % 2 == 1 and m_el < 0 and m_el % 6 == 3:
                return 'B1u'
            elif el % 2 == 1 and m_el >= 0 and m_el % 6 == 3:
                return 'B2u'
            elif el % 2 == 1 and m_el % 6 == 5:
                return 'E1u',m_el,-m_el
            elif el % 2 == 1 and m_el % 6 == 1:
                return 'E1u',-m_el,m_el
            elif el % 2 == 1 and m_el % 6 == 4:
                return 'E2u',m_el,-m_el
            elif el % 2 == 1 and m_el % 6 == 2:
                return 'E2u',-m_el,m_el
        elif sym == 'D2d':
            if (el % 2 == 0 and m_el >= 0 and m_el % 4 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 4 == 2):
                return 'A1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 4 == 2) or (el % 2 == 0 and m_el < 0 and m_el % 4 == 0):
                return 'A2'
            elif (el % 2 == 0 and m_el >= 0 and m_el % 4 == 2) or (el % 2 == 1 and m_el < 0 and m_el % 4 == 0):
                return 'B1'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 4 == 0) or (el % 2 == 0 and m_el < 0 and m_el % 4 == 2):
                return 'B2'
            elif m_el % 4 == 3:
                return 'E',m_el,-m_el
            elif m_el % 4 == 1:
                return 'E',-m_el,m_el
        elif sym == 'D3d':
            if (el % 2 == 0 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 3):
                return 'A1g'
            elif (el % 2 == 0 and m_el >= 0 and m_el % 6 == 3) or (el % 2 == 0 and m_el < 0 and m_el % 6 == 0):
                return 'A2g'
            elif el % 2 == 0 and m_el % 3 == 2:
                return 'Eg',m_el,-m_el
            elif el % 2 == 0 and m_el % 3 == 1:
                return 'Eg',-m_el,m_el
            if (el % 2 == 1 and m_el >= 0 and m_el % 6 == 3) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 0):
                return 'A1u'
            elif (el % 2 == 1 and m_el >= 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el < 0 and m_el % 6 == 3):
                return 'A2u'
            elif el % 2 == 1 and m_el % 3 == 2:
                return 'Eu',m_el,-m_el
            elif el % 2 == 1 and m_el % 3 == 1:
                return 'Eu',-m_el,m_el
        elif sym == 'C2v':
            if m_el >= 0 and m_el % 2 == 0:
                return 'A1'
            elif m_el < 0 and m_el % 2 == 0:
                return 'A2'
            elif m_el < 0 and m_el % 2 == 1:
                return 'B1'
            elif m_el >= 0 and m_el % 2 == 1:
                return 'B2'
        elif sym == 'C3v_y':
            if (m_el >= 0 and m_el % 6 == 0) or (m_el < 0 and m_el % 6 == 3):
                return 'A1'
            elif (m_el >= 0 and m_el % 6 == 3) or (m_el < 0 and m_el % 6 == 0):
                return 'A2'
            elif m_el % 6 == 5 or m_el % 6 == 4:
                return 'E',m_el,-m_el
            elif m_el % 6 == 1 or m_el % 6 == 2:
                return 'E',-m_el,m_el
        elif sym == 'C3v':
            if m_el >= 0 and m_el % 3 == 0:
                return 'A1'
            elif m_el < 0 and m_el % 3 == 0:
                return 'A2'
            elif m_el % 3 == 2:
                return 'E',m_el,-m_el
            elif m_el % 3 == 1:
                return 'E',-m_el,m_el
        elif sym == 'C4v':
            if m_el >= 0 and m_el % 4 == 0:
                return 'A1'
            elif m_el < 0 and m_el % 4 == 0:
                return 'A2'
            if m_el >= 0 and m_el % 4 == 2:
                return 'B1'
            elif m_el < 0 and m_el % 4 == 2:
                return 'B2'
            elif m_el % 4 == 3:
                return 'E',m_el,-m_el
            elif m_el % 4 == 1:
                return 'E',-m_el,m_el
        elif sym == 'C6v':
            if m_el >= 0 and m_el % 6 == 0:
                return 'A1'
            elif m_el < 0 and m_el % 6 == 0:
                return 'A2'
            if m_el < 0 and m_el % 6 == 3:
                return 'B1'
            elif m_el >= 0 and m_el % 6 == 3:
                return 'B2'
            elif m_el % 6 == 5:
                return 'E1',m_el,-m_el
            elif m_el % 6 == 1:
                return 'E1',-m_el,m_el
            elif m_el % 6 == 4:
                return 'E2',m_el,-m_el
            elif m_el % 6 == 2:
                return 'E2',-m_el,m_el
        elif sym == 'C2h':
            if el % 2 == 0 and m_el % 2 == 0:
                return 'Ag'
            elif el % 2 == 0 and m_el % 2 == 1:
                return 'Bg'
            if el % 2 == 1 and m_el % 2 == 0:
                return 'Au'
            elif el % 2 == 1 and m_el % 2 == 1:
                return 'Bu'
        elif sym == 'C3h':
            if (el % 2 == 0 and m_el % 6 == 0) or (el % 2 == 1 and m_el % 6 == 3):
                return 'A^'
            elif (el % 2 == 1 and m_el % 6 == 1) or (el % 2 == 0 and m_el % 6 == 4):
                return '1_E^'
            elif (el % 2 == 1 and m_el % 6 == 5) or (el % 2 == 0 and m_el % 6 == 2):
                return '2_E^'
            elif (el % 2 == 1 and m_el % 6 == 0) or (el % 2 == 0 and m_el % 6 == 3):
                return 'A^^'
            elif (el % 2 == 0 and m_el % 6 == 1) or (el % 2 == 1 and m_el % 6 == 4):
                return '1_E^^'
            elif (el % 2 == 0 and m_el % 6 == 5) or (el % 2 == 1 and m_el % 6 == 2):
                return '2_E^^'
        elif sym == 'C4h':
            if el % 2 == 0 and m_el % 4 == 0:
                return 'Ag'
            elif el % 2 == 0 and m_el % 4 == 2:
                return 'Bg'
            elif el % 2 == 0 and m_el % 4 == 1:
                return '1_Eg'
            elif el % 2 == 0 and m_el % 4 == 3:
                return '2_Eg'
            elif el % 2 == 1 and m_el % 4 == 0:
                return 'Au'
            elif el % 2 == 1 and m_el % 4 == 2:
                return 'Bu'
            elif el % 2 == 1 and m_el % 4 == 1:
                return '1_Eu'
            elif el % 2 == 1 and m_el % 4 == 3:
                return '2_Eu'
        elif sym == 'C6h':
            if el % 2 == 0 and m_el % 6 == 0:
                return 'Ag'
            elif el % 2 == 0 and m_el % 6 == 3:
                return 'Bg'
            elif el % 2 == 0 and m_el % 6 == 1:
                return '1_E1g'
            elif el % 2 == 0 and m_el % 6 == 5:
                return '2_E1g'
            elif el % 2 == 0 and m_el % 6 == 4:
                return '1_E2g'
            elif el % 2 == 0 and m_el % 6 == 2:
                return '2_E2g'
            elif el % 2 == 1 and m_el % 6 == 0:
                return 'Au'
            elif el % 2 == 1 and m_el % 6 == 3:
                return 'Bu'
            elif el % 2 == 1 and m_el % 6 == 1:
                return '1_E1u'
            elif el % 2 == 1 and m_el % 6 == 5:
                return '2_E1u'
            elif el % 2 == 1 and m_el % 6 == 4:
                return '1_E2u'
            elif el % 2 == 1 and m_el % 6 == 2:
                return '2_E2u'
    if sym in  ('Oh','O','Td','Th','T'):
        def cubic_groups(sym,sym_label):
            dim = sym_label[0]
            if sym == 'O':
                if dim in ('A','T'):
                    return sym_label[:2]
                elif dim == 'E':
                    return dim
            elif sym == 'T':
                return dim
            elif sym == 'Th':

                return dim + sym_label[-1]
            elif sym == 'Td':

                if dim in ('A','T'):
                    if sym_label[1:3] in ('1g','2u'):
                        return dim + '1'
                    elif sym_label[1:3] in ('1u','2g'):
                        return dim + '2'
                elif dim == 'E':
                    return dim

        c = 0
        for sym_l in symmetry_data[el]:
            if sym_l[0] == 'A':
                n = 1
            elif sym_l[0] == 'E':
                n = 2
            elif sym_l[0] == 'T':
                n = 3
            num = symmetry_data[el][sym_l]
            if c + n * num > m:
                num_label = int((m-c)/n)
                num_function = (m-c) % n
                key = sym_l
                break
            else:
                c+= n * num
        if el in Oh_sym[key]:
            ms = Oh_sym[key][el][num_label][0]
            coef = Oh_sym[key][el][num_label][1][num_function]
            if key[0] == 'T' and num_function == 0:
                ms = tuple(-np.array(ms,dtype= 'int'))
            elif key[0] == 'E':
                coef =  tuple(np.sqrt(2)*np.array(coef))
            if sym != 'Oh':
                final_new_sym = cubic_groups(sym,key)
                new_symmetry_data = []
                c = 0
                f = 0
                for sym_l in symmetry_data[el]:
                    new_sym = cubic_groups(sym,sym_l)
                    if sym_l[0][0] == 'A':
                        n = 1
                    elif sym_l[0][0] == 'E':
                        n = 2
                    elif sym_l[0][0] == 'T':
                        n = 3
                    num = symmetry_data[el][sym_l]
                    if c + n * num > m:
                        num_label = f + int((m-c)/n)
                        key = new_sym
                        break
                    else:
                        if new_sym == final_new_sym:
                            f += symmetry_data[el][sym_l]
                        c+= n * num

            return (key,(ms,coef)),num_label+1
        else:
            return (None,(None,None)),None



    else:
        el_sym = []
        for m_el in range(-el,el+1):
            el_sym.append(first_label(m_el))
        m_sym = el_sym[m]

        num = 0
        deg_list = []
        for mm,temp_sym in enumerate(el_sym):
            if not isinstance(m_sym,str) and not isinstance(temp_sym,str):
                if temp_sym[0] == m_sym[0]:
                    if temp_sym not in deg_list:
                        num +=1
                        if temp_sym == m_sym:
                            break
                        else:
                            deg_list.append(temp_sym)
            else:
                if temp_sym == m_sym:
                    num +=1
                if mm == m:
                    break
        return m_sym,num

# Solid Angles time series --> Rotor Value timeseries
def rotor_function(time_series,el,m,sym,time=True):
    """
    Converts solid angle to rotor value

    Parameters
    ----------
    time_series : numpy.ndarray, shape = (n_b,2,t)
        n_b : number of objects around central atom
            ex. Br-MLWFC --> (4,2,t)
            ex. Sn-MLWFC --> (1,2,t)
            ex. Sn-Br --> (6,2,t)
        2 : index 0 is phi, index 1 is theta as found in cart2sph()
        t : number of timesteps
    el : int, 0 >= el
        angular momentum quantum number
    m : int, 0 >= m <= 2*el
        index of symmetry adapted function for given el
    sym : str
        Point group in Schoenflies notation
    time : boolean
        if incoming array is timeseries of vectors then True
        if incoming array is for orientational distrubtion function calculation then False

    Returns
    -------
    rot_time_series : numpy.ndarray
        Time series of rotor values


    Examples
    --------
    >>> import numpy as np
    >>> from scipy.special import sph_harm
    ... # A distorted tetrahedron flipping polarization along z-axis
    ... cartesian = np.array([[[0,0,1],[0,0,-1]],[[0,1,-0.5],[0,1,0.5]],[[-0.3,-0.67,-0.5],[-0.3,-0.67,0.5]],[[-0.3,0.67,-0.5],[-0.3,0.67,0.5]]])
    ... time_series = np.empty((cartesian.shape[0],2,cartesian.shape[1]))
    ... for b,cart_b in enumerate(cartesian):
    ...     x,y,z = cart_b.T
    ...     phi,theta = cart2sph(x,y,z)[1:]
    ...     time_series[b,0] = phi
    ...     time_series[b,1] = theta
    ... rot_time_series = rotor_function(time_series,3,3,'D4h')
    ... print(rot_time_series)
     [ 0.41871469, -0.41871469]
    ... # This polarized distorted tetrahedron overlaps with the S^{3,3}_Z function. The rotor value flips depedening on how its polarization along z-axis
    ... rot_time_series = rotor_function(time_series,3,2,'D4h')
    ... print(rot_time_series)
     [-2.08166817e-17,  5.55111512e-17]
    ... # This polarized distorted tetrahedron does not overlap well with the S^{3,2}_Z function

    """
    def calc_rotor(phi,theta):
        n_steps = phi.shape[0]
        if sym in ('Oh','O','Td','Th','T'):
            # Cubic Harmonic is linear combination of real spherical harmonics with their coefficients
            ms,coefs = finding_sym(sym,el,m)[0][1]
            kh = np.zeros(n_steps)
            for el_m,coef in zip(ms,coefs):
                if coef != 0:
                    Y = sph_harm(abs(el_m), el, theta,phi)
                    # Linear combination of Y_l,m and Y_l,-m to create the real form.
                    if el_m < 0:
                        Y = np.sqrt(2) * (-1)**int(el_m) * Y.imag
                    elif el_m > 0:
                        Y = np.sqrt(2) * (-1)**int(el_m) * Y.real
                    else:
                        Y = Y.real
                    kh += Y * coef
            return kh
        else:
            el_m = m - el
            Y = sph_harm(abs(el_m), el, theta,phi)
            # Linear combination of Y_l,m and Y_l,-m to create the real form.
            if el_m < 0:
                Y = np.sqrt(2) * (-1)**el_m * Y.imag
            elif el_m > 0:
                Y = np.sqrt(2) * (-1)**el_m * Y.real
            else:
                Y = Y.real
            return Y
    if time:
        n_coord,n,n_steps = time_series.shape
        rot_time_series = np.zeros(n_steps)
        for b in time_series:
            phi,theta = b
            rot_time_series += calc_rotor(phi,theta)
    else:
        phi,theta = time_series
        return calc_rotor(phi,theta)
    # Return average value over the objects
    return rot_time_series/n_coord

# Find Coeffeicents for Laplace Series
def laplace_coef(time_series,sym,el_cutoff,fluc=False):
    """
    Laplace Series coefficients of orientational distribution of time series
    The coefficients is the average value of symmetry adapted function and non-zero for partner functions to the fully symmetric representations

    Parameters
    ----------
    time_series : numpy.ndarray, shape = (n_a,n_b,2,t)
        n_a : number of central atoms
        n_b : number of objects around central atom
            ex. Br-MLWFC --> (192,4,2,t)
            ex. Sn-MLWFC --> (64,1,2,t)
            ex. Sn-Br --> (64,6,2,t)
        2 : index 0 is phi, index 1 is theta as found in cart2sph()
        t : number of timesteps
    sym : str
        Point group in Schoenflies notation
    el_cutoff : int
        Laplace Series cutoff (max of 18 for cubic point groups)

    fluc : boolean
        If set to True flucations will be calcualted for every function

    Returns
    -------
    av_dict : dict
        dictionary of coeffeints with keys 'l' and sub keys 'm' with coefficents
        ex. {1:{0:0, 1:0.5 ,2:0},}

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.special import sph_harm
    ... cartesian = np.array([[[0,0,1],[0,0,-1]],[[0,1,-0.5],[0,1,0.5]],[[-0.3,-0.67,-0.5],[-0.3,-0.67,0.5]],[[-0.3,0.67,-0.5],[-0.3,0.67,0.5]]])
    ... time_series = np.empty((1,cartesian.shape[0],2,cartesian.shape[1]))
    ... for b,cart_b in enumerate(cartesian):
    ...     x,y,z = cart_b.T
    ...     phi,theta = cart2sph(x,y,z)[1:]
    ...     time_series[0,b,0] = phi
    ...     time_series[0,b,1] = theta
    ... av_dict,fluc_dict = laplace_coef(time_series,'D4h',5)
    ... print(av_dict)
    {1: {0: 0, 1: 0, 2: 0}, 2: {0: 0, 1: 0, 2: 0.11838077878935692, 3: 0, 4: 0}, 3: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, 4: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0.01099747764246678, 5: 0, 6: 0, 7: 0, 8: 0.08364483209125098}}

    """

    av_dict = {el: {m: 0 for m in range(2 * el + 1)} for el in range(1,el_cutoff)}
    if fluc:
        fluc_dict = {el: {m: 0 for m in range(2 * el + 1)} for el in range(1,el_cutoff)}
    else:
        fluc_dict = None

    n_a = time_series.shape[0]
    for ts in time_series:
        for el in range(1,el_cutoff):
            for m in range(2*el + 1):
                # Check if irrep is fully symmetric represention. el = 0, m = 0 is always the fully symmetric representation
                if finding_sym(sym,el,m)[0] == finding_sym(sym,0,0)[0]:
                    rot_time_series = rotor_function(ts,el,m,sym)
                    av_dict[el][m] += np.mean(rot_time_series)/n_a
                    if fluc:
                        fluc_dict[el][m] += np.mean(np.square(rot_time_series))/n_a
                elif fluc:
                    rot_time_series = rotor_function(i,el,m,sym)
                    fluc_dict[el][m] += np.mean(np.square(rot_time_series))/n_a

    return av_dict,fluc_dict

def main():
    parser = argparse.ArgumentParser(description="A script with two functions: add and subtract.")
    parser.add_argument('--h', type=str, choices=['cart2sph', 'finding_sym','rotor_function','laplace_coef'], help="Show help for the specified function.")

    args = parser.parse_args()

    if args.h:
        if args.h == "cart2sph":
            help(cart2sph)
        elif args.h == "finding_sym":
            help(finding_sym)
        elif args.h == "rotor_function":
            help(rotor_function)
        elif args.h == "laplace_coef":
            help(laplace_coef)
    else:
        print("Please provide the --h flag followed by the function name (add or subtract) to get help for the function.")

if __name__ == "__main__":
    main()
