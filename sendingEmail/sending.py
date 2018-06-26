import boto3

ses = boto3.client('ses')

email_from = 'nata@nata.com'
email_to = 'natal@gmail.com'
email_cc = ''
emaiL_subject = 'Subject'
email_body = 'Body'


def lambda_handler(event, context):
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )
