import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('contact_info_file', help='The path to respondent_contact.csv file')
parser.add_argument('other_info_file', help='The path to respondent_other.csv file')
parser.add_argument('output_file', help='The path to the output file')
args = parser.parse_args()

# (1) merge the two input data files based on the ID of each respondent.
contact_df = pd.read_csv(args.contact_info_file)
other_df = pd.read_csv(args.other_info_file)
merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')

# (2) drop any rows with missing values.
merged_df.dropna(inplace=True)

# (3) drop rows if the job value contains 'insurance' or 'Insurance'.
merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

# (4) write the cleaned data to the file specified by the output_file argument.
merged_df.to_csv(args.output_file, index=False)

print(merged_df)
print("Output file shape:")
print(merged_df.shape)