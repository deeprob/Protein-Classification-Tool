from scripts import parse_raw_files, create_features


raw_protein_train_file = './data/raw/trainfile.csv'
raw_protein_test_file = './data/raw/testfile.csv'
kernel_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/r_kernels/bin/Rscript'
kernel_script_loc = './external/kebabs/generate_kernel_features.R'
ifeature_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/prot-class/bin/python'
ifeature_script_loc = './external/ifeature/generate_ifeatures.py'

if __name__ == '__main__':
    create_features.create_ifeatures(ifeature_interpreter_loc, ifeature_script_loc)
#    parse_raw_files.make_train_test_data(raw_protein_train_file, raw_protein_test_file)
#    create_features.create_kernel_features(kernel_interpreter_loc, kernel_script_loc)

