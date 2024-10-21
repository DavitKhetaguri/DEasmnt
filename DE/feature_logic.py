import json
import datetime
from date_utils import format_pd_date, format_date_json, compare_dates




def get_day_sinlastloan(data, date):
    last_loan = None
    for i in data:
        if i.get('summa'):
            print('here')
            if not last_loan or compare_dates(format_date_json(i.get('contract_date')), last_loan):
                last_loan = format_date_json(i.get('contract_date'))
    return (date - last_loan).days if last_loan else -1



def get_disbursed_amount(data):
    amount = 0
    loan_count = 0
    for i in data:
        if i.get('bank') not in ['LIZ', 'LOM', 'MKO', 'SUG', None] and i.get('contract_date') is not None:
            if i.get('loan_summa', 0): 
                summa = i.get('loan_summa')
            else:
                summa = 0    
            amount = amount + summa 
            loan_count += 1
    if not loan_count:
        return -1
    return amount


def get_total_claims(data, date):
    
    number_of_claims = 0
    for i in data:
        if i.get('claim_id') and compare_dates(format_date_json(i.get('claim_date')), date):
            number_of_claims += 1

    return number_of_claims if number_of_claims else -3





################# formaters

def tot_claim_cnt_l180d(json_data, date):
    
    date = format_pd_date(date)
    days_ago = date - datetime.timedelta(days=180)
    try:
        data = json.loads(json_data)
    except:
        return -3

    ## empty json
    if not data:
        return -3
    ### dict json
    if type(data) == dict:
        data = [data]
   
    return get_total_claims(data, days_ago)



############ 2
def disb_bank_loan_wo_tbc(json_data):
    try:
        data = json.loads(json_data)
    except:
        return -1
    
     ## empty json
    if not data:
        return -3
    ### dict json
    if type(data) == dict:
        data = [data]
        
    return get_disbursed_amount(data)


def day_sinlastloan(json_data, date):
    date = format_pd_date(date)
    try:
        data = json.loads(json_data)
    except:
        return -1

    ## empty json
    if not data:
        return -1
    ### dict json
    if type(data) == dict:
        data = [data]

    return get_day_sinlastloan(data, date)