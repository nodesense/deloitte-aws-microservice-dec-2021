change template with initial gk to your initial

```
aws cloudformation create-stack  --stack-name gk-simple-lambda-function-stack  --template-body file://./cloudformation_template.yaml  --capabilities CAPABILITY_NAMED_IAM
```

```
aws cloudformation wait   stack-create-complete    --stack-name gk-simple-lambda-function-stack
```


```
aws cloudformation create-stack  --stack-name gk-s3-trigger-lambda-function-stack  --template-body file://./s3-trigger.yaml  --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=BucketName,ParameterValue=gk2022-bucket
```


sample.json

```
{
    "name": "Gopal",
    "training": "AWS"
}
```
