from boto3 import resource
from os import environ
from pprint import pprint


aws_access_key_id=environ.get('AWS_ACCES_KEY_ID', "402553776944")
aws_secret_access_key=environ.get('AWS_SECRET_ACCESS_KEY', "#Benman98")
region_name=environ.get('REGION_NAME', "eu-north-1")


pprint(
    [
        aws_access_key_id,aws_secret_access_key,region_name
    ]
)

dynamodb = resource(
    "dynamodb",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)


tables = [
    {
        "TableName": "Song",
        
        "AttributeDefinitions": [
            {
                'AttributeName': 'LoaderId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SongId',
                'AttributeType': 'S'
            }
        ],

        "KeySchema": [
            {
                'AttributeName': 'LoaderId',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SongId',
                'KeyType': 'RANGE'
            },

        ],
    },
]


def create_tables():

    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:

        print(e)
