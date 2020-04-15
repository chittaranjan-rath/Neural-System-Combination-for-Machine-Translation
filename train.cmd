
nohup nice ~/mosesdecoder/scripts/training/train-model.perl -root-dir train
-corpus ~/corpus/en-hi.clean
-f fr -e en -alignment grow-diag-final-and -reordering msd-bidirectional-fe
-lm 0:3:$HOME/lm/en-hi.cor
-external-bin-dir ~/mosesdecoder/tools >& training.out &
