# import logging
#
# from django.core.management import BaseCommand
# from selenium.webdriver.common.by import By
#
# from selenium import webdriver
#
# from only_fans_stat.models import AccountDetail, Links
#
# driver = webdriver.Chrome()
# logger = logging.getLogger(__name__)
#
#
# class Command(BaseCommand):
#     """Command to parse data from only fans web account"""
#
#     @staticmethod
#     def parse_data_from_link(account_link):
#         driver.get(account_link)
#
#         try:
#             post_count = driver.find_element(
#                 By.XPATH, '//*[@id="profilePostTab"]/a/span').text
#             media_count = driver.find_element(
#                 By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div[2]/div/div[4]/ul/li[2]/a/span').text
#             likes_count = driver.find_element(
#                 By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/div[3]/span/span').text
#
#             AccountDetail.objects.get_or_create().update(
#                 post_count=post_count, media_count=media_count,
#                 likes_count=likes_count
#             )
#
#         except Exception as e:
#             logger.info(f"An error occurred: {e}")
#
#         # Close the driver
#         driver.quit()
#
#     def handle(self, *args, **options):
#         account_links = Links.objects.all()
#
#         for account_link in account_links:
#             self.parse_data_from_link(account_link)
#             logger.info("Finished")
#
