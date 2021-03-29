import re
import numpy as np
from . import checkFasta


def Moran(fastas, props=['CIDH920105', 'BHAR880101', 'CHAM820101', 'CHAM820102',
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
	AAidx = AAidx1.reshape((len(AAidx), 20))

	propMean = np.mean(AAidx,axis=1)
	propStd = np.std(AAidx, axis=1)

	for i in range(len(AAidx)):
		for j in range(len(AAidx[i])):
			AAidx[i][j] = (AAidx[i][j] - propMean[i]) / propStd[i]

	index = {}
	for i in range(len(AA)):
		index[AA[i]] = i

	encodings = []
	header = ['#']
	for p in props:
		for n in range(1, nlag+1):
			header.append(p + '.lag' + str(n))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		code = [name]
		N = len(sequence)
		for prop in range(len(props)):
			xmean = sum([AAidx[prop][index[aa]] for aa in sequence]) / N
			for n in range(1, nlag + 1):
				if len(sequence) > nlag:
					# if key is '-', then the value is 0
					fenzi = sum([(AAidx[prop][index.get(sequence[j], 0)] - xmean) * (AAidx[prop][index.get(sequence[j + n], 0)] - xmean) for j in range(len(sequence) - n)]) / (N - n)
					fenmu = sum([(AAidx[prop][index.get(sequence[j], 0)] - xmean) ** 2 for j in range(len(sequence))]) / N
					rn = fenzi / fenmu
				else:
					rn = 'NA'
				code.append(rn)
		encodings.append(code)
	return encodings
