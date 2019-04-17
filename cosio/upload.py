import os

from .helper import is_file


def upload_to_object_store(local, bucket_name, remote, transfer_manager):
    if not os.path.exists(local):
        os.makedirs(local, exist_ok=True)

    try:
        if is_file(local):
            local_filename = os.path.basename(local)
            remote = os.path.join(remote, local_filename)
            upload_file(local, bucket_name, remote, transfer_manager)
        else:
            upload_directory(local, bucket_name, remote, transfer_manager)
    except Exception as e:
        print(e.args)
        # print(e)


def upload_file(local_file, bucket_name, remote_file, transfer_manager):
    print('Uploading file {} to bucket {} as {}'.format(
        local_file, bucket_name, remote_file))
    future = transfer_manager.upload(local_file, bucket_name, remote_file)
    future.result()


def upload_directory(local_directory, bucket_name, remote_directory, transfer_manager):
    print('Uploading local directory {} to bucket {} as {}'.format(
        local_directory, bucket_name, remote_directory))

    future = transfer_manager.upload_directory(local_directory, bucket_name, remote_directory)
    future.result()
