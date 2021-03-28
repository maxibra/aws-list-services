#!/bin/bash

role_suffix="run_wo_test"
aws_credentials="$HOME/.aws/credentials"

export AWS_ACCESS_KEY_ID=$(grep -A5 "\-${role_suffix}" ${aws_credentials}|grep aws_access_key_id|awk '{print $3}')
export AWS_SECRET_ACCESS_KEY=$(grep -A5 "\-${role_suffix}" ${aws_credentials}|grep aws_secret_access_key|awk '{print $3}')
export AWS_SESSION_TOKEN=$(grep -A5 "\-${role_suffix}" ${aws_credentials}|grep aws_session_token|awk '{print $3}')
