import random

training = list()
test = list()

with open("trainingData10.txt", encoding='utf-8') as inFile:
    with open("training.txt", "w", encoding='utf-8') as trainingFile:
        with open("test.txt", "w", encoding='utf-8') as testFile:
            testIds = random.sample(range(25046), k=2500)
            testIds = set(testIds)
            i = 0
            for line in inFile:
                if i in testIds:
                    testFile.write(line)
                    test.append(line)
                else:
                    trainingFile.write(line)
                    training.append(line)
                i = i+1
            # random.shuffle(test)
            # random.shuffle(training)

            # testFile.writelines(test)
            # trainingFile.writelines(training)
