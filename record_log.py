"""
@Filename:  /log
@Author:    wyj
@Time:      4/8/2024 5:30 下午
@Describe:  ...
"""
import json
import os
from datetime import datetime


def log_record(request, user_name, response_data, log_dir='/Users/wangyanjun/Desktop/pythonProject/logs'):
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
