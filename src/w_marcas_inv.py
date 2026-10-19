# -*- coding: utf-8 -*-
"""Inventario de marcas, personajes y titulos con copyright que siguen vivos
en lo publicado. No sustituye nada: solo busca y ensena el contexto, para
decidir caso por caso."""
import io, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PROD = [('Juego', 'out3/art/juego.html'),
        ('Acelerado', 'out3/art/acelerado.html'),
        ('La Idea', 'out3/art/tesis.html'),
        ('App', 'out3/nogum_app.html')]

SOSPECHOSOS = {
 'Rol y editoriales': [
   'D&D', 'Dungeons', 'Calabozos y Dragones', 'Pathfinder', 'Warhammer', 'Shadowrun',
   'Vampiro: la Mascarada', 'Vampire: the Masquerade', 'Mundo de Tinieblas', 'World of Darkness',
   'Call of Cthulhu', 'La Llamada de Cthulhu', 'Traveller', 'Cyberpunk 2020', 'Cyberpunk 2077',
   'Blades in the Dark', 'Dungeon World', 'Numenera', 'Cypher', 'Genesys', 'Nosolorol',
   'Paizo', 'Wizards of the Coast', 'Chaosium', 'Evil Hat', 'Steve Jackson'],
 'Fantasia': [
   'Tolkien', 'Gandalf', 'Frodo', 'Sauron', 'Mordor', 'Hobbit', 'Rivendel', 'Rivendell',
   'Conan', 'Cimmeri', 'Elric', 'Drizzt', 'Reinos Olvidados', 'Forgotten Realms',
   'Geralt', 'Brujo de Rivia', 'Witcher', 'Skyrim', 'Elder Scrolls', 'Hogwarts',
   'Harry Potter', 'Narnia', 'Terramar', 'Earthsea'],
 'Ciencia ficcion': [
   'Star Wars', 'La Guerra de las Galaxias', 'Jedi', 'Sith', 'Darth', 'Vader',
   'Estrella de la Muerte', 'Death Star', 'Halcón Milenario', 'Millennium Falcon',
   'Star Trek', 'Spock', 'Enterprise', 'Klingon', 'Dune', 'Arrakis', 'Fremen',
   'Blade Runner', 'Replicante', 'Alien', 'Xenomorfo', 'Nostromo', 'Ripley',
   'Matrix', 'Neo', 'Terminator', 'Skynet', 'Neuromante', 'Gibson', 'Fallout',
   'Mad Max', 'Vault', 'Doctor Who', 'TARDIS', 'Firefly', 'Battlestar'],
 'Anime y manga': [
   'Dragon Ball', 'Goku', 'Vegeta', 'Piccolo', 'Námek', 'Namek', 'Saiyan', 'Saiyajin',
   'guerreros Z', 'Z Warriors', 'Naruto', 'One Piece', 'Akira', 'Evangelion', 'EVA-01',
   'Gundam', 'Sailor Moon', 'Death Note', 'Shingeki', 'Titan', 'JoJo', 'Pokémon',
   'Caballeros del Zodiaco', 'Saint Seiya', 'Bola de Dragón'],
 'Superheroes': [
   'Marvel', 'DC Comics', 'Batman', 'Superman', 'Spider', 'Hombre Araña', 'Iron Man',
   'Thanos', 'Gema del Infinito', 'Infinity Stone', 'Vengadores', 'Avengers',
   'Liga de la Justicia', 'Justice League', 'X-Men', 'Patrulla-X', 'Watchmen',
   'Homelander', 'Patria', 'Kryptonita', 'Kryptonite', 'Batmóvil', 'Batmobile',
   'Capa de Levitación', 'Cloak of Levitation', 'Mjolnir', 'Thor', 'Hulk'],
 'Terror': [
   'Cthulhu', 'Lovecraft', 'Necronomic', 'Innsmouth', 'Arkham', 'Miskatonic',
   'Freddy Krueger', 'Jason Voorhees', 'Michael Myers', 'Hellraiser', 'Cenobita',
   'Evil Dead', 'Resident Evil', 'Silent Hill', 'Dracón', 'Drácula', 'Dracula',
   'Frankenstein', 'Van Helsing'],
 'Cine y TV': [
   'Indiana Jones', 'James Bond', '007', 'John Wick', 'Jungla de Cristal', 'Die Hard',
   'Kill Bill', 'Pulp Fiction', 'Tarantino', 'Breaking Bad', 'Los Soprano', 'The Wire',
   'Stranger Things', 'Juego de Tronos', 'Game of Thrones', 'Mundodisco', 'Discworld',
   'Pratchett', 'Regreso al futuro', 'Back to the Future', 'DeLorean', 'Jurassic'],
}

hall = []
for nom, ruta in PROD:
    if not os.path.exists(ruta):
        print('FALTA', ruta); continue
    s = io.open(ruta, encoding='utf-8').read()
    if nom == 'App':
        s = re.sub(r'<script type="application/json" id="canon">.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<template id="src-en">.*?</template>', '', s, flags=re.S)
    t = re.sub(r'</?(?:p|li|td|th|tr|div|h[1-6]|section|table|dt|dd)\b[^>]*>', '\n', s)
    t = re.sub(r'<[^>]+>', ' ', t)
    for cat, lista in SOSPECHOSOS.items():
        for m in lista:
            W = r'A-Za-zà-ÿ'
            for g in re.finditer(r'(?<![%s])%s(?![%s])' % (W, re.escape(m), W), t, re.I):
                ctx = re.sub(r'\s+', ' ', t[max(0, g.start() - 80):g.start() + len(m) + 80]).strip()
                hall.append((cat, m, nom, ctx))

print('=' * 72)
print(' MARCAS Y PERSONAJES QUE SIGUEN EN LO PUBLICADO')
print('=' * 72)
if not hall:
    print('  ninguno de la lista.')
vistos = set()
for cat, m, nom, ctx in hall:
    k = (m, nom, ctx[:60])
    if k in vistos:
        continue
    vistos.add(k)
    print('\n[%s] %-22s (%s)' % (cat, m, nom))
    print('   ...%s...' % ctx)
print()
print('total de apariciones distintas: %d' % len(vistos))
