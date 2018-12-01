import bpy
import bmesh
import ps2_bonedic
# vertex group translator
# takes the names of Planetside 2 ARMOR rig vertex groups and 
# creates copies for Manuel Bastiony Labs(1.6) rigs

def params_check():
    
    choice = bpy.context.selected_objects
    
    if (len(choice)!=1):
        print("wrong amount of params " + len(choice) + " given")    
        return False
    
    ob = choice[0]
    
    if ob.type!="ARMATURE":
        print("selected item " + ob.name + " is not a rig")
        return False
    
    return ob        
    
# helper of list_all        
def list_children(C):
    
    for ch in C.children:
        print(ch.name)

# helper of list_all
def list_bones(C):
    
    for bo in C.data.bones:
        print(bo.name)

def list_vertex_weightgroups(C):
    vg_dic = ps2_bonedic.rig_dict
    mesh_orig = C.children[0]
    #new_mesh =mesh_orig.copy()
    print(len(mesh_orig.vertex_groups))
    newname ="";
    #new_mesh = "";
    if ( len(mesh_orig.vertex_groups) > 0 ):
        for vg in mesh_orig.vertex_groups:
            
            print("Name: {}, index:{} ".format(vg.name, vg.index))
            
            for dic_v in vg_dic.values():
                if vg.name in dic_v:
                    
                    newname=list(vg_dic.keys())[list(vg_dic.values()).index(dic_v)]
                    vg.name = newname
                    """
                    print(newname)
                    if (newname == dic_v):
                        print("NO CHANGE TO WRITE")
            
            for i, v in enumerate(C.children[0].data.vertices):
                for vgs in v.groups:
                    if (vg.index==vgs.group):
                        
                        obj_v = vgs.weight
                        v_index = v.index
                        
                        if (newname != dic_v):
                            new_vg = mesh_orig.vertex_groups.get(newname)
                            
                        if (new_vg == None):
                            new_vg = mesh_orig.vertex_groups.new(newname)
                        new_vg.add([i], vgs.weight, 'REPLACE')       
                            
                        print("V Index in mesh: " + str(i)+
                       "Vector weight for group: " +  vg.name +
                        " ! " + str(vgs.weight)) 
                        """

    print(ps2_bonedic.rig_dict)
                    

def list_all():
    C=params_check();
    if ( C !=False ):
    
        print(C.name + "  | " + C.type)
        print("---------------------------------")
        list_children(C)
        print("---------------------------------")
        list_bones(C)
        print("---------------------------------")
        list_vertex_weightgroups(C)
        print("---------------------------------")
        
                


#Prerequisites
list_all() # verbose, can just use params_check()
#get both rigs identified

#build a dictionarty of 'old_name':'new_name' entries

#get the mesh of the PS2fbx armor character

#get a list of the Weights

#append a list of new names with old weights

#change the parent of the PS2fbx mesh

