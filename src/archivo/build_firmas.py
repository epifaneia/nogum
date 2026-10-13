# -*- coding: utf-8 -*-
import json, re, os

HERE = os.path.dirname(os.path.abspath(__file__))

# Spanish fixes applied on top of the author's text (old -> new)
FIXES = [
    ("carrerotes prolongadas", "carreras prolongadas"),
    ("cables o cables de alta tensión", "cables o tendidos de alta tensión"),
    ("enfocados a dormitar", "enfocados a dormir"),
    ("Breos y Aceites Tácticos", "Ungüentos y Aceites Tácticos"),
    ("documentos oficialistas", "documentos oficiales"),
    ("Copia e insonorización de volúmenes masivos", "Copia y extracción silenciosa de volúmenes masivos"),
    ("frecuencias radio", "frecuencias de radio"),
]

# English per discipline, in file order: list of (name, description)
EN = {
"Atletismo": ("Athletics", [
 ("Marathon / Endurance", "Holding the pace over long runs without building up fatigue."),
 ("Impossible Leap", "Clearing vertical or horizontal gaps at the very limit."),
 ("Free Climbing", "Scaling vertical surfaces quickly, with no harness or gear."),
 ("Extreme Swimming", "Moving and manoeuvring through rough water, currents or under pressure."),
 ("Reflex Dodge", "Sidesteps and snap cover against projectiles or impacts."),
]),
"Acrobacia": ("Acrobatics", [
 ("Controlled Fall", "Absorbing or dispersing the impact of falls from great heights."),
 ("Contortionism", "Squeezing through extremely tight spaces or slipping out of bonds."),
 ("Extreme Balance", "Moving steadily along narrow ledges, cables or power lines."),
 ("Flips and Feints", "Aerial moves to change facing in combat or wrong-foot an opponent."),
 ("Urban Parkour", "Flowing over architectural obstacles at top speed."),
]),
"Sigilo": ("Stealth", [
 ("Shadow Cloak", "Moving through the blind spots of lighting and surroundings."),
 ("Silent Movement", "Muffling footsteps on any surface (glass, wood, metal)."),
 ("Mimicry / Cover", "Staying motionless, blending the body's outline into the scenery."),
 ("Zero Trace", "Moving without leaving footprints, scents or any disturbance behind."),
 ("Shadowing", "Tailing and stalking targets at close range without being spotted."),
]),
"Juego de Manos": ("Sleight of Hand", [
 ("Light Fingers (Pickpocket)", "Lifting or planting objects in someone's pockets or kit without them noticing."),
 ("Card Tricks / Cheating", "Physically rigging dice, cards or other small games of chance."),
 ("Quick Disarm", "Mechanically disabling or snatching a weapon from an unwary foe."),
 ("Body Concealment", "Hiding small tools, keys or weapons in clothing or against the skin."),
 ("Lockpicking", "Opening and manipulating traditional mechanical locks."),
]),
"Potencia": ("Might", [
 ("Battering Ram / Door Breaker", "Brute force to bring down structures, barricades or doors."),
 ("Heavy Lifting", "Raising and holding massive static loads (beams, vehicles, rubble)."),
 ("Death Grip", "Crushing strength to pin, choke or break holds."),
 ("Heavy Throw", "Hurling heavy objects as improvised projectiles at range."),
 ("Structural Feat", "Holding up ceilings or collapsing loads to buy others time."),
]),
"Entereza": ("Fortitude", [
 ("Pain Tolerance", "Ignoring penalties from wounds, physical pain or torture."),
 ("Toxin Resistance", "Metabolic filtering of poisons, drugs, gases or intoxicants."),
 ("Thermal / Environmental Immunity", "Withstanding extreme temperatures (freezing or heat) or lack of air."),
 ("Cardio-Pulmonary Stamina", "Sustaining physical effort on minimal oxygen (breath-holding)."),
 ("Rapid Stabilisation", "Cutting bleeding time and speeding physiological recovery after trauma."),
]),
"Pelea": ("Brawling", [
 ("Throws and Locks", "Using an opponent's strength for takedowns, throws or joint locks."),
 ("Boxing / Heavy Blows", "Direct strikes (fists, elbows) aimed to knock out or cause trauma."),
 ("Street / Dirty Fighting", "Using the surroundings, biting, headbutts and blows to soft spots."),
 ("Tactical Submission", "Holds meant to put someone to sleep or subdue them without lasting harm."),
 ("Block and Absorb", "Positioning the body to reduce damage from unarmed strikes."),
]),
"Armas": ("Weapons", [
 ("Short Blades / Daggers", "Wielding knives, daggers, katanas or other fast-striking blades."),
 ("Blunt / Heavy Weapons", "Maces, hammers, greatswords, axes and other high-momentum weapons."),
 ("Polearms", "Controlling distance with spears, halberds, staves and poles."),
 ("Light Firearms", "Accurate shooting with pistols, revolvers and submachine guns at close range."),
 ("Precision / Ranged Weapons", "Handling sniper rifles, bows, crossbows or heavy projectiles."),
]),
"Ciencias": ("Sciences", [
 ("Theoretical and Applied Physics", "Calculating trajectories, impact vectors, ballistics and gravity."),
 ("Chemistry and Pharmacology", "Analysing and creating compounds, poisons, explosives and antidotes."),
 ("Biology and Anatomy", "Knowing the body's structure to find weak points or to heal."),
 ("Mathematics and Cryptography", "Cracking analogue codes, algorithms and complex patterns."),
 ("Geology and Earth Sciences", "Reading strata, ground stability and minerals."),
]),
"Humanidades": ("Humanities", [
 ("History and Precedent", "Analysing past events, historical tactics and lineages."),
 ("Philosophy and Logic", "Spotting fallacies, theoretical debate and structuring arguments."),
 ("Polyglot and Linguistics", "Translation, dialect analysis and deciphering dead languages."),
 ("Sociology and Anthropology", "Understanding social structures, customs and cultural rites."),
 ("Archaeology and Appraisal", "Authenticating, dating and valuing artefacts and relics."),
]),
"Ocultismo": ("Occultism", [
 ("Demonology and Cryptozoology", "Identifying creatures and myths, their weaknesses and behaviour."),
 ("Grimoires and Forbidden Texts", "Reading and interpreting ancient tomes, runes and formulae."),
 ("Esoteric Symbology", "Recognising seals, mystic marks and sacred geometry."),
 ("Prophecies and Omens", "Interpreting auguries, star readings or implied timelines."),
 ("Multiverse Lore", "Knowledge of planes, parallel dimensions and unearthly laws."),
]),
"Actualidad": ("Current Affairs", [
 ("Pop Culture and Trends", "Command of references, street slang and consumer culture."),
 ("Geopolitics and Macroeconomics", "Tracking money flows, corporate markets and political borders."),
 ("Press and Social Media", "Tracing hoaxes, data leaks and real-time information."),
 ("Underworld and Organised Crime", "Knowing the gangs, smuggling routes and street codes."),
 ("Bureaucracy and Local Law", "Navigating red tape, corporate regulations and legal loopholes."),
]),
"Investigación": ("Investigation", [
 ("Scene Deduction", "Reconstructing events from traces, stains and disarray."),
 ("Technical Interrogation", "Extracting information by cross-checking contradictions and applying logical pressure."),
 ("Forensic Analysis", "On-site visual examination of wounds, causes of death and samples."),
 ("Connecting the Dots", "Finding patterns or common threads between unrelated data."),
 ("Records Search", "Quickly tracking down specific information in physical or digital archives."),
]),
"Alerta": ("Alertness", [
 ("Ambush Sense", "Reading the surroundings to detect imminent danger or ambushes."),
 ("Body Reading", "Spotting micro-expressions, nerves or lies in real time."),
 ("Trap Detection", "Locating sensors, tripwires, mechanisms or mines before they go off."),
 ("Auditory Focus", "Filtering out background noise to catch distant conversations or footsteps."),
 ("Perimeter Awareness", "Keeping a mental map of where everything around you is."),
]),
"Táctica": ("Tactics", [
 ("Ambushes and Enfilades", "Planning and springing surprise attacks from a positional advantage."),
 ("Reading the Ground", "Quickly identifying hard cover, choke points and escape routes."),
 ("Squad Coordination", "Optimising combined attacks and suppressing fire with allies."),
 ("Anticipating Mistakes", "Predicting enemy moves from their combat patterns."),
 ("Tactical Retreat", "Organising regroups or evacuations without taking losses on the way out."),
]),
"Supervivencia": ("Survival", [
 ("Tracking", "Following footprints, broken plants or trails in natural or urban settings."),
 ("Foraging", "Finding drinking water, safe food and makeshift shelter."),
 ("Navigation / Orienteering", "Finding your way without maps or compass (by stars, terrain or weather)."),
 ("Field First Aid", "Tourniquets, cauterisation and emergency stabilisation without an operating theatre."),
 ("Hunting Traps", "Building improvised snares, holding pens or alarms."),
]),
"Persuasión": ("Persuasion", [
 ("Dialectical Oratory", "Winning over groups or audiences with structured arguments and facts."),
 ("Tactical Negotiation", "Securing deals, trades and mutually beneficial pacts."),
 ("Moral Appeal", "Playing on the other party's sense of guilt, duty or ethics."),
 ("Crisis Diplomacy", "Verbally de-escalating tense situations or imminent conflict."),
 ("Aligned Interests", "Convincing a third party that your goals match their own."),
]),
"Engaño": ("Deception", [
 ("Impersonation", "Passing yourself off as someone else through clothing, voice and manner."),
 ("Alibi Building", "Inventing and sustaining complex lies that stand up to scrutiny."),
 ("Verbal Obfuscation / Gaslighting", "Confusing a rival until they doubt their own facts or perception."),
 ("Forgery", "Creating or altering passes, credentials and official documents."),
 ("Tactical Distraction", "Diverting attention or raising false alarms through a dramatic performance."),
]),
"Empatía": ("Empathy", [
 ("Reading Intentions", "Sensing the target's underlying emotional state and true motives."),
 ("Soothing Tempers", "Easing stress, hysteria or hostility in an agitated person."),
 ("Finding Weak Spots", "Identifying a target's fears, hang-ups or secret desires."),
 ("Emotional Validation", "Building instant trust by showing complete understanding."),
 ("Group Dynamics", "Working out who is in charge, who is suffering and who is the weak link in a group."),
]),
"Seducción": ("Seduction", [
 ("Magnetic Allure", "Stirring fascination or desire through presence, charisma and body language."),
 ("Easy Charm", "Winning strangers over instantly in relaxed or festive settings."),
 ("Cry for Help", "Projecting vulnerability so that others step in as protectors or allies."),
 ("Tactical Flirting", "Coaxing out information or small favours through innuendo or coquetry."),
 ("Calculated Flattery", "Working the other person's ego with well-aimed compliments."),
]),
"Liderazgo": ("Leadership", [
 ("Rallying Cry", "Granting bonuses or keeping allies' morale up in moments of crisis."),
 ("Command and Discipline", "Giving direct orders that are carried out without hesitation when it counts."),
 ("Role Assignment", "Coordinating a team by handing out tasks to suit each member's strengths."),
 ("Keeping Order", "Preventing panic, rout or insubordination within a group."),
 ("Leading by Example", "Heading the charge so that others push past their own limits or fears."),
]),
"Intimidación": ("Intimidation", [
 ("Physical Coercion / Open Violence", "A direct show of force to cow people and impose silence."),
 ("Cold Pressure / Veiled Threat", "Hinting at dire consequences without raising your voice or losing your composure."),
 ("Commanding Presence", "Using size, posture or stare to make a rival feel small."),
 ("Psychological Torture", "Breaking a captive's will through deprivation or sustained attrition."),
 ("Mass Intimidation", "Terrifying a crowd or large group with a single gesture or warning."),
]),
"Contactos": ("Contacts", [
 ("Underground Network / Criminal Circles", "Finding informants, fences and mercenaries in the underworld."),
 ("Corporate / Institutional Elite", "Links to executives, diplomats and senior government officials."),
 ("Calling in Favours", "Collecting old debts to secure shelter, gear or safe passage."),
 ("Street Informant Network", "Picking up rumours and fresh intel on the streets via beggars or cabbies."),
 ("VIP Access / Safe-Conducts", "Getting into restricted areas by dropping the names of patrons or referees."),
]),
"Recursos": ("Resources", [
 ("Cash Injection", "Immediate funding for costly purchases, bribes or bail."),
 ("Logistics and Supply", "Mobilising warehouses, transport and heavy provisioning."),
 ("Speculation / Laundering", "Managing and hiding financial assets in tax havens or crypto."),
 ("Market Monopoly", "Controlling or cornering a specific resource in a region."),
 ("Unlimited Credit Line", "No-questions-asked spending power in corporate or banking circles."),
]),
"Mecánica": ("Mechanics", [
 ("Emergency Repair", "Patching up engines, structures or broken machinery mid-combat."),
 ("Engine Tuning / Overdrive", "Pushing vehicles or mechanical systems beyond their limits."),
 ("Reverse Engineering", "Taking apart and understanding an unknown or alien mechanism."),
 ("Toolmaking", "Making tools, pulleys or simple mechanisms from scrap or whatever is to hand."),
 ("Structural Sabotage", "Disabling machinery, bridges or lifts by hitting their mechanical weak points."),
]),
"Electrónica": ("Electronics", [
 ("Hotwiring", "Bypassing control panels, ignitions or physical circuits without a code."),
 ("Microchip / Hardware Design", "Building or repairing boards, transmitters and logic components."),
 ("Board Diagnostics", "Spotting voltage faults, short circuits or burnt-out components at a glance."),
 ("Signal Jamming", "Blocking local radio, Wi-Fi, GPS or radar frequencies."),
 ("Analogue Computing / Sensors", "Calibrating and fitting motion sensors, night vision or thermal imaging."),
]),
"Biotecnia": ("Biotech", [
 ("Implants and Prosthetics", "Fitting, maintaining and calibrating cybernetics, prosthetics or bio-augmentations."),
 ("Biomedical Synthesis", "Producing stimulants, combat serums, coagulants or drugs."),
 ("Tissue Culture", "Maintaining biological samples, basic cloning or genetic patches."),
 ("Genetic Engineering", "DNA analysis, sequencing and detection of biological mutations."),
 ("Cyber-Diagnostics", "Detecting cybernetic rejection, neural viruses or organic-hardware incompatibilities."),
]),
"Artesanía": ("Crafting", [
 ("Gunsmithing and Tuning", "Adjusting, servicing and technically modifying firearms or melee weapons."),
 ("Forging and Metallurgy", "Working metals and alloys, armour plating and structural welding."),
 ("Technical / Ballistic Tailoring", "Making reinforced clothing, disguises or suits with thermal or chemical protection."),
 ("Glassblowing and Glass Chemistry", "Making lenses, optical ampoules and reaction vessels."),
 ("Tactical Carpentry", "Putting up barricades, timber fortifications or containment structures."),
]),
"Pilotaje": ("Driving", [
 ("Evasive Driving", "Getaway manoeuvres, drifts and chases in land vehicles."),
 ("Vehicular Ramming", "Using a car or lorry as a weapon against other vehicles or structures."),
 ("Heavy Machinery", "Operating cranes, diggers, bulldozers or industrial lifts."),
 ("Seamanship", "Piloting speedboats, ships or submersibles in extreme conditions."),
 ("Off-Road / All-Terrain", "Crossing desert, mud or broken ground at high speed."),
]),
"Vuelo": ("Flight", [
 ("Air Combat (Dogfight)", "Pursuit, interception and evasion manoeuvres in jets, fighters or combat craft."),
 ("Emergency Landing", "Setting down aircraft, helicopters or modules with dead engines or in pieces."),
 ("Nap-of-the-Earth / Under the Radar", "Flying low to dodge anti-aircraft fire or radar detection."),
 ("Air Insertion", "Parachute jumps (HALO), fast-roping or troop drops."),
 ("VTOL / Drone Handling", "Piloting vertical take-off craft or swarms of flying drones."),
]),
"Sistemas": ("Systems", [
 ("Network Intrusion (Hacking)", "Breaking firewalls to get into private servers or databases."),
 ("Cybersecurity / Defences", "Blocking intrusions in real time and tracing the attacker's IP or origin."),
 ("AI Infiltration", "Tricking, reprogramming or isolating artificial intelligence routines."),
 ("Malware Injection", "Deploying trojans, ransomware or viruses to cripple entire systems."),
 ("Data Exfiltration", "Quietly copying and extracting massive volumes of encrypted data without leaving a log."),
]),
"Seguridad": ("Security", [
 ("Vulnerability Assessment", "Finding the blind spots in a building's patrols, cameras and protocols."),
 ("Biometric Bypass", "Fooling retina, fingerprint or voice-pattern scanners."),
 ("Camera Control / CCTV", "Looping footage, remote shutdown or tampering with alarm sensors."),
 ("Bomb Disposal (EOD)", "Neutralising mines, traps, time bombs or detonators."),
 ("Lockdown Control", "Triggering containment, sealing blast doors and isolating zones."),
]),
"Proyección": ("Projection", [
 ("Energy / Plasma Blast", "A direct ranged discharge of energy (fire, telekinesis, plasma)."),
 ("Astral / Psychic Projection", "Separating consciousness from the body to scout or communicate mentally."),
 ("Kinetic Shockwave", "Releasing a blast wave that repels and knocks down targets all around."),
 ("Focused Emanation", "Channelling energy through the eyes or hands to weaken or paralyse."),
 ("Phantom Double / Illusion", "Creating intangible copies or mental or holographic projections of oneself."),
]),
"Alteración": ("Alteration", [
 ("Physiological Transmutation", "Changing bodily features (claws, scales, bone density, rigidity)."),
 ("Local Elemental Control", "Altering the immediate surroundings (freezing water, lighting fires, moving earth)."),
 ("Fine Telekinesis", "Moving and handling small objects or mechanisms at a distance with the mind."),
 ("Phase Shift / Intangibility", "Making the body partly incorporeal to pass through solids or attacks."),
 ("Metabolic Acceleration", "Boosting reaction and movement speed for a few moments."),
]),
"Adivinación": ("Divination", [
 ("Past Sight (Retrocognition)", "Reading the emotional or historical imprint left on an object or place."),
 ("Immediate Foresight (Precognition)", "Sensing danger or foreseeing an enemy's move a second ahead."),
 ("Aura Reading / Mystic Senses", "Perceiving life energy, power level or hidden intentions."),
 ("Clairaudience / Clairvoyance", "Seeing or hearing distant places without being physically there."),
 ("Empathic Attunement / Telepathy", "Feeling emotions directly or sending thoughts to another mind."),
]),
"Protección": ("Protection", [
 ("Force Shield / Kinetic Barrier", "Generating an energy field that stops physical or thermal impacts."),
 ("Mystic Ward / Cleansing", "Dispelling harmful effects, curses, poisons or mind control."),
 ("Damage Reflection", "Turning part of the impact or energy received straight back on the attacker."),
 ("Ontological Anchor", "Immunity to forced displacement, gravity shifts or warping of space."),
 ("Veiled Path / Unseen", "Becoming imperceptible to mystic senses, radar or arcane scanners."),
]),
"Alquimia": ("Alchemy", [
 ("Transmutation Potions", "Brewing draughts that grant physical abilities or accelerated healing."),
 ("Tactical Salves and Oils", "Corrosive, flammable or paralysing substances applied to weapons or surroundings."),
 ("Reactive Gases and Vapours", "Making grenades or flasks of thick smoke, acid or hallucinogens."),
 ("Power Catalysts", "Preparing reagents that boost the arcane abilities of others."),
 ("Revealing Powders", "Compounds that expose the invisible, magical traces or hidden structures."),
]),
"Invocación": ("Summoning", [
 ("Binding Entities / Familiars", "Calling up a mystic servant or creature for specific tasks."),
 ("Portal Opening / Displacement", "Tearing brief rifts between two points in space or between dimensions."),
 ("Elemental Summoning", "Bringing forth pure manifestations of an element for combat or destruction."),
 ("Calling Lesser Entities", "Conjuring swarms or mooks for distraction or cover."),
 ("Feast / Mystic Provision", "Summoning supplies, sustenance or temporary shelter from outside reality."),
]),
"Encantamiento": ("Enchantment", [
 ("Rune / Glyph Inscription", "Carving seals on doors or floors that trigger as traps or locks."),
 ("Imbue Properties", "Temporarily lending elemental damage or heightened accuracy to a weapon or piece of kit."),
 ("Warding Talismans", "Making portable objects that soak up a single fatal blow or curse."),
 ("Forging Mystic Items", "Permanently binding a magical effect to an item through ritual."),
 ("Zone Sealing", "Shutting down magic, technology or powers within a defined area."),
]),
"Vínculos": ("Bonds", [
 ("Blood Pact / Loyalty", "Forging an unbreakable link with an ally to share resilience or communication."),
 ("Vitality Transfer", "Draining energy or life from a target to heal yourself or an ally."),
 ("Shared Pain Curse", "Linking two enemies so that damage suffered by one is suffered by the other."),
 ("Psychic Anchor / Tracking", "Marking a target to know their exact position, however far away."),
 ("Severing Bonds / Exorcism", "Breaking other people's mystic ties, mental domination or arcane contracts."),
]),
}

