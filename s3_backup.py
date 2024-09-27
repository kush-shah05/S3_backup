import boto3

s3 = boto3.resource('s3')

def showbuckets(s3):
    for bucket in s3.buckets.all():
        print(bucket)

def createbucket(s3):
    # Remove CreateBucketConfiguration for us-east-1 region
    s3.create_bucket(Bucket='pythonfordevopsbykush')
#C:\Users\Kush\OneDrive\Desktop\DevOps2024\Linux\backup_20240924_201054.tar.gz
def uploadbackup(s3):
    data=open(r'C:\Users\Kush\OneDrive\Desktop\DevOps2024\Linux\backup_20240924_201054.tar.gz','rb')
    s3.Bucket('pythonfordevopsbykush').put_object(Key='my_backup.tar.gz',Body=data)
    print('backed up successfully!!')
uploadbackup(s3)
#createbucket(s3)
#showbuckets(s3)
