import boto3
import json
import os

from pathlib import Path


def get_session(region='us-west-2'):
    print(os.environ['AWS_ACCESS_KEY_ID'])
    session = boto3.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=os.environ['AWS_SESSION_TOKEN'],
        region_name=region
    )

    print(session.region_name)
    return session


def get_services(session) -> list:
    return session.get_available_services()


def print_dict_to_file(dict2print: dict, file_name: str) -> None:
    with open(file_name, 'w') as out_f:
        try:
            json.dump(dict2print, out_f)
        except TypeError:
            out_f.write(str(dict2print))


def create_out_dir(file_path):
    try:
        os.stat(file_path)
    except:
        Path(file_path).mkdir(parents=True, exist_ok=True)