from hashlib import sha256
import processor as ps
import webscraper as scraper

rawInputs = []
cleanTexts = []

sermonText = scraper.SermonCentralText()
rawInput = sermonText.getText("Genesis", 50)

rawInputs.append(rawInput)

rawInputs.append('''
1Joseph threw himself on his father and wept over him and kissed him. 2Then Joseph directed the physicians in his service to embalm his father Israel. So the physicians embalmed him,

3taking a full forty days, for that was the time required for embalming. And the Egyptians mourned for him seventy days. 4When the days of mourning had passed, Joseph said to Pharaoh’s court, “If I have found favor in your eyes, speak to Pharaoh for me. Tell him,

5‘My father made me swear an oath and said, “I am about to die; bury me in the tomb I dug for myself in the land of Canaan.” Now let me go up and bury my father; then I will return.’ ”

6Pharaoh said, “Go up and bury your father, as he made you swear to do.” 7So Joseph went up to bury his father. All Pharaoh’s officials accompanied him—the dignitaries of his court and all the dignitaries of Egypt— 8besides all the members of Joseph’s household and his brothers and those belonging to his father’s household. Only their children and their flocks and herds were left in Goshen.

9Chariots and horsemen [a] also went up with him. It was a very large company. 10When they reached the threshing floor of Atad, near the Jordan, they lamented loudly and bitterly; and there Joseph observed a seven-day period of mourning for his father.

11When the Canaanites who lived there saw the mourning at the threshing floor of Atad, they said, “The Egyptians are holding a solemn ceremony of mourning.” That is why that place near the Jordan is called Abel Mizraim. [b] 12So Jacob’s sons did as he had commanded them: 13They carried him to the land of Canaan and buried him in the cave in the field of Machpelah, near Mamre, which Abraham had bought along with the field as a burial place from Ephron the Hittite.

14After burying his father, Joseph returned to Egypt, together with his brothers and all the others who had gone with him to bury his father.

Joseph Reassures His Brothers
15When Joseph’s brothers saw that their father was dead, they said, “What if Joseph holds a grudge against us and pays us back for all the wrongs we did to him?” 16So they sent word to Joseph, saying, “Your father left these instructions before he died:

17‘This is what you are to say to Joseph: I ask you to forgive your brothers the sins and the wrongs they committed in treating you so badly.’ Now please forgive the sins of the servants of the God of your father.” When their message came to him, Joseph wept.

18His brothers then came and threw themselves down before him. “We are your slaves,” they said. 19But Joseph said to them, “Don’t be afraid. Am I in the place of God? 20You intended to harm me, but God intended it for good to accomplish what is now being done, the saving of many lives.

21So then, don’t be afraid. I will provide for you and your children.” And he reassured them and spoke kindly to them.

The Death of Joseph
22Joseph stayed in Egypt, along with all his father’s family. He lived a hundred and ten years

23and saw the third generation of Ephraim’s children. Also the children of Makir son of Manasseh were placed at birth on Joseph’s knees. [c] 24Then Joseph said to his brothers, “I am about to die. But God will surely come to your aid and take you up out of this land to the land he promised on oath to Abraham, Isaac and Jacob.”

25And Joseph made the Israelites swear an oath and said, “God will surely come to your aid, and then you must carry my bones up from this place.” 26So Joseph died at the age of a hundred and ten. And after they embalmed him, he was placed in a coffin in Egypt.
''')

# rawInputs.append('''
# The Beginning
# 1In the beginning God created the heavens and the earth.
# 2Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. 3And God said, “Let there be light,” and there was light. 4God saw that the light was good, and he separated the light from the darkness.
# 5God called the light “day,” and the darkness he called “night.” And there was evening, and there was morning—the first day. 6And God said, “Let there be a vault between the waters to separate water from water.” 7So God made the vault and separated the water under the vault from the water above it. And it was so.
# 8God called the vault “sky.” And there was evening, and there was morning—the second day. 9And God said, “Let the water under the sky be gathered to one place, and let dry ground appear.” And it was so.
# 10God called the dry ground “land,” and the gathered waters he called “seas.” And God saw that it was good. 11Then God said, “Let the land produce vegetation: seed-bearing plants and trees on the land that bear fruit with seed in it, according to their various kinds.” And it was so. 12The land produced vegetation: plants bearing seed according to their kinds and trees bearing fruit with seed in it according to their kinds. And God saw that it was good.
# 13And there was evening, and there was morning—the third day. 14And God said, “Let there be lights in the vault of the sky to separate the day from the night, and let them serve as signs to mark sacred times, and days and years, 15and let them be lights in the vault of the sky to give light on the earth.” And it was so. 16God made two great lights—the greater light to govern the day and the lesser light to govern the night. He also made the stars. 17God set them in the vault of the sky to give light on the earth, 18to govern the day and the night, and to separate light from darkness. And God saw that it was good.
# 19And there was evening, and there was morning—the fourth day. 20And God said, “Let the water teem with living creatures, and let birds fly above the earth across the vault of the sky.” 21So God created the great creatures of the sea and every living thing with which the water teems and that moves about in it, according to their kinds, and every winged bird according to its kind. And God saw that it was good. 22God blessed them and said, “Be fruitful and increase in number and fill the water in the seas, and let the birds increase on the earth.”
# 23And there was evening, and there was morning—the fifth day. 24And God said, “Let the land produce living creatures according to their kinds: the livestock, the creatures that move along the ground, and the wild animals, each according to its kind.” And it was so.
# 25God made the wild animals according to their kinds, the livestock according to their kinds, and all the creatures that move along the ground according to their kinds. And God saw that it was good.
# 26Then God said, “Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, [a] and over all the creatures that move along the ground.”
# 27So God created mankind in his own image, in the image of God he created them; male and female he created them.
# 28God blessed them and said to them, “Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.” 29Then God said, “I give you every seed-bearing plant on the face of the whole earth and every tree that has fruit with seed in it. They will be yours for food.
# 30And to all the beasts of the earth and all the birds in the sky and all the creatures that move along the ground—everything that has the breath of life in it—I give every green plant for food.” And it was so. 31God saw all that he had made, and it was very good. And there was evening, and there was morning—the sixth day.
# ''')

