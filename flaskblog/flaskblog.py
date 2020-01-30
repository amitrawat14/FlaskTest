from flask import Flask, render_template, url_for
app = Flask(__name__)
import boto3

import boto3
client = boto3.client('ec2',region_name='us-east-1')
subnets = client.describe_subnets()
subnet_list = []
az_list = []

# for i in subnets['Subnets']:print(i['CidrBlock'] , i['AvailabilityZone'])
for i in subnets['Subnets']:
    subnet_list.append([i['CidrBlock'], i['AvailabilityZone'],i['AvailabilityZoneId']])
    # az_list.append(i['AvailabilityZone'])
    # subnet_list.append(i['CidrBlock'])
    # print(i['CidrBlock'] , i['AvailabilityZone'])

print(subnet_list,az_list)

# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]

posts = ['This is first post' , 'This is second post ','This is 3rd Post']
name ='amit'
job = 'time pass'

@app.route("/")
@app.route("/home")
def home():
    # return render_template('home.html', posts=posts)
    return render_template('data.html', title='Data Layer',name=name , job=job, subnets=subnet_list)

@app.route("/style")
def style():
    # return render_template('home.html', posts=posts)
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])



@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/data")
def data():
    # return render_template('data.html', title='Data Layer',name=name , job=job, subnets=subnet_list,az_list=az_list)
    # return render_template('data.html', title='Data Layer',name=name , job=job, subnets=subnets['Subnets'])
    return render_template('data.html', title='Data Layer',name=name , job=job, subnets=subnet_list)



if __name__ == '__main__':
    app.run(debug=True)