import argparse
import pandas as pd

def preprocess_file(filename):
    print("Preprocessing file...")

    with open(filename, "r") as file:
        contents = file.read()
    contents = contents.replace(";","")
    with open(filename, "w") as preprocessed_file:
        preprocessed_file.write(contents)
    return filename

def process_data(filename):
    df = pd.read_csv(filename, sep=';', skip_blank_lines=False, na_filter=False, on_bad_lines='skip')
    return df

def df_first_col_to_list(df):
    df_first_col = df.columns[0]
    col_data = []
    for row in df.itertuples():
        if hasattr(row, df_first_col):
            col_data.append(getattr(row, df_first_col))
        else: 
            col_data.append("")
    return col_data

def main():
    parser = argparse.ArgumentParser(description='Process CSV files.')
    parser.add_argument('texts_csv', type=str, help='The csv file that contains a column of texts to be annotated by the concept recogniser.')
    args = parser.parse_args()
    texts_csv = args.texts_csv 

    if texts_csv:
        print(f'Processing labels CSV file: {texts_csv}')
        preprocessed_texts_csv = preprocess_file(texts_csv)
        texts_df = process_data(preprocessed_texts_csv)
        print(texts_df)

    else:
        print(f'No labels CSV file found.')

if __name__ == '__main__':
    main()