import os
import requests

def get_url(namespace, name, deployment_env='', user_id=''):
    if deployment_env == '':
        deployment_env = os.environ.get('sdk_deployment_env')
    if deployment_env != 'dev' and deployment_env != 'prod':
        raise ValueError("Unsupported deployment_env")
    if user_id == '':
        user_id = os.environ.get('sdk_user_id')
    if user_id is None:
        raise ValueError("Invalid user_id")
    gw = os.environ.get('sdk_workspace_gateway')
    if gw is None:
        raise ValueError("Invalid gateway")

    req_url = gw + '/api/v0.5/sdk/alpha/invocation-url' 
    params = {
        'namespace': namespace, 
        'name': name, 
        'deployment_env': deployment_env,
        'user_id': user_id
    }
    try:
        resp = requests.get(url=req_url, params=params, verify=False)
    except Exception as e:
        raise Exception("Bad gateway")

    if resp.status_code != 200:
        raise Exception("Bad gateway")
    return resp.text

