import vk_api
import os
import sms
from dotenv import load_dotenv
from time import sleep
load_dotenv()


ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

session = vk_api.VkApi(token=ACCESS_TOKEN)


def check_online(prev_status, current_status):
    prev_status = current_status
    user_data = session.method('users.get',
        {'user_ids': 221277111, 'fields': 'online'})
    current_status = user_data[0].get('online')
    if not prev_status and current_status:
        sms.send_sms('{} {} онлайн'.format(user_data[0].get('first_name'),
                                           user_data[0].get('last_name')))
    if prev_status and not current_status:
        sms.send_sms('{} {} оффлайн'.format(user_data[0].get('first_name'),
                                            user_data[0].get('last_name')))
    return [prev_status, current_status]


if __name__ == "__main__":
    prev_status = False
    current_status = False
    while True:
        prev_status, current_status = map(bool, check_online(prev_status,
                                                             current_status))
        sleep(60)
