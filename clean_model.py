import h5py

# This script removes the 'groups' argument that crashes Keras 3
input_file = 'keras_model.h5'
output_file = 'keras_model_fixed.h5'

with h5py.File(input_file, 'r') as f:
    # Get the model configuration string
    model_config = f.attrs.get('model_config')
    if isinstance(model_config, bytes):
        model_config = model_config.decode('utf-8')

    # Remove the 'groups': 1 argument that causes the crash
    fixed_config = model_config.replace('"groups": 1,', '')
    fixed_config = fixed_config.replace('"groups": 1', '')

# Create a copy with the new configuration
import shutil
shutil.copy(input_file, output_file)

with h5py.File(output_file, 'a') as f:
    f.attrs.modify('model_config', fixed_config.encode('utf-8'))

print("Success! Created 'keras_model_fixed.h5'. Now update your Teach.py to use this new file.")
