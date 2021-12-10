change template with initial gk to your initial

```
aws cloudformation create-stack  --stack-name gk-simple-lambda-function-stack  --template-body file://./cloudformation_template.yaml  --capabilities CAPABILITY_NAMED_IAM
```

```
aws cloudformation wait   stack-create-complete    --stack-name gk-simple-lambda-function-stack
```
