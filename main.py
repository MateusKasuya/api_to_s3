import boto3

s3 = boto3.client("s3")

s3.upload_file('kasuya_acess_keys.txt', 'smartbetting', 'Credenciais/kasuya_acess_keys.txt')