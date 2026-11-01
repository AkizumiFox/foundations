# Chapter Review

## Summary

A line in \( \nR^n \) is \( p + \nR v \) with \( v \ne 0 \), and two distinct points lie on exactly one line (@prp-line-through-two-points). A point lies on the segment \( [p, q] \) exactly when its distances to the ends add up to \( \norm{p - q} \), and then those two distances fix it (@thm-betweenness, @cor-point-pinned-on-segment). A hyperplane \( H_{a,c} \) determines its normal vector up to a non-zero factor (@prp-hyperplane-normals). The points equidistant from \( p \ne q \) form a hyperplane (@prp-perpendicular-bisector). Every point has exactly one nearest point on a line and on a hyperplane, with explicit formulas (@prp-nearest-point-on-line, @prp-nearest-point-on-hyperplane). A line meets a sphere in zero, one or two points according to its distance from the center (@prp-line-meets-sphere). Balls, lines, segments, hyperplanes and half-spaces are convex, and so is any intersection of convex sets (@prp-balls-convex, @prp-convex-examples, @prp-convex-operations). The convex hull of a set is the set of convex combinations of its points (@thm-convex-hull-combinations-rn).

What is open: the words "open ball" and "closed ball" are only names here. *Analysis on the Real Line* explains them, defines balls for any distance, and starts the analysis that uses this chapter's geometry.

## Proof methods in this chapter

- **Parametrize and solve** (@exm-method-parametrize). Give each line or segment its own parameter, write one equation per coordinate, solve, and check every equation, with the range \( [0, 1] \) for a segment. Introduced in Section 10.1, where it decides whether two lines in space meet. It returns more briefly in Section 10.2, where a line meets a sphere at the parameters solving one quadratic equation.
- **Use the equality case** (@exm-method-equality-case). When a known inequality holds with equality, write its equality condition with a named multiplier and solve. Introduced in Section 10.1, where it proves that a point with \( \norm{p - x} + \norm{x - q} = \norm{p - q} \) lies on \( [p, q] \). Exercise B3 of Section 10.3 uses it again, to show that the points strictly between two points of a sphere lie inside it.
- **The two-point test** (@exm-method-two-point-test). To prove a set convex, take two of its points and \( t \in [0, 1] \), split \( (1 - t)p + tq \) into \( (1 - t)(\dots) + t(\dots) \), and finish by the triangle inequality or by linearity. Introduced in Section 10.3, where it shows that balls are convex. Exercise B2 there runs it for sums of convex sets, and review exercise R2 offers it as a second route.
- **Peel off the last point.** Convexity speaks about two points at a time, so a statement about \( k + 1 \) points is reduced to one about \( k \) points and a segment. It proves in Section 10.3 that a convex set contains every convex combination of its points (@thm-convex-contains-combinations).

## Terms

- **closed ball**, **open ball**: \( \overline{B}(c, r) = \{x : \norm{x - c} \le r\} \) and \( B(c, r) = \{x : \norm{x - c} < r\} \), for \( r > 0 \) (@def-ball-rn).
- **collinear points**: points that all lie on one line (@def-collinear).
- **convex combination**: a sum \( \lambda_1 p_1 + \dots + \lambda_k p_k \) with every \( \lambda_i \ge 0 \) and \( \lambda_1 + \dots + \lambda_k = 1 \) (@def-convex-combination-rn).
- **convex hull**: the intersection of all convex sets containing a set \( S \), written \( \operatorname{conv} S \) (@def-convex-hull-rn).
- **convex set**: a set that contains the segment between any two of its points (@def-convex-set-rn).
- **half-space**: one of the sets \( \{\inner{a}{x} \le c\} \), \( \{\inner{a}{x} \ge c\} \) (closed) or \( \{\inner{a}{x} < c\} \), \( \{\inner{a}{x} > c\} \) (open), for \( a \ne 0 \) (@def-hyperplane-rn).
- **hyperplane**: a set \( H_{a,c} = \{x \in \nR^n : \inner{a}{x} = c\} \) with \( a \ne 0 \) (@def-hyperplane-rn).
- **line**: a set \( p + \nR v = \{p + tv : t \in \nR\} \) with \( v \ne 0 \); \( t \mapsto p + tv \) is a parametrization of it (@def-line-rn).
- **normal vector**: the vector \( a \) in \( H_{a,c} \), fixed by the hyperplane only up to a non-zero factor (@def-hyperplane-rn).
- **segment**: \( [p, q] = \{(1 - t)p + tq : t \in [0, 1]\} \), with midpoint \( (p + q)/2 \) (@def-segment-rn).
- **sphere**: \( S(c, r) = \{x : \norm{x - c} = r\} \), for \( r > 0 \) (@def-sphere-rn).
- **star-shaped set**: a set \( S \) with a point \( c \in S \) such that \( [c, x] \subseteq S \) for every \( x \in S \) (@def-star-shaped).

