# ---------------------------------------- 
# file: main.py
# author: emirng
# ----------------------------------------

import colorsys
from glb_material_mesh_index import glb_material_mesh_index
from PIL import Image, ImageDraw


view_size = 800
color_type = 'MESH_INDEX'


def p3dto2d( vertex ):
    # projection method.
    # TODO: it has some hard coded transformations here. this should be done outside this method
    scale = 250 # TODO: remove scale from this method
    vertex = vertex * scale
    y,x,z = vertex # TODO: assing to x,y,z in correct order
    z = -z # TODO: remove this
    r = (
        x - y + view_size//2,
        x + y - z + view_size//2,
    )
    return r


with open('guy.glb', 'rb') as f:
    data = list( glb_material_mesh_index(f) )


# --- setup color lists
materials = set()
mesh_indexes = set()

for _, material, mesh_index in data:
    materials.add( material )
    mesh_indexes.add( mesh_index )

material_colors = []
for i in range(len(materials)):
    material_colors.append( tuple(
        [ int(c*255) for c in colorsys.hsv_to_rgb( (1/len( materials ))*i,1,1 )]))

mesh_index_colors = []
for i in range(len(mesh_indexes)):
    mesh_index_colors.append( tuple(
        [ int(c*255) for c in colorsys.hsv_to_rgb( (1/len( mesh_indexes ))*i,1,1 )]))
# ---


final_image = Image.new( 'RGB', (view_size,)*2, '#000000' ) 
drawer = ImageDraw.Draw( final_image )  


for face, material, mesh_index in data:
    if color_type == 'MATERIAL':
        color = material_colors[ material ]
    elif color_type == 'MESH_INDEX':
        color = mesh_index_colors[ mesh_index ]
    polygon = [ p3dto2d( vertex ) for vertex in face ]
    drawer.polygon( polygon , outline = color  ) 

final_image.show()


