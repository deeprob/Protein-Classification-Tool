import os
import re
from external.ifeature.codes import readFasta
import argparse

dbName = '~/work/iFeature/myData/uniref50/uniref50db'
ncbidir = '/opt/aci/sw/ncbi-rmblastn/2.9.0_gcc-8.3.1-bxy/bin/'
outputdir = 'out/'


def generatePSSMProfile(fastas, outDir, blastpgp, db):
	"""
	Generate PSSM file by using the psi-blast program in NCBI blast-2.2.18 package.

	Parameters
	----------
	fastas : file
		the file, which include the protein sequences in fasta format.

	blastpgp: string
		the path of blastpgp program.
		
	db: string 
		the uniref50 data base, which is formated by the 'formatdb' program in blast package.

	Returns
	-------
	a string: 
		A directory name, which include the predicted protein PSSM information.
	"""


	if os.path.exists(outDir) == False:
		os.mkdir(outDir)

	fastas = readFasta.readFasta(fastas)

	for i in fastas:
		name, sequence = re.sub('\|', '', i[0]), i[1]
		with open(name + '.txt', 'w') as f:
			f.write('>'+name+'\n'+sequence + '\n')
		myCmd = blastpgp + ' -query ' + name + '.txt' + ' -db ' + db + ' -num_iterations 3 -num_threads 24 -out_ascii_pssm ' + outDir + '/' + name +'.pssm'
		print('Running psiblast for protein: ' + name)
		os.system(myCmd)
		os.remove(name + '.txt')
	return outDir


if __name__ == '__main__':
	parser = argparse.ArgumentParser(usage="it's usage tip.", description="generate PSSM profile")
	parser.add_argument("--file", required=True, help="protein sequence file in fasta format")
	parser.add_argument("--blastpgp", help="the path of NCBI psiblast program")
	parser.add_argument("--db", help="the path of uniref50 database")
	args = parser.parse_args()

	blastpgp = args.blastpgp if args.blastpgp != None else ncbidir + 'psiblast' #ncbidir + '/blastpgp'
	db = args.db if args.db != None else dbName
	fastas = readFasta.readFasta(args.file)
	outputDir = generatePSSMProfile(fastas, outputdir, blastpgp, db)
	print('The PSSM profiles are stored in directory: ' + outputDir)








