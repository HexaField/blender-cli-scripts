# Convert .obj files to .glb files. Usage:
# blender --background --python ./convert.py -- <directory>

import bpy
import sys
import os

# Get all args after "--"
argv = sys.argv
argv = argv[argv.index("--") + 1:]

directory = argv[0]

files = os.listdir(directory)
files = [f for f in files if os.path.isfile(directory+'/'+f) and f.endswith('.obj')]

# prints all files
print("Converting files:", files)

for f in files:
    bpy.ops.scene.new(type='EMPTY')
    obj_in = directory + '/' + f
    gltf_out = directory + '/' + f.split('.')[0] + '.glb'
    bpy.ops.wm.obj_import(filepath=obj_in, forward_axis='NEGATIVE_Z', up_axis='Y')
    bpy.ops.export_scene.gltf(filepath=gltf_out)
    print('Converted', obj_in, 'to', gltf_out)
