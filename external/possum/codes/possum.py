import fileinput
from os import listdir
from os.path import isfile, join
import re
import numpy as np
from possum_ft import *


def feat_possum(inputFile, outputFile, algoType, pssmdir, argument=None, variable=None):

    check_head = re.compile(r'\>')
    smplist = []
    smpcnt = 0
    for line, strin in enumerate(fileinput.input(inputFile)):
        if not check_head.match(strin):
            smplist.append(strin.strip())
            smpcnt += 1

    onlyfiles = [ f for f in listdir(pssmdir) if isfile(join(pssmdir,f)) ]
    fastaDict = {}

    for fi in onlyfiles:
        cntnt = ''
        pssmContentMatrix=readToMatrix(fileinput.input(pssmdir+'/'+fi))
        pssmContentMatrix=np.array(pssmContentMatrix)
        sequence=pssmContentMatrix[:,0]
        seqLength=len(sequence)
        for i in range(seqLength):
            cntnt+=sequence[i]
        if cntnt in fastaDict:
            continue
        fastaDict[cntnt] = fi

    finalist = []
    for smp in smplist:
        finalist.append(pssmdir+'/'+fastaDict[smp])

    file_out = file(outputFile,'w')

    for fi in finalist:
        #pass in original matrix
        input_matrix=fileinput.input(fi)
        #output a feature vector
        feature_vector=calculateDescriptors(input_matrix, algoType, argument, variable)
        np.savetxt(file_out, feature_vector, delimiter=",")

    return
