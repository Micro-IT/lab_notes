import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from pprint import pprint

df_czech = pd.read_excel('Czech_allele_only_2.xlsx', sheet_name = 'allele_only')
df_usa = pd.read_excel ('USA_allele_only.xlsx', sheet_name = 'allele_only')


# quick look at data column headings (allele designations)
print("Column headings:")
print(df_czech.columns)
print(df_usa.columns)

# print column name list (allele lists)
df_usa.columns.tolist()
df_czech.columns.tolist()

#identify overlapping allele designations
df_czech.columns.intersection(df_usa.columns)

#identify allele designations in czech not in usa
df_czech.columns.difference(df_usa.columns)

#drop the alelle designations that don't match from .difference

df_czech_match = df_czech.drop(columns=['NEIS1777.7', 'NEIS1778.7', 'NEIS1779.7', 'NEIS1780.8'])
df_czech_match.columns.difference(df_usa.columns) #check

# keep only the loci with at least 80% of values (they are present in at least 80% of the isolates)
## for czech
df_czech_eighty = df_czech_match.dropna(axis = 'columns', thresh = 218*0.8)
df_czech_full = df_czech_match.dropna(axis = 'columns' , thresh = 218)
df_czech_clean = df_czech_eighty.dropna(thresh = 14071*0.8)
print ('czech_raw' + str(df_czech_match.shape))
print ('czech_column_eighty: ' + str(df_czech_eighty.shape))
print ('czech_clean' + str(df_czech_clean.shape))

## for USA
df_usa_eighty = df_usa.dropna(axis = 'columns', thresh = 324*0.8)
df_usa_full = df_usa.dropna(axis = 'columns' , thresh = 324)
df_usa_clean = df_usa_eighty.dropna(thresh = 14259*0.8)
print ('usa_raw' + str(df_usa.shape))
print ('usa_column_eighty: ' + str(df_usa_eighty.shape))
print ('usa_clean: ' + str(df_usa_clean.shape))

# drop the columns that don't match round two
## remaining overlapping columns
df_usa_clean.columns.intersection(df_czech_clean.columns)


df_usa_cleanlap = df_usa_clean[df_usa_clean.columns.intersection(df_czech_clean.columns)]
df_czech_cleanlap = df_czech_clean[df_usa_clean.columns.intersection(df_czech_clean.columns)]
print ('usa_cleanlap: ' + str(df_usa_cleanlap.shape), 'czech_cleanlap: ' + str(df_czech_cleanlap.shape))

# ---------------------------------------------------------------------------------

#find allele names that don't start with NEIS
nNEIS_cols_usa = [col for col in df_usa＿cleanlap.columns if 'NEIS' not in col]
pprint(nNEIS_cols_usa)

nNEIS_cols_czech = [col for col in df_czech_cleanlap.columns if 'NEIS' not in col]
pprint(nNEIS_cols_czech)
#delete certain columns based off of this
df_usa_fclean = df_usa_cleanlap.drop(columns=[
                                    'fHbp_peptide', 'fHbp_peptide.1', 'NHBA_peptide', "'fHbp.1", "'fHbp.2", "'fHbp.3", "'fHbp.4",
                                    'PorA_VR1.1', 'PorA_VR2.1', 'abcZ.1', 'adk.1', 'aroE.1', 'fumC.1', 'gdh.1', 'pdhC.1', 'pgm.1',
                                    'ST (MLST)', 'genospecies (rplF species)', 'rplF_id (rplF species)', 'rST (Ribosomal MLST)',
                                    'genus (Ribosomal MLST)', 'species (Ribosomal MLST)', 'NG_ponA'
                                    ])

df_czech_fclean = df_czech_cleanlap.drop(columns=[
                                        'fHbp_peptide', 'fHbp_peptide.1', 'NHBA_peptide', "'fHbp.1", "'fHbp.2", "'fHbp.3", "'fHbp.4",
                                        'PorA_VR1.1', 'PorA_VR2.1', 'abcZ.1', 'adk.1', 'aroE.1', 'fumC.1', 'gdh.1', 'pdhC.1', 'pgm.1',
                                        'ST (MLST)', 'genospecies (rplF species)', 'rplF_id (rplF species)', 'rST (Ribosomal MLST)',
                                        'genus (Ribosomal MLST)', 'species (Ribosomal MLST)', 'NG_ponA'
                                        ])
#check
# nNEIS_cols_usa_fclean = [col for col in df_usa_fclean.columns if 'NEIS' not in col]
# pprint(nNEIS_cols_usa_fclean)

# ---------------------------------------------------------------------------------
#pickle it
df_usa_fclean.to_pickle('usa_allele_clean.pkl')
df_czech_fclean.to_pickle('czech_allele_clean.pkl')

# ---------------------------------------------------------------------------------

#relative frequency counts of each value(unique allele)for a given loci (allele X is present in n% of the population)
print (df_usa_cleanlap['NEIS1279'].value_counts(normalize=True, dropna=True))
# store the frequency counts of a loci into dictionary 'counts'
counts = df_usa_cleanlap['NEIS1279'].value_counts(normalize=True, dropna=True).to_dict()
pprint(counts)
#based off of this, intermediate frequency alleles = 5~95% of alleles?

#number of unique alleles at each loci

# df_usa_cleanlap.apply(pd.Series.nunique, axis=0)
