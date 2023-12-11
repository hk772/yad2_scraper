import re


def get_feed_items(soup):
    post_items = soup.find_all('div', class_='post-item')
    feed_list = soup.find_all("div", class_="feed_list")
    _items = feed_list[0].find_all_next(class_="feeditem table")
    return _items


def find_element_by_regular_exp(_soup, exp):
    _pattern = re.compile(exp)
    element = _soup.find(id=_pattern)
    value = element.contents[0]
    return value


def extract_middle_col(_soup):
    _room_num = find_element_by_regular_exp(_soup, r'data_rooms_\d+')
    _floor = find_element_by_regular_exp(_soup, r'data_floor_\d+')
    _size = find_element_by_regular_exp(_soup, r'data_SquareMeter_\d+')

    return _room_num, _floor, _size


def extract_address(item):
    pattern = re.compile(r'([\s\S]+?)\s+(\d+)')

    # Match the pattern in the string
    try:
        match = pattern.match(item.strip())
        _street_name = match.group(1).strip()
        street_number = match.group(2)
    except:
        _street_name = item.strip()
        street_number = None
    return _street_name, street_number


def extract_col1(_soup):
    address_element = _soup.find(id=re.compile(r'feed_item_(\d+)_title'))
    title_contents = address_element.findNext(class_='title').contents
    _street_name, _street_num = extract_address(title_contents[0])

    _subtitle = address_element.next_sibling.next_sibling.contents[0]
    split_subtitle = _subtitle.split(",")
    _property_type = split_subtitle[0]
    if len(split_subtitle) > 2:
        _area = split_subtitle[1]
        _city = split_subtitle[2]
    else:
        _area = None
        _city = split_subtitle[1]

    return _street_name, _street_num, _property_type, _area, _city


# save_html_to_file(html_content, "yad2_snapshot.html")


def parse_items_from_page(soup):
    items = get_feed_items(soup)
    extracted_item_list = {}
    i = 0
    for item in items:
        col1 = item.findNext(class_='right_col')
        street_name, street_num, property_type, area, city = extract_col1(col1)

        col2 = item.findNext(class_='middle_col')
        room_num, floor, size = extract_middle_col(col2)

        col3 = item.findNext(class_='left_col with_new_tab')
        price_str = find_element_by_regular_exp(col3, r'feed_item_(\d+)_price').strip()

        numeric_string = re.sub(r'[^\d]', '', price_str)
        try:
            price = int(numeric_string)
        except:
            price = -1

        extracted_item_list[i] = [city, street_name, street_num, property_type, area, room_num, floor, size, price]
        i += 1

    return extracted_item_list
