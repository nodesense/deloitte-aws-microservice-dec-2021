
mkdir lambda-requests

cd lambda-requests


pip install --target . requests

create a file lambda_function.py inside lambda-requests

```
import requests
def lambda_handler(event, context):   
    response = requests.get("https://example.com/")
    print(response.text)
    return response.text
```


created a lambda function  gk-lambda-request python 3.9, GK_LAMBDA_ROLE


compress the folder lambda-request into lambda-request.zip

or PowerShell to compress 
Window start -> PowerShell

cd aws
cd lambda-request

Compress-Archive -Path .\* -DestinationPath .\lambda-request.zip


aws lambda update-function-code --function-name gk-lambda-request --zip-file fileb://lambda-request.zip
