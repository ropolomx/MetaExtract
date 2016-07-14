from Bio import Entrez
from Bio import SeqIO
from collections import defaultdict
import pandas as pd

# See if there is an alternative to download this
Entrez.email = "r.ortegapolo@uleth.ca"

# Read in list of accession numbers

id_list = 

serotype_dict = defaultdict(list)

handle = Entrez.efetch(db="nuccore", id=id_list, rettype="gb", retmode="text")

for record in SeqIO.parse(handle, "gb"):
    serotype = 'Untyped'
    for feature in record.features:
        if 'serotype' in feature.qualifiers:
            serotype = feature.qualifiers['serotype']
    sero_dict[record.name].append(serotype)

handle.close()

sero_DF = pd.DataFrame(sero_dict, index=(['Serotype'])).T
sero_DF.index.name = 'Accession'

sero_DF.to_csv('sero_DF.csv')

# A way to get serotype information from the title or the serotype field
