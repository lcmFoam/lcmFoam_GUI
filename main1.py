#create executable with pyinstaller main1.py --onefile
#Fehlermeldungen als Pop-Up-Fenster


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import platform
import sys

root = tk.Tk()
root.title("Create lcmFoam case")
root.resizable(False, False)
root.columnconfigure(1, weight=1)



# Physical variables
tk.Label(
    root,
    text="g [m/s^2]=",
).grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
g1 = ttk.Entry(root)
g1.insert(0,"0")
g1.grid(row=0, column=2, padx=5, pady=5, ipadx=5)
g2 = ttk.Entry(root)
g2.insert(0,"0")
g2.grid(row=0, column=3, padx=5, pady=5, ipadx=5)
g3 = ttk.Entry(root)
g3.insert(0,"0")
g3.grid(row=0, column=4, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="rho_resin [kg/m^3]=",
).grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
rho_resin = ttk.Entry(root)
rho_resin.insert(0,"917")
rho_resin.grid(row=1, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="nu_resin [m^2/s]=",
).grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
nu_resin = ttk.Entry(root)
nu_resin.insert(0,"0.00007088")
nu_resin.grid(row=2, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="rho_air [kg/m^3]=",
).grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)
rho_air = ttk.Entry(root)
rho_air.insert(0,"1.225")
rho_air.grid(row=3, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="nu_air [m^2/s]=",
).grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)
nu_air = ttk.Entry(root)
nu_air.insert(0,"1.48e-5")
nu_air.grid(row=4, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="sigma [N/m]=",
).grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)
sigma = ttk.Entry(root)
sigma.insert(0,"0")
sigma.grid(row=5, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="p_init [N/m^2]=",
).grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)
p_init = ttk.Entry(root)
p_init.insert(0,"0")
p_init.grid(row=6, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="p_inlet [N/m^2]=",
).grid(row=7, column=1, padx=5, pady=5, sticky=tk.E)
p_inlet = ttk.Entry(root)
p_inlet.insert(0,"2392")
p_inlet.grid(row=7, column=2, padx=5, pady=5, ipadx=5)

#Cell zone Fluid 1 input
tk.Label(
    root,
    text="Cell zone 1:",
).grid(row=0, column=5, padx=5, pady=5, sticky=tk.E)
fluid1 = ttk.Combobox(
    root,
    values=["Used"],  #["Used", "Not used"],
    state="readonly",
)
fluid1.current(0)
fluid1.grid(row=0, column=6, padx=5, pady=5)
tk.Label(
    root,
    text="porosity [-]=",
).grid(row=1, column=5, padx=5, pady=5, sticky=tk.E)
fluid1_porosity = ttk.Entry(root)
fluid1_porosity.insert(0,"0.868")
fluid1_porosity.grid(row=1, column=6, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="permeability [m^2]=",
).grid(row=2, column=5, padx=5, pady=5, sticky=tk.E)
fluid1_permeability1 = ttk.Entry(root)
fluid1_permeability1.insert(0,"10.32e-9")
fluid1_permeability1.grid(row=2, column=6, padx=5, pady=5, ipadx=5)
fluid1_permeability2 = ttk.Entry(root)
fluid1_permeability2.insert(0,"2.06e-9")
fluid1_permeability2.grid(row=2, column=7, padx=5, pady=5, ipadx=5)
fluid1_permeability3 = ttk.Entry(root)
fluid1_permeability3.insert(0,"1e-9")
fluid1_permeability3.grid(row=2, column=8, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="origin [m]=",
).grid(row=3, column=5, padx=5, pady=5, sticky=tk.E)
fluid1_origin1 = ttk.Entry(root)
fluid1_origin1.insert(0,"0")
fluid1_origin1.grid(row=3, column=6, padx=5, pady=5, ipadx=5)
fluid1_origin2 = ttk.Entry(root)
fluid1_origin2.insert(0,"0")
fluid1_origin2.grid(row=3, column=7, padx=5, pady=5, ipadx=5)
fluid1_origin3 = ttk.Entry(root)
fluid1_origin3.insert(0,"0")
fluid1_origin3.grid(row=3, column=8, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="e1 [m]=",
).grid(row=4, column=5, padx=5, pady=5, sticky=tk.E)
fluid1_e1_1 = ttk.Entry(root)
fluid1_e1_1.insert(0,"1")
fluid1_e1_1.grid(row=4, column=6, padx=5, pady=5, ipadx=5)
fluid1_e1_2 = ttk.Entry(root)
fluid1_e1_2.insert(0,"0")
fluid1_e1_2.grid(row=4, column=7, padx=5, pady=5, ipadx=5)
fluid1_e1_3 = ttk.Entry(root)
fluid1_e1_3.insert(0,"0")
fluid1_e1_3.grid(row=4, column=8, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="e2 [m]=",
).grid(row=5, column=5, padx=5, pady=5, sticky=tk.E)
fluid1_e2_1 = ttk.Entry(root)
fluid1_e2_1.insert(0,"0")
fluid1_e2_1.grid(row=5, column=6, padx=5, pady=5, ipadx=5)
fluid1_e2_2 = ttk.Entry(root)
fluid1_e2_2.insert(0,"1")
fluid1_e2_2.grid(row=5, column=7, padx=5, pady=5, ipadx=5)
fluid1_e2_3 = ttk.Entry(root)
fluid1_e2_3.insert(0,"0")
fluid1_e2_3.grid(row=5, column=8, padx=5, pady=5, ipadx=5)


