import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, disk_file_path, local_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
                   }
        params = {'path': disk_file_path,
                  'overwrite': 'true'
                  }
        response_load_place = requests.get(upload_url, headers=headers, params=params).json()
        href = response_load_place.get('href', '')
        response_write = requests.put(href, data=open(local_file_path, 'rb'))
        response_write.raise_for_status()
        if response_write.status_code == 201:
            print('Success')


if __name__ == '__main__':
    local_file_path = 'Task_8.txt'
    disk_file_path = 'Task_8.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(disk_file_path, local_file_path)
