import pygame
import random
import sys
import os
import math
import csv
import time
last_income_time = time.time()


# Initialisation de Pygame
pygame.init()
pygame.mixer.init()


# Dimensions de la fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()  # Met à jour les dimensions avec celles de l'écran


# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (30, 30, 60)

def load_image(filename, width=None, height=None):
    """Charge une image en gérant le bon chemin d'accès."""
    # Gestion des chemins pour PyInstaller
    if getattr(sys, '_MEIPASS', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    
    image_path = os.path.join(base_path, filename)
    image = pygame.image.load(image_path)

    if width and height:
        image = pygame.transform.scale(image, (width, height))
    
    return image


# Fonction pour charger l'image d'une carte spécifique
def load_card_image(card_name):
    card_info = cards.get(card_name)
    if card_info:
        return load_image(card_info["image"], 300, 400)  # Charge l'image de la carte avec la fonction load_image
    else:
        return None  # Si la carte n'existe pas

# Chargement des images


booster_img = load_image("images/booster.png")
booster_img2 = load_image("images/BOpack.png")
booster_img3 = load_image("images/packicon.png")
booster_img4 = load_image("images/packcol.png")
card_back_img = load_image("images/card_back.jpg", 300, 400)
background_img = load_image("images/background2.jpg", WIDTH, HEIGHT)
background_img2 = load_image("images/background.jpg", WIDTH, HEIGHT)
background_img3 = load_image("images/win.jpg", WIDTH, HEIGHT)
background_img4 = load_image("images/bleu.jpg", WIDTH, HEIGHT)
background_img5 = load_image("images/vert.jpg", WIDTH, HEIGHT)
background_img6 = load_image("images/rouge.jpg", WIDTH, HEIGHT)
background_img7 = load_image("images/violet.jpg", WIDTH, HEIGHT)
background_img8 = load_image("images/fond.jpg", WIDTH, HEIGHT)
background_img9 = load_image("images/BO.jpg", WIDTH, HEIGHT)
background_img10 = load_image("images/EAC.jpg", WIDTH, HEIGHT)
background_img11 = load_image("images/iconb.jpg", WIDTH, HEIGHT)
background_img12 = load_image("images/bg.jpg", WIDTH, HEIGHT)
background_img13 = load_image("images/fu.webp", WIDTH, HEIGHT)
background_img14 = load_image("images/fl.jpg", WIDTH, HEIGHT)
background_img15 = load_image("images/vi.jpg", WIDTH, HEIGHT)
background_img16 = load_image("images/bg16.jpg", WIDTH, HEIGHT)
terrain = load_image("images/terrain.jpg", WIDTH, HEIGHT)



# Définition des annonces disponibles
annonces = {
    "Porsche 911 GT2 RS": {"image": "images/p.jpg", "price": 289175, "category": "Voitures"},
    "Porsche 911 GT3 RS": {"image": "images/iris.jpg", "price": 248000, "category": "Voitures"},
    "Ferrari LaFerrari": {"image": "images/lf.jpg", "price": 4000000, "category": "Voitures"},
    "Aston Martin DBS": {"image": "images/martin.jpg", "price": 274995, "category": "Voitures"},
    "BMW M4 G82": {"image": "images/g82.jpg", "price": 194100, "category": "Voitures"},
    "Bugatti Bolide": {"image": "images/bolide.jpeg", "price": 4150000, "category": "Voitures"},
    "Ferrari 812 Superfast": {"image": "images/812.jpg", "price": 569974, "category": "Voitures"},
    "Bugatti Divo": {"image": "images/divo.jpg", "price": 5000000, "category": "Voitures"},
    "Revuelto Spécial": {"image": "images/revuelto.jpg", "price": 510000, "category": "Voitures"},
    "Lamborghini revuelto": {"image": "images/rev2.jpg", "price": 500000, "category": "Voitures"},
    "tofaş yelkenci": {"image": "images/aze.jpg", "price": 5000, "category": "Voitures"},
    "Tuatara Striker": {"image": "images/tuatara.webp", "price": 2200000, "category": "Voitures"},
    "Mercedes AMG GT": {"image": "images/amg.jpg", "price": 134950, "category": "Voitures"},
    "Chevrolet Corvette": {"image": "images/corvet.png", "price": 132000, "category": "Voitures"},
    "Chevrolet Corvette c8 stingray": {"image": "images/c8.jpg", "price": 250000, "category": "Voitures"},
    "Ferrari 458 Italia": {"image": "images/458.jpg", "price": 510000, "category": "Voitures"},
    "Audi RS6 GT": {"image": "images/rs6.jpg", "price": 192500, "category": "Voitures"},
    "Lamborghini Veneno": {"image": "images/venemo.jpg", "price": 10000000, "category": "Voitures"},
    "Peugeot 206": {"image": "images/206.jpg", "price": 3349, "category": "Voitures"},
    "BMW E-tron GT": {"image": "images/etron.webp", "price": 128250, "category": "Voitures"},
    "Bugatti Chiron": {"image": "images/chiron.jpg", "price": 3200000, "category": "Voitures"},
    "Ariel Atom": {"image": "images/ariel.jpg", "price": 79000, "category": "Voitures"},
    "Ford Mustang": {"image": "images/mustang.jpg", "price": 59300, "category": "Voitures"},
    "koenigsegg regera": {"image": "images/regera.webp", "price": 3430000, "category": "Voitures"},
    "Koenigsegg Agera": {"image": "images/agera.jpg", "price": 3100000, "category": "Voitures"},
    "Audi RSQ8": {"image": "images/rsq8.jpg", "price": 191550, "category": "Voitures"},
    "Bentley Continental GT": {"image": "images/bentley.jpg", "price": 293748, "category": "Voitures"},
    "Audi RS3": {"image": "images/rs3.jpg", "price": 75000, "category": "Voitures"},
    "Opel Astra": {"image": "images/astra.webp", "price": 29000, "category": "Voitures"},
    "Reliant Supervan III": {"image": "images/reliant.jpg", "price": 20000, "category": "Voitures"},
    "Pagani Zonda R": {"image": "images/zonda.jpg", "price": 1746000, "category": "Voitures"},
    "Audi M4": {"image": "images/m4.jpg", "price": 123000, "category": "Voitures"},
    "Alpine A110": {"image": "images/a110.jpg", "price": 65000, "category": "Voitures"},
    "Lamborghini Urus": {"image": "images/urus.webp", "price": 215000, "category": "Voitures"},
    "Ford GT": {"image": "images/gt.jpg", "price": 400000, "category": "Voitures"},
    "Ferrari F12 Berlineta ": {"image": "images/f12.jpg", "price": 271786, "category": "Voitures"},
    "Ferrari 458 Spécial": {"image": "images/458spe.jpg", "price": 415000, "category": "Voitures"},
    "Ferrari FXX K": {"image": "images/fxxk.jpg", "price": 2400000, "category": "Voitures"},
    "Mercedes-Benz E 220": {"image": "images/220.png", "price": 94000, "category": "Voitures"},
    "Ferrari 488 GB": {"image": "images/488.webp", "price": 235000, "category": "Voitures"},
    "Rolls-Royce Droptail": {"image": "images/rr.webp", "price": 23000000, "category": "Voitures"},
    "BMW IX M60": {"image": "images/ix.webp", "price": 100000, "category": "Voitures"},
    "BMW série 5 G30 ": {"image": "images/g30.jpg", "price": 58000, "category": "Voitures"},
    "Audi A4": {"image": "images/a4.jpeg", "price": 58000, "category": "Voitures"},
    "Lexus ES": {"image": "images/lexus.webp", "price": 60200, "category": "Voitures"},
    "BMW I8 Tunning": {"image": "images/tuning.jpg", "price": 165000, "category": "Voitures"},
    "Lamborghini Avantador": {"image": "images/lambo.png", "price": 380000, "category": "Voitures"},
    "Aston Martin Valkyrie": {"image": "images/valk.jpg", "price": 2500000, "category": "Voitures"},
    "Aston Martin Valhalla": {"image": "images/Your-Valhalla.jpeg", "price": 860000, "category": "Voitures"},
    "Aston Martin Vanquish": {"image": "images/vanq.jpeg", "price": 400000, "category": "Voitures"},
    "Aston Martin Vantage": {"image": "images/vantage.jpeg", "price": 260000, "category": "Voitures"},
    "Mclaren 750s": {"image": "images/750s.png", "price": 280000, "category": "Voitures"},
    "Mclaren P1": {"image": "images/mclaren.webp", "price": 1500000, "category": "Voitures"},
    "Mclaren Senna": {"image": "images/sena.jpg", "price": 930000, "category": "Voitures"},
    "Mclaren 720s": {"image": "images/720.jpg", "price": 250000, "category": "Voitures"},
    "Ferrari 488 Chalenge Evo": {"image": "images/488cha.jpg", "price": 260000, "category": "Voitures"},
    "Audi RS7 Sportback": {"image": "images/rs7.jpg", "price": 157000, "category": "Voitures"},
    "Mercedes-AMG ONE": {"image": "images/amgone.webp", "price": 2275000, "category": "Voitures"},
    "SP Automotive Chaos": {"image": "images/chaos.jpg", "price": 5500000, "category": "Voitures"},
    "Aspark Owl": {"image": "images/owl.jpg", "price": 2500000, "category": "Voitures"},
    "Czinger 21C": {"image": "images/21c.jpg", "price": 2600000, "category": "Voitures"},
    "Muray T.50": {"image": "images/t50.jpg", "price": 2000000, "category": "Voitures"},
    "Brabus Rocket 1000": {"image": "images/brabus.PNG", "price": 560000, "category": "Voitures"},
    "Porsche 918 Spyder": {"image": "images/Porsche-spyder-918.jpg", "price": 775000, "category": "Voitures"},
    "KMT Xbow GT-XR": {"image": "images/kmt.jpg", "price": 280000, "category": "Voitures"},
    "Lamborghini sian FKP57": {"image": "images/sian.jpg", "price": 3700000, "category": "Voitures"},
    "Maserati MC20": {"image": "images/maserati.png", "price": 280000, "category": "Voitures"},
    "Lamborghini Huracan": {"image": "images/uracan.png", "price": 250000, "category": "Voitures"},
    "Ferrari F80": {"image": "images/fefe.png", "price": 3600000, "category": "Voitures"},
    "Zenvo TSR-S": {"image": "images/zenvo.jpg", "price": 1450000, "category": "Voitures"},
    "koenigsegg Jesko": {"image": "images/jesko.jpg", "price": 2500000, "category": "Voitures"},
    "Hennessey Venom F5": {"image": "images/venom.jpg", "price": 2400000, "category": "Voitures"},
    "Ferrari SF90": {"image": "images/sf90.jpg", "price": 440000, "category": "Voitures"},
    "Porsche Taycan": {"image": "images/taycan.jpg", "price": 106000, "category": "Voitures"},
    "Porsche Panamera": {"image": "images/panamera.jpg", "price": 119000, "category": "Voitures"},
    "BMW M5": {"image": "images/m5.jpg", "price": 160000, "category": "Voitures"},
    "Lamborghini Centanario": {"image": "images/cen.webp", "price": 2100000, "category": "Voitures"},
    "Ferrari F12TDF": {"image": "images/f12tdf.jpg", "price": 500000, "category": "Voitures"},
    "Mercedes AVTR": {"image": "images/avtr.jpg", "price": 1250000, "category": "Voitures"},
    "BMW i4": {"image": "images/i4.jpg", "price": 70000, "category": "Voitures"},
    "Bugatti Tourbillon": {"image": "images/tou.webp", "price": 3800000, "category": "Voitures"},
    "Bugatti Mistral": {"image": "images/mis.jpg", "price": 5000000, "category": "Voitures"},
    "Daytona SP3": {"image": "images/day.jpg", "price": 1968000, "category": "Voitures"},
    "GTR R35": {"image": "images/gtr.jpg", "price": 70000, "category": "Voitures"},
    "Bugatti Centodieci": {"image": "images/cen.jpg", "price": 8000000, "category": "Voitures"},
    "Bugatti La Voiture Noire": {"image": "images/lvn.jpg", "price": 15900000, "category": "Voitures"},
    "Audi R8": {"image": "images/r8.jpg", "price": 260000, "category": "Voitures"},
    "Audi R8 GT2": {"image": "images/r8v.webp", "price": 300000, "category": "Voitures"},
    "Formule 1 Mercedes": {"image": "images/f1.jpeg", "price": 1000000, "category": "Voitures"},
    "Rimac Nevera": {"image": "images/Rimac Nevera.webp", "price": 2000000, "category": "Voitures"},
    "McLaren Speedtail": {"image": "images/mc.jpg", "price": 2100000, "category": "Voitures"},
    "Ferrari Roma": {"image": "images/roma.jpg", "price": 250000, "category": "Voitures"},
    "Audi ABT R8 XGT": {"image": "images/abt.jpg", "price": 600000, "category": "Voitures"},
    "Ferrari 488 Pista": {"image": "images/pista.jpg", "price": 410000, "category": "Voitures"},
    "Apollo INTENSA EMOZIONE": {"image": "images/apolloin.jpg", "price": 1050000, "category": "Voitures"},
    "Aston Martin Vulcan": {"image": "images/as.jpg", "price": 1500000, "category": "Voitures"},
    "Chevrolet Camaro GT": {"image": "images/camaro.png", "price": 50000, "category": "Voitures"},
    "Lamborggini Gallardo": {"image": "images/gallardo.jpg", "price": 210000, "category": "Voitures"},
    "Lamborghini Sesto": {"image": "images/sesto.jpg", "price": 2700000, "category": "Voitures"},
    "Lamborghini Murcielago": {"image": "images/murcielago.jpg", "price": 180000, "category": "Voitures"},
    "Mercedes-Benz SLR McLaren": {"image": "images/slr.webp", "price": 300000, "category": "Voitures"},

    "Onyx F 25": {"image": "images/onyx2.jpg", "price": 400000, "category": "Voitures"},
    "Onyx Black car": {"image": "images/onyx3.jpg", "price": 1200000, "category": "Voitures"},
    "Onyx F 20": {"image": "images/onyx.jpg", "price": 850000, "category": "Voitures"},
    "Onyx OV 1": {"image": "images/fefe.jpg", "price": 250000, "category": "Voitures"},
    "Onyx Z2": {"image": "images/onyx4.jpg", "price": 550000, "category": "Voitures"},
    "Onyx Z1": {"image": "images/ferrari z.png", "price": 600000, "category": "Voitures"},
    "Onyx M1": {"image": "images/Onyx6.jpg", "price": 550000, "category": "Voitures"},
    "Onyx OV 2": {"image": "images/Onyx5.jpg", "price": 600000, "category": "Voitures"},
    
    "A380 Fly Emirates": {"image": "images/a380.jpg", "price": 445000000, "category": "avions"},
    "A350 Fly Emirates": {"image": "images/a350.webp", "price": 366000000, "category": "avions"},
    "B777 Qatar Airways": {"image": "images/777.jpg", "price": 442000000, "category": "avions"},
    "Dassault Rafale": {"image": "images/rafale.webp", "price": 78000000, "category": "avions"},
    "F-22 Raptor": {"image": "images/f22.jpg", "price": 316000000, "category": "avions"},
    "Cesna 172": {"image": "images/172.jpg", "price": 400000, "category": "avions"},
     
    "AirFrance": {"image": "images/airfrance.jpg", "price": 2700000000, "category": "Entreprises"},
    "Paris SG": {"image": "images/psg.png", "price": 4200000000, "category": "Entreprises"},
    "Lutti": {"image": "images/lutti.png", "price": 175000000, "category": "Entreprises"},
    "Salon de coiffure": {"image": "images/coif.png", "price": 25000, "category": "Entreprises"},
    "La Bonne Fournée": {"image": "images/lbn.png", "price": 350000, "category": "Entreprises"},

    "Maillot FC Parrot domicile": {"image": "images/parrotdom.png", "price": 120, "category": "Maillots"},
    "Maillot FC Parrot extérieur": {"image": "images/parrotext.png", "price": 120, "category": "Maillots"},
    "Maillot FC Parrot third": {"image": "images/parrotthi.png", "price": 120, "category": "Maillots"},
    "Maillot FC Parrot fourth": {"image": "images/parrotfour.png", "price": 120, "category": "Maillots"},
    "Maillot FC Parrot spécial": {"image": "images/parotspe.png", "price": 120, "category": "Maillots"},
    "Maillot FC Calamar domicile": {"image": "images/calamdom.png", "price": 120, "category": "Maillots"},
    "Maillot FC Calamar extérieur": {"image": "images/calamext.png", "price": 120, "category": "Maillots"},
    "Maillot FC Calamar third": {"image": "images/calamthi.png", "price": 120, "category": "Maillots"},
    "Maillot FC Calamar fourth": {"image": "images/calamfour.png", "price": 120, "category": "Maillots"},
    "Maillot SP Axolotl domicile": {"image": "images/axodom.jpg", "price": 120, "category": "Maillots"},
    "Maillot SP Axolotl extérieur": {"image": "images/axoext.jpg", "price": 120, "category": "Maillots"},
    "Maillot SP Axolotl third": {"image": "images/axothi.jpg", "price": 120, "category": "Maillots"},
    "Maillot Inter Wolf domicile": {"image": "images/wolfdom.png", "price": 120, "category": "Maillots"},
    "Maillot Inter Wolf extérieur": {"image": "images/wolfext.png", "price": 120, "category": "Maillots"},
    "Maillot Inter Wolf third": {"image": "images/wolfthi.png", "price": 120, "category": "Maillots"},
    "Maillot Allemagne domicile": {"image": "images/allemext.png", "price": 120, "category": "Maillots"},
    "Maillot Allemagne extérieur": {"image": "images/allemdom.png", "price": 120, "category": "Maillots"},
    "Maillot Brésil domicile": {"image": "images/bredom.png", "price": 120, "category": "Maillots"},
    "Maillot Brésil extérieur": {"image": "images/breext.png", "price": 120, "category": "Maillots"},
    "Maillot FC Dauphin domicile": {"image": "images/fradom.png", "price": 120, "category": "Maillots"},
    "Maillot FC Dauphin extérieur": {"image": "images/fraext.png", "price": 120, "category": "Maillots"},
    "Maillot Tigre FC Domicile": {"image": "images/tigredom.png", "price": 120, "category": "Maillots"},
    "Maillot Tigre FC exterieur": {"image": "images/tigreext.png", "price": 120, "category": "Maillots"},
    "Maillot Tigre FC third": {"image": "images/tigrethi.png", "price": 120, "category": "Maillots"},
    "Maillot FC Pnj Domicile": {"image": "images/pnjdom.png", "price": 120, "category": "Maillots"},
    "Maillot FC Pnj extérieur": {"image": "images/pnjext.png", "price": 120, "category": "Maillots"},
    "Maillot FC Pnj third": {"image": "images/pnjthi.png", "price": 120, "category": "Maillots"},
    "Maillot FC Paris Domicile": {"image": "images/pardom.png", "price": 120, "category": "Maillots"},
    "Maillot FC Paris exterieur": {"image": "images/parext.png", "price": 120, "category": "Maillots"},
    "Maillot FC Paris third": {"image": "images/parthi.png", "price": 120, "category": "Maillots"},
    "Maillot Ghast United Domicile": {"image": "images/gast.png", "price": 120, "category": "Maillots"},
    "Maillot Ghast United exterieur": {"image": "images/gastext.png", "price": 120, "category": "Maillots"},
    "Maillot Ghast United third": {"image": "images/gastthi.png", "price": 120, "category": "Maillots"}
}


nb_voitures = sum(1 for a in annonces.values() if a["category"] == "Voitures")
print("nb voiture",nb_voitures)



def format_price(price):
    # Convertir le prix en chaîne de caractères
    price_str = str(price)
    
    # Si le prix est supérieur ou égal à 1000, appliquer le format
    if len(price_str) > 3:
        # Inverser la chaîne pour appliquer le format des milliers de droite à gauche
        reversed_price_str = price_str[::-1]
        # Diviser la chaîne en segments de 3 chiffres
        formatted_price_str = " ".join([reversed_price_str[i:i+3] for i in range(0, len(reversed_price_str), 3)])
        # Réinverser la chaîne et supprimer les espaces excédentaires
        return formatted_price_str[::-1].strip()
    else:
        return price_str  # Si le prix est inférieur ou égal à 999, on ne le formate pas




# Définition des cartes et des raretés
cardsgame = {
    "Tavinho": {"image": "images/tavinho.jpg", "rarity": "commun", "chance": 90, "attack": 84, "defense": 10},
    "Ekkrare": {"image": "images/ekkrare.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 91},
    "Matteo Jr": {"image": "images/mateo.png", "rarity": "légendaire", "chance": 1, "attack": 89, "defense": 40},
    "Aaron": {"image": "images/aaron.jpg", "rarity": "légendaire", "chance": 1, "attack": 94, "defense": 40},
    "Apolskis Jr": {"image": "images/apolskis.jpg", "rarity": "légendaire", "chance": 1, "attack": 91, "defense": 40},
    "wea1": {"image": "images/wea1.jpg", "rarity": "mythique", "chance": 3, "attack": 80, "defense": 50},
    "Aaron Jr": {"image": "images/aaron_jr.jpg", "rarity": "épique", "chance": 8, "attack": 87, "defense": 30},
    "Nolan": {"image": "images/nolan.jpg", "rarity": "rare", "chance": 60, "attack": 84, "defense": 20},
    "Stony Jr": {"image": "images/stony_jr.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 30},
    "Thethe": {"image": "images/thethe.jpg", "rarity": "mythique", "chance": 3, "attack": 75, "defense": 65},
    "Sachluxk": {"image": "images/sachluxk.jpg", "rarity": "commun", "chance": 90, "attack": 84, "defense": 10},
    "Nezox": {"image": "images/nezox.jpg", "rarity": "mythique", "chance": 3, "attack": 85, "defense": 40},
    "Amau": {"image": "images/amau.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Diego": {"image": "images/diego.jpg", "rarity": "épique", "chance": 10, "attack": 60, "defense": 89},
    "Kopoti": {"image": "images/kopoti.jpg", "rarity": "épique", "chance": 10, "attack": 50, "defense": 85},
    "Icardi": {"image": "images/icardi.jpg", "rarity": "mythique", "chance": 3, "attack": 90, "defense": 40},
    "Diamond Doku": {"image": "images/diamond_doku.jpg", "rarity": "épique", "chance": 20, "attack": 84, "defense": 30},
    "Nathinio": {"image": "images/nathinio.jpg", "rarity": "mythique", "chance": 3, "attack": 89, "defense": 40},
    "B": {"image": "images/b.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 87},
    "Mex Jr": {"image": "images/mex_jr.jpg", "rarity": "épique", "chance": 10, "attack": 85, "defense": 30},
    "Johan": {"image": "images/johan.jpg", "rarity": "mythique", "chance": 3, "attack": 70, "defense": 70},
    "Felix Jr": {"image": "images/felix_jr.jpg", "rarity": "rare", "chance": 60, "attack": 84, "defense": 20},
    "Tima": {"image": "images/tima.jpg", "rarity": "mythique", "chance": 3, "attack": 50, "defense": 91},
    "The Unique R": {"image": "images/the_unique_r.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 91},
    "Camille Strider": {"image": "images/camille_strider.jpg", "rarity": "commun", "chance": 90, "attack": 82, "defense": 10},
    "RL9": {"image": "images/rl9.jpg", "rarity": "mythique", "chance": 3, "attack": 91, "defense": 40},
    "Amau jr": {"image": "images/amau_jr.jpg", "rarity": "épique", "chance": 10, "attack": 97, "defense": 37},
    "Cosmos": {"image": "images/cosmos.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 75},
    "Dufour": {"image": "images/dufour.png", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Hgame": {"image": "images/Hgame.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 94},
    "Liam": {"image": "images/liam.png", "rarity": "épique", "chance": 10, "attack": 70, "defense": 75},
    "Lumii": {"image": "images/lumii.png", "rarity": "épique", "chance": 10, "attack": 20, "defense": 86},
    "lumii jr": {"image": "images/lumii_jr.jpg", "rarity": "rare", "chance": 60, "attack": 74, "defense": 10},
    "Nono Mero": {"image": "images/nono_mero.jpg", "rarity": "mythique", "chance": 3, "attack": 88, "defense": 40},
    "Sade": {"image": "images/sade.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Slapy": {"image": "images/slapy.jpg", "rarity": "légendaire", "chance": 1, "attack": 92, "defense": 40},
    "trotali jr": {"image": "images/trotali_jr.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Alexandre": {"image": "images/alexandre.jpg", "rarity": "commun", "chance": 90, "attack": 30, "defense": 70},
    "Brc": {"image": "images/brc.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 20},
    "Catmau": {"image": "images/catmau.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Elekkrare_jr": {"image": "images/elekkrare_jr.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Esteban": {"image": "images/esteban.jpg", "rarity": "mythique", "chance": 3, "attack": 30, "defense": 92},
    "Flo jr": {"image": "images/flo_jr.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 80},
    "Forceclan": {"image": "images/forceclan.jpg", "rarity": "rare", "chance": 60, "attack": 70, "defense": 60},
    "Gabriel": {"image": "images/gabriel.jpg", "rarity": "commun", "chance": 90, "attack": 20, "defense": 60},
    "Gorgein": {"image": "images/gorgein.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 79},
    "Imot": {"image": "images/Imot.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 20},
    "Kai": {"image": "images/kai.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 20},
    "Kilyan": {"image": "images/kilyan.jpg", "rarity": "épique", "chance": 10, "attack": 90, "defense": 30},
    "Lloyd": {"image": "images/Lloyd.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Louka city": {"image": "images/louka_city.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 75},
    "Luka": {"image": "images/luka.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 85},
    "M-7": {"image": "images/m-7.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 30},
    "MonkeyDM": {"image": "images/monkeyDM.jpg", "rarity": "rare", "chance": 60, "attack": 0, "defense": 77},
    "MXT": {"image": "images/mxt.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    "Nika jr": {"image": "images/nika_jr.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Omerta": {"image": "images/omerta.jpg", "rarity": "commun", "chance": 90, "attack": 60, "defense": 50},
    "Polak": {"image": "images/polak.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 65},
    "Rayan": {"image": "images/rayan.jpg", "rarity": "épique", "chance": 10, "attack": 83, "defense": 30},
    "Rodri": {"image": "images/rodri.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 70},
    "Rodrygocelot": {"image": "images/rodrygocelot.jpg", "rarity": "commun", "chance": 90, "attack": 75, "defense": 10},
    "Ryan": {"image": "images/ryan.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 70},
    "Savinho": {"image": "images/savinho.jpg", "rarity": "commun", "chance": 90, "attack": 75, "defense": 10},
    "Spirit": {"image": "images/spirit.jpg", "rarity": "commun", "chance": 90, "attack": 30, "defense": 70},
    "Timeo": {"image": "images/timeo.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 82},
    "Valox": {"image": "images/valox.jpg", "rarity": "mythique", "chance": 3, "attack": 40, "defense": 86},
    "Zeerox": {"image": "images/zeerox.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "ZX Crakito": {"image": "images/zx_crakito.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "Loueye": {"image": "images/loureg.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    
    "Alexis Futur": {"image": "images/alexis.jpg", "rarity": "fu", "chance": 0, "attack": 89, "defense": 30},
    "Casinox Futur": {"image": "images/cas.jpg", "rarity": "fu", "chance": 0, "attack": 0, "defense": 90},
    "Hector Futur": {"image": "images/hec.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Pacho Futur": {"image": "images/pac.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 88},
    "Marius Futur": {"image": "images/mar1.jpg", "rarity": "fu", "chance": 0, "attack": 91, "defense": 30},
    "Mathis JR Futur": {"image": "images/mat.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Mbappé JR Futur": {"image": "images/mbap.jpg", "rarity": "fu", "chance": 0, "attack": 88, "defense": 40},
    "Tavinho Futur": {"image": "images/tav2.jpg", "rarity": "fu", "chance": 0, "attack": 93, "defense": 40},
    "Rodri Futur": {"image": "images/rodr.jpg", "rarity": "fu", "chance": 0, "attack": 92, "defense": 30},
    "WanHida Futur": {"image": "images/wan.jpg", "rarity": "fu", "chance": 0, "attack": 89, "defense": 30},
    "Yanis Futur": {"image": "images/yanos.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 87}
}

cards = {
    "Tavinho": {"image": "images/tavinho.jpg", "rarity": "commun", "chance": 90, "attack": 84, "defense": 10},
    "Ekkrare": {"image": "images/ekkrare.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 91},
    "Matteo Jr": {"image": "images/mateo.png", "rarity": "légendaire", "chance": 1, "attack": 89, "defense": 40},
    "Aaron": {"image": "images/aaron.jpg", "rarity": "légendaire", "chance": 1, "attack": 94, "defense": 40},
    "Apolskis Jr": {"image": "images/apolskis.jpg", "rarity": "légendaire", "chance": 1, "attack": 91, "defense": 40},
    "wea1": {"image": "images/wea1.jpg", "rarity": "mythique", "chance": 3, "attack": 80, "defense": 50},
    "Aaron Jr": {"image": "images/aaron_jr.jpg", "rarity": "épique", "chance": 8, "attack": 87, "defense": 30},
    "Nolan": {"image": "images/nolan.jpg", "rarity": "rare", "chance": 60, "attack": 84, "defense": 20},
    "Stony Jr": {"image": "images/stony_jr.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 30},
    "Thethe": {"image": "images/thethe.jpg", "rarity": "mythique", "chance": 3, "attack": 75, "defense": 65},
    "Sachluxk": {"image": "images/sachluxk.jpg", "rarity": "commun", "chance": 90, "attack": 84, "defense": 10},
    "Nezox": {"image": "images/nezox.jpg", "rarity": "mythique", "chance": 3, "attack": 85, "defense": 40},
    "Amau": {"image": "images/amau.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Diego": {"image": "images/diego.jpg", "rarity": "épique", "chance": 10, "attack": 60, "defense": 89},
    "Kopoti": {"image": "images/kopoti.jpg", "rarity": "épique", "chance": 10, "attack": 50, "defense": 85},
    "Icardi": {"image": "images/icardi.jpg", "rarity": "mythique", "chance": 3, "attack": 90, "defense": 40},
    "Diamond Doku": {"image": "images/diamond_doku.jpg", "rarity": "épique", "chance": 20, "attack": 84, "defense": 30},
    "Nathinio": {"image": "images/nathinio.jpg", "rarity": "mythique", "chance": 3, "attack": 89, "defense": 40},
    "B": {"image": "images/b.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 87},
    "Mex Jr": {"image": "images/mex_jr.jpg", "rarity": "épique", "chance": 10, "attack": 85, "defense": 30},
    "Johan": {"image": "images/johan.jpg", "rarity": "mythique", "chance": 3, "attack": 70, "defense": 70},
    "Felix Jr": {"image": "images/felix_jr.jpg", "rarity": "rare", "chance": 60, "attack": 84, "defense": 20},
    "Tima": {"image": "images/tima.jpg", "rarity": "mythique", "chance": 3, "attack": 50, "defense": 91},
    "The Unique R": {"image": "images/the_unique_r.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 91},
    "Camille Strider": {"image": "images/camille_strider.jpg", "rarity": "commun", "chance": 90, "attack": 82, "defense": 10},
    "RL9": {"image": "images/rl9.jpg", "rarity": "mythique", "chance": 3, "attack": 91, "defense": 40},
    "Amau jr": {"image": "images/amau_jr.jpg", "rarity": "épique", "chance": 10, "attack": 97, "defense": 37},
    "Cosmos": {"image": "images/cosmos.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 75},
    "Dufour": {"image": "images/dufour.png", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Hgame": {"image": "images/Hgame.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 94},
    "Liam": {"image": "images/liam.png", "rarity": "épique", "chance": 10, "attack": 70, "defense": 75},
    "Lumii": {"image": "images/lumii.png", "rarity": "épique", "chance": 10, "attack": 20, "defense": 86},
    "lumii jr": {"image": "images/lumii_jr.jpg", "rarity": "rare", "chance": 60, "attack": 74, "defense": 10},
    "Nono Mero": {"image": "images/nono_mero.jpg", "rarity": "mythique", "chance": 3, "attack": 88, "defense": 40},
    "Sade": {"image": "images/sade.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Slapy": {"image": "images/slapy.jpg", "rarity": "légendaire", "chance": 1, "attack": 92, "defense": 40},
    "trotali jr": {"image": "images/trotali_jr.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Alexandre": {"image": "images/alexandre.jpg", "rarity": "commun", "chance": 90, "attack": 30, "defense": 70},
    "Brc": {"image": "images/brc.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 20},
    "Catmau": {"image": "images/catmau.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Elekkrare_jr": {"image": "images/elekkrare_jr.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Esteban": {"image": "images/esteban.jpg", "rarity": "mythique", "chance": 3, "attack": 30, "defense": 92},
    "Flo jr": {"image": "images/flo_jr.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 80},
    "Forceclan": {"image": "images/forceclan.jpg", "rarity": "rare", "chance": 60, "attack": 70, "defense": 60},
    "Gabriel": {"image": "images/gabriel.jpg", "rarity": "commun", "chance": 90, "attack": 20, "defense": 60},
    "Gorgein": {"image": "images/gorgein.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 79},
    "Imot": {"image": "images/Imot.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 20},
    "Kai": {"image": "images/kai.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 20},
    "Kilyan": {"image": "images/kilyan.jpg", "rarity": "épique", "chance": 10, "attack": 90, "defense": 30},
    "Lloyd": {"image": "images/Lloyd.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Louka city": {"image": "images/louka_city.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 75},
    "Luka": {"image": "images/luka.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 85},
    "M-7": {"image": "images/m-7.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 30},
    "MonkeyDM": {"image": "images/monkeyDM.jpg", "rarity": "rare", "chance": 60, "attack": 0, "defense": 77},
    "MXT": {"image": "images/mxt.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    "Nika jr": {"image": "images/nika_jr.jpg", "rarity": "rare", "chance": 60, "attack": 80, "defense": 20},
    "Omerta": {"image": "images/omerta.jpg", "rarity": "commun", "chance": 90, "attack": 60, "defense": 50},
    "Polak": {"image": "images/polak.jpg", "rarity": "commun", "chance": 90, "attack": 0, "defense": 65},
    "Rayan": {"image": "images/rayan.jpg", "rarity": "épique", "chance": 10, "attack": 83, "defense": 30},
    "Rodri": {"image": "images/rodri.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 70},
    "Rodrygocelot": {"image": "images/rodrygocelot.jpg", "rarity": "commun", "chance": 90, "attack": 75, "defense": 10},
    "Ryan": {"image": "images/ryan.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 70},
    "Savinho": {"image": "images/savinho.jpg", "rarity": "commun", "chance": 90, "attack": 75, "defense": 10},
    "Spirit": {"image": "images/spirit.jpg", "rarity": "commun", "chance": 90, "attack": 30, "defense": 70},
    "Timeo": {"image": "images/timeo.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 82},
    "Valox": {"image": "images/valox.jpg", "rarity": "mythique", "chance": 3, "attack": 40, "defense": 86},
    "Zeerox": {"image": "images/zeerox.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "ZX Crakito": {"image": "images/zx_crakito.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "Loueye": {"image": "images/loureg.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    
    "Sebrice MHSC EAC": {"image": "images/1.jpg", "rarity": "EAC", "chance": 0, "attack": 92, "defense": 40},
    "Trotali JR EAC": {"image": "images/8.jpg", "rarity": "EAC", "chance": 0, "attack": 91, "defense": 25},
    "Mattéo JR EAC": {"image": "images/7.jpg", "rarity": "EAC", "chance": 0, "attack": 97, "defense": 30},
    "Gab EAC": {"image": "images/3.jpg", "rarity": "EAC", "chance": 0, "attack": 96, "defense": 20},
    "Léveillé EAC": {"image": "images/5.jpg", "rarity": "EAC", "chance": 0, "attack": 35, "defense": 95},
    "Louis29 EAC": {"image": "images/9.jpg", "rarity": "EAC", "chance": 0, "attack": 89, "defense": 89},
    "Tima EAC": {"image": "images/4.jpg", "rarity": "EAC", "chance": 2, "attack": 30, "defense": 93},
    "Nezox EAC": {"image": "images/2.jpg", "rarity": "EAC", "chance": 2, "attack": 30, "defense": 95},
    "Esteban EAC": {"image": "images/6.jpg", "rarity": "EAC", "chance": 2, "attack": 40, "defense": 94},
    "Hgame EAC": {"image": "images/10.jpg", "rarity": "EAC", "chance": 2, "attack": 0, "defense": 99},
    "Slapy EAC": {"image": "images/11.jpg", "rarity": "EAC", "chance": 0, "attack": 98, "defense": 65},
    
    "Louis29 BO": {"image": "images/loubo.jpg", "rarity": "BO", "chance": 0, "attack": 94, "defense": 94},
    "Mattéo JR BO": {"image": "images/matbo.jpg", "rarity": "BO", "chance": 0, "attack": 99, "defense": 40},
    "Aaron BO": {"image": "images/aarbo.jpg", "rarity": "BO", "chance": 0, "attack": 101, "defense": 40},
    "Slapy BO": {"image": "images/slabo.jpg", "rarity": "BO", "chance": 0, "attack": 100, "defense": 40},
    "Slapy BO top 1": {"image": "images/slao.jpg", "rarity": "BO", "chance": 0, "attack": 105, "defense": 40},
    "Gab BO top 2": {"image": "images/gabo.jpg", "rarity": "BO", "chance": 0, "attack": 104, "defense": 40},
    "Rl9 BO top 3": {"image": "images/rl9o.jpg", "rarity": "BO", "chance": 0, "attack": 102, "defense": 40},
    "Nezox JR BO top 4": {"image": "images/nezo.jpg", "rarity": "BO", "chance": 0, "attack": 101, "defense": 40},
    "Salmane BO top 5": {"image": "images/salo.jpg", "rarity": "BO", "chance": 0, "attack": 99, "defense": 40},
    "Hgame Best GK": {"image": "images/hgag.jpg", "rarity": "BO", "chance": 0, "attack": 0, "defense": 113},
    
    "Fuzety ICON Prime": {"image": "images/fuzety.jpg", "rarity": "ICON", "chance": 0, "attack": 115, "defense": 50},
    "Fuzety ICON Mid": {"image": "images/fuzety2.jpg", "rarity": "ICON", "chance": 0, "attack": 110, "defense": 45},
    "Fuzety ICON End": {"image": "images/fuzety3.jpg", "rarity": "ICON", "chance": 0, "attack": 100, "defense": 40},
    "Fuzety ICON": {"image": "images/fuz.jpg", "rarity": "ICON", "chance": 0, "attack": 107, "defense": 40},
    "Nezox ICON": {"image": "images/nez.jpg", "rarity": "ICON", "chance": 0, "attack": 40, "defense": 101},
    "Mandancraft ICON": {"image": "images/man.jpg", "rarity": "ICON", "chance": 0, "attack": 0, "defense": 106},
    "Osico ICON": {"image": "images/osi.jpg", "rarity": "ICON", "chance": 0, "attack": 94, "defense": 81},
    "Barcola rtist ICON": {"image": "images/bar.jpg", "rarity": "ICON", "chance": 0, "attack": 98, "defense": 40},
    
    "Nezox JR Crack": {"image": "images/nezcr.png", "rarity": "cr", "chance": 90, "attack": 103, "defense": 40},
    "Diego Crack": {"image": "images/diecr.jpg", "rarity": "cr", "chance": 0, "attack": 40, "defense": 100},
    "Icardi Crack": {"image": "images/icacr.png", "rarity": "cr", "chance": 0, "attack": 95, "defense": 40},
    "Nathinio Crack": {"image": "images/natcr.jpg", "rarity": "cr", "chance": 0, "attack": 99, "defense": 40},
    "Skerry JR Crack": {"image": "images/skecr.png", "rarity": "cr", "chance": 0, "attack": 98, "defense": 40},
    "Rl9 Crack": {"image": "images/rl9cr.jpg", "rarity": "cr", "chance": 0, "attack": 100, "defense": 40},
    "Nono Mero Crack": {"image": "images/noncr.png", "rarity": "cr", "chance": 0, "attack": 101, "defense": 40},
    "Elekkrare Crack": {"image": "images/elecr.png", "rarity": "cr", "chance": 0, "attack": 30, "defense": 99},
    "Stony JR Crack": {"image": "images/stocr.png", "rarity": "cr", "chance": 0, "attack": 95, "defense": 30},
    "Apolskis JR Crack": {"image": "images/apocr.png", "rarity": "cr", "chance": 0, "attack": 106, "defense": 40},
    "Cold Creeper Crack": {"image": "images/colcr.png", "rarity": "cr", "chance": 0, "attack": 89, "defense": 91},
    "Kopoti Crack": {"image": "images/kopcr.png", "rarity": "cr", "chance": 0, "attack": 40, "defense": 101},
    
    "Alexis Futur": {"image": "images/alexis.jpg", "rarity": "fu", "chance": 0, "attack": 89, "defense": 30},
    "Casinox Futur": {"image": "images/cas.jpg", "rarity": "fu", "chance": 0, "attack": 0, "defense": 90},
    "Hector Futur": {"image": "images/hec.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Pacho Futur": {"image": "images/pac.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 88},
    "Marius Futur": {"image": "images/mar1.jpg", "rarity": "fu", "chance": 0, "attack": 91, "defense": 30},
    "Mathis JR Futur": {"image": "images/mat.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Mbappé JR Futur": {"image": "images/mbap.jpg", "rarity": "fu", "chance": 0, "attack": 88, "defense": 40},
    "Tavinho Futur": {"image": "images/tav2.jpg", "rarity": "fu", "chance": 0, "attack": 93, "defense": 40},
    "Rodri Futur": {"image": "images/rodr.jpg", "rarity": "fu", "chance": 0, "attack": 92, "defense": 30},
    "WanHida Futur": {"image": "images/wan.jpg", "rarity": "fu", "chance": 0, "attack": 89, "defense": 30},
    "Yanis Futur": {"image": "images/yanos.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 87},
    
    "Alexis flower": {"image": "images/ale.jpg", "rarity": "fl", "chance": 0, "attack": 89, "defense": 30},
    "Lumii flower": {"image": "images/lum.jpg", "rarity": "fl", "chance": 0, "attack": 0, "defense": 90},
    "Marius flower": {"image": "images/mar.jpg", "rarity": "fl", "chance": 0, "attack": 87, "defense": 30},
    "MXT Flower": {"image": "images/mxt1.jpg", "rarity": "fl", "chance": 0, "attack": 30, "defense": 88},
    "Nika Flower": {"image": "images/nik.jpg", "rarity": "fl", "chance": 0, "attack": 91, "defense": 30},
    "Nolan Flower": {"image": "images/nol.jpg", "rarity": "fl", "chance": 0, "attack": 87, "defense": 30},
    "Thethe Flower": {"image": "images/thet.jpg", "rarity": "fl", "chance": 0, "attack": 88, "defense": 40},
    "Wea1 Flower": {"image": "images/wea.jpg", "rarity": "fl", "chance": 0, "attack": 93, "defense": 40},
    "Yao Flower": {"image": "images/yao.jpg", "rarity": "fl", "chance": 0, "attack": 92, "defense": 30},
    "M10 Flower": {"image": "images/m10.jpg", "rarity": "fl", "chance": 0, "attack": 89, "defense": 30},
    "Loueye Flower": {"image": "images/lou.jpg", "rarity": "fl", "chance": 0, "attack": 30, "defense": 87},
    
    "Amau Vision": {"image": "images/ama.jpg", "rarity": "vi", "chance": 0, "attack": 92, "defense": 30},
    "Eva vision": {"image": "images/eva.jpg", "rarity": "vi", "chance": 0, "attack": 80, "defense": 60},
    "Mbappé JR vision": {"image": "images/mba.jpg", "rarity": "vi", "chance": 0, "attack": 86, "defense": 30},
    "Rodri vision": {"image": "images/rod.jpg", "rarity": "vi", "chance": 0, "attack": 93, "defense": 30},
    "Tavinho vision": {"image": "images/tav.jpg", "rarity": "vi", "chance": 0, "attack": 93, "defense": 30},
    "The Unique R vision": {"image": "images/the.jpg", "rarity": "vi", "chance": 0, "attack": 0, "defense": 95},
    "Under Doué vision": {"image": "images/und.jpg", "rarity": "vi", "chance": 0, "attack": 93, "defense": 40},
    "Liam vision": {"image": "images/liam.jpg", "rarity": "vi", "chance": 0, "attack": 80, "defense": 70},
    "Trotali JR vision": {"image": "images/cb.jpg", "rarity": "vi", "chance": 0, "attack": 94, "defense": 40},
    "M10 vision": {"image": "images/tro.jpg", "rarity": "vi", "chance": 0, "attack": 91, "defense": 30},
    "Mex JR vision": {"image": "images/mex.jpg", "rarity": "vi", "chance": 0, "attack": 86, "defense": 30},
    
    "Hgame TOTY": {"image": "images/hgat.jpg", "rarity": "TOTY", "chance": 0, "attack": 0, "defense": 111},
    "Ronaldo TOTY": {"image": "images/ront.jpg", "rarity": "TOTY", "chance": 0, "attack": 40, "defense": 103},
    "Esteban TOTY": {"image": "images/estt.jpg", "rarity": "TOTY", "chance": 0, "attack": 30, "defense": 107},
    "Léveillé TOTY": {"image": "images/levt.jpg", "rarity": "TOTY", "chance": 0, "attack": 30, "defense": 108},
    "Tima TOTY": {"image": "images/timt.jpg", "rarity": "TOTY", "chance": 0, "attack": 40, "defense": 104},
    "Louis29 TOTY": {"image": "images/lout.jpg", "rarity": "TOTY", "chance": 0, "attack": 98, "defense": 95},
    "Nathinio TOTY": {"image": "images/natt.jpg", "rarity": "TOTY", "chance": 0, "attack": 99, "defense": 90},
    "Amau TOTY": {"image": "images/amat.jpg", "rarity": "TOTY", "chance": 0, "attack": 107, "defense": 30},
    "Slapy TOTY": {"image": "images/slat.jpg", "rarity": "TOTY", "chance": 0, "attack": 112, "defense": 40},
    "Aaron TOTY": {"image": "images/aart.jpg", "rarity": "TOTY", "chance": 0, "attack": 109, "defense": 30},
    "Mattéo JR TOTY": {"image": "images/matt.jpg", "rarity": "TOTY", "chance": 0, "attack": 106, "defense": 30},
    "Rl9 TOTY": {"image": "images/rl9t.jpg", "rarity": "TOTY", "chance": 0, "attack": 106, "defense": 30},
    
    "Nezox JR Honorable": {"image": "images/nezt.jpg", "rarity": "TOTY", "chance": 0, "attack": 101, "defense": 30},
    "Icardi Honorable": {"image": "images/icat.png", "rarity": "TOTY", "chance": 0, "attack": 98, "defense": 30},
    "Kopoti Honorable": {"image": "images/kopt.png", "rarity": "TOTY", "chance": 0, "attack": 40, "defense": 97},
    "Apolskis JR Honorable": {"image": "images/apot.png", "rarity": "TOTY", "chance": 0, "attack": 101, "defense": 30},
    "Wea1 Honorable": {"image": "images/wea1t.png", "rarity": "TOTY", "chance": 0, "attack": 99, "defense": 30},
    "Gab Honorable": {"image": "images/gabt.png", "rarity": "TOTY", "chance": 0, "attack": 102, "defense": 30},
    "Elekkrare Honorable": {"image": "images/elet.png", "rarity": "TOTY", "chance": 0, "attack": 30, "defense": 100},
    "Skerry JR Honorable": {"image": "images/sket.png", "rarity": "TOTY", "chance": 0, "attack": 99, "defense": 30},
    "Cold Creeper Honorable": {"image": "images/colt.png", "rarity": "TOTY", "chance": 0, "attack": 92, "defense": 87},
    "SebriceMHSC Honorable": {"image": "images/sebt.png", "rarity": "TOTY", "chance": 0, "attack": 98, "defense": 30},
    "Cold Bee Honorable": {"image": "images/coltb.png", "rarity": "TOTY", "chance": 0, "attack": 97, "defense": 30},
}


cardscol = {
    "Matteo Jr": {"image": "images/mateo.png", "rarity": "légendaire", "chance": 1, "attack": 89, "defense": 40},
    "Aaron": {"image": "images/aaron.jpg", "rarity": "légendaire", "chance": 1, "attack": 94, "defense": 40},
    "Apolskis Jr": {"image": "images/apolskis.jpg", "rarity": "légendaire", "chance": 1, "attack": 91, "defense": 40},
    "The Unique R": {"image": "images/the_unique_r.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 91},
    "Hgame": {"image": "images/Hgame.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 94},
    "Slapy": {"image": "images/slapy.jpg", "rarity": "légendaire", "chance": 1, "attack": 92, "defense": 40},
    
    "Sebrice MHSC EAC": {"image": "images/1.jpg", "rarity": "EAC", "chance": 1, "attack": 92, "defense": 40},
    "Trotali JR EAC": {"image": "images/8.jpg", "rarity": "EAC", "chance": 1, "attack": 91, "defense": 25},
    "Mattéo JR EAC": {"image": "images/7.jpg", "rarity": "EAC", "chance": 1, "attack": 97, "defense": 30},
    "Gab EAC": {"image": "images/3.jpg", "rarity": "EAC", "chance": 1, "attack": 96, "defense": 20},
    "Léveillé EAC": {"image": "images/5.jpg", "rarity": "EAC", "chance": 1, "attack": 35, "defense": 95},
    "Louis29 EAC": {"image": "images/9.jpg", "rarity": "EAC", "chance": 1, "attack": 89, "defense": 89},
    "Tima EAC": {"image": "images/4.jpg", "rarity": "EAC", "chance": 2, "attack": 30, "defense": 93},
    "Nezox EAC": {"image": "images/2.jpg", "rarity": "EAC", "chance": 2, "attack": 30, "defense": 95},
    "Esteban EAC": {"image": "images/6.jpg", "rarity": "EAC", "chance": 2, "attack": 40, "defense": 94},
    "Hgame EAC": {"image": "images/10.jpg", "rarity": "EAC", "chance": 2, "attack": 0, "defense": 99},
    "Slapy EAC": {"image": "images/11.jpg", "rarity": "EAC", "chance": 1, "attack": 98, "defense": 65},
    
    "Louis29 BO": {"image": "images/loubo.jpg", "rarity": "BO", "chance": 0, "attack": 94, "defense": 94},
    "Mattéo JR BO": {"image": "images/matbo.jpg", "rarity": "BO", "chance": 1, "attack": 99, "defense": 40},
    "Aaron BO": {"image": "images/aarbo.jpg", "rarity": "BO", "chance": 0, "attack": 101, "defense": 40},
    "Slapy BO": {"image": "images/slabo.jpg", "rarity": "BO", "chance": 0, "attack": 100, "defense": 40},
    "Slapy BO top 1": {"image": "images/slao.jpg", "rarity": "BO", "chance": 0, "attack": 105, "defense": 40},
    "Salmane BO top 5": {"image": "images/salo.jpg", "rarity": "BO", "chance": 1, "attack": 99, "defense": 40},
    "Rl9 BO top 3": {"image": "images/rl9o.jpg", "rarity": "BO", "chance": 1, "attack": 102, "defense": 40},
    "Gab BO top 2": {"image": "images/gabo.jpg", "rarity": "BO", "chance": 0, "attack": 104, "defense": 40},
    "Nezox JR BO top 4": {"image": "images/nezo.jpg", "rarity": "BO", "chance": 1, "attack": 101, "defense": 40},
    
    "Nezox ICON": {"image": "images/nez.jpg", "rarity": "ICON", "chance": 0, "attack": 40, "defense": 101},
    "Mandancraft ICON": {"image": "images/man.jpg", "rarity": "ICON", "chance": 0, "attack": 0, "defense": 106},
    "Fuzety ICON": {"image": "images/fuz.jpg", "rarity": "ICON", "chance": 0, "attack": 107, "defense": 40},
    "Osico ICON": {"image": "images/osi.jpg", "rarity": "ICON", "chance": 1, "attack": 94, "defense": 81},
    "Barcola rtist ICON": {"image": "images/bar.jpg", "rarity": "ICON", "chance": 1, "attack": 98, "defense": 40},
    
    "Nezox JR Crack": {"image": "images/nezcr.png", "rarity": "cr", "chance": 90, "attack": 103, "defense": 40},
    "Diego Crack": {"image": "images/diecr.jpg", "rarity": "cr", "chance": 0, "attack": 40, "defense": 100},
    "Icardi Crack": {"image": "images/icacr.png", "rarity": "cr", "chance": 0, "attack": 95, "defense": 40},
    "Nathinio Crack": {"image": "images/natcr.jpg", "rarity": "cr", "chance": 1, "attack": 99, "defense": 40},
    "Skerry JR Crack": {"image": "images/skecr.png", "rarity": "cr", "chance": 1, "attack": 98, "defense": 40},
    "Rl9 Crack": {"image": "images/rl9cr.jpg", "rarity": "cr", "chance": 0, "attack": 100, "defense": 40},
    "Nono Mero Crack": {"image": "images/noncr.png", "rarity": "cr", "chance": 0, "attack": 101, "defense": 40},
    "Elekkrare Crack": {"image": "images/elecr.png", "rarity": "cr", "chance": 0, "attack": 30, "defense": 99},
    "Stony JR Crack": {"image": "images/stocr.png", "rarity": "cr", "chance": 1, "attack": 95, "defense": 30},
    "Apolskis JR Crack": {"image": "images/apocr.png", "rarity": "cr", "chance": 1, "attack": 106, "defense": 40},
    "Cold Creeper Crack": {"image": "images/colcr.png", "rarity": "cr", "chance": 0, "attack": 89, "defense": 91},
    "Kopoti Crack": {"image": "images/kopcr.png", "rarity": "cr", "chance": 0, "attack": 40, "defense": 101},
    
    "Alexis Futur": {"image": "images/alexis.jpg", "rarity": "fu", "chance": 1, "attack": 89, "defense": 30},
    "Casinox Futur": {"image": "images/cas.jpg", "rarity": "fu", "chance": 1, "attack": 0, "defense": 90},
    "Hector Futur": {"image": "images/hec.jpg", "rarity": "fu", "chance": 1, "attack": 87, "defense": 30},
    "Pacho Futur": {"image": "images/pac.jpg", "rarity": "fu", "chance": 1, "attack": 30, "defense": 88},
    "Marius Futur": {"image": "images/mar1.jpg", "rarity": "fu", "chance": 1, "attack": 91, "defense": 30},
    "Mathis JR Futur": {"image": "images/mat.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Mbappé JR Futur": {"image": "images/mbap.jpg", "rarity": "fu", "chance": 0, "attack": 88, "defense": 40},
    "Tavinho Futur": {"image": "images/tav2.jpg", "rarity": "fu", "chance": 0, "attack": 93, "defense": 40},
    "Rodri Futur": {"image": "images/rodr.jpg", "rarity": "fu", "chance": 1, "attack": 92, "defense": 30},
    "WanHida Futur": {"image": "images/wan.jpg", "rarity": "fu", "chance": 1, "attack": 89, "defense": 30},
    "Yanis Futur": {"image": "images/yanos.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 87},
    
    "Alexis flower": {"image": "images/ale.jpg", "rarity": "fl", "chance": 1, "attack": 89, "defense": 30},
    "Lumii flower": {"image": "images/lum.jpg", "rarity": "fl", "chance": 1, "attack": 0, "defense": 90},
    "Marius flower": {"image": "images/mar.jpg", "rarity": "fl", "chance": 1, "attack": 87, "defense": 30},
    "MXT Flower": {"image": "images/mxt1.jpg", "rarity": "fl", "chance": 1, "attack": 30, "defense": 88},
    "Nika Flower": {"image": "images/nik.jpg", "rarity": "fl", "chance": 1, "attack": 91, "defense": 30},
    "Nolan Flower": {"image": "images/nol.jpg", "rarity": "fl", "chance": 0, "attack": 87, "defense": 30},
    "Thethe Flower": {"image": "images/thet.jpg", "rarity": "fl", "chance": 0, "attack": 88, "defense": 40},
    "Wea1 Flower": {"image": "images/wea.jpg", "rarity": "fl", "chance": 0, "attack": 93, "defense": 40},
    "Yao Flower": {"image": "images/yao.jpg", "rarity": "fl", "chance": 1, "attack": 92, "defense": 30},
    "M10 Flower": {"image": "images/m10.jpg", "rarity": "fl", "chance": 1, "attack": 89, "defense": 30},
    "Loueye Flower": {"image": "images/lou.jpg", "rarity": "fl", "chance": 0, "attack": 30, "defense": 87},
    
    "Amau Vision": {"image": "images/ama.jpg", "rarity": "vi", "chance": 1, "attack": 92, "defense": 30},
    "Eva vision": {"image": "images/eva.jpg", "rarity": "vi", "chance": 1, "attack": 80, "defense": 60},
    "Mbappé JR vision": {"image": "images/mba.jpg", "rarity": "vi", "chance": 1, "attack": 86, "defense": 30},
    "Rodri vision": {"image": "images/rod.jpg", "rarity": "vi", "chance": 1, "attack": 93, "defense": 30},
    "Tavinho vision": {"image": "images/tav.jpg", "rarity": "vi", "chance": 1, "attack": 93, "defense": 30},
    "The Unique R vision": {"image": "images/the.jpg", "rarity": "vi", "chance": 0, "attack": 0, "defense": 95},
    "Under Doué vision": {"image": "images/und.jpg", "rarity": "vi", "chance": 0, "attack": 93, "defense": 40},
    "Liam vision": {"image": "images/liam.jpg", "rarity": "vi", "chance": 0, "attack": 80, "defense": 70},
    "Trotali JR vision": {"image": "images/cb.jpg", "rarity": "vi", "chance": 1, "attack": 94, "defense": 40},
    "M10 vision": {"image": "images/tro.jpg", "rarity": "vi", "chance": 1, "attack": 91, "defense": 30},
    "Mex JR vision": {"image": "images/mex.jpg", "rarity": "vi", "chance": 0, "attack": 86, "defense": 30},
    
    "Hgame TOTY": {"image": "images/hgat.jpg", "rarity": "TOTY", "chance": 1, "attack": 0, "defense": 111},
    "Ronaldo vision": {"image": "images/ront.jpg", "rarity": "TOTY", "chance": 1, "attack": 40, "defense": 103},
    "Esteban JR TOTY": {"image": "images/estt.jpg", "rarity": "TOTY", "chance": 1, "attack": 30, "defense": 107},
    "Léveillé TOTY": {"image": "images/levt.jpg", "rarity": "TOTY", "chance": 1, "attack": 30, "defense": 108},
    "Tima TOTY": {"image": "images/timt.jpg", "rarity": "TOTY", "chance": 1, "attack": 40, "defense": 104},
    "Louis29 TOTY": {"image": "images/lout.jpg", "rarity": "TOTY", "chance": 0, "attack": 98, "defense": 95},
    "Nathinio TOTY": {"image": "images/natt.jpg", "rarity": "TOTY", "chance": 0, "attack": 99, "defense": 90},
    "Amau TOTY": {"image": "images/amat.jpg", "rarity": "TOTY", "chance": 0, "attack": 107, "defense": 30},
    "Slapy TOTY": {"image": "images/slat.jpg", "rarity": "TOTY", "chance": 1, "attack": 112, "defense": 40},
    "Aaron TOTY": {"image": "images/aart.jpg", "rarity": "TOTY", "chance": 1, "attack": 109, "defense": 30},
    "Mattéo JR TOTY": {"image": "images/matt.jpg", "rarity": "TOTY", "chance": 0, "attack": 106, "defense": 30},
    "Rl9 TOTY": {"image": "images/rl9t.jpg", "rarity": "TOTY", "chance": 1, "attack": 106, "defense": 30},
    

    "Nezox JR Honorable": {"image": "images/nezt.jpg", "rarity": "TOTY", "chance": 1, "attack": 101, "defense": 30},
    "Icardi Honorable": {"image": "images/icat.png", "rarity": "TOTY", "chance": 1, "attack": 98, "defense": 30},
    "Kopoti Honorable": {"image": "images/kopt.png", "rarity": "TOTY", "chance": 1, "attack": 40, "defense": 97},
    "Apolskis JR Honorable": {"image": "images/apot.png", "rarity": "TOTY", "chance": 1, "attack": 101, "defense": 30},
    "Wea1 Honorable": {"image": "images/wea1t.png", "rarity": "TOTY", "chance": 1, "attack": 99, "defense": 30},
    "Gab Honorable": {"image": "images/gabt.png", "rarity": "TOTY", "chance": 1, "attack": 102, "defense": 30},
    "Elekkrare Honorable": {"image": "images/elet.png", "rarity": "TOTY", "chance": 1, "attack": 30, "defense": 100},
    "Skerry JR Honorable": {"image": "images/sket.png", "rarity": "TOTY", "chance": 1, "attack": 99, "defense": 30},
    "Cold Creeper Honorable": {"image": "images/colt.png", "rarity": "TOTY", "chance": 1, "attack": 92, "defense": 87},
    "SebriceMHSC Honorable": {"image": "images/sebt.png", "rarity": "TOTY", "chance": 1, "attack": 98, "defense": 30},
    "Cold Bee Honorable": {"image": "images/coltb.png", "rarity": "TOTY", "chance": 1, "attack": 97, "defense": 30},
}


cardsBO = {
    "Ekkrare": {"image": "images/ekkrare.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 91},
    "Matteo Jr": {"image": "images/mateo.png", "rarity": "légendaire", "chance": 1, "attack": 89, "defense": 40},
    "Aaron": {"image": "images/aaron.jpg", "rarity": "légendaire", "chance": 1, "attack": 94, "defense": 40},
    "Apolskis Jr": {"image": "images/apolskis.jpg", "rarity": "légendaire", "chance": 1, "attack": 91, "defense": 40},
    "wea1": {"image": "images/wea1.jpg", "rarity": "mythique", "chance": 3, "attack": 80, "defense": 50},
    "Aaron Jr": {"image": "images/aaron_jr.jpg", "rarity": "épique", "chance": 8, "attack": 87, "defense": 30},
    "Stony Jr": {"image": "images/stony_jr.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 30},
    "Thethe": {"image": "images/thethe.jpg", "rarity": "mythique", "chance": 3, "attack": 75, "defense": 65},
    "Nezox": {"image": "images/nezox.jpg", "rarity": "mythique", "chance": 3, "attack": 85, "defense": 40},
    "Amau": {"image": "images/amau.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Diego": {"image": "images/diego.jpg", "rarity": "épique", "chance": 10, "attack": 60, "defense": 89},
    "Kopoti": {"image": "images/kopoti.jpg", "rarity": "épique", "chance": 10, "attack": 50, "defense": 85},
    "Icardi": {"image": "images/icardi.jpg", "rarity": "mythique", "chance": 3, "attack": 90, "defense": 40},
    "Diamond Doku": {"image": "images/diamond_doku.jpg", "rarity": "épique", "chance": 20, "attack": 84, "defense": 30},
    "Nathinio": {"image": "images/nathinio.jpg", "rarity": "mythique", "chance": 3, "attack": 89, "defense": 40},
    "B": {"image": "images/b.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 87},
    "Mex Jr": {"image": "images/mex_jr.jpg", "rarity": "épique", "chance": 10, "attack": 85, "defense": 30},
    "Johan": {"image": "images/johan.jpg", "rarity": "mythique", "chance": 3, "attack": 70, "defense": 70},
    "Tima": {"image": "images/tima.jpg", "rarity": "mythique", "chance": 3, "attack": 50, "defense": 91},
    "The Unique R": {"image": "images/the_unique_r.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 91},
    "RL9": {"image": "images/rl9.jpg", "rarity": "mythique", "chance": 3, "attack": 91, "defense": 40},
    "Amau jr": {"image": "images/amau_jr.jpg", "rarity": "épique", "chance": 10, "attack": 97, "defense": 37},
    "Cosmos": {"image": "images/cosmos.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 75},
    "Dufour": {"image": "images/dufour.png", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Hgame": {"image": "images/Hgame.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 94},
    "Liam": {"image": "images/liam.png", "rarity": "épique", "chance": 10, "attack": 70, "defense": 75},
    "Lumii": {"image": "images/lumii.png", "rarity": "épique", "chance": 10, "attack": 20, "defense": 86},
    "Nono Mero": {"image": "images/nono_mero.jpg", "rarity": "mythique", "chance": 3, "attack": 88, "defense": 40},
    "Sade": {"image": "images/sade.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Slapy": {"image": "images/slapy.jpg", "rarity": "légendaire", "chance": 1, "attack": 92, "defense": 40},
    "trotali jr": {"image": "images/trotali_jr.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Brc": {"image": "images/brc.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 20},
    "Esteban": {"image": "images/esteban.jpg", "rarity": "mythique", "chance": 3, "attack": 30, "defense": 92},
    "Kilyan": {"image": "images/kilyan.jpg", "rarity": "épique", "chance": 10, "attack": 90, "defense": 30},
    "Luka": {"image": "images/luka.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 85},
    "M-7": {"image": "images/m-7.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 30},
    "MXT": {"image": "images/mxt.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    "Rayan": {"image": "images/rayan.jpg", "rarity": "épique", "chance": 10, "attack": 83, "defense": 30},
    "Rodri": {"image": "images/rodri.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 70},
    "Timeo": {"image": "images/timeo.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 82},
    "Valox": {"image": "images/valox.jpg", "rarity": "mythique", "chance": 3, "attack": 40, "defense": 86},
    "Zeerox": {"image": "images/zeerox.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "ZX Crakito": {"image": "images/zx_crakito.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    
    "Sebrice MHSC EAC": {"image": "images/1.jpg", "rarity": "EAC", "chance": 1, "attack": 92, "defense": 40},
    "Trotali JR EAC": {"image": "images/8.jpg", "rarity": "EAC", "chance": 2, "attack": 91, "defense": 25},
    "Mattéo JR EAC": {"image": "images/7.jpg", "rarity": "EAC", "chance": 1, "attack": 97, "defense": 30},
    "Gab EAC": {"image": "images/3.jpg", "rarity": "EAC", "chance": 1, "attack": 96, "defense": 20},
    "Léveillé EAC": {"image": "images/5.jpg", "rarity": "EAC", "chance": 1, "attack": 35, "defense": 95},
    "Louis29 EAC": {"image": "images/9.jpg", "rarity": "EAC", "chance": 1, "attack": 89, "defense": 89},
    "Tima EAC": {"image": "images/4.jpg", "rarity": "EAC", "chance": 2, "attack": 30, "defense": 93},
    "Nezox EAC": {"image": "images/2.jpg", "rarity": "EAC", "chance": 1, "attack": 30, "defense": 95},
    "Esteban EAC": {"image": "images/6.jpg", "rarity": "EAC", "chance": 1, "attack": 40, "defense": 94},
    "Hgame EAC": {"image": "images/10.jpg", "rarity": "EAC", "chance": 2, "attack": 0, "defense": 99},
    "Slapy EAC": {"image": "images/11.jpg", "rarity": "EAC", "chance": 1, "attack": 98, "defense": 65},
    
    "Louis29 BO": {"image": "images/loubo.jpg", "rarity": "BO", "chance": 2, "attack": 94, "defense": 94},
    "Mattéo JR BO": {"image": "images/matbo.jpg", "rarity": "BO", "chance": 2, "attack": 99, "defense": 40},
    "Aaron BO": {"image": "images/aarbo.jpg", "rarity": "BO", "chance": 2, "attack": 101, "defense": 40},
    "Slapy BO": {"image": "images/slabo.jpg", "rarity": "BO", "chance": 2, "attack": 100, "defense": 40},
    "Slapy BO top 1": {"image": "images/slao.jpg", "rarity": "BO", "chance": 2, "attack": 105, "defense": 40},
    "Salmane BO top 5": {"image": "images/slao.jpg", "rarity": "BO", "chance": 2, "attack": 99, "defense": 40},
    "Rl9 BO top 3": {"image": "images/rl9o.jpg", "rarity": "BO", "chance": 2, "attack": 102, "defense": 40},
    "Gab BO top 2": {"image": "images/gabo.jpg", "rarity": "BO", "chance": 2, "attack": 104, "defense": 40},
    "Nezox JR BO top 4": {"image": "images/nezo.jpg", "rarity": "BO", "chance": 2, "attack": 101, "defense": 40},

    "Alexis Futur": {"image": "images/alexis.jpg", "rarity": "fu", "chance": 1, "attack": 89, "defense": 30},
    "Casinox Futur": {"image": "images/cas.jpg", "rarity": "fu", "chance": 1, "attack": 0, "defense": 90},
    "Hector Futur": {"image": "images/hec.jpg", "rarity": "fu", "chance": 1, "attack": 87, "defense": 30},
    "Pacho Futur": {"image": "images/pac.jpg", "rarity": "fu", "chance": 1, "attack": 30, "defense": 88},
    "Marius Futur": {"image": "images/mar1.jpg", "rarity": "fu", "chance": 1, "attack": 91, "defense": 30},
    "Mathis JR Futur": {"image": "images/mat.jpg", "rarity": "fu", "chance": 0, "attack": 87, "defense": 30},
    "Mbappé JR Futur": {"image": "images/mbap.jpg", "rarity": "fu", "chance": 0, "attack": 88, "defense": 40},
    "Tavinho Futur": {"image": "images/tav2.jpg", "rarity": "fu", "chance": 0, "attack": 93, "defense": 40},
    "Rodri Futur": {"image": "images/rodr.jpg", "rarity": "fu", "chance": 1, "attack": 92, "defense": 30},
    "WanHida Futur": {"image": "images/wan.jpg", "rarity": "fu", "chance": 1, "attack": 89, "defense": 30},
    "Yanis Futur": {"image": "images/yanos.jpg", "rarity": "fu", "chance": 0, "attack": 30, "defense": 87},
    
    "Alexis flower": {"image": "images/ale.jpg", "rarity": "fl", "chance": 1, "attack": 89, "defense": 30},
    "Lumii flower": {"image": "images/lum.jpg", "rarity": "fl", "chance": 1, "attack": 0, "defense": 90},
    "Marius flower": {"image": "images/mar.jpg", "rarity": "fl", "chance": 1, "attack": 87, "defense": 30},
    "MXT Flower": {"image": "images/mxt1.jpg", "rarity": "fl", "chance": 1, "attack": 30, "defense": 88},
    "Nika Flower": {"image": "images/nik.jpg", "rarity": "fl", "chance": 1, "attack": 91, "defense": 30},
    "Nolan Flower": {"image": "images/nol.jpg", "rarity": "fl", "chance": 0, "attack": 87, "defense": 30},
    "Thethe Flower": {"image": "images/thet.jpg", "rarity": "fl", "chance": 0, "attack": 88, "defense": 40},
    "Wea1 Flower": {"image": "images/wea.jpg", "rarity": "fl", "chance": 0, "attack": 93, "defense": 40},
    "Yao Flower": {"image": "images/yao.jpg", "rarity": "fl", "chance": 1, "attack": 92, "defense": 30},
    "M10 Flower": {"image": "images/m10.jpg", "rarity": "fl", "chance": 1, "attack": 89, "defense": 30},
    "Loueye Flower": {"image": "images/lou.jpg", "rarity": "fl", "chance": 0, "attack": 30, "defense": 87},
    
    "Amau Vision": {"image": "images/ama.jpg", "rarity": "vi", "chance": 1, "attack": 92, "defense": 30},
    "Eva vision": {"image": "images/eva.jpg", "rarity": "vi", "chance": 1, "attack": 80, "defense": 60},
    "Mbappé JR vision": {"image": "images/mba.jpg", "rarity": "vi", "chance": 1, "attack": 86, "defense": 30},
    "Rodri vision": {"image": "images/rod.jpg", "rarity": "vi", "chance": 1, "attack": 93, "defense": 30},
    "Tavinho vision": {"image": "images/tav.jpg", "rarity": "vi", "chance": 1, "attack": 93, "defense": 30},
    "The Unique R vision": {"image": "images/the.jpg", "rarity": "vi", "chance": 0, "attack": 0, "defense": 95},
    "Under Doué vision": {"image": "images/und.jpg", "rarity": "vi", "chance": 0, "attack": 93, "defense": 40},
    "Liam vision": {"image": "images/liam.jpg", "rarity": "vi", "chance": 0, "attack": 80, "defense": 70},
    "Trotali JR vision": {"image": "images/cb.jpg", "rarity": "vi", "chance": 1, "attack": 94, "defense": 40},
    "M10 vision": {"image": "images/tro.jpg", "rarity": "vi", "chance": 1, "attack": 91, "defense": 30},
    "Mex JR vision": {"image": "images/mex.jpg", "rarity": "vi", "chance": 0, "attack": 86, "defense": 30},
    
    "Hgame TOTY": {"image": "images/hgat.jpg", "rarity": "TOTY", "chance": 1, "attack": 0, "defense": 111},
    "Ronaldo vision": {"image": "images/ront.jpg", "rarity": "TOTY", "chance": 1, "attack": 40, "defense": 103},
    "Esteban JR TOTY": {"image": "images/estt.jpg", "rarity": "TOTY", "chance": 1, "attack": 30, "defense": 107},
    "Léveillé TOTY": {"image": "images/levt.jpg", "rarity": "TOTY", "chance": 1, "attack": 30, "defense": 108},
    "Tima TOTY": {"image": "images/timt.jpg", "rarity": "TOTY", "chance": 1, "attack": 40, "defense": 104},
    "Louis29 TOTY": {"image": "images/lout.jpg", "rarity": "TOTY", "chance": 0, "attack": 98, "defense": 95},
    "Nathinio TOTY": {"image": "images/natt.jpg", "rarity": "TOTY", "chance": 0, "attack": 99, "defense": 90},
    "Amau TOTY": {"image": "images/amat.jpg", "rarity": "TOTY", "chance": 0, "attack": 107, "defense": 30},
    "Slapy TOTY": {"image": "images/slat.jpg", "rarity": "TOTY", "chance": 1, "attack": 112, "defense": 40},
    "Aaron TOTY": {"image": "images/aart.jpg", "rarity": "TOTY", "chance": 1, "attack": 109, "defense": 30},
    "Mattéo JR TOTY": {"image": "images/matt.jpg", "rarity": "TOTY", "chance": 0, "attack": 106, "defense": 30},
    "Rl9 TOTY": {"image": "images/rl9t.jpg", "rarity": "TOTY", "chance": 1, "attack": 106, "defense": 30},
    
    
}




cardsICON = {
    "Ekkrare": {"image": "images/ekkrare.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 91},
    "Matteo Jr": {"image": "images/mateo.png", "rarity": "légendaire", "chance": 1, "attack": 89, "defense": 40},
    "Aaron": {"image": "images/aaron.jpg", "rarity": "légendaire", "chance": 1, "attack": 94, "defense": 40},
    "Apolskis Jr": {"image": "images/apolskis.jpg", "rarity": "légendaire", "chance": 1, "attack": 91, "defense": 40},
    "wea1": {"image": "images/wea1.jpg", "rarity": "mythique", "chance": 3, "attack": 80, "defense": 50},
    "Aaron Jr": {"image": "images/aaron_jr.jpg", "rarity": "épique", "chance": 8, "attack": 87, "defense": 30},
    "Stony Jr": {"image": "images/stony_jr.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 30},
    "Thethe": {"image": "images/thethe.jpg", "rarity": "mythique", "chance": 3, "attack": 75, "defense": 65},
    "Nezox": {"image": "images/nezox.jpg", "rarity": "mythique", "chance": 3, "attack": 85, "defense": 40},
    "Amau": {"image": "images/amau.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Diego": {"image": "images/diego.jpg", "rarity": "épique", "chance": 10, "attack": 60, "defense": 89},
    "Kopoti": {"image": "images/kopoti.jpg", "rarity": "épique", "chance": 10, "attack": 50, "defense": 85},
    "Icardi": {"image": "images/icardi.jpg", "rarity": "mythique", "chance": 3, "attack": 90, "defense": 40},
    "Diamond Doku": {"image": "images/diamond_doku.jpg", "rarity": "épique", "chance": 20, "attack": 84, "defense": 30},
    "Nathinio": {"image": "images/nathinio.jpg", "rarity": "mythique", "chance": 3, "attack": 89, "defense": 40},
    "B": {"image": "images/b.jpg", "rarity": "épique", "chance": 10, "attack": 30, "defense": 87},
    "Mex Jr": {"image": "images/mex_jr.jpg", "rarity": "épique", "chance": 10, "attack": 85, "defense": 30},
    "Johan": {"image": "images/johan.jpg", "rarity": "mythique", "chance": 3, "attack": 70, "defense": 70},
    "Tima": {"image": "images/tima.jpg", "rarity": "mythique", "chance": 3, "attack": 50, "defense": 91},
    "The Unique R": {"image": "images/the_unique_r.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 91},
    "RL9": {"image": "images/rl9.jpg", "rarity": "mythique", "chance": 3, "attack": 91, "defense": 40},
    "Amau jr": {"image": "images/amau_jr.jpg", "rarity": "épique", "chance": 10, "attack": 97, "defense": 37},
    "Cosmos": {"image": "images/cosmos.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 75},
    "Dufour": {"image": "images/dufour.png", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Hgame": {"image": "images/Hgame.jpg", "rarity": "légendaire", "chance": 1, "attack": 0, "defense": 94},
    "Liam": {"image": "images/liam.png", "rarity": "épique", "chance": 10, "attack": 70, "defense": 75},
    "Lumii": {"image": "images/lumii.png", "rarity": "épique", "chance": 10, "attack": 20, "defense": 86},
    "Nono Mero": {"image": "images/nono_mero.jpg", "rarity": "mythique", "chance": 3, "attack": 88, "defense": 40},
    "Sade": {"image": "images/sade.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Slapy": {"image": "images/slapy.jpg", "rarity": "légendaire", "chance": 1, "attack": 92, "defense": 40},
    "trotali jr": {"image": "images/trotali_jr.jpg", "rarity": "mythique", "chance": 3, "attack": 92, "defense": 40},
    "Brc": {"image": "images/brc.jpg", "rarity": "épique", "chance": 10, "attack": 87, "defense": 20},
    "Esteban": {"image": "images/esteban.jpg", "rarity": "mythique", "chance": 3, "attack": 30, "defense": 92},
    "Kilyan": {"image": "images/kilyan.jpg", "rarity": "épique", "chance": 10, "attack": 90, "defense": 30},
    "Luka": {"image": "images/luka.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 85},
    "MXT": {"image": "images/mxt.jpg", "rarity": "épique", "chance": 10, "attack": 82, "defense": 30},
    "Rayan": {"image": "images/rayan.jpg", "rarity": "épique", "chance": 10, "attack": 83, "defense": 30},
    "Rodri": {"image": "images/rodri.jpg", "rarity": "épique", "chance": 10, "attack": 75, "defense": 70},
    "Ryan": {"image": "images/ryan.jpg", "rarity": "rare", "chance": 60, "attack": 75, "defense": 70},
    "Timeo": {"image": "images/timeo.jpg", "rarity": "épique", "chance": 10, "attack": 20, "defense": 82},
    "Valox": {"image": "images/valox.jpg", "rarity": "mythique", "chance": 3, "attack": 40, "defense": 86},
    "Zeerox": {"image": "images/zeerox.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    "ZX Crakito": {"image": "images/zx_crakito.jpg", "rarity": "épique", "chance": 10, "attack": 80, "defense": 70},
    
    "Sebrice MHSC EAC": {"image": "images/1.jpg", "rarity": "EAC", "chance": 1, "attack": 92, "defense": 40},
    "Trotali JR EAC": {"image": "images/8.jpg", "rarity": "EAC", "chance": 1, "attack": 91, "defense": 25},
    "Mattéo JR EAC": {"image": "images/7.jpg", "rarity": "EAC", "chance": 1, "attack": 97, "defense": 30},
    "Gab EAC": {"image": "images/3.jpg", "rarity": "EAC", "chance": 1, "attack": 96, "defense": 20},
    "Léveillé EAC": {"image": "images/5.jpg", "rarity": "EAC", "chance": 1, "attack": 35, "defense": 95},
    "Louis29 EAC": {"image": "images/9.jpg", "rarity": "EAC", "chance": 1, "attack": 89, "defense": 89},
    "Tima EAC": {"image": "images/4.jpg", "rarity": "EAC", "chance": 1, "attack": 30, "defense": 93},
    "Nezox EAC": {"image": "images/2.jpg", "rarity": "EAC", "chance": 1, "attack": 30, "defense": 95},
    "Esteban EAC": {"image": "images/6.jpg", "rarity": "EAC", "chance": 1, "attack": 40, "defense": 94},
    "Hgame EAC": {"image": "images/10.jpg", "rarity": "EAC", "chance": 1, "attack": 0, "defense": 99},
    "Slapy EAC": {"image": "images/11.jpg", "rarity": "EAC", "chance": 1, "attack": 98, "defense": 65},
    
    "Nezox ICON": {"image": "images/nez.jpg", "rarity": "ICON", "chance": 3, "attack": 40, "defense": 101},
    "Mandancraft ICON": {"image": "images/man.jpg", "rarity": "ICON", "chance": 2, "attack": 0, "defense": 106},
    "Fuzety ICON": {"image": "images/fuz.jpg", "rarity": "ICON", "chance": 1, "attack": 107, "defense": 40},
    "Osico ICON": {"image": "images/osi.jpg", "rarity": "ICON", "chance": 3, "attack": 94, "defense": 81},
    "Barcola rtist ICON": {"image": "images/bar.jpg", "rarity": "ICON", "chance": 3, "attack": 98, "defense": 40},   
}

leg = 0
rare = 0
commune = 0
myth = 0
epique = 0
icon = 0
EAC = 0
BO = 0
cr = 0
fu = 0

for card in cards:
    if cards[card]["rarity"] == "légendaire":
        leg+=1
        print(cards[card]["image"])
    if cards[card]["rarity"] == "mythique":
        myth += 1
    if cards[card]["rarity"] == "épique":
        epique += 1
    if cards[card]["rarity"] == "rare":
        rare += 1
    if cards[card]["rarity"] == "commun":
        commune +=1
    if cards[card]["rarity"] == "EAC":
        EAC += 1
    if cards[card]["rarity"] == "BO":
        BO += 1
    if cards[card]["rarity"] == "cr":
        cr += 1
    if cards[card]["rarity"] == "ICON":
        icon +=1  
    if cards[card]["rarity"] == "fu":
        fu +=1

print("legendaire: ",leg,"mythique: ",myth,"épique: ",epique,"rare: ",rare,"commune: ",commune,"BO: ",BO,"EAC: ",EAC,"cr: ",cr, "icon:",icon,"futur: ",fu)


# Fonction pour charger les cartes débloquées depuis un fichier CSV
def load_unlocked_cards_from_csv(file_path):
    unlocked_cards = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            unlocked_cards[name] = {
                'image': load_image(row['image'], 300, 400),
                'rarity': row['rarity'],
                'chance': int(row['chance']),
                'attack': int(row['attack']),
                'defense': int(row['defense'])
            }
    return unlocked_cards

# Charger les cartes débloquées depuis le fichier CSV
unlocked_cards = load_unlocked_cards_from_csv('unlocked_cards.csv')

def test_read_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)  # Affiche chaque ligne du CSV
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")

# Teste en appelant la fonction
test_read_csv('purchased_annonces.csv')

import csv
import pygame

# Fonction pour charger l'argent depuis le fichier CSV
def load_money_from_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return int(row['money'])  # Renvoie la valeur de l'argent
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
        return 0  # Retourne 0 si le fichier n'existe pas
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        return 0

# Fonction pour mettre à jour l'argent dans le fichier CSV
def update_money_in_csv(file_path, money):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['money']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'money': money})  # Met à jour la valeur de l'argent
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier CSV : {e}")

# Fonction pour charger les annonces achetées depuis un fichier CSV
def load_purchased_annonces(file_path):
    purchased_annonces = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                purchased_annonces.append({
                    'name': row['name'],
                    'image': row['image'],
                    'price': int(row['price']),
                    'category': row.get('category', 'Inconnue')
                })
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
    return purchased_annonces

def add_purchased_announcement_to_csv(file_path, annonce_name, annonce_image, annonce_price, annonce_category="Inconnue"):
    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'image', 'price', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'name': annonce_name,
            'image': annonce_image,
            'price': annonce_price,
            'category': annonce_category
        })

def show_annonces():
    global money, last_income_time
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')

    scroll_y = 0
    scroll_speed = 30
    spacing_y = 320
    spacing_x = 700
    start_y = 300
    start_x = 400

    categories = ["Tout", "Voitures", "Maillots", "avions", "Entreprises"]
    selected_category = "Tout"

    sorted_annonces_by_category = {
        category: sorted(
            [(name, {**data, 'price': int(data['price'])}) for name, data in annonces.items() if data['category'] == category or category == "Tout"],
            key=lambda item: item[1]['price'],
            reverse=True
        ) for category in categories
    }

    all_sorted_annonces = sorted_annonces_by_category[selected_category]
    total_rows = (len(all_sorted_annonces) + 1) // 2
    total_height = total_rows * spacing_y
    max_scroll = max(0, total_height - HEIGHT + start_y)

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                    if annonce['name'] == "Paris SG":
                        money += 128000
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                    if annonce['name'] == "Lutti":
                        money += 2300
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
            update_money_in_csv('money.csv', money)

        draw_start_screen(background_img2)

        for i, (name, annonce) in enumerate(all_sorted_annonces):
            row = i // 2
            col = i % 2
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y - scroll_y

            if y > HEIGHT or y + 220 < 0:
                continue

            if 'loaded_image' not in annonce:
                raw_img = pygame.image.load(annonce['image']).convert_alpha()
                annonce['loaded_image'] = scale_and_center_image(raw_img)

            screen.blit(annonce['loaded_image'], (x + 100, y))
            draw_text(name, x - 100, y + 110, size=30, color=WHITE)
            draw_text(f"Prix: {format_price(annonce['price'])}€", x - 100, y + 140, size=30, color=WHITE)

            already_bought = name in [a['name'] for a in purchased_annonces]
            button_text = "Déjà acheté" if already_bought else "Acheter"
            button_color = (0, 200, 0) if already_bought else (200, 0, 0)
            hover_color = (0, 255, 0) if already_bought else (255, 0, 0)

            draw_button(x + 200, y + 180, 200, 40, button_text, color=button_color, hover_color=hover_color)

        # Boutons fixes
        draw_button(310, 50, 180, 50, "Entreprises", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(510, 50, 180, 50, "Tout", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(710, 50, 180, 50, "Voitures", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(910, 50, 180, 50, "Maillots", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(1110, 50, 180, 50, "Avions", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(10, 700, 180, 50, "Mes achats", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(10, 800, 180, 50, "Menu", color=(0, 200, 0), hover_color=(0, 255, 0))

        draw_text(f"Argent: {money}€", 10, 10, size=30, color=WHITE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = event.pos

                # Gérer les clics sur les boutons de catégorie
                if 310 <= x_mouse <= 500 and 50 <= y_mouse <= 100:
                    selected_category = "Entreprises"
                    scroll_y = 0
                    all_sorted_annonces = sorted_annonces_by_category[selected_category]
                elif 510 <= x_mouse <= 700 and 50 <= y_mouse <= 100:
                    selected_category = "Tout"
                    scroll_y = 0
                    all_sorted_annonces = sorted_annonces_by_category[selected_category]
                elif 710 <= x_mouse <= 900 and 50 <= y_mouse <= 100:
                    selected_category = "Voitures"
                    scroll_y = 0
                    all_sorted_annonces = sorted_annonces_by_category[selected_category]
                elif 910 <= x_mouse <= 1100 and 50 <= y_mouse <= 100:
                    selected_category = "Maillots"
                    scroll_y = 0
                    all_sorted_annonces = sorted_annonces_by_category[selected_category]
                elif 1110 <= x_mouse <= 1300 and 50 <= y_mouse <= 100:
                    selected_category = "avions"
                    scroll_y = 0 
                    all_sorted_annonces = sorted_annonces_by_category[selected_category]
                elif 10 <= x_mouse <= 190 and 700 <= y_mouse <= 750:
                    show_purchased_annonces()
                elif 10 <= x_mouse <= 190 and 800 <= y_mouse <= 850:
                    main_menu()

                # Vérification des clics sur les annonces
                for i, (name, annonce) in enumerate(all_sorted_annonces):
                    row = i // 2
                    col = i % 2

                    x = start_x + col * spacing_x
                    y = start_y + row * spacing_y - scroll_y

                    if y <= y_mouse <= y + 220 and x + 200 <= x_mouse <= x + 400:
                        already_bought = name in [a['name'] for a in purchased_annonces]
                        if not already_bought and money >= annonce['price']:
                            add_purchased_announcement_to_csv(
                                'purchased_annonces.csv',
                                name,
                                annonce['image'],
                                annonce['price'],
                                annonce['category']
                            )
                            money -= annonce['price']
                            update_money_in_csv('money.csv', money)
                            purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
                        elif not already_bought:
                            draw_text("Pas assez d'argent !", WIDTH // 2 - 100, HEIGHT - 50, size=24, color=RED)

            # ← ICI ! Molette gérée hors du if précédent
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    scroll_y = max(scroll_y - scroll_speed, 0)
                elif event.button == 5:  # Scroll down
                    scroll_y = min(scroll_y + scroll_speed, max_scroll)


# Fonction optionnelle si tu veux l'utiliser ailleurs
def filter_annonces_by_category(category):
    if category == "Tout":
        return annonces
    return {name: data for name, data in annonces.items() if data["category"] == category}
      




def show_purchased_annonces():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')

    scroll_y = 0
    scroll_speed = 30
    spacing_y = 320
    spacing_x = 700
    start_y = 300
    start_x = 400
    categories = ["Tout", "Voitures", "Maillots","avions","Entreprises"]
    selected_category = "Tout"

    # Chargement des images + ajout des données manquantes si besoin
    for annonce in purchased_annonces:
        raw_img = pygame.image.load(annonce['image']).convert_alpha()
        annonce['loaded_image'] = scale_and_center_image(raw_img)
        annonce['price'] = int(annonce['price'])  # au cas où ce soit encore une string

    def get_annonces_by_category(cat):
        if cat == "Tout":
            return purchased_annonces
        return [a for a in purchased_annonces if a['category'] == cat]

    all_sorted_annonces = sorted(get_annonces_by_category(selected_category), key=lambda a: a['price'], reverse=True)

    total_rows = (len(all_sorted_annonces) + 1) // 2
    total_height = total_rows * spacing_y
    max_scroll = max(0, total_height - HEIGHT + start_y)

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        draw_start_screen(background_img2)


        # Affichage des annonces achetées
        for i, annonce in enumerate(all_sorted_annonces):
            row = i // 2
            col = i % 2

            x = start_x + col * spacing_x
            y = start_y + row * spacing_y - scroll_y

            if y > HEIGHT or y + 220 < 0:
                continue

            screen.blit(annonce['loaded_image'], (x + 100, y))
            draw_text(annonce['name'], x - 100, y + 110, size=30, color=WHITE)
            draw_text(f"Prix: {format_price(annonce['price'])}€", x - 100, y + 140, size=30, color=WHITE)
            
            # Boutons de filtre par catégorie
        draw_button(310, 50, 180, 50, "Entreprises", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(510, 50, 180, 50, "Tout", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(710, 50, 180, 50, "Voitures", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(910, 50, 180, 50, "Maillots", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(1110, 50, 180, 50, "Avions", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(10, 700, 180, 50, "Retour", color=(0, 200, 0), hover_color=(0, 255, 0))
        draw_button(10, 800, 180, 50, "Menu", color=(0, 200, 0), hover_color=(0, 255, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = event.pos

                # Filtrage par catégorie
                if 310 <= x_mouse <= 500 and 50 <= y_mouse <= 100:
                    selected_category = "Entreprises"
                if 510 <= x_mouse <= 700 and 50 <= y_mouse <= 100:
                    selected_category = "Tout"
                if 710 <= x_mouse <= 900 and 50 <= y_mouse <= 100:
                    selected_category = "Voitures"
                if 910 <= x_mouse <= 1100 and 50 <= y_mouse <= 100:
                    selected_category = "Maillots"
                if 1110 <= x_mouse <= 1300 and 50 <= y_mouse <= 100:
                    selected_category = "avions"
                all_sorted_annonces = sorted(get_annonces_by_category(selected_category), key=lambda a: a['price'], reverse=True)

                # Boutons retour/menu
                if 10 <= x_mouse <= 190 and 700 <= y_mouse <= 750:
                    return
                if 10 <= x_mouse <= 190 and 800 <= y_mouse <= 850:
                    return main_menu()

                # Scroll
                if event.button == 4:
                    scroll_y = max(scroll_y - scroll_speed, 0)
                elif event.button == 5:
                    scroll_y = min(scroll_y + scroll_speed, max_scroll)

        if scroll_y > max_scroll:
            scroll_y = max_scroll



    

#chargement d'argent
money = load_money_from_csv('money.csv')
print(f"Montant actuel : {money}€")



def scale_and_center_image(image):
    # Calcul de l'échelle en maintenant le ratio
    width, height = image.get_size()
    target_width = 400
    target_height = 200

    # Calcul du ratio
    scale_ratio = min(target_width / width, target_height / height)
    new_width = int(width * scale_ratio)
    new_height = int(height * scale_ratio)

    # Redimensionnement de l'image
    image = pygame.transform.scale(image, (new_width, new_height))

    # Création d'une nouvelle surface avec transparence pour y centrer l'image
    centered_image = pygame.Surface((target_width, target_height), pygame.SRCALPHA)
    x_offset = (target_width - new_width) // 2
    y_offset = (target_height - new_height) // 2
    centered_image.blit(image, (x_offset, y_offset))

    return centered_image









aze = 0
for card in cards:
    aze +=1
print ("nombre de carte :",aze)

# Liste des musiques disponibles
musics = {
    "Kids": "musics/kids.mp3",
    "Wherever I Go": "musics/Wherever I Go.mp3",
    "Timeless": "musics/Timeless.mp3",
    "Believer": "musics/believer.mp3",
    "This is what you came for": "musics/cv.mp3",
    "The search": "musics/nf.mp3",
    "CAN'T STOP THE FEELING": "musics/CAN'T STOP THE FEELING.mp3",
    "Blame": "musics/blame.mp3",
    "Summer": "musics/summer.mp3",
    "Dolce camara": "musics/dolce_camara.mp3",
    "Safe and sound": "musics/safe and sound.mp3",
    "imogen heap": "musics/imogen heap.mp3",
    "Feet Dont Fail Me Now": "musics/Feet Dont Fail Me Now.mp3",
    "Heat Waves": "musics/Heat Waves.mp3"
}

def play_music(path=None):
    if path is None:
        path = random.choice(list(musics.values()))  # Choisir une musique aléatoire
    
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Déclencher un événement à la fin



for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.USEREVENT:  # La musique est terminée
        play_music()  # Jouer une nouvelle musique aléatoire

# Charger une musique par défaut
play_music(list(musics.values())[0])


def music_menu():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    volume = 1  # Valeur initiale du volume (100%)
    slider_width = 300  # Largeur du curseur
    slider_rect = pygame.Rect(WIDTH // 2 - slider_width // 2, HEIGHT - 100, slider_width, 10)  # Position et taille du curseur
    slider_handle_width = 30  # Largeur du curseur
    dragging = False  # Variable pour savoir si on est en train de glisser le curseur

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        draw_start_screen(background_img2)
        draw_text("Sélection de musique", WIDTH // 2 - 160, 50, size=48, color=WHITE)

        # Afficher les musiques comme avant
        x_offset = WIDTH // 2 - 575  # Décalage horizontal
        y_offset = 150
        col = 0  # Compteur de colonnes

        buttons = []  # Stocke les boutons pour la détection des clics

        for title, path in musics.items():
            buttons.append((x_offset - 20, y_offset, 350, 50, path))  # Sauvegarde du bouton
            draw_button(x_offset - 20, y_offset, 350, 50, title)

            col += 1
            if col % 3 == 0:  # Retour à la ligne toutes les 3 musiques
                x_offset = WIDTH // 2 - 575
                y_offset += 80
            else:
                x_offset += 440  # Espacement entre les boutons

        # Bouton Retour
        buttons.append((WIDTH // 2 - 100, y_offset + 250, 200, 50, "Retour"))
        draw_button(WIDTH // 2 - 100, y_offset + 250, 200, 50, "Retour")

        # Afficher le curseur de volume
        pygame.draw.rect(screen, (30, 30, 30), slider_rect)  # Fond du curseur (plus sombre pour un effet de profondeur)

        # Nouveau dégradé sur la barre de volume (bleu à vert)
        for i in range(slider_width):
            # Transition de bleu à vert
            r = int(0 + (i / slider_width) * 40)  # Transition du bleu vers un bleu-vert
            g = int(0 + (i / slider_width) * 255)  # Du bleu vers le vert pastel
            b = int(255 - (i / slider_width) * 100)  # Bleu qui se fait plus pâle vers le vert
            pygame.draw.line(screen, (r, g, b), (slider_rect.x + i, slider_rect.y), (slider_rect.x + i, slider_rect.y + slider_rect.height))

        # Affichage du curseur
        cursor_x = slider_rect.x + volume * slider_width - slider_handle_width // 2
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(cursor_x, slider_rect.y - 5, slider_handle_width, slider_rect.height + 10))  # Curseur blanc avec effet lumineux
        pygame.draw.circle(screen, (255, 255, 255), (cursor_x + slider_handle_width // 2, slider_rect.centery), 12)  # Curseur rond (style)

        draw_text(f"Volume: {int(volume * 100)}%", slider_rect.centerx, slider_rect.y - 30, size=24, color=WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Vérifier si on a cliqué sur le curseur
                if slider_rect.collidepoint(x, y):
                    dragging = True  # Commence à glisser le curseur
                    volume = (x - slider_rect.x) / slider_width  # Met à jour le volume
                    volume = max(0, min(1, volume))  # Limite la valeur du volume entre 0 et 1

                for bx, by, bw, bh, path in buttons:
                    if bx <= x <= bx + bw and by <= y <= by + bh:
                        if path == "Retour":
                            return  # Retour au menu principal
                        play_music(path)  # Jouer la musique sélectionnée

            if event.type == pygame.MOUSEMOTION and dragging:
                x, y = event.pos
                # Met à jour le volume si on est en train de glisser le curseur
                volume = (x - slider_rect.x) / slider_width
                volume = max(0, min(1, volume))  # Limite la valeur du volume entre 0 et 1

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False  # Arrête de glisser le curseur

        # Appliquer le volume à la musique en cours
        pygame.mixer.music.set_volume(volume)


backgrounds = [
    ("Apolskis jr", "images/yamal.jpg"),
    ("Apolskis jr II", "images/test.jpg"),
    ("Nono Mero", "images/back1.jpg"),
    ("Nono Mero II", "images/nono_II.jpg"),
    ("Icardi", "images/icardiback.jpg"),
    ("Icardi II", "images/icardiII.jpg"),
    ("Nezox jr", "images/nezoxbg.jpg"),
    ("Nezox jr II", "images/nezoxbg_II.jpg"),
    ("Kopoti", "images/peakpx.jpg"),
    ("Kopoti II", "images/kop.jpg"),
    ("Ldc", "images/backldc.jpg"),
    ("Messi", "images/messiback.jpg"),
    ("Mbappé", "images/mbappepsg.jpg"),
    ("Forêt", "images/forest.png"),
    ("Nébuleuse", "images/nebula.jpg"),
]

selected_background = load_image("images/forest.png", WIDTH, HEIGHT)  # Fond par défaut

def backmenu():
    global selected_background  # Permet de modifier la variable globale
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
        # Effacer l'écran avant de dessiner le nouveau contenu
        screen.fill(BLACK)

        # Dessiner l'écran de fond avec le fond sélectionné
        draw_start_screen(selected_background)
        draw_text("Choisir un fond", WIDTH // 2 - 150, 50, size=48, color=WHITE)

        # Coordonnées de base pour positionner les boutons
        x_center = WIDTH // 2 - 350  # Centrage horizontal
        y_start = 300  # Position de départ des boutons
        spacing_x = 250  # Espacement horizontal entre les boutons
        spacing_y = 100  # Espacement vertical entre les lignes

        buttons = []  # Stocke les positions pour gérer les clics

        # Dessiner les boutons dans une grille de 3 colonnes
        for i, (label, image_path) in enumerate(backgrounds):
            row, col = divmod(i, 3)
            x = x_center + col * spacing_x
            y = y_start + row * spacing_y
            draw_button(x, y, 200, 50, label)
            buttons.append((x, y, 200, 50, image_path))

        # Bouton retour au menu
        draw_button(WIDTH // 2 - 100, y_start + spacing_y * 5, 200, 50, "Menu")

        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Vérification des clics sur les boutons de fond d'écran
                for bx, by, bw, bh, image_path in buttons:
                    if bx <= x <= bx + bw and by <= y <= by + bh:
                        selected_background = load_image(image_path, WIDTH, HEIGHT)

                # Bouton retour au menu
                if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and y_start + spacing_y * 5 <= y <= y_start + spacing_y * 5 + 50:
                    return






# Génération de la liste des cartes avec probabilités
card_pool = [card for card, info in cards.items() for _ in range(info["chance"])]

def draw_text(text, x, y, size=36, color=WHITE, outline=BLACK, background=None):
    font = pygame.font.Font(None, size)

    # Ombre du texte (contour)
    outline_surface = font.render(text, True, outline)
    screen.blit(outline_surface, (x - 2, y - 2))
    screen.blit(outline_surface, (x + 2, y - 2))
    screen.blit(outline_surface, (x - 2, y + 2))
    screen.blit(outline_surface, (x + 2, y + 2))

    # Texte principal
    text_surface = font.render(text, True, color)

    if background:
        background_rect = text_surface.get_rect(topleft=(x - 10, y - 5))
        pygame.draw.rect(screen, background, background_rect)
    
    screen.blit(text_surface, (x, y))




def draw_button(x, y, width, height, text, color=(100, 100, 100), hover_color=WHITE):
    # Dessiner le bouton avec des coins arrondis et une légère ombre portée
    radius = 20  # Rayon des coins arrondis
    shadow_offset = 5  # Décalage de l'ombre pour l'effet de profondeur

    # Ombre portée du bouton
    pygame.draw.rect(screen, (0, 0, 0), (x + shadow_offset, y + shadow_offset, width, height), border_radius=radius)

    # Dessiner le bouton
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_color = color if not (x <= mouse_x <= x + width and y <= mouse_y <= y + height) else hover_color
    pygame.draw.rect(screen, button_color, (x, y, width, height), border_radius=radius)

    # Déterminer la couleur du texte en fonction de la couleur du bouton
    text_color = WHITE if button_color != WHITE else BLACK  # Texte blanc sur fond sombre, texte noir sur fond blanc

    # Afficher le texte centré dans le bouton
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect.topleft)




# Fonction pour les couleurs de rareté
def get_background_color(rarity):
    colors = {
        "commun": (0, 200, 0),
        "rare": (0, 0, 200),
        "épique": (128, 0, 128),
        "mythique": (200, 0, 0),  # Rouge
        "légendaire": (255, 255, 0),
    }
    return colors.get(rarity, (0, 0, 139))

def get_light_color(rarity):
    light_colors = {
        "commun": (50, 255, 0),
        "rare": (0, 191, 255),
        "épique": (153, 50, 204),
        "mythique": (255, 69, 0),
        "légendaire": (255, 215, 0),
        "EAC": (0, 0, 255),
        "BO": (255, 215, 0),
        "ICON": (255, 215, 0),
        "cr": (255, 50, 204),
        "fu": (255, 70, 210),
        "fl": (110, 110, 255),
        "vi": (110, 110, 255),
        "TOTY": (110, 110, 255),
    }
    return light_colors.get(rarity, (75, 0, 130))

# Reste du code inchangé...


def draw_start_screen(back):
    # Afficher l'image de fond
    screen.blit(back, (0, 0))
    if back == terrain :
        back = pygame.transform.rotate(back, 90) # Dessiner le texte du titre
    # Ajoute d'autres éléments que tu veux afficher sur cet écran ici

# Fonction pour afficher l'argent
def display_money(money):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f"Argent : {money}€", True, (255, 255, 255))  # Texte en blanc
    screen.blit(text, (10, 10))  # Afficher en haut à gauche



def main_menu():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
        
        # Ajouter un délai pour éviter une surcharge du processeur
        time.sleep(0.01)
        screen.fill(BLACK)
        draw_start_screen(selected_background)
        draw_text("Mobcraft Pack Opener", WIDTH // 2 - 230, 50, size=64, color=WHITE)
        display_money(money)

        x_center = WIDTH // 2 - 100
        y_start = 400
        spacing_y = 100

        draw_button(x_center - 250, y_start, 200, 50, "Packs")
        draw_button(x_center, y_start, 200, 50, "Cartes")
        draw_button(x_center + 250, y_start, 200, 50, "Jouer")

        draw_button(x_center - 250, y_start + spacing_y, 200, 50, "Entrainement")
        draw_button(x_center, y_start + spacing_y, 200, 50, "Musique")
        draw_button(x_center + 250, y_start + spacing_y, 200, 50, "Quitter")

        draw_button(x_center - 250, y_start + 2 * spacing_y, 200, 50, "Mes Cartes")
        draw_button(x_center, y_start + 2 * spacing_y, 200, 50, "Fond d'écran")
        draw_button(x_center + 250, y_start + 2 * spacing_y, 200, 50, "Boutique")

        pygame.display.flip()

        # GESTION DES ÉVÉNEMENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # gestion des clics sur les boutons (comme tu l’avais déjà)
                # Vérification des clics sur les boutons
                if y_start <= y <= y_start + 50:  # Première ligne
                    if x_center - 250 <= x <= x_center - 50:
                        pack_menu()
                    elif x_center <= x <= x_center + 200:
                        show_cards()
                    elif x_center + 250 <= x <= x_center + 450:
                        play()
                
                elif y_start + spacing_y <= y <= y_start + spacing_y + 50:  # Deuxième ligne
                    if x_center - 250 <= x <= x_center - 50:
                        run_game()  # S'entrainer
                    elif x_center <= x <= x_center + 200:
                        music_menu()
                    elif x_center + 250 <= x <= x_center + 450:
                        pygame.quit()
                        exit()

                elif y_start + 2 * spacing_y <= y <= y_start + 2 * spacing_y + 50:  # Troisième ligne (Fond d'écran)
                    if x_center - 250 <= x <= x_center - 50:
                        show_cards_from_csv()
                    if x_center <= x <= x_center + 200:
                        backmenu()
                    elif x_center + 250 <= x <= x_center + 450:
                        show_annonces()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
def pack_menu():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
        
        # Ajouter un délai pour éviter une surcharge du processeur
        time.sleep(0.01)
        screen.fill(BLACK)
        draw_start_screen(selected_background)
        draw_text("Packs MB25", WIDTH // 2 - 230, 50, size=64, color=WHITE)
        display_money(money)

        x_center = WIDTH // 2 - 100
        y_start = 400
        spacing_y = 100

        draw_button(x_center - 250, y_start, 200, 50, "Pack Basique")
        draw_button(x_center, y_start, 200, 50, "Pack Icon")
        draw_button(x_center + 250, y_start, 200, 50, "Pack Ballon d'Or")
        
        draw_text(" 150 ", x_center - 170, 470, size=25, color=WHITE)
        draw_text("50000", x_center + 80, 470, size=25, color=WHITE)
        draw_text("60000", x_center + 325, 470, size=25, color=WHITE)

#         draw_button(x_center - 250, y_start + spacing_y, 200, 50, "Entrainement")
        draw_button(x_center, y_start + spacing_y, 200, 50, "Pack Spécial")
#         draw_button(x_center + 250, y_start + spacing_y, 200, 50, "Quitter")

        draw_text("100000", x_center + 80, 570, size=25, color=WHITE)

#         draw_button(x_center - 250, y_start + 2 * spacing_y, 200, 50, "Mes Cartes")
        draw_button(x_center, y_start + 2 * spacing_y, 200, 50, "Menu")
#         draw_button(x_center + 250, y_start + 2 * spacing_y, 200, 50, "Boutique")

        pygame.display.flip()

        # GESTION DES ÉVÉNEMENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # gestion des clics sur les boutons (comme tu l’avais déjà)
                # Vérification des clics sur les boutons
                if y_start <= y <= y_start + 50:  # Première ligne
                    if x_center - 250 <= x <= x_center - 50 and money >= 100:
                        money -= 150
                        update_money_in_csv('money.csv', money)
                        game()
                    elif x_center <= x <= x_center + 200 and money >= 20000:
                        money -= 20000
                        update_money_in_csv('money.csv', money)
                        gameICON()
                    elif x_center + 250 <= x <= x_center + 450 and money >= 40000:
                        money -= 40000
                        update_money_in_csv('money.csv', money)
                        gameBO()
                
                elif y_start + spacing_y <= y <= y_start + spacing_y + 50:  # Deuxième ligne
                    if x_center - 250 <= x <= x_center - 50:
                        pass
                    if x_center <= x <= x_center + 200 and money >= 30000:
                        money -= 100000
                        update_money_in_csv('money.csv', money)
                        gamecol()
                    elif x_center + 250 <= x <= x_center + 450:
                        pass
# 
                elif y_start + 2 * spacing_y <= y <= y_start + 2 * spacing_y + 50:  # Troisième ligne (Fond d'écran)
#                     if x_center - 250 <= x <= x_center - 50:
#                         show_cards_from_csv()
                     if x_center <= x <= x_center + 200:
                         main_menu()
#                     elif x_center + 250 <= x <= x_center + 450:
#                         show_annonces()
                        





def show_cards():
    global money, last_income_time
    last_income_time = time.time()
    t = 0

    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')

    scroll_y = 0
    scroll_speed = 30
    max_per_row = 6
    card_width, card_height = 120, 160
    spacing_x, spacing_y = 210, 200
    title_y, start_y = 50, 170

    total_row_width = max_per_row * spacing_x
    start_x = (WIDTH - total_row_width) // 2

    # Tri par rareté
    rarities = {
        "commun": 1,
        "rare": 2,
        "épique": 3,
        "mythique": 4,
        "légendaire": 5,
        "fu": 6,
        "vi": 6.5,
        "EAC": 7,
        "fl": 7.5,
        "cr": 8,
        "ICON": 9,
        "BO": 10,
        "TOTY": 11,
    }

    # Trier les cartes par rareté
    sorted_cards = sorted(cards.items(), key=lambda x: rarities.get(x[1]["rarity"], 0), reverse=True)
    

    total_rows = (len(sorted_cards) + max_per_row - 1) // max_per_row
    total_height = start_y + total_rows * spacing_y

    # Précharger les images
    card_images = {
        name: pygame.image.load(info['image']) for name, info in cards.items()
    }

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            total_gain = 0
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        total_gain += 4756000
                    elif annonce['name'] == "Paris SG":
                        total_gain += 128000
                    elif annonce['name'] == "La Bonne Fournée":
                        total_gain += 1000
                    elif annonce['name'] == "Lutti":
                        total_gain += 2300
                    elif annonce['name'] == "Salon de coiffure":
                        total_gain += 150
            if total_gain > 0:
                money += total_gain
                update_money_in_csv('money.csv', money)

        draw_start_screen(background_img2)

        title_position_y = title_y - scroll_y
        draw_text("Toutes les Cartes", WIDTH // 2 - 150, title_position_y, size=48, color=WHITE)

        max_scroll = max(0, total_height - HEIGHT + 150)
        scroll_y = max(0, min(scroll_y, max_scroll))

        # Affichage des cartes triées
        for i, (card_name, info) in enumerate(sorted_cards):
            row = i // max_per_row
            col = i % max_per_row
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y - scroll_y

            if -card_height < y < HEIGHT:
                card_img = pygame.transform.scale(card_images[card_name], (card_width, card_height))
                screen.blit(card_img, (x + 25, y))
                draw_text_with_background(
                    card_name, x + card_width // 2 + 25, y + card_height + 25,
                    size=20, color=WHITE, background_color=(0, 0, 0, 128)
                )

        draw_button(WIDTH // 2 - 100, HEIGHT - 100, 200, 50, "Retour au menu", color=(0, 200, 0), hover_color=(0, 255, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 4:
                    scroll_y -= scroll_speed
                elif event.button == 5:
                    scroll_y += scroll_speed
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 100 <= y <= HEIGHT - 50:
                    return

                
                
                
import csv

def show_cards_from_csv():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    scroll_y = 0  # Décalage vertical
    scroll_speed = 30  # Vitesse du défilement
    max_per_row = 6  # Nombre max de cartes par ligne
    card_width = 120
    card_height = 160
    spacing_x = 210  # Espacement horizontal
    spacing_y = 200  # Espacement vertical
    title_y = 50  # Position de départ du titre
    start_y = 170  # Position de départ des cartes

    # Calcul de la position horizontale pour centrer les cartes
    total_row_width = max_per_row * spacing_x
    start_x = (WIDTH - total_row_width) // 2

    # Chargement des cartes depuis le CSV
    cards_from_csv = []
    with open('unlocked_cards.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cards_from_csv.append({
                'name': row['name'],
                'image': row['image'],
                'rarity': row['rarity'],
                'chance': int(row['chance']),
                'attack': int(row['attack']),
                'defense': int(row['defense'])
            })

    # Définir l'ordre des raretés
    rarity_order = {
        'TOTY': 11,
        'BO': 10,
        'ICON' : 9,
        "fl": 7.5,
        'EAC': 7,
        'cr' : 8,
        "fu": 6,
        'légendaire': 5,
        'épique': 4,
        'mythique': 3,
        'rare': 2,
        'commun': 1
    }

    # Trier les cartes par rareté (utilisation de l'ordre défini ci-dessus)
    cards_from_csv.sort(key=lambda card: rarity_order.get(card['rarity'], 0), reverse=True)

    # Calcul de la hauteur totale du contenu
    total_rows = (len(cards_from_csv) + max_per_row - 1) // max_per_row  # Nombre total de lignes
    total_height = start_y + total_rows * spacing_y  # Hauteur totale nécessaire

    # Pré-charge toutes les images des cartes
    card_images = {}
    for card in cards_from_csv:
        card_images[card['name']] = pygame.image.load(card['image'])

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
        draw_start_screen(background_img2)

        # Ajuste la position du titre avec le scroll
        title_position_y = title_y - scroll_y
        draw_text("Cartes Débloquées", WIDTH // 2 - 150, title_position_y, size=48, color=WHITE)

        # Limite du scroll pour éviter de remonter trop haut ou trop bas
        max_scroll = max(0, total_height - HEIGHT + 150)  # 150 de marge
        scroll_y = max(0, min(scroll_y, max_scroll))  # Clamp du scroll

        # Affichage des cartes en fonction du scroll
        for i, card in enumerate(cards_from_csv):
            row = i // max_per_row
            col = i % max_per_row
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y - scroll_y  # Décale avec le scroll

            if -card_height < y < HEIGHT:  # Affiche uniquement les cartes visibles
                card_img = pygame.transform.scale(card_images[card['name']], (card_width, card_height))
                screen.blit(card_img, (x + 25, y))
                draw_text_with_background(card['name'], x + card_width // 2 + 25, y + card_height + 25, size=20, color=WHITE, background_color=(0, 0, 0, 128))

        # Bouton "Retour au menu"
        draw_button(WIDTH // 2 - 100, HEIGHT - 100, 200, 50, "Retour au menu", color=(0, 200, 0), hover_color=(0, 255, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 4:  # Molette vers le haut
                    scroll_y -= scroll_speed
                elif event.button == 5:  # Molette vers le bas
                    scroll_y += scroll_speed
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 100 <= y <= HEIGHT - 50:
                    return  # Retour au menu principal






def draw_text_centered(text, x, y, size=24, color=BLACK):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect.topleft)

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    
    for word in words:
        # Ajouter le mot suivant, vérifier si la ligne dépasse la largeur maximale
        if font.size(current_line + word)[0] <= max_width:
            current_line += word + " "
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        lines.append(current_line.strip())  # Ajouter la dernière ligne
    
    return lines


def draw_text_with_background(text, x, y, size=30, color=WHITE, background_color=(0, 255, 255, 128)):
    font = pygame.font.Font(None, size)
    
    # Définir la largeur maximale pour la ligne de texte
    max_width = WIDTH - 40  # 40px pour laisser une marge
    
    # Découper le texte en plusieurs lignes si nécessaire
    lines = wrap_text(text, font, max_width)
    
    # Calculer la hauteur nécessaire pour toutes les lignes
    total_height = sum([font.size(line)[1] for line in lines])
    
    # Positionner verticalement les lignes
    current_y = y - total_height // 2
    
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, current_y))
        
        # Créer un fond pour chaque ligne
        background_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 10), pygame.SRCALPHA)
        background_surface.fill(background_color)
        
        screen.blit(background_surface, (text_rect.left - 10, text_rect.top - 5))  # Dessiner le fond
        screen.blit(text_surface, text_rect.topleft)  # Afficher le texte
        
        current_y += font.size(line)[1]  # Ajuster la position pour la ligne suivante




def game():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    booster_opened = False
    card_index = 0
    show_front = False
    card_rarity = None  # Variable pour garder la rareté de la carte actuelle
    leg=0
    myt=0
    epi=0
    rar=0
    com=0
    EAC=0
    ico=0
    BO=0
    fu=0
    cr=0
    fl=0
    vi=0
    TOTY=0
    
    # Sélection des cartes en évitant les doublons
    unique_cards = list(cardsgame.keys())
    selected_cards = []

    # Si vous avez plus de 3 cartes disponibles, choisissez 3 cartes uniques
    if len(unique_cards) >= 3:
        selected_cards = random.sample(unique_cards, 3)  # Sélectionne 3 cartes aléatoires uniques
        # Si une carte légendaire est présente, remplacez-la par une carte non légendaire
        for card in selected_cards:
            if cardsgame[card]["rarity"] == "légendaire":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "EAC":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "BO":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "ICON":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "cr":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "fu":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "fl":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "vi":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "TOTY":
                print ("toty")
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
                
        for card in selected_cards:
            if cardsgame[card]["rarity"] == "légendaire":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "EAC":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "BO":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "ICON":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "cr":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "fu":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "fl":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "vi":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsgame[card]["rarity"] == "TOTY":
                print ("toty")
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire


    else:
        selected_cards = random.choices(unique_cards, k=3)  # Choisir parmi toutes les cartes disponibles

    # Ajouter les cartes à unlocked_cards si elles ne sont pas encore débloquées
    for card_name in selected_cards:
        if card_name not in unlocked_cards:
            unlocked_cards[card_name] = {
                'image': cardsgame[card_name]['image'],
                'rarity': cardsgame[card_name]['rarity'],
                'chance': cardsgame[card_name]['chance'],
                'attack': cardsgame[card_name]['attack'],
                'defense': cardsgame[card_name]['defense']
            }

            # Optionnel : Ajoute la carte dans le CSV si elle est débloquée
            with open('unlocked_cards.csv', mode='a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'image', 'rarity', 'chance', 'attack', 'defense']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'name': card_name,
                    'image': cardsgame[card_name]['image'],
                    'rarity': cardsgame[card_name]['rarity'],
                    'chance': cardsgame[card_name]['chance'],
                    'attack': cardsgame[card_name]['attack'],
                    'defense': cardsgame[card_name]['defense']
                })

    # 🔴 AFFICHAGE DU BOOSTER AVANT L'OUVERTURE
    screen.fill((0, 0, 139))  # Bleu foncé
    booster_rect = booster_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(booster_img, booster_rect.topleft)
    pygame.display.flip()

    # Attente d'un clic avant d'ouvrir le pack
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # Le joueur a cliqué, on peut commencer

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        if card_index < len(selected_cards):
            current_card = selected_cards[card_index]
            card_rarity = cardsgame[current_card]["rarity"]  # Récupère la rareté de la carte actuelle
            
            if not booster_opened:
                screen.fill((0, 0, 139))  # Fond bleu foncé tant que le booster n'est pas ouvert
            elif show_front:
                # Afficher un fond spécial selon la rareté de la carte
                if card_rarity == "légendaire":
                    if leg==0:
                        money += 10000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        leg+=1
                    draw_start_screen(background_img3)
                elif card_rarity == "rare":
                    if rar==0:
                        money += 20; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        rar+=1
                    draw_start_screen(background_img4)
                elif card_rarity == "commun":
                    if com==0:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        com+=1
                    draw_start_screen(background_img5)
                elif card_rarity == "mythique":
                    if myt==0:
                        money += 300; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        myt+=1
                    draw_start_screen(background_img6)
                elif card_rarity == "épique":
                    if epi==0:
                        money += 50; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        epi+=1
                    draw_start_screen(background_img7)
                elif card_rarity == "EAC":
                    if EAC==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        EAC+=1
                    draw_start_screen(background_img10)
                elif card_rarity == "ICON":
                    if ico==0:
                        money += 50000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        ico+=1
                    draw_start_screen(background_img11)
                elif card_rarity == "cr":
                    if cr==0:
                        money += 35000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img12)
                elif card_rarity == "fu":
                    if cr==0:
                        money += 40000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img13)
                elif card_rarity == "fl":
                    if cr==0:
                        money += 45000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img14)
                elif card_rarity == "vi":
                    if cr==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img15)
                elif card_rarity == "TOTY":
                    if TOTY==0:
                        money += 25000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        TOTY+=1
                    draw_start_screen(background_img16)
                elif card_rarity == "BO":
                    if BO==0:
                        money += 22500; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        BO+=1
                    draw_start_screen(background_img9)
                else:
                    screen.fill(get_background_color(card_rarity))  # Fond selon la rareté

                # Afficher le nom de la carte avec un fond transparent
                draw_text_with_background(current_card, WIDTH // 2, 50, size=30, color=WHITE, background_color=(0, 0, 0, 20))

            else:
                screen.fill((0, 0, 139))  # Bleu foncé

            # Afficher la carte avec son image
            card_img = pygame.image.load(cardsgame[current_card]["image"]) if show_front else card_back_img
            card_img = pygame.transform.scale(card_img, (300, 400))  # Redimensionner l'image de la carte
            card_rect = card_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(card_img, card_rect.topleft)

            # Effet lumineux statique autour de la carte (seulement si la carte est de face)
            if show_front:
                light_rect = pygame.Rect(
                    card_rect.left - 10,
                    card_rect.top - 10,
                    card_rect.width + 20,
                    card_rect.height + 20
                )
                light_color = get_light_color(card_rarity)  # Couleur du halo basé sur la rareté
                pygame.draw.rect(screen, light_color, light_rect, 5)  # Rectangle lumineux

        else:
            draw_start_screen(background_img8)  # Fond pour le récapitulatif

            # Organise les cartes en 2 lignes (3 cartes sur la première, 3 cartes sur la deuxième)
            y_offset = 150
            x_offset_first_row = WIDTH // 2 - 3 * 100  # Centre la première ligne de 3 cartes
            x_offset_second_row = WIDTH // 2 - 300  # Centre la deuxième ligne de 3 cartes

            # Affiche les cartes sur deux lignes
            for i in range(3):  
                card_img = pygame.transform.scale(pygame.image.load(cardsgame[selected_cards[i]]["image"]), (195, 260))
                card_rect = card_img.get_rect(center=(x_offset_first_row + i * 300, y_offset + 300))
                screen.blit(card_img, card_rect.topleft)
                draw_text_with_background(selected_cards[i], x_offset_first_row + i * 300, y_offset + 460, color=WHITE, background_color=(0, 0, 0, 128))

            # Affichage des boutons
            draw_button(WIDTH // 2 - 100, HEIGHT - 70, 200, 50, "Réouvrir", color=(0, 200, 0), hover_color=(0, 255, 0))
            draw_button(WIDTH // 2 + 150, HEIGHT - 70, 200, 50, "Quitter", color=(200, 0, 0), hover_color=(255, 0, 0))
            draw_button(WIDTH // 2 - 350, HEIGHT - 70, 200, 50, "Menu", color=(0, 0, 200), hover_color=(0, 0, 255))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if card_index < len(selected_cards):
                    if not booster_opened:
                        booster_opened = True
                    if not show_front:
                        show_front = True  # Afficher le recto de la carte au premier clic
                    else:
                        card_index += 1  # Passer à la carte suivante après avoir vu le recto
                        show_front = False  # Montrer à nouveau le dos de la carte
                elif card_index == len(selected_cards):
                    # Vérifie si l'utilisateur clique sur les boutons "Réouvrir" ou "Quitter"
                    if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        game()  # Réouvrir un booster
                    elif WIDTH // 2 - 350 <= x <= WIDTH // 2 - 350 + 200 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        main_menu()
                    elif WIDTH // 2 + 150 <= x <= WIDTH // 2 + 350 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        pygame.quit()
                        exit()
                        
                        
def gameBO():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    booster_opened = False
    card_index = 0
    show_front = False
    card_rarity = None  # Variable pour garder la rareté de la carte actuelle
    leg=0
    myt=0
    epi=0
    rar=0
    com=0
    EAC=0
    ico=0
    cr=0
    fu=0
    fl=0
    vi=0
    TOTY=0
    
    # Sélection des cartes en évitant les doublons
    unique_cards = list(cardsBO.keys())
    selected_cards = []

    # Si vous avez plus de 3 cartes disponibles, choisissez 3 cartes uniques
    if len(unique_cards) >= 3:
        selected_cards = random.sample(unique_cards, 3)  # Sélectionne 3 cartes aléatoires uniques
        # Si une carte légendaire est présente, remplacez-la par une carte non légendaire
        for card in selected_cards:
            if cardsBO[card]["rarity"] == "légendaire":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardsBO[card]["rarity"] == "EAC":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire

    else:
        selected_cards = random.choices(unique_cards, k=3)  # Choisir parmi toutes les cartes disponibles

    # Ajouter les cartes à unlocked_cards si elles ne sont pas encore débloquées
    for card_name in selected_cards:
        if card_name not in unlocked_cards:
            unlocked_cards[card_name] = {
                'image': cardsBO[card_name]['image'],
                'rarity': cardsBO[card_name]['rarity'],
                'chance': cardsBO[card_name]['chance'],
                'attack': cardsBO[card_name]['attack'],
                'defense': cardsBO[card_name]['defense']
            }

            # Optionnel : Ajoute la carte dans le CSV si elle est débloquée
            with open('unlocked_cards.csv', mode='a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'image', 'rarity', 'chance', 'attack', 'defense']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'name': card_name,
                    'image': cardsBO[card_name]['image'],
                    'rarity': cardsBO[card_name]['rarity'],
                    'chance': cardsBO[card_name]['chance'],
                    'attack': cardsBO[card_name]['attack'],
                    'defense': cardsBO[card_name]['defense']
                })

    # 🔴 AFFICHAGE DU BOOSTER AVANT L'OUVERTURE
    screen.fill((0, 0, 139))  # Bleu foncé
    booster_rect = booster_img2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(booster_img2, booster_rect.topleft)
    pygame.display.flip()

    # Attente d'un clic avant d'ouvrir le pack
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # Le joueur a cliqué, on peut commencer

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        if card_index < len(selected_cards):
            current_card = selected_cards[card_index]
            card_rarity = cardsBO[current_card]["rarity"]  # Récupère la rareté de la carte actuelle
            
            if not booster_opened:
                screen.fill((0, 0, 139))  # Fond bleu foncé tant que le booster n'est pas ouvert
            elif show_front:
                # Afficher un fond spécial selon la rareté de la carte
                if card_rarity == "légendaire":
                    if leg==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        leg+=1
                    draw_start_screen(background_img3)
                elif card_rarity == "rare":
                    if rar==0:
                        money += 20; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        rar+=1
                    draw_start_screen(background_img4)
                elif card_rarity == "commun":
                    if com==0:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        com+=1
                    draw_start_screen(background_img5)
                elif card_rarity == "mythique":
                    if myt==0:
                        money += 300; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        myt+=1
                    draw_start_screen(background_img6)
                elif card_rarity == "épique":
                    if epi==0:
                        money += 50; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        epi+=1
                    draw_start_screen(background_img7)
                elif card_rarity == "EAC":
                    if EAC==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        EAC+=1
                    draw_start_screen(background_img10)
                elif card_rarity == "BO":
                    if BO==0:
                        money += 70000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        BO+=1
                    draw_start_screen(background_img9)
                elif card_rarity == "fu":
                    if cr==0:
                        money += 40000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img13)
                elif card_rarity == "fl":
                    if cr==0:
                        money += 45000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img14)
                elif card_rarity == "vi":
                    if cr==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img15)
                elif card_rarity == "TOTY":
                    if cr==0:
                        money += 100000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img16)
                else:
                    screen.fill(get_background_color(card_rarity))  # Fond selon la rareté

                # Afficher le nom de la carte avec un fond transparent
                draw_text_with_background(current_card, WIDTH // 2, 50, size=30, color=WHITE, background_color=(0, 0, 0, 20))

            else:
                screen.fill((0, 0, 139))  # Bleu foncé

            # Afficher la carte avec son image
            card_img = pygame.image.load(cardsBO[current_card]["image"]) if show_front else card_back_img
            card_img = pygame.transform.scale(card_img, (300, 400))  # Redimensionner l'image de la carte
            card_rect = card_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(card_img, card_rect.topleft)

            # Effet lumineux statique autour de la carte (seulement si la carte est de face)
            if show_front:
                light_rect = pygame.Rect(
                    card_rect.left - 10,
                    card_rect.top - 10,
                    card_rect.width + 20,
                    card_rect.height + 20
                )
                light_color = get_light_color(card_rarity)  # Couleur du halo basé sur la rareté
                pygame.draw.rect(screen, light_color, light_rect, 5)  # Rectangle lumineux

        else:
            draw_start_screen(background_img8)  # Fond pour le récapitulatif

            # Organise les cartes en 2 lignes (3 cartes sur la première, 3 cartes sur la deuxième)
            y_offset = 150
            x_offset_first_row = WIDTH // 2 - 3 * 100  # Centre la première ligne de 3 cartes
            x_offset_second_row = WIDTH // 2 - 300  # Centre la deuxième ligne de 3 cartes

            # Affiche les cartes sur deux lignes
            for i in range(3):  
                card_img = pygame.transform.scale(pygame.image.load(cardsBO[selected_cards[i]]["image"]), (195, 260))
                card_rect = card_img.get_rect(center=(x_offset_first_row + i * 300, y_offset + 300))
                screen.blit(card_img, card_rect.topleft)
                draw_text_with_background(selected_cards[i], x_offset_first_row + i * 300, y_offset + 460, color=WHITE, background_color=(0, 0, 0, 128))

            # Affichage des boutons
            draw_button(WIDTH // 2 - 100, HEIGHT - 70, 200, 50, "Réouvrir", color=(0, 200, 0), hover_color=(0, 255, 0))
            draw_button(WIDTH // 2 + 150, HEIGHT - 70, 200, 50, "Quitter", color=(200, 0, 0), hover_color=(255, 0, 0))
            draw_button(WIDTH // 2 - 350, HEIGHT - 70, 200, 50, "Menu", color=(0, 0, 200), hover_color=(0, 0, 255))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if card_index < len(selected_cards):
                    if not booster_opened:
                        booster_opened = True
                    if not show_front:
                        show_front = True  # Afficher le recto de la carte au premier clic
                    else:
                        card_index += 1  # Passer à la carte suivante après avoir vu le recto
                        show_front = False  # Montrer à nouveau le dos de la carte
                elif card_index == len(selected_cards):
                    # Vérifie si l'utilisateur clique sur les boutons "Réouvrir" ou "Quitter"
                    if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        gameBO()  # Réouvrir un booster
                    elif WIDTH // 2 - 350 <= x <= WIDTH // 2 - 350 + 200 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        main_menu()
                    elif WIDTH // 2 + 150 <= x <= WIDTH // 2 + 350 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        pygame.quit()
                        exit()
                        

def gamecol():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    booster_opened = False
    card_index = 0
    show_front = False
    card_rarity = None  # Variable pour garder la rareté de la carte actuelle
    leg=0
    myt=0
    epi=0
    rar=0
    com=0
    EAC=0
    ico=0
    cr=0
    fu=0
    fl=0
    vi=0
    TOTY=0
    
    # Sélection des cartes en évitant les doublons
    unique_cards = list(cardscol.keys())
    selected_cards = []

    # Si vous avez plus de 3 cartes disponibles, choisissez 3 cartes uniques
    if len(unique_cards) >= 3:
        selected_cards = random.sample(unique_cards, 3)  # Sélectionne 3 cartes aléatoires uniques
        # Si une carte légendaire est présente, remplacez-la par une carte non légendaire
        for card in selected_cards:
            if cardscol[card]["rarity"] == "légendaire":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire
            if cardscol[card]["rarity"] == "EAC":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire

    else:
        selected_cards = random.choices(unique_cards, k=3)  # Choisir parmi toutes les cartes disponibles

    # Ajouter les cartes à unlocked_cards si elles ne sont pas encore débloquées
    for card_name in selected_cards:
        if card_name not in unlocked_cards:
            unlocked_cards[card_name] = {
                'image': cardscol[card_name]['image'],
                'rarity': cardscol[card_name]['rarity'],
                'chance': cardscol[card_name]['chance'],
                'attack': cardscol[card_name]['attack'],
                'defense': cardscol[card_name]['defense']
            }

            # Optionnel : Ajoute la carte dans le CSV si elle est débloquée
            with open('unlocked_cards.csv', mode='a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'image', 'rarity', 'chance', 'attack', 'defense']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'name': card_name,
                    'image': cardscol[card_name]['image'],
                    'rarity': cardscol[card_name]['rarity'],
                    'chance': cardscol[card_name]['chance'],
                    'attack': cardscol[card_name]['attack'],
                    'defense': cardscol[card_name]['defense']
                })

    # 🔴 AFFICHAGE DU BOOSTER AVANT L'OUVERTURE
    screen.fill((0, 0, 139))  # Bleu foncé
    booster_rect = booster_img2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(booster_img4, booster_rect.topleft)
    pygame.display.flip()

    # Attente d'un clic avant d'ouvrir le pack
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # Le joueur a cliqué, on peut commencer

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        if card_index < len(selected_cards):
            current_card = selected_cards[card_index]
            card_rarity = cardscol[current_card]["rarity"]  # Récupère la rareté de la carte actuelle
            
            if not booster_opened:
                screen.fill((0, 0, 139))  # Fond bleu foncé tant que le booster n'est pas ouvert
            elif show_front:
                # Afficher un fond spécial selon la rareté de la carte
                if card_rarity == "légendaire":
                    if leg==0:
                        money += 45000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        leg+=1
                    draw_start_screen(background_img3)
                elif card_rarity == "rare":
                    if rar==0:
                        money += 20; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        rar+=1
                    draw_start_screen(background_img4)
                elif card_rarity == "commun":
                    if com==0:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        com+=1
                    draw_start_screen(background_img5)
                elif card_rarity == "mythique":
                    if myt==0:
                        money += 300; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        myt+=1
                    draw_start_screen(background_img6)
                elif card_rarity == "épique":
                    if epi==0:
                        money += 50; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        epi+=1
                    draw_start_screen(background_img7)
                elif card_rarity == "BO":
                    if BO==0:
                        money += 110000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        BO+=1
                    draw_start_screen(background_img9)
                elif card_rarity == "EAC":
                    if EAC==0:
                        money += 45000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        EAC+=1
                    draw_start_screen(background_img10)
                elif card_rarity == "ICON":
                    if ico==0:
                        money += 80000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        ico+=1
                    draw_start_screen(background_img11)
                elif card_rarity == "cr":
                    if cr==0:
                        money += 50000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img12)
                elif card_rarity == "fu":
                    if cr==0:
                        money += 40000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img13)
                elif card_rarity == "fl":
                    if cr==0:
                        money += 40000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img14)
                elif card_rarity == "vi":
                    if cr==0:
                        money += 25000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img15)
                elif card_rarity == "TOTY":
                    if TOTY==0:
                        money += 100000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        TOTY+=1
                    draw_start_screen(background_img16)
                else:
                    screen.fill(get_background_color(card_rarity))  # Fond selon la rareté

                # Afficher le nom de la carte avec un fond transparent
                draw_text_with_background(current_card, WIDTH // 2, 50, size=30, color=WHITE, background_color=(0, 0, 0, 20))

            else:
                screen.fill((0, 0, 139))  # Bleu foncé

            # Afficher la carte avec son image
            card_img = pygame.image.load(cardscol[current_card]["image"]) if show_front else card_back_img
            card_img = pygame.transform.scale(card_img, (300, 400))  # Redimensionner l'image de la carte
            card_rect = card_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(card_img, card_rect.topleft)

            # Effet lumineux statique autour de la carte (seulement si la carte est de face)
            if show_front:
                light_rect = pygame.Rect(
                    card_rect.left - 10,
                    card_rect.top - 10,
                    card_rect.width + 20,
                    card_rect.height + 20
                )
                light_color = get_light_color(card_rarity)  # Couleur du halo basé sur la rareté
                pygame.draw.rect(screen, light_color, light_rect, 5)  # Rectangle lumineux

        else:
            draw_start_screen(background_img8)  # Fond pour le récapitulatif

            # Organise les cartes en 2 lignes (3 cartes sur la première, 3 cartes sur la deuxième)
            y_offset = 150
            x_offset_first_row = WIDTH // 2 - 3 * 100  # Centre la première ligne de 3 cartes
            x_offset_second_row = WIDTH // 2 - 300  # Centre la deuxième ligne de 3 cartes

            # Affiche les cartes sur deux lignes
            for i in range(3):  
                card_img = pygame.transform.scale(pygame.image.load(cardscol[selected_cards[i]]["image"]), (195, 260))
                card_rect = card_img.get_rect(center=(x_offset_first_row + i * 300, y_offset + 300))
                screen.blit(card_img, card_rect.topleft)
                draw_text_with_background(selected_cards[i], x_offset_first_row + i * 300, y_offset + 460, color=WHITE, background_color=(0, 0, 0, 128))

            # Affichage des boutons
            draw_button(WIDTH // 2 - 100, HEIGHT - 70, 200, 50, "Réouvrir", color=(0, 200, 0), hover_color=(0, 255, 0))
            draw_button(WIDTH // 2 + 150, HEIGHT - 70, 200, 50, "Quitter", color=(200, 0, 0), hover_color=(255, 0, 0))
            draw_button(WIDTH // 2 - 350, HEIGHT - 70, 200, 50, "Menu", color=(0, 0, 200), hover_color=(0, 0, 255))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if card_index < len(selected_cards):
                    if not booster_opened:
                        booster_opened = True
                    if not show_front:
                        show_front = True  # Afficher le recto de la carte au premier clic
                    else:
                        card_index += 1  # Passer à la carte suivante après avoir vu le recto
                        show_front = False  # Montrer à nouveau le dos de la carte
                elif card_index == len(selected_cards):
                    # Vérifie si l'utilisateur clique sur les boutons "Réouvrir" ou "Quitter"
                    if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        gamecol()  # Réouvrir un booster
                    elif WIDTH // 2 - 350 <= x <= WIDTH // 2 - 350 + 200 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        main_menu()
                    elif WIDTH // 2 + 150 <= x <= WIDTH // 2 + 350 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        pygame.quit()
                        exit()


                        
def gameICON():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    booster_opened = False
    card_index = 0
    show_front = False
    card_rarity = None  # Variable pour garder la rareté de la carte actuelle
    leg=0
    myt=0
    epi=0
    rar=0
    com=0
    EAC=0
    ico=0
    
    # Sélection des cartes en évitant les doublons
    unique_cards = list(cardsICON.keys())
    selected_cards = []

    # Si vous avez plus de 3 cartes disponibles, choisissez 3 cartes uniques
    if len(unique_cards) >= 3:
        selected_cards = random.sample(unique_cards, 3)  # Sélectionne 3 cartes aléatoires uniques
        # Si une carte légendaire est présente, remplacez-la par une carte non légendaire
        for card in selected_cards:
            if cardsICON[card]["rarity"] == "légendaire":
                selected_cards.remove(card)  # Retirer une carte légendaire
                # Sélectionner une carte supplémentaire
                remaining_cards = list(set(unique_cards) - set(selected_cards))  # Cartes restantes
                selected_cards += random.sample(remaining_cards, 1)  # Ajoute une nouvelle carte aléatoire

    else:
        selected_cards = random.choices(unique_cards, k=3)  # Choisir parmi toutes les cartes disponibles

    # Ajouter les cartes à unlocked_cards si elles ne sont pas encore débloquées
    for card_name in selected_cards:
        if card_name not in unlocked_cards:
            unlocked_cards[card_name] = {
                'image': cardsICON[card_name]['image'],
                'rarity': cardsICON[card_name]['rarity'],
                'chance': cardsICON[card_name]['chance'],
                'attack': cardsICON[card_name]['attack'],
                'defense': cardsICON[card_name]['defense']
            }

            # Optionnel : Ajoute la carte dans le CSV si elle est débloquée
            with open('unlocked_cards.csv', mode='a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'image', 'rarity', 'chance', 'attack', 'defense']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'name': card_name,
                    'image': cardsICON[card_name]['image'],
                    'rarity': cardsICON[card_name]['rarity'],
                    'chance': cardsICON[card_name]['chance'],
                    'attack': cardsICON[card_name]['attack'],
                    'defense': cardsICON[card_name]['defense']
                })

    # 🔴 AFFICHAGE DU BOOSTER AVANT L'OUVERTURE
    screen.fill((0, 0, 139))  # Bleu foncé
    booster_rect = booster_img3.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(booster_img3, booster_rect.topleft)
    pygame.display.flip()

    # Attente d'un clic avant d'ouvrir le pack
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # Le joueur a cliqué, on peut commencer

    while True:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        if card_index < len(selected_cards):
            current_card = selected_cards[card_index]
            card_rarity = cardsICON[current_card]["rarity"]  # Récupère la rareté de la carte actuelle
            
            if not booster_opened:
                screen.fill((0, 0, 139))  # Fond bleu foncé tant que le booster n'est pas ouvert
            elif show_front:
                # Afficher un fond spécial selon la rareté de la carte
                if card_rarity == "légendaire":
                    if leg==0:
                        money += 1000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        leg+=1
                    draw_start_screen(background_img3)
                elif card_rarity == "rare":
                    if rar==0:
                        money += 20; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        rar+=1
                    draw_start_screen(background_img4)
                elif card_rarity == "commun":
                    if com==0:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        com+=1
                    draw_start_screen(background_img5)
                elif card_rarity == "mythique":
                    if myt==0:
                        money += 300; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        myt+=1
                    draw_start_screen(background_img6)
                elif card_rarity == "épique":
                    if epi==0:
                        money += 50; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        epi+=1
                    draw_start_screen(background_img7)
                elif card_rarity == "EAC":
                    if EAC==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        EAC+=1
                    draw_start_screen(background_img10)
                elif card_rarity == "ICON":
                    if ico==0:
                        money += 35000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        ico+=1
                    draw_start_screen(background_img11)
                elif card_rarity == "fu":
                    if cr==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img13)
                elif card_rarity == "fl":
                    if cr==0:
                        money += 20000; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        cr+=1
                    draw_start_screen(background_img14)
                else:
                    screen.fill(get_background_color(card_rarity))  # Fond selon la rareté

                # Afficher le nom de la carte avec un fond transparent
                draw_text_with_background(current_card, WIDTH // 2, 50, size=30, color=WHITE, background_color=(0, 0, 0, 20))

            else:
                screen.fill((0, 0, 139))  # Bleu foncé

            # Afficher la carte avec son image
            card_img = pygame.image.load(cardsICON[current_card]["image"]) if show_front else card_back_img
            card_img = pygame.transform.scale(card_img, (300, 400))  # Redimensionner l'image de la carte
            card_rect = card_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(card_img, card_rect.topleft)

            # Effet lumineux statique autour de la carte (seulement si la carte est de face)
            if show_front:
                light_rect = pygame.Rect(
                    card_rect.left - 10,
                    card_rect.top - 10,
                    card_rect.width + 20,
                    card_rect.height + 20
                )
                light_color = get_light_color(card_rarity)  # Couleur du halo basé sur la rareté
                pygame.draw.rect(screen, light_color, light_rect, 5)  # Rectangle lumineux

        else:
            draw_start_screen(background_img8)  # Fond pour le récapitulatif

            # Organise les cartes en 2 lignes (3 cartes sur la première, 3 cartes sur la deuxième)
            y_offset = 150
            x_offset_first_row = WIDTH // 2 - 3 * 100  # Centre la première ligne de 3 cartes
            x_offset_second_row = WIDTH // 2 - 300  # Centre la deuxième ligne de 3 cartes

            # Affiche les cartes sur deux lignes
            for i in range(3):  
                card_img = pygame.transform.scale(pygame.image.load(cardsICON[selected_cards[i]]["image"]), (195, 260))
                card_rect = card_img.get_rect(center=(x_offset_first_row + i * 300, y_offset + 300))
                screen.blit(card_img, card_rect.topleft)
                draw_text_with_background(selected_cards[i], x_offset_first_row + i * 300, y_offset + 460, color=WHITE, background_color=(0, 0, 0, 128))

            # Affichage des boutons
            draw_button(WIDTH // 2 - 100, HEIGHT - 70, 200, 50, "Réouvrir", color=(0, 200, 0), hover_color=(0, 255, 0))
            draw_button(WIDTH // 2 + 150, HEIGHT - 70, 200, 50, "Quitter", color=(200, 0, 0), hover_color=(255, 0, 0))
            draw_button(WIDTH // 2 - 350, HEIGHT - 70, 200, 50, "Menu", color=(0, 0, 200), hover_color=(0, 0, 255))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if card_index < len(selected_cards):
                    if not booster_opened:
                        booster_opened = True
                    if not show_front:
                        show_front = True  # Afficher le recto de la carte au premier clic
                    else:
                        card_index += 1  # Passer à la carte suivante après avoir vu le recto
                        show_front = False  # Montrer à nouveau le dos de la carte
                elif card_index == len(selected_cards):
                    # Vérifie si l'utilisateur clique sur les boutons "Réouvrir" ou "Quitter"
                    if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        gameICON()  # Réouvrir un booster
                    elif WIDTH // 2 - 350 <= x <= WIDTH // 2 - 350 + 200 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        main_menu()
                    elif WIDTH // 2 + 150 <= x <= WIDTH // 2 + 350 and HEIGHT - 70 <= y <= HEIGHT - 20:
                        money += 10; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
                        pygame.quit()
                        exit()



                        
def play():
    global money, last_income_time
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')

    rarities = {
        "commun": 1,
        "rare": 2,
        "épique": 3,
        "mythique": 4,
        "légendaire": 5,
        "ICON" : 13,
        "cr" : 7,
        "BO" : 11,
        "EAC" : 6,
        "fu" : 10,
        "fl" : 8,
        "vi" : 9,
        "TOTY" : 12 
    }


    # Étape 1 : Sélection du deck de l'ennemi avec exactement un gardien
    enemy_deck = []
    all_cards = list(cards.keys())

    # Sélection des gardiens (attaque == 0)
    goalkeepers = [card for card in all_cards if cards[card]["attack"] == 0]

    # Ajout d'un gardien s'il y en a au moins un
    if goalkeepers:
        selected_goalkeeper = random.choice(goalkeepers)
        enemy_deck.append(selected_goalkeeper)
    else:
        selected_goalkeeper = None  # au cas où tu veux le réutiliser plus tard

    # Exclure les gardiens du reste du tirage
    remaining_cards = [card for card in all_cards if card not in goalkeepers]

    # Tirer les 10 autres cartes (non-gardiens uniquement)
    selected_deck=[]
    enemy_deck.extend(random.sample(remaining_cards, 10))
    show_cards_for_5_seconds(enemy_deck)

    card_images = {}
    for card_name, card_info in cards.items():
        card_images[card_name] = pygame.image.load(card_info['image']).convert_alpha()

    selecting_deck = True
    scroll_offset = 0
    scroll_speed = 70
    card_positions = []

    team_name = ""
    input_active = False
    input_rect = pygame.Rect(WIDTH // 2 - 150, 20, 300, 40)

    available_cards = list(unlocked_cards.keys())
    if len(available_cards) < 10:
        selected_cards = list(cards.keys())
    else:
        selected_cards = available_cards

    # Tri par rareté
    selected_cards.sort(key=lambda c: rarities.get(cards[c]['rarity'], 0), reverse=True)

    while selecting_deck:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)

        draw_start_screen(background_img8)
        draw_text("Sélectionnez vos 11 cartes (Cliquez pour sélectionner)", WIDTH // 2 - 270, 80, size=32, color=WHITE)

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2 if input_active else 1)
        draw_text(team_name if team_name else "Cliquez pour entrer un nom", input_rect.x + 10, input_rect.y + 10,
                  size=28, color=WHITE if input_active else (180, 180, 180))

        card_positions = []
        card_width, card_height = 165, 220
        card_margin = 80

        for i, card_name in enumerate(selected_cards):
            x = (i % 3) * (card_width + card_margin) + 550
            y = (i // 3) * (card_height + card_margin) + 250 - scroll_offset

            card_img = pygame.transform.scale(card_images[card_name], (card_width, card_height))
            card_rect = card_img.get_rect(center=(x, y))
            screen.blit(card_img, card_rect.topleft)
            card_positions.append(card_rect)

            if card_name in selected_deck:
                pygame.draw.rect(screen, (255, 255, 255), card_rect, 6)

            draw_text_with_background(card_name, x, y + card_height // 2 + 25, color=WHITE, background_color=(0, 0, 0, 128))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if input_rect.collidepoint(x, y):
                    input_active = True
                else:
                    input_active = False

                for i, card_rect in enumerate(card_positions):
                    if card_rect.collidepoint(x, y) and selected_cards[i] not in selected_deck:
                        selected_deck.append(selected_cards[i])

                if len(selected_deck) == 11:
                    selecting_deck = False

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        team_name = team_name[:-1]
                    else:
                        team_name += event.unicode

                if event.key == pygame.K_DOWN:
                    scroll_offset += scroll_speed
                if event.key == pygame.K_UP:
                    scroll_offset -= scroll_speed

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    scroll_offset -= scroll_speed
                elif event.y < 0:
                    scroll_offset += scroll_speed

    show_scores_and_winner(selected_deck, enemy_deck, team_name)






import random

def calculate_team_scores(player_deck, enemy_deck):
    # Initialisation des scores globaux
    player_attack = sum(cards[card]["attack"] for card in player_deck)
    player_defense = sum(cards[card]["defense"] for card in player_deck)

    enemy_attack = sum(cards[card]["attack"] for card in enemy_deck)
    enemy_defense = sum(cards[card]["defense"] for card in enemy_deck)

    # Atténuation de l'attaque du joueur et boost de l'attaque adverse
    player_score = max(0, player_attack - enemy_defense)
    enemy_score = max(0, enemy_attack + 10 - player_defense)

    # Ajout du bonus de rareté
    rarity_score = {
        "commun": 10,
        "rare": 20,
        "épique": 30,
        "mythique": 40,
        "légendaire": 50,
        "ICON" : 80,
        "cr" : 50,
        "BO" : 70,
        "EAC" : 50,
        "fu" : 50,
        "fl" : 50,
        "vi" : 50,
        "TOTY" : 60
    }

    player_score += sum(rarity_score[cards[card]["rarity"]] for card in player_deck)
    enemy_score += sum(rarity_score[cards[card]["rarity"]] for card in enemy_deck)

    # Pénalité si la défense est trop faible
    if player_defense < player_attack * 0.7:
        player_score -= 500  # Pénalité si l'équipe est trop offensive

    # Bonus caché pour l'adversaire
    enemy_score += random.randint(100, 200)

    return round(player_score,1), round(enemy_score,1)






def show_cards_for_5_seconds(cards_to_show):
    start_time = pygame.time.get_ticks()
    num_cards = len(cards_to_show)
    card_width = 165
    card_height = 220
    spacing = 20  # Espace entre les cartes

    # Calcul du nombre de cartes par ligne
    num_cards_first_row = (num_cards + 1) // 2  # Première ligne a +1 si impair
    num_cards_second_row = num_cards // 2  # Deuxième ligne a le reste

    # Centrage des lignes
    total_width_first_row = num_cards_first_row * (card_width + spacing) - spacing
    total_width_second_row = num_cards_second_row * (card_width + spacing) - spacing

    start_x_first_row = (WIDTH - total_width_first_row) // 2
    start_x_second_row = (WIDTH - total_width_second_row) // 2

    while pygame.time.get_ticks() - start_time < 5000:  # Affichage pendant 5 secondes
        draw_start_screen(background_img8)

        for i, card_name in enumerate(cards_to_show):
            # Déterminer la ligne et la position
            if i < num_cards_first_row:
                x = start_x_first_row + i * (card_width + spacing)
                y = HEIGHT // 2 - card_height - 20  # Légèrement remonté
            else:
                x = start_x_second_row + (i - num_cards_first_row) * (card_width + spacing)
                y = HEIGHT // 2 + 20  # Un peu d'écart entre les deux lignes

            # Affichage de la carte
            card_image_path = cards[card_name]["image"]  # Récupérer le chemin de l'image
            card_img = pygame.image.load(card_image_path)  # Charger l'image en tant que Surface
            card_img = pygame.transform.scale(card_img, (card_width, card_height))  # Redimensionner l'image

            card_rect = card_img.get_rect(center=(x + card_width // 2, y + card_height // 2))
            screen.blit(card_img, card_rect.topleft)

            # Affichage du nom centré sous la carte
            draw_text_centered(card_name, x + card_width // 2, y + card_height + 15, size=30, color=WHITE)

        # Titre en haut
        draw_text_centered("Equipe de l'adversaire", WIDTH // 2, 50, size=64, color=WHITE)

        pygame.display.flip()
        pygame.time.delay(100)  # Petite pause pour la fluidité







def show_scores_and_winner(selected_deck, enemy_deck, team_name):
    global money
    # Calcul des scores
    score_team_1, score_team_2 = calculate_team_scores(selected_deck, enemy_deck)

    # Déterminer le vainqueur avec couleur dynamique
    if score_team_1 > score_team_2:
        winner_text = "Vous avez gagné !"
        color = (0, 255, 0)  # Vert pour victoire
        money += 1500; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
    elif score_team_2 > score_team_1:
        winner_text = "Vous avez perdu..."
        color = (255, 0, 0)  # Rouge pour défaite
        money += 50; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV
    else:
        winner_text = "Match nul !"
        color = (255, 255, 0)  # Jaune pour égalité
        money += 800; update_money_in_csv('money.csv', money)  # Ajoute 10€ à l'argent et met à jour le CSV 

    # Appliquer le fond d'écran
    draw_start_screen(background_img2)

    # Ajout d’un rectangle semi-transparent pour l'affichage des scores
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  
    screen.blit(overlay, (0, 0))

    # Fonction pour afficher le texte centré
    def draw_centered_text(text, x, y, size, color):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # Affichage progressif du score et du vainqueur
    if team_name == "":
        team_name = "Invité"

    pygame.display.flip()
    pygame.time.delay(500)  # Pause avant l'affichage des scores

    draw_centered_text(f"Score de {team_name} : {score_team_1}", WIDTH // 2, HEIGHT // 2 - 80, 36, WHITE)
    pygame.display.flip()
    pygame.time.delay(500)

    draw_centered_text(f"Score de l'ennemi : {score_team_2}", WIDTH // 2, HEIGHT // 2 - 40, 36, WHITE)
    pygame.display.flip()
    pygame.time.delay(500)

    draw_centered_text(winner_text, WIDTH // 2, HEIGHT // 2 + 30, 48, color)
    pygame.display.flip()

    # Ajout d'un bouton "Retour au menu"
    button_x = WIDTH // 2 - 100
    button_y = HEIGHT // 2 + 80
    draw_button(button_x, button_y, 200, 50, "Retour au menu")

    pygame.display.flip()

    # Attente d'un événement
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_x <= x <= button_x + 200 and button_y <= y <= button_y + 50:
                    waiting = False  # Retour au menu



def calculate_score(rarity):
    score_map = {
        "commun": 10,
        "rare": 20,
        "épique": 30,
        "mythique": 40,
        "légendaire": 50,
        "ICON" : 80,
        "cr" : 50,
        "BO" : 70,
        "EAC" : 50,
        "fu" : 50,
        "fl" : 50,
        "vi" : 50,
        "TOTY" : 60
    }
    return score_map.get(rarity, 0)


#-------------------------------#
#          entrainement         #
#-------------------------------#



# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# Paramètres du joueur
PLAYER_RADIUS = 20
PLAYER_SPEED = 3

# Paramètres du ballon
BALL_RADIUS = 15
FRICTION = 0.98 
SHOOT_DISTANCE = PLAYER_RADIUS + BALL_RADIUS + 20  # Distance max pour tirer


SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
GOAL_OFFSET = 100  # Distance supplémentaire depuis le bord
GOAL_BORDER_WIDTH = 10
GOAL_WIDTH = 100  # Ajuste si besoin
GOAL_HEIGHT = 200
GOAL_LEFT = (0, SCREEN_HEIGHT // 2 - GOAL_HEIGHT // 2)  # But collé à gauche
GOAL_RIGHT = (SCREEN_WIDTH - GOAL_WIDTH, SCREEN_HEIGHT // 2 - GOAL_HEIGHT // 2)  # But collé à droite


# Variables de score
score_left = 0
score_right = 0
font = pygame.font.SysFont("Arial", 40)
match_time = 0  # Temps écoulé en secondes
font_small = pygame.font.SysFont("Arial", 30)

def draw_score():
    score_text = font.render(f"{score[0]} - {score[1]}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    # Affichage du temps sous forme mm:ss
    minutes = int(match_time) // 60
    seconds = int(match_time) % 60
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, WHITE)
    screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 60))

    

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roulette_active = False
        self.roulette_angle = 0  # Angle pour la rotation autour du ballon
        self.roulette_timer = 0  # Compteur pour la durée de la roulette

    def move(self, keys, left, right, up, down):
        if not self.roulette_active:
            # Déplacement classique du joueur
            if keys[left]:
                self.x -= PLAYER_SPEED
            if keys[right]:
                self.x += PLAYER_SPEED
            if keys[up]:
                self.y -= PLAYER_SPEED
            if keys[down]:
                self.y += PLAYER_SPEED

            # Contrainte des limites de l'écran
            self.x = max(PLAYER_RADIUS, min(SCREEN_WIDTH - PLAYER_RADIUS, self.x))
            self.y = max(PLAYER_RADIUS, min(SCREEN_HEIGHT - PLAYER_RADIUS, self.y))
        else:
            # Rotation autour du ballon lorsque la roulette est active
            if self.roulette_timer > 0:
                self.roulette_timer -= 1
                # Calcul de la nouvelle position en utilisant l'angle de roulette
                self.x = ball.x + math.cos(self.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
                self.y = ball.y + math.sin(self.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
                
                # Mise à jour de l'angle de rotation (rotation dans le sens horaire ou antihoraire)
                self.roulette_angle += 0.05  # Ajuste la vitesse de rotation ici (plus petit pour plus lent)
                if self.roulette_angle >= 2 * math.pi:
                    self.roulette_angle -= 2 * math.pi  # Recommence après un tour complet

            else:
                self.roulette_active = False  # Arrêter la roulette après le timer
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.curve = 0
        self.curve_target = 0
        self.curve_distance = 0

    def move(self):
        # Si un joueur tourne autour, le ballon ne bouge pas
        if player1.roulette_active or player2.roulette_active:
            self.vel_x = 0
            self.vel_y = 0
        else:
            self.x += self.vel_x
            self.y += self.vel_y

            if self.curve_distance > 0:
                self.vel_x += self.curve
                self.curve_distance -= math.hypot(self.vel_x, self.vel_y)
                if self.curve_distance <= 0:
                    self.curve = 0

            self.vel_x *= FRICTION
            self.vel_y *= FRICTION

            # Gestion des rebonds
            if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > SCREEN_WIDTH:
                self.vel_x = -self.vel_x * 0.7
                self.x = max(BALL_RADIUS, min(SCREEN_WIDTH - BALL_RADIUS, self.x))
            if self.y - BALL_RADIUS < 0 or self.y + BALL_RADIUS > SCREEN_HEIGHT:
                self.vel_y = -self.vel_y * 0.7
                self.y = max(BALL_RADIUS, min(SCREEN_HEIGHT - BALL_RADIUS, self.y))


    
    def check_collision(self, player1, player2):
        # Collision avec le joueur 1 (Rouge)
        distance1 = math.hypot(self.x - player1.x, self.y - player1.y)
        if distance1 < PLAYER_RADIUS + BALL_RADIUS:
            # Calculer l'angle de collision
            angle = math.atan2(self.y - player1.y, self.x - player1.x)
            # Repousser légèrement le ballon vers l'extérieur
            self.vel_x = math.cos(angle) * 5
            self.vel_y = math.sin(angle) * 5
        
        # Collision avec le joueur 2 (Bleu)
        distance2 = math.hypot(self.x - player2.x, self.y - player2.y)
        if distance2 < PLAYER_RADIUS + BALL_RADIUS:
            # Calculer l'angle de collision
            angle = math.atan2(self.y - player2.y, self.x - player2.x)
            # Repousser légèrement le ballon vers l'extérieur
            self.vel_x = math.cos(angle) * 5
            self.vel_y = math.sin(angle) * 5

        # Lorsque les deux joueurs sont proches du ballon et qu'il est entre eux
        if distance1 < PLAYER_RADIUS + BALL_RADIUS and distance2 < PLAYER_RADIUS + BALL_RADIUS:
            # Calculer la position centrale entre les deux joueurs
            center_x = (player1.x + player2.x) / 2
            center_y = (player1.y + player2.y) / 2
            # Calculer l'angle du ballon par rapport au centre
            angle_to_center = math.atan2(self.y - center_y, self.x - center_x)

            # Repousser le ballon perpendiculairement à la ligne entre les deux joueurs
            self.vel_x = math.cos(angle_to_center + math.pi / 2) * 5
            self.vel_y = math.sin(angle_to_center + math.pi / 2) * 5




    
    def shoot(self, player, curve_direction=0):
        print(f"Tir tenté par {('Rouge' if player == player1 else 'Bleu')} !")
        distance = math.hypot(self.x - player.x, self.y - player.y)
        if distance <= SHOOT_DISTANCE:
            angle = math.atan2(self.y - player.y, self.x - player.x)
            self.vel_x += math.cos(angle) * 10
            self.vel_y += math.sin(angle) * 10

            # Ajout de l'effet d'enroulé
            if curve_direction != 0:
                self.curve = curve_direction * 0.3  # Courbure (valeur ajustable)
                self.curve_distance = 700  # Distance sur laquelle l'effet agit

            print(f"Tir effectué avec effet {'gauche' if curve_direction < 0 else 'droite'} par {('Rouge' if player == player1 else 'Bleu')} !")


def init_game():
    global player1, player2, ball, score
    player1 = Player(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)
    player2 = Player(SCREEN_WIDTH * 2 // 3, SCREEN_HEIGHT // 2)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    score = [0, 0]

def handle_input():
    keys = pygame.key.get_pressed()

    # Mouvement des joueurs
    player1.move(keys, pygame.K_q, pygame.K_d, pygame.K_z, pygame.K_s)  # Joueur 1 (rouge)
    player2.move(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)  # Joueur 2 (bleu)

    # Gestion des enroulés pour le joueur 1 (rouge)
    if keys[pygame.K_a] and math.hypot(ball.x - player1.x, ball.y - player1.y) < PLAYER_RADIUS + BALL_RADIUS + 10:
        ball.shoot(player1, -1)  # Enroulé à gauche
    if keys[pygame.K_e] and math.hypot(ball.x - player1.x, ball.y - player1.y) < PLAYER_RADIUS + BALL_RADIUS + 10:
        ball.shoot(player1, 1)  # Enroulé à droite

    # Gestion des enroulés pour le joueur 2 (bleu)
    if keys[pygame.K_KP4] and math.hypot(ball.x - player2.x, ball.y - player2.y) < PLAYER_RADIUS + BALL_RADIUS + 10:
        ball.shoot(player2, -1)  # Enroulé à gauche
    if keys[pygame.K_KP6] and math.hypot(ball.x - player2.x, ball.y - player2.y) < PLAYER_RADIUS + BALL_RADIUS + 10:
        ball.shoot(player2, 1)  # Enroulé à droite

    # Tir normal pour le joueur 1 (rouge) si pas en roulette
    if not player1.roulette_active and keys[pygame.K_SPACE]:  # Tir normal
        ball.shoot(player1)

    # Tir normal pour le joueur 2 (bleu) si pas en roulette
    if not player2.roulette_active and keys[pygame.K_SPACE]:  # Tir normal
        ball.shoot(player2)

    # Gestion de la roulette pour le joueur 1 (rouge)
    if keys[pygame.K_r] and math.hypot(ball.x - player1.x, ball.y - player1.y) < PLAYER_RADIUS + BALL_RADIUS + 20:
        player1.roulette_active = True
        player1.roulette_timer = 5  # Durée de la roulette
        player1.roulette_angle = math.atan2(player1.y - ball.y, player1.x - ball.x)

    # Gestion de la roulette pour le joueur 2 (bleu)
    if keys[pygame.K_KP0] and math.hypot(ball.x - player2.x, ball.y - player2.y) < PLAYER_RADIUS + BALL_RADIUS + 20:
        player2.roulette_active = True
        player2.roulette_timer = 5  # Durée de la roulette
        player2.roulette_angle = math.atan2(player2.y - ball.y, player2.x - ball.x)

    # Mouvement de la roulette (rotation autour du ballon) pour le joueur 1
    if player1.roulette_active:
        if player1.roulette_timer > 0:
            player1.roulette_timer -= 1
            player1.x = ball.x + math.cos(player1.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
            player1.y = ball.y + math.sin(player1.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
            player1.roulette_angle += 0.05  # Ajuste la vitesse de rotation
        else:
            player1.roulette_active = False  # Arrêter la roulette après le timer

    # Mouvement de la roulette (rotation autour du ballon) pour le joueur 2
    if player2.roulette_active:
        if player2.roulette_timer > 0:
            player2.roulette_timer -= 1
            player2.x = ball.x + math.cos(player2.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
            player2.y = ball.y + math.sin(player2.roulette_angle) * (PLAYER_RADIUS + BALL_RADIUS + 10)
            player2.roulette_angle += 0.05  # Ajuste la vitesse de rotation
        else:
            player2.roulette_active = False  # Arrêter la roulette après le timer




        
        


def update_game():
    global match_time
    ball.move()
    ball.check_collision(player1, player2)
    print("Ball position:", ball.x, ball.y)  # Vérifier où est la balle en temps réel
    check_goal()
    match_time += 1/60  # Ajoute 1/60ème de seconde à chaque frame (60 FPS)
    for player in [player1, player2]:
        if player.roulette_active and player.roulette_timer > 0:
            player.roulette_angle += 0.2  # Tourne autour du ballon
            distance = PLAYER_RADIUS + BALL_RADIUS + 5  # Distance fixe autour du ballon
            player.x = ball.x + math.cos(player.roulette_angle) * distance
            player.y = ball.y + math.sin(player.roulette_angle) * distance
            player.roulette_timer -= 1
        else:
            player.roulette_active = False  # Désactive la roulette








def check_goal():
    global score
    print(f"check_goal appelé - Balle: x={ball.x}, y={ball.y}")

    if ball.x - BALL_RADIUS <= 0 and GOAL_LEFT[1] < ball.y < GOAL_LEFT[1] + GOAL_HEIGHT:
        print("But pour le joueur bleu !")
        score[1] += 1
        display_goal_message()
        reset_positions()

    elif ball.x + BALL_RADIUS >= SCREEN_WIDTH and GOAL_RIGHT[1] < ball.y < GOAL_RIGHT[1] + GOAL_HEIGHT:
        print("But pour le joueur rouge !")
        score[0] += 1
        display_goal_message()
        reset_positions()



# SCREEN_WIDTH = pygame.display.Info().current_w
# SCREEN_HEIGHT = pygame.display.Info().current_h
# GOAL_OFFSET = 100  # Distance supplémentaire depuis le bord
# GOAL_BORDER_WIDTH = 10
# GOAL_WIDTH = 100  # Ajuste si besoin
# GOAL_HEIGHT = 200
# GOAL_LEFT = (0, SCREEN_HEIGHT // 2 - GOAL_HEIGHT // 2)  # But collé à gauche
# GOAL_RIGHT = (SCREEN_WIDTH - GOAL_WIDTH, SCREEN_HEIGHT // 2 - GOAL_HEIGHT // 2)  # But collé à droite



def reset_ball():
    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2
    ball.vel_x = 0
    ball.vel_y = 0
    ball.curve = 0  # Réinitialisation de la courbure
    ball.curve_distance = 0  # Empêche tout effet d'enroulé au prochain mouvement
    pygame.time.delay(500)  # Petite pause avant l'engagement



def update_ball(ball):
    """ Met à jour la position et les rebonds de la balle. """
    print(f"Avant update: x={ball.x}, y={ball.y}, vel_x={ball.vel_x}, vel_y={ball.vel_y}, spin={ball.spin}")
    ball.x += ball.vel_x
    ball.y += ball.vel_y

    # Rebond contre le haut et le bas
    if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
        ball.vel_y *= -1
        normalize_velocity(ball)  # Évite les rebonds étranges
    print(f"Après update: x={ball.x}, y={ball.y}, vel_x={ball.vel_x}, vel_y={ball.vel_y}, spin={ball.spin}")
        


def normalize_velocity(ball):
    speed = math.sqrt(ball.vel_x ** 2 + ball.vel_y ** 2)
    if speed > 0:  
        factor = 5 / speed  # Garde une vitesse constante de 5 (ajuste si nécessaire)
        ball.vel_x *= factor
        ball.vel_y *= factor
        
def draw_game():
    draw_start_screen(terrain)
    #draw_goals()
    pygame.draw.circle(screen, RED, (int(player1.x), int(player1.y)), PLAYER_RADIUS)
    pygame.draw.circle(screen, BLUE, (int(player2.x), int(player2.y)), PLAYER_RADIUS)
    pygame.draw.circle(screen, WHITE, (int(ball.x), int(ball.y)), BALL_RADIUS)
    draw_score()
    draw_menu_button()
    pygame.display.flip()


def draw_menu_button():
    text = font.render("Menu", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - 135, 30))

def handle_menu_click(pos):
    if SCREEN_WIDTH - 150 <= pos[0] <= SCREEN_WIDTH - 20 and 20 <= pos[1] <= 70:
        main_menu()

def display_goal_message():
    goal_text = font.render("BUT!", True, WHITE)
    screen.blit(goal_text, (SCREEN_WIDTH // 2 - goal_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(3000)

def reset_positions():
    player1.x, player1.y = SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2
    player2.x, player2.y = SCREEN_WIDTH * 2 // 3, SCREEN_HEIGHT // 2

    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2
    ball.vel_x = 0
    ball.vel_y = 0
    ball.curve = 0  # Supprime tout effet d'enroulé
    ball.curve_distance = 0  # Empêche la balle de tourner seule

    pygame.time.delay(1000)  # Pause avant la reprise

def run_game():
    global money, last_income_time  # Ajoute money ici
    last_income_time = time.time()
    t = 0
    purchased_annonces = load_purchased_annonces('purchased_annonces.csv')
    
    init_game()  # Initialise le jeu
    running = True
    clock = pygame.time.Clock()
    
    # Commence avec la balle au centre et arrêtée
    reset_positions()

    while running:
        t += 0.01
        if t >= 2:
            t = 0
            print("t=10!")
            for annonce in purchased_annonces:
                if annonce['category'] == "Entreprises":
                    if annonce['name'] == "AirFrance":
                        money += 4756000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Paris SG":
                        money += 128000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "La Bonne Fournée":
                        money += 1000
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Lutti":
                        money += 2300
                        update_money_in_csv('money.csv', money)
                    if annonce['name'] == "Salon de coiffure":
                        money += 150
                        update_money_in_csv('money.csv', money)
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(event.pos)
        
        handle_input()  # Gère les entrées du joueur
        update_game()  # Met à jour la logique du jeu (mouvement des joueurs, de la balle, etc.)
        draw_game()  # Dessine la scène
        clock.tick(60)  # Limite à 60 images par seconde



main_menu()