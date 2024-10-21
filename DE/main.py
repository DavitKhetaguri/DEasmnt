import pandas as pd
import json
import datetime
import dateutil.parser
from feature_logic import tot_claim_cnt_l180d, disb_bank_loan_wo_tbc, day_sinlastloan


def get_df():

    df = pd.read_csv("./DE Assessment/data.csv") 
    
    df['tot_claim_cnt_l180d'] = df.apply(lambda x: tot_claim_cnt_l180d(x['contracts'], x['application_date']), axis=1)
    df['disb_bank_loan_wo_tbc'] = df.apply(lambda x: disb_bank_loan_wo_tbc(x['contracts']), axis=1)
    df['day_sinlastloan'] = df.apply(lambda x: day_sinlastloan(x['contracts'], x['application_date']), axis=1)

    return df

def write_df(df):
    df.drop(columns=['contracts'], inplace=True)
    df.to_csv("DE/contract_features.csv")

def main():
    df = get_df()
    write_df(df)

if __name__ == "__main__":
   
    main()
    