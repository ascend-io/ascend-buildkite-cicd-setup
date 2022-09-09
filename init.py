import ascend
import fileinput
import os
import sys

from ascend.sdk.client import Client
from ascend.sdk.render import download_dataflow


def replace(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=True):
        line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)


def main():
    try:
        hostname = input('Enter the name of the hostname: ')
        dataserv = input('Enter the name of the data service: ')
        dataflow = input('Enter the name of the data flow: ')
        access_key = input('Enter access key id: ')
        secret_key = input('Enter secret access key: ')
        
        client = Client(hostname=hostname, access_key=access_key, secret_key=secret_key)
        download_dataflow(client, data_service_id=dataserv, dataflow_id=dataflow, resource_base_path='.')
        os.rename(f'{dataflow}.py', 'upload.py')
        replace('upload.py', f'client = Client("{hostname}")',
                """client = Client(hostname=os.getenv("hostname"),
                    access_key=os.getenv("ASCEND_ACCESS_KEY"),
                    secret_key=os.getenv("ASCEND_SECRET_KEY"))""")
        replace('.buildkite/pipeline.yml', '<<replace_env>>', hostname)
    except:
        #TODO:  add error statements later
        pass

main()
