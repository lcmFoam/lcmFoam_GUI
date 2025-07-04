// Gmsh project created on Thu Jul 03 11:09:03 2025
SetFactory("OpenCASCADE");
Merge "FPCM16_geometry.stp";
Coherence;

//+
Extrude {0, 0, 0.6} {
  Surface{6}; Layers {2}; Recombine;
}
Coherence;
//+
Extrude {0, 0, -2.4} {
  Surface{6}; Layers {4}; Recombine;
}
Coherence;

//+
Physical Volume("fluid", 36) = {1};
//+
Physical Volume("fluid2", 37) = {2};
//+
Physical Surface("inlet", 38) = {19, 13};
//+
Physical Surface("outlet", 39) = {15, 9, 14, 8, 17, 11, 16, 10};
//+
Physical Surface("wall", 40) = {12};
//+
Physical Surface("wall2", 41) = {18};

Mesh 3;
Coherence Mesh;//+

