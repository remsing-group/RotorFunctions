# Examples
## Files
In the real simulation the number of Br is 192 with over 500000 timesteps.
The files here are truncated just to show examples

All xyz files are Br-MLWFC (Maxiammly Localized Wannier Centers) vectors with the x,y,z components of the vectors being represented.
One could get this data by reading in a trajectory file, finding the 4 closest MLWFCs near a given Br, and then find the distance vector between them while applying periodic boundary conditions.

Br_#_MLWFC.npy files are 3D numpy file with shape (4,2,1000) with 4 being the number of MLWFC, 2 being theta and phi, and 1000 being the number of timesteps

Brs_MLWFC.npy is a 4D numpy files with shape (2,4,2,1000) with 2, being number of Br, 4 being the number of MLWFC, 2 being theta and phi, and 1000 being the number of timesteps

sym.inp is the symmetry input file.
The format is: 
(point group in Schoenflies notation) (angular momentum quantum number) (index of symmetry adapted function for given el)

sym_cubic.inp is an example of a cubic point group input file

## Example commands
First move Rotor_functions.py to local directory

This outputs 2 outfiles which is the theta and phi values of the inputted vectors
```
python3 Rotor_functions.py --f cart2sph --i Br_MLWFC_1_0.xyz
```

This prints out any info about the irrep for a given site symmetry group, el, and m
```
python3 Rotor_functions.py --f finding_sym --i sym.inp
```
```
python3 Rotor_functions.py --f finding_sym --i sym_cubic.inp
```

This outputs an outfile of the rotor values for a given set of input vectors and rotor function defined by sym.inp
```
python3 Rotor_functions.py --f rotor_function --i Br_1_MLWFC.npy
```

This outputs a json dictionary with the Laplace series coefficients 
```
python3 Rotor_functions.py --f laplace_coef --i Brs_MLWFC.npy
```
