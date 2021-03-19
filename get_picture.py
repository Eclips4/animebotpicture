import random
import requests
from bs4 import BeautifulSoup as bs


class Picture:
    def __init__(self, link):
        self.link = link
        self.links = []
        self.images = []

    def get_count_pages(self):
        mainpage = requests.get(self.link)
        parse_mainpage = bs(mainpage.text, 'html.parser')
        pages = parse_mainpage.find(class_='next')['href']
        pages_count = pages[pages.rfind('/') + 1:]
        get_art_page = requests.get(f'{self.link}/{random.randint(1, int(pages_count))}')
        return get_art_page

    def get_links(self):
        parse_page = self.get_count_pages()
        parse_art_page = bs(parse_page.text, 'html.parser')
        links_page = parse_art_page.findAll(class_='link')
        links = random.choice([tag['href'] for tag in links_page])
        link = random.choice(links)
        return link

    def get_pictures(self):
        img_post_link = requests.get(f'http://anime.reactor.cc{self.get_links()}')
        images = bs(img_post_link.text, 'html.parser')
        class_image = images.findAll(class_='image')
        images_links = [i.__str__()[i.__str__().find('src="') + 5:i.__str__().find(' ', i.__str__().find('src="')) - 1]
                        for i in class_image]
        links_correct_images = list(filter(lambda x: "comment" not in x and "class" not in x, images_links))
        return links_correct_images
