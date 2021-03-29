from scripts import create_features #generatePSSMProfile #parse_raw_files, create_features

# Raw files for making compatible train-test data
raw_protein_train_file = './data/raw/trainfile.csv'
raw_protein_test_file = './data/raw/testfile.csv'

# interpreter and script file location for kernel features
kernel_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/r_kernels/bin/Rscript'
kernel_script_loc = './external/kebabs/generate_kernel_features.R'

# interpreter and script file location for ifeature features
ifeature_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/prot-class/bin/python'
ifeature_interpreter_loc2 = '/storage/home/dzb5732/.conda/envs/prot-class/bin/python'
ifeature_script_loc = './external/ifeature/generate_ifeatures.py'

# interpreter location, uniref db loc, blast psi program loc, fasta file
uniref_db_loc = '~/work/iFeature/myData/uniref50/uniref50db'
blastpsi_loc = '/opt/aci/sw/ncbi-rmblastn/2.9.0_gcc-8.3.1-bxy/bin/psiblast'
outputdir = './data/features/possum/pssm_profiles/'
train_fasta_file = './data/seq/TrainEnzymeFasta.fa'
test_fasta_file = './data/seq/TestEnzymeFasta.fa'

if __name__ == '__main__':
#    pass

#    parse_raw_files.make_train_test_data(raw_protein_train_file, raw_protein_test_file)
#    create_features.create_kernel_features(kernel_interpreter_loc, kernel_script_loc)
    create_features.create_ifeatures(ifeature_interpreter_loc2, ifeature_script_loc)
#    generatePSSMProfile.generatePSSMProfile(train_fasta_file, outputdir + '/train/', blastpsi_loc, uniref_db_loc)
#    generatePSSMProfile.generatePSSMProfile(test_fasta_file, outputdir + '/test/', blastpsi_loc, uniref_db_loc)

