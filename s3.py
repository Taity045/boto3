import boto3
s3 = boto3.client('s3')

s3 = boto3.client(
    's3',
    aws_access_key_id = '',
    aws_secret_access_key = ''
)

bucket = raw_input('Enter your bucket name')
key = raw_input('Enter your desired filename/key for this upload')

print('Generating pree\-signed url...')

print(s3.generate_presigned_url('put_object',Params={'Bucket':bucket,'Key':key}, ExpireIn=3600, HttpMethod='PUT'))