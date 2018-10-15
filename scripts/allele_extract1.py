import json
import os
import requests
from pprint import pprint

pubmlst_url_base = 'http://rest.pubmlst.org/db/pubmlst_neisseria_isolates/isolates/'

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

def get_isolate_record(url):
    response = requests.get(url, headers = HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
#--------------------------------- provide idlist (could also be input)
idlist = [1,2,392]
# test this idlist import from the url list obtained by webcrawler


for isolate_id in idlist:
    isolate_id_url = pubmlst_url_base + str(isolate_id)
    isolate_record = get_isolate_record(isolate_id_url)

    json.dumps(isolate_record)
    #pprint (data)
#--------------------------------- isolate record information & checkpoint
    if isolate_record is not None:
        print("isolate record: ")
        for k, v in isolate_record['allele_designations'].items():
            print('{0}:{1}'.format(k, v))

        else:
            print('Request Ended, rerun boostrapping algorithm')
#---------------------------------- extract allele_ids information

    des_count = (isolate_record.get('allele_designations', {}).get('designation_count')) ##extract value of 'designation_count' from nested dictionary
    allele_url = (isolate_record.get('allele_designations', {}).get('allele_ids'))

    if des_count > 2000:
        print ('designation_count = ' + str(des_count))
        allele = requests.get(allele_url)
        allele_id_re = allele.json()
        print(allele.status_code)
#----------------------------------  get full list of alleles (no pagination)
        allele_full = (allele_id_re.get('paging', {}).get('return_all'))
        allelefull = requests.get(allele_full)
        allelefull_dict = allelefull.json()
        pprint(allelefull_dict)

        allelefull_list = json.dumps(allelefull_dict)
        with open("allelefilex.{}.csv".format(isolate_id), "w") as f:  # put a counter inside the files name
            f.write(allelefull_l)
        print( os.listdir("./"))
        print ('')

    else:
        print('[!] incomplete loci info')
        print ('')
