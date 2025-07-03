# lcmFoam_GUI

Python GUI (tkinter package) for creating a lcmFoam case, running the case and post-processing the case.
Tested under Ubuntu.

## Required input
- Mesh file in Gmsh format (FPCM16_mesh.msh available)
- Input for simulation presented at FPCM16 (https://www.researchgate.net/publication/388184799_Improved_Finite_Volume_multiphase_flow_simulation_model_for_strongly_inhomogeneous_porous_media):
![image](https://github.com/user-attachments/assets/0f79836c-f3c0-496c-8ef6-30f0b7fe2851)

## Usage
- Copy Python script main1.py, shell script start_gui.sh, icon lcmfoam_icon.png, desktop file start_gui.desktop and mesh file FPCM_mesh.msh in a directory
- Copy the desktop file to the desktop and modify the path to the icon and to the start_gui.sh
- Start the GUI by double clicking on the desktop icon

## Mesh generation with Gmsh
Have a look at the video tutorial from https://www.youtube.com/watch?v=zQXUGmNJS6w to see how a structured mesh for thin-walled cavities can be created. A non-structured tetrahedron mesh only works if there is not flow in thickness direction. Anyway the simulation time for structured meshes is must shorter than for tetrahedron meshes.
