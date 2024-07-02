from os import path
import os
import preprocess_data
import argparse
import numpy as np
import pandas as pd
from FastHPOCR.HPOAnnotator import HPOAnnotator

HPO_INDEX_DIR = path.join(os.getcwd(), "hpo_index", "hp.index")
ORPHA_INDEX_DIR = path.join(os.getcwd(), "orpha_index", "orpha.index")
MONDO_INDEX_DIR = path.join(os.getcwd(), "mondo_index", "mondo.index")

def annotate_text(ontology_index, text):
    print(f"Input: {text}")
    hpoAnnotator = HPOAnnotator(ontology_index)
    annotations = hpoAnnotator.annotate(text, longestMatch=True)
    hpoAnnotator.printResults(annotations)

def annotate_data(ontology_index, texts, codes, labels):
    # Preprocessing texts
    preprocess_texts = preprocess_data.preprocess_file(texts)
    texts_df = preprocess_data.process_data(preprocess_texts)
    texts_list = preprocess_data.df_first_col_to_list(texts_df)
    results_df = texts_df

    # Preprocessing URIs
    if codes:
        uri_df = preprocess_data.process_data(codes)
        uri_codes = preprocess_data.df_first_col_to_list(uri_df)
        uri_codes_np = np.array(uri_codes)
        results_df['code_expected'] = uri_codes_np.tolist()
    
    # Preprocessing labels 
    if labels:
        labels_df = preprocess_data.process_data(labels)
        labels_list = preprocess_data.df_first_col_to_list(labels_df)
        labels_list_np = np.array(labels_list)
        results_df['labels_expected'] = labels_list_np.tolist()

    # Run concept recogniser
    mined_URIs = []
    mined_labels = []
    hpoAnnotator = HPOAnnotator(ontology_index)
    for text in texts_list:
        minedData = hpoAnnotator.annotate(text, longestMatch=True)
        if len(minedData) == 0:
            mined_URIs.append("")
            mined_labels.append("")
        else:
            mined_URIs.append(minedData[0].getHPOUri())
            mined_labels.append(minedData[0].getHPOLabel())
    
    mined_URIs_np = np.array(mined_URIs)
    mined_labels_np = np.array(mined_labels)
    results_df['code_output'] = mined_URIs_np.tolist()
    results_df['labels_output'] = mined_labels_np.tolist()
    print("Results:")
    print(results_df)

def main():
    parser = argparse.ArgumentParser(description='Process CSV files.')
    parser.add_argument('ontology', choices=['hpo', 'orpha', 'mondo'], help='The ontology indexing option to use.')
    parser.add_argument('--t', action='store_true', help='Annotate the text provided.') 
    parser.add_argument('texts_csv', type=str, help='The csv file that contains a column of texts to be annotated by the concept recogniser.')
    parser.add_argument('codes_csv', type=str, nargs='?', help='The csv file that contains a column of the expected codes/URIs.')
    parser.add_argument('labels_csv', type=str, nargs='?', help='Optional csv file that contains a column of the expected labels.')

    args = parser.parse_args()
    texts_csv = args.texts_csv 
    codes_csv = args.codes_csv
    labels_csv = args.labels_csv

    options = {
        'hpo': HPO_INDEX_DIR,
        'orpha': ORPHA_INDEX_DIR,
        'mondo': MONDO_INDEX_DIR,
    }

    selected_ontology = options.get(args.ontology)

    if args.t:
        annotate_text(selected_ontology, texts_csv)
    else:
        annotate_data(selected_ontology, texts_csv, codes_csv, labels_csv)

if __name__ == '__main__':
    main()