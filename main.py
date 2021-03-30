from scripts import run_model, create_featvec, create_features, generatePSSMProfile, parse_raw_files

# Raw files for making compatible train-test data
raw_protein_train_file = './data/raw/TE_trainset.csv'
raw_protein_test_file = './data/raw/TE_testset.csv'

# interpreter and script file location for kernel features
kernel_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/r_kernels/bin/Rscript'
kernel_interpreter_loc2 = '/storage/home/dzb5732/.conda/envs/r_kernels/bin/Rscript'
kernel_script_loc = './external/kebabs/generate_kernel_features.R'

# interpreter and script file location for ifeature features
ifeature_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/prot-class/bin/python'
ifeature_interpreter_loc2 = '/storage/home/dzb5732/.conda/envs/prot-class/bin/python'
ifeature_script_loc = './external/ifeature/generate_ifeatures.py'

# interpreter location, uniref db loc, blast psi program loc, fasta file
uniref_db_loc = '~/work/iFeature/myData/uniref50/uniref50db'
blastpsi_loc = '/opt/aci/sw/ncbi-rmblastn/2.9.0_gcc-8.3.1-bxy/bin/psiblast'
output_dir = './data/features/possum/pssm_profiles/'
train_fasta_file = './data/seq/TrainEnzymeFasta.fa'
test_fasta_file = './data/seq/TestEnzymeFasta.fa'

# interpreter and script file location for possum features
possum_interpreter_loc = '/Users/dzb5732/opt/anaconda3/envs/possum-env/bin/python'
possum_interpreter_loc2 = '/storage/home/dzb5732/.conda/envs/possum-env/bin/python'
possum_script_loc = './external/possum/generate_possum_features.py'

# make ifeature vectors from ifeature files
ifeat_trainfile_loc = './data/features/ifeature/featfiles/train/'
ifeat_testfile_loc = './data/features/ifeature/featfiles/test/'

# make possum feature vectors from possum feature files
possum_trainfile_loc = './data/features/possum/featfiles/train/'
possum_testfile_loc = './data/features/possum/featfiles/test/'

# make kernel feature vectors from kernel feature files; kernels have only one directory for both train and test
kernel_file_loc = './data/features/kernel/featfiles/'

# files for running the model
# Sequence and label files
train_enz_file = './data/seq/TrainEnzymeSequence.csv'
label_file = './data/label/TrainEnzymeLabels.csv'

# Feature dir for iFeature,kernel,possum
ifeat_vec_dir = './data/features/ifeature/featvec/train/'
kernel_vec_dir = './data/features/kernel/featvec/train/'
possum_vec_dir = './data/features/possum/featvec/train/'

train_feat_vecs = [ifeat_vec_dir, kernel_vec_dir, possum_vec_dir]

if __name__ == '__main__':
#     parse_raw_files.make_train_test_data(raw_protein_train_file, raw_protein_test_file)
#     create_features.create_kernel_features(kernel_interpreter_loc2, kernel_script_loc)
#     create_features.create_ifeatures(ifeature_interpreter_loc2, ifeature_script_loc)
#     generatePSSMProfile.generatePSSMProfile(train_fasta_file, output_dir + '/train/', blastpsi_loc, uniref_db_loc)
#     generatePSSMProfile.generatePSSMProfile(test_fasta_file, output_dir + '/test/', blastpsi_loc, uniref_db_loc)
#     create_features.create_possum_features(possum_interpreter_loc2, possum_script_loc)
#     create_featvec.save_i_featvecs(ifeat_trainfile_loc)
#     create_featvec.save_i_featvecs(ifeat_testfile_loc)
#     create_featvec.save_possum_featvecs(possum_trainfile_loc, train_fasta_file)
#     create_featvec.save_possum_featvecs(possum_testfile_loc, test_fasta_file)
#     create_featvec.save_kernel_featvecs(kernel_file_loc)
    obj = run_model.get_te(train_enz_file, None, label_file, train_feat_vecs,  None, 'SVM', False, 10)
    print(obj.precision, obj.recall, obj.en.acc)


