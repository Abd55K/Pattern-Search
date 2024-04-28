# Pattern-Search
Searches a 2D pattern in the 2D image 

Sample Run:
>>> P1 = ["AXA", "XAY"]
>>> P2 = ["AXA", "XAZ"]
>>> I = ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"]
>>> pattern_search(P1, I)
(1, 3, 270)
>>> pattern_search(P2, I)
False
