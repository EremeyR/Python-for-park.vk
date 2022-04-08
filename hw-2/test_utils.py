test_buf = ""


counter_value = 0


def counter(sth):
    global counter_value
    counter_value += 1


def add_to_buf(value):
    global test_buf
    test_buf += value


def clear_buf():
    global test_buf
    test_buf = ""


def clear_counter_value():
    global counter_value
    counter_value = 0


def test_open_tag_callback(open_tag):
    add_to_buf('[' + open_tag + '|')


def test_close_tag_callback(close_tag):
    add_to_buf('|' + close_tag + ']')


def test_data_callback(data):
    add_to_buf(data)
