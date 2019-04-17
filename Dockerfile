FROM python:3.6

RUN pip install ibm_cos_sdk cos_aspera

ENV HOME /home
WORKDIR $HOME
ADD object_store_downloader.py .

ENTRYPOINT ["python", "object_store_downloader.py"]
