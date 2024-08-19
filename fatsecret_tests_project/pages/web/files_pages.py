import csv
import os

import allure
import requests
from pypdf import PdfReader
from selene import be, query
from selene.support.shared import browser

from fatsecret_tests_project.data.products import product_1, product_2



def create_content_folder():
    os.makedirs("content_folder", exist_ok=True)

CONTENT_DIR = os.path.abspath("content_folder")


class ExportFile:
    @allure.step("Click Print")
    def click_print(self):
        browser.element('[title="Print"]').should(be.clickable).click()

    @allure.step("Check Export PDF")
    def check_export_pdf_button(self):
        browser.element(".rec").should(be.present).element("../..").element(
            '[href*="foods.pdf"]'
        ).should(be.clickable)

    @allure.step("Check Export CSV button")
    def check_export_csv_button(self):
        browser.element(".rec").should(be.present).element("../..").element(
            '[href*="foods.csv"]'
        ).should(be.clickable)

    def download_pdf(self):
        create_content_folder()
        download_url = (
            browser.element(".rec")
            .should(be.present)
            .element("../..")
            .element('[href*="foods.pdf"]')
            .get(query.attribute("href"))
        )

        content = requests.get(url=download_url).content
        file_path = os.path.join(CONTENT_DIR, "pdf")
        with open(file_path, "wb") as file:
            file.write(content)

    def download_csv(self):
        create_content_folder()
        download_url = (
            browser.element(".rec")
            .should(be.present)
            .element("../..")
            .element('[href*="foods.csv"]')
            .get(query.attribute("href"))
        )

        content = requests.get(url=download_url).content
        file_path = os.path.join(CONTENT_DIR, "csv")
        with open(file_path, "wb") as file:
            file.write(content)

    @allure.step("Check PDF file has products info")
    def check_pdf_file_has_products_info(self, *products):
        for product in products:
            with open(os.path.join(CONTENT_DIR, "pdf"), "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                text = reader.pages[0].extract_text()
                assert "Food Diary Report" in text
                assert product.name in text
                assert product.calories_quantity in text

    @allure.step("Check CSV file has products info")
    def check_csv_file_has_product_info(self):

        with open(os.path.join(CONTENT_DIR, "csv")) as csv_file:
            content = csv_file.read()
            csvreader = list(csv.reader(content.splitlines()))
            header_row = csvreader[1]
            last_added_row = csvreader[11]
            first_added_row = csvreader[13]

            assert "Food Diary Report" in header_row[0]
            assert product_2.name in last_added_row[0]
            assert product_1.name in first_added_row[0]

            for row in csvreader:
                if any(product_2.name in cell for cell in row):
                    assert any(product_2.calories_quantity in cell for cell in row)

            for row in csvreader:
                if any(product_1.name in cell for cell in row):
                    assert any(product_1.calories_quantity in cell for cell in row)


export_file = ExportFile()
