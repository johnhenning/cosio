import ibm_boto3
from ibm_botocore.client import Config
from ibm_s3transfer.aspera.manager import AsperaTransferManager


def create_transfer_manager(credentials):
    cos_client = ibm_boto3.client(service_name='s3',
                                  ibm_api_key_id=credentials['apikey'],
                                  ibm_service_instance_id=credentials['resource_instance_id'],
                                  ibm_auth_endpoint=credentials['auth_endpoint'],
                                  config=Config(signature_version='oauth'),
                                  endpoint_url=credentials['endpoint'])

    return AsperaTransferManager(cos_client)
