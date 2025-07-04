# lcmFoam_GUI

Python GUI (tkinter package) for creating a lcmFoam case, running the case and post-processing the case.
Tested under Ubuntu.

## Required input
- Mesh file in Gmsh format (FPCM16_mesh.msh available)
- Input for simulation presented at FPCM16 (https://www.researchgate.net/publication/388184799_Improved_Finite_Volume_multiphase_flow_simulation_model_for_strongly_inhomogeneous_porous_media). Please see the correlation between the values in the table and the GUI.

![image](https://github.com/user-attachments/assets/d11f568d-5fb3-461a-b41c-584ba8b95eda)

![image](https://github.com/user-attachments/assets/f0e18c1b-2fec-4cf1-bf3d-c9abdee147af)

The filling pattern after 30 s filling time for the two different wall boundary conditions should look like this:
![image](https://github.com/user-attachments/assets/1a3ea238-bc08-4fc3-befb-2fb4a91bc5b0)



## Usage
- Follow the instructions for OpenFoam and lcmFoam solver installation from https://github.com/lcmFoam/lcmFoam24?tab=readme-ov-file#installation-for-openfoam-v2406-on-ubuntu-operating-systems 
- Copy Python script main1.py, shell script start_gui.sh, icon lcmfoam_icon.png, desktop file start_gui.desktop and mesh file FPCM_mesh.msh in a directory
- Copy the desktop file to the desktop and modify the path to the icon and to the start_gui.sh
- Start the GUI by double clicking on the desktop icon

## Mesh generation with Gmsh
The free meshing software Gmsh can be downloaded from https://gmsh.info/ 

Have a look at the video tutorial from https://www.youtube.com/watch?v=zQXUGmNJS6w to see how a structured mesh for thin-walled cavities can be created. Mesh must include one or two cellZones (fluid and fluid2; typical use of fluid2 if there is a flow distribution medium on top). Currently, only two cellZones can be addressed via the GUI. Boundary faces must be labelled inlet, wall and outlet. Step-file geometry FPCM16_geometry.stp and Gmsh geo-file FPCM_mesh.geo are uploaded for demonstration purpose.

A non-structured tetrahedron mesh only works if there is not flow in thickness direction. Anyway the simulation time for structured meshes is must shorter than for tetrahedron meshes.
