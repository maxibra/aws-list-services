# __AWS. List Services__
## Description

   Collect services details from AWS
   Python implementation
## Requirements
* python 3.8 
* pipenv
* Optional:

    * Tool to create token to work with MFA's Role in AWS: https://github.com/broamski/aws-mfa

## Running
* Change dir to your project's directory
* Create token to run the tool without MFA

        git clone https://github.com/broamski/aws-mfa
        cd aws-mfa
        ./aws-mfa --profile <profile_name> --long-term-suffix none --short-term-suffix test --device <ARN_MFA_Device_of_User> --assume-role <ARN_AWS_Role> --role-session-name run_wo_mfa


* Install and run the tool to collect service's details

        git clone https://github.com/maxibra/aws-list-services.git
        cd aws-list-services
        source ./define_aws_access.sh
        pipenv install
        pipenv shell
        python setup.py install
        ./aws-ls --help


## __TODO__ :
|ToDo|Status|
| :- | :-: |
| Code| InProgress|
| Pagination| -|
| Async| -|
| API Throttling| -|
