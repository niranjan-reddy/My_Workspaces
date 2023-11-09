import boto3
#import io
#import os
#import pandas as pd
import awswrangler as wr

def lambda_handler():#event, context):
    session = boto3.Session(aws_access_key_id='AKIATZDFL332HFV5IZLS',
                            aws_secret_access_key='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')

    s3 = session.resource('s3')
    bucket = s3.Bucket('scalablecapital')
    s3_client = boto3.client('s3', use_ssl=False)
    file_name = ''

    try:
        for bucket_object in bucket.objects.all():
            file_name = bucket_object.key
            print('File Name: ', file_name)
            #df = pd.read_csv(io.BytesIO(bucket_object['Body'].read()))
            #file = open(io.BytesIO(bucket_object['Body'].read()))

            df = wr.s3.read_csv(path='s3://scalablecapital/' + file_name,
                                boto3_session=session,
                                skiprows=0,
                                sep=',',
                                decimal='.',
                                na_values=['--'])

            # file_object = s3_client.get_object(Bucket=bucket, Key=bucket_object)
            # df = pd.read_fwf((io.BytesIO(file_object['Body'].read())), encoding='unicode_escape', delimiter=',',
            #                  error_bad_lines=False, header=None, dtype=str)
            process_data(file_name, df)

    except Exception as e:
        print(e)
        print('EXCEPTION OCCURRED: Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(file_name, bucket))
        raise e

def process_data(file_name, df):
    print('DICT: ', df.to_dict())
    #dict = df.to_dict()
    if 'clients' in file_name:
        print('CLIENTS: ', df)
        # for record in dict:
        #     record_id = record.get('record_id')
        #     first_name = record.get('first_name')
        #     last_name = record.get('last_name')
        #     client_reference = record.get('client_reference')
        #     tax_free_allowance = record.get('tax_free_allowance')
        #     print('record_id : {}, first_name: {}, last_name: {}, client_reference: {}, tax_free_allowance: {}'.format(record_id, first_name, last_name, client_reference, tax_free_allowance))

        #for record in df:
        record_id = df('record_id')[0]
        first_name = df('first_name')[0]
        last_name = df('last_name')[0]
        client_reference = df('client_reference')[0]
        tax_free_allowance = df('tax_free_allowance')[0]
        print('record_id : {}, first_name: {}, last_name: {}, client_reference: {}, tax_free_allowance: {}'.format(
                record_id, first_name, last_name, client_reference, tax_free_allowance))

    elif 'portfolios' in file_name:
        print('PORTFOLIOS: ', df)
        for record in df:
            record_id = record[0]
            account_number = record[1]
            portfolio_reference = record[2]
            client_reference = record[3]
            agent_code = record[4]
            print('record_id : {}, account_number: {}, portfolio_reference: {}, client_reference: {}, agent_code: {}'.format(
                record_id, account_number, portfolio_reference, client_reference, agent_code))

    elif 'accounts' in file_name:
        print('ACCOUNTS: ', df)
        for record in df:
            record_id = record[0]
            account_number = record[1]
            cash_balance = record[2]
            currency = record[3]
            taxes_paid = record[4]
            print('record_id : {}, account_number: {}, cash_balance: {}, currency: {}, taxes_paid: {}'.format(
                record_id, account_number, cash_balance, currency, taxes_paid))

    elif 'transactions' in file_name:
        print('TRANSACTIONS: ', df)
        for record in df:
            record_id = record[0]
            account_number = record[1]
            transaction_reference = record[2]
            amount = record[3]
            keyword = record[4]
            print('record_id : {}, account_number: {}, transaction_reference: {}, amount: {}, keyword: {}'.format(
                record_id, account_number, transaction_reference, amount, keyword))

    else:
        exit()


def push_to_queue(json_data):
    print('push_to_queue')


def form_message(data):
    print('form_message')
    # return data


def cleanup_files(file_name):
    print('cleanup_files')


lambda_handler()