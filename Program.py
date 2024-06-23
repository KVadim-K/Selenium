from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Функция для получения параграфов статьи
def get_article_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"Paragraph {i + 1}: {paragraph.text[:100]}...")  # Печатаем первые 100 символов параграфа
        if (i + 1) % 5 == 0:
            cont = input("Продолжить листать? (да/нет): ")
            if cont.lower() != 'да':
                break

# Функция для получения внутренних ссылок
def get_internal_links(browser):
    # Поиска всех элементов <a> внутри основного контента страницы
    links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(@class)]")
    # функция находит все ссылки на текущей странице, которые начинаются с "https://ru.wikipedia.org/wiki/"
    internal_links = [link for link in links if link.get_attribute('href').startswith('https://ru.wikipedia.org/wiki/')]
    print(f"Всего связанных страниц: {len(internal_links)}")
    return internal_links

# Основная функция для поиска на Википедии
def search_wikipedia(query):
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org")

    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # Ждём загрузки страницы

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия (1, 2, 3): ")

        if choice == '1':
            get_article_paragraphs(browser)
        elif choice == '2':
            internal_links = get_internal_links(browser)
            print("\nСписок доступных связанных страниц:")
            for i, link in enumerate(internal_links[:10]):  # Ограничим до 10 ссылок для удобства
                print(f"{i + 1}. {link.text} - {link.get_attribute('href')}")

            link_choice = int(input("Выберите номер страницы для перехода: ")) - 1
            if 0 <= link_choice < len(internal_links):
                browser.get(internal_links[link_choice].get_attribute('href'))
                time.sleep(2)  # Ждём загрузки страницы
            else:
                print("Некорректный выбор.")
        elif choice == '3':
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(query)