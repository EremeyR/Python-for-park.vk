def simple_open_tag_callback(open_tag):
    print("Open", open_tag)


def simple_close_tag_callback(close_tag):
    print("Close", close_tag)


def simple_data_callback(tag, data):
    print(data, "| from", tag)


def parse_tag(html_str: str, position):
    tag_list = []

    while html_str[position] != '>':
        tag_list.append(html_str[position])
        position += 1

    return ''.join(tag_list), position + 1


def parse_message(html_str: str, position):
    message_list = []

    while html_str[position] != '<':
        message_list.append(html_str[position])
        position += 1

    return ''.join(message_list), position


def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback):
    html_stack = []

    position = 0
    html_len = len(html_str)
    while position < html_len:
        if html_str[position] == '<':
            if html_str[position + 1] != '/':
                tag, position = parse_tag(html_str, position + 1)
                open_tag_callback(tag)

                html_stack.append([tag, ""])
            else:
                tag, position = parse_tag(html_str, position + 2)

                closing_tag, closing_data = html_stack.pop()
                data_callback(closing_tag, closing_data)

                close_tag_callback(tag)
        else:
            message, position = parse_message(html_str, position)
            html_stack[-1][1] += message


if __name__ == '__main__':
    html = "<p>text<internal>internal text</internal> txet</p>"
    parse_html(html, simple_open_tag_callback, simple_data_callback, simple_close_tag_callback)
