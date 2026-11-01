# Lines, Hyperplanes, and Convex Sets

Chapter 9 gave \( \nR^n \) a distance. This chapter asks how much of the familiar geometry that distance already decides. A great deal: lines and segments, spheres and balls are all sets cut out by distances, and "\( x \) lies between \( p \) and \( q \)" is a statement about three distances and nothing else. One linear equation \( \inner{a}{x} = c \) cuts out a hyperplane, and the distance from a point to it has a formula. A set is convex when it contains the segment between any two of its points. The smallest convex set containing a given set is the set of its convex combinations.

Analysis uses all of this from its first chapters on. The mean value theorem moves along a segment, and a ball is the set of points where an estimate holds. In a convex set, an argument made along one segment works between any two points.

**What you need.**

- Vectors, the dot product, the norm and the distance, from Chapter 9, Sections 9.2 to 9.4 (@def-norm-rn).
- The triangle inequality and its equality case, from Section 9.5 (@thm-triangle-inequality-rn).
- Projection onto a line and the closest-point theorem, from Section 9.6 (@thm-projection-closest-point).
- The rules of an ordered field and square roots in \( \nR \), from *Number Systems: From \(\nN\) to \(\nR\)* (@fd3:prp-cof-square-roots).
- Finite sums and induction, from Chapter 1 and *Sets and Functions*, for convex combinations of many points (@fd2:thm-induction).

**Time.** About 15 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 20 hours for everything.

## Roadmap

- **Lines and Segments.** Lines \( p + \nR v \), segments \( [p, q] \), and the theorem that \( x \) lies on \( [p, q] \) exactly when \( \norm{p - x} + \norm{x - q} = \norm{p - q} \) (@thm-betweenness).
- **Hyperplanes and Nearest Points.** Hyperplanes \( \inner{a}{x} = c \), the nearest point on a line or a hyperplane with the distance to it (@prp-nearest-point-on-hyperplane), and how a line meets a sphere.
- **Convex Sets and Hulls.** Convex sets, which include balls (@prp-balls-convex), convex combinations, and the convex hull of a set as the set of convex combinations of its points.
