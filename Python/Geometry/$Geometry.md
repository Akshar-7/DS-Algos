## Table of Contents
* [Pick's Theorem](#picks-theorem)
* [Point distance from a Line](#point-distance-from-a-line)

### Pick's Theorem
<div align="center">
<img width="254" height="230" alt="image" src="https://github.com/user-attachments/assets/a45335a9-f748-4f18-8eb4-74db78432c59" />
</div>

According to Pick's Theorem, we can calculate the area of any polygon by counting the number of interior and boundary lattice points. If the number of interior points is $I$ and the number of boundary lattice points is $B$, then the Area ($A$) of the polygon is given by:

$$
A = I + \frac{B}{2} - 1
$$

### Point distance from a Line
<div align="center">
<img width="373" height="200" alt="image" src="https://github.com/user-attachments/assets/5b5fee4c-5bd9-425c-ac4e-7be330831671" />
</div>

The area of the triangle whose vertices are $s_1$, $s_2$ and $p$ can be calculated in two ways: it is both $\frac{1}{2}|s_2 - s_1|d$ and $\frac{1}{2}((s_1 - p) \times (s_2 - p))$. Thus, the shortest distance is:

$$
d = \frac{(s_1 - p) \times (s_2 - p)}{|s_2 - s_1|}.
$$
