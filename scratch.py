from scripts import deep

print(type(deep))

interpreter_path = '/Users/dzb5732/opt/anaconda3/envs/prot-class/bin/python'
script_path = './external/possum/generate_possum_features.py'

deep.create_script(interpreter_path, script_path)