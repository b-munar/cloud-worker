import zipfile
import tarfile
from cloud_db.models import File, Task
from database import Session
from celery import Celery


app = Celery('tasks', backend='redis://broker:6379', broker='redis://broker:6379')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, queueing.s())

@app.task()
def compress_zip(file_id):
    session = Session()
    file_to_zip = session.query(File).filter(File.id == file_id).first() 
    with zipfile.ZipFile(f"{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip", 'w') as zip:
        zip.write(file_to_zip.path)
        task = session.query(Task).filter(Task.file_id==file_id).first()
        task.status=True
        session.commit()
        
@app.task()
def compress_targz(file_id):
    session = Session()
    file_to_tar = session.query(File).filter(File.id == file_id).first()  
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.gz", 'w:gz') as tar:
        tar.add(file_to_tar.path)
        task = session.query(Task).filter(Task.file_id==file_id).first()
        task.status=True
        session.commit()

@app.task()
def compress_tarbz2(file_id):
    session = Session()
    file_to_tar = session.query(File).filter(File.id == file_id).first()   
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.bz2", 'w:bz2') as tar:
        tar.add(file_to_tar.path)
        task = session.query(Task).filter(Task.file_id==file_id).first()
        task.status=True
        session.commit()

@app.task()
def queueing():
    session = Session()
    for task_to_zip in session.query(Task).filter(Task.status == False, Task.type_task==1):
        compress_zip.delay(task_to_zip.file_id)
    for task_to_targz in  session.query(Task).filter(Task.status == False, Task.type_task==2):
        compress_targz.delay(task_to_targz.file_id)
    for task_to_tarbz2 in  session.query(Task).filter(Task.status == False, Task.type_task==3):
        compress_tarbz2.delay(task_to_tarbz2.file_id)
        
        
