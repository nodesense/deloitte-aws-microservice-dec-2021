
https://medium.com/trackit/tutorial-how-to-create-an-api-gateway-with-python-cognito-and-serverless-1543644a836a

https://github.com/trackit/aws-api-gateway-cognito

Authorization: IdToken


1. Download the source code
2. Change config.json



```
serverless deploy
```

create user

```
aws cognito-idp admin-create-user --user-pool-id us-east-2_Y9x8Q8jMe --username gopalakrishnan.subramani@gmail.com --temporary-password AwsGk@826

```

change password

step 0: we need to enable the client to allow user to login with username and password
        in cognito, under user pool, under client settings,
          enable username/password login, check the below setting

          Enable username password based authentication
          Enable username password auth for admin APIs for authentication


step 1:to change password, user must login first time, to get session id

step 2: based on session id, the password can be changed..


step 1:to change password, user must login first time, to get session id

```
aws cognito-idp admin-initiate-auth --cli-input-json file://example-auth.json
```

step 2: change password with session copied from step 1

aws cognito-idp admin-respond-to-auth-challenge --user-pool-id us-east-2_Y9x8Q8jMe   --client-id 523405abplghsmm1hvtcng7c6 --challenge-name NEW_PASSWORD_REQUIRED --challenge-responses NEW_PASSWORD=AwsGk@742,USERNAME=gopalakrishnan.subramani@gmail.com --session   AYABeFVyaYAbVAV-s6NiIYy5V6kAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMjo0MTc1Njc5MDM0Njk6a2V5LzVjZDI0ZDRjLWVjNWItNGU4Ny05MGI2LTVkODdkOTZmY2RkMgC4AQIBAHiDgLf0JMCQi10Le18mRz-AZa5fOI0Qay69WItbdSFa4AGx1Yfh2v9twa_WtAUO0niWAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMsMWZrh46m81OAn80AgEQgDvQe5EKe8kSlKA9Mf0DADzWZ0TGeEqbZZCDL6es-3syAn7NM1hhvP_K9hfg26IwgZWV22JVqlXngVmuTgIAAAAADAAAEAAAAAAAAAAAAAAAAACd5WMtgq77puN0j05S79b3_____wAAAAEAAAAAAAAAAAAAAAEAAADU7E7fUpEyKIajEd1pf80sdZww0gLw1WKeebgLFOQaE7zfCPQQZeZzDNT14heJSC4mcw6ALJIna5hTTJaudbTJt_-PTbhQm40Yn71X5M6Uk66DAyO8Q7VSY_KMIwgdQOfqEbeq9TXbbueMFvdpngNOxHLov1pCttKwfTnUqobj2hMwsIna110U6Pu3jV3ji1dhgjNaLOwm63pUA6yIDi5H6opcvXDjvB9xZyfTko_U9cZltFowp155xz4Jm3UejYyU1jrTnYbIaRYm_6wNKmdrUd6Ohml-NQ4SswHSK27i_x4Fcmah


step 3: change password in example-auth.json

step 4: get the access, refresh an id tokens 

```
aws cognito-idp admin-initiate-auth --cli-input-json file://example-auth.json
```

Step 5: Use Postman to access secured api wiht 

    Authorization: <<IDToken>>