#Cell zone Fluid 2 input
tk.Label(
    root,
    text="Cell zone 2:",
).grid(row=0, column=9, padx=5, pady=5, sticky=tk.E)
fluid2 = ttk.Combobox(
    root,
    values=["Used", "Not used"],
    state="readonly",
)
fluid2.current(1)
fluid2.grid(row=0, column=10, padx=5, pady=5)
tk.Label(
    root,
    text="porosity [-]=",
).grid(row=1, column=9, padx=5, pady=5, sticky=tk.E)
fluid2_porosity = ttk.Entry(root)
fluid2_porosity.insert(0,"0.868")
fluid2_porosity.grid(row=1, column=10, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="permeability [m^2]=",
).grid(row=2, column=9, padx=5, pady=5, sticky=tk.E)
fluid2_permeability1 = ttk.Entry(root)
fluid2_permeability1.insert(0,"10.32e-9")
fluid2_permeability1.grid(row=2, column=10, padx=5, pady=5, ipadx=5)
fluid2_permeability2 = ttk.Entry(root)
fluid2_permeability2.insert(0,"2.06e-9")
fluid2_permeability2.grid(row=2, column=11, padx=5, pady=5, ipadx=5)
fluid2_permeability3 = ttk.Entry(root)
fluid2_permeability3.insert(0,"1e-9")
fluid2_permeability3.grid(row=2, column=12, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="origin [m]=",
).grid(row=3, column=9, padx=5, pady=5, sticky=tk.E)
fluid2_origin1 = ttk.Entry(root)
fluid2_origin1.insert(0,"0")
fluid2_origin1.grid(row=3, column=10, padx=5, pady=5, ipadx=5)
fluid2_origin2 = ttk.Entry(root)
fluid2_origin2.insert(0,"0")
fluid2_origin2.grid(row=3, column=11, padx=5, pady=5, ipadx=5)
fluid2_origin3 = ttk.Entry(root)
fluid2_origin3.insert(0,"0")
fluid2_origin3.grid(row=3, column=12, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="e1 [m]=",
).grid(row=4, column=9, padx=5, pady=5, sticky=tk.E)
fluid2_e1_1 = ttk.Entry(root)
fluid2_e1_1.insert(0,"1")
fluid2_e1_1.grid(row=4, column=10, padx=5, pady=5, ipadx=5)
fluid2_e1_2 = ttk.Entry(root)
fluid2_e1_2.insert(0,"0")
fluid2_e1_2.grid(row=4, column=11, padx=5, pady=5, ipadx=5)
fluid2_e1_3 = ttk.Entry(root)
fluid2_e1_3.insert(0,"0")
fluid2_e1_3.grid(row=4, column=12, padx=5, pady=5, ipadx=5)
tk.Label(
    root,
    text="e2 [m]=",
).grid(row=5, column=9, padx=5, pady=5, sticky=tk.E)
fluid2_e2_1 = ttk.Entry(root)
fluid2_e2_1.insert(0,"0")
fluid2_e2_1.grid(row=5, column=10, padx=5, pady=5, ipadx=5)
fluid2_e2_2 = ttk.Entry(root)
fluid2_e2_2.insert(0,"1")
fluid2_e2_2.grid(row=5, column=11, padx=5, pady=5, ipadx=5)
fluid2_e2_3 = ttk.Entry(root)
fluid2_e2_3.insert(0,"0")
fluid2_e2_3.grid(row=5, column=12, padx=5, pady=5, ipadx=5)


#Spacer
spacer1=tk.Label(root,text="")
spacer1.grid(row=10, column=1, padx=5, pady=5, ipadx=5)


