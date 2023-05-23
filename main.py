import vk_api, time

token = "" #Токен с доступом к отсылу сообщений
text = "" #В ковычки текст, который будет выводиться
ids = [] #айди беседы через запятую. Пример: [1, 2, 3]

vk = vk_api.VkApi(token=token)


def main():
    while True:
        time.sleep(3600) # Ждем один час
        for i in ids:
            try: # Пытаемся выполнить
                vk.method('messages.send', {'chat_id': i, 'message': text, "random_id": 0})
            except Exception as e: #Если выбивает ошибку, то выводим её
                print(e)


if __name__ == '__main__':
    main()
