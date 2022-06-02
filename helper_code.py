# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:57:48 2022

@author: Keerthana
"""
import glob
import csv
import os
import json
import pandas as pd


all_the_features ={}
interested_events = ['compiled','compiled successfully',"ran tests","modified"]
quantified_events=["test_results","total_time"]
sub_events=["add_lines","change","remove_lines"]
csv_fields=['Student',"total_time",'compiled','compiled successfully',"ran_tests","test_results","modified","add_lines","change","remove_lines","average_test_results"]

def write_to_csv():
    '''
    with open("student_dataset.csv", "a") as f:
        w = csv.DictWriter(f, csv_fields)
        w.writeheader()
        for k in all_the_features:
            w.writerow({field: all_the_features[k].get(field) or k for field in csv_fields})
    '''
    df=pd.DataFrame.from_dict(all_the_features).transpose()

    df.to_csv('plagiarism_student.csv',)
    
def convert_to_dict(lst):
    init = iter(lst)  
    res_dct = dict(zip(init, init))  
    return res_dct 

def get_features(file,dictionary):
    data=json.load(file)
    if len(data)!=0 and type(data) is not list:
        for majorkey, subdict in data.items():
            #print('majorkey time=>',subdict.keys())
            for subkey, value in subdict.items():
                #print('Subkey=>', subkey, 'Value=>',value)
    
                if subkey =='events':
                    for i in range(len(value)):
                        
    
                        
    
                        if value[i]['text'] in interested_events:
                            
                            if value[i]['text']=='compiled':
                                dictionary['compiled']=1+dictionary.get('compiled',0)
                            elif value[i]['text']=='compiled successfully':
                                dictionary['compiled']=1+dictionary.get('compiled',0)
                                dictionary['compiled successfully']=1+dictionary.get('compiled successfully',0)
                            elif value[i]['text']=='ran tests':
                                dictionary['ran_tests']=1+dictionary.get('ran_tests',0)
                                if value[i]['test_results'][:-3]!='':
                                    dictionary['test_results']=int(value[i]['test_results'][:-3])+dictionary.get('test_results',0)
                                    #print((value[i]['test_results'][:-3]))
                            elif value[i]['text']=='modified':
                                dictionary['modified']=1+dictionary.get('modified',0)
                                if "diff" in value[i]:
                                    if  (value[i]['diff']!= None) and (type(value[i]['diff']) != 'list'):
        
                                        if 'add_lines' in value[i]["diff"]:
                                            dictionary['add_lines']=len(value[i]['diff']['add_lines'])+dictionary.get('add_lines',0)
                                        elif 'remove_lines' in value[i]["diff"]:
                                            dictionary['remove_lines']=len(value[i]['diff']['remove_lines'])+dictionary.get('remove_lines',0)
                                        elif 'change' in value[i]["diff"]:
                                            dictionary['change']=len(value[i]['diff']['change'])+dictionary.get('change',0)
                                
                                  
                        #Total time spent on a problem
                if 'total_time' in subdict.keys():
                    #print('hello')
                    dictionary['total_time']=subdict['total_time']+dictionary.get('total_time',0)
        if 'test_results' in dictionary:
            dictionary['average_test_results'] = dictionary['test_results']/(dictionary['ran_tests'])
        else:
            dictionary['average_test_results']=None
    
        return dictionary
               
            
    




root_dir = '/Users/rhuthuhegde/Desktop/Others/plagiarism-dataset/stats'

for filename in glob.glob(root_dir + '**/**', recursive=True):
    if os.path.isfile(filename):
        with open(filename,'r') as file:
            d = dict()
            feature = get_features(file,d)
            all_the_features[filename[88:-5]]=feature
            #print('All the features=>',all_the_features)
            write_to_csv()
            