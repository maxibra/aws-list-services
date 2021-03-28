import click

from awsls import common, operations

from awsls.aws_service import AWSService


@click.command()
@click.option(
    "--get_services",
    "-s",
    is_flag=True, 
    help="Show all possible services.",
)
def main(get_services):
    session = operations.get_session()
    default_region = session.region_name
    available_services = list()
    if get_services:
        available_services = operations.get_services(session)
        if not available_services:
            print("Failed to receive services. Please verify credentials")

        # print(available_services)

    
    s = AWSService(session, 'ec2', default_region)
    print(s.service_regions())


        



