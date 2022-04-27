from email.policy import strict
import string
from configs import engine, SGK1
import pandas as pd
import os
from sendgrid import SendGridAPIClient
import json

string_filter = ["IPs were throttled by recipient server"]

with engine.connect() as conn:
    query_reg= "SELECT * from users_registered"
    df_reg = pd.read_sql(query_reg, con=conn)

"""
dfx= df[["email_address","user_fullname", "Bad? ", "phone"]]
dfx = dfx[dfx["Bad? "]==1]
"""

def emails_from_response_dict_filtered(dict_list, str_filter_list):
    
    Emails_to_process= []
    for dictx in dict_list:
        if not any(x in str(dictx["reason"]) for x in str_filter_list):
            Emails_to_process.append(dictx["email"])

    Emails_to_process = list(set(Emails_to_process))
    return Emails_to_process

def emails_from_all_lists(string_filter):

    sg = SendGridAPIClient(SGK1)
    response_invalid_dict = sg.client.suppression.invalid_emails.get().body
    response_invalid_dict = json.loads(response_invalid_dict)

    response_blocks_dict = sg.client.suppression.blocks.get().body
    response_blocks_dict = json.loads(response_blocks_dict)


    headers = {'Accept': 'application/json'}
    response_bounces_dict = sg.client.suppression.bounces.get( request_headers=headers).body
    response_bounces_dict = json.loads(response_bounces_dict)

    


    List_Bad= emails_from_response_dict_filtered(response_blocks_dict, string_filter) +\
                emails_from_response_dict_filtered(response_invalid_dict, string_filter)+\
                    emails_from_response_dict_filtered(response_bounces_dict, string_filter)

    return List_Bad


def emails_from_all_lists(string_filter):

    sg = SendGridAPIClient(SGK1)
    response_invalid_dict = sg.client.suppression.invalid_emails.get().body
    response_invalid_dict = json.loads(response_invalid_dict)

    response_blocks_dict = sg.client.suppression.blocks.get().body
    response_blocks_dict = json.loads(response_blocks_dict)


    headers = {'Accept': 'application/json'}
    response_bounces_dict = sg.client.suppression.bounces.get( request_headers=headers).body
    response_bounces_dict = json.loads(response_bounces_dict)

    


    List_Bad= emails_from_response_dict_filtered(response_blocks_dict, string_filter) +\
                emails_from_response_dict_filtered(response_invalid_dict, string_filter)+\
                    emails_from_response_dict_filtered(response_bounces_dict, string_filter)

    return List_Bad


def reasons():

    List_reasons = []
    sg = SendGridAPIClient(SGK1)
    response_invalid_dict = sg.client.suppression.invalid_emails.get().body
    response_invalid_dict = json.loads(response_invalid_dict)

    response_blocks_dict = sg.client.suppression.blocks.get().body
    response_blocks_dict = json.loads(response_blocks_dict)


    headers = {'Accept': 'application/json'}
    response_bounces_dict = sg.client.suppression.bounces.get( request_headers=headers).body
    response_bounces_dict = json.loads(response_bounces_dict)

    return List_reasons

#Log reasons to DB

def emails_bounced_invalid_lists(string_filter):

    sg = SendGridAPIClient(SGK1)
    response_invalid_dict = sg.client.suppression.invalid_emails.get().body
    response_invalid_dict = json.loads(response_invalid_dict)


    headers = {'Accept': 'application/json'}
    response_bounces_dict = sg.client.suppression.bounces.get( request_headers=headers).body
    response_bounces_dict = json.loads(response_bounces_dict)

    
    List_Bad= emails_from_response_dict_filtered(response_invalid_dict, string_filter)+\
                    emails_from_response_dict_filtered(response_bounces_dict, string_filter)
    return List_Bad


#Log in DB the 3 lists- see if the dict structure is same, add column with source
#Delete from SG the bounces and invalid https://docs.sendgrid.com/api-reference/bounces-api/delete-bounces
#Send SMS about incorrect data (bounced and invalid) - if number is Moldovan
#AWAIT for session- when the phone is around!
#LOG SMS to DB
#Remove from DB users_registered those bounces and invalid





