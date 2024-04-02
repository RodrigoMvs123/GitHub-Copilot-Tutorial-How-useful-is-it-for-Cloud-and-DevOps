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
