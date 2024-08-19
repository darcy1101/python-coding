"""
@Filename:  /todos
@Author:    wyj
@Time:      4/8/2024 3:22 下午
@Describe:  ...
"""
import requests
import log_service


user_name = input('请输入你的名字：')
log_service.read_user_logs(user_name)
while True:
    user_input_id = int(input('输入参数id： '))
    if user_input_id == 0:
        print(f'退出程序，{user_name} bye~')
        break
    else:
        url = 'https://jsonplaceholder.typicode.com/todos'
        params = {'id': user_input_id}
        response = requests.get(url, params=params)
        data = response.json()
        print(data)
        log_service.log_record(params, user_name, data)
        log_service.delete_user_logs(user_name)





