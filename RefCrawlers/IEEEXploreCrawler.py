import urllib

class IEEEXploreCrawler:
    _detailedPageUrl = "http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber={%ARTICLE_ID%}"
    def __init__(self, start_id, end_id):
        for article_id in range(start_id, end_id):
            url_str = str.replace("{%ARTICLE_ID%}", article_id)
            fp = urllib.urlopen(url)
            try:
                data = fp.read()
            finally:
                fp.close()

    def references_to_triplets(self):
        
            
