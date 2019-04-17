import argparse
import json
import os.path
import ibm_boto3
from ibm_botocore.client import Config
from ibm_s3transfer.aspera.manager import AsperaTransferManager


def download_directory(local_directory, bucket_name, remote_directory, transfer_manager):
    if not os.path.exists(local_directory):
        os.makedirs(local_directory, exist_ok=True)
    future = transfer_manager.download_directory(
        bucket_name, remote_directory, local_directory)
    future.result()


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('local', type=str,
                        help='local directory to save downloaded folder')
    parser.add_argument('bucket', type=str,
                        help='remote bucket to download from')
    parser.add_argument('remote', type=str,
                        help='Remote directory to download')
    parser.add_argument('credentials', type=str,
                        help='credentials file for cloud object storage')
    return parser.parse_args()


def main():
    args = parse_args()
    credentials = load_json(args.credentials)
    print('Connecting to IBM Object Storage')
    cos_client = ibm_boto3.client(service_name='s3',
                                  ibm_api_key_id=credentials['apikey'],
                                  ibm_service_instance_id=credentials['resource_instance_id'],
                                  ibm_auth_endpoint=credentials['auth_endpoint'],
                                  config=Config(signature_version='oauth'),
                                  endpoint_url=credentials['endpoint'])

    transfer_manager = AsperaTransferManager(cos_client)
    print('Downloading directory {args.remote} from bucket {args.bucket} to {args.local}'.format(
        args=args))
    download_directory(args.local,
                       args.bucket,
                       args.remote,
                       transfer_manager)


if __name__ == "__main__":
    main()
