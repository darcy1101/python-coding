"""
@Filename:  /delete_userlog
@Author:    wyj
@Time:      11/8/2024 6:19 下午
@Describe:  ...
"""
import json
import os

def delete_user_logs(log_dir, user_name):
    user_logs = []
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as log_file:
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

    if len(user_logs) > 5:
        for log in user_logs[5:]:
            os.remove(log['file_path'])
        user_logs = user_logs[0: 5]