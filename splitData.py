
def splitTrainTest(path, filename, ratio):
    lines = open(path+filename, encoding='utf-8').read().strip().split('\n')
    print("Total lines: ", len(lines))
    split_index = int(ratio * len(lines))
    print("split_index is: ", split_index)
    train_lines = lines[0:split_index]
    test_lines = lines[split_index:]
    print("Train lines: ", len(train_lines))
    print("Test lines: ", len(test_lines))
    
    train_file = open(path+"train_"+filename, mode='w', encoding='utf-8')
    for line in train_lines:
        train_file.write(line+'\n')
    train_file.close()    

    test_file = open(path+"test_"+filename, mode='w', encoding='utf-8')
    for line in test_lines:
        test_file.write(line+'\n')
    test_file.close()

if __name__ == "__main__":
    path = "../Dataset/pruned/"
    filename = "pruned_train.en"
    splitTrainTest(path, filename, 0.6)
    filename = "pruned_train.hi"
    splitTrainTest(path, filename, 0.6)
    