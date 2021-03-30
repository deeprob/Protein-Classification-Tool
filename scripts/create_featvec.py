import os
import re
import pandas as pd
from scipy import sparse, io
import numpy as np


def save_i_featvec(data_file_dir, output_file_dir, feat_file):
    df = pd.read_csv(data_file_dir+feat_file, header=None, skiprows=1, sep='\t')
    df = df.set_index(0)
    df.to_csv(output_file_dir+feat_file.replace('.tsv', '.csv.gz'), index=True, header=False,
              compression='gzip')
    return


def save_i_featvecs(ifeat_file_dir):
    output_file_dir = re.sub('featfiles', 'featvec', ifeat_file_dir)
    for file in os.scandir(ifeat_file_dir):
        if file.name.endswith('.tsv'):
            save_i_featvec(ifeat_file_dir, output_file_dir, file.name)
    return


def get_enzyme_names(fasta_file):
    enz_names = []
    with open(fasta_file, 'r') as f:
        for lines in f:
            if lines.startswith('>'):
                enz_name = lines.replace('>', '').rstrip()
                enz_names.append(enz_name)
    return enz_names


def save_possum_featvec(data_file_dir, output_file_dir, feat_file, fasta_file):
    df = pd.read_csv(data_file_dir + feat_file, header=None)
    names = get_enzyme_names(fasta_file)
    df['index'] = names
    df = df.set_index('index')
    df.to_csv(output_file_dir + feat_file + '.gz', index=True, header=False, compression='gzip')
    return


def save_possum_featvecs(possum_file_dir, fasta_file):
    output_file_dir = re.sub('featfiles', 'featvec', possum_file_dir)

    for file in os.scandir(possum_file_dir):
        if file.name.endswith('.csv'):
            save_possum_featvec(possum_file_dir, output_file_dir, file.name, fasta_file)
    return


def save_kernel_featvec(kernel_file_dir, output_file_dir, file_prefix):
    sp_mat_file = kernel_file_dir + file_prefix + '_kern_sparsematrix.txt'
    enz_name_file = kernel_file_dir + file_prefix + '_kern_rownames.txt'
    sp_mat = io.mmread(sp_mat_file).tocsr()
    enz_names = np.genfromtxt(enz_name_file, dtype=str)

    train_enz_idx = []
    test_enz_idx = []

    for idx, enz_name in enumerate(enz_names):
        if enz_name.startswith('enz'):
            train_enz_idx.append(idx)
        elif enz_name.startswith('test'):
            test_enz_idx.append(idx)
        else:
            raise ValueError('Wrong Enzyme Prefix')

    X_train, X_test = sp_mat[train_enz_idx, :], sp_mat[test_enz_idx, :]
    enz_names_train, enz_names_test = enz_names[train_enz_idx], enz_names[test_enz_idx]

    assert X_train.shape[0] == len(enz_names_train)
    assert X_test.shape[0] == len(enz_names_test)

    sparse.save_npz(output_file_dir + 'train/' + file_prefix + 'mat.npz', X_train)
    sparse.save_npz(output_file_dir + 'test/' + file_prefix + 'mat.npz', X_test)

    np.savetxt(output_file_dir + 'train/' + file_prefix + 'enz_names.txt', enz_names_train, fmt='%s')
    np.savetxt(output_file_dir + 'test/' + file_prefix + 'enz_names.txt', enz_names_test, fmt='%s')
    return


def save_kernel_featvecs(kernel_file_dir):
    output_file_dir = re.sub('featfiles', 'featvec', kernel_file_dir)
    file_prefixes = ['spec', 'gap', 'mism']
    for fp in file_prefixes:
        save_kernel_featvec(kernel_file_dir, output_file_dir, fp)
    return
