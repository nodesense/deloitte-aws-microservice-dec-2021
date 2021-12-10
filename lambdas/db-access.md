### Working with db, mysql, postgresql, aurora, redshift

```
mkdir lambda-dbaccess

cd lambda-dbaccess

pip install --target . PyMySQL
pip install --target . pg8000
```

create file lambda_function.py

paste below code

```
def lambda_handler(event, context):   
    return "Working"
```

In powershell, or compress using winzip/7zip, ensure lambda_function in the root of archive

```
Compress-Archive -Path .\* -DestinationPath .\lambda-dbaccess.zip
```
```
aws lambda update-function-code --function-name gk_lambda_dbaccess --zip-file fileb://lambda-dbaccess.zip
```
