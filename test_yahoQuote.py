import unittest
import requests

from yahooQuote import*

class test_yahooQuote(unittest.TestCase):
    def setUp(self):
        pass

    def test_send_request(self):
        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + "FB" + "&f=sl1d1t1c1ohgv&e‌​=.csv"
        self.assertEqual(send_request(url).status_code, 200)

        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + "IBM" + "&f=sl1d1t1c1ohgv&e‌​=.csv"
        self.assertEqual(send_request(url).status_code, 200)

        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + "Twitter" + "&f=sl1d1t1c1ohgv&e‌​=.csv"
        self.assertFalse(send_request(url).status_code == 300)

    def test_assembl_url(self):
        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + "FB" + "&f=sl1d1t1c1ohgv&e‌​=.csv"
        self.assertEqual(assembl_url("FB"), url)
        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + "" + "&f=sl1d1t1c1ohgv&e‌​=.csv"
        self.assertEqual(assembl_url(""), url)

    def test_get_stock_symbol(self):
        self.assertEqual(get_stock(""), "")
        self.assertEqual(get_stock("FB"), "FB")
        self.assertEqual(get_stock("GOOG"), "GOOG")

    
if __name__ == '__main__':
    unittest.main()
