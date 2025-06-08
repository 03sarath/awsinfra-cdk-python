import aws_cdk as cdk
from aws_cdk import assertions

from awsinfra_cdk_python.awsinfra_cdk_python_stack import AwsinfraCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in awsinfra_cdk_python/awsinfra_cdk_python_stack.py
def test_sqs_queue_created():
    app = cdk.App()
    stack = AwsinfraCdkPythonStack(app, "awsinfra-cdk-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
