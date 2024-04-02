# GitHub-Copilot-Tutorial-How-useful-is-it-for-Cloud-and-DevOps

https://www.youtube.com/watch?v=9JGONx_X4ho 

https://raw.githubusercontent.com/RodrigoMvs123/GitHub-Copilot-Tutorial-How-useful-is-it-for-Cloud-and-DevOps/main/README.md

What is Github Copilot

Ai assistant for coding - developed by GitHub
GitHub is available as an extension in your code editor or IDE
Helps you write your code within your editor 

How GitHub Copilot works 

Context-aware and specifically designed for software development 

AI models provide better answers when they have more context 

Gathers context from your code to answer your questions 

Context is NOT your entire codebase

GitHub Copilot gathers context from
Current open file
Other open tabs in the IDE
File name and type
Repository URLs or file paths

Other ways of context
Highlighted code 
Previous questions and responses

How does it work behind the scenes ?
Powered by a Generative AI Model developed by GitHub, OpenAI and Microsoft
LLM = Large Language Model trained to understand and replicate the syntax, patterns and paradigms in human-generated code
Trained on billions of lines of code in public repositories
Trained on all programming languages ( the more available or a specific language, the better the suggestions )

Different ways of Interaction

1 - Copilot Chat

Replies to your request
You ask to explain code, improve existing code, generate tests etc.

2 - Autocomplete code suggestions

Typing code and AI autocompletes it
Code suggestion presented to accept or reject 
Constructs a prompt from your context

Code Suggestions
Tries to give you recommendation and useful next steps

GitHub Copilot
Visual Studio Code
Pulumi / Python ( Infrastructure as a Code Tool )

AWS - https://aws.amazon.com/ 
Pulumi Installed - https://www.pulumi.com/docs/install/ 
Install Python - https://www.python.org/downloads/ 
Download Visual Studio Code - https://code.visualstudio.com/download 
Setup GitHub Copilot - https://github.com/features/copilot 
Visual Studio Code - GitHub Copilot Extension

Visual Studio Code
Terminal
pulumi new aws-python

https://app.pulumi.com/account/tokens 

Pulumi UI

Personal Access Token 
Create Token
aws-python ( Copy )

Terminal 
Past

project name (copilot-pulumi):
…
…
…
…
eu-west-2

Visual Studio Code
Explorer
Open Editors
test.py

test.py
Press x I to ask GitHub Copilot Chat to do something. Start typing to dismiss 

ctrl + I
Ask Copilot or type / for commands

Visual Studio Code
Explorer
Open Editors
test.py
__main__.py

__main__.py
import pulumi
from pulumi-aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket 
pulumi.export('bucket_name', bucket.id)

Github Copilot Chat
create 10 s3 buckets with unique names

Visual Studio Code
Explorer
Open Editors
test.py
__main__.py

__main__.py
import pulumi
from pulumi-aws import s3

# Create 10 AWS resources (S3 Buckets)
for i in range(1, 11):
    bucket = s3.Bucket(f'my-bucket-{i}')

    # Export the name of the bucket 
pulumi.export(f'bucket_name_{i}', bucket.id)

Visual Studio Code
Explorer
Open Editors
test.py
__main__.py

__main__.py
import pulumi
# import s3 and ec2 modules from pulumi_aws package 
from pulumi_aws import s3, ec2 

# create 10 s3 bucket with unique names
for i in range(10):
    bucket = s3.Bucket(f"my-bucket-{i}")
    pulumi.export(f"bucket_{i}_name", bucket.id)

# create 5 ec2 instances for my web application 
for i in range(5):
    instance = ec2.Instance(f"my-instance-{i}", 
        # use  t2.small instance type
        instance_type="t2-small",
        # use Ubuntu 18.04 LTS
        ami="ami-0ac80df6eff0e70b5",
        tags={
            "Name": f"my-instance-{i}",
        })
    pulumi.export(f"instance_{i}_id", instance.id)

Limitations

GitHub Copilot is not up-to-date
If tools release new versions, Copilot does not know about it
Cut-Off Knowledge is 2021

Extension Voice Command 

Visual Studio Code Speech 















