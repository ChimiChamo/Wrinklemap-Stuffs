import bpy

# Select the active object (assuming the object is selected in the viewport)
obj = bpy.context.object

# Ensure the object has shape keys
if obj and obj.data.shape_keys:
    shape_keys = obj.data.shape_keys.key_blocks
    
    # Iterate through all the shape keys
    for shape_key in shape_keys:
        # Check if the name ends with 'L' and does not contain 'AD'
        if shape_key.name.endswith('L') and 'AD' not in shape_key.name:
            # Remove the 'L' from the end
            new_name = shape_key.name[:-1]
            print(f"Renaming {shape_key.name} to {new_name}")
            
            # Rename the shape key
            shape_key.name = new_name
        else:
            print(f"Skipping {shape_key.name}")
else:
    print("No shape keys found on the active object.")
