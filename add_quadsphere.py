import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty

bl_info = {
    "name": "Quadsphere",
    "description": "Turn a cube into a sphere with proper quad topology. Shift+A to add.. ",
    "author": "Tijl Prinssen",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "VIEW3D > Add > Mesh",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh"
    }


class QS_OP_add_quadsphere(bpy.types.Operator):
    bl_idname =  "mesh.quadsphere_add"
    bl_label =  "Quadsphere"
    bl_description =  "Add a sphere with proper quad topology"
    bl_options =  {'REGISTER', 'UNDO'}

    size: FloatProperty(
        name = "Size",
        description = "Size",
        default = 2.0,
        min = 0.1,
        soft_max = 10
    )
 
    apply_modifiers: BoolProperty(
        name =  "Apply Modifiers",
        description =  "Make mesh real",
        default = False
    )

    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "size")    
        
        # layout.prop(self, "show_wire")

        layout.separator()            
        layout.prop(self, "apply_modifiers", icon="CHECKMARK")


    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=self.size, calc_uvs=True, align='WORLD')
        bpy.ops.object.modifier_add(type='SUBSURF')
        context.active_object.modifiers["Subdivision"].levels = 4
        bpy.ops.object.modifier_add(type='CAST')
        context.active_object.modifiers["Cast"].factor = 1
        bpy.ops.object.shade_smooth()

        # if self.show_wire:
        
        if self.apply_modifiers:
            bpy.ops.object.modifier_apply(modifier="Subdivision")
            bpy.ops.object.modifier_apply(modifier="Cast")

        return {'FINISHED'}


def add_quadsphere_to_menu(self, context):
    self.layout.operator('mesh.quadsphere_add', text="Quadsphere", icon="SPHERE")
  

classes = {
    QS_OP_add_quadsphere,
}

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.append(add_quadsphere_to_menu)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_quadsphere_to_menu)
