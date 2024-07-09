import logging

from celery import shared_task
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from only_fans_stat.models import Links, AccountDetail

logger = logging.getLogger(__name__)
driver = webdriver.WebDriver()


def parse_data_from_link(account_link):
    driver.get(account_link)

    try:
        post_count = driver.find_element(
            By.XPATH, '//*[@id="profilePostTab"]/a/span').text
        media_count = driver.find_element(
            By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div[2]/div/div[4]/ul/li[2]/a/span').text
        likes_count = driver.find_element(
            By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/div[3]/span/span').text

        AccountDetail.objects.get_or_create().update(
            post_count=post_count, media_count=media_count,
            likes_count=likes_count
        )

    except Exception as e:
        logger.info(f"An error occurred: {e}")

    # Close the driver
    driver.quit()


@shared_task(name='parse_data_from_accounts', bind=True)
def parse_data_from_accounts(self):
    """Parse data from all accounts in Links table"""
    account_links = Links.objects.all()

    for account_link in account_links:
        parse_data_from_link(account_link)

    logger.info("Finished")
