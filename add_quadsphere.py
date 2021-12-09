import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty, FloatVectorProperty

bl_info = {
    "name": "Quadsphere",
    "description": "Turn a cube into a sphere with proper quad topology. Shift+A to add.. ",
    "author": "Tijl Prinssen",
    "version": (0, 3, 0),
    "blender": (2, 80, 0),
    "location": "VIEW3D > Add > Mesh",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh"
    }


class QS_OP_add_quadsphere(bpy.types.Operator):
    bl_idname =  "mesh.quadsphere_add"
    bl_label =  "Quadsphere"
    bl_description =  """Add a sphere with proper quad topology"""
    bl_options =  {'REGISTER', 'UNDO'}

    size: FloatProperty(
        name = "Size",
        description = "Size",
        default = 2.0,
        min = 0.01,
        soft_max = 5
    )
    subdiv_level: IntProperty(
        name = "Subdivisions",
        description="Levels of Subdivision",
        default=4,
        min=0,
        soft_max=6,
        max=10
    )
    apply_modifiers: BoolProperty(
        name =  "Apply Modifiers",
        description =  "Make mesh real",
        default = False
    )

    

    
    def draw(self, context):
        layout = self.layout
        obj = context.object   
        view = context.space_data      

        layout.prop(self, "size")    
        layout.prop(self, "subdiv_level")    
        
        layout.separator()
        
        row = layout.row()
        # row.prop(self, 'align')
        # row.prop(self, "object_color")
        row.operator("wm.set_viewport_color", text="Viewport Color", icon="MATERIAL")
        row.prop(self, "apply_modifiers", icon="CHECKMARK")


    def execute(self, context):
        # add cube
        bpy.ops.mesh.primitive_cube_add(size=self.size, calc_uvs=True)

        # set subdiv 
        object = context.object
        self.add_subdivision_modifier(object, self.subdiv_level)

        # set render subdiv levels equal to viewport
        subdiv_levels = context.active_object.modifiers["Subdivision"].levels         
        context.active_object.modifiers["Subdivision"].render_levels = subdiv_levels

        # cast to sphere
        bpy.ops.object.modifier_add(type='CAST')
        context.active_object.modifiers["Cast"].factor = 1
        bpy.ops.object.shade_smooth()

           
        # apply modifiers
        if self.apply_modifiers:
            bpy.ops.object.modifier_apply(modifier="Subdivision")
            bpy.ops.object.modifier_apply(modifier="Cast")

        return {'FINISHED'}



    def add_subdivision_modifier(self, object, subdiv_level):
        mod = object.modifiers.new(name="Subdivision", type="SUBSURF")
        mod.subdivision_type = 'CATMULL_CLARK'
        mod.levels = subdiv_level



class QS_OP_add_shader(bpy.types.Operator):
    bl_idname =  "wm.set_viewport_color" 
    bl_label = "Viewport Color"
    bl_options = {'REGISTER', 'UNDO'}

    object_color : FloatVectorProperty(
        name='Color',
        subtype='COLOR_GAMMA',
        size=4,
        default=(0.5, 0.5, 0.5, 1), 
        min= 0, 
        max= 1
    )
    object_metallic: FloatProperty(
    name = "Metallic",
    description = "Metallic factor, should be set to either 0 or 1 for realism",
    default = 0,
    min = 0,
    max = 1
    )
    object_specular: FloatProperty(
    name = "Specular",
    description = "Amount of specularity",
    default = 0,
    min = 0,
    max = 1
    )
    object_roughness: FloatProperty(
    name = "Roughness",
    description = "Amount of roughness",
    default = 0,
    min = 0,
    max = 1
    )

    def execute(self, context): 
        # object.data.materials.append(mat)
        # create viewport material
        object = bpy.context.active_object
        mat = bpy.data.materials.new(name="Material")
        mat.use_nodes = False
        bpy.context.object.active_material = mat
        object.active_material.diffuse_color = self.object_color
        object.active_material.metallic = self.object_metallic
        object.active_material.specular_intensity = self.object_specular
        object.active_material.roughness = self.object_roughness

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width= 210)




def add_quadsphere_to_menu(self, context):
    self.layout.operator('mesh.quadsphere_add', text="Quadsphere", icon="SPHERE")
  

classes = {
    QS_OP_add_shader,
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
