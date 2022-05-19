# github-actions-with-aws-sam

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
github-actions-with-aws-sam$ sam local start-api
github-actions-with-aws-sam$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
github-actions-with-aws-sam$ sam logs -n HelloWorldFunction --stack-name github-actions-with-aws-sam --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
github-actions-with-aws-sam$ pip install -r tests/requirements.txt --user
# unit test
github-actions-with-aws-sam$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
github-actions-with-aws-sam$ AWS_SAM_STACK_NAME=<stack-name> python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name github-actions-with-aws-sam
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

## Pasos

```
python3 -m venv venv/
source venv/bin/activate
# para desactivar
deactivate

# https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
export ARCHFLAGS="-arch x86_64"
pip3 install cx_Oracle --upgrade --user

```

## Pasos lambda layer oracle cli python

```
# https://github.com/dennisoft/cxoracle
mkdir LAMBDA-PYTHON-LAYER
cd LAMBDA-PYTHON-LAYER/
sudo yum update -y
sudo yum install python3 -y
mkdir ~/oracle_cli_layer_python
mkdir oracle_cli_layer_python
cd oracle_cli_layer_python/
mkdir python/ lib/
pip-3.7 install cx_Oracle -t python/
wget https://download.oracle.com/otn_software/linux/instantclient/193000/instantclient-basic-linux.x64-19.3.0.0.0dbru.zip -O oracle.zip
unzip -j oracle.zip -d lib/
cp /lib64/libaio.so.1 lib/libaio.so.1
zip -r -y layer-lambda-python-oracle-cli.zip python/ lib/
aws s3 cp layer-lambda-python-oracle-cli.zip s3://bx-dev-lambda-layers/layer-lambda-python-oracle-cli.zip --region us-west-2
```


## Publish lambda
```
aws lambda publish-layer-version --layer-name cx_Oracle --description "BX cx_Oracle python layer" --content S3Bucket=bx-dev-lambda-layers,S3Key=layer.zipcompatible-runtimes python3.7 --region us-west-2
```

## publish layer

```
# https://docs.aws.amazon.com/cli/latest/reference/lambda/publish-layer-version.html
aws lambda publish-layer-version \
--layer-name bx-python-cx_Oracle  \
--description "bx-python-cx_Oracle"  \
--content S3Bucket=bx-dev-lambda-layers,S3Key=layer-lambda-python-oracle-cli.zip  \
--compatible-runtimes "python3.7"
--region us-west-2
```

output

´´´
{
    "Content": {
        "Location": "https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/311028179126/bx-python-cx_Oracle-8bf08dd3-0836-40fc-863b-57e7193690ca?versionId=sleX72RmdX8n2CW9YS7CB5BirtLiKwgr&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCiLVh4ORNqhxF0pyKh%2F25F%2FZjezRLB%2B8FV2%2FnGuAMb2wIgQJQQVjPgnm0LaChdKbjOItSj7dQUCH4wLXGJLsAsIqoq2wQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAEGgw1MDIyOTcwNzYxNjMiDIKcUZ3bZ%2FdM%2FzNzISqvBKBB2vLCBnQHDs3is72esb2VpzJ7O8GQz2kxmiWQF1X13W%2BNpDgrqVZeaz11I5H16BMzJjfYkPCw0iGae05VO4q818lep1fIymI%2B2vccd%2FunCOlsZ7jO10iueFcz9IeNt9oLwOLc5H0nG%2BSwka1acU6MAGC%2BCfOc%2BvL0KQMk34kOT4sWZqN2tH%2FcE074GTjIjCJMRpxO%2Bcf75vVm2rO94UNMAfs8V%2BclJIiZrEkuXpjtylCjMGfX6j5P7hhAwPRcX6Sf4fyY1tE2jN2biMksUw5cKn7BIrUBjwBgqTQdPOJEM0iWprWLdJcHe3DvSI%2F3o%2B7ofg4d8yAhPlIgS1Bovmd4V5SHFpXDmfYyLQtrJ9XADXxj1M60Mji%2BpmtiC3TXOzg%2BixGxJxGdJM5WJFO4smUfc4ao4V%2BBz5JgZtZDl9ir7Q3jEWtn0EBWhwFrhfDoZldtWCbGrhYUsjK5ZgppQdAX1LogHFXClB2Ctn1uQeG3fUjPpRtfsZWF12aWElDuzf%2BGb%2FztA9YjxNMYfEV%2BUJOQhJN3bqNGtigsMMjST91vMUR9uQKd%2FYCKxoEjd4wH1HX05B6vMcoAzUPbxxD53JuoBD3MauAX%2Fvummi2wJxgh%2F5p1kc79zM5zXavPff9KFrOfam%2BAs9yBDPWimSvVai5yYZJn6SpftUX58fAfZyQAN6CvDvsDF1eySmNXBb71afL6I9FveA4RaRilQg8ZpQ9m0YvjmFFXHXoXFwKqEn4w1LqYlAY6qQEggNMmLS7A1%2BSRqmmROOhlkTpZVcJrIpPVy6aapRHm562m5JMHO9bsOWLbJlki84AniMbmaLA0vPoYPSGzeU%2F61%2FtQEpnVlYdD%2FBwtqh1htcz32GHsmW%2B6zQYJ5j32IfUeVP9UaI%2FIfjhg0IXnfF6tSjOVe15um%2FWDD8B37lh2Q%2Fr8Hqzb2sFB44mDzIjPRN3OW%2Bc3AXHpfSmvX0z5BNI2xf%2FNMfYy7dCK&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220519T122545Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAXJ4Z5EHBRKJNBZEN%2F20220519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=4e9a33b01900f2af0e7f602c5a7f7b4f858117f6a56626ef390ff3d31cf12545",
        "CodeSha256": "wdvI6/Kf3c/4dybdyScB7YY6cPpv5P3CHVqnmABRw2w=",
        "CodeSize": 75962415
    },
    "LayerArn": "arn:aws:lambda:us-west-2:311028179126:layer:bx-python-cx_Oracle",
    "LayerVersionArn": "arn:aws:lambda:us-west-2:311028179126:layer:bx-python-cx_Oracle:2",
    "Description": "bx-python-cx_Oracle",
    "CreatedDate": "2022-05-19T12:25:56.618+0000",
    "Version": 2,
    "CompatibleRuntimes": [
        "python3.7"
    ]
}
´´´