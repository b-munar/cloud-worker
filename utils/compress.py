import zipfile
import tarfile
from cloud_db.models import File, Task
from database import Session
from utils.gcp_storage import download_file, upload_file
import os
from io import BytesIO

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/usr/src/app/linen-mason-384315-d051f5f132d3.json'


def compress_zip(file_id):
    session = Session()
    file_to_zip = session.query(File).filter(File.id == file_id).first() 

    file_download, content_type = download_file(bucket_name="gropo-2-nube-2023", file_name=file_to_zip.path)

    in_memory_zip = BytesIO()

    with zipfile.ZipFile(in_memory_zip, "a", zipfile.ZIP_DEFLATED, False) as zip:
        zip.writestr(file_to_zip.name, file_download)

    in_memory_zip.seek(0)
    
    upload_file(bucket_name="gropo-2-nube-2023", 
                source_file=in_memory_zip, 
                destination_file_name=f"{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip",
                content_type="application/zip"
                )

    in_memory_zip.close()
    
    task = session.query(Task).filter(Task.file_id==file_id).first()
    task.status=True
    session.commit()


def compress_targz(file_id):
    session = Session()
    file_to_tar = session.query(File).filter(File.id == file_id).first()  
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.gz", 'w:gz') as tar:
        tar.add(file_to_tar.path)
        task = session.query(Task).filter(Task.file_id==file_id).first()
        task.status=True
        session.commit()

def compress_tarbz2(file_id):
    session = Session()
    file_to_tar = session.query(File).filter(File.id == file_id).first()   
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.bz2", 'w:bz2') as tar:
        tar.add(file_to_tar.path)
        task = session.query(Task).filter(Task.file_id==file_id).first()
        task.status=True
        session.commit()
