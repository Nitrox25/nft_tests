import random
import time

import pytest
import allure
from FrontPages import SearchHelper
from api import get_event_by_name, get_event_by_collection_id


@pytest.fixture(scope="module")
def setup(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.authorization()
    main_page.enter_password(words="1234")
    main_page.enter_button().click()
    main_page.go_to_site()
    return main_page


@pytest.mark.parametrize("name, symbol, token_url", [
    ("test_name1", "sym1", "https://url1.com"),
])
def test_collection(setup, name, symbol, token_url):
    main_page = setup
    with allure.step(""):
        main_page.enter_collection_name(words=name)
        main_page.enter_collection_symbol(words=symbol)
        main_page.enter_collection_token_url(words=token_url)
        main_page.buttons_send_to()[0].click()

        main_page.wait_for_new_window()
        main_page.notification()
        main_page.enter_button_conform().click()
        main_page.go_to_site()
        last_event = get_event_by_name(name)
        assert last_event['name'] == name
        assert last_event['symbol'] == symbol
        assert last_event['eventName'] == 'CollectionCreated'
        assert last_event['collection'] in main_page.select_last_event().text


@pytest.mark.parametrize('collection_address, recipient_address',
                         [('test_name1', '0x8b37ACE77Fc4837f0507eF4f5B78E4164aF29Ef7'),
                          ])
def test_NFT(setup, collection_address, recipient_address):
    main_page = setup
    token_id = random.randint(1, 10 ** 6)
    if not collection_address.startswith('0x'):
        last_event = get_event_by_name(collection_name=collection_address)
        collection_address = last_event['collection']

    main_page.enter_collection_address(words=collection_address)
    main_page.enter_recipient_address(words=recipient_address)
    main_page.enter_token_id(words=token_id)
    main_page.buttons_send_to()[1].click()
    main_page.wait_for_new_window()
    main_page.notification()
    main_page.enter_button_conform().click()
    main_page.go_to_site()

    event = get_event_by_collection_id(collection_id=collection_address, token_id=token_id)

    assert event['collection'] == collection_address
    assert event['recipient'] == recipient_address
    assert event['tokenId'] == token_id
    assert event['eventName'] == 'TokenMinted'

    assert collection_address in main_page.select_last_event().text
    assert recipient_address in main_page.select_last_event().text
    assert str(token_id) in main_page.select_last_event().text
