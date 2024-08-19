"""
@Filename:  /log_service
@Author:    wyj
@Time:      11/8/2024 6:47 下午
@Describe:  ...
"""
import json
import os
from datetime import datetime

LOG_DIR = "./logs"


def read_log_list(user_name, log_dir=LOG_DIR):
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

    return user_logs


def delete_user_logs(user_name):
    user_logs = read_log_list(user_name)

    if len(user_logs) > 5:
        for log in user_logs[5:]:
            os.remove(log['file_path'])


def read_user_logs(user_name, log_dir=LOG_DIR):
    user_logs = read_log_list(user_name)

    if user_logs:
        print(f"用户 {user_name} 的所有操作日志 ({len(user_logs)}条):")
        for log in user_logs:
            print(f"\n文件名: {log['file_name']}")
            print(f"用户 ID: {log['user_id']}")
            print("日志内容:")
            print(json.dumps(log['log_data'], indent=4, ensure_ascii=False))
    else:
        print(f"未找到用户 {user_name} 的日志。")


def log_record(request, user_name, response_data, log_dir=LOG_DIR):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_filename = os.path.join(log_dir, f"{timestamp}.json")
    log_data = {
        "user_name": user_name,
        "timestamp": timestamp,
        "request": request,
        "response_data": response_data
    }
    with open(log_filename, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=4)