# rawInputs.append('''
# The Beginning
# 1In the beginning God created the heavens and the earth. 2Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.
# 3And God said, “Let there be light,” and there was light. 4God saw that the light was good, and he separated the light from the darkness. 5God called the light “day,” and the darkness he called “night.” And there was evening, and there was morning—the first day.
# 6And God said, “Let there be a vault between the waters to separate water from water.” 7So God made the vault and separated the water under the vault from the water above it. And it was so. 8God called the vault “sky.” And there was evening, and there was morning—the second day.
# 9And God said, “Let the water under the sky be gathered to one place, and let dry ground appear.” And it was so. 10God called the dry ground “land,” and the gathered waters he called “seas.” And God saw that it was good.
# 11Then God said, “Let the land produce vegetation: seed-bearing plants and trees on the land that bear fruit with seed in it, according to their various kinds.” And it was so. 12The land produced vegetation: plants bearing seed according to their kinds and trees bearing fruit with seed in it according to their kinds. And God saw that it was good. 13And there was evening, and there was morning—the third day.
# 14And God said, “Let there be lights in the vault of the sky to separate the day from the night, and let them serve as signs to mark sacred times, and days and years, 15and let them be lights in the vault of the sky to give light on the earth.” And it was so. 16God made two great lights—the greater light to govern the day and the lesser light to govern the night. He also made the stars. 17God set them in the vault of the sky to give light on the earth, 18to govern the day and the night, and to separate light from darkness. And God saw that it was good. 19And there was evening, and there was morning—the fourth day.
# 20And God said, “Let the water teem with living creatures, and let birds fly above the earth across the vault of the sky.” 21So God created the great creatures of the sea and every living thing with which the water teems and that moves about in it, according to their kinds, and every winged bird according to its kind. And God saw that it was good. 22God blessed them and said, “Be fruitful and increase in number and fill the water in the seas, and let the birds increase on the earth.” 23And there was evening, and there was morning—the fifth day.
# 24And God said, “Let the land produce living creatures according to their kinds: the livestock, the creatures that move along the ground, and the wild animals, each according to its kind.” And it was so. 25God made the wild animals according to their kinds, the livestock according to their kinds, and all the creatures that move along the ground according to their kinds. And God saw that it was good.
# 26Then God said, “Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, and over all the creatures that move along the ground.”
# 27So God created mankind in his own image,
# in the image of God he created them;
# male and female he created them.
# 28God blessed them and said to them, “Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature that moves on the ground.”
# 29Then God said, “I give you every seed-bearing plant on the face of the whole earth and every tree that has fruit with seed in it. They will be yours for food. 30And to all the beasts of the earth and all the birds in the sky and all the creatures that move along the ground—everything that has the breath of life in it—I give every green plant for food.” And it was so.
# 31God saw all that he had made, and it was very good. And there was evening, and there was morning—the sixth day.
# ''')



# Remove line breaks and spaces
for i in range(0, len(rawInputs)):
    cleanTexts.append(rawInputs[i].replace('\n', ' '))
    cleanTexts[i] = cleanTexts[i].replace(' ', '_')
    cleanTexts[i] = ps.remove_footnote_brackets(cleanTexts[i])
    cleanTexts[i] = ps.remove_space_duplicates(cleanTexts[i], "_")



# # Remove Case differences
# for i in range(0, len(cleanTexts[0])):

#     if (input_text_1[i] != input_text_2[i]):
#         input_text_1 = replace_character_at_index(input_text_1, i, input_text_1[i].lower())
#         input_text_2 = replace_character_at_index(input_text_2, i, input_text_2[i].lower())


print("\nBIBLE HASHER")
print(f"\n \n")
for i in range(0, len(rawInputs)):
    print(cleanTexts[i])
    print(f"\n")

for i in range(0, len(rawInputs)):
    print(sha256(cleanTexts[i].encode('utf-8')).hexdigest())
