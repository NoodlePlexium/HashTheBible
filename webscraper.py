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
        


            for element in bible_content.find_all(recursive=True):
                if element.get("class") is None:
                    continue  # Skip elements with no class
                        
                if element.get("class")[0] == "verse-text":

                    for child in element.find_all(recursive=True):

                        if child.name == "footnote":
                            child.extract()

                        if child.get("class") != None:

                            if child.get("class")[0] == "verse-number":
                                child.extract()   

                if element.get("class")[0] == "verse-title":
                    element.extract()           
              

            # GENERATE TEXT STRING
            text = ""
            for element in bible_content:
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
            "Ruth" : "RUT",
            "1 Samuel" : "1SA",
            "2 Samuel" : "2SA",
            "1 Kings" : "1KI",
            "2 Kings" : "2KI",
            "1 Chronicles" : "1CH",
            "2 Chronicles" : "2CH",
            "Ezra" : "EZR",
            "Nehemiah" : "NEH",
            "Esther" : "EST",
            "Job" : "JOB",
            "Psalms" : "PSA",
            "Proverbs" : "PRO",
            "Ecclesiastes" : "ECC",
            "Song of Songs" : "SNG", 
            "Isaiah" : "ISA",
            "Jeremiah" : "JER",
            "Lamentations" : "LAM",
            "Ezekiel" : "EZK",
            "Daniel" : "DAN",
            "Hosea" : "HOS",
            "Joel" : "JOL",
            "Amos" : "AMO",
            "Obadiah" : "OBA",
            "Jonah" : "JON",
            "Micah" : "MIC",
            "Nahum" : "NAM",
            "Habakkuk" : "HAB",
            "Zephaniah" : "ZEP",
            "Haggai" : "HAG",
            "Zechariah" : "ZEC",
            "Malachi" : "MAL",
            "Matthew" : "MAT",
            "Mark" : "MRK",
            "Luke" : "LUK",
            "John" : "JHN",
            "Acts" : "ACT",
            "Romans" : "ROM",
            "1 Corinthians" : "1CO",
            "2 Corinthians" : "2Co",
            "Galatians" : "GAL",
            "Ephesians" : "EPH",
            "Philippians" : "PHP",
            "Colossians" : "COL",
            "1 Thessalonians" : "1TH",
            "2 Thessalonians" : "2TH",
            "1 Timothy" : "1TI",
            "2 Timothy" : "2TI",
            "Titus" : "TIT",
            "Philemon" : "PHM",
            "Hebrews" : "HEB",
            "James" : "JAS",
            "1 Peter" : "1PE",
            "2 Peter" : "2PE",
            "1 John" : "1JN",
            "2 John" : "2JN",
            "3 John" : "3JN",
            "Jude" : "JUD",
            "Revelation" : "REV"
        }


    def getText(self, book, chapter):

        # GET HTML CONTENT
        url = "https://www.bible.com/bible/111/"+ self.bookAbreviation[book] +"." + str(chapter) + ".NIV"
        response = requests.get(url)

        if response.status_code == 200:

            # GET HTML
            soup = BeautifulSoup(response.content, "html.parser")
            bible_content = soup.find("div", class_="ChapterContent_chapter__uvbXo")

            # REMOVE NOTES
            for element in bible_content.find_all(recursive=True):
                if element.get("class") is not None:
                    
                    if element.get("class")[0] == "ChapterContent_note__YlDW0":
                        element.extract()




            span_elements = bible_content.find_all("span")
            

            # KEEP CERTAIN ELEMENTS
            keep_elements = []
            for element in span_elements:
                eClass = element.get("class")[0]
                
                if eClass == "ChapterContent_content__RrUqA":
                    keep_elements.append(element)

            # GENERATE TEXT STRING
            text = ""
            for element in keep_elements:
                text += element.get_text() + "\n"

            return text

        else:
            print("Failed to retrieve the webpage")
            return None


        
class BibleGatewayScraper:

    def __init__(self):
        self.bookAbreviation = {
            "Genesis" : "Genesis",
            "Exodus" : "Exodus",
            "Leviticus" : "Leviticus",
            "Numbers" : "Numbers",
            "Deuteronomy" : "Deuteronomy",
            "Joshua" : "Joshua",
            "Judges" : "Judges",
            "Ruth" : "Ruth",
            "1 Samuel" : "1-Samuel",
            "2 Samuel" : "2-Samuel",
            "1 Kings" : "1-Kings",
            "2 Kings" : "2-Kings",
            "1 Chronicles" : "1-Chronicles",
            "2 Chronicles" : "2-Chronicles",
            "Ezra" : "Ezra",
            "Nehemiah" : "Nehemiah",
            "Esther" : "Esther",
            "Job" : "Job",
            "Psalms" : "Psalms",
            "Proverbs" : "Proverbs",
            "Ecclesiastes" : "Ecclesiastes",
            "Song of Songs" : "Song-of-Solomon", 
            "Isaiah" : "Isaiah",
            "Jeremiah" : "Jeremiah",
            "Lamentations" : "Lamentations",
            "Ezekiel" : "Ezekiel",
            "Daniel" : "Daniel",
            "Hosea" : "Hosea",
            "Joel" : "Joel",
            "Amos" : "Amos",
            "Obadiah" : "Obadiah",
            "Jonah" : "Jonah",
            "Micah" : "Micah",
            "Nahum" : "Nahum",
            "Habakkuk" : "Habakkuk",
            "Zephaniah" : "Zephaniah",
            "Haggai" : "Haggai",
            "Zechariah" : "Zechariah",
            "Malachi" : "Malachi",
            "Matthew" : "Matthew",
            "Mark" : "Mark",
            "Luke" : "Luke",
            "John" : "John",
            "Acts" : "Acts",
            "Romans" : "Romans",
            "1 Corinthians" : "1-Corinthians",
            "2 Corinthians" : "2-Corinthians",
            "Galatians" : "Galatians",
            "Ephesians" : "Ephesians",
            "Philippians" : "Philippians",
            "Colossians" : "Colossians",
            "1 Thessalonians" : "1-Thessalonians",
            "2 Thessalonians" : "2-Thessalonians",
            "1 Timothy" : "1-Timothy",
            "2 Timothy" : "2-Timothy",
            "Titus" : "Titus",
            "Philemon" : "Philemon",
            "Hebrews" : "Hebrews",
            "James" : "James",
            "1 Peter" : "1-Peter",
            "2 Peter" : "2-Peter",
            "1 John" : "1-John",
            "2 John" : "2-John",
            "3 John" : "3-John",
            "Jude" : "Jude",
            "Revelation" : "Revelation"
        }

    def getText(self, book, chapter):

        # GET HTML CONTENT
        url = "https://www.biblestudytools.com/"+self.bookAbreviation[book].lower()+"/"+ str(chapter) + ".html"
        response = requests.get(url)

        if response.status_code == 200:

            # GET HTML
            soup = BeautifulSoup(response.content, "html.parser")
            bible_content = soup.find("div", class_="py-5 px-3 md:px-12 text-xl")

            # REMOVE NOTES
            for element in bible_content.find_all(recursive=True):
                if element.get("class") is not None:

                    # print(element.get("class"))
                    
                    if element.get("class")[0] == "verse-reference" or element.get("class")[0] == "text-blue-600":
                        element.extract()

                    if len(element.get("class")) >= 3:
                        if element.get("class")[2] == "subject-heading":
                            element.extract()


            # GENERATE TEXT STRING
            text = ""
            for e in bible_content:

                text += e.get_text()

            return text

        else:
            print("Failed to retrieve the webpage")
            return None
