"""
Merchandising API functional tests

Prerequisites:
 - python-nose (unit test discovery and execution without too much magic)
 - python-httplib2 (a comprehensive HTTP client library)
 - python-lxml (feature-rich, easy to use library for XML and HTML processing)
 - TBD python-sqlalchemy (Python SQL Toolkit and ORM)
Install using "yum install" (RHEL/CentOS/Fedora) or "apt-get install" (Ubuntu).
 
Usage:
  nosetests [--where=.] [--tests=test_merch_api] [--nologcapture] -d -v
            [--with-xunit] [--xunit-file=<path to XUnit XML file>]
  Runs all tests in current directory (or specific tests in specific directory).
  Show detailed errors and verbose output.
  Logs capture can be disabled. Standard XUnit XML report file support.
  
  nosetests -d -v test_merch_api.py:test_login_success
                  test_merch_api.py:TestAPI.test_products_by_device
  Runs only specific tests.
  
Authors: 
Initial framework by Miroslav Madecki (miroslav.madecki@nokia.com)
Expanded by Qian Ouyang (qian.1.ouyan@nokia.com) 

Status:	Prototype
Since:	Phase 1, 05/19/2011
"""

import logging
import httplib2
from lxml import etree

#=======================================================================
# Setup & Utilities
#=======================================================================

log = logging.getLogger("merch-api")
logging.basicConfig()
log.setLevel(logging.INFO)

# apiUrl="http://172.19.188.14/merch-api-p1/merch-api/"

# apiUrl="http://merchapi.nokia.com/merch-api-test/merch-api/"

# apiUrl="https://mapi.store.nokia.com/merch-api/"

apiUrl="http://merchapi.nokia.com/devint1/merch-api/"
http = httplib2.Http()
sessionToken = None

def get(urlpath):
    """For a given full or partial url path (adds service endpoint or
       session_token if missing) make HTTP request and return
       HTTP status, object (parsed XML or JSON).
       Values if 0, None respectively, indicate failure.
    """
    if urlpath.find("http") != 0: # if supplied url doesn't start with http
        urlpath = apiUrl + urlpath

    if urlpath.find("session_token") < 0 and sessionToken != None: # if no session_token in the urlpath and sessionToken exists
        if urlpath.find("?") > 0: # if ? is after the first letter/not the first letter in urlpath
           urlpath += "&session_token=%s" % sessionToken # append &session_token and its value at the end of urlpath, meaning to supply ssession token
        else: # if ? is the first letter or ? doesn't exist in urlpath
           urlpath += "?session_token=%s" % sessionToken # append ?session_token and its value at the end of urlpath, meaning to get session_token

    log.info("get urlpath=%s" % urlpath)
    status = 0
    obj = None
    try:
        rsp, cont = http.request(urlpath) # Execute HTTP request
        log.debug("get response=%s\ncontent=%s" % (rsp, cont))
        status = int(rsp['status'])  # Extract HTTP status code from response
        obj = etree.fromstring(cont) # Parse XML response (element tree)
    except Exception, e:
        log.exception(e)
    return status, obj # this function returns http response status and response content formated as XML tree

#=======================================================================
# TESTS
#=======================================================================

def test_login_success():
    s, r = get("session_token/user/API/password/api")
    assert s == 200 and r != None and r.tag == 'session_token' and r.text != ''

def test_login_failure():
    s, r = get("session_token/user/API/password/api1")
    assert s == 401 and r != None and r.tag == 'error' and r.text != '' 

def test_valid_login_invalid_session_token():
    s, r = get("session_token/user/DDR/password/ddr")
    assert s == 200 and r != None and r.tag == 'session_token' and r.text != ''
    sessionToken = r.text
    s, r = get("products")
    assert s == 401 and r != None and r.tag == 'error' and r.text != ''     	
    
class TestAPI:

    def setUp(self):
        "Login and set session_token for all follow on requests"
        global sessionToken
        s, r = get("session_token/user/API/password/api")
        sessionToken = r.text
        self.devices = ['5800', '6210', 'E72', 'N76', 'N97', 'N8-00', 'C6-00']
	self.devices_negative = ['Focus', 'Boston', '10000']
	self.countries = ['US', 'CN', 'CA', 'IT', 'HK', 'FR', 'RU', 'BR', 'EG', 'TW', 'GB', 'CC'] # currently, country can = to anything and will return products, 10 items/page
	self.countries_negative = ['AB', 'XY', 'US'] # This test case will always fail now, see above
	#country = AB is a true supported country, Abkhazia, so need to change to another value
	self.languages = ['en', 'fr', 'ch','aa','vi'] # currently, language can = to anything and will return products, 10 items/page
	self.languages_negative = ['xx', 'oo','ab'] # This test case will always fail now, see above
	self.categories = ['applications', 'application', 'games', 'Audio & Video','Sports','action', 'Audio', 'Wallpapers']
	self.categories_negative = ['apps', 'agame','&'] # "&" behaves differently, it will returned 10 items/page, causing the test to fail
	   
    def tearDown(self):
        "Reset session token to make sure other tests don't re-use it"
        global sessionToken
        sessionToken = None
    ###########################################################################################################


    def test_products(self):
        s, r = get("products")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10
	num = len(variants)
	print num	

    def test_countries(self):
        s, r = get("countries")
        countries = r.findall("country")
        assert s == 200 and len(countries) == 230

    def test_devices(self):
        s, r = get("devices")
        devices = r.findall("deviceType")
        assert s == 200 and len(devices) == 308
#was 269, 280

    def test_languages(self):
        s, r = get("languages")
        languages = r.findall("language")
        assert s == 200 and len(languages) == 55
#was 56
                       
    def test_categories(self):
        s, r = get("categories")
        categories = r.findall("category")
        assert s == 200 and len(categories) == 67
    ###########################################################################################################

    
    def test_products_US_N97_en_count(self):
        s, r = get("products?country=US&device=N97&language=en")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_US_N97_en_product_order(self):
        s, r = get("products?country=US&device=N97&language=en")
#        pids = [p.text.split("/")[-1] for p in r.findall("productVariant/product/uri")]
        pids = [p.text for p in r.findall("productVariant/product/id")]
        pvids = [p.text.split("/")[-1] for p in r.findall("productVariant/uri")]
        ppv = zip(pids, pvids)
        log.info("pid,pvid list %r" % ppv)
        assert s == 200 and \
               ppv ==  [('1391', '21516'), ('1395', '60311'), ('1618', '13357'), ('1623', '3002'), ('1800', '3111'), ('1825', '4676'), ('1838', '3077'), ('1845', '3083'), ('1877', '21596'), ('1883', '457450')]
