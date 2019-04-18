import os

from .helper import is_file, to_absolute_path


def upload_to_object_store(local, bucket_name, remote, transfer_manager):
    local = to_absolute_path(local)
    if not os.path.exists(local):
        print('Path does not exist')
        return

    try:
        if is_file(local):
            local_filename = os.path.basename(local)
            remote = os.path.join(remote, local_filename)
            upload_file(local, bucket_name, remote, transfer_manager)
        else:
            upload_directory(local, bucket_name, remote, transfer_manager)
    except Exception as e:
        print(e)


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
