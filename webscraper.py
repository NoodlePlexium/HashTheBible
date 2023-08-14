import requests
from bs4 import BeautifulSoup


class SermonCentralScraper:

    def getText(self, book, chapter):

        # GET HTML CONTENT
        url = "https://www.sermoncentral.com/bible/new-international-version-niv/" + book.lower() + "-"+str(chapter)+"?passage="+ book + "+"+str(chapter)
        response = requests.get(url)
        
        if response.status_code == 200:

            # GET HTML
            soup = BeautifulSoup(response.content, "html.parser")
            bible_content = soup.find("div", class_="bible-content")
            span_elements = []

            for element in bible_content.find_all(recursive=False):
                for child in element.find_all(recursive=False):
                    if child.name == "span": 
                        span_elements.append(child)       

            # search through span element children
            childrenToExtract = []
            for spanElement in span_elements:
                children = spanElement.find_all(recursive=False)
                for child in children:
                    if child.name != "a" and child.name != "small":
                        childrenToExtract.append(child)

            # remove children that are not <a> tags
            for child in childrenToExtract: child.extract()  
            
            # APPEND HTML TEXT
            text = ""
            for element in span_elements:
                text += element.get_text() + "\n"
            
            return text
        else:
            print("Failed to retrieve the webpage")
            return None


class YouVersionScraper:

    def __init__(self):
        self.bookAbreviation = {
            "Genesis" : "GEN",
            "Exodus" : "EXO",
            "Leviticus" : "LEV",
            "Numbers" : "NUM",
            "Deuteronomy" : "DEU",
            "Joshua" : "JOS",
            "Judges" : "JDG",
            "Ruth" : "RUT"
        }


    def getText(self, book, chapter):

        # GET HTML CONTENT
        url = "https://www.bible.com/bible/111/"+ self.bookAbreviation[book] +"." + str(chapter) + ".NIV"
        response = requests.get(url)

        if response.status_code == 200:

            # GET HTML
            soup = BeautifulSoup(response.content, "html.parser")
            bible_content = soup.find("div", class_="ChapterContent_chapter__uvbXo")
            span_elements = bible_content.find_all("span")

            # KEEP CERTAIN ELEMENTS
            keep_elements = []
            for element in span_elements:
                eClass = element.get("class")[0]
                
                if eClass == "ChapterContent_content__RrUqA" or eClass == "ChapterContent_label__R2PLt" or eClass == "ChapterContent_heading__xBDcs":
                    keep_elements.append(element)

            # GENERATE TEXT STRING
            text = ""
            for element in keep_elements:
                text += element.get_text() + "\n"

            return text

        else:
            print("Failed to retrieve the webpage")
            return None


        

