
import FileManager
from Models import RentalProperty
from PropertyFactory import ForSalePropertyFactory, RentalPropertyFactory
from Tool import Tool

t = Tool('sqlite:///db.db')

# # t.scrape_data('https://www.yad2.co.il/realestate/forsale?price=300000-1100000', 2)
# t.scraped_data = {0: FileManager.load_html_from_file("page_0.html")}
#
t.scrape_data('https://www.yad2.co.il/realestate/rent?priceOnly=1&imgOnly=1', 2)
t.parse_data()
# t.view_data()
t.commit_data(RentalPropertyFactory())


# p = RentalProperty(0, "c", "s", 12, "t", "b", 3, 2, 64, 1000000)