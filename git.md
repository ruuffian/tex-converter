# The Dot Product

The **Dot Product** is a measure of how similar 2 vectors are to each other based on direction.
> If the dot product is **0** then they are **perpendicular**


## Formula
Let

<img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Bv%7D%20%3D%20%3Ca%2C%20b%2C%20c%3E">


<img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Bu%7D%20%3D%20%3Cx%2C%20y%2C%20z%3E">

Then

<img src="https://render.githubusercontent.com/render/math?math=%5Cboxed%7B%5Cvec%7Bv%7D%5Ccdot%5Cvec%7Bu%7D%20%3D%20ax%2Bby%2Bcz%7D">


## Properties

1. <img src="https://render.githubusercontent.com/render/math?math=a%5Ccdot%20a%20%3D%20%5Clvert%20a%20%5Crvert">
2. <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20%28b%2Bc%29%20%3D%20a%5Ccdot%20c%20%2B%20a%20%5Ccdot%20b">
3. <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20b%20%3D%20b%20%5Ccdot%20a">
4. <img src="https://render.githubusercontent.com/render/math?math=ca%20%5Ccdot%20b%20%3D%20c%28a%20%5Ccdot%20b%29%20%3D%20a%20%5Ccdot%20cb">

All can be proven with elementary algebra. 

## Relation to Cosine
> <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20b%20%3D%20%5Clvert%20a%20%5Crvert%20%5Clvert%20b%20%5Crvert%20%5Ccos%7B%5Ctheta%7D">
> <img src="https://render.githubusercontent.com/render/math?math=0%5Cleq%5Ctheta%5Cleq%5Cpi">

Notice at <img src="https://render.githubusercontent.com/render/math?math=%5Ctheta%20%3D%20%5Cfrac%7B%5Cpi%7D%7B2%7D">, <img src="https://render.githubusercontent.com/render/math?math=%5Ccos%7B%5Ctheta%7D%20%3D%200"> showing is that if <img src="https://render.githubusercontent.com/render/math?math=a%20%5Cperp%20b%20%5Cimplies%20a%20%5Ccdot%20b%20%3D%200">
### Observation
Suppose the angle is:
1. Acute: <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20b%20%5Cgt%200">
2. <img src="https://render.githubusercontent.com/render/math?math=%5Ctheta%20%3D%2090">: <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20b%20%3D%200">
3. Obtuse: <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ccdot%20b%20%5Clt%200">

## Projections
![[projectionExample.png]]

**Goal**: Find the length of the project of B *onto* A

### Derivation
Let **C** be the length of the projection of B onto A

Notice that 

<img src="https://render.githubusercontent.com/render/math?math=%5Ccos%7B%5Ctheta%7D%20%3D%20%5Cfrac%7BC%7D%7B%5Clvert%20b%20%5Crvert%7D%20%5Cto%20%5Clvert%20b%20%5Crvert%5Ccos%7B%5Ctheta%7D%20%3D%20C">

Recall the 'Relation to Cosine' for the **Dot product**

<img src="https://render.githubusercontent.com/render/math?math=C%20%3D%20%5Cfrac%7Ba%20%5Ccdot%20b%7D%7B%5Clvert%20a%20%5Crvert%20%5Clvert%20b%20%5Crvert%7D%5Clvert%20b%20%5Crvert">


<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bcomp%7D_%5Cvec%7Bb%7D%20%5Cvec%7Ba%7D%20%3D%20%5Cfrac%7Ba%20%5Ccdot%20b%7D%7B%5Clvert%20a%20%5Crvert%7D">


<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bcomp%7D_%5Cvec%7Bb%7D%5Cvec%7Ba%7D"> is the length of this projection **C**.

To get a Vector Project we just multipy <img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bcomp%7D_%5Cvec%7Bb%7D%20%5Cvec%7Ba%7D"> with the unit vector of <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Ba%7D">

<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bproj%7D_%5Cvec%7Bb%7D%5Cvec%7Ba%7D%20%3D%20%5Ctext%7Bcomp%7D_%5Cvec%7Bb%7D%5Cvec%7Ba%7D%28%5Cfrac%7B%5Cvec%7Ba%7D%7D%7B%5Clvert%20a%20%5Crvert%7D%29%0A">


<img src="https://render.githubusercontent.com/render/math?math=%0A%5Ctext%7Bproj%7D_%5Cvec%7Bb%7D%5Cvec%7Ba%7D%20%3D%20%5Cvec%7Ba%7D%5Cfrac%7Ba%20%5Ccdot%20b%7D%7B%28%5Clvert%20a%20%5Crvert%29%5E2%7D%0A">

---
### Projection Formulas
> <img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bcomp%7D_%5Cvec%7Bb%7D%20%5Cvec%7Ba%7D%20%3D%20%5Cfrac%7Ba%20%5Ccdot%20b%7D%7B%5Clvert%20a%20%5Crvert%7D">
> 
><img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bproj%7D_%5Cvec%7Bb%7D%5Cvec%7Ba%7D%20%3D%20%5Cvec%7Ba%7D%5Cfrac%7Ba%20%5Ccdot%20b%7D%7B%28%5Clvert%20a%20%5Crvert%29%5E2%7D">
---


# The cross Product
The **cross Product** produces a vector that is perpendicular to the 2 supplied.
## Formula 
Let

<img src="https://render.githubusercontent.com/render/math?math=a%20%3D%20%5Clangle%20a_1%2C%20a_2%2C%20a_3%20%5Crangle">


<img src="https://render.githubusercontent.com/render/math?math=b%20%3D%20%5Clangle%20b_1%2C%20b_2%2C%20b_3%20%5Crangle">



<img src="https://render.githubusercontent.com/render/math?math=%0Aa%20%5Ctimes%20b%20%3D%20%5Ctext%7Bdet%7D%0A%5Cbegin%7Bvmatrix%7D%0A%5Cvec%7Bi%7D%20%26%20%5Cvec%7Bj%7D%20%26%20%5Cvec%7Bk%7D%20%5C%5C%20%0Aa_1%20%26%20a_2%20%26%20a_3%20%5C%5C%0Ab_1%20%26%20b_2%20%26%20b_3%0A%5Cend%7Bvmatrix%7D%0A">

*Notation: The matrix inside the <img src="https://render.githubusercontent.com/render/math?math=det"> can also be transposed to give the same vector out*

Then:
> <img src="https://render.githubusercontent.com/render/math?math=%28a%20%5Ctimes%20b%29%20%5Ccdot%20a%20%3D%200">
> <img src="https://render.githubusercontent.com/render/math?math=%28a%20%5Ctimes%20b%29%20%5Ccdot%20b%20%3D%200">

Note if <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Ba%7D"> and <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Bb%7D"> are parallel **or** <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Ba%7D%20%3D%20%5Cvec%7Bb%7D"> then:

<img src="https://render.githubusercontent.com/render/math?math=a%20%5Ctimes%20b%20%3D%200">


Recall that the function **det**() gets the area of a parallelogram after a Linear Transformation T. This is why the vectors are loaded into a matrix and passed to the determinant.  

## Cross Product Geometry 
> <img src="https://render.githubusercontent.com/render/math?math=%7Ca%20%5Ctimes%20b%7C%20%3D%20%5Clvert%20a%20%5Crvert%20%5Clvert%20b%20%5Crvert%20%5Csin%7B%5Ctheta%7D"> 
> for <img src="https://render.githubusercontent.com/render/math?math=0%20%5Cleq%20%5Ctheta%20%5Cleq%20%5Cpi">

<img src="https://render.githubusercontent.com/render/math?math=%7Ca%20%5Ctimes%20b%7C"> represents the area of the parallogram spanned by <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Ba%7D"> & <img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Bb%7D">

## Properties
1. <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ctimes%20b%20%3D%20-%28b%20%5Ctimes%20a%29"> **antisymmetric**
2. <img src="https://render.githubusercontent.com/render/math?math=a%20%5Ctimes%20%28b%20%2B%20c%29%20%3D%20%28a%20%5Ctimes%20b%29%20%2B%20%28a%20%5Ctimes%20c%29">
3. <img src="https://render.githubusercontent.com/render/math?math=ra%20%5Ctimes%20b%20%3D%20r%28a%20%5Ctimes%20b%29%20%3D%20a%20%5Ctimes%20rb">
4. <img src="https://render.githubusercontent.com/render/math?math=%28a%20%2B%20b%29%20%5Ctimes%20c%20%3D%20%28a%20%5Ctimes%20c%29%20%2B%20%28b%20%5Ctimes%20c%29">
5. <img src="https://render.githubusercontent.com/render/math?math=%28a%20%5Ctimes%20b%29%5Ccdot%20c%20%3D%20a%20%5Ccdot%20%28b%20%5Ctimes%20c%29"> **Triple Product**

### Triple Product
The Triple Product represents the volume spanned by the 3 vectors

<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Babs%7D%28a%20%5Ctimes%20b%5Ccdot%20c%29%20%3D%20V">
