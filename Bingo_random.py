from pyscript import display
from js import document
import js
import random

Bingo={
    1:"Lutes gets a new arm",
    2:"Abel hesitates to become the new leader of exorcists",
    3:"Lute is jealous of Abel",
    4:"No one knows about Lilith being in Heaven expect Lute",
    5:"Racism in Heaven",
    6:"Sir Pentious is feeling homesick",
    7:"Molly talks",
    8:"Emily is the only true person who comforts Sir Pentious in Heaven",
    9:"No egg bois in Heaven",
    10:"Sir Pentious mentions his egg boys",
    11:"Sir Pentious's crime in human world, was accindetally killing someone by his (any) invention",
    12:"Baxter is a spy",
    13:"Baxter's soul belongs to Vox",
    14:"We get to explain what are the egg bois",
    15:"Niffty tries to stab Baxter at least one time",
    16:"Niffty sings about how much she likes bad boys",
    17:"Cherri joins in the hotel  because of Sir Pentious",
    18:"We get a sense of an 'AFTER THE BATTLE' card, with Vox and Valentino",
    19:"Vox gets his screen broken",
    20:"Vox's hand gets cut off",
    21:"Something will crash Vox",
    22:"Clarification between Vox's and Valentino's relationship",
    23:"VEES has their song (all three sing together)",
    24:"Mini flashback of Vox's and Alastor's 'relationship'",
    25:"Vox's old design on screen (old CRT TV screen)",
    26:"Katie Killjoy goes to the hotel to get some report",
    27:"Screen time of Pepermint(Vox's eel assistant)",
    28:"Beef with Alastor and Lucifer",
    29:"Alastor doesn't get his cane back at least at the end of the season",
    30:"Lucifer learns about Charlie's and Alastor's 'soul' deal",
    31:"Vaggie comforts Charlie because she (Charlie) feels guilty about Sir Pentious death / misses him",
    32:"Flashback of Alastor's mother",
    33:"Abel is nothing like his Father",
    34:"Helluva boss reference or easter egg",
    35:"The same wall gets destroyed",
    36:"Screen time of Vox's sharks",
    37:"Vox uses his hypnotic eye",
    38:"Cherri adopts Frank",
    39:"Baxter was working with Sir Pentious (past invetor partners",
    40:"Someone sees Alastor's scar",
    41:"Baxter made the egg bois with Sir Pentious",
    42:"Baxter will be disgust / annoyed with Frank",
    43:"Someone will at least call Baxter short",
    44:"Cherri confused feelings of loving Sir Pentious",
    45:"Lucifer learns about Vaggie's wings",
    46:"Zestial promise to protect Carmilla",
    47:"Frederick Dev speaks(skull Overlord)",
    48:"Cannibals took care of Adam's body",
    49:"Alastor's death flashback",
    50:"Sir Pentious's death flashback",
    51:"Show of Valentino's drawings",
    52:"Valentino gets reverge of Angel (because of club accident)"
    }

def x(event=None):
    random_key=random.sample(list(Bingo.keys()),24)
    cells=document.querySelectorAll("td")
    data_index=0
    for i in range(len(cells)):
        if i==12:
            continue
        cells[i].innerText=random_key[data_index]
        data_index +=1

