import unittest

import test_utils
import ParserHTML

from faker import Faker
from unittest.mock import patch
Faker.seed(42)


def generate_fake_html(numb_of_blocs):
    fake = Faker()
    tag_stack = []
    html = ""
    for i in range(numb_of_blocs):
        current_tag = fake.color_name()
        tag_stack.append(current_tag)

        html += '<' + current_tag + '>'
        html += fake.currency_name()

    for i in range(numb_of_blocs):
        current_tag = tag_stack.pop()

        html += str(fake.pyfloat())
        html += '</' + current_tag + '>'

    return html


class TestStringMethods(unittest.TestCase):

    html_100 = generate_fake_html(100)

    def test_empty_body(self):
        html = "<body></body>"
        ParserHTML.parse_html(html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        right_return = "[body||body]"
        self.assertEqual(test_utils.test_buf, right_return)

        test_utils.clear_buf()

    def test_one_comment(self):
        html = "<body>comment</body>"
        ParserHTML.parse_html(html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        right_return = "[body|comment|body]"
        self.assertEqual(test_utils.test_buf, right_return)

        test_utils.clear_buf()

    def test_one_comment_one_empty_header(self):
        html = "<body>comment<h></h></body>"
        ParserHTML.parse_html(html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        right_return = "[body|[h||h]comment|body]"
        self.assertEqual(test_utils.test_buf, right_return)

        test_utils.clear_buf()

    def test_one_comment_one_header(self):
        html = "<body>comment<h>header</h></body>"
        ParserHTML.parse_html(html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        right_return = "[body|[h|header|h]comment|body]"
        self.assertEqual(test_utils.test_buf, right_return)

        test_utils.clear_buf()

    def test_two_comments_one_header(self):
        html = "<body>comment1<h>header</h>+comment2</body>"
        ParserHTML.parse_html(html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        right_return = "[body|[h|header|h]comment1+comment2|body]"
        self.assertEqual(test_utils.test_buf, right_return)

        test_utils.clear_buf()

    def test_100_open_tags_counter(self):

        with patch('test_utils.test_open_tag_callback') as open_tag_mock:
            open_tag_mock.side_effect = test_utils.counter
            ParserHTML.parse_html(self.html_100, test_utils.test_open_tag_callback,
                                  test_utils.test_data_callback, test_utils.test_close_tag_callback)

        self.assertEqual(test_utils.counter_value, 100)

        test_utils.clear_buf()
        test_utils.clear_counter_value()

    def test_100_close_tags_counter(self):
        with patch('test_utils.test_close_tag_callback') as open_tag_mock:
            open_tag_mock.side_effect = test_utils.counter
            ParserHTML.parse_html(self.html_100, test_utils.test_open_tag_callback,
                                  test_utils.test_data_callback, test_utils.test_close_tag_callback)

        self.assertEqual(test_utils.counter_value, 100)

        test_utils.clear_buf()
        test_utils.clear_counter_value()

    def test_100_data_callbacks_counter(self):
        with patch('test_utils.test_close_tag_callback') as open_tag_mock:
            open_tag_mock.side_effect = test_utils.counter
            ParserHTML.parse_html(self.html_100, test_utils.test_open_tag_callback,
                                  test_utils.test_data_callback, test_utils.test_close_tag_callback)

        self.assertEqual(test_utils.counter_value, 100)

        test_utils.clear_buf()
        test_utils.clear_counter_value()

    def test_long_html(self):
        long_html = generate_fake_html(10000)

        ParserHTML.parse_html(long_html, test_utils.test_open_tag_callback,
                              test_utils.test_data_callback, test_utils.test_close_tag_callback)

        test_utils.clear_buf()


if __name__ == '__main__':
    unittest.main()
