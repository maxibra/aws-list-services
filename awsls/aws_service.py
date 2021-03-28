import botocore

from time import sleep

from awsls import conf

class AWSService:
    wait_time = 0

    def __init__(self, session, name, region):
        self.session = session
        self.client = session.client(name)
        self.name = name
        self.region = region
        self.details_methods = self.get_details_methods()
        self.methods_required_params = list()

    def __get_method_response(self, method_name: str) -> dict:
        """ Return any Details about the service by the specific method
            If the method require any parameter empty dict is returned
        """
        method_response = dict()
        try:
            if wait_time > 0:
                sleep(wait_time)
            method_response = getattr(self.client, method_name)()
            method_response.pop('ResponseMetadata', None)
        except botocore.exceptions.ParamValidationError as error:
            # TODO: collect methods with this error to skip them next time
            methods_required_params.append(method_name)

        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'LimitExceededException':
                AWSService.wait_time *= 2
            else:
                raise error

        return method_response
        

    def get_service_regions(self) -> list:
        """Return list of all regions the service works in them"""
        return self.session.get_available_regions(self.name)


    def get_details_methods(self) -> list:
        """Return list of all possible methodes with any details about the service"""
        # TODO: exclude methods with required parameters maybe by inspect.signature 

        return_methods = list()
        for mthd in dir(self.client):
            for prfx in conf.prefixes_detail_methods:
                if mthd.startswith(prfx) and mthd not in conf.exclude_methods_pattern:
                    return_methods.append(mthd)
        return return_methods


    

    

    

    

    
