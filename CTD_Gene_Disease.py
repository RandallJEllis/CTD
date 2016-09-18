# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 16:24:58 2016

@author: ellisrj2
"""
"""
 Refer to http://ctdbase.org/help/linking.jsp#batchqueries for all acceptable input/report combinations
Input types: 'chem', 'disease', 'gene', 'go', 'pathway', 'reference'
Report types: 'cgixns', 'chems', 'diseases', 'genes', 'go', 'pathways_curated', 'pathways_inferred', 'pathways_enriched'
Format types: 'CSV', 'TSV', 'JSON', 'XML' 
"""

def CTD_association(input_type, input_terms_file, report_type, format_type):
    import requests
    import csv 
    
    base_url = 'http://ctdbase.org/tools/batchQuery.go?'
    input_Type = 'inputType=' + input_type + '&'
    input_Terms_tag = 'inputTerms='
    input_Terms = []
    report = '&report=' + report_type + '&'
    format_Type = 'format=' + format_type
    
    query_terms = [gene.rstrip('\n') for gene in open(input_terms_file)] 
    query_terms = list(set(query_terms)) # removes duplicates
    
    
    for query in query_terms:
        input_Terms.append(query + '|')
    input_Terms = ''.join(input_Terms)
    
    response_object = requests.get(base_url + input_Type + input_Terms_tag + input_Terms + report + format_Type)

    with open(input_terms_file[:-4] + '_' + report_type + '.csv', 'wb') as thefile:
        data_write = csv.writer(thefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_write.writerow([response_object.content])
