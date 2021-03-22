# Protein Classification Tool
## Description
A python-based Machine Learning tool to classify protein sequences into their respective functional groups. 
This package is particularly suited for small to medium sized datasets with high sequence similarity.
It uses three external packages to generate 47 types of features for a given training set of protein sequences:

1. iFeature: *provide link* 
2. Kebabs: *provide link*
3. POSSUM: *provide link*

After generating features, 47 different base models are trained using one of the three specified learning algorithms 
(SVM, GBC, NN) to create 47 base classifiers. The classifiers are used to predict the labels of uncharacterized protein 
sequences provided in the test set. Each classifier predicts a particular class for a given sequence. The predictions of
the base models are them combined by a hard voting based meta learner that outputs the final model predicted functional
group of the uncharacterized protein sequence.

 ## Installation
 To install the tool, please clone the repository using git. 
 Example command: Enter "git clone <repo-link>" in your terminal.
 
 ## Setup
 The tool uses three different conda environments to manage the three external packages required for feature extraction.
 The base package environment file is present in the root directory of the package. The two other environment files are:
 
 1. external/kebabs/environment.yml
 2. external/possum/environment.yml
 
 Before using the tool, the user must follow the steps given below:
 
 0. change directory to the root directory of the package
 Command: cd <path to directory>/Protein-Classification-Tool/
 1. create a conda environment using the environment.yml file given in the root directory of this package.
 Command: conda create -f environment.yml
 2. create a conda environment using the environment.yml file given in the external/kebabs directory of this package.
 Command: conda create -f external/kebabs/environment.yml
 3. create a conda environment using the environment.yml file given in the root directory of this package.
 Command: conda create -f external/possum/environment.yml
 4.     