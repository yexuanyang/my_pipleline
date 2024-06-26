# Python3
import yaml
import xmlrpc.client
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
job_dir = os.path.join(script_dir, '../tests/jobs_defination')
rpc_url = 'http://admin:longrandomtokenadmin@10.161.28.28:9999/RPC2/'

def submit_single_job(job_path, rpc_url):
    with open(job_path) as f:
        config = yaml.dump(yaml.load(f, yaml.FullLoader))
        server=xmlrpc.client.ServerProxy(rpc_url)
        jobid=server.scheduler.submit_job(config)
        print("submit job " + str(jobid))

def submit_all_jobs_in_directory(directory, rpc_url):
    for root, dirs, files in os.walk(directory):
        for file_name in files: 
            file_path = os.path.join(root, file_name)
            submit_single_job(file_path, rpc_url)

submit_all_jobs_in_directory(job_dir, rpc_url)
