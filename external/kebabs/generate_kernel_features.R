# Title     : Kernel Feature Generation
# Objective : A script to create three kernel features using the kebabs package
# Created by: Deepro Banerjee
# Created on: 3/21/21

library(kebabs)
library(Matrix)


aa <- readAAStringSet(paste('./data/seq/CombinedEnzymeFasta.fa', sep=''))

specK7 <- spectrumKernel(k=7, normalized=FALSE)
specFeat <- getExRep(aa, kernel=specK7, sparse=TRUE)

output_dir_prefix <- "./data/features/kernel/featfiles/"

matCSR_spec <- as(specFeat,"dgRMatrix")
write(colnames(matCSR_spec), file = paste(output_dir_prefix, "spec_kern_colnames.txt",sep=""))
write(rownames(matCSR_spec), file = paste(output_dir_prefix, "spec_kern_rownames.txt",sep=""))
writeMM(matCSR_spec, file = paste(output_dir_prefix, "spec_kern_sparsematrix.txt",sep=""))


mismK3M1 <- mismatchKernel(k=3, m=1, normalized=FALSE)
mismFeat <- getExRep(aa, kernel=mismK3M1, sparse=TRUE)

matCSR_mism <- as(mismFeat,"dgRMatrix")
write(colnames(matCSR_mism), file = paste(output_dir_prefix, "mism_kern_colnames.txt",sep=""))
write(rownames(matCSR_mism), file = paste(output_dir_prefix, "mism_kern_rownames.txt",sep=""))
writeMM(matCSR_mism, file = paste(output_dir_prefix, "mism_kern_sparsematrix.txt",sep=""))

gappyK1M2 <- gappyPairKernel(k=3, m=2, normalized=FALSE)
gappyFeat <- getExRep(aa, kernel=gappyK1M2, sparse=TRUE)

matCSR_gap <- as(gappyFeat, "dgRMatrix")
write(colnames(matCSR_gap), file = paste(output_dir_prefix, "gap_kern_colnames.txt",sep=""))
write(rownames(matCSR_gap), file = paste(output_dir_prefix, "gap_kern_rownames.txt",sep=""))
writeMM(matCSR_gap, file = paste(output_dir_prefix, "gap_kern_sparsematrix.txt",sep=""))