src = open(os.path.join(HERE, "firmas_autor.txt"), encoding="utf-8").read()
applied = []
for old, new in FIXES:
    n = src.count(old)
    assert n == 1, (old, n)
    src = src.replace(old, new)
    applied.append((old, new))

out, cur = [], None
for line in src.splitlines():
    line = line.strip()
    if not line:
        continue
    m = re.match(r"Disciplina:\s*(.+)$", line)
    if m:
        cur = {"dis": m.group(1).strip(), "items": []}
        out.append(cur)
        continue
    m = re.match(r"\d\.\s+(.+?):\s+(.+)$", line)
    if m and cur is not None and not line.split(". ", 1)[1].startswith("ÁMBITO"):
        cur["items"].append((m.group(1).strip(), m.group(2).strip()))

result = []
for d in out:
    en_dis, en_items = EN[d["dis"]]
    assert len(d["items"]) == 5 and len(en_items) == 5, d["dis"]
    result.append({
        "dis": [d["dis"], en_dis],
        "items": [{"n": [es[0], en[0]], "d": [es[1], en[1]]} for es, en in zip(d["items"], en_items)],
    })

with open(os.path.join(HERE, "firmas.json"), "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)

# validation
data = json.load(open(os.path.join(HERE, "firmas.json"), encoding="utf-8"))
assert len(data) == 40, len(data)
expected = ["Athletics","Acrobatics","Stealth","Sleight of Hand","Might","Fortitude","Brawling","Weapons",
 "Sciences","Humanities","Occultism","Current Affairs","Investigation","Alertness","Tactics","Survival",
 "Persuasion","Deception","Empathy","Seduction","Leadership","Intimidation","Contacts","Resources",
 "Mechanics","Electronics","Biotech","Crafting","Driving","Flight","Systems","Security",
 "Projection","Alteration","Divination","Protection","Alchemy","Summoning","Enchantment","Bonds"]
assert [o["dis"][1] for o in data] == expected
n = 0
for o in data:
    assert len(o["dis"]) == 2 and all(isinstance(s, str) and s.strip() for s in o["dis"])
    assert len(o["items"]) == 5
    for it in o["items"]:
        for k in ("n", "d"):
            assert len(it[k]) == 2 and all(isinstance(s, str) and s.strip() for s in it[k])
        n += 1
print("OK", len(data), "disciplines,", n, "signatures")
