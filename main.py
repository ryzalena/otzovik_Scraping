import requests
from bs4 import BeautifulSoup
import os


def main():
    user_agent = 'Mozilla/5.0 '
    url = 'https://otzovik.com/reviews/online_fashion_shop_wildberries_ru/'
    for i in range (1, 6): #для каждой звезды
        max_pages = 9999
        for p in range(max_pages): #максимальная страница

            cur_url = url + str(p + 1)
            print("Скрапинг страницы №: %d" % (p + 1))
            html_text = requests.get(cur_url , headers={"User-Agent": user_agent}).text
            soup = BeautifulSoup(html_text, 'lxml')
            info_max_page = soup.find('a', class_='pager-item last tooltip-top', href=True)
            print(soup)
            print('*******')
            ad = soup.find_all(class_='review-teaser').text
            print (ad)
            if not os.path.isdir("dataset"):  # создаем папку, если ее еще нет
                os.mkdir("dataset")
            for i in range(1, 6):  # создаем подпапки для каждой звезды
                if not os.path.isdir("dataset/" + str(i)):
                    os.makedirs("dataset/" + str(i))
            for i in range(1, 6):  # заполняем отзывами
                number_opinion = 1
                namefile = str(number_opinion).zfill(4)
                number_opinion += 1
                text = 'Отзыв:\n' + ad
                with open('dataset/' + str(i) + '/' + namefile + '.txt', 'w+') as file:
                    file.write(text)

            page_nav = soup.find_all('a', class_='pager-item last tooltip-top')
            if (len(page_nav) == 0):
                print("Максимальный номер страницы: %d" % (p))
                break


if __name__ == '__main__':
    main()