# Time
tk.Label(
    root,
    text="endTime [s]=",
).grid(row=11, column=1, padx=5, pady=5, sticky=tk.E)
endTime = ttk.Entry(root)
endTime.insert(0,"60")
endTime.grid(row=11, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="writeInterval [s]=",
).grid(row=12, column=1, padx=5, pady=5, sticky=tk.E)
writeInterval = ttk.Entry(root)
writeInterval.insert(0,"1")
writeInterval.grid(row=12, column=2, padx=5, pady=5, ipadx=5)

tk.Label(
    root,
    text="deltaT [s]=",
).grid(row=13, column=1, padx=5, pady=5, sticky=tk.E)
deltaT = ttk.Entry(root)
deltaT.insert(0,"1e-9")
deltaT.grid(row=13, column=2, padx=5, pady=5, ipadx=5)

# dynamic b.c.
#Slip or dynamic wall b.c.
tk.Label(
    root,
    text="Wall pressure b.c.:",
).grid(row=11, column=5, padx=5, pady=5, sticky=tk.E)
pWallType = ttk.Combobox(
    root,
    values=["Constant value", "Dynamic"],
    state="readonly",
)
pWallType.current(0)
pWallType.grid(row=11, column=6, padx=5, pady=5)
pWallType



#Spacer
spacer2=tk.Label(root,text="")
spacer2.grid(row=20, column=1, padx=5, pady=5, ipadx=5)



system = platform.system()
print(system)
if system=="Linux"or system=="linux":
    initialdir_val = "/home"
else:
    initialdir_val = "C:"
print(initialdir_val)

# Select mesh file button
f1=tk.StringVar()
def select_mesh_file():
    meshfile1=filedialog.askopenfilename(title="Select mesh file",filetypes=[("Gmsh files", ".msh")],initialdir = initialdir_val)
    if meshfile1:
        f1.set(meshfile1)
submit1 = tk.Button(
    root,
    text="Select mesh file" ,
    command=lambda: select_mesh_file()
)
submit1.grid(row=21, column=1, padx=5, pady=5, sticky=tk.E)
submit1_label = tk.Label(root, textvariable=f1, bg="lightgray", fg="black")
submit1_label.grid(row=21, column=2, columnspan=5, padx=5, pady=5, sticky=tk.E)

tk.Label(
    root,
    text="Mesh scaling factor: ",
).grid(row=22, column=1, padx=5, pady=5, sticky=tk.E)
scaling_factor = ttk.Entry(root)
scaling_factor.insert(0,"0.001")
scaling_factor.grid(row=22, column=2, padx=5, pady=5, ipadx=5)


#Spacer
spacer3=tk.Label(root,text="")
spacer3.grid(row=23, column=1, padx=5, pady=5, ipadx=5)


tk.Label(
    root,
    text="Case name: ",
).grid(row=25, column=1, padx=5, pady=5, sticky=tk.E)
case_name = ttk.Entry(root)
case_name.insert(0,"lcmFoamCase1")
case_name.grid(row=25, column=2, padx=5, pady=5, ipadx=5)

# Select case directory button
d1=tk.StringVar()
def browse():
    dir1=filedialog.askdirectory(title="Select case directory",mustexist=1,initialdir = initialdir_val)
    if dir1:
        d1.set(dir1)
submit2 = tk.Button(
    root,
    text="Create case in folder" ,
    command=lambda: browse()
)
submit2.grid(row=26, column=1, padx=5, pady=5, sticky=tk.E)
label1 = tk.Label(root, textvariable=d1, bg="lightgray", fg="black")
label1.grid(row=26, column=2, columnspan=5, padx=5, pady=5, sticky=tk.E)


#Spacer
spacer3=tk.Label(root,text="")
spacer3.grid(row=27, column=1, padx=5, pady=5, ipadx=5)



tk.Label(
    root,
    text="OpenFOAM version: ",
).grid(row=28, column=1, padx=5, pady=5, sticky=tk.E)
openfoam_version = ttk.Entry(root)
openfoam_version.insert(0,"openfoam2406")
openfoam_version.grid(row=28, column=2, padx=5, pady=5, ipadx=5)

#Spacer
spacer3=tk.Label(root,text="")
spacer3.grid(row=29, column=1, padx=5, pady=5, ipadx=5)

# Submit button
submit = ttk.Button(
    root,
    text="Create case",
    command=lambda: create_case()
)
submit.grid(row=40, column=1, padx=5, pady=5, sticky=tk.E)


