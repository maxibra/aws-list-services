import boto3
import os


def get_session():
    session = boto3.Session(
        aws_access_key_id='asdsad',
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=os.environ['AWS_SESSION_TOKEN'],
    )

    print(session.region_name)
    return session

def get_services(session) -> list:
    return session.get_available_services()