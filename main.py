from hashlib import sha256
import processor as ps
import webscraper as scraper


sermonText = scraper.SermonCentralText()

for i in range(1, 50):

    rawInput = sermonText.getText("Genesis", i)
    cleanText = ""

    # Remove line breaks and spaces
    cleanText = rawInput.replace('\n', ' ')
    cleanText = cleanText.replace(' ', '_')
    cleanText = ps.remove_footnote_brackets(cleanText)
    cleanText = ps.remove_space_duplicates(cleanText, "_")

    print(sha256(cleanText.encode('utf-8')).hexdigest())
