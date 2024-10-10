import boto3
from keys import ACCESS_KEY, SECRET_KEY

bucket_name = "aws-dantor-1"

def connectS3():
    session_aws = boto3.session.Session(ACCESS_KEY,SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print("Successful connection")
    return session_s3

def save_photo(photo, id):
    photo_name = id + ".jpg"
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    return photo_path, photo_name

def upload_photo(photo_path, photo_name):
    session_s3 = connectS3()
    session_s3.meta.client.upload_file(photo_path, bucket_name, photo_name)
    print ("uploaded")
    return

def get_files():
    session_s3 = connectS3()
    bucket_s3 = session_s3.Bucket(bucket_name)
    all_objects = bucket_s3.objects.all()
    for obj in all_objects:
        print(obj.key)
