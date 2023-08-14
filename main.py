from hashlib import sha256
import processor as ps
import webscraper as scraper


def cleanRawText(rawText):
    cleanText = ""
    cleanText = rawText.replace('\n', ' ')
    cleanText = ps.capitalize_all(cleanText)
    cleanText = ps.whitelist_symbols(cleanText, [".", '”', "“", "!", "?", ",", "’", ":", ";", "(", ")"])
    cleanText = ps.remove_footnotes(cleanText)
    cleanText = ps.remove_space_duplicates(cleanText, " ")
    cleanText = ps.insert_spaces_between_numbers_and_words(cleanText)
    cleanText = ps.remove_spaces_before(cleanText, [".", '”', "!", "?", ",", "’", ":", ";", ")"])

    return cleanText

# Webscraper class
youText = scraper.YouVersionScraper()
sermonText = scraper.SermonCentralScraper()

for i in range(1, 50):

    # YouText Text Processing
    rawText1 = youText.getText("Genesis", i)
    cleanText1 = cleanRawText(rawText1)

    # SermonText Text Processing
    rawText2 = sermonText.getText("Genesis", i)
    cleanText2 = cleanRawText(rawText2)

    # Console output
    hash1 = sha256(cleanText1.encode('utf-8')).hexdigest()
    hash2 = sha256(cleanText2.encode('utf-8')).hexdigest()
    print(hash1)
  

    if (hash1 != hash2):
        print(f"Genesis {i}")
        print(hash1)
        print(hash2)   
        print(cleanText1)
        print(cleanText2)
        print("\n")