#Spacer
spacer3=tk.Label(root,text="")
spacer3.grid(row=41, column=1, padx=5, pady=5, ipadx=5)

# Submit button
submit41 = ttk.Button(
    root,
    text="Clear case",
    command=lambda: clear_case()
)
submit41.grid(row=42, column=3, padx=5, pady=5, sticky=tk.E)
def clean_case():
    print('Clean case')
    str_openfoam=openfoam_version.get()  #"openfoam2406"
    str_casefolder=os.path.join(d1.get(),case_name.get())  #dir_name
    command41=str_openfoam + "formListTimes -rm -case "+ str_casefolder
    print(command41)
    os.system(command41)
    

# Submit button
submit42 = ttk.Button(
    root,
    text="Run case",
    command=lambda: run_case()
)
submit42.grid(row=42, column=1, padx=5, pady=5, sticky=tk.E)
def run_case():
    print('Run case')
    str_openfoam=openfoam_version.get()  #"openfoam2406"
    str_casefolder=os.path.join(d1.get(),case_name.get())  #dir_name
    command42=str_openfoam +" lcmFoam24 -case "+ str_casefolder
    print(command42)
    os.system(command42)


submit43 = ttk.Button(
    root,
    text="Post-process case",
    command=lambda: run_parafoam()
)
submit43.grid(row=42, column=2, padx=5, pady=5, sticky=tk.E)
def run_parafoam():
    print('Post-process case')
    str_openfoam=openfoam_version.get()  #"openfoam2406"
    str_casefolder=os.path.join(d1.get(),case_name.get())  #dir_name
    command43=str_openfoam +" paraFoam -case "+ str_casefolder
    print(command43)
    os.system(command43)
    
    
    
