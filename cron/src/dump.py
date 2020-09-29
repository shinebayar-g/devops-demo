import subprocess
import logging
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

import settings
import send_email

# 1. Dump database
def dump_database():
    print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 1 - Dumping database: " + settings.DB_NAME)

    # Username + Password included script
    cmd = subprocess.run([f"mysqldump --single-transaction --quick -h {settings.DB_HOST} -P {settings.DB_PORT} -u {settings.DB_USER} -p\"{settings.DB_PASS}\" {settings.DB_NAME} > {settings.BACKUP_FILE}"], capture_output=True, text=True, shell=True)

    # username password read from ~/.my.cnf (not working!)
    # cmd = subprocess.run([f"mysqldump --single-transaction --quick -h {settings.DB_HOST} -P {settings.DB_PORT} {settings.DB_NAME} > {settings.BACKUP_FILE}"], capture_output=True, text=True, shell=True)

    if cmd.stderr == "":
        if (cmd.stdout != ""):
            print(cmd.stdout)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 1 - Successfully dumped database: " + settings.DB_NAME)
        archive_database()
    else:
        send_email.SendErrorEmail()
        print(cmd.stderr)
        cmd = subprocess.run([f"rm {settings.BACKUP_FILE}"], capture_output=True, text=True, shell=True)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 1 - Dump error!")

# 2. Create tarball
def archive_database():
    print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 2 - Archiving database dump file: " + settings.BACKUP_FILE)
    cmd = subprocess.run(["tar -zcf " + settings.BACKUP_FILE + ".tar.gz " + settings.BACKUP_FILE], capture_output=True, text=True, shell=True)

    if cmd.stderr == "":
        if (cmd.stdout != ""):
            print(cmd.stdout)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 2 - Successfully archived dump file: " + settings.BACKUP_FILE + ".tar.gz")
        upload_file(settings.BACKUP_FILE + ".tar.gz", settings.S3_BUCKET, settings.S3_PREFIX + settings.BACKUP_FILE + ".tar.gz")
        cmd = subprocess.run(["rm " + settings.BACKUP_FILE + ".tar.gz"], capture_output=True, text=True, shell=True)
        cmd = subprocess.run(["rm " + settings.BACKUP_FILE], capture_output=True, text=True, shell=True)
    else:
        send_email.SendErrorEmail()
        print(cmd.stderr)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 2 - Archive error!")

# 3. Upload archived tarball to S3
def upload_file(file_name, bucket, object_name=None):
    print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 3 - Uploading file: " + object_name)
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 3 - Successfully uploaded to S3")
        send_email.SendEmail()
    except ClientError as e:
        logging.error(e)
        print(datetime.now().strftime('%Y/%m/%d-%H:%M:%S') + " Step 3 - Upload error!")
        send_email.SendErrorEmail()
        return False
    return True

dump_database()
