# Rotor Functions
## Code
Software to calculate rotor functions $`\mathcal{M}_{\xi}^{\ell,m}`$ values from a numpy array of vectors around central point/atom. 

Contains 4 functions:

- cart2sph: Converts Cartesian to Spherical Coordinates 
- finding_sym: Finds ith irrep label of symmetry adapted function
- rotor_function: Converts solid angle to rotor value
- laplace_coef: Finds Laplace Series coefficients of orientational distribution of time series


The help flag provides more detailed help for each function by running 
```
python3 Rotor_functions.py --h [function]
```
Please cite [Colin M. Hylton-Farrington, R. C. R., Dynamic Local Symmetry Fluctuations of Electron Density in Halide Perovskites. arXiv 2024.](https://arxiv.org/abs/2404.11247)

## Theory
Rotor functions, $`\mathcal{M}_{\xi}^{\ell,m}`$, naturally arise in the expansion of the orientational distribution function,
```math
 f_{\mu}\left(\Theta\right)=\frac{1}{4\pi} + \sum\limits_{\ell=1}^{\infty}\ \sum\limits_{m=0}^{2\ell} \left<\mathcal{M}_{\xi}^{\ell,m}(\textbf{R};\mu)\right> \mathcal{S}_{\xi}^{\ell,m}\left(\Theta_{i}\right),
```
where $\left<\cdots\right>$ indicates an ensemble average over configurations $\textbf{R}$ and the sums are over angular momentum ($\ell$) and index $m$.
Note that $`0 \leq m \leq 2\ell`$. 
The composite label $`\mu=(\alpha,\beta)`$ defines the vectors for which the solid angle, $\Theta$.
The first label, $`\alpha`$, indicates the identity of the central atom. 
The second label, $`\beta`$, defines a vector or set of vectors made by $\alpha$ and symmetry equivalent sites in its first coordination shell.
The expansion of $`f_\mu\left(\Theta_{i}\right)`$ is similar to the multipole expansion, and the rotor functions describe the structure of the multipoles of increasing angular momentum ($`\ell`$).

A rotor function, $`\mathcal{M}_{\xi}^{\ell,m}`$, describes the orientation of vectors centered at a defined site under a symmetry-adapted function $`\mathcal{S}_{\xi}^{\ell,m}`$ according to
```math
{\mathcal M}_{\xi}^{\ell,m} = \frac{1}{N}\sum_{i=1}^{N}{\mathcal S}_{\xi}^{\ell,m}\left(\Theta_{i}\right),
```
where *i* is the index of a vector centered on the site of interest, $N$ is the number of vectors for that site,
and $\Theta_i$ is the solid angle of vector $i$.

In crystals, the symmetry-adapted functions $`\mathcal{S}_{\xi}^{\ell,m}`$ are linear combinations of spherical harmonics that are partner functions to irreducible representations (irreps) of a particular crystallographic point group, where $\xi$ denotes the type of harmonic.
For all but cubic crystallographic point groups, the partner functions are the real spherical harmonics, also known as the Tesseral harmonics, $`\xi = \mathcal Z`$.
For cubic point groups, the symmetry-adapted functions are the cubic harmonics, $`\xi = \mathcal K`$. 
```math
S_{\mathcal{K}}^{\ell,m} = \sum_{m^\prime = 0}^{2\ell} a^{\ell,m^\prime}S_{\mathcal{Z}}^{\ell,m^{\prime}}.
```


