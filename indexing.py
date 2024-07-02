from os import path
import os
import argparse
from FastHPOCR.IndexHPO import IndexHPO
from FastHPOCR.IndexORPHANET import IndexORPHANET
from FastHPOCR.IndexMONDO import IndexMONDO


def hpoindex(indexConfig):
    print("Indexing HPO...")
    HPO_INDEX_FOLDER_DIR = path.join(os.getcwd(), "hpo_index")
    HPO_OBO_FILE_DIR = path.join(HPO_INDEX_FOLDER_DIR, "hp.obo")
    indexHPO = IndexHPO(
        HPO_OBO_FILE_DIR, HPO_INDEX_FOLDER_DIR, indexConfig=indexConfig
    )
    print(f"indexConfig: {indexConfig}")
    indexHPO.index()

def orphaindex(indexConfig):
    print("Indexing ORPHA...")
    ORPHA_INDEX_FOLDER_DIR = path.join(os.getcwd(), "orpha_index")
    ORPHA_JSON_FILE_DIR = path.join(ORPHA_INDEX_FOLDER_DIR, "en_product1.json")
    indexORPHANET = IndexORPHANET(
        ORPHA_JSON_FILE_DIR, ORPHA_INDEX_FOLDER_DIR, indexConfig=indexConfig
    )
    print(f"indexConfig: {indexConfig}")
    indexORPHANET.index()

def mondoindex(indexConfig):
    print("Indexing MONDO...")
    MONDO_INDEX_FOLDER_DIR = path.join(os.getcwd(), "mondo_index")
    MONDO_OBO_FILE_DIR = path.join(MONDO_INDEX_FOLDER_DIR, "mondo.obo")
    indexMONDO = IndexMONDO(
        MONDO_OBO_FILE_DIR, MONDO_INDEX_FOLDER_DIR, indexConfig=indexConfig
    )
    print(f"indexConfig: {indexConfig}")
    indexMONDO.index()

def main():
    parser = argparse.ArgumentParser(description="Indexing Ontology files.")
    parser.add_argument(
        "ontology",
        choices=["hpo", "orpha", "mondo"],
        help="The ontology indexing option to use.",
    )
    parser.add_argument("--allow-3-letter-acronyms", action="store_true") 
    parser.add_argument("--include-top-level-category", action="store_true") 
    parser.add_argument("--allow-duplicate-entries", action="store_true") 
    args = parser.parse_args()

    options = {
        "hpo": hpoindex,
        "orpha": orphaindex,
        "mondo": mondoindex,
    }

    selected_function = options.get(args.ontology)
    indexConfig = {
        "allow3LetterAcronyms": args.allow_3_letter_acronyms,
        "includeTopLevelCategory": args.include_top_level_category,
        "allowDuplicateEntries": args.allow_duplicate_entries,
    }
    selected_function(indexConfig)

if __name__ == "__main__":
    main()
