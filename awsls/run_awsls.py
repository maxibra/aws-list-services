import click

from awsls import common, operations

from awsls.aws_service import AWSService


session = operations.get_session()
default_region = session.region_name

@click.command()
@click.option(
    "--all_services_list",
    "-a",
    is_flag=True, 
    help="Show all possible services.",
)
@click.option(
    "--regions", 
    "-r",
    multiple=True,
    help="Regions to collect. Possible values: exact name, any prefix of a name to collect from any region contains it",
)
@click.option(
    "--services_to_collect", 
    "-s",
    multiple=True,
    help="Services to collect",
)
@click.option(
    "--output_directory", 
    "-d",
    type=str,
    default="/tmp",
    show_default=True,
    help="Directory of all outputs files",
)
def main(all_services_list, regions, services_to_collect, output_directory):
    available_services = list()

    available_services = operations.get_services(session)

    operations.create_out_dir(output_directory)
    if not available_services:
        print("Failed to receive services. Please verify credentials")
        exit(1)

    if services_to_collect:
        for srvice in services_to_collect:
            if srvice not in available_services:
                print(f"The given service {srvice} doesn't exist")
                exit(2)
        available_services = services_to_collect

    if all_services_list:
        operations.print_dict_to_file(
            collect_regions_per_services(available_services),
            f"{output_directory}/services.json"
        )
        exit(0)
    
    srvice = AWSService(session, 's3', default_region)
    # print(s.get_service_regions())

    # s.get_meta()


def collect_regions_per_services(services_names: list) -> dict:
    regions_per_service = dict()
    for service_name in services_names:
        srvice = AWSService(session, service_name, default_region)
        regions_per_service[service_name] = srvice.get_service_regions()
    return regions_per_service



