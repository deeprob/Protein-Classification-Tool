import numpy as np
import multiprocessing as mp
from model.classifier import TEClassification


def get_te(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, base_algo, opt, rs):
    te = TEClassification(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, random_seed=rs,
                          model=base_algo, optimize=opt)
    return te


def check_base_performance(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, base_algo, opt, rs):
    te = get_te(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, base_algo, opt, rs)
    return te.precision, te.recall, te.en.acc


def check_performance(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, base_algo, opt, N):
    pool = mp.Pool(mp.cpu_count())
    
    iter_svm = zip([enz_file for _ in range(N)],
                   [test_enz_file for _ in range(N)],
                   [label_file for _ in range(N)],
                   [train_feat_dirs for _ in range(N)],
                   [test_feat_dirs for _ in range(N)],
                   [base_algo for _ in range(N)],
                   [opt for _ in range(N)],
                   range(N))
    
    metrics = pool.starmap(check_base_performance,iter_svm)
    
    precision = [m[0] for m in metrics]
    recall = [m[1] for m in metrics]
    accuracy = [m[2] for m in metrics]
    
    return round(np.mean(precision),2), round(np.mean(recall),2), round(np.mean(accuracy),2)
