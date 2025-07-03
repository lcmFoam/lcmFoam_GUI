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

//Mesh(3);
//Coherence Mesh;//+
Physical Volume("fluid", 36) = {1};
//+
Physical Volume("fluid2", 37) = {2};
//+
Physical Surface("inlet", 38) = {19, 13};
//+
Physical Surface("wall", 39) = {12, 18};
//+
Physical Surface("outlet", 40) = {15, 9, 14, 8, 17, 11, 16, 10};

Mesh 3;
Coherence Mesh;