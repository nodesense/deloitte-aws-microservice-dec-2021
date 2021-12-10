
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

