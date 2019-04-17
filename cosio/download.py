import os

from .helper import is_file


def download_from_object_store(local, bucket_name, remote, transfer_manager):
    if not os.path.exists(local):
        os.makedirs(local, exist_ok=True)
    if is_file(remote):
        remote_filename = os.path.basename(remote)
        local = os.path.join(local, remote_filename)
        download_file(local, bucket_name, remote, transfer_manager)
    else:
        download_directory(local, bucket_name, remote, transfer_manager)


def download_file(local_file, bucket_name, remote_file, transfer_manager):
    print('Downloading remote file {} from bucket {} to {}'.format(
        remote_file, bucket_name, local_file))
    future = transfer_manager.download(
        bucket_name, remote_file, local_file)
    future.result()


def download_directory(local_directory, bucket_name, remote_directory, transfer_manager):
    print('Downloading remote directory {} from bucket {} to {}'.format(
        remote_directory, bucket_name, local_directory))
    future = transfer_manager.download_directory(
        bucket_name, remote_directory, local_directory)
    future.result()
