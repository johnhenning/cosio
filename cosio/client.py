import ibm_boto3
from ibm_botocore.client import Config
from ibm_s3transfer.aspera.manager import AsperaTransferManager
from ibm_s3transfer.manager import TransferManager
from ibm_s3transfer.aspera.manager import AsperaConfig


def create_client(credentials):
    return ibm_boto3.client(service_name='s3',
                            ibm_api_key_id=credentials['apikey'],
                            ibm_service_instance_id=credentials['resource_instance_id'],
                            ibm_auth_endpoint=credentials['auth_endpoint'],
                            config=Config(signature_version='oauth'),
                            endpoint_url=credentials['endpoint'])


def create_aspera_transfer_manager(credentials):
    cos_client = create_client(credentials)
    ms_transfer_config = AsperaConfig(multi_session=2,
                                      multi_session_threshold_mb=60)
    return AsperaTransferManager(cos_client, transfer_config=ms_transfer_config)


def create_transfer_manager(credentials):
    cos_client = create_client(credentials)
    return TransferManager(cos_client)
