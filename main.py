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
    cleanText = ps.remove_spaces_after(cleanText, ["(", "“"])

    return cleanText

# Webscraper class
youText = scraper.YouVersionScraper()
sermonText = scraper.SermonCentralScraper()

book = "Judges"

for i in range(21):

    # YouText Text Processing
    rawText1 = youText.getText(book, i+1)
    cleanText1 = cleanRawText(rawText1)

    # SermonText Text Processing
    rawText2 = sermonText.getText(book, i+1)
    cleanText2 = cleanRawText(rawText2)

    # Console output
    hash1 = sha256(cleanText1.encode('utf-8')).hexdigest()
    hash2 = sha256(cleanText2.encode('utf-8')).hexdigest()

    if (hash1 != hash2):
        print(f"{book} {i+1}")
        print(hash1)
        print(hash2)   
        print(cleanText1)
        print(cleanText2)
        print("\n")

    else:
        print(hash1)   

