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

                html_stack.append("")
            else:
                tag, position = parse_tag(html_str, position + 2)

                current_data = html_stack.pop()
                data_callback(current_data)

                close_tag_callback(tag)
        else:
            message, position = parse_message(html_str, position)
            html_stack[-1] += message


if __name__ == '__main__':
    html = "<p>text<internal>internal text</internal> text</p>"
    parse_html(html, lambda x: print("Open", x), lambda x: print("Data", x), lambda x: print("Close", x))