## Results used from earlier volumes

*Number Systems: From \(\nN\) to \(\nR\)*:

- the rules of an ordered ring (@fd3:prp-ordered-ring-rules), an ordered field (@fd3:prp-ordered-field-halves) and the absolute value (@fd3:prp-absolute-value-ordered-field), on nearly every page;
- square roots in \( \nR \) (@fd3:prp-cof-square-roots, @fd3:thm-reals-complete-ordered-field), for spheres meeting lines and for the warning of Section 10.3;
- completeness (@fd3:def-complete-ordered-field), in Exercise C1 of Section 10.3;
- the irrationality of \( \sqrt 2 \) (@fd3:thm-no-rational-square-two).

*Sets and Functions*:

- intersections of families (@fd2:def-family-union-intersection) and the smallest set with a property (@fd2:prp-smallest-closed-set), for convex hulls;
- induction (@fd2:thm-induction), for convex combinations of many points.

## Results used from earlier chapters

- Chapter 9, Sections 9.2 to 9.4: vectors and their operations (@def-vector-operations-rn), the norm (@def-norm-rn, @prp-norm-basic-rn), the distance (@def-distance-rn), expanding a square (@exm-method-expand-the-square) and Pythagoras (@prp-pythagoras-rn).
- Chapter 9, Section 9.5: the triangle inequality with its equality case (@thm-triangle-inequality-rn), which Section 10.1 rests on.
- Chapter 9, Section 9.6: projection onto a line (@def-projection-rn) and the closest-point theorem (@thm-projection-closest-point), which give every nearest point of Section 10.2.
- Chapter 1, Section 1.1: the rules for finite sums (@lem-ring-finite-sums, @prp-sum-reindex), in Section 10.3.
- Chapter 8, Section 8.3: the infimum by reflection (@prp-real-infimum), in Exercise C1 of Section 10.3.
- For the review exercises of Section 10.3 only:
  - the coordinate bounds for the norm (@prp-norm-coordinate-bounds) and the plane read as \( \nC \) (@prp-plane-is-complex-plane), from Section 9.4;
  - the modulus (@thm-conjugate-properties) and the unit circle (@prp-unit-circle), from Sections 3.2 and 3.5;
  - evaluation of polynomials (@thm-evaluation-respects-operations), from Section 6.4.

## Borrowed facts

The chapter borrows nothing new. It uses no cosine, sine or \( \pi \), and no angle: everything in it is proved from the ordered field \( \nR \) and the results listed above. It uses no linear algebra either, and no limits.

## Threads

- **Betweenness by distances.** Section 10.1 says "\( x \) lies on \( [p, q] \)" using distances alone (@thm-betweenness). The equality case behind it belongs to the Euclidean distance. For the distance that measures by the largest coordinate, the square \( \{\max(\abs{x_1}, \abs{x_2}) \le 1\} \) has a whole segment in its edge, so the analogue of Exercise B3 of Section 10.3 fails. *Analysis on the Real Line* takes the distance-only form to sets with any distance. *Affine and Projective Geometry* uses it to show that distance-preserving maps keep segments.
- **Convex and star-shaped sets.** Balls are convex (Section 10.3), and convex sets are star-shaped about each of their points. *Analysis on the Real Line* joins points of a ball by segments when it studies connectedness. *Complex Analysis* proves Cauchy's theorem first on discs and convex sets, where a primitive is built by integrating along segments. *Analysis on Manifolds* proves the Poincaré lemma on star-shaped sets.
