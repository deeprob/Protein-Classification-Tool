from codes import readFasta, saveCode, AAC, CKSAAP, TPC, DPC, DDE, GAAC, CKSAAGP, GTPC, GDPC, Moran,\
	Geary, NMBroto, CTDC, CTDT, CTDD, CTriad, KSCTriad, SOCNumber, QSOrder, PAAC, APAAC


train_fasta_file = './data/seq/TrainEnzymeFasta.fa'
test_fasta_file = './data/seq/TestEnzymeFasta.fa'
feat_types = ('AAC', 'CKSAAP', 'TPC', 'DPC', 'DDE', 'GAAC', 'CKSAAGP', 'GTPC', 'GDPC', 'Moran', 'Geary', 'NMBroto',
			  'CTDC', 'CTDT', 'CTDD', 'CTriad', 'KSCTriad', 'SOCNumber', 'QSOrder', 'PAAC', 'APAAC')


def get_feature(protein_fasta_file, feature_type, output_dir):
	fastas = readFasta.readFasta(protein_fasta_file)
	userDefinedOrder = 'ACDEFGHIKLMNPQRSTVWY'
	myAAorder = {
		'alphabetically': 'ACDEFGHIKLMNPQRSTVWY',
		'polarity': 'DENKRQHSGTAPYVMCWIFL',
		'sideChainVolume': 'GASDPCTNEVHQILMKRFYW',
		'userDefined': userDefinedOrder
	}

	myOrder = 'ACDEFGHIKLMNPQRSTVWY'
	kw = {'order': myOrder}

	myFun = f"{feature_type}.{feature_type}(fastas, **kw)"
	print('Descriptor type: ' + feature_type)
	encodings = eval(myFun)
	outFile = f'{output_dir}{feature_type}.tsv'
	saveCode.savetsv(encodings, outFile)
	return


def get_features():
	out_dir_prefix = './data/features/ifeature/featfiles/'
	for ft in feat_types:
		get_feature(train_fasta_file, ft, out_dir_prefix+'train/')
		get_feature(test_fasta_file, ft, out_dir_prefix+'test/')
	return


get_features()
