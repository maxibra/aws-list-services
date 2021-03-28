

class AWSService:
    def __init__(self, session, name, region):
        self.session = session
        self.client = session.client(name)
        self.name = name
        self.region = region
        

    def get_service_regions(self) -> list:
        print(self.session.get_available_regions(self.name))

    
