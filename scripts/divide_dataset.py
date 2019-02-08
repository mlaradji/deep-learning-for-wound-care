import sys

import os

import shutil

import numpy as np

# Set constant random seed for reproducibility.

np.random.seed(1500)

def divide_dataset(inputpath, workingpath, val_split, test_split):

    

    # Get file list.

    file_list = []

    for root, dirs, files in os.walk(inputpath):



        if os.path.basename(root)[0]=='.': continue # Skip hidden folders.
        if root == inputpath: continue # Skip root folder.

        for f in files:
            file_list.append(os.path.join(os.path.basename(root),f))

    # Shuffle file list.

    np.random.shuffle(file_list)

    

    # Split into training, validation and testing.

    test_splitmark = int((1-test_split)*len(file_list))

    val_splitmark = int((1-test_split-val_split)*len(file_list))

    

    train_list = file_list[:val_splitmark]

    val_list = file_list[val_splitmark:test_splitmark]

    test_list = file_list[test_splitmark:]

    

    # Copy the files into their respective folders in the working directory.

    

    for file in train_list:
        os.makedirs(os.path.join(workingpath, 'train', os.path.dirname(file)), exist_ok=True)

        shutil.copy2(os.path.join(inputpath, file), os.path.join(workingpath, 'train', file))

        

    for file in val_list:

        os.makedirs(os.path.join(workingpath, 'val', os.path.dirname(file)), exist_ok=True)

        shutil.copy2(os.path.join(inputpath, file), os.path.join(workingpath, 'val', file))

        

    for file in test_list:

        os.makedirs(os.path.join(workingpath, 'test', os.path.dirname(file)), exist_ok=True)

        shutil.copy2(os.path.join(inputpath, file), os.path.join(workingpath, 'test', file))

    

    return

            

if __name__ == "__main__":
	
	inputpath = sys.argv[1]
	workingpath = sys.argv[2]
	val_split = float(sys.argv[3])
	test_split = float(sys.argv[4])

	divide_dataset(inputpath, workingpath, val_split, test_split)
