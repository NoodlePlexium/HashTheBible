from hashlib import sha256
import processor as ps
import webscraper as scraper
import time


def cleanRawText(rawText):
    cleanText = ""
    cleanText = rawText.replace('\n', ' ')
    cleanText = ps.capitalize_all(cleanText)
    cleanText = ps.whitelist_characters(cleanText, " .,”“!?;:’()—ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    cleanText = ps.insert_spaces_between_numbers_and_words(cleanText)
    cleanText = ps.format_numbers_with_commas(cleanText)
    cleanText = ps.remove_space_duplicates(cleanText, " ")

    # SYMBOL SPACING
    cleanText = ps.insert_spaces_after(cleanText, [",", ".", "!", "?", ")", '”', ";", ":"])
    cleanText = ps.insert_spaces_before(cleanText, ["(", "“"])
    cleanText = ps.remove_spaces_before(cleanText, ["”", ")", "’", "!", "?", ",", ".", ";", ":", "—"])
    cleanText = ps.remove_spaces_after(cleanText, ["“", "(", "—"])

    cleanText = ps.remove_spaces_between_numbers(cleanText)

    return cleanText

BibleFormat = {
    "Genesis": 50,
    "Exodus": 40,
    "Leviticus": 27,
    "Numbers": 36,
    "Deuteronomy": 34,
    "Joshua": 24,
    "Judges": 21,
    "Ruth": 4,
    "1 Samuel": 31,
    "2 Samuel": 24,
    "1 Kings": 22,
    "2 Kings": 25,
    "1 Chronicles": 29,
    "2 Chronicles": 36,
    "Ezra": 10,
    "Nehemiah": 13,
    "Esther": 10,
    "Job": 42,
    "Psalms": 150,
    "Proverbs": 31,
    "Ecclesiastes": 12,
    "Song of Songs": 8,
    "Isaiah": 66,
    "Jeremiah": 52,
    "Lamentations": 5,
    "Ezekiel": 48,
    "Daniel": 12,
    "Hosea": 14,
    "Joel": 3,
    "Amos": 9,
    "Obadiah": 1,
    "Jonah": 4,
    "Micah": 7,
    "Nahum": 3,
    "Habakkuk": 3,
    "Zephaniah": 3,
    "Haggai": 2,
    "Zechariah": 14,
    "Malachi": 4,
    "Matthew": 28,
    "Mark": 16,
    "Luke": 24,
    "John": 21,
    "Acts": 28,
    "Romans": 16,
    "1 Corinthians": 16,
    "2 Corinthians": 13,
    "Galatians": 6,
    "Ephesians": 6,
    "Philippians": 4,
    "Colossians": 4,
    "1 Thessalonians": 5,
    "2 Thessalonians": 3,
    "1 Timothy": 6,
    "2 Timothy": 4,
    "Titus": 3,
    "Philemon": 1,
    "Hebrews": 13,
    "James": 5,
    "1 Peter": 5,
    "2 Peter": 3,
    "1 John": 5,
    "2 John": 1,
    "3 John": 1,
    "Jude": 1,
    "Revelation": 22
}


# Webscraper class
youText = scraper.YouVersionScraper()
sermonText = scraper.SermonCentralScraper()
gatewayText = scraper.BibleGatewayScraper()

# Create a text file for writing
output_file = open("output.txt", "w")


start_time = time.time()
for book, chapters in BibleFormat.items():
    
    print(book)

    output_file.write(f"{book}\n")

    for i in range(int(chapters)):

        # YouText Text Processing
        rawText1 = youText.getText(book, i+1)
        cleanText1 = cleanRawText(rawText1)

        # SermonText Text Processing
        rawText2 = sermonText.getText(book, i+1)
        cleanText2 = cleanRawText(rawText2)

        # Bible Gateway Text Processing
        rawText3 = gatewayText.getText(book, i+1)
        cleanText3 = cleanRawText(rawText3)

        # print(cleanText1)
        # print(cleanText2)
        # print(cleanText3)

        hash1 = sha256(cleanText1.encode('utf-8')).hexdigest()
        hash2 = sha256(cleanText2.encode('utf-8')).hexdigest()
        hash3 = sha256(cleanText3.encode('utf-8')).hexdigest()

        # good
        if (hash1 == hash2):
            print(hash1)
            output_file.write(hash1 + "\n")

        elif (hash1 == hash2):
            print(hash1)
            output_file.write(hash1 + "\n")

        elif (hash2 == hash3):
            print(hash2)
            output_file.write(hash2 + "\n")   

        elif (hash1 == hash3):
            print(hash1)
            output_file.write(hash3 + "\n")        

        else: 
            print("\n\n\n")
            print(f"Hash mismatch {book} {i+1}")
            print(hash1)
            print(hash2)
            print(hash3)
            print(cleanText1)
            print("\n")
            print(cleanText2)
            print("\n")
            print(cleanText3)
            output_file.write(f"HASH CONFLICT! {hash1}\n")

    output_file.write("\n")     
    print("\n")   


# Close the output file
output_file.close()

print(time.time() - start_time)
