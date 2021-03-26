(*Description: Takes in the Cartesian coordinates (2-dimensional) of any pair of opposite corners of a rectangle and returns the area of the rectangle. The sides of the rectangle are parallel to the axes. *)

let abs x = if x < 0 then (-x) else x;;

let area (left,top) (right,bottom) =
(
  abs (left - right) * abs (top - bottom);
);;

area (1, 1) (2, 2);;
area (2, 2) (1, 1);;
area (2, 1) (1, 2);;
area (0, 1) (2, 3);;
area (1, 1) (1, 1);;
area ((-1), (-1)) (1, 1);;
