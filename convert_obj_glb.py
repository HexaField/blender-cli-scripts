# Convert .obj files to .glb files. Usage:
# blender --background --python ./convert_obj_glb.py -- <directory>

import bpy
import sys
import os

def deleteAllObjects():
    """
    Deletes all objects in the current scene
    """
    deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                     'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

    # Select all objects in the scene to be deleted:

    for o in bpy.context.scene.objects:
        for i in deleteListObjects:
            if o.type == i:
                o.select_set(False)
            else:
                o.select_set(True)
    # Deletes all selected objects in the scene:

    bpy.ops.object.delete() 



# Get all args after "--"
argv = sys.argv
argv = argv[argv.index("--") + 1:]

directory = argv[0]

files = os.listdir(directory)
files = [f for f in files if os.path.isfile(directory+'/'+f) and f.endswith('.obj')]

# prints all files
print("Converting files:", files)

for f in files:
    # reset
    deleteAllObjects()
    # import obj and export as glb
    obj_in = directory + '/' + f
    gltf_out = directory + '/' + f.split('.')[0] + '.glb'
    bpy.ops.wm.obj_import(filepath=obj_in, forward_axis='NEGATIVE_Z', up_axis='Y')
    bpy.ops.export_scene.gltf(filepath=gltf_out)
    print('Converted', obj_in, 'to', gltf_out)
