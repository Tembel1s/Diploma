import csv
from selene import be
from selene.support.shared import browser
from pypdf import PdfReader
import allure

from Data.products import product_1, product_2


class ExportFile:
    @allure.step('Click Print')
    def click_print(self):
        browser.element('[title="Print"]').should(be.clickable).click()

    @allure.step('Click Export PDF')
    def click_export_pdf(self):
        browser.element('.rec').should(be.present).element('../..').element('[href*="foods.pdf"]').should(
            be.clickable).click()

    @allure.step('Click Export CSV')
    def click_export_csv(self):
        browser.element('.rec').should(be.present).element('../..').element('[href*="foods.csv"]').should(
            be.clickable).click()

    @allure.step('Check PDF file has products info')
    def check_pdf_file_has_products_info(self, *products):
        import os
        import glob

        current_file_dir = os.path.dirname(__file__)
        relative_path = os.path.join('../../..', 'tests', 'web', 'content_folder')
        folder_path = os.path.abspath(os.path.join(current_file_dir, relative_path))
        pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
        file_path = pdf_files[0]

        for product in products:
            with open(file_path, "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                text = reader.pages[0].extract_text()
                assert "Food Diary Report" in text
                assert product.name in text
                assert product.calories_quantity in text

    @allure.step('Check CSV file has products info')
    def check_csv_file_has_product_info(self):
        import os
        import glob

        current_file_dir = os.path.dirname(__file__)
        relative_path = os.path.join('../../..', 'tests', 'web', 'content_folder')
        folder_path = os.path.abspath(os.path.join(current_file_dir, relative_path))
        csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
        file_path = csv_files[0]

        #
        with open(file_path) as csv_file:
            content = csv_file.read()
            csvreader = list(csv.reader(content.splitlines()))
            header_row = csvreader[1]
            last_added_row = csvreader[11]
            first_added_row = csvreader[13]

            assert 'Food Diary Report' in header_row[0]
            assert product_2.name in last_added_row[0]
            assert product_1.name in first_added_row[0]

            for row in csvreader:
                if any(product_2.name in cell for cell in row):
                    assert any(product_2.calories_quantity in cell for cell in row)

            for row in csvreader:
                if any(product_1.name in cell for cell in row):
                    assert any(product_1.calories_quantity in cell for cell in row)
