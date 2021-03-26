(* Description: Takes in the Cartesian coordinates (3-dimensional) of two opposite corners of a rectangular prism and returns its volume. The sides of the rectangular prism are parallel to the axes *)

let abs x = if x < 0 then (-x) else x;;

let volume (x1,y1,z1) (x2,y2,z2) =
(
  abs (x1 - x2) * abs (y1 - y2) * abs (z1 - z2);
);;

volume (1, 1, 1) (2, 2, 2);;
volume (2, 2, 2) (1, 1, 1);;
volume (0, 1, 2) (2, 3, 5);;
volume (1, 1, 1) (1, 1, 1);;
volume ((-1), (-1), (-1)) (1, 1, 1);;