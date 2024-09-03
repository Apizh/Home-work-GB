import time
import requests
import argparse
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count


# Функция для сохранения изображения на диск
def save_image(image_content, filename):
    with open(filename, 'wb') as f:
        f.write(image_content)


# Синхронная функция загрузки изображения
def download_image(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        filename = url.split("/")[-1]
        save_image(response.content, filename)
        print(f"Downloaded {filename} in {time.time() - start_time:.2f} seconds.")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")


# Асинхронная функция загрузки изображения
async def download_image_async(url, session):
    start_time = time.time()
    print(url)
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            image_content = await response.read()
            filename = url.split("/")[-1]
            save_image(image_content, filename)
            print(f"Downloaded {filename} in {time.time() - start_time:.2f} seconds.")
    except aiohttp.ClientError as e:
        print(f"Error downloading {url}: {e}")


# Асинхронный запуск загрузок
async def async_main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(url, session) for url in urls]
        await asyncio.gather(*tasks)


# Запуск многопоточного скачивания
def threaded_download(urls):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_image, urls)
    print(f"Threaded download completed in {time.time() - start_time:.2f} seconds.")


# Запуск многопроцессорного скачивания
def multiprocessing_download(urls):
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        executor.map(download_image, urls)
    print(f"Multiprocessing download completed in {time.time() - start_time:.2f} seconds.")


# Основная функция
def main(urls, mode):
    start_time = time.time()

    if mode == 'threading':
        threaded_download(urls)
    elif mode == 'multiprocessing':
        multiprocessing_download(urls)
    elif mode == 'asyncio':
        asyncio.run(async_main(urls))
    else:
        print("Invalid mode. Choose from 'threading', 'multiprocessing', 'asyncio'.")

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from URLs using different methods.")
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='List of URLs to download images from.')
    parser.add_argument('--mode', choices=['threading', 'multiprocessing', 'asyncio'], required=True,
                        help='Download mode: threading, multiprocessing, or asyncio.')

    args = parser.parse_args()
    main(args.urls, args.mode)
