import re
import random

file = open('data/HDFS_2k.log', 'r')

lines = file.read().splitlines()

def augment_line(line):
    counter = 1
    newstring = ''
    start = 0
    for m in re.finditer(r"blk_(|-)[0-9]+", line):
        end, newstart = m.span()
        newstring += line[start:end]
        randomly_shuffled_dynamic_blk = ''.join(random.sample(m.group()[4:], len(m.group()[4:])))
        rep = str("blk_") + str(randomly_shuffled_dynamic_blk)
        newstring += rep
        start = newstart
        counter += 1
    newstring += line[start:]
    augmented_line = newstring
    return augmented_line

AUGMENT_TIMES = 9

with open('augmented_data/HDFS_20k_augmented.log', 'w+') as f:
    for line in lines:
        f.write(line + '\n')
        print(line)
        for _ in range(AUGMENT_TIMES):
            augmented_line = augment_line(line)
            f.write(augmented_line + '\n')
            print(augmented_line)
