from Bio import Entrez
from Bio import SeqIO


# See if there is an alternative to download this
Entrez.email = "r.ortegapolo@uleth.ca"

# Read in list of accession numbers

id_list = 

handle = Entrez.efetch(db="nuccore", id=id_list, rettype="gb", retmode="text")

for record in SeqIO.parse(handle, "gb"):
    sero = 'Untyped'
    for feature in record.features:
        if 'serotype' in feature.qualifiers:
            sero = feature.qualifiers['serotype']
    print(record.name, sero)
handle.close()
