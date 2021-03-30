from scripts import run_model
import time

# files for running the model
# Sequence and label files
train_enz_file = './data/seq/TrainEnzymeSequence.csv'
label_file = './data/label/TrainEnzymeLabels.csv'

# Feature dir for iFeature,kernel,possum
ifeat_vec_dir = './data/features/ifeature/featvec/train/'
kernel_vec_dir = './data/features/kernel/featvec/train/'
possum_vec_dir = './data/features/possum/featvec/train/'

train_feat_vecs = [ifeat_vec_dir, kernel_vec_dir, possum_vec_dir]

start_time = time.time()
mean_mets = run_model.check_performance(train_enz_file, None, label_file, train_feat_vecs, None, 'SVM', False, 10000)
end_time = time.time()
print(mean_mets)
print(f"Time required to generate results is: {end_time-start_time} seconds")
