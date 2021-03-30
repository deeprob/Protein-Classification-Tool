from model.classifier import TEClassification


def get_te(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, rs, base_algo, opt):
    te = TEClassification(enz_file, test_enz_file, label_file, train_feat_dirs, test_feat_dirs, random_seed=rs,
                          model=base_algo, optimize=opt)
    return te
