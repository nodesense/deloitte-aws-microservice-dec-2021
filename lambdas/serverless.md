
Open miniconda command prompt

```
cd aws
```


serverless to create python lambda

```
sls create --template aws-python3 --path gk_serverless_request
```

CREATE VIRTUAL ENV per python project,  mini python enviornment, that isolate 
            python library dependencies
                    PostgresQL lib 
                                2.0 -- for project 1
                                3.3 -- for project 2
            python versions
                    3.6
                    3.7
                    3.8

How to create virtual env....
```
    python -m venv c:\users\Gopalakrishnan\aws-lambda-env
```

to activate the environment,
```
    C:\Users\Gopalakrishnan\aws-lambda-env\Scripts\activate
```


newly installed packages, shall be installed inside virtual env..

```
pip install requests

```

print all the python installed package into requirements.txt 

```
pip freeze > requirements.txt
```



add below line in handler.py

```
import requests
def lambda_handler(event, context):   
    response = requests.get("https://example.com/")
    print(response.text)
    return response.text
```



packages deployed without dependencies , it won't work..

```
sls deploy
```


now, we need to have serverless to bundle all python dependencies..

create package.json [node.js dependencies ]

```
    npm init -y
```

download plugin for servess to bundle python requirements packages in zip file

```
npm install --save serverless-python-requirements
```

patch your serverless.yml file to add the plugin..

at end of serverless.yml file, add below [no indentation for plugins, custom]

```
plugins:
  - serverless-python-requirements
```


ensure funstions in serverless matches the name in python module..

handler: handler.lambda_handler



```
sls deploy
```


now check lambda, has all python dependencies from requirements.txt packaged..
