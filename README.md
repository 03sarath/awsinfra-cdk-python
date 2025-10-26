# AWS CDK Python CI/CD Pipeline Project

This project demonstrates how to create a CI/CD pipeline using AWS CDK with Python. The pipeline pulls code from GitHub and uses AWS CodeBuild to update a simple text file.

## Prerequisites

- Python 3.6 or later
- AWS CLI configured with appropriate credentials
- GitHub account and repository
- AWS CDK CLI installed (`npm install -g aws-cdk`)

## Setup Steps

1. **Initialize a new CDK project**
   ```bash
   mkdir awsinfra-cdk-python
   cd awsinfra-cdk-python
   cdk init app --language python
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # OR
   source .venv/bin/activate  # On Unix/MacOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Update requirements.txt**
   Make sure your `requirements.txt` contains:
   ```
   aws-cdk-lib==2.199.0
   constructs>=10.0.0,<11.0.0
   ```

5. **Store GitHub token in AWS Secrets Manager**
   ```bash
   aws secretsmanager create-secret --name github-token --secret-string "your-github-token"
   ```

6. **Update the stack configuration**
   - Open `awsinfra_cdk_python/awsinfra_cdk_python_stack.py`
   - Update the GitHub repository details:
     ```python
     owner='your-github-username'
     repo='your-repository-name'
     branch='your-branch-name'
     ```

7. **Synthesize CloudFormation template**
   ```bash
   cdk synth
   ```
   ```
   cdk bootstrap
   ```

8. **Deploy the stack**
   ```bash
   cdk deploy
   ```

## Project Structure

- `app.py`: The entry point for the CDK app
- `awsinfra_cdk_python/awsinfra_cdk_python_stack.py`: Contains the stack definition
- `cdk.json`: CDK configuration file
- `requirements.txt`: Python dependencies

## Pipeline Components

1. **Source Stage**
   - Pulls code from GitHub repository
   - Uses GitHub webhook for automatic triggers

2. **Build Stage**
   - Uses AWS CodeBuild
   - Updates or creates a `hello.txt` file
   - Adds timestamp and build information

## Useful Commands

- `cdk ls` - List all stacks in the app
- `cdk synth` - Emits the synthesized CloudFormation template
- `cdk deploy` - Deploy this stack to your default AWS account/region
- `cdk diff` - Compare deployed stack with current state
- `cdk destroy` - Destroy the deployed stack

## Troubleshooting

If you encounter issues:

1. **Build Script Errors**
   - Check the CodeBuild logs in AWS Console
   - Verify the build commands in the stack file

2. **GitHub Connection Issues**
   - Verify the GitHub token in AWS Secrets Manager
   - Check repository permissions
   - Ensure the webhook is properly configured

3. **CDK Deployment Issues**
   - Make sure AWS credentials are properly configured
   - Check if you have necessary permissions
   - Verify the region and account settings

## Cleanup

To remove all resources:
```bash
cdk destroy
```

## Security Notes

- Never commit sensitive information like tokens or credentials
- Use AWS Secrets Manager for storing sensitive data
- Follow the principle of least privilege when setting up IAM roles
