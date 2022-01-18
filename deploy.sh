# Build the docker image
docker build -t 448605878489.dkr.ecr.us-east-2.amazonaws.com/fastapilambdacontainer:latest .

# Login to the AWS ECR - fastapilambdacontainer is the name of the ECR Repository
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 448605878489.dkr.ecr.us-west-2.amazonaws.com

# Push the built image
docker push 448605878489.dkr.ecr.us-west-2.amazonaws.com/fastapilambdacontainer:latest