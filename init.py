#!/usr/bin/env python3

import ascend
import fileinput
import os
import shutil
import sys
import typer

from ascend.sdk.client import Client
from ascend.sdk.render import download_dataflow, download_data_service

app = typer.Typer()


def replace(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=True):
        line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)


@app.command()
def create_dataflow(
        hostname: str,
        data_service_id: str,
        dataflow_id: str):
    """
    Download dataflow locally
    """
    dataserv = data_service_id.replace('-', '_').replace(' ', '__')
    dataflow = dataflow_id.replace('-', '_').replace(' ', '__')

    client = Client(hostname=hostname)
    download_dataflow(client, data_service_id=dataserv, dataflow_id=dataflow, resource_base_path='.')
    os.rename(f'{dataflow}.py', 'upload.py')
    replace('upload.py', f'client = Client("{hostname}")',
            'client = Client(os.getenv("ASCEND_HOSTNAME"))')
    replace('upload.py', f'apply_dataflow(client, "{dataserv}"',
            'apply_dataflow(client, os.getenv("ASCEND_DATA_SERVICE")')
    replace('upload.py', f'id=\'{dataflow}\'', f'id=os.getenv("ASCEND_DATAFLOW")')
    replace('upload.py', f'name=\'{dataflow}\'', f'name=os.getenv("ASCEND_DATAFLOW")')

    shutil.copy('.buildkite/pipeline.yml.template', '.buildkite/pipeline.yml')
    replace('.buildkite/pipeline.yml', '<<REPLACE_ENV_DEV>>', hostname)
    replace('.buildkite/pipeline.yml', '<<REPLACE_DATA_SERVICE_DEV>>', dataserv)
    replace('.buildkite/pipeline.yml', '<<REPLACE_DATAFLOW_DEV>>', dataflow)
    
    print(f"renamed: {dataflow}.py to upload.py")


if __name__ == "__main__":
    app()
