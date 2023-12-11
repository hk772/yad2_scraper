from bs4 import BeautifulSoup


def load_html_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    # _soup = BeautifulSoup(html_content, 'html.parser')
    # return _soup


class FileManager:
    def save_html_to_file(self, html_content, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
