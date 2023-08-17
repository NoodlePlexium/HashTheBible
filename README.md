# HashTheBible
A project focused on preserving the original Bible text cryptographically, protecting it from false teachings and false edits.

Every chapter from every book form an many translations as possible wll be hased using SHA256. These hashes will be stored on the Ethereum blockchain using smart contracts.
Nobody will be able to counterfiet a single letter in the Bible



## NIV BIBLE HASH
### eb2d16cf74478a1104660ba3db69fad493625d848cbbb459780244b3018187f4

## ALL NIV CHAPTER HASHES
https://github.com/NoodlePlexium/HashTheBible/blob/main/NIV-HASHES.txt


## HASHING AND FORMATTING RULES:
No headers
No verse numbers

1 - remove line spacing
2 - capitalize all
3 - whitelist characters  .,”“!?;:’()— ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
4 - remove space duplicates
5 - insert spaces between numbers and letters
6 - format numbers with commas
7 - remove space duplicates
8 - insert spaces after , . ! ? ) ” ; :
9 - insert spaces before ( “
10 - remove spaces before ” ) ’ ! ? , . ; : —
11 - remove spaces after “ ( —
12 - remove spaces between numbers


## BLOCKCHAIN STORAGE COST ESTIMATE
The cost of storing 50 hashes as of 2023/08/14 is $33.21

gas price = 18
256 bits costs 20000 gwei
data = 256 bits * 50 
gwei cost = 1mil
Eth cost = 18 * 1mil / 1,000,000,000 = 0.018 Eth
Dollar cost = 0.018 * 1845 
### = $33.21
