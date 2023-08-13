from hashlib import sha256
import processor as ps
import webscraper as scraper

rawInputs = []
cleanTexts = []

sermonText = scraper.SermonCentralText()
rawInput = sermonText.getText("Nehemiah", 8)

rawInputs.append(rawInput)

rawInputs.append('''
1all the people came together as one in the square before the Water Gate. They told Ezra the teacher of the Law to bring out the Book of the Law of Moses, which the Lord had commanded for Israel.
2So on the first day of the seventh month Ezra the priest brought the Law before the assembly, which was made up of men and women and all who were able to understand. 3He read it aloud from daybreak till noon as he faced the square before the Water Gate in the presence of the men, women and others who could understand. And all the people listened attentively to the Book of the Law.
4Ezra the teacher of the Law stood on a high wooden platform built for the occasion. Beside him on his right stood Mattithiah, Shema, Anaiah, Uriah, Hilkiah and Maaseiah; and on his left were Pedaiah, Mishael, Malkijah, Hashum, Hashbaddanah, Zechariah and Meshullam.
5Ezra opened the book. All the people could see him because he was standing above them; and as he opened it, the people all stood up. 6Ezra praised the Lord, the great God; and all the people lifted their hands and responded, “Amen! Amen!” Then they bowed down and worshiped the Lord with their faces to the ground.
7The Levites—Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodiah, Maaseiah, Kelita, Azariah, Jozabad, Hanan and Pelaiah—instructed the people in the Law while the people were standing there. 8They read from the Book of the Law of God, making it clear and giving the meaning so that the people understood what was being read.
9Then Nehemiah the governor, Ezra the priest and teacher of the Law, and the Levites who were instructing the people said to them all, “This day is holy to the Lord your God. Do not mourn or weep.” For all the people had been weeping as they listened to the words of the Law.
10Nehemiah said, “Go and enjoy choice food and sweet drinks, and send some to those who have nothing prepared. This day is holy to our Lord. Do not grieve, for the joy of the Lord is your strength.”
11The Levites calmed all the people, saying, “Be still, for this is a holy day. Do not grieve.”
12Then all the people went away to eat and drink, to send portions of food and to celebrate with great joy, because they now understood the words that had been made known to them.
13On the second day of the month, the heads of all the families, along with the priests and the Levites, gathered around Ezra the teacher to give attention to the words of the Law. 14They found written in the Law, which the Lord had commanded through Moses, that the Israelites were to live in temporary shelters during the festival of the seventh month 15and that they should proclaim this word and spread it throughout their towns and in Jerusalem: “Go out into the hill country and bring back branches from olive and wild olive trees, and from myrtles, palms and shade trees, to make temporary shelters”—as it is written.
16So the people went out and brought back branches and built themselves temporary shelters on their own roofs, in their courtyards, in the courts of the house of God and in the square by the Water Gate and the one by the Gate of Ephraim. 17The whole company that had returned from exile built temporary shelters and lived in them. From the days of Joshua son of Nun until that day, the Israelites had not celebrated it like this. And their joy was very great.
18Day after day, from the first day to the last, Ezra read from the Book of the Law of God. They celebrated the festival for seven days, and on the eighth day, in accordance with the regulation, there was an assembly.
''')



# Remove line breaks and spaces
for i in range(0, len(rawInputs)):
    cleanTexts.append(rawInputs[i].replace('\n', ''))
    cleanTexts[i] = cleanTexts[i].replace(' ', '')
    cleanTexts[i] = ps.remove_footnote_brackets(cleanTexts[i])
    cleanTexts[i] = ps.capitalize_all(cleanTexts[i])

print("\nBIBLE HASHER")
print(f"\n \n")
for i in range(0, len(rawInputs)):
    print(cleanTexts[i])
    print(f"\n")

for i in range(0, len(rawInputs)):
    print(sha256(cleanTexts[i].encode('utf-8')).hexdigest())
