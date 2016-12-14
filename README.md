This repository contains code to calculate values of p(a, b), that is, the
number of partitions of Gaussian integers a + bi into parts u + vi so that
u > 0 and v > 0. This is listed as sequence
[A090806](http://oeis.org/A090806) in the Online Encyclopedia of Integer
Sequences.

A table of values for 1 <= a <= 500 and 1 <= b <= 500 is also included as a
csv for convenience if time or computational resources are scarce.

The notebook provides an introduction to the problem and uses pandas as a
convenience, but it is not required for the calculations.

The `multip` module can also be run as a standalone script to calculate these
values, printing the main diagonal ([OEIS A108469](http://oeis.org/A108469)).

This work is released under
[CC0](https://creativecommons.org/publicdomain/zero/1.0/).
See LICENSE for more details.

The person who associated a work with this deed has dedicated the work to the
public domain by waiving all of his or her rights to the work worldwide under
copyright law, including all related and neighboring rights, to the extent
allowed by law.
