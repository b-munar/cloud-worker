import zipfile
import tarfile
from cloud_db.models import File, Task
from database import Session
from utils.gcp_storage import download_file, upload_file
import os
import shutil

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/usr/src/app/linen-mason-384315-d051f5f132d3.json'


def compress_zip(file_id):
    session = Session()
    file_to_zip = session.query(File).filter(File.id == file_id).first() 

    os.makedirs(f"/{file_to_zip.dir}", exist_ok=True)

    download_file(bucket_name="gropo-2-nube-2023", file_cloud_name=file_to_zip.path)
    
    with zipfile.ZipFile(f"/{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip", 'w') as zip:
        zip.write(f"/{file_to_zip.path}")


    upload_file(bucket_name="gropo-2-nube-2023", 
                source_file=f"/{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip", 
                destination_file_name=f"{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip",
                content_type="application/zip"
                )

    shutil.rmtree(f"/{file_to_zip.dir}")
    
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
