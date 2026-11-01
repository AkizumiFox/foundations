# Coordinates and Vectors in \( \nR^n \)

Chapter 3 built the complex plane as pairs of real numbers and gave it a length, the modulus, with a triangle inequality. Analysis needs the same for lists of any length. A point of \( \nR^n \) is its list of coordinates. Points can be added and stretched by a real number. One more operation, the dot product, takes two points to a number. From the dot product come the length, the distance and the right angle, and one inequality, Cauchy–Schwarz, from which the other rules follow. This chapter builds that structure from the real numbers and proves every rule. It uses no linear algebra and no limits. Angles appear only in the last section, where the cosine of the angle between two vectors is defined as a quotient.

Calculus on \( \nR^n \) is built on this. A ball is the set of points at distance less than \( r \) from a center, and convergence of vectors is convergence of distances. The triangle inequality of Section 9.5 is behind every estimate. The linear algebra volumes take the same operations as axioms and prove the same rules for an abstract vector space.

**What you need.**

- Ordered pairs and Cartesian products, from *Sets and Functions* (@fd2:def-cartesian-product).
- Finite sums, from *Sets and Functions*, Chapter 3, with their rules from Chapter 1, Section 1.1 (@lem-ring-finite-sums).
- The rules of an ordered field, the absolute value and square roots in \( \nR \), from *Number Systems: From \(\nN\) to \(\nR\)* (@fd3:prp-cof-square-roots).
- The complex numbers, the modulus and the triangle inequality in \( \nC \), from Chapter 3 (@thm-complex-triangle-inequality).
- Fields (Chapter 4) for one remark in Section 9.2, polynomials (Chapters 6 and 7) for one exercise of Section 9.6, and groups (Chapter 5) and monotone functions (Chapter 8) for the review exercises of Section 9.6.

**Time.** About 25 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 30 hours for everything.

## Roadmap

- **Points and Coordinates.** The space \( \nR^n \) of lists of \( n \) real numbers (@def-real-n-space), subsets of the plane given by conditions on coordinates, and boxes.
- **Adding Points and Scaling Them.** Addition and scaling coordinate by coordinate, which obey the laws of a vector space (@prp-vector-space-laws-rn), and the standard vectors.
- **The Dot Product.** The dot product \( \inner{x}{y} = x_1 y_1 + \dots + x_n y_n \), its laws (@prp-dot-product-laws-rn), and orthogonal vectors.
- **Length and Distance.** The norm and the distance, Pythagoras (@prp-pythagoras-rn), the parallelogram law, and the comparison of the norm with the coordinates.
- **Cauchy–Schwarz and the Triangle Inequality.** The inequality \( \abs{\inner{x}{y}} \le \norm{x}\norm{y} \) with its equality case (@thm-cauchy-schwarz-rn), and the triangle inequality that follows from it.
- **Projection onto a Line and the Cosine of an Angle.** The projection of \( x \) onto the line through \( y \) is the closest point of that line to \( x \) (@thm-projection-closest-point), and the cosine of an angle lies between \( -1 \) and \( 1 \).
