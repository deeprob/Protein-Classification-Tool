import re
import numpy as np
from . import checkFasta


def QSOrder(fastas, nlag=30, w=0.1, **kw):
	if checkFasta.minSequenceLengthWithNormalAA(fastas) < nlag + 1:
		print('Error: all the sequence length should be larger than the nlag+1: ' + str(nlag + 1) + '\n\n')
		return 0

	dataFile = './external/ifeature/data/Schneider-Wrede.txt'
	dataFile1 = './external/ifeature/data/Grantham.txt'

	AA = 'ACDEFGHIKLMNPQRSTVWY'
	AA1 = 'ARNDCQEGHILKMFPSTWYV'

	DictAA = {}
	for i in range(len(AA)):
		DictAA[AA[i]] = i

	DictAA1 = {}
	for i in range(len(AA1)):
		DictAA1[AA1[i]] = i

	with open(dataFile) as f:
		records = f.readlines()[1:]
	AADistance = []
	for i in records:
		array = i.rstrip().split()[1:] if i.rstrip() != '' else None
		AADistance.append(array)
	AADistance = np.array(
		[float(AADistance[i][j]) for i in range(len(AADistance)) for j in range(len(AADistance[i]))]).reshape((20, 20))

	with open(dataFile1) as f:
		records = f.readlines()[1:]
	AADistance1 = []
	for i in records:
		array = i.rstrip().split()[1:] if i.rstrip() != '' else None
		AADistance1.append(array)
	AADistance1 = np.array(
		[float(AADistance1[i][j]) for i in range(len(AADistance1)) for j in range(len(AADistance1[i]))]).reshape(
		(20, 20))

	encodings = []
	header = ['#']
	for aa in AA1:
		header.append('Schneider.Xr.' + aa)
	for aa in AA1:
		header.append('Grantham.Xr.' + aa)
	for n in range(1, nlag + 1):
		header.append('Schneider.Xd.' + str(n))
	for n in range(1, nlag + 1):
		header.append('Grantham.Xd.' + str(n))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		code = [name]
		arraySW = []
		arrayGM = []
		for n in range(1, nlag + 1):
			arraySW.append(
				sum([AADistance[DictAA[sequence[j]]][DictAA[sequence[j + n]]] ** 2 for j in range(len(sequence) - n)]))
			arrayGM.append(sum(
				[AADistance1[DictAA1[sequence[j]]][DictAA1[sequence[j + n]]] ** 2 for j in range(len(sequence) - n)]))
		myDict = {}
		for aa in AA1:
			myDict[aa] = sequence.count(aa)
		for aa in AA1:
			code.append(myDict[aa] / (1 + w * sum(arraySW)))
		for aa in AA1:
			code.append(myDict[aa] / (1 + w * sum(arrayGM)))
		for num in arraySW:
			code.append((w * num) / (1 + w * sum(arraySW)))
		for num in arrayGM:
			code.append((w * num) / (1 + w * sum(arrayGM)))
		encodings.append(code)
	return encodings
