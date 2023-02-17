# input1 = input("Enter your First Input : ")
# input2 = input("Enter your Second Input : ")
# output1 = []
# output2 = []
# for each in input1:
#     if each not in input2:
#         output1.append(each)
# for each in input2:
#     if each not in input1:
#         output2.append(each)
#
# print("Output1 where characters present in Input1 but not in Input2 : " + ''.join(output1))
# print("Output2 where characters present in Input2 but not in Input1 : " + ''.join(output2))
#

import json
import boto3

import test


def lambda_handler(event, context):
    def publish_to_sns(msg):
        topic_arn = 'arn:aws:sns:eu-central-1:381142393247:AdminToolTest'
        sns = boto3.client("sns")
        response = sns.publish(
            TopicArn=topic_arn,
            Message=msg,
            Subject="Hi"
        )

    def final_status():
        res = "Exception raised while performing Disaster Recovery on  DBInstance with Error"
        print(res)
        publish_to_sns(f"""
            Automated Email From AWS SNS
            
            --------------------------------
            Error Message : {res}

            """)

    final_status()


import itertools
F1 = ["u1,u2", "u3,u5", "u3,u7", "u2,u1", "u7,u3", "u9,u2", "u8,u1"]
New_F1 = []
F2 = []
#Preparing list of lists
for each in F1:
    users = each.split(",")
    New_F1.append(users)


#Append the Values into New list to sort it out
for each in New_F1:
    F2.append(sorted(each))

#remove Duplicates4
F2.sort()
print("Unique List : " + str(list(k for k,_ in itertools.groupby(F2))))






