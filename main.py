# from bs4 import BeautifulSoup
# from requests import get, exceptions
#
#
# def count_tags():
#     number_of_tags = 0
#     tags_with_attrs = 0
#
#     url = 'https://jetlend.ru/'
#     try:
#         response = get(url)
#     except exceptions.ConnectionError:
#         print(f'Service - {url} is not available')
#         return
#     content = response.text
#     soup = BeautifulSoup(content, "html.parser")
#     for child in soup.recursiveChildGenerator():
#         if child.name:
#             number_of_tags += 1
#             if child.attrs:
#                 tags_with_attrs += 1
#     print(f'Tags on the page - {number_of_tags}')
#     print(f'Tags with attributes on the page - {tags_with_attrs}')
#
#
# if __name__ == '__main__':
#     count_tags()


def get_ip() -> str:
    from requests import get, exceptions
    url = 'https://ifconfig.me/ip'
    try:
        response = get(url)
    except exceptions.ConnectionError:
        return f'Service - {url} is not available'
    return response.content.decode()


print(get_ip())
