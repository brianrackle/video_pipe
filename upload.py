#!/usr/bin/python3

import boto3
import argparse
import re

def AWSKeys(keyfilepath):
    accesskeyid = None
    secretkey = None

    keyfile = open(keyfilepath, 'r')
    for line in keyfile:
        accesskeyidmatch = re.match('AWSAccessKeyId=(.*)', line)
        if accesskeyidmatch:
            accesskeyid = accesskeyidmatch.group(1)

        secretkeymatch = re.match('AWSSecretKey=(.*)', line)
        if secretkeymatch:
            secretkey = secretkeymatch.group(1)
    
    return accesskeyid, secretkey


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyfile')
    parser.add_argument('--upload')
    parser.add_argument('--name')
    parser.add_argument('--bucket')
    args = parser.parse_args()

    accesskeyid, secretkey = AWSKeys(args.keyfile)
    s3client = boto3.client('s3', aws_access_key_id=accesskeyid, aws_secret_access_key=secretkey) #region_name
    s3client.upload_file(args.upload, args.bucket, args.name)
    return

if __name__ == "__main__":
    main()