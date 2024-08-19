"""
@Filename:  /read_userLog
@Author:    wyj
@Time:      6/8/2024 11:54 上午
@Describe:  ...
"""
import json
import os

def read_user_logs(log_dir, user_name):
    user_logs = []
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as log_file:
                #将字符串的内容反序列化成Python对象
                log_data = json.load(log_file)
                if log_data.get('user_name') == user_name:
                    user_id = log_data['request']['id']
                    timestamp = log_data.get('timestamp')
                    user_logs.append({
                        'user_id': user_id,
                        'file_name': filename,
                        'log_data': log_data,
                        'timestamp': timestamp,
                        'file_path': file_path
                    })
    user_logs.sort(key=lambda log: log['timestamp'], reverse=True)


    if user_logs:
        print(f"用户 {user_name} 的所有操作日志 ({len(user_logs)}条):")
        for log in user_logs:
            print(f"\n文件名: {log['file_name']}")
            print(f"用户 ID: {log['user_id']}")
            print("日志内容:")
            #将Python对象处理成JSON格式的字符串
            print(json.dumps(log['log_data'], indent=4, ensure_ascii=False))
    else:
        print(f"未找到用户 {user_name} 的日志。")