#-------------------------------------------------------------------------------------------------------------------
# Function for creating case files
#-------------------------------------------------------------------------------------------------------------------
def create_case():
    #create case folder
    print('Create case')
    str1=d1.get()  #"/home/obertscheider/myOpenFOAM/GUI"
    str2=case_name.get()  #"case1"
    dir_name=os.path.join(str1,str2)
    
    #delete case folder
    command0="rm -r " + dir_name 
    print(command0)
    os.system(command0)
    
    #create case folder
    try:    
        os.mkdir(dir_name)
        print(f"Director '{dir_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    str3="0"
    dir_name3=os.path.join(dir_name,str3)
    try:    
        os.mkdir(dir_name3)
        print(f"Director '{dir_name3}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    str4="constant"
    dir_name4=os.path.join(dir_name,str4)
    try:    
        os.mkdir(dir_name4)
        print(f"Director '{dir_name4}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    str5="system"
    dir_name5=os.path.join(dir_name,str5)
    try:    
        os.mkdir(dir_name5)
        print(f"Director '{dir_name5}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

    system_dir=dir_name5
    controlDict_file=os.path.join(system_dir,"controlDict")
    try:
        d=open(controlDict_file,"w")
    except:
        print("controlDict not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    version     2.0;\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "system";\n')
    d.write("    object      controlDict;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("application     lcmFoam24;\n")
    d.write("\n")
    d.write("startFrom       latestTime;\n")
    d.write("\n")
    d.write("startTime       0;\n")
    d.write("\n")
    #d.write("endTime         60;\n")
    d.write("endTime         "+ endTime.get() +";\n")
    d.write("\n")
    d.write("stopAt          endTime;\n")
    d.write("\n") 
    #d.write("deltaT          1e-9; \n")
    d.write("deltaT          "+ deltaT.get() +"; \n")
    d.write("\n")
    d.write("writeControl    adjustableRunTime;\n")
    d.write("\n")
    #d.write("writeInterval   1;\n")
    d.write("writeInterval   "+ writeInterval.get() +";\n")
    d.write("\n")
    d.write("purgeWrite      0;\n")
    d.write("\n")
    d.write("writeFormat     binary;\n")
    d.write("\n")
    d.write("writePrecision  6;\n")
    d.write("\n")
    d.write("writeCompression off;\n")
    d.write("\n")
    d.write("timeFormat      general;\n")
    d.write("\n")
    d.write("timePrecision   6;\n")
    d.write("\n")
    d.write("runTimeModifiable true;\n")
    d.write("\n")
    d.write("adjustTimeStep  true;\n")
    d.write("\n")
    d.write("maxCo           0.5;\n")
    d.write("\n")
    d.write("maxAlphaCo      0.5;\n")
    d.write("\n") 
    d.write("maxDeltaT       1;\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()
    
    system_dir=dir_name5
    fvSchemes_file=os.path.join(system_dir,"fvSchemes")
    try:
        d=open(fvSchemes_file,"w")
    except:
        print("fvSchemes not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    version     2.0;\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "system";\n')
    d.write("    object      fvSchemes;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("ddtSchemes\n")
    d.write("{\n")
    d.write("    default         Euler;\n")
    d.write("}\n")
    d.write("\n")
    d.write("gradSchemes\n")
    d.write("{\n")
    d.write("    default         cellLimited Gauss linear 1;\n")
    d.write("}\n")
    d.write("\n")
    d.write("divSchemes\n")
    d.write("{\n")
    d.write("    //default          Gauss linear;    Options: Gauss linearUpwind grad(U) //bounded Gauss upwind; //Gauss QUICK;  //bounded Gauss vanLeer;\n")
    d.write("    div(rhoPhi,U)    Gauss linearUpwind grad(U);\n")
    d.write("    div(phi,alpha1_) Gauss vanLeer;  \n")
    d.write("    div(phi)         Gauss vanLeer;\n")
    d.write("    div(phi,p_rgh)   Gauss vanLeer;\n")
    d.write("    div(phiHbyA)     bounded Gauss upwind;   \n")
    d.write("    div(phi,rgh_)    bounded Gauss upwind; \n")
    d.write("    div(phi,rgh_)    bounded Gauss upwind; \n")
    d.write("    div(interpolate(U),alpha1_) Gauss vanLeer;\n")
    d.write("    div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear;\n")
    d.write("    div(U)           Gauss linear; \n")
    d.write("    div(phi,alpha)   Gauss vanLeer;\n")
    d.write("    div(phirb,alpha) Gauss linear;\n")
    d.write("    div(interpolate((rho*U)),U) bounded Gauss upwind;\n")
    d.write("}\n")
    d.write("\n")
    d.write("laplacianSchemes\n")
    d.write("{\n")
    d.write("    default         Gauss linear corrected;\n")
    d.write("}\n")
    d.write("\n")
    d.write("interpolationSchemes\n")
    d.write("{\n")
    d.write("    default         linear;\n")
    d.write("}\n")
    d.write("\n")
    d.write("snGradSchemes\n")
    d.write("{\n")       
    d.write("    default         corrected;\n")
    d.write("}\n")    
    d.write("\n")    
    d.write("// ************************************************************************* //\n")
    d.close()    

    system_dir=dir_name5
    fvSolution_file=os.path.join(system_dir,"fvSolution")
    try:
        d=open(fvSolution_file,"w")
    except:
        print("fvSolution not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    version     2.0;\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "system";\n')
    d.write("    object      fvSolution;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("solvers\n")
    d.write("{\n")
    d.write('    "alpha.*"\n')
    d.write("    {\n")
    d.write("        nAlphaCorr      1;\n")
    d.write("        nAlphaSubCycles 2;\n")
    d.write("        cAlpha          1;\n")
    d.write("\n")
    d.write("        solver          smoothSolver;\n")
    d.write("        smoother        GaussSeidel;\n")
    d.write("        tolerance       1e-06;\n")
    d.write("        relTol          0;\n")
    d.write("        nSweeps         1;\n")
    d.write("    }\n")
    d.write("\n")
    d.write('    "pcorr.*"\n')
    d.write("    {\n")
    d.write("        solver          PCG;\n")
    d.write("        preconditioner  DIC;\n")
    d.write("        tolerance       1e-5;\n")
    d.write("        relTol          0;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    p_rgh\n")
    d.write("    {\n")
    d.write("        solver          PCG;\n")
    d.write("        preconditioner  DIC;\n")
    d.write("        tolerance       1e-07;\n")
    d.write("        relTol          0.05;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    p_rghFinal\n")
    d.write("    {\n")
    d.write("        $p_rgh;\n")
    d.write("        relTol          0;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    alpha1_\n")
    d.write("    {\n")       
    d.write("        solver          smoothSolver;\n")
    d.write("        smoother        symGaussSeidel;\n")
    d.write("        tolerance       1e-09;\n")
    d.write("        relTol          0;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    alpha1_Final\n")
    d.write("    {\n")
    d.write("        $alpha1_;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    U\n")
    d.write("    {\n")
    d.write("        solver          smoothSolver;\n")
    d.write("        smoother        symGaussSeidel;\n")
    d.write("        tolerance       1e-6;\n")
    d.write("        relTol          0;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    UFinal\n")
    d.write("    {\n")
    d.write("        $U;\n")
    d.write("    }\n")
    d.write("\n")
    d.write("    doc\n")
    d.write("    {\n")
    d.write("        solver          smoothSolver;\n")
    d.write("        smoother        symGaussSeidel;\n")
    d.write("        tolerance       1e-06;\n")
    d.write("        relTol          0;\n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("PIMPLE\n")
    d.write("{\n")
    d.write("    momentumPredictor   no;\n")
    d.write("    nOuterCorrectors    6;  //2;  \n")
    d.write("    nCorrectors         1;  //3;  \n")
    d.write("    nNonOrthogonalCorrectors 0;  //3;\n")
    d.write("}\n")
    d.write("\n")       
    d.write("relaxationFactors\n")
    d.write("{\n")
    d.write("    fields\n")
    d.write("    {\n")
    d.write("        p               1.0;\n")
    d.write("    }\n")
    d.write("    equations\n")
    d.write("    {\n")
    d.write("        U               1.0;\n")
    d.write("    }\n")       
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()   

    #copy mesh file there
    #call openfoam for gmshToFoam and scale: 
    str_openfoam=openfoam_version.get()  #"openfoam2406"
    str_meshfilename=f1.get()  #"permeameter_cavity3.msh"
    str_casefolder=os.path.join(d1.get(),case_name.get())  #dir_name
    command0="cp " + str_meshfilename +" "+str_casefolder  #+"/."
    print(command0)
    os.system(command0)

    command1=str_openfoam +" gmshToFoam "+ str_meshfilename + " -case "+ str_casefolder
    print(command1)
    os.system(command1)
    str_scaling=scaling_factor.get()  #"0.001"
    command2=str_openfoam +" transformPoints -scale "+ str_scaling + " -case "+ str_casefolder
    print(command2)
    os.system(command2)


    
    
    
    
    #create 0 folder
    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"alpha.air")
    try:
        d=open(controlDict_file,"w")
    except:
        print("alpha.air not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      alpha.air;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 0 0 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform 1;\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            value uniform 0;  \n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            value uniform 1;  \n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()

    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"alpha.resin")
    try:
        d=open(controlDict_file,"w")
    except:
        print("alpha.resin not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      alpha.resin;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 0 0 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform 0;\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            value uniform 1;  \n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            inletValue uniform 0;\n")
    d.write("            value uniform 0;\n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()

    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"alpha1_")
    try:
        d=open(controlDict_file,"w")
    except:
        print("alpha1_ not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      alpha1_;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 0 0 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform 0;\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            value uniform 1;\n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type advective;\n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()

    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"alpha1_out")
    try:
        d=open(controlDict_file,"w")
    except:
        print("alpha1_out not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      alpha1_out;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 0 0 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform 0;\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    d.write("            value uniform 1;\n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type advective;\n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()

    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"porosity_out")
    try:
        d=open(controlDict_file,"w")
    except:
        print("porosity not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      porosity;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 0 0 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform 1;\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("        type            zeroGradient;\n")
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()
    
    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"p_rgh")
    try:
        d=open(controlDict_file,"w")
    except:
        print("p_rgh not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volScalarField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      p_rgh;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [1 -1 -2 0 0 0 0];\n")
    d.write("\n")
    #d.write("internalField   uniform 0;\n")
    d.write("internalField   uniform "+ p_init.get() +";\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    if pWallType.get()=="Dynamic":
        d.write("    wall\n")
        d.write("    {\n")
        d.write("        type         codedMixed;\n")
        d.write("        refValue        uniform "+p_init.get()+";\n")
        d.write("        refGradient uniform 0.0;\n")
        d.write("        valueFraction uniform 1.0;\n")
        d.write("        name    myBC7;\n")
        d.write("        code\n")
        d.write("        #{\n")
        d.write('            const tmp<scalarField>& p=patch().lookupPatchField<volScalarField, scalar>("p").patchInternalField();\n')
        d.write('            const tmp<scalarField>& alpha1=patch().lookupPatchField<volScalarField, scalar>("alpha.resin").patchInternalField();\n')
        d.write("            const fvPatch& boundaryPatch = patch();\n")
        d.write("            const vectorField& Cf = boundaryPatch.Cf();\n")
        d.write("            scalarField& val=this->refValue();\n")
        d.write("            scalarField& grad=this->refGrad();\n")
        d.write("            scalarField& frac=this->valueFraction();\n")
        d.write("            scalar fracVal=1.0;\n")
        d.write("            forAll(Cf, faceI)\n")
        d.write("            {\n")
        d.write("                frac[faceI]=1.0-min(max(alpha1.ref()[faceI],0.0),1.0);  //linear transition\n")
        d.write("            }\n")
        d.write("        #};\n")
        d.write("    }\n")
    else:
        d.write("    wall\n")
        d.write("    {\n")
        d.write("        type            zeroGradient;\n")
        d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type fixedValue;\n")
    #d.write("            value uniform 2392;\n")
    d.write("            value uniform "+ p_inlet.get() +";\n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type totalPressure;\n")
    d.write("            p0 uniform "+ p_init.get() +";\n")    
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()    
    
    system_dir=dir_name3
    controlDict_file=os.path.join(system_dir,"U")
    try:
        d=open(controlDict_file,"w")
    except:
        print("U not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       volVectorField;\n")
    d.write('    location    "0";\n')    
    d.write("    object      U;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 1 -1 0 0 0 0];\n")
    d.write("\n")
    d.write("internalField   uniform (0 0 0);\n")
    d.write("\n")
    d.write("boundaryField\n")
    d.write("{\n")
    d.write("    wall\n")
    d.write("    {\n")
    d.write("        type            slip;\n")
    d.write("    }\n")
    d.write("    inlet\n")
    d.write("    {\n")
    d.write("            type pressureInletOutletVelocity;\n")
    d.write("            value uniform (0 0 0);\n")
    d.write("    }\n")
    d.write("    outlet\n")
    d.write("    {\n")
    d.write("            type pressureInletOutletVelocity;\n")
    d.write("            value uniform (0 0 0);\n")    
    d.write("    }\n")
    d.write("}\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()      

    #create constant folder
    system_dir=dir_name4
    controlDict_file=os.path.join(system_dir,"dynamicMeshDict")
    try:
        d=open(controlDict_file,"w")
    except:
        print("dynamicMeshDict not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "constant";\n')    
    d.write("    object      dynamicMeshDict;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dynamicFvMesh   staticFvMesh;\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()   

    system_dir=dir_name4
    controlDict_file=os.path.join(system_dir,"g")
    try:
        d=open(controlDict_file,"w")
    except:
        print("g not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "constant";\n')    
    d.write("    object      g;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("dimensions      [0 1 -2 0 0 0 0];\n")
    #d.write("value           ( 0 0 0 );  //( 0 0 -9.81 );\n")
    d.write("value           ( "+g1.get()+" "+g2.get()+" "+g3.get()+" );  //( 0 0 -9.81 );\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()   

    system_dir=dir_name4
    controlDict_file=os.path.join(system_dir,"porosityProperties")
    try:
        d=open(controlDict_file,"w")
    except:
        print("porosityProperties not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "constant";\n')    
    d.write("    object      porosityProperties;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("porosity1\n")
    d.write("{\n")
    d.write("    type            DarcyForchheimer;\n")
    d.write("    active          yes;\n")
    d.write("    cellZone        fluid;\n")
    #d.write("    porosity        0.868;\n")
    d.write("    porosity        "+fluid1_porosity.get()+";\n")
    d.write("    \n")
    d.write("    DarcyForchheimerCoeffs\n")
    d.write("    {\n")
    d.write("        d   ("+str(1/float(fluid1_permeability1.get()))+" "+str(1/float(fluid1_permeability2.get()))+" "+str(1/float(fluid1_permeability3.get()))+");\n")
    #d.write("        d   (9.69e7 48.45e7 1e9);\n")
    d.write("        f   (0 0 0);\n")
    d.write("        \n")
    d.write("        coordinateSystem\n")
    d.write("        {\n")
    d.write("            type    cartesian;\n")
    d.write("            origin  ("+fluid1_origin1.get()+" "+fluid1_origin3.get()+" "+fluid1_origin3.get()+");\n")
    #d.write("            origin  (0 0 0);\n")
    d.write("            rotation\n")
    d.write("            {\n")
    d.write("                type    axes;\n")
    d.write("                e1      ("+fluid1_e1_1.get()+" "+fluid1_e1_2.get()+" "+fluid1_e1_3.get()+");\n")
    #d.write("                e1      (1 0 0);\n")
    d.write("                e2      ("+fluid1_e2_1.get()+" "+fluid1_e2_2.get()+" "+fluid1_e2_3.get()+");\n")
    #d.write("                e2      (0 1 0);\n")
    d.write("            }\n")
    d.write("        }\n")
    d.write("    }\n")
    d.write("}\n")
    
    if fluid2.get()=="Used":
        d.write("\n")
        d.write("porosity2\n")
        d.write("{\n")
        d.write("    type            DarcyForchheimer;\n")
        d.write("    active          yes;\n")
        d.write("    cellZone        fluid2;\n")
        #d.write("    porosity        0.868;\n")
        d.write("    porosity        "+fluid2_porosity.get()+";\n")
        d.write("    \n")
        d.write("    DarcyForchheimerCoeffs\n")
        d.write("    {\n")
        d.write("        d   ("+str(1/float(fluid2_permeability1.get()))+" "+str(1/float(fluid2_permeability2.get()))+" "+str(1/float(fluid2_permeability3.get()))+");\n")
        #d.write("        d   (9.69e7 48.45e7 1e9);\n")
        d.write("        f   (0 0 0);\n")
        d.write("        \n")
        d.write("        coordinateSystem\n")
        d.write("        {\n")
        d.write("            type    cartesian;\n")
        d.write("            origin  ("+fluid2_origin1.get()+" "+fluid2_origin3.get()+" "+fluid2_origin3.get()+");\n")
        #d.write("            origin  (0 0 0);\n")
        d.write("            rotation\n")
        d.write("            {\n")
        d.write("                type    axes;\n")    
        d.write("                e1      ("+fluid2_e1_1.get()+" "+fluid2_e1_2.get()+" "+fluid2_e1_3.get()+");\n")
        #d.write("                e1      (1 0 0);\n")
        d.write("                e2      ("+fluid2_e2_1.get()+" "+fluid2_e2_2.get()+" "+fluid2_e2_3.get()+");\n")
        #d.write("                e2      (0 1 0);\n")
        d.write("            }\n")
        d.write("        }\n")
        d.write("    }\n")
        d.write("}\n")    
    
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()  

    system_dir=dir_name4
    controlDict_file=os.path.join(system_dir,"transportProperties")
    try:
        d=open(controlDict_file,"w")
    except:
        print("transportProperties not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "constant";\n')    
    d.write("    object      transportProperties;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("phases          (resin air);\n")
    d.write("\n")
    d.write("resin\n")
    d.write("{\n")
    d.write("    transportModel  Newtonian;\n")
    #d.write("    nu              nu [ 0 2 -1 0 0 0 0 ] 0.00007088;\n")
    d.write("    nu              nu [ 0 2 -1 0 0 0 0 ] "+nu_resin.get()+";\n")
    #d.write("    rho             rho [ 1 -3 0 0 0 0 0 ] 917;\n")
    d.write("    rho             rho [ 1 -3 0 0 0 0 0 ] "+rho_resin.get()+";\n")
    d.write("}\n")
    d.write("\n")
    d.write("air\n")
    d.write("{\n")
    d.write("    transportModel  Newtonian;\n")
    #d.write("    nu              nu [ 0 2 -1 0 0 0 0 ] 1.48e-05;\n")
    d.write("    nu              nu [ 0 2 -1 0 0 0 0 ] "+nu_air.get()+";\n")
    #d.write("    rho             rho [ 1 -3 0 0 0 0 0 ] 1.225;\n")
    d.write("    rho             rho [ 1 -3 0 0 0 0 0 ] "+rho_air.get()+";\n")
    d.write("}\n")
    d.write("\n")
    #d.write("sigma            sigma [ 1 0 -2 0 0 0 0 ] 0.0;   //0.07;\n")
    d.write("sigma            sigma [ 1 0 -2 0 0 0 0 ] "+sigma.get()+";   //0.07;\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()  

    system_dir=dir_name4
    controlDict_file=os.path.join(system_dir,"turbulenceProperties")
    try:
        d=open(controlDict_file,"w")
    except:
        print("turbulenceProperties not opened")
        sys.exit(0)
    d.write("\n")
    d.write("/*--------------------------------*- C++ -*----------------------------------*\\n")
    d.write("| =========                 |                                                 |\n")
    d.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
    d.write("|  \\    /   O peration     | Version:  2.3.0                                 |\n")
    d.write("|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
    d.write("|    \\/     M anipulation  |                                                 |\n")
    d.write("\*---------------------------------------------------------------------------*/\n")
    d.write("FoamFile\n")
    d.write("{\n")
    d.write("    format      ascii;\n")
    d.write("    class       dictionary;\n")
    d.write('    location    "constant";\n')    
    d.write("    object      turbulenceProperties;\n")
    d.write("}\n")
    d.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
    d.write("\n")
    d.write("simulationType  laminar;\n")
    d.write("\n")
    d.write("// ************************************************************************* //\n")
    d.close()  



root.mainloop()
