import json
import numpy as np
import os

if __name__ == "__main__":
    train = []
    dev = []

    subjective_path = os.path.join("E:\Master\Term1\DRGA\TrainData\SUBJ", "quote.tok.gt9.5000" )
    objective_path = os.path.join("E:\Master\Term1\DRGA\TrainData\SUBJ", "plot.tok.gt9.5000" )

    c = 0
    with open( subjective_path, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.strip()
            data = {
                "words": '|'.join(line.split()),
                "solution": 0
            }

            if np.random.binomial(1, 0.7):
                train.append(data)
            else:
                dev.append(data)

            c +=1
            if c == 50:
                break


    c = 0       
    with open(objective_path, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.strip()
            data = {
                "words": '|'.join(line.split()),
                "solution": 1
            }

            if np.random.binomial(1, 0.7):
                train.append(data)
            else:
                dev.append(data)
            c+=1
            if c == 50:
                break
            


### TEST
    test2 = []
    dev2 = []

    for d in dev:
        if np.random.binomial(n = 1, p = .5):
            dev2.append(d)
        else:
            test2.append(d)
     


    print(f"Do dai tap train: {len(train)}")
    print(f"Do dai tap dev: {len(dev2)}")
    print(f"Do dai tap test: {len(test2)}")
    with open("train_small.txt", "w") as outfile:
        json.dump(train, outfile)

    with open("dev_small.txt", "w") as outfile:
        json.dump(dev, outfile)

    with open("test_small.txt", "w") as outfile:
        json.dump(dev, outfile)