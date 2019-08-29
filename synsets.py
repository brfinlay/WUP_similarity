import nltk 
from nltk.corpus import wordnet as wn


# Trying Wu Palmer similarity on "ant" and "bee" only 
syn1 = wn.synsets("ant")
syn2 = wn.synsets("bee")

ant = syn1[0]
bee = syn2[0]

ant.wup_similarity(bee)
# 91.66666% similarity
# Now for comparing semantic distance between ant and bee
ant.shortest_path_distance(bee)
# result was 2 units


# Animate and Inanimate Lists

animate_list = ["ant", "bee", "ear", "flamingo", "lion", "snail", "tiger", "zebra", "faces", "beaver", "cockroach", "dalmation", "fly", "goldfish", "goose", "gorilla", "grasshopper", "hamster", "hog", "koala", "ladybug", "otter", "ox", "peacock", "starfish", "triceratops", "wing"]
inanimate_big_list = ["ambulance", "barn", "bathtub", "church", "mailbox", "stove", "television", "tractor", "bookcase", "crib", "desk", "jeep", "lawn mower", "library", "pole", "racer", "refrigerator", "restaurant", "rocking chair", "screen", "sewing machine", "swing"]
inanimate_small_list = ["backpack", "banana", "baseball", "basketball", "broccoli", "broom", "bucket", "candle", "envelope", "hammer", "lipstick", "microphone", "nail", "necklace", "paintbrush", "pillow", "pineapple", "pizza", "radio", "screwdriver", "shovel", "sock", "strawberry", "teapot", "umbrella", "acorn", "balloon", "bib", "bow", "bubble", "cauliflower", "chain", "cheeseburger", "coffeepot", "comic book", "cucumber", "daisy", "diaper", "drum", "gown", "hay", "hook", "hotdog", "jean", "kite", "knot", "lampshade", "lemon", "lotion", "mailbag", "mask", "mitten", "orange", "pajama", "pencil sharpener", "piggy bank", "pot", "pretzel", "safe", "sandal", "spider web", "sunglass", "sunglasses", "sweatshirt", "tray", "wallet", "whistle", "wig"]

def get_synset(a_list):
    synset_list = []
    for word in a_list:
        a = wn.synsets(word)[:1] #The index is to ensure each word gets assigned 1st synset only
        synset_list.append(a)
    return synset_list


animate_synsets = get_synset(animate_list)

inanimate_big_synsets = get_synset(inanimate_big_list)

inanimate_small_synsets = get_synset(inanimate_small_list)



# Getting Definition of a Synset
#ant_def = wn.synset('ant.n.01').definition()
#print(ant_def)



def wn_syns(given_list): 
       synset_wn = []
       for word in given_list:
           synset_wn.append("wn.[%s]" % word)
       return synset_wn

animate_wn = wn_syns(animate_synsets)
inanimate_b_wn = wn_syns(inanimate_big_synsets)
inanimate_s_wn = wn_syns(inanimate_small_synsets)


def lower(list):
    new_list = []
    for word in list:
        new_list.append(word.lower())
    return new_list

lower_a = lower(animate_wn)
lower_ib = lower(inanimate_b_wn)
lower_is = lower(inanimate_s_wn)

def clean(a_list): 
    new_list = []
    for word in a_list:
        w = word.replace("[", "").replace("]", "").replace("wn.synset", "").replace("(", "").replace(")", "").replace("'", "")
        new_list.append(w)
    return new_list

clean_a = clean(lower_a)
clean_ib = clean(lower_ib)
clean_is = clean(lower_is)
print(clean_a)
print(clean_ib)
print(clean_is)

#def get_definitions(words):
   # definitions = []
    #for string in words:
     #   defin = (wn.synset(string)).definition()
      #  definitions.append(defin)
    #return definitions


#print(get_definitions(clean_a))
#print(get_definitions(clean_ib))
#print(get_definitions(clean_is))

# Definitions couldn't be obtained by a function since (a) synsets are not iterable, (b) string do not have attribute definition..

# Animate Definitions
ant = wn.synset('ant.n.01').definition()
bee = wn.synset('bee.n.01').definition()
ear = wn.synset('ear.n.01').definition()
flamingo = wn.synset('flamingo.n.01').definition()
lion = wn.synset('lion.n.01').definition()
snail = wn.synset('snail.n.01').definition()
tiger = wn.synset('tiger.n.01').definition()
zebra = wn.synset('zebra.n.01').definition()
faces = wn.synset('face.n.01').definition()
beaver = wn.synset('beaver.n.01').definition()
cockroach = wn.synset('cockroach.n.01').definition()
#dalmation = wn.synset('wn.').definition()
fly = wn.synset('fly.n.01').definition()
goldfish = wn.synset('goldfish.n.01').definition()
goose = wn.synset('goose.n.01').definition()
gorilla = wn.synset('gorilla.n.01').definition()
grasshopper = wn.synset('grasshopper.n.01').definition()
hamster = wn.synset('hamster.n.01').definition()
hog = wn.synset('hog.n.01').definition()
koala = wn.synset('koala.n.01').definition()
ladybug = wn.synset('ladybug.n.01').definition()
otter = wn.synset('otter.n.01').definition()
ox = wn.synset('ox.n.01').definition()
peacock = wn.synset('peacock.n.01').definition()
starfish = wn.synset('starfish.n.01').definition()
triceratops = wn.synset('triceratops.n.01').definition()
wing = wn.synset('wing.n.01').definition()



#Inanimate BIG
ambulance = wn.synset('ambulance.n.01').definition()
print(ambulance)
barn = wn.synset('barn.n.01').definition()
print(barn)
bathtub = wn.synset('bathtub.n.01').definition()
print(bathtub)
church = wn.synset('church.n.01').definition()
print(church)
mailbox = wn.synset('mailbox.n.01').definition()
print(mailbox)
stove = wn.synset('stove.n.01').definition()
print(stove)
television = wn.synset('television.n.01').definition()
print(television)
tractor = wn.synset('tractor.n.01').definition()
print(tractor)
bookcase = wn.synset('bookcase.n.01').definition()
print(bookcase)
crib = wn.synset('crib.n.01').definition()
print(crib)
desk = wn.synset('desk.n.01').definition()
print(desk)
jeep = wn.synset('jeep.n.01').definition()
print(jeep)
lawn_mower = wn.synset('wn.').definition()
library = wn.synset('library.n.01').definition()
print(library)
pole = wn.synset('pole.n.01').definition()
print(pole)
racer = wn.synset('racer.n.01').definition()
print(racer)
refrigerator = wn.synset('refrigerator.n.01').definition()
print(refrigerator)
restaurant = wn.synset('restaurant.n.01').definition()
print(restaurant)
rocking_chair = wn.synset('wn.').definition()
screen = wn.synset('screen.n.01').definition()
print(screen)
sewing_machine = wn.synset('wn.').definition()
swing = wn.synset('swing.n.01').definition()
print(swing)

#inanimate small
backpack = wn.synset('backpack.n.01').definition()
print(backpack)
banana = wn.synset('banana.n.01').definition()
print(banana) 
baseball = wn.synset('baseball.n.01').definition()
print(baseball)
basketball = wn.synset('basketball.n.01').definition()
print(basketball)
broccoli = wn.synset('broccoli.n.01').definition()
print(broccoli)
broom = wn.synset('broom.n.01').definition()
print(broom)
bucket = wn.synset('bucket.n.01').definition()
print(bucket)
candle = wn.synset('candle.n.01').definition()
print(candle)
envelope = wn.synset('envelope.n.01').definition()
print(envelope)
hammer = wn.synset('hammer.n.01').definition()
print(hammer)
lipstick = wn.synset('lipstick.n.01').definition()
print(lipstick)
microphone = wn.synset('microphone.n.01').definition()
print(microphone)
nail = wn.synset('nail.n.01').definition()
print(nail)
necklace = wn.synset('necklace.n.01').definition()
print(necklace)
paintbrush = wn.synset('paintbrush.n.01').definition()
print(paintbrush)
pillow = wn.synset('pillow.n.01').definition()
print(pillow)
pineapple = wn.synset('pineapple.n.01').definition()
print(pineapple)
pizza = wn.synset('pizza.n.01').definition()
print(pizza)
radio = wn.synset('radio.n.01').definition()
print(radio)
screwdriver = wn.synset('screwdriver.n.01').definition()
print(screwdriver)
shovel = wn.synset('shovel.n.01').definition()
print(shovel)
sock = wn.synset('sock.n.01').definition()
print(sock)
strawberry = wn.synset('strawberry.n.01').definition()
print(strawberry)
teapot = wn.synset('teapot.n.01').definition()
print(teapot)
umbrella = wn.synset('umbrella.n.01').definition()
print(umbrella)
acorn = wn.synset('acorn.n.01').definition()
print(acorn)
balloon = wn.synset('balloon.n.01').definition()
print(balloon)
bib = wn.synset('bib.n.01').definition()
print(bib)
bow = wn.synset('bow.n.01').definition()
print(bow)
bubble = wn.synset('bubble.n.01').definition()
print(bubble)
cauliflower = wn.synset('cauliflower.n.01').definition()
print(cauliflower)
chain = wn.synset('chain.n.01').definition()
print(chain)
cheeseburger = wn.synset('cheeseburger.n.01').definition()
print(cheeseburger)
coffeepot = wn.synset('coffeepot.n.01').definition()
print(coffeepot)
#comic_book = wn.synset('wn.').definition()
cucumber = wn.synset('cucumber.n.01').definition()
print(cucumber)
daisy = wn.synset('daisy.n.01').definition()
print(daisy)
diaper = wn.synset('diaper.n.01').definition()
print(diaper)
drum = wn.synset('drum.n.01').definition()
print(drum)
gown = wn.synset('gown.n.01').definition()
print(gown)
hay = wn.synset('hay.n.01').definition()
print(hay)
hook = wn.synset('hook.n.01').definition()
print(hook)
hotdog = wn.synset('hotdog.n.01').definition()
print(hotdog)
jean = wn.synset('jean.n.01').definition()
print(jean)
kite = wn.synset('kite.n.01').definition()
print(kite)
knot = wn.synset('knot.n.01').definition()
print(knot)
lampshade = wn.synset('lampshade.n.01').definition()
print(lampshade)
lemon = wn.synset('lemon.n.01').definition()
print(lemon)
lotion = wn.synset('lotion.n.01').definition()
print(lotion)
mailbag = wn.synset('mailbag.n.01').definition()
print(mailbag)
mask = wn.synset('mask.n.01').definition()
print(mask)
mitten = wn.synset('mitten.n.01').definition()
print(mitten)
orange = wn.synset('orange.n.01').definition()
print(orange)
pajama = wn.synset('pajama.n.01').definition()
print(pajama)
#pencil_sharpener = wn.synset('wn.').definition()
#piggy_bank = wn.synset('wn.').definition()
pot = wn.synset('pot.n.01').definition()
print(pot)
pretzel = wn.synset('pretzel.n.01').definition()
print(pretzel)
safe = wn.synset('safe.n.01').definition()
print(safe)
sandal = wn.synset('sandal.n.01').definition()
print(sandal)
#spider_web = wn.synset('wn.').definition()
sunglass = wn.synset('sunglass.n.01').definition()
print(sunglass)
sunglasses = wn.synset('sunglasses.n.01').definition()
print(sunglasses)
sweatshirt = wn.synset('sweatshirt.n.01').definition()
print(sweatshirt)
tray = wn.synset('tray.n.01').definition()
print(tray)
wallet = wn.synset('wallet.n.01').definition()
print(wallet)
whistle = wn.synset('whistle.n.01').definition()
print(whistle)
wig = wn.synset('wig.n.01').definition()
print(wig)


dodgy_defs = ['bee', 'tiger', 'beaver', 'cockroach', 'hog', 'otter', 'peacock', 'church', 'mailbox', 'television', 'refrigerator', 'swing', 'banana', 'broccoli', 'hammer', 'radio', 'chain', 'hotdog', 'kite', 'pajama', 'whistle']


def get_synset_n2(a_list):
    synset_list = []
    for word in a_list:
        a = wn.synsets(word)[1:2] 
        synset_list.append(a)
    return synset_list

syn_2 = get_synset_n2(dodgy_defs)
wn_2 = wn_syns(syn_2)
lower_syn_2 = lower(wn_2)
clean_syn_2 = clean(lower_syn_2)
print(clean_syn_2)

#Definition of Syn[1]
bee_1 = wn.synset('bee.n.02').definition()
print(bee_1)
tiger_1 = wn.synset('tiger.n.02').definition()
print(tiger_1)
beaver_1 = wn.synset('oregonian.n.01').definition()
print(beaver_1)
#cockroach_1 = wn.synset('wn.').definition()
hog_1 = wn.synset('hog.n.02').definition()
print(hog_1)
otter_1 = wn.synset('otter.n.02').definition()
print(otter_1)
peacock_1 = wn.synset('peacock.n.02').definition()
print(peacock_1)
church_1 = wn.synset('church.n.02').definition()
print(church_1)
mailbox_1 = wn.synset('postbox.n.01').definition()
print(mailbox_1)
television_1 = wn.synset('television.n.02').definition()
print(television_1)
#refrigerator_1 = wn.synset('wn.').definition()
swing_1 = wn.synset('swing.n.02').definition()
print(swing_1)
banana_1 = wn.synset('banana.n.02').definition()
print(banana_1)
broccoli_1 = wn.synset('broccoli.n.02').definition()
print(broccoli_1)
hammer_1 = wn.synset('hammer.n.02').definition()
print(hammer_1)
radio_1 = wn.synset('radio_receiver.n.01').definition()
print(radio_1)
chain_1 = wn.synset('chain.n.02').definition()
print(chain_1)
hotdog_1 = wn.synset('hotdog.n.02').definition()
print(hotdog_1)
kite_1 = wn.synset('kite.n.02').definition()
print(kite_1)
pajama_1 = wn.synset('pajama.n.02').definition()
print(pajama_1)
whistle_1 = wn.synset('whistle.n.02').definition()
print(whistle_1)

# Stubborn ones

wn.synsets('cockroach')
wn.synsets('refrigerator')
wn.synsets('bee')
wn.synsets('beaver')
wn.synsets('hog')
wn.synsets('kite')

#Beaver
b3 = wn.synset('beaver.n.03').definition()
print(b3)
b5 = wn.synset('beaver.n.05').definition()
print(b5)
b6 = wn.synset('beaver.n.06').definition()
print(b6)
b7 = wn.synset('beaver.n.07').definition()
print(b7)

#Hog
h3 = wn.synset('hog.n.03').definition()
print(h3)

#Kite
k3 = wn.synset('kite.n.03').definition()
print(k3)
k4 = wn.synset('kite.n.04').definition()
print(k4)

# WuPalmer Similarity 
# Animate - In B
# Animate - In S
# In B - In S

#1st, assign variables to final synsets

#animate_variables 
ant_syn = wn.synset('ant.n.01')
bee_syn = wn.synset('bee.n.01')
ear_syn = wn.synset('ear.n.01')
flamingo_syn = wn.synset('flamingo.n.01')
lion_syn = wn.synset('lion.n.01')
snail_syn = wn.synset('snail.n.01')
tiger_syn = wn.synset('tiger.n.02')
zebra_syn = wn.synset('zebra.n.01')
face_syn = wn.synset('face.n.01')
beaver_syn = wn.synset('beaver.n.07')
cockroach_syn = wn.synset('cockroach.n.01')
fly_syn = wn.synset('fly.n.01')
goldfish_syn = wn.synset('goldfish.n.01')
goose_syn = wn.synset('goose.n.01')
gorilla_syn = wn.synset('gorilla.n.01')
grasshopper_syn = wn.synset('grasshopper.n.01')
hamster_syn = wn.synset('hamster.n.01')
hog_syn = wn.synset('hog.n.03')
koala_syn = wn.synset('koala.n.01')
ladybug_syn = wn.synset('ladybug.n.01')
otter_syn = wn.synset('otter.n.02')
ox_syn = wn.synset('ox.n.01')
peacock_syn = wn.synset('peacock.n.02')
starfish_syn = wn.synset('starfish.n.01')
triceratops_syn = wn.synset('triceratops.n.01')
wing_syn = wn.synset('wing.n.01')

animate_variables = [ant_syn, bee_syn, ear_syn, flamingo_syn, lion_syn, snail_syn, tiger_syn, zebra_syn, face_syn, beaver_syn, cockroach_syn, fly_syn, goldfish_syn, goose_syn, gorilla_syn, grasshopper_syn, hamster_syn, hog_syn, koala_syn, ladybug_syn, otter_syn, ox_syn, peacock_syn, starfish_syn, triceratops_syn, wing_syn]

#ib_variables
ambulance_syn = wn.synset('ambulance.n.01')
barn_syn = wn.synset('barn.n.01')
bathtub_syn = wn.synset('bathtub.n.01')
church_syn = wn.synset('church.n.02')
postbox_syn = wn.synset('postbox.n.01')
stove_syn = wn.synset('stove.n.01')
television_syn = wn.synset('television.n.02')
tractor_syn = wn.synset('tractor.n.01')
bookcase_syn = wn.synset('bookcase.n.01')
crib_syn = wn.synset('crib.n.01')
desk_syn = wn.synset('desk.n.01')
jeep_syn = wn.synset('jeep.n.01')
library_syn = wn.synset('library.n.01')
pole_syn = wn.synset('pole.n.01')
racer_syn = wn.synset('racer.n.01')
refrigerator_syn = wn.synset('refrigerator.n.01')
restaurant_syn = wn.synset('restaurant.n.01')
screen_syn = wn.synset('screen.n.01')
swing_syn = wn.synset('swing.n.02')

ib_variables = [ambulance_syn, barn_syn, bathtub_syn, church_syn, postbox_syn, stove_syn, television_syn, tractor_syn, bookcase_syn, crib_syn, desk_syn, jeep_syn, library_syn, pole_syn, racer_syn, refrigerator_syn, restaurant_syn, screen_syn, swing_syn]

#is_variables
backpack_syn = wn.synset('backpack.n.01')
banana_syn = wn.synset('banana.n.02')
baseball_syn = wn.synset('baseball.n.01')
basketball_syn = wn.synset('basketball.n.01')
broccoli_syn = wn.synset('broccoli.n.01')
broom_syn = wn.synset('broom.n.01')
bucket_syn = wn.synset('bucket.n.01')
candle_syn = wn.synset('candle.n.01')
envelope_syn = wn.synset('envelope.n.01')
hammer_syn = wn.synset('hammer.n.02')
lipstick_syn = wn.synset('lipstick.n.01')
microphone_syn = wn.synset('microphone.n.01')
nail_syn = wn.synset('nail.n.01')
necklace_syn = wn.synset('necklace.n.01')
paintbrush_syn = wn.synset('paintbrush.n.01')
pillow_syn = wn.synset('pillow.n.01')
pineapple_syn = wn.synset('pineapple.n.01')
pizza_syn = wn.synset('pizza.n.01')
radio_syn = wn.synset('radio_receiver.n.01')
screwdriver_syn = wn.synset('screwdriver.n.01')
shovel_syn = wn.synset('shovel.n.01')
sock_syn = wn.synset('sock.n.01')
strawberry_syn = wn.synset('strawberry.n.01')
teapot_syn = wn.synset('teapot.n.01')
umbrella_syn = wn.synset('umbrella.n.01')
acorn_syn = wn.synset('acorn.n.01')
balloon_syn = wn.synset('balloon.n.01')
bib_syn = wn.synset('bib.n.01')
bow_syn = wn.synset('bow.n.01')
bubble_syn = wn.synset('bubble.n.01')
cauliflower_syn = wn.synset('cauliflower.n.01')
chain_syn = wn.synset('chain.n.01')
cheeseburger_syn = wn.synset('cheeseburger.n.01')
coffeepot_syn = wn.synset('coffeepot.n.01')
cucumber_syn = wn.synset('cucumber.n.01')
daisy_syn = wn.synset('daisy.n.01')
diaper_syn = wn.synset('diaper.n.01')
drum_syn = wn.synset('drum.n.01')
gown_syn = wn.synset('gown.n.01')
hay_syn = wn.synset('hay.n.01')
hook_syn = wn.synset('hook.n.01')
hotdog_syn = wn.synset('hotdog.n.02')
jean_syn = wn.synset('jean.n.01')
kite_syn = wn.synset('kite.n.03')
knot_syn = wn.synset('knot.n.01')
lampshade_syn = wn.synset('lampshade.n.01')
lemon_syn = wn.synset('lemon.n.01')
lotion_syn = wn.synset('lotion.n.01')
mailbag_syn = wn.synset('mailbag.n.01')
mask_syn = wn.synset('mask.n.01')
mitten_syn = wn.synset('mitten.n.01')
orange_syn = wn.synset('orange.n.01')
pajama_syn = wn.synset('pajama.n.02')
pot_syn = wn.synset('pot.n.01')
pretzel_syn = wn.synset('pretzel.n.01')
safe_syn = wn.synset('safe.n.01')
sandal_syn = wn.synset('sandal.n.01')
sunglass_syn = wn.synset('sunglass.n.01')
sunglasses_syn = wn.synset('sunglasses.n.01')
sweatshirt_syn = wn.synset('sweatshirt.n.01')
tray_syn = wn.synset('tray.n.01')
wallet_syn = wn.synset('wallet.n.01')
whistle_syn = wn.synset('whistle.n.02')
wig_syn = wn.synset('wig.n.01')

is_variables = [backpack_syn, banana_syn, baseball_syn, basketball_syn, broccoli_syn, broom_syn, bucket_syn, candle_syn, envelope_syn, hammer_syn, lipstick_syn, microphone_syn, nail_syn, necklace_syn, paintbrush_syn, pillow_syn, pineapple_syn, pizza_syn, radio_syn, screwdriver_syn, shovel_syn, sock_syn, strawberry_syn, teapot_syn, umbrella_syn, acorn_syn, balloon_syn, bib_syn, bow_syn, bubble_syn, cauliflower_syn, chain_syn, cheeseburger_syn, coffeepot_syn, cucumber_syn, daisy_syn, diaper_syn, drum_syn, gown_syn, hay_syn, hook_syn, hotdog_syn, jean_syn, kite_syn, knot_syn, lampshade_syn, lemon_syn, lotion_syn, mailbag_syn, mask_syn, mitten_syn, orange_syn, pajama_syn, pot_syn, pretzel_syn, safe_syn, sandal_syn, sunglass_syn, sunglasses_syn, sweatshirt_syn, tray_syn, wallet_syn, whistle_syn, wig_syn]

# wup similarity

def similarity(list1, list2):
    sim_dict = {}
    for syn in list1:
        for sin in list2:
            sim = (syn).wup_similarity(sin)
            if sim >= 0.5:
                sim_dict.update({(syn, sin): sim})
    return sim_dict

a_b = similarity(animate_variables, ib_variables)
a_s = similarity(animate_variables, is_variables)
b_s = similarity(ib_variables, is_variables)


key = list(b_s.keys())
value = list(b_s.values())

import pandas as pd

df = pd.DataFrame()
df['keys'] = key
df['values'] = value

df.to_csv('/Users/brendafinlay/Documents/Cusack Lab/synsets_dataframe.csv', index=False)

keya = list(a_s.keys())
valuea = list(a_s.values())

df = pd.DataFrame()
df['object'] = keya
df['score'] = valuea

df.to_csv('/Users/brendafinlay/Documents/Cusack Lab/animatescore_dataframe.csv', index=False)

def some_similarity(list1, list2):
    sim_dict = {}
    for syn in list1:
        for sin in list2:
            sim = (syn).wup_similarity(sin)
            if sim >= 0.25:
                sim_dict.update({(syn, sin): sim})
    return sim_dict

a_ib25 = some_similarity(animate_variables, ib_variables)

df = pd.DataFrame()
df['Animate, Big Inanimate'] = list(a_ib25.keys())
df['Score'] = list(a_ib25.values())
df.to_csv('/Users/brendafinlay/Documents/Cusack Lab/0.25_dataframe.csv', index=False)
