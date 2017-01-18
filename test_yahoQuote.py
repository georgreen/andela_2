import unittest

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
        pass


    def test_get_stock_symbol(self):
        pass

    def test_get_stock_info(self):
        pass



if __name__ == '__main__':
    unittest.main()
