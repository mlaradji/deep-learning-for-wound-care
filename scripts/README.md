## Usage example for `split_dataset.py`.

The format is:
```
python scripts/divide_dataset.py INPUTPATH WORKINGPATH VALSPLIT TESTSPLIT
```

For example, to split the dataset in `data/google-images-medetec-combined` with validation and test splits of 0.15 and 0.15, respectively, and save the new dataset in `data/gimages-medetec-combined-split`, execute the following command:
```
python scripts/divide_dataset.py 'data/google-images-medetec-combined' 'data/gimages-medetec-combined-split' 0.15 0.15
```
