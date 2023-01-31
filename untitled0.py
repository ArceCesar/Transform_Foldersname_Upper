# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:40:43 2023
This will convert all the directory names in the "Key" column to upper case 
and replace spaces with underscores. You can use this dataframe to extract 
the directory names into Snowflake.
@author: cearce
"""

import pandas as pd 
import boto3

# Connect to S3 using boto3
s3 = boto3.client("s3")

# List all the objects in a specific bucket
result = s3.list_objects(Bucket="your-bucket-name")

# Extract the "Contents" from the result
contents = result["Contents"]

# Convert the contents to a dataframe
df = pd.DataFrame(contents)

# Convert the "Key" column to upper case
df["Key"] = df["Key"].str.upper()

# Replace spaces with underscores
df["Key"] = df["Key"].str.replace(" ", "_")

# Show the resulting dataframe
print(df)
