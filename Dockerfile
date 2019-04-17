FROM python:3.6

RUN pip install ibm_cos_sdk cos_aspera

ENV HOME /home
WORKDIR $HOME
ADD download_object_store_directory.py .

ENTRYPOINT ["python", "download_object_store_directory.py"]
