import argparse

import cosio


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('task', choices=['upload', 'download'], help='decide which task you want to run')
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
    credentials = cosio.helper.load_credentials(args.credentials)
    print('Connecting to IBM Object Storage')
    transfer_manager = cosio.client.create_aspera_transfer_manager(credentials)
    if args.task == 'upload':
        cosio.upload.upload_to_object_store(args.local, args.bucket, args.remote, transfer_manager)
    else:
        cosio.download.download_from_object_store(args.local, args.bucket, args.remote, transfer_manager)


if __name__ == "__main__":
    main()
