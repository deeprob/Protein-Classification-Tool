import pandas as pd


# make all the sequences upper and get rid of any '-' between sequences
def up_seq(seq_string):
    return seq_string.upper().replace('-', '')


def make_train_test_data(raw_train_datafile, raw_test_datafile, output_dir="./data/"):
    """Files created:
    - 1 csv file with train_enz_alias,train_enz_sequence; stored in dir data/seq
    - 1 csv file with test_enz_alias,test_enz_sequence; stored in dir data/seq
    - 1 csv files with enz_alias,enz_labels; stored in dir data/labels
    - 1 csv file with train_enz_alias,train_enz_name mapping; stored in dir data/mappings
    - 1 csv file with test_enz_alias,test_enz_name mapping; stored in dir data/mappings
    - 1 Fasta file with header as train_enz_alias and second line as train_enz_sequence; stored in dir data/seq
    - 1 Fasta file with header as test_enz_alias and second line as test_enz_sequence; stored in dir data/seq
    - 1 Fasta file with header as train/test_enz_alias and second lines as train/test_enz_sequence
    to be used by kebabs; stored in dir data/seq"""

    raw_train_df = pd.read_csv(raw_train_datafile, header=None)
    raw_test_df = pd.read_csv(raw_test_datafile, header=None)

    raw_train_df.columns = ['enzNames', 'sequence', 'label']
    raw_test_df.columns = ['enzNames', 'sequence']

    raw_train_df['sequence'] = raw_train_df.sequence.apply(up_seq)
    raw_test_df['sequence'] = raw_test_df.sequence.apply(up_seq)

    # get rid of sequences with values in 'B', 'J', 'O', 'U', 'X' and 'Z'
    train_df = raw_train_df.loc[~raw_train_df['sequence'].str.contains('B|J|O|U|X|Z')]
    test_df = raw_test_df.loc[~raw_test_df['sequence'].str.contains('B|J|O|U|X|Z')]

    # give enz_alias
    enz_alias_train = [f'enz_{i}' for i in range(len(train_df['enzNames']))]
    train_df = train_df.assign(enzAlias=enz_alias_train)
    enz_alias_test = [f'test_enz_{i}' for i in range(len(test_df['enzNames']))]
    test_df = test_df.assign(enzAlias=enz_alias_test)

    # save the csv sequence file
    train_df.loc[:, ['enzAlias', 'sequence']].to_csv(output_dir + 'seq/TrainEnzymeSequence.csv',
                                                     header=None, index=None)
    test_df.loc[:, ['enzAlias', 'sequence']].to_csv(output_dir + 'seq/TestEnzymeSequence.csv',
                                                    header=None, index=None)

    # save the csv label files
    train_df.loc[:, ['enzAlias', 'label']].to_csv(output_dir + 'label/TrainEnzymeLabels.csv',
                                                  header=None, index=None)

    # save the enzyme name mappings
    train_df.loc[:, ['enzAlias', 'enzNames']].to_csv(output_dir + 'mappings/EnzymeNameMap.csv',
                                                     header=None, index=None)
    test_df.loc[:, ['enzAlias', 'enzNames']].to_csv(output_dir + 'mappings/TestEnzymeNameMap.csv',
                                                    header=None, index=None)

    # create Fasta file train
    with open(output_dir + 'seq/TrainEnzymeFasta.fa', 'w') as f:
        for enz_alias, enz_seq in zip(train_df.enzAlias, train_df.sequence):
            f.write('>' + enz_alias)
            f.write('\n')
            f.write(enz_seq + '\n')

    # create Fasta file test
    with open(output_dir + 'seq/TestEnzymeFasta.fa', 'w') as f:
        for enz_alias, enz_seq in zip(test_df.enzAlias, test_df.sequence):
            f.write('>' + enz_alias)
            f.write('\n')
            f.write(enz_seq + '\n')

    # create Fasta file combined
    with open(output_dir + 'seq/CombinedEnzymeFasta.fa', 'w') as f:
        for enz_alias, enz_seq in zip(train_df.enzAlias, train_df.sequence):
            f.write('>' + enz_alias)
            f.write('\n')
            f.write(enz_seq + '\n')

        for enz_alias, enz_seq in zip(test_df.enzAlias, test_df.sequence):
            f.write('>' + enz_alias)
            f.write('\n')
            f.write(enz_seq + '\n')
    return
