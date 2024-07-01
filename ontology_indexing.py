from os import path
import os
from FastHPOCR.IndexHPO import IndexHPO
from FastHPOCR.IndexORPHANET import IndexORPHANET

# Paths
# dir_path = os.path.dirname(os.path.realpath(__file__))

def hpoindex():
    print("Indexing HPO...")
    HPO_INDEX_FOLDER_DIR = path.join(os.getcwd(), "hpo_index")
    HPO_OBO_FILE_DIR = path.join(HPO_INDEX_FOLDER_DIR, "hp.obo")
    indexConfig = {
        'allow3LetterAcronyms': False,
        'includeTopLevelCategory': False,
        'allowDuplicateEntries': True,
    }
    indexHPO = IndexHPO(HPO_OBO_FILE_DIR, HPO_INDEX_FOLDER_DIR, indexConfig=indexConfig)
    indexHPO.index()

def ordoindex():
    print("Indexing ORDO...")
    ORDO_INDEX_FOLDER_DIR = path.join(os.getcwd(), "ordo_index")
    ORDO_JSON_FILE_DIR = path.join(ORDO_INDEX_FOLDER_DIR, "en_product1.json")

    indexConfig = {
        'allow3LetterAcronyms': False,
        'includeTopLevelCategory': False,
        'allowDuplicateEntries': True,
    }

    #indexORPHANET = IndexORPHANET(ORDO_JSON_FILE_DIR, ORDO_INDEX_FOLDER_DIR, indexConfig=indexConfig)
    #indexORPHANET.index()

if __name__ == '__main__':
    print("TODO")