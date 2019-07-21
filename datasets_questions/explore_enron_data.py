#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open('../final_project/final_project_dataset_unix.pkl', 'rb'))

print(len(enron_data))

print(len(enron_data['METTS MARK']))

print((enron_data['METTS MARK']))


#print((enron_data.keys()))

#enron_data_poi = dict(filter(lambda x: x['poi']==1 in x, enron_data.items()))
#enron_data_poi = filter(lambda x: x['poi'], enron_data.items())
enron_data_poi = [v for k, v in enron_data.items() if v['poi']]
print(len(enron_data_poi))

# Qual é o valor total das ações (stock) pertencentes ao James Prentice?
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# Quantos emails nós temos do Wesley Colwell para POIs?
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# Qual é o valor das opções de ações do Jeffrey K Skilling?
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])


# How much money did that person get?
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])

# How is an unfilled feature denoted?
print(enron_data['FASTOW ANDREW S']['deferral_payments'])

enron_data_salary = [v for k, v in enron_data.items() if v['salary'] != 'NaN']
print(len(enron_data_salary))
enron_data_email = [v for k, v in enron_data.items() if v['email_address'] != 'NaN']
print(len(enron_data_email))

enron_total_payments = [v for k, v in enron_data.items() if (v['poi'] & (v['total_payments'] == 'NaN'))]
#print(len(enron_total_payments)/len(enron_data))
print(len(enron_total_payments))
print(len(enron_data))

enron_total_payments = [v for k, v in enron_data.items() if ((v['total_payments'] == 'NaN'))]
#print(len(enron_total_payments)/len(enron_data))
print(len(enron_total_payments))