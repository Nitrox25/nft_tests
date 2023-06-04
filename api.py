import time
import requests


def get_event_by_name(collection_name, timeout=120):
    start_time = time.time()  # начальное время

    while True:
        response = requests.get('http://127.0.0.1:4000/events')
        response.raise_for_status()
        events = response.json()
        for event in events:
            if event['name'] == collection_name:
                return event

        if time.time() - start_time > timeout:  # если время ожидания превысило заданный тайм-аут
            raise TimeoutError(f"Event with collection name '{collection_name}' was not found within {timeout} seconds")

        time.sleep(1)  # подождите одну секунду перед следующим запросом


def get_event_by_collection_id(collection_id, token_id, timeout=120):
    start_time = time.time()

    while True:
        response = requests.get('http://127.0.0.1:4000/events')
        response.raise_for_status()
        events = response.json()
        for event in events:
            # добавляем проверку на наличие 'tokenId' в событии
            if 'tokenId' in event and event['collection'] == collection_id and event['tokenId'] == token_id:
                return event

        if time.time() - start_time > timeout:  # если время ожидания превысило заданный тайм-аут
            raise TimeoutError()

        time.sleep(1)  # подождите одну секунду перед следующим запросом
