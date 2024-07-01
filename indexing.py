import argparse
import ontology_indexing

def main():
    parser = argparse.ArgumentParser(description='Indexing Ontology files.')
    parser.add_argument('ontology', choices=['hpo', 'ordo', 'mondo'], help='The ontology indexing option to use.')

    args = parser.parse_args()

    options = {
        'hpo': ontology_indexing.hpoindex,
        # 'ordo': index_ordo,
        # 'mondo': index_mondo,
    }
    
    selected_function = options.get(args.ontology)
    selected_function()

if __name__ == '__main__':
    main()