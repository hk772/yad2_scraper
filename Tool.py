from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import Parser
from FileManager import FileManager
from Models import Base
from Scraper import Scraper


class Tool:
    def __init__(self, db_location):
        self.scraped_data = {}
        self.parsed_data = {}
        self.scraper = Scraper()
        self.engine = create_engine(db_location, echo=True)
        Base.metadata.create_all(self.engine)

    def scrape_data(self, url, num_of_pages):
        self.scraper.start()
        self.scraped_data = self.scraper.get_htmls_for_pages(url, num_of_pages)

    def parse_data(self):
        for key in self.scraped_data:
            self.parsed_data[key] = Parser.parse_items_from_page(BeautifulSoup(self.scraped_data[key], 'html.parser'))

    def view_data(self):
        print(self.parsed_data)

    def commit_data(self, property_factory):
        property_list = []
        i = 0
        for page in self.parsed_data.keys():
            for index in self.parsed_data[page]:
                new_property = property_factory.create_property(i, *self.parsed_data[page][index])
                property_list.append(new_property)
                i += 1

        self.persist(property_list)

    def persist(self, property_list):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Add the instance to the session
        for p in property_list:
            session.add(p)

        # Commit the changes to the database
        session.commit()
        session.close()

        # Create a session
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Add the instance to the session
        for p in property_list:
            session.add(p)

        # Commit the changes to the database
        session.commit()
        session.close()
