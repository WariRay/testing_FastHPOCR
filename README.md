# testing_FastHPOCR

## Requirements
__These are just steps to install the dependencies.__

### Dependencies
Enter the the folder that contains the Python package and pip install the package.
```
pip3 install -e fast_hpo_cr/pypi/FastHPOCR
```

Install the rest of dependencies from requirement.txt.
```
pip3 install -r requirements.txt 
```

## Usage
### Running indexing.py
Indexing ontologies:
```
python3 indexing.py <hpo/orpha/mondo>
```
### Running run_cr.py
## Arguments:
- {hpo,orpha,mondo}  The ontology indexing option to use.
- texts_csv          The csv file that contains a column of texts to be annotated by the concept recogniser.
- codes_csv          The csv file that contains a column of the expected codes/URIs.
- labels_csv         Optional csv file that contains a column of the expected labels.
## Options:
- -h, --help         Show this help message and exit
- --t                Annotate the text provided.

Running run_cr.py with hpo index, texts.csv, codes.csv (optional) and labels.csv (optional).
```
python3 run_cr.py hpo texts.csv codes.csv labels.csv
```

Running run_cr.py with hpo index and a text string (when you only want to annotate a single text).
```
python3 run_cr.py hpo --t "Sturge-Weber syndrome"
```