# -*- coding: utf-8 -*-
"""El contenido de los cuatro formularios: vinetas, polos y motor de escalas."""

# ---------------------------------------------------------------- bloque A
# tablas de preguntas, motor de escalas y funciones de aplicacion
BLOQUE_A = r"""var SECTIONS = [['Universo','Universe'],['Edición','Edition'],['Tono','Tone'],['Peligro','Danger'],['Escala','Scale'],['Resumen','Summary']];

/* ======================= MOTOR DE ESCALAS =======================
   Cada pregunta vale de 1 a 5 y suma en el contador de su sector, que no se
   ensena mientras se contesta. Tres preguntas por sector: dos situaciones muy
   distintas y una frase final que dice en voz alta el extremo alto de la
   escala. Minimo 3, maximo 15. */
var AC = [['Muy en desacuerdo','Strongly disagree'], ['Muy de acuerdo','Strongly agree']];
function Q(v, a, b){ return {v:v, a:a || AC[0], b:b || AC[1]}; }
function banda3(s){ return s <= 7 ? 0 : s <= 10 ? 1 : 2; }
function rung5(s){ return s <= 4 ? 0 : s <= 7 ? 1 : s <= 10 ? 2 : s <= 13 ? 3 : 4; }
function rungGrid(s){ return s <= 6 ? 0 : s <= 9 ? 1 : s <= 12 ? 2 : s <= 14 ? 3 : 4; }
function cuantas(s){ return s <= 5 ? 0 : s <= 8 ? 1 : s <= 11 ? 2 : s <= 13 ? 3 : 4; }
function ans(fid, sid){ return (S.q[fid] && S.q[fid][sid]) || []; }
function setAns(fid, sid, i, v){ S.q[fid] = S.q[fid] || {}; var a = ans(fid, sid).slice(); a[i] = v; S.q[fid][sid] = a; }
function sc(fid, sid){ var a = ans(fid, sid), s = 0, n = 0; a.forEach(function(v){ if (v) { s += v; n++; } }); while (n < 3) { s += 3; n++; } return s; }
function sc1(fid, sid){ return ans(fid, sid)[0] || 0; }
function hecho(fid, sid, n){ var a = ans(fid, sid); for (var i = 0; i < (n || 3); i++) if (!a[i]) return false; return true; }

/* --------------------------------- 1. EL TONO --------------------------------- */
var S_TONO = [
 {id:'opt', k:['El optimismo','Optimism'], qs:[
   Q(['Alguien se descuelga por la fachada y a mitad de bajada descubre que la cuerda no llega. Debajo hay quince metros de nada.',
      'Somebody is rappelling down a façade and halfway down finds the rope is too short. Below there are fifteen metres of nothing.'],
     ['La cuerda no llega y eso es todo lo que hay que saber. Se cae.','The rope is too short and that is all there is to it. They fall.'],
     ['Justo debajo hay un toldo, y detrás del toldo una ventana abierta. Pasan esas cosas.','Right below there is an awning, and behind the awning an open window. Those things happen.']),
   Q(['El plan entero dependía de que el guardia girase la cabeza en el momento justo.',
      'The whole plan depended on the guard turning their head at exactly the right moment.'],
     ['El guardia mira donde le toca mirar, y lo que le toca mirar sois vosotros.','The guard looks where they are supposed to look, and what they are supposed to look at is you.'],
     ['Claro que la gira. Estas cosas salen cuando tienen que salir.','Of course they turn it. These things work out when they need to.']),
   Q(['En vuestras partidas el mundo echa una mano a los protagonistas. La suerte no es neutral: está de su lado, y eso se nota en cuanto alguien toca un dado.',
      'In your games the world lends the protagonists a hand. Luck is not neutral: it is on their side, and you can tell the moment anyone touches a die.'])]},
 {id:'caos', k:['El caos','Chaos'], qs:[
   Q(['Lleváis tres sesiones preparando el golpe. Tenéis planos, horarios y un mapa del alcantarillado dibujado a mano.',
      'You have spent three sessions preparing the job. You have blueprints, timetables and a hand-drawn map of the sewers.'],
     ['Y sale como estaba previsto, porque para eso se prepara un golpe.','And it goes as planned, because that is what preparing a job is for.'],
     ['Y aparece algo que no estaba en ningún plano. Siempre aparece.','And something turns up that was on none of the blueprints. Something always does.']),
   Q(['Una pelea de taberna entre dos borrachos, sin nada importante en juego.',
      'A tavern brawl between two drunks, with nothing important at stake.'],
     ['Gana el más grande de los dos. Es una pelea de taberna.','The bigger of the two wins. It is a tavern brawl.'],
     ['Acaba con el techo en el suelo, un cerdo suelto y alguien prometido en matrimonio.','It ends with the roof on the floor, a loose pig and somebody engaged to be married.']),
   Q(['Vuestro mundo no es un reloj: es una máquina con piezas de más. Los planes se tuercen por sitios que nadie había mirado, y eso es justo parte de la diversión.',
      'Your world is not a clock: it is a machine with spare parts. Plans go wrong in places nobody had looked at, and that is exactly part of the fun.'])]},
 {id:'vida', k:['La vida','Health'], qs:[
   Q(['Os han hecho una emboscada. De la nada aparecen seis tipos apuntando a todo el equipo y os piden que soltéis las armas.',
      'You have been ambushed. Out of nowhere six people appear aiming at the whole party and tell you to drop your weapons.'],
     ['Obedecer. No hay otra: alguna bala cae fija, y con una basta.','Obey. There is no other option: some bullet is bound to land, and one is enough.'],
     ['Atacar. ¡Por fin un reto de verdad!','Attack. Finally a real challenge!']),
   Q(['Un personaje recibe un impacto limpio de algo que estaba pensado para matar.',
      'A character takes a clean hit from something designed to kill.'],
     ['Se desploma. Lo que venga después ya es la escena de otro.','They go down. Whatever comes next is somebody else’s scene.'],
     ['Aprieta los dientes, se tapa la herida y sigue en la pelea. Se sentará cuando acabe.','They grit their teeth, cover the wound and stay in the fight. They will sit down when it is over.']),
   Q(['Hay una pelea grande y larga. Los personajes se golpean una vez y otra y otra, hay tiempo de cambiar de estrategia a mitad, y cada disparo es un rasguño que se va sumando a los demás.',
      'There is a big, long fight. The characters hit each other again and again, there is time to change tactics halfway through, and every shot is a scratch that adds to the others.'])]},
 {id:'estilo', k:['El estilo','Style'], qs:[
   Q(['Tres matones de callejón se cruzan con un personaje que ya ha matado a un dragón.',
      'Three alley thugs run into a character who has already killed a dragon.'],
     ['Se tira igual. Tres cuchillos son tres cuchillos y la mala suerte existe.','You roll anyway. Three knives are three knives and bad luck exists.'],
     ['No se tira para ver si gana. Se tira para ver qué frase suelta mientras acaba.','You do not roll to see whether they win. You roll to see what line they deliver while finishing.']),
   Q(['Un personaje tiene que cruzar una sala llena de enemigos muy por debajo de su nivel.',
      'A character has to cross a room full of enemies far below their level.'],
     ['Uno a uno, con sus tiradas. Que cueste.','One by one, with their rolls. Make it cost.'],
     ['La cruza. Lo que importa es cómo queda la sala cuando ha pasado.','They cross it. What matters is how the room looks once they have gone through.']),
   Q(['En vuestra mesa los enemigos menores no son un obstáculo: son el escenario donde los protagonistas demuestran lo que son. Despacharlos con una floritura es parte de lo que hace gracia.',
      'At your table lesser enemies are not an obstacle: they are the stage where the protagonists show what they are. Dispatching them with a flourish is part of the fun.'])]}
];
var RES_TONO = {
 opt:[[['El universo os pone a prueba','The universe puts you to the test'], ['Se lee el menor de dos dados: si algo puede salir mal, saldrá peor.','The lower of two dice is read: if anything can go wrong, it will go worse.']],
      [['El universo es imparcial','The universe is impartial'], ['Un dado, o la suma de dos. Si te disparan, sangras.','One die, or the sum of two. If you get shot, you bleed.']],
      [['El universo está de vuestra parte','The universe is on your side'], ['Se lee el mayor de dos dados: la suerte es casi un superpoder.','The higher of two dice is read: luck is almost a superpower.']]],
 caos:[[['Un mundo de reloj','A clockwork world'], ['Los resultados se agrupan en el centro y la planificación funciona.','Results cluster in the middle and planning works.']],
       [['Un mundo de película','A film-like world'], ['Hay giros, pero la historia tiene sentido de principio a fin.','There are twists, but the story makes sense from start to finish.']],
       [['Un universo caótico','A chaotic universe'], ['Críticos y pifias más anchos, y éxitos que salen con una factura.','Wider criticals and fumbles, and successes that arrive with a bill.']]],
 vida:[[['Aquí una bala decide','Here one bullet decides'], ['Vida fractal en tres bloques: crudo, corto e inmediato.','Fractal Health in three blocks: raw, short and immediate.']],
       [['Hacen falta varios golpes','It takes several hits'], ['Vida fractal en nueve casillas: aventura con margen de error.','Fractal Health in nine boxes: adventure with room for error.']],
       [['Los combates son guerras de desgaste','Fights are wars of attrition'], ['Vida fractal en veintisiete puntos: épico y largo.','Fractal Health in twenty-seven points: epic and long.']]],
 estilo:[[['Cada enemigo cuenta','Every enemy counts'], ['Regla del Estilo apagada: hasta el último matón se tira.','Style Rule off: even the last thug gets rolled for.']],
         [['Cada enemigo cuenta','Every enemy counts'], ['Regla del Estilo apagada: hasta el último matón se tira.','Style Rule off: even the last thug gets rolled for.']],
         [['Con floritura','With a flourish'], ['Regla del Estilo encendida: contra inferiores se tira para quedar bien.','Style Rule on: against lesser foes you roll to look good.']]]
};
function aplicaTono(){
  var o = banda3(sc('tono','opt')), c = sc('tono','caos'), cb = banda3(c);
  M.opt = ['bajo','neutro','alto'][o];
  M.caos = ['bajo','medio','alto'][cb];
  M.zoom = ['cascara','carne','nucleo'][banda3(sc('tono','vida'))];
  M.estilo = banda3(sc('tono','estilo')) === 2;
  M.card = null;
  /* las dos casillas sin tarjeta se reparten con el contador, no con otra
     pregunta: si el caos se quedó en el borde alto de su banda, tira a la
     vecina caótica. Se puede cambiar en la barra. */
  M.hueco = (c >= 10) ? 'caos' : 'prev';
  S.scene = null;
}

/* ------------------------------- 2. EL UNIVERSO ------------------------------- */
var G_SOBR = Q(['Antes de seguir, una de delimitación: en vuestro mundo, ¿hay algo que no se explique? Magia, monstruos, poderes, milagros, cosas que no deberían estar ahí.',
                'Before we go on, one to set the boundaries: in your world, is there anything that cannot be explained? Magic, monsters, powers, miracles, things that should not be there.'],
               ['Nada. Lo raro siempre tiene una explicación.','Nothing. The strange always has an explanation.'],
               ['Bastante, y además se puede usar.','Quite a lot, and it can be used, too.']);
var S_UNI = [
 {id:'tec', k:['El metal','The metal'], qs:[
   Q(['Alguien tiene que cruzar medio continente con un mensaje urgente.',
      'Somebody has to cross half a continent with an urgent message.'],
     ['Ensilla un caballo y reza por que los puentes sigan en pie.','They saddle a horse and pray the bridges are still standing.'],
     ['Lo manda, y llega antes de que acabe de escribirlo.','They send it, and it arrives before they have finished writing it.']),
   Q(['Un personaje quiere saber quién vive en una casa que no conoce.',
      'A character wants to know who lives in a house they do not know.'],
     ['Pregunta en la taberna de la esquina.','They ask at the tavern on the corner.'],
     ['Cruza tres registros a la vez y se entera también de lo que cenaron.','They cross-reference three databases and also find out what they had for dinner.']),
   Q(['El mundo que tenéis en la cabeza funciona con máquinas: hay cables, hay pantallas, hay cosas que se encienden. Cuanto más de acuerdo, más lejos del caballo y más cerca de la nave.',
      'The world you have in mind runs on machines: there are cables, screens, things that switch on. The more you agree, the further from the horse and the closer to the starship.'])]},
 {id:'magia', k:['La magia','Magic'], sup:true, qs:[
   Q(['En vuestro mundo, un enfermo grave que no mejora con medicinas…',
      'In your world, a seriously ill person who does not get better with medicine…'],
     ['…se muere, como se han muerto siempre.','…dies, the way they have always died.'],
     ['…busca a alguien que sepa las palabras, y a veces funciona.','…looks for somebody who knows the words, and sometimes it works.']),
   Q(['Una puerta cerrada con una cerradura muy buena.',
      'A door locked with a very good lock.'],
     ['Se abre con herramientas, con maña o con un hacha.','It opens with tools, with skill or with an axe.'],
     ['Se abre con la palabra correcta, si sabes cuál es y qué te va a costar.','It opens with the right word, if you know which one it is and what it will cost you.']),
   Q(['La magia existe y se puede aprender: hay quien la estudia, quien la cobra y quien la teme. No es un milagro suelto, es un oficio con facturas.',
      'Magic exists and can be learned: some study it, some charge for it and some fear it. It is not a stray miracle, it is a trade with invoices.'])]},
 {id:'mons', k:['Lo que acecha','What lurks'], sup:true, qs:[
   Q(['Un pueblo cierra las puertas al anochecer y nadie os explica por qué.',
      'A village bars its gates at nightfall and nobody explains why.'],
     ['Por los lobos y por los bandidos, que ya es bastante.','Because of wolves and bandits, which is quite enough.'],
     ['Por lo que viene de noche y tiene nombre, aunque no se diga en voz alta.','Because of what comes at night and has a name, even if nobody says it out loud.']),
   Q(['En el espejo del fondo del pasillo hay alguien que no eres tú.',
      'In the mirror at the end of the corridor there is somebody who is not you.'],
     ['Es un espejo. Hay una explicación y la vais a encontrar.','It is a mirror. There is an explanation and you will find it.'],
     ['Es exactamente lo que parece, y ya os ha visto.','It is exactly what it looks like, and it has already seen you.']),
   Q(['Vuestro mundo tiene monstruos de verdad, con reglas propias: cosas que beben sangre, que no envejecen o que no deberían estar aquí. Y que a veces llevan corbata y se sientan a negociar.',
      'Your world has real monsters, with rules of their own: things that drink blood, that do not age, or that should not be here. And that sometimes wear a tie and sit down to negotiate.'])]},
 {id:'cuerpo', k:['El cuerpo','The body'], sup:true, qs:[
   Q(['Alguien levanta un coche.','Somebody lifts a car.'],
     ['Con un gato hidráulico y paciencia.','With a hydraulic jack and patience.'],
     ['Con las manos, y encima lo lanza.','With their bare hands, and then throws it.']),
   Q(['Dos personas se baten en un tejado de tejas sueltas.',
      'Two people duel on a roof of loose tiles.'],
     ['Y una se resbala, porque son tejas sueltas.','And one slips, because the tiles are loose.'],
     ['Y siguen subiendo, de tejado en tejado, sin tocar el suelo en diez minutos.','And they keep going up, roof after roof, without touching the ground for ten minutes.']),
   Q(['En vuestro mundo hay cuerpos que rompen las reglas: superpoderes, técnicas imposibles, gente que corre por las paredes. No es magia aprendida, es algo que llevan dentro.',
      'In your world there are bodies that break the rules: superpowers, impossible techniques, people who run along walls. It is not learned magic, it is something they carry inside.'])]},
 {id:'palabra', k:['Las palabras','Words'], qs:[
   Q(['Una cena con gente importante y un secreto que no debe salir de la mesa.',
      'A dinner with important people and a secret that must not leave the table.'],
     ['Se come, se sonríe y a casa. La trama está en otra parte.','You eat, you smile and you go home. The plot is somewhere else.'],
     ['Es la escena principal de la sesión, y alguien va a salir herido sin que se levante una mano.','It is the main scene of the session, and somebody will leave wounded without a hand being raised.']),
   Q(['Un personaje queda en evidencia delante de quien decide los ascensos.',
      'A character is shown up in front of whoever decides promotions.'],
     ['Mal rato. Mañana nadie se acuerda.','An awkward moment. Tomorrow nobody remembers.'],
     ['Eso le va a costar meses, y lo vais a jugar.','That will cost them months, and you are going to play it out.']),
   Q(['En vuestra mesa las palabras hacen daño de verdad: hay duelos que se ganan con una frase, y perder la cara se paga tan caro como perder sangre.',
      'At your table words do real damage: there are duels won with a single line, and losing face costs as dearly as losing blood.'])]},
 {id:'roto', k:['El mundo roto','The broken world'], qs:[
   Q(['Encontráis una gasolinera con el cartel todavía intacto.',
      'You find a petrol station with its sign still intact.'],
     ['Y un empleado dentro que os cobra el depósito.','And an attendant inside who charges you for the tank.'],
     ['Y es el mejor hallazgo del mes, si el depósito no está seco.','And it is the best find of the month, if the tank is not dry.']),
   Q(['Alguien necesita antibióticos.','Somebody needs antibiotics.'],
     ['Va a una farmacia.','They go to a pharmacy.'],
     ['Organiza una expedición y vuelve alguien menos.','They organise an expedition and come back one person short.']),
   Q(['Vuestro mundo ya se rompió una vez. Lo que queda son restos, y todo lo bueno es algo que alguien fabricó antes de que todo se fuera al diablo.',
      'Your world has already broken once. What is left are remains, and everything good is something somebody made before it all went to hell.'])]},
 {id:'escala', k:['Las hazañas','The deeds'], qs:[
   Q(['Lo más gordo que han hecho los protagonistas hasta ahora…',
      'The biggest thing the protagonists have done so far…'],
     ['…fue salir vivos de una pelea que no buscaban.','…was getting out alive of a fight they did not pick.'],
     ['…cambió el mapa. Literalmente: hubo que redibujarlo.','…changed the map. Literally: it had to be redrawn.']),
   Q(['Si uno de ellos se enfada de verdad y pierde el control, ¿qué se rompe?',
      'If one of them really loses their temper and their control, what breaks?'],
     ['Una mesa, una nariz, una amistad.','A table, a nose, a friendship.'],
     ['Un barrio. Puede que una ciudad.','A district. Possibly a city.']),
   Q(['Las hazañas de vuestros personajes no son de escala humana: lo que hacen se mide en edificios, en ciudades o en países, y el mundo entero nota cuando aparecen.',
      'Your characters’ deeds are not on a human scale: what they do is measured in buildings, cities or countries, and the whole world notices when they show up.'])]}
];
var Q_TOON = Q(['Y una última, que decide mucho: en vuestro mundo, si alguien se cae de un acantilado, lo que decide si se hace daño no es la altura. Es si tiene gracia.',
                'And one last one, which decides a lot: in your world, if somebody falls off a cliff, what decides whether they get hurt is not the height. It is whether it is funny.']);
var TECID = ['espadas','vapor','hoy','neon','espacio'];
var TECN = [[['Espadas y castillos','Swords and castles'],['El Bazar abre La mazmorra y la estepa.','The Bazaar opens The Dungeon and the Steppe.']],
            [['Pólvora y vapor','Gunpowder and steam'],['El Bazar abre La Ciudad de Latón.','The Bazaar opens The City of Brass.']],
            [['Hoy mismo','Present day'],['El Bazar abre el equipo contemporáneo.','The Bazaar opens contemporary gear.']],
            [['Neón y cromo','Neon and chrome'],['El Bazar abre La Ciudad de Neón.','The Bazaar opens The City of Neon.']],
            [['Naves y estrellas','Ships and stars'],['El Bazar abre Ópera de Estrellas.','The Bazaar opens Star Opera.']]];
function uniSobrOn(){ return sc1('uni','sobr') >= 3; }
function resUni(sec){
  var s = sc('uni', sec.id), b = banda3(s);
  if (sec.id === 'tec') { var r = rung5(s); return {t:TECN[r][0], d:TECN[r][1]}; }
  if (sec.id === 'magia') return b === 2 ? {t:['Hay magia y se aprende','There is magic, and it is learned'], d:['Entra el Arcano: la quinta barra, el quinto ámbito y catorce puntos de habilidad en vez de doce.','The Arcane comes in: the fifth track, the fifth sphere and fourteen skill points instead of twelve.']}
    : {t:['Sin magia de oficio','No magic as a trade'], d:['Lo que haya de raro no se estudia ni se compra.','Whatever is strange is neither studied nor bought.']};
  if (sec.id === 'mons') return s >= 11 ? {t:['Monstruos, y de los malos','Monsters, and the bad kind'], d:['Entran el horror gótico y el cósmico.','Gothic and cosmic horror come in.']}
    : s >= 8 ? {t:['Hay monstruos','There are monsters'], d:['Entra el horror gótico: clanes, sangre y política nocturna.','Gothic horror comes in: clans, blood and night-time politics.']}
    : {t:['Nada que aceche','Nothing lurking'], d:['Los peligros de vuestro mundo tienen cara y nombre.','The dangers of your world have a face and a name.']};
  if (sec.id === 'cuerpo') return s >= 12 ? {t:['Cuerpos imposibles','Impossible bodies'], d:['Entran los superpoderes y las técnicas de ki.','Superpowers and ki techniques come in.']}
    : s >= 8 ? {t:['Técnicas imposibles','Impossible techniques'], d:['Entra el wuxia: carreras por las paredes y golpes con nombre.','Wuxia comes in: wall-running and named strikes.']}
    : {t:['Cuerpos de carne','Bodies of flesh'], d:['Lo que pueda hacer un cuerpo humano, y nada más.','Whatever a human body can do, and nothing more.']};
  if (sec.id === 'palabra') return b === 2 ? {t:['Las palabras cortan','Words cut'], d:['Entra el arsenal social: dieciséis armas que hacen Daño Social.','The social arsenal comes in: sixteen weapons that deal Social Damage.']}
    : {t:['Se habla, pero no se sangra','There is talk, but no bleeding'], d:['La intriga se narra; el daño viene de otro sitio.','Intrigue is narrated; damage comes from elsewhere.']};
  if (sec.id === 'roto') return b === 2 ? {t:['El mundo ya se rompió','The world already broke'], d:['Entra el Post-Apocalipsis: chatarra, agua y gasolina.','Post-Apocalypse comes in: scrap, water and fuel.']}
    : {t:['El mundo sigue en pie','The world is still standing'], d:['Hay tiendas, hay hospitales y hay quien pasa la factura.','There are shops, there are hospitals and there is somebody sending the bill.']};
  var g = rungGrid(s) + 1;
  return {t:[GRIDN[g][0], GRIDN[g][1]], d:[['Rejilla de Potencia: nivel inicial ','Power Grid: starting level '][L()] + g + '.', '']};
}
function aplicaUni(){
  if (M.known && M.world !== null) return;
  var u = [], sup = [], xtra = [];
  var tec = TECID[rung5(sc('uni','tec'))];
  M.tech = tec;
  M.era = (tec === 'espadas' || tec === 'vapor') ? 'pasado' : tec === 'hoy' ? 'presente' : 'futuro';
  u.push({espadas:'fantasia', vapor:'steampunk', hoy:'terror', neon:'neon', espacio:'opera'}[tec]);
  if (uniSobrOn()) {
    if (banda3(sc('uni','magia')) === 2) { u.push('fantasia'); sup.push('magia'); }
    var mo = sc('uni','mons');
    if (mo >= 8) { u.push('gotico'); sup.push('monstruos'); }
    if (mo >= 11) u.push('terror');
    var cu = sc('uni','cuerpo');
    if (cu >= 8) { u.push('wuxia'); sup.push('ki'); }
    if (cu >= 12) { u.push('supers'); sup.push('poderes'); }
  }
  if (banda3(sc('uni','palabra')) === 2) { u.push('social'); xtra.push('intriga'); }
  if (banda3(sc('uni','roto')) === 2) u.push('postapo');
  if (sc1('uni','toon') >= 4) { u.push('toon'); xtra.push('toon'); }
  M.unis = u.filter(function(x, i){ return u.indexOf(x) === i; });
  M.sup = sup.length ? sup : ['none'];
  M.xtra = xtra.length ? xtra : ['none'];
  M.known = false; M.world = null; M.family = null;
  M.grid = rungGrid(sc('uni','escala')) + 1;
}

/* --------------------------------- 3. EL BAÚL --------------------------------- */
var G_CHICHA = Q(['Estáis a mitad de una persecución por los tejados y hay que saber si el salto sale. ¿Qué preferís que pase en la mesa?',
                  'You are halfway through a rooftop chase and you need to know whether the jump works. What would you rather happen at the table?'],
                 ['Un dado y a correr. Si hay que mirar una tabla, la persecución se ha roto.','One die and keep running. If somebody has to look up a table, the chase is broken.'],
                 ['Un dado, el reloj de la guardia y restar lo que pesa la mochila. Eso es lo divertido.','One die, the watch’s clock and subtracting the weight of the pack. That is the fun part.']);
var G_INSIST = Q(['Te lo pregunto otra vez de otra manera, porque de esto depende el resto. Una regla nueva, aunque sea de una línea, es una regla que alguien tiene que acordarse de aplicar en mitad de la escena.',
                  'Let me ask again another way, because the rest depends on this. A new rule, even a one-liner, is a rule somebody has to remember to apply in the middle of a scene.'],
                 ['Entonces ninguna. El juego base ya me da lo que necesito.','Then none. The base game already gives me what I need.'],
                 ['Una o dos, si de verdad cambian algo.','One or two, if they really change something.']);
var S_BAUL = [
 {id:'t0', k:['Narración y ritmo','Narration and pace'], qs:[
   Q(['Un jugador dice: «¿y si resulta que yo ya había comprado al portero?»',
      'A player says: “what if it turns out I had already bribed the doorman?”'],
     ['Pues no lo habías comprado. Se juega lo que se ha jugado.','Then you had not bribed them. You play what has been played.'],
     ['Pues cuéntamelo, lo tiramos, y si sale, lo habías comprado.','Then tell me, we roll for it, and if it works, you had.']),
   Q(['El Director tira un dado detrás de la pantalla y no dice qué ha salido.',
      'The Director rolls a die behind the screen and does not say what came up.'],
     ['Eso me pone nervioso. Quiero ver los números.','That makes me nervous. I want to see the numbers.'],
     ['Eso es exactamente lo que quiero que pase.','That is exactly what I want to happen.']),
   Q(['En vuestra mesa el tiempo y la narración son herramientas: se salta al pasado, se mide cuánto falta para que pase lo malo, y un éxito justito deja factura. Os gusta que la estructura de la historia también tenga reglas.',
      'At your table time and narration are tools: you jump to the past, you measure how long until the bad thing happens, and a narrow success leaves a bill. You like the structure of the story to have rules too.'])]},
 {id:'t1', k:['Riesgo y poder','Risk and power'], qs:[
   Q(['Un personaje está a punto de perder y alguien, o algo, le ofrece ayuda.',
      'A character is about to lose and somebody, or something, offers help.'],
     ['No hay nadie ofreciendo nada. Pierde.','There is nobody offering anything. They lose.'],
     ['Siempre hay alguien ofreciendo algo, y el precio se cobra más tarde.','There is always somebody offering something, and the price is collected later.']),
   Q(['Llega el momento en que el personaje se quita el abrigo y se ve lo que es de verdad.',
      'The moment comes when the character takes off their coat and you see what they really are.'],
     ['Eso en mi mesa no pasa.','That does not happen at my table.'],
     ['Eso en mi mesa pasa una vez por sesión, y con música.','That happens once a session at my table, and with music.']),
   Q(['Os gusta que el poder tenga palanca: transformaciones, pactos, momentos en que un personaje sube de golpe y hace mucho más de lo normal. Aunque se pague después.',
      'You like power to have a lever: transformations, pacts, moments when a character surges and does far more than usual. Even if it is paid for afterwards.'])]},
 {id:'t2', k:['Cuerpo, identidad y lazos','Body, identity and bonds'], qs:[
   Q(['En la ficha, al lado del nombre, hay un hueco para escribir a quién quiere el personaje.',
      'On the sheet, next to the name, there is a space to write down who the character loves.'],
     ['Es decoración. No lo voy a mirar.','It is decoration. I am not going to look at it.'],
     ['Es la mitad de la ficha, y el Director lo va a usar contra mí.','It is half the sheet, and the Director is going to use it against me.']),
   Q(['Un personaje muere y el jugador sigue sentado a la mesa.',
      'A character dies and the player is still sitting at the table.'],
     ['Se hace una ficha nueva y a seguir.','You make a new sheet and carry on.'],
     ['Depende de qué cuerpo era, y de si había otro esperando.','It depends which body it was, and whether there was another one waiting.']),
   Q(['En vuestras partidas el cuerpo y la identidad son material de juego: lo que te mueve por dentro, a quién quieres, de quién depende tu cara. Os interesa que eso tenga reglas y no solo notas al margen.',
      'In your games body and identity are playable material: what drives you inside, who you love, whose opinion your face depends on. You want that to have rules, not just margin notes.'])]},
 {id:'t3', k:['Un mundo que muerde','A world that bites'], qs:[
   Q(['Lleváis cuatro horas de viaje por el pantano y nadie ha tirado un dado contra nadie.',
      'You have spent four hours travelling through the swamp and nobody has rolled a die against anybody.'],
     ['Pues qué bien. A ver si llegamos ya.','Good. Let us get there already.'],
     ['Pues el pantano debería haber cobrado algo. Para eso es un pantano.','Then the swamp should have charged something. That is what a swamp is for.']),
   Q(['Un personaje queda muy malherido. ¿Qué queréis saber?',
      'A character is badly wounded. What do you want to know?'],
     ['Si puede seguir o no. Lo demás lo narramos.','Whether they can go on or not. The rest we narrate.'],
     ['Qué le ha pasado exactamente. Que lo diga una tabla y que quede escrito.','Exactly what happened to them. Let a table say it and let it stay written down.']),
   Q(['El mundo de vuestras partidas no espera a que alguien ataque: el frío, la enfermedad, el destino y la mala suerte son enemigos con reglas propias.',
      'The world of your games does not wait for somebody to attack: cold, disease, fate and bad luck are enemies with rules of their own.'])]}
];
/* dentro de cada tema, primero las reglas sin chicha y luego las que piden
   llevar un numero. El orden es el de "lo mas caracteristico del tema". */
var BAUL_ORD = [
 {light:[1,15,8], heavy:[0]},
 {light:[10,2,11], heavy:[3]},
 {light:[14], heavy:[13,6,7]},
 {light:[5], heavy:[9,12,4]}
];
function baulChicha(){ return sc1('baul','chicha') >= 3; }
function baulCero(){ return !baulChicha() && sc1('baul','insiste') > 0 && sc1('baul','insiste') <= 2; }
function baulCand(gi){ var o = BAUL_ORD[gi]; return o.light.concat(baulChicha() ? o.heavy : []); }
function baulDe(gi){ return baulCand(gi).slice(0, cuantas(sc('baul','t' + gi))); }
function aplicaBaul(){
  if (baulCero()) { setBaulMask(0); return; }
  var m = 0;
  BAUL_ORD.forEach(function(x, gi){ baulDe(gi).forEach(function(k){ m |= (1 << k); }); });
  setBaulMask(m);
}
function resBaul(gi){
  var on = baulDe(gi);
  return on.length
    ? {t:[on.length + (on.length === 1 ? ' regla' : ' reglas'), on.length + (on.length === 1 ? ' rule' : ' rules')],
       d:[on.map(function(k){ return DATA.baul[k][0]; }).join(', '), on.map(function(k){ return DATA.baul[k][1]; }).join(', ')]}
    : {t:['Ninguna de este tema','None from this theme'], d:['El núcleo se encarga.','The core handles it.']};
}
"""

