Ref:

a. ```https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/```

b. ```https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html```

### Step 1: Create an AWS Identity and Access Management (IAM) role
1. Open the IAM Management Console. Select Roles from the left navigation pane and then choose Create role.

2. On the Create role screen, under Trusted entity type, keep AWS service selected. Under Use case, search Step Functions in the dropdown and select Step Functions. Choose Next.

3. In the Add permissions section, choose Next.

In the Name, review, and create section, in Role name, enter **step_functions_basic_execution**. Choose Create role.

### Step 2: Create your Lambda functions
1. Open the AWS Lambda console. Choose Create function.

2. Select Author from scratch.

3. Configure your first Lambda function with these settings :

    Name – my-function.

    Runtime – Python 3.9.

    Role – Choose an existing role.

    Existing role – lambda-role.

4. Choose Create function.

5. To configure a test event, choose Test.

6. For Event name, enter test.

7. Choose Save changes.

8. To invoke the function, choose Test.






