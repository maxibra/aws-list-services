import click

from awsls import common, conf, operations

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
    "-o",
    type=str,
    default="/tmp",
    show_default=True,
    help="Directory of all outputs files",
)
@click.option(
    "--full_details",
    "-d",
    is_flag=True, 
    help="Collect possible details about services.",
)
def main(all_services_list, regions, services_to_collect, output_directory, full_details):
    available_services = list()

    available_services = operations.get_services(session)
    all_regions = AWSService(session, 's3', default_region).get_service_regions()
    if not all_regions:
        print("Failed to receive all regions. Please verify credentials")
        exit(1)       

    operations.create_out_dir(output_directory)
    if not available_services:
        print("Failed to receive services. Please verify credentials")
        exit(2)

    regions_to_collect = all_regions
    if regions:
        regions_names = list()
        for prefix_rgion in regions:
            for rgion in all_regions:
                if rgion.startswith(prefix_rgion):
                    regions_names.append(rgion)
        if not regions_names:
            print(f"Bad regions prefixes: {regions}")
            exit(3)
        else:
            regions_to_collect = regions_names
    print(f"{regions_to_collect}")


    if services_to_collect:
        for srvice in services_to_collect:
            if srvice not in available_services:
                print(f"The given service {srvice} doesn't exist")
                exit(4)
        available_services = services_to_collect


    if all_services_list:
        operations.print_dict_to_file(
            collect_regions_per_services(available_services),
            f"{output_directory}/services.json"
        )

    if full_details:
        for rgion in regions_to_collect:
            collected_details = dict()
            session_of_region = operations.get_session(rgion)
            print(session_of_region)
            for srvice in available_services:
                s = AWSService(session_of_region, srvice, rgion)
                collected_details[srvice] = s.collect_detailed_methods()
            print(f"Before Print: {type(collected_details)}")
            operations.print_dict_to_file(
                collected_details,
                f"{output_directory}/{rgion}_services_details.json"
            )



def collect_regions_per_services(services_names: list) -> dict:
    regions_per_service = dict()
    for service_name in services_names:
        srvice = AWSService(session, service_name, default_region)
        regions_per_service[service_name] = srvice.get_service_regions()
    return regions_per_service



