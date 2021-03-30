from codes import possum

train_fasta_file = './data/seq/TrainEnzymeFasta.fa'
test_fasta_file = './data/seq/TestEnzymeFasta.fa'
pssm_profile_dir = './data/features/possum/pssm_profiles/'
output_dir = './data/features/possum/featfiles/'

feat_types = ('aac_pssm', 'd_fpssm', 'smoothed_pssm', 'ab_pssm', 'pssm_composition', 'rpm_pssm', 's_fpssm', 'dpc_pssm',
              'k_separated_bigrams_pssm', 'tri_gram_pssm', 'eedp', 'tpc', 'edp', 'rpssm', 'pse_pssm', 'dp_pssm',
              'pssm_ac', 'pssm_cc', 'aadp_pssm', 'aatp', 'medp')

argument_dict = {ft: 0 for ft in feat_types}
variable_dict = {ft: 0 for ft in feat_types}

# set the default values for some of feature types from possum documentation
argument_dict['smoothed_pssm'] = 7
variable_dict['smoothed_pssm'] = 50
argument_dict['k_separated_bigrams_pssm'] = 1
argument_dict['pse_pssm'] = 1
argument_dict['dp_pssm'] = 5
argument_dict['pssm_ac'] = 10
argument_dict['pssm_cc'] = 10


def get_feature(fasta_file, output_file, feature_type, pssm_dir, argument, variable):
    possum.feat_possum(fasta_file, output_file, feature_type, pssm_dir, argument, variable)
    return


def get_features(fasta_file, output_dir_suffix):
    for ft in feat_types:
        print ft
        get_feature(fasta_file, output_dir + output_dir_suffix + ft + '.csv', ft, pssm_profile_dir + output_dir_suffix,
                    argument_dict[ft], variable_dict[ft])
    return


get_features(train_fasta_file, 'train/')
get_features(test_fasta_file, 'test/')
