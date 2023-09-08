# glb_material_mesh_index

This project provides a method that loads a complete mesh from a GLB-file. Beside the mesh it also provides data for materials and inner meshes within the complete mesh.

## The glb_material_mesh_index-method
The glb_material_mesh_index-method can be found in glb_material_mesh_index.py. It takes a io.BufferedReader as argument (or anything with a similar interface).
It returns a numpy-array float3d-(n ,3, 3) that contain all the trigons on the mesh. It also returns a material list and a mesh-index list. All lists are ordered and the order corresponds to the same item in all lists.

## viewer.py
The viewer.py is a script is just a showcase. The The glb_material_mesh_index is not depended on this script.

## Setup
Recommended setup. This setup makes it so everything works including the viewer.py. If you are just in need of the glb_material_mesh_index-method skip this setup and just install numpy.
```
cd <to project folder>
python3 -m virtualenv env
source env/bin/active
pip install -r requirements
```

## Run the viewer.py
(Based on the recommended setup above)
```
cd <to project folder>
source env/bin/active
python3 viewer.py
```

![image](https://github.com/emirng/glb_material_mesh_index/assets/135670768/f9b90d06-542a-4078-b97b-9a9c09f97958)
*Showcase for material based colors. Each Material has its own color*

![image](https://github.com/emirng/glb_material_mesh_index/assets/135670768/62a7ed8b-d176-4a40-805c-642e5714bf56)
*Showcase for mesh based color. Each mesh has its own color. (According to the GLB-file Left leg is its own mesh, Right arm is its own mesh and so on...)
