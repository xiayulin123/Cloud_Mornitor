import boto3

ecr_clien = boto3.client('ecr')
repository_name = "my-cloud-native-repo"

response = cecr_lient.create_repository(

    repositoryName=repository_name

)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)