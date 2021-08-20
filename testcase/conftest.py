import requests


def login(user='18503008150', password=None):
    """登录获取token"""
    url = 'https://test-api.codemao.cn/tiger/v3/web/accounts/login'
    data = {
        "identity": user,
        "password": password if password else '123456',
        "pid": "65edCTyg"
    }
    response = requests.post(url, json=data).json()
    token = response['auth']['token']
    print(response)
    return token


def insert_works(works_name, works_url, token, cover=None):
    """插入云端作品到账号中"""
    url = 'https://test-api.codemao.cn/nemo/v3/works/upload/1'
    headers = {
        'Content-Type': 'application/json',
        'authorization': f'Bearer {token}'
    }
    data = {
        "name": works_name,
        "preview": cover if cover else "https://dev-static-onlyfortest.codemao.cn/nemo/Bkp5Xqf2V.cover",
        "work_url": works_url,
        "n_blocks": 3,
        "n_roles": 3,
        "template_id": 201,
        "template_type": 3,
        "bcm_version": "0.5",
        "cloud_variables": []
    }
    response = requests.post(url, headers=headers, json=data).json()
    print(response)