#               ppv == [('1853', '8722'), ('2014', '427212'), ('2178', '7983'), ('2333', '4520'), ('2349', '3455'), ('2364', '3475'), ('2365', '3476'), ('2373', '3481'), ('2392', '3495'), ('2398', '3504')]		

    def test_products_US_N97_en_page(self):
        s, r = get("products?country=US&device=N97&language=en&page=10")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_US_N97_en_page_size(self):
        s, r = get("products?country=US&device=N97&language=en&page_size=80")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 80

    def test_products_US_N97_en_page_page_size(self):
        s, r = get("products?country=US&device=N97&language=en&page=5&page_size=8")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 8
    #############################################################################################################

    
    def test_products_FR_7230_fr_count(self):
        s, r = get("products?country=FR&device=7230&language=fr")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_FR_7230_fr_product_order(self):
        s, r = get("products?country=FR&device=7230&language=fr")
        pids = [p.text for p in r.findall("productVariant/product/id")]
        pvids = [p.text.split("/")[-1] for p in r.findall("productVariant/uri")]
        ppv = zip(pids, pvids)
        log.info("pid,pvid list %r" % ppv)
        assert s == 200 and \
               ppv ==  [('3455', '8274'), ('3464', '20937'), ('28776', '354495'), ('29778', '431280'), ('33883', '428700'), ('36243', '431024'), ('36711', '441047'), ('37364', '431786'), ('42334', '437138'), ('50774', '451112')]

    def test_products_FR_7230_fr_page(self):
        s, r = get("products?country=FR&device=7230&language=fr&page=2")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_FR_7230_fr_page_size(self):
        s, r = get("products?country=FR&device=7230&language=fr&page_size=12")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 12

    def test_products_FR_7230_fr_page_page_size(self):
        s, r = get("products?country=FR&device=7230&language=fr&page=3&page_size=5")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 5
    #############################################################################################################

    
    def test_products_CN_N800_zh_cn_count(self):
        s, r = get("products?country=CN&device=N8-00&language=zh_cn")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_CN_N800_zh_cn_product_order(self):
        s, r = get("products?country=CN&device=N8-00&language=zh_cn")
        pids = [p.text for p in r.findall("productVariant/product/id")]
        pvids = [p.text.split("/")[-1] for p in r.findall("productVariant/uri")]
        ppv = zip(pids, pvids)
        log.info("pid,pvid list %r" % ppv)
        assert s == 200 and \
               ppv ==  [('2579', '31482'), ('3677', '21902'), ('3683', '22284'), ('9712', '19539'), ('12205', '21464'), ('12206', '19059'), ('12824', '19658'), ('12825', '21237'), ('12830', '19654'), ('12840', '19173')]

    def test_products_CN_N800_zh_cn_page(self):
        s, r = get("products?country=CN&device=N8-00&language=zh_cn&page=13")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_CN_N800_zh_cn_page_size(self):
        s, r = get("products?country=CN&device=N8-00&language=zh_cn&page_size=25")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 25

    def test_products_CN_N800_zh_cn_page_page_size(self):
        s, r = get("products?country=CN&device=N8-00&language=zh_cn&page=9&page_size=18")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 18
    #############################################################################################################

    
    def test_products_BR_N900_pt_br_count(self):
        s, r = get("products?country=BR&device=N900&language=pt_br")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_BR_N900_pt_br_product_order(self):
        s, r = get("products?country=BR&device=N900&language=pt_br")
        pids = [p.text for p in r.findall("productVariant/product/id")]
        pvids = [p.text.split("/")[-1] for p in r.findall("productVariant/uri")]
        ppv = zip(pids, pvids)
        log.info("pid,pvid list %r" % ppv)
        assert s == 200 and \
               ppv ==  [('3455', '6944'), ('3464', '13655'), ('21546', '29406'), ('21547', '29407'), ('21548', '30194'), ('21549', '48920'), ('21550', '29409'), ('21552', '29412'), ('21553', '29413'), ('21554', '29414')]

    def test_products_BR_N900_pt_br_page(self):
        s, r = get("products?country=BR&device=N900&language=pt_br&page=6")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 10

    def test_products_BR_N900_pt_br_page_size(self):
        s, r = get("products?country=BR&device=N900&language=pt_br&page_size=50")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 50

    def test_products_BR_N900_pt_br_page_page_size(self):
        s, r = get("products?country=BR&device=N900&language=pt_br&page=11&page_size=12")
        variants = r.findall("productVariant")
        assert s == 200 and len(variants) == 12
    #############################################################################################################

               
    def test_products_by_device(self):
        for d in self.devices:
            s, r = get("products?device=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for device %s" % (len(pv), d))
            assert s == 200 and len(pv) > 0

    def test_products_by_device_negative(self):
        for d in self.devices_negative:
            s, r = get("products?device=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for device %s" % (len(pv), d))
            assert s == 200 and len(pv) == 0

    def test_products_by_country(self):
        for d in self.countries:
            s, r = get("products?country=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for country %s" % (len(pv), d))
            assert s == 200 and len(pv) > 0

    def test_products_by_country_negative(self):
        for d in self.countries_negative:
            s, r = get("products?country=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for country %s" % (len(pv), d))
            assert s == 200 and len(pv) == 0

    def test_products_by_language(self):
        for d in self.languages:
            s, r = get("products?language=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for language %s" % (len(pv), d))
            assert s == 200 and len(pv) > 0

    def test_products_by_language_negative(self):
        for d in self.languages_negative:
            s, r = get("products?language=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for language %s" % (len(pv), d))
            assert s == 200 and len(pv) == 0

    def test_products_by_category(self):
        for d in self.categories:
            s, r = get("products?category=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for category %s" % (len(pv), d))
            assert s == 200 and len(pv) > 0

    def test_products_by_category_negative(self):
        for d in self.categories_negative:
            s, r = get("products?category=%s" % d)
            pv = r.findall("productVariant")
            log.info("Found %d variants for category %s" % (len(pv), d))
            assert s == 200 and len(pv) == 0

