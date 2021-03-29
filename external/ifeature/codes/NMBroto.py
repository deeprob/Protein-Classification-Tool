import re
import numpy as np
from . import checkFasta


def NMBroto(fastas, props=['CIDH920105', 'BHAR880101', 'CHAM820101', 'CHAM820102',
										 'CHOC760101', 'BIGC670101', 'CHAM810101', 'DAYM780201'],
				nlag = 30, **kw):
	if checkFasta.minSequenceLengthWithNormalAA(fastas) < nlag + 1:
		print('Error: all the sequence length should be larger than the nlag+1: ' + str(nlag + 1) + '\n\n')
		return 0

	AA = 'ARNDCQEGHILKMFPSTWYV'
	fileAAidx = './external/ifeature/data/AAidx.txt'
	with open(fileAAidx) as f:
		records = f.readlines()[1:]
	myDict = {}
	for i in records:
		array = i.rstrip().split('\t')
		myDict[array[0]] = array[1:]

	AAidx = []
	AAidxName = []
	for i in props:
		if i in myDict:
			AAidx.append(myDict[i])
			AAidxName.append(i)
		else:
			print('"' + i + '" properties not exist.')
			return None

	AAidx1 = np.array([float(j) for i in AAidx for j in i])
	AAidx = AAidx1.reshape((len(AAidx),20))
	pstd = np.std(AAidx, axis=1)
	pmean = np.average(AAidx, axis=1)

	for i in range(len(AAidx)):
		for j in range(len(AAidx[i])):
			AAidx[i][j] = (AAidx[i][j] - pmean[i]) / pstd[i]

	index = {}
	for i in range(len(AA)):
		index[AA[i]] = i

	encodings = []
	header = ['#']
	for p in props:
		for n in range(1, nlag + 1):
			header.append(p + '.lag' + str(n))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		code = [name]
		N = len(sequence)
		for prop in range(len(props)):
			for n in range(1, nlag + 1):
				if len(sequence) > nlag:
					# if key is '-', then the value is 0
					rn = sum([AAidx[prop][index.get(sequence[j], 0)] * AAidx[prop][index.get(sequence[j + n], 0)] for j in range(len(sequence)-n)]) / (N - n)
				else:
					rn = 'NA'
				code.append(rn)
		encodings.append(code)
	return encodings
