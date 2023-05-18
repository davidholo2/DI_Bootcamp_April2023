import requests
import time


def measure_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    load_time = end_time - start_time
    return load_time


websites = ["https://en.wikipedia.org/wiki/Capybara",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.instagram.com/elonmusk.ab/?hl=en"
            ]

for website in websites:
    load_time = measure_page_load_time(website)
    print(f"Page load time for {website}: {load_time} seconds")
