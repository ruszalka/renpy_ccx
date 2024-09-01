#Personajes
define Marina = Character('Instructora Marina', color="#ece580")
define Sabino = Character('Capitán Gentile', color="#9ca1e9")
define Daria = Character('Daria', color="#db6b6b")
define Vlad = Character ('Instructor Vlad', color="#6bdbb9")

#Inicio del juego 
label start:
    play music "audio/background.mp3"
    image arbol = "bg-tree.png"
    scene arbol

"Todo comenzó durante la pandemia."
"No porque algo hubiera cambiado de forma dramática, sino precisamente porque nada había cambiado."
"De repente, me di cuenta de que había estado viviendo como si estuviera en confinamiento mucho antes de que el confinamiento fuera real."
"Y, entonces, me golpeó: ¿qué había hecho con mi libertad cuando realmente la tenía?"
"¿Cuánto tiempo había pasado desde la última vez que sentí esa chispa de vida, ese deseo de explorar lo desconocido?"

"Al principio, pensé que sería fácil."
"No tener que inventar excusas para cancelar planes."
"No tener que forzar sonrisas o buscar algo interesante que decir."
"La verdad, me gustaba la idea de no tener que enfrentarme al mundo exterior cada día."
"Era como si, de repente, todos estuviéramos en mi misma página, compartiendo el mismo espacio limitado, las mismas restricciones."

"Pero, a medida que pasaban las semanas, la realidad me empezó a pesar."
"Los días se volvieron monótonos, como un bucle interminable de lo mismo."
"Levantarme cada mañana para sentarme frente a la computadora."
"Trabajar, distraerme, todo sin moverme de las mismas cuatro paredes."
"Mi hogar, que antes sentía como un refugio, se convirtió en una especie de jaula, y la rutina en la cadena que me ataba."

"Los días se convirtieron en semanas, y las semanas en meses."
"Setenta y cinco metros cuadrados. Esa era la medida de mi vida, mi mundo entero, por meses."
"Y por primera vez, no era por elección."
"Fue entonces cuando supe que necesitaba algo más."
"Necesitaba salir."
"Salir al mundo."
"Ver más allá de mi ventana, más allá de lo que conocía."

"Empecé a buscar consuelo en videos de otros lugares."
"Primero, para ver cómo estaban lidiando los demás con todo esto."
"Luego, simplemente para imaginar cómo sería estar en otro lugar, en otra vida."
"Cada video era una pequeña ventana a un mundo diferente."
"A un mundo donde la gente seguía adelante, aún en medio de la incertidumbre."

"Y así, terminé viendo videos de azafatas que habían perdido su trabajo debido a la pandemia."
"Mujeres de todas partes, de diferentes edades, culturas y trayectorias, que contaban cómo extrañaban los cielos abiertos."
"Las nubes, esa sensación de estar flotando a 40,000 pies de altura."
"Me encontré escuchando sus historias, una tras otra."
"Y, poco a poco, algo en mí comenzó a despertar."

"Me pregunté si alguna vez había sentido una pasión así por algo."
"Y me di cuenta de que no."
"Que siempre había dejado que el miedo me detuviera, que había permitido que las excusas me mantuvieran en mi zona de confort."

"Desde que todo volvió a la 'normalidad', me di cuenta de que nada es realmente igual."
"Nadie lo es."
"Hay algo en el aire, una especie de nostalgia por lo que fuimos antes de todo esto."
"Mezclada con una curiosidad sobre lo que podríamos ser ahora."

"Y, quizás por esa misma razón, decidí dar un salto."
"Me inscribí en el proceso de selección para ser azafata en la aerolínea más grande del país."
"El mundo está empezando a sanar."
"Los aviones vuelven a surcar los cielos."

"Y yo… quiero saber si estoy lista para esa vida."
"Una vida que me lleve a lugares que aún no he visto, a conocer personas que aún no he encontrado."
"Quiero sentir esa adrenalina, esa emoción de lo desconocido."
"¿Estoy preparada para dejar atrás mis miedos y lanzarme al vacío?"
"Solo hay una forma de saberlo."

"Quiero conocer el mundo."
"Y esta vez, no pienso desperdiciar mi oportunidad."

scene arbol
with dissolve

#- Modulo 1 - introduccion a la aviacion comercial y a la funcion del tcp


image sala = "background1.png"
scene sala

image iMarina = "crew1.png"
show iMarina at left
with fade

"Bienvenidos al entrenamiento de tripulante de cabina de pasajeros de Sky-Blue Airlines."

Marina "Mi nombre es Marina, y seré su principal instructora a lo largo de esta capacitación."
Marina "Antes que nada me gustaría felicitarlos por haber sido seleccionados para esta capacitación tras un riguroso proceso. Cientos de candidatos se postulan año a año, siendo apenas unos pocos los egreados que lleguen a los estandares para volar con nosotros."
Marina "Asi que no se preocupen. Si bien hay etapas en este proceso que son excluyentes, en caso de quedar fuera de la selección final en esta oportunidad, podrán volver a postularse luego de seis meses tantas veces como quieran."
Marina "La capacitación inicial dentro de la aerolinea tiene una duración total de seis semanas, donde aprenderán todo lo necesário tanto a nivel práctico como técnico y legal, para tripular con tranquilidad y garantizar un vuelo seguro a otros."
Marina "Durante este periodo, estaremos viendo un módulo por dia, con una prueba al final de cada módulo. Esta instancia es excluyente, solo serán aptos para volver al siguiente dia quienes hayan aprobado la prueba anterior."
Marina "Parece exigente y realmente lo es. En Sky-Blue Airlines no escatimamos recursos para mantener nuestros estandares de excelencia."
Marina "El dia de hoy aprenderemos sobre la historia de la aviación comercial y como el rol del Tripulante de Cabina de Pasajeros, o sea, ustedes, ha cambiado a lo largo del tiempo."
Marina "Les sugiero que tomen nota de las siguientes informaciones porque podrán usar los descansos para estudiar y revisar sus apuntes antes de la prueba."
Marina "Todos listos? Empecemos."

image PScreen ="projectionscreen.png"
show PScreen at right
with moveintop

Marina "Todo se remonta al inicio del sigo pasado, entre 1900 y 1920, luego después de la Primera Guerra Mundial, cuando se utilizaron aviones miliates desmantelados para el transporte de correo y pasajeros."
Marina "En 1919, se estableció la primera aerolínea internacional, KLM, y la primera aerolínea estadounidense, American Airways (ahora American Airlines)."
Marina "Los primeros vuelos eran incómodos, ruidosos y solo accesibles para personas adineradas."
Marina "No fue hasta la década del 30 que se introdujeron aviones más grandes y seguros como el Douglas DC-3, que fue fundamental para la expansión de la aviación comercial."
Marina "Ya durante la Segunda Guerra Mundial, la aviación comercial se estancó, pero la tecnología desarrollada durante la guerra ayudó a mejorar la seguridad y eficiencia de los vuelos después."
Marina "La posguerra da inicio a la era del jet, que comenzó con el De Havilland Comet y, posteriormente, con el Boeing 707, lo que permitió vuelos más rápidos y eficientes."
Marina "Los vuelos comerciales se hicieron más accesibles para la clase media, y el turismo internacional comenzó a florecer."
Marina "Los aeropuertos y las aerolíneas comenzaron a estandarizarse, estableciendo procedimientos de seguridad y confort para los pasajeros."
Marina "La década del 70 da inicio a la era moderna de la aeronáutica. La introducción del Boeing 747 en 1970 marcó el inicio de la era de los aviones de fuselaje ancho, aumentando la capacidad de pasajeros y reduciendo los costos por asiento."
Marina "En la década de 1990, la aviación comercial se democratizó aún más con la aparición de aerolíneas de bajo costo como Southwest Airlines y Ryanair."
Marina "Comenzamos los años 2000 y los avances no cesan. Avances tecnológicos como el Airbus A380 y el Boeing 787 Dreamliner han mejorado la eficiencia de combustible y el confort a bordo."
Marina "La aviación comercial también enfrenta nuevos desafíos, como la sostenibilidad y la competencia en un mercado globalizado."
Marina "Ahora tomaremos un descanso de 20 minutos, pueden aprovechar este tiempo para revisar sus apuntes. En la segunda mitad estaremos hablando del desarrollo de las funciones de los Tripulantes de Cabina de Pasajeros."

hide iMarina
with dissolve

#primera aparicion de daria
image iDaria ="daria.png"
show iDaria
with fade

Daria "Cómo te llamas?"
menu:
    "Me llamo Maria":
        jump nombrea

    "Maria":
        jump nombreb
            
label nombrea:
    Daria "Encantada. Necesitas ayuda con los apuntes?"
   

label nombreb:
    Daria "Encantada."
   

hide iDaria
with dissolve

show iMarina at left
with fade

Marina "Espero hayan podido relajarse pero no mucho, que la parte que viene es tan densa como interesante."
Marina "Hablaremos sobre el desarrollo de la carrera de TCP (Tripulante de Cabina de Pasajeros) y sus funciones."
Marina "La carrera de TCP comenzó en los años 1920, con las primeras azafatas, quienes originalmente eran enfermeras contratadas para garantizar la seguridad y el bienestar de los pasajeros en vuelos que a menudo eran turbulentos y riesgosos."
Marina "Las primeras TCP también tenían la tarea de ayudar con la carga de equipaje, servir comidas y bebidas, y proporcionar primeros auxilios."
Marina "En la década de 1930, las TCP se convirtieron en un símbolo de modernidad y glamour. Su trabajo seguía siendo enfocado en la seguridad, pero también en la hospitalidad."
Marina "Durante los años 1940 y 1950, las funciones de las TCP se ampliaron con la introducción de aviones más grandes y la comercialización del viaje aéreo. Además de atender a los pasajeros, se esperaba que representaran a la aerolínea con elegancia y profesionalismo."
Marina "Con la introducción de los aviones jet y el aumento del tráfico aéreo, la capacitación de las TCP se volvió más rigurosa, con énfasis en la evacuación de emergencia, el manejo de crisis, y la atención médica."
Marina "En los años 1970, se comenzaron a romper estereotipos, permitiendo a hombres entrar a la profesión y eliminando restricciones de edad y apariencia física para las TCP."
Marina "En la actualidad, los TCP son profesionales altamente capacitados en seguridad, atención al cliente, y manejo de situaciones de emergencia."
Marina "Las aerolíneas han aumentado la diversidad en sus equipos de cabina y han enfocado la capacitación en la gestión de pasajeros problemáticos, manejo de desastres, y la adaptación cultural."
Marina "Las responsabilidades de las TCP han crecido con la expansión del servicio a bordo, el incremento de la seguridad aérea, y la atención a pasajeros con necesidades especiales."
Marina "Hoy en día, ser TCP implica no solo ser el rostro visible de la aerolínea, sino también garantizar la seguridad de los pasajeros y del vuelo en general, lo que convierte esta carrera en una mezcla única de hospitalidad y profesionalismo en situaciones de alta presión."

hide iMarina
with dissolve

hide PScreen
with moveouttop

#Modulo 2 - reglamentacion nacional e internacional


show iMarina at left
with fade

Marina "Bienvenidos al segundo día de capacitación. Espero que la prueba del dia de ayer les haya calmado los nervios."
Marina "Como podrán ver, fue bastante sencillo. Bastaba con prestar atención a la clase y anotar los apuntes correctos para aprobar. Preferimos que asi sea."
Marina "Asi premiamos a los que aprovechan el curso en integridad. Siendo puntuales a las clases y atentos a los contenidos."
Marina "De igual manera, sugerimos que guarden sus apuntes. A mitad de curso vamos a tener una examen mayor, con todo lo aprendido hasta el momento. Y otra final. Ambas excluyentes, aunque a diferencia de las demas evaluaciones, esos examenes podrán hacerlas hasta dos veces."
Marina "Pero ese es tema para otro momento. El dia de hoy vamos a aprender sobre la relgamentación nacional e internacional en la aeronautica."
Marina "La reglamentación en la aviación civil y específicamente en relación a los Tripulantes de Cabina de Pasajeros está sujeta a normativas nacionales e internacionales para garantizar la seguridad, la eficiencia y el buen funcionamiento de las operaciones aéreas. En la clase de hoy además, les proporcionaré una visión general de la reglamentación en Uruguay y en el ámbito internacional."
Marina "En Uruguay, la autoridad encargada de la regulación y supervisión de la aviación civil es la Dirección Nacional de Aviación Civil e Infraestructura Aeronáutica (DINACIA). Esta entidad se encarga de aplicar las normativas y regulaciones que rigen la aviación en el país, incluyendo las relacionadas con los TCPs."
Marina "Los TCPs deben obtener una Licencia de Tripulante de Cabina emitida por DINACIA. Para obtener la licencia, los aspirantes deben completar un curso de formación aprobado por DINACIA, que incluye formación en seguridad, primeros auxilios, procedimientos de emergencia, y evacuación, entre otros."
Marina "Se requiere la realización de exámenes médicos regulares para garantizar que los TCPs estén en condiciones físicas y psicológicas adecuadas para desempeñar sus funciones."
Marina "Los TCPs deben cumplir con las regulaciones relativas a horas de servicio, que limitan la cantidad de horas que pueden trabajar en un día o semana para evitar la fatiga."
Marina "Existe un enfoque riguroso en la formación continua, con requerimientos de capacitación periódica para mantener la licencia activa, especialmente en áreas clave como la seguridad y la atención médica de emergencia."
Marina "Las regulaciones también estipulan los procedimientos de seguridad que los TCPs deben seguir durante las operaciones de vuelo, incluyendo la inspección de equipos de emergencia, la instrucción a los pasajeros sobre procedimientos de seguridad, y la supervisión del cumplimiento de las normativas de seguridad a bordo."
Marina "La normativa internacional en aviación civil está regulada por la Organización de Aviación Civil Internacional (OACI), una agencia especializada de las Naciones Unidas que establece normas y regulaciones para garantizar la seguridad y eficiencia del transporte aéreo en todo el mundo."
Marina "La OACI establece las Normas y Prácticas Recomendadas (SARPs), que son aplicadas por los Estados miembros a través de sus autoridades nacionales. Estas incluyen estándares para la formación y certificación de los TCPs, procedimientos de seguridad, y gestión de emergencias."
Marina "Los Estados deben adaptar estas normas a sus legislaciones nacionales, lo que significa que las regulaciones de Uruguay están alineadas con las directrices de la OACI."
Marina "El Convenio sobre Aviación Civil Internacional, también conocido como Convenio de Chicago, es el tratado fundacional de la OACI y establece los principios que rigen la aviación civil internacional, incluyendo la seguridad, la protección del medio ambiente, y los derechos de los Estados."
Marina "A través de este convenio, se garantiza que los TCPs reciban formación y certificación conforme a estándares internacionales, y que las aerolíneas cumplan con normativas uniformes en la operación de vuelos internacionales."
Marina "Las regulaciones internacionales también incluyen normas sobre las horas de trabajo y descanso para los TCPs, con el fin de mitigar la fatiga y garantizar que los tripulantes estén en óptimas condiciones para cumplir sus funciones."
Marina "La Asociación Internacional de Transporte Aéreo (IATA) también juega un rol importante, promoviendo buenas prácticas y estándares operacionales a nivel global."
Marina "El cumplimiento de estas normativas es supervisado tanto por las autoridades nacionales (como DINACIA en Uruguay) como por auditorías y evaluaciones realizadas por organismos internacionales. Las aerolíneas y los TCPs están sujetos a inspecciones y evaluaciones periódicas para garantizar que se adhieren a todas las regulaciones pertinentes, manteniendo los más altos niveles de seguridad y profesionalismo en la industria aérea."
Marina "La clase de hoy fue bastante mas corta pero con informaciones mas sustanciales, si se quiere. Terminaremos por aqui, y los minutos restantes antes de la prueba los pueden usar para repasar con sus colegas. Aprovechen a conocerse, ya que trabajar en equipo es fundamental en el desempeño de sus futuras funciones."


hide iMarina
with dissolve

#Modulo 3 - procedimientos de rutina, obligaciones y repsonsabilidades


show iMarina at left
with fade

Marina "Bienvenidos a todos nuevamente. Es un placer ver que se mantienen firmes y fuertes en el camino de convertirse en grandes tripulantes."
Marina "Espero que vayan sintiendo esta sala poco a poco como su propio hogar. Porque cuando menos lo esperen, lo será."
Marina "Sin mas dilación, el día de hoy hablaremos sobre los procedimientos de rutina, obligaciones y responsabilidades."
Marina "Empecemos."
Marina "Los Tripulantes de Cabina de Pasajeros (TCPs) tienen un papel crucial en la operación segura y eficiente de un vuelo. Sus procedimientos de rutina, obligaciones y responsabilidades están diseñados para garantizar la seguridad, comodidad y bienestar de los pasajeros, así como para colaborar con la tripulación técnica en la gestión de emergencias."
Marina "Los TCPs se reúnen con el resto de la tripulación antes de cada vuelo para recibir un informe sobre las condiciones del vuelo, el número de pasajeros, información específica sobre pasajeros con necesidades especiales, y repasar procedimientos de emergencia. A este procedimiento le llamamos briefing, y se realiza siempre previo al vuelo en cuestión."
Marina "Enseguida después del briefing, los TCPs inspeccionan el equipo de emergencia a bordo, como chalecos salvavidas, extintores, botiquines de primeros auxilios, y las salidas de emergencia para asegurarse de que todo esté en su lugar y en buen estado."
Marina "Una vez realizada la inspección, se hace la preparación de cabina. Se verifica que los compartimentos de equipaje estén cerrados, que los asientos estén en posición vertical, y que los cinturones de seguridad estén visibles y accesibles. También se asegura que los baños estén en condiciones óptimas. Nos certificamos de que todo esté listo para la recepción de los pasajeros."
Marina "Cuando todo esté listo y chequeado, los TCPs dan la bienvenida a los pasajeros a bordo, los ayudan a encontrar sus asientos y aseguran que coloquen su equipaje de manera adecuada."
Marina "Proporcionan asistencia a pasajeros con discapacidades, personas mayores, y familias con niños pequeños, ayudándolos a acomodarse y a entender las instrucciones de seguridad."
Marina "Se supervisa el cumplimiento. Aseguran que los pasajeros sigan las normativas de seguridad, como el uso del cinturón de seguridad, la colocación de dispositivos electrónicos en modo avión, y la ubicación correcta de los equipajes."
Marina "Dadas las condiciones óptimas, se puede despegar. Pero nunca antes del briefing, inspección de seguridad, preparación de cabina, recepción de pasajeros, asistenica especial y supervisión de cumplimiento."
Marina "Una vez en el aire, se hace la demostración de seguridad. Los TCPs realizan o supervisan la demostración de seguridad al inicio del vuelo, donde se explica a los pasajeros cómo utilizar los cinturones de seguridad, máscaras de oxígeno, chalecos salvavidas y las salidas de emergencia."
Marina "De estar contemplado, se da el servicio a bordo. Los TCPs encargan de servir alimentos y bebidas a los pasajeros, y de atender solicitudes, garantizando un servicio de alta calidad. Siempre y cuando el servicio esté incluido, y las condiciones climáticas lo habiliten. No se da el servicio a bordo en condiciones adversas, como por ejemplo, turbulencias."
Marina "Los TCPs realizan recorridos regulares por la cabina para verificar el bienestar de los pasajeros, responder preguntas, y asegurarse de que no haya situaciones inusuales o peligrosas."
Marina "En caso de turbulencia, despresurización, incendio, o cualquier otro tipo de emergencia, los TCPs deben seguir procedimientos estrictos para proteger a los pasajeros y mantener la calma en la cabina."
Marina "Una vez en tierra, supervisan el desembarque de los pasajeros, asegurándose de que lo hagan de manera ordenada y segura."
Marina "Y por último, se hace una revisión final de la cabina. Después de que los pasajeros han desembarcado, los TCPs realizan una inspección final de la cabina para asegurarse de que no haya quedado nada fuera de lugar, y de que no se hayan dejado objetos personales en el avión."
Marina "Todas estas son nuestras responsabilidades y obligaciones como Tripulates de Cabina de Pasajeros."
Marina "La responsabilidad primordial de un TCP es la seguridad de los pasajeros. Esto incluye asegurarse de que todos cumplan con las normativas de seguridad y estar preparados para actuar en caso de una emergencia."
Marina "Los TCPs son responsables de conocer y poder ejecutar los procedimientos de evacuación y uso del equipo de emergencia."
Marina "Los TCPs están capacitados para proporcionar primeros auxilios y asistir en emergencias médicas, utilizando el equipo disponible a bordo como botiquines de primeros auxilios y desfibriladores automáticos externos (DEA)."
Marina "Deben saber cómo coordinarse con profesionales médicos en tierra en caso de una emergencia grave a bordo."
Marina "En casos extremos, los TCPs tienen la autoridad para informar al comandante y solicitar medidas disciplinarias, como la restricción de un pasajero a bordo."
Marina "Entre su larga lista de tareas, están obligados a cumplir y hacer cumplir todas las regulaciones de aviación aplicables, tanto nacionales como internacionales."
Marina "Deben seguir estrictamente los procedimientos establecidos por la aerolínea y las autoridades de aviación para cada etapa del vuelo."
Marina "Los TCPs mantienen una comunicación constante con la cabina de mando, informando al comandante de cualquier irregularidad, emergencia o situación especial que ocurra en la cabina de pasajeros."
Marina "Deben estar preparados para asistir a la tripulación técnica en situaciones críticas, como aterrizajes de emergencia."
Marina "Además, tienen otras responsabilidades adicionales."
Marina "Los TCPs deben mantener la confidencialidad sobre la información del vuelo y de los pasajeros, y actuar siempre con profesionalismo."
Marina "Están obligados a participar en programas de formación continua para mantenerse actualizados en las normativas y procedimientos de seguridad, así como en nuevas técnicas de atención al cliente."
Marina "Dado que su trabajo puede ser físicamente exigente y estresante, los TCPs deben mantener un buen estado de salud física y mental, cumpliendo con los requisitos médicos establecidos por las autoridades."
Marina "Estas obligaciones y responsabilidades hacen que los TCPs sean una parte esencial en la operación segura y efectiva de cualquier vuelo, más allá del aspecto de servicio al cliente que es más visible para los pasajeros."
Marina "Como habrán notado a estas alturas, ser Tripulante de Cabina de Pasajeros mas que un trabajo, es un estilo de vida."
Marina "Será transversal a cada aspecto de su rutina, desde la alimentación, el sueño, su salud mental, hasta su forma de comunicarse, observar el mundo y otras personas."
Marina "Además, afectará a sus calendarios y por consiguiente, sus encuentros con familias y amigos."
Marina "El equipo de tripulación, también llamado Cabin Crew, será como su familia."
Marina "Los unos a los otros serán el único apoyo fraternal que tendrán a 40.000 pies de altura."
Marina "Pues bien. Como hemos visto hoy, no es todo pasta y pollo, o viajes gratis."
Marina "Ser un gran Tripulante de Cabina conlleva a una gran responsabilidad."
Marina "Hagamos una pausa de unos minutos, para volver a la prueba de hoy. No piensen que se han salvado todavia, jaja."

hide iMarina
with dissolve

#Modulo 4 - Conocimientos basicos de aeronaves y motores

image iSabino ="crew2.png"
show iSabino at left
with fade

Sabino "Buenos dias a todos, y bienvenidos al módulo de conocimientos básicos de aeronaves y motores."
Sabino "Mi nombre es Sabino Gentile, y desempeño el rol de Capitán de formación en Sky-Blue Airlines, a mas de 15 años. Anteriormente era oficial de la fuerza aérea."
Sabino "Estoy muy feliz de ver tantos jóvenes interesados en el mundo de la aeronáutica."
Sabino "Como ya les habrá mencionado mi colega Marina, es un estilo de vida que se lleva con mucho honor, dado a que conforman una parte escencial en la conexión intercultural del mundo."
Sabino "Y se debe desempeñar con un gran sentido de responsabilidad."
Sabino "En los 75 años de funcionamiento de nuestra aerolinea, nunca hemos tenido ningún accidente en un vuelo comercial."
Sabino "Y porque sabemos que gran parte de los accidentes se producen por errores humanos, no nos permitimos formar profesionales menos que excelentes."
Sabino "Los errores fatales están muy ligados al valor que se le da a la vida en la cultura empresarial, y en general."
Sabino "Trabajar en la aeronáutica muchas veces implica cumplir funciones de alto riesgo. Y para ello vamos a darles todas las herramientas para que puedan vivir y disfrutar a pleno este trabajo, que tan hermoso es, sin preocuparse por nada mas."
Sabino "Volar por el mundo es un privilegio, y vivir de ello es invaluable."
Sabino "Sin mas preambulos, comencemos."
Sabino "Aunque los Tripulantes de Cabina de Pasajeros no están encargados del pilotaje ni del mantenimiento técnico de la aeronave, se espera que tengan conocimientos básicos sobre el funcionamiento de las aeronaves y sus motores. Este conocimiento es esencial para entender mejor las operaciones del vuelo, la seguridad a bordo, y para manejar situaciones de emergencia de manera eficaz."
Sabino "Empezaremos por las partes principales de una aeronave."
Sabino "El fuselaje: Es el cuerpo principal de la aeronave donde se encuentra la cabina de pasajeros, la cabina de mando, la bodega de carga y otros compartimentos."
Sabino "Las alas: Proveen la sustentación necesaria para que la aeronave vuele. Los TCPs deben conocer la ubicación de las salidas de emergencia sobre las alas y cómo utilizarlas en caso de evacuación."
Sabino "El empenaje: Conjunto de superficies en la parte trasera de la aeronave que incluye la cola, el estabilizador vertical (timón) y el estabilizador horizontal (elevadores), responsables de la estabilidad y control en el eje vertical y horizontal."
Sabino "Los motores: Se encargan de proporcionar la propulsión para el vuelo. Los TCPs deben tener una comprensión básica de cómo funcionan y qué ruidos o comportamientos son normales o anormales durante el vuelo."
Sabino "El tren de aterrizaje: Conjunto de ruedas y amortiguadores que permiten el despegue y aterrizaje. Los TCPs deben conocer su funcionamiento básico, como el tiempo durante el cual debe estar desplegado o retraído durante estas maniobras."
Sabino "Todos estos son los componentes básicos que ustedes deben aprender a reconocerlos fácilmente. En caso de que, por ejemplo, vean fuego en un ala en el despegue, sepan que quizás venga desde el motor de turbina y puedan notificar la información correcta."
Sabino "Anotaron lo necesario? Bien, seguimos."
Sabino "Además de las partes de la aeronave, es indispensable que sepan el funcionamiento básico de los motores y a diferenciarlos entre los diferentes tipos que existen."
Sabino "Existen los motores de Turbina (también llamados Jets). Los aviones comerciales modernos suelen estar equipados con motores de turbina, que funcionan tomando aire, comprimiéndolo, mezclándolo con combustible y quemándolo para generar empuje."
Sabino "Existen los motores de Pistón (comúnes en Aviación General). Aunque menos comunes en aviones comerciales grandes, los TCPs pueden estar expuestos a aeronaves más pequeñas con motores de pistón, que funcionan de manera similar a los motores de automóvil, utilizando cilindros para generar movimiento mecánico."
Sabino "Los TCPs deben estar familiarizados con los ruidos normales asociados con el funcionamiento del motor, como el aumento de la potencia durante el despegue o la reducción durante el aterrizaje. Deberían poder identificar ruidos o vibraciones inusuales que puedan indicar un problema."
Sabino "También tienen que tener en cuenta los sistemas principales del avión."
Sabino "El sistema electrico proporciona energía para la iluminación, los sistemas de entretenimiento, los equipos de comunicación y otros sistemas críticos. Es importante que los TCPs comprendan qué hacer en caso de un fallo eléctrico, como el uso de iluminación de emergencia."
Sabino "El sistema hidráulico controla los sistemas que requieren una gran cantidad de fuerza, como el tren de aterrizaje, los frenos y las superficies de control de vuelo. Conocer las ubicaciones de los componentes hidráulicos es útil en caso de emergencias que afecten estas áreas."
Sabino "Los sistemas de presurización y aire acondicionado mantienen la presión y el aire en niveles seguros y confortables dentro de la cabina. Los TCPs deben estar capacitados para actuar en caso de una despresurización, utilizando las máscaras de oxígeno y asegurando que los pasajeros también lo hagan."
Sabino "Y el sistema de combustible que distribuye el combustible a los motores de manera uniforme. Los TCPs deben tener conocimientos sobre la seguridad del combustible, especialmente en situaciones de emergencia como fuego a bordo."
Sabino "Ahora, que sucede en caso de que alguno de estos sistemas o partes del avión no funcionen correctamente? Para ello, tenemos procedimientos de emergencia relacionados a las aeronaves y motores correspondientes."
Sabino "Hay que saber cómo manejar una despresurización repentina, incluida la activación de las máscaras de oxígeno y la instrucción a los pasajeros sobre su uso."
Sabino "Los TCPs deben estar preparados para las posibles consecuencias de un fallo de motor, como un aterrizaje de emergencia, y cómo deben asistir en tales situaciones."
Sabino "Deben tener conocimiento de los procedimientos para manejar incendios en motores o en la cabina, incluyendo el uso de extintores y la coordinación con la cabina de mando."
Sabino "Y entender cómo la configuración de la aeronave afecta los procedimientos de evacuación y cómo guiar a los pasajeros hacia las salidas de emergencia de manera segura y rápida."
Sabino "Todo esto deben aprenderlo para poder solucionar cualquier incidiente dentro del avión, con ayuda de sus colegas de TCPs y una comunicación asertiva con la tripulación técnica."
Sabino "Los TCPs deben conocer la terminología básica utilizada por los pilotos y el personal técnico para poder comunicarse de manera efectiva durante las operaciones regulares y en situaciones de emergencia."
Sabino "Saber cómo y cuándo informar sobre anomalías observadas, como ruidos inusuales, vibraciones, o comportamiento extraño de los pasajeros que podría afectar la seguridad del vuelo."
Sabino "Este conocimiento técnico básico no solo ayuda a los TCPs a desempeñar mejor sus funciones diarias, sino que es crucial en situaciones de emergencia, donde una comprensión de los sistemas de la aeronave puede ser la diferencia entre una respuesta efectiva y una situación peligrosa. Además, este conocimiento les permite brindar información precisa y tranquilizadora a los pasajeros en momentos críticos, lo que es fundamental para mantener la calma y la seguridad a bordo."
Sabino "Bueno, eso ha sido todo por hoy. Espero que la clase les haya dado una idea un poco mas técnica del desempeño de sus futuras tareas."
Sabino "Como terminamos muy sobre la hora, les daré unos 20 minutos de descanso y para que puedan repasar sus apuntes. Marina en breve vendrá a dictar la prueba del dia de hoy. Mucha suerte a todos! Espero que hayan disfrutado del modulo de hoy tanto como a mi presentarlo. La clase de mañana estará a mi cargo nuevamente."

hide iSabino
with dissolve

#Modulo 5 - meteorologia basica


show iSabino at left
with fade

Sabino "Buenos dias a todos. Hoy concluimos la primera semana de curso. Asi que daremos un ultimo empujon hasta el tan deseado fin de semana, que me imagino estarán esperando."
Sabino "Como habrán visto en el calendário del curso, hoy daremos el módulo de meteorología básica."
Sabino "El conocimiento básico de meteorología es crucial para los Tripulantes de Cabina de Pasajeros, ya que les permite entender las condiciones atmosféricas que pueden afectar el vuelo y prepararse para manejar situaciones relacionadas con el clima de manera eficaz. Aquí te presento un resumen de los conceptos meteorológicos esenciales para los TCPs."
Sabino "Empecemos con los fundamentos de la meteorología."
Sabino "Primero. Los TCPs deben entender que la atmósfera está compuesta por varias capas (troposfera, estratosfera, etc.), pero la mayoría de los fenómenos meteorológicos que afectan el vuelo ocurren en la troposfera, que se extiende hasta unos 12 kMarina de altura."
Sabino "Segundo, deben entender la presión atmosférica. Es la fuerza que el aire ejerce sobre la superficie de la Tierra. Los TCPs deben conocer que las variaciones en la presión atmosférica pueden afectar la altitud y el rendimiento de la aeronave, así como la percepción de los pasajeros, especialmente durante el despegue y el aterrizaje."
Sabino "Tercero y no menos importante, la temperatura. La temperatura del aire disminuye con la altitud. Este enfriamiento afecta la densidad del aire, lo que a su vez puede influir en el rendimiento del avión y la formación de fenómenos como el hielo en las alas."
Sabino "Hasta aquí todo claro? Pues, seguimos."
Sabino "Otro conjunto de factores importantes son los fenómenos meteorológicos comunes."
Sabino "Como por ejemplo, las turbulencias. Hoy mencionaremos dos de ellas."
Sabino "Primero tenemos a la Turbulencia en Aire Claro (CAT). Ocurre en cielos despejados, generalmente en niveles altos, y no está asociada a nubes o tormentas. Puede ser difícil de prever, pero los TCPs deben saber cómo prepararse y preparar a los pasajeros cuando se anticipa."
Sabino "Después, tenemos la Turbulencia Convectiva. La misma es asociada con tormentas o formaciones nubosas como cúmulos o cumulonimbos, donde las corrientes de aire ascendente y descendente causan movimientos bruscos."
Sabino "Los TCPs deben asegurarse de que los pasajeros tengan el cinturón de seguridad abrochado cuando se anticipa turbulencia, asegurar todos los objetos sueltos en la cabina y estar preparados para suspender el servicio a bordo."
Sabino "Otro fenomeno común es la llamada Cizalladura del Viento"
Sabino "Es un cambio repentino en la velocidad o dirección del viento, especialmente peligroso durante el despegue y el aterrizaje. Los TCPs deben conocer su existencia, ya que puede causar movimientos bruscos o desviaciones en la trayectoria de la aeronave."
Sabino "Espero estén tomando apuntes de todo lo que les estoy diciendo, ya que es muchisima información para recordar."
Sabino "Tenemos las tormentas eléctricas. Anoten este nombre porque es muy dificil."
Sabino "Las cumulonimbos. Estas son nubes grandes y densas que pueden causar fuertes lluvias, granizo, rayos y turbulencias severas. Las tormentas eléctricas están asociadas con estas nubes y pueden hacer que el vuelo sea muy inestable."
Sabino "Durante tormentas eléctricas, los TCPs deben asegurarse de que todo esté asegurado en la cabina y prepararse para posibles cambios repentinos en la altitud y la dirección del vuelo."
Sabino "Llegando casi al final de nuestra lista, no podemos dejar de lado a la niebla."
Sabino "La niebla puede afectar la visibilidad durante el despegue y el aterrizaje, lo que puede llevar a retrasos o cambios en la programación del vuelo. Aunque no es peligroso en vuelo, los TCPs deben estar conscientes de su impacto en las operaciones de tierra."
Sabino "Y en último lugar tenemos al hielo."
Sabino "El hielo puede formarse en las alas y otras superficies de la aeronave cuando las temperaturas están por debajo del punto de congelación y hay humedad en el aire. Esto puede afectar la sustentación y el control del avión."
Sabino " Aunque el deshielo es principalmente responsabilidad de la tripulación técnica, los TCPs deben estar atentos a las indicaciones de los pilotos y saber cómo actuar si hay acumulación de hielo en la cabina, como en las ventanas."
Sabino "Antes de cada vuelo, los TCPs reciben un informe meteorológico que incluye información sobre las condiciones esperadas durante el vuelo y en el destino. Conocer cómo leer y entender estos informes básicos es fundamental para estar preparados."
Sabino "El ATIS (Automatic Terminal Information Service), es un informe continuo sobre las condiciones meteorológicas y operativas en un aeropuerto específico. Aunque más utilizado por los pilotos, los TCPs deben estar familiarizados con su contenido y propósito."
Sabino "Entender los símbolos meteorológicos básicos que indican tipos de nubes, precipitaciones, y vientos, es útil para los TCPs cuando reciben información meteorológica de la tripulación técnica."
Sabino "Todas estas son variables de las condiciones meteorologicas que pueden producir impacto en los pasajeros."
Sabino "Los cambios de altitud y presión pueden causar molestias en los oídos de los pasajeros, especialmente en despegues y aterrizajes. Los TCPs deben conocer técnicas para ayudar a los pasajeros a igualar la presión, como masticar chicle o realizar maniobras para abrir las trompas de Eustaquio."
Sabino "Algunos pasajeros pueden experimentar ansiedad o malestar físico durante la turbulencia. Los TCPs deben estar capacitados para brindar apoyo emocional y físico, como ofrecer agua, evitar el servicio de comidas durante turbulencias fuertes y mantener la calma."
Sabino "La baja humedad en la cabina puede causar deshidratación. Los TCPs deben estar atentos a ofrecer suficiente agua a los pasajeros y aconsejarles sobre cómo minimizar los efectos de la deshidratación."
Sabino "En caso de condiciones meteorologicas adversas, debemos apoyarnos en nuestros procedimientos"
Sabino "Antes de entrar en una zona de turbulencia o mal tiempo, los TCPs deben asegurar todo en la cabina, advertir a los pasajeros sobre la necesidad de abrocharse el cinturón y, si es necesario, suspender el servicio a bordo."
Sabino "Mantener una comunicación constante con la cabina de mando sobre las condiciones meteorológicas y seguir sus instrucciones en todo momento."
Sabino "En casos extremos, como despresurización o impactos de rayos, los TCPs deben estar preparados para seguir los procedimientos de emergencia, incluyendo el uso de máscaras de oxígeno y la coordinación de una posible evacuación."
Sabino "Estos conocimientos permiten a los TCPs manejar de manera efectiva cualquier situación relacionada con las condiciones meteorológicas, garantizando la seguridad y el confort de los pasajeros durante el vuelo." 

hide iSabino
with dissolve

#Modulo 6 - CRMarina Crew Resource MAgnament


show iMarina at left
with fade

Marina "Buenos dias a todos."
Marina "Espero hayan disfrutado de las clases del jueves y viernes con el Capitán Gentile."
Marina "Sabino Gentile es de las personas que mas tiempo han estado dentro de la companía en su rol."
Marina "Ha instruido a generaciones de excelentes profesionales. Inclusve a mi."
Marina "El día que empiecen a volar con nosotros, entenderán que es un referente, sobre todo para los nuevos ingresos."
Marina "Más allá de ello, espero que también hayan podido disfrutar de su primer fin de semana, trás un arduo entrenamiento."
Marina "Que hayan podido aprovechar para distenderse, y sobre todo, estudiar mas."
Marina "Si realmente desean esta posición, sabrán aprovechar cada instante, y el entrenamiento terminará antes de que puedan darse cuenta."
Marina "El dia de hoy hablaremos del CRMarina y sus implicaciones."
Marina "Saquen lápiz y papel, que hoy vamos a anotar mucho."
Marina "El Crew Resource Management (CRM), o Gestión de los Recursos de la Tripulación, es un conjunto de procedimientos de capacitación diseñados para mejorar la seguridad en la aviación mediante la promoción de una comunicación efectiva, la toma de decisiones, la resolución de problemas, y la coordinación entre todos los miembros de la tripulación, incluidos los pilotos, los Tripulantes de Cabina de Pasajeros (TCPs), y otros miembros del equipo."
Marina "Para los TCPs, el CRMarina es esencial porque su rol va más allá de atender a los pasajeros; son una parte crítica de la tripulación en la gestión de situaciones normales y de emergencia. El CRMarina ayuda a los TCPs a interactuar de manera efectiva con el resto de la tripulación y a contribuir a la seguridad del vuelo."
Marina "En Sky-Blue Airlines, lo dividimos en seis pilares principales."
Marina "El primero, la comunicación efectiva."
Marina "Efectiva en el intercambio de información. Los TCPs deben comunicarse clara y efectivamente con la cabina de mando y otros miembros de la tripulación. Esto incluye la capacidad de proporcionar información relevante de manera concisa y asegurarse de que los mensajes se entienden correctamente."
Marina " Y ademas tener escucha activa. Es crucial que los TCPs escuchen con atención y respondan apropiadamente a las instrucciones y la información proporcionada por la cabina de mando y otros miembros de la tripulación."
Marina "El pilar número dos es la conciencia situacional."
Marina "Este pilar se constituye de entender el entorno operacional. Los TCPs deben estar al tanto de las condiciones del vuelo, las posibles amenazas y las situaciones anómalas. Mantener una alta conciencia situacional significa estar siempre atentos a lo que sucede a bordo y estar preparados para actuar."
Marina "Y segundo pero no menos importante, reconocer indicadores de problemas. Esto incluye identificar señales de comportamiento inusual en los pasajeros, posibles riesgos de seguridad, o indicios de que algo podría no estar funcionando correctamente en la aeronave."
Marina "El tercer pilar está compuesto por la toma de decisiones."
Marina "Que implica en una parte, la evaluación de opciones. Evaluación de Opciones. Los TCPs deben ser capaces de evaluar rápidamente las opciones disponibles durante una situación de emergencia o conflicto y decidir cuál es la mejor acción a tomar."
Marina "Y por otra parte, el uso del juicio profesional. Esto implica aplicar el conocimiento y la experiencia de manera que se priorice siempre la seguridad de los pasajeros y la tripulación."
Marina "Nuestro cuarto pilar es el trabajo en equipo y coordinación."
Marina "Colaborar con el resto de la tripulación es muy importante. Los TCPs deben trabajar en estrecha colaboración con los pilotos, otros TCPs y, en ocasiones, con el personal de tierra, especialmente en situaciones que requieren una respuesta coordinada, como evacuaciones de emergencia."
Marina "Y ni que hablar del apoyo mutuo. Los TCPs deben estar dispuestos a ayudar y apoyar a sus compañeros de tripulación, compartiendo información y responsabilidades cuando sea necesario."
Marina "El quinto pilar es para mi el mas dificil, que es la gestión del estrés."
Marina "Es crucial poder mantener la calma bajo presión. Los TCPs deben poder manejar el estrés de manera efectiva, especialmente durante situaciones de emergencia, para tomar decisiones claras y racionales."
Marina "Y dentro de este pilar también aprenderemos técnicas de relajación. Es útil que los TCPs conozcan y apliquen técnicas para reducir el estrés, tanto para ellos mismos como para tranquilizar a los pasajeros."
Marina "Nuestro último pilar está compuesto por diferentes items referentes a la resolución de conflictos."
Marina "El primero sería el manejo de pasajeros conflictivos. El CRMarina incluye técnicas para manejar y desescalar conflictos con pasajeros, asegurando que el vuelo se mantenga seguro y que las situaciones potencialmente peligrosas se resuelvan de manera adecuada."
Marina "Y la negociación y persuasión. Los TCPs deben ser capaces de utilizar la persuasión y la negociación para obtener la cooperación de los pasajeros en situaciones difíciles."
Marina "Y bien, que les ha parecido? Son bastantes cosas que recordar, pero considero que todas ellas bastante intuitivas, una vez que entiendes el trabajo del TCP."
Marina "Ahora veremos la aplicación del CMR en situaciones reales."
Marina "Evacuaciones de Emergencia: En caso de una evacuación de emergencia, el CRMarina asegura que todos los miembros de la tripulación trabajen juntos de manera eficiente, siguiendo los procedimientos establecidos y comunicándose constantemente para asegurar que todos los pasajeros salgan del avión de manera segura."
Marina "Incidentes de Salud a Bordo: Si un pasajero sufre una emergencia médica, los TCPs deben coordinarse con los pilotos, otros TCPs, y, si es necesario, con el personal médico en tierra. Aquí, la comunicación efectiva y la toma rápida de decisiones son esenciales."
Marina "Turbulencia o Mal Tiempo: Durante turbulencia severa o condiciones meteorológicas adversas, los TCPs deben aplicar el CRMarina para asegurar que todos los pasajeros están seguros, comunicarse con la cabina de mando sobre las condiciones en la cabina, y coordinar cualquier acción necesaria para mantener la seguridad."
Marina "El CRMarina trae muchisimos beneficios para todos los TCPs, porque sistematiza procesos que son dificiles de deducir en situaciones complejas. El poder organizar estas practicas mentalmente nos ayuda a recordarlas."
Marina "Ni que hablar como mejoran la seguridad del vuelo. Al promover la comunicación y la coordinación efectiva, el CRMarina reduce el riesgo de errores humanos y mejora la respuesta de la tripulación en situaciones críticas."
Marina "Aumenta la Eficiencia Operacional. Una tripulación que utiliza CRMarina de manera efectiva puede manejar situaciones inesperadas de manera más fluida, minimizando interrupciones y asegurando un vuelo más eficiente."
Marina "Fortalece el Trabajo en Equipo. El CRMarina fomenta un ambiente de trabajo en equipo, donde todos los miembros de la tripulación se apoyan mutuamente y trabajan juntos hacia un objetivo común: la seguridad y el éxito del vuelo."
Marina "El CRMarina es, por lo tanto, una herramienta fundamental para los TCPs, ayudándolos a desempeñar su papel de manera efectiva y asegurando que contribuyen positivamente a la seguridad y el bienestar de todos a bordo."

hide iMarina
with dissolve

#Modulo 7 - Modulo AVSEC (Seguridad en la aviación, Safety y Security)


show iMarina at left
with fade

Marina "Buenos dias. Cómo están?"
Marina "Espero estén descansados y con muchas ganas de aprender, porque el día de hoy vamos a ver la columna vertebral de lo que sería la función de TCP."
Marina "Hoy hablaremos de la seguridad en la aviación. Motivo por el cual se creó la función del TCP."
Marina "Empezaremos a utilizar la sigla AVSEC, que corresponde a Seguridad en aviación, safety and security."
Marina "Vayan haciendose a la idea que aprenderán muchas terminologias en inglés, inclusive inglés técnico es un módulo a futuro."
Marina "Lapiz y papel en mano. Empecemos."
Marina "AVSEC es una abreviatura de Aviation Security (Seguridad en la Aviación), un campo crucial en la aviación que se enfoca en proteger a los pasajeros, la tripulación, la aeronave y las instalaciones aeroportuarias de actos ilícitos, como terrorismo, sabotaje, interferencias ilegales, y otros riesgos de seguridad. Para un Tripulante de Cabina de Pasajeros (TCP), entender AVSEC es fundamental para desempeñar sus responsabilidades de manera segura y eficiente."
Marina "Aunque existen diferencias conceptuales entre safety y security."
Marina "Safety se refiere a la prevención de accidentes e incidentes relacionados con la operación segura de la aeronave. Involucra procedimientos, sistemas y capacitación destinados a proteger a la tripulación y a los pasajeros de riesgos derivados de fallos mecánicos, errores humanos o condiciones adversas. Ejemplos incluyen procedimientos de evacuación, manejo de turbulencias, y respuesta a emergencias médicas."
Marina "Por otra parte, security se e refiere a la protección contra actos de interferencia ilícita, como terrorismo, secuestros, sabotaje, y otras actividades criminales. Involucra medidas preventivas y reactivas para asegurar que los vuelos, aeropuertos y aviones no sean blanco de estos actos. Ejemplos incluyen controles de seguridad en los aeropuertos, manejo de pasajeros conflictivos, y procedimientos en caso de amenazas de bomba."
Marina "El AVSEC para un TCP está repleto de responsabilidades y procedimientos."
Marina "Los primeros de ellos corresponden a los conocimientos de cumplimientos y normativas."
Marina "Los TCPs deben estar familiarizados con las regulaciones AVSEC tanto a nivel nacional como internacional, incluyendo aquellas emitidas por organizaciones como la Organización de Aviación Civil Internacional (OACI) y las autoridades locales de aviación civil."
Marina "Deben entender las políticas de seguridad de la aerolínea, como el manejo de equipaje no reclamado, la detección de pasajeros sospechosos, y los procedimientos en caso de amenazas de seguridad."
Marina "Segundo, el control y supervisión de seguridad a bordo."
Marina "Algunos de estos mencionamos anteriormente."
Marina "Como la revisión de Cabina."
Marina "Antes del embarque, los TCPs realizan inspecciones de la cabina para asegurarse de que no haya objetos extraños o sospechosos. También revisan las áreas de almacenamiento, baños y otros compartimentos."
Marina "La supervisión durante el embarque."
Marina "Los TCPs deben estar atentos al comportamiento de los pasajeros durante el embarque, buscando señales de comportamiento sospechoso o nervioso que puedan indicar una amenaza de seguridad."
Marina "En tercer lugar, hablamos del manejo de situaciones de seguridad."
Marina "Es muy importante, por ejemplo, es el manejo de pasajeros conflictivos."
Marina "Los TCPs están entrenados para manejar pasajeros conflictivos o agresivos de manera que se minimicen los riesgos para la seguridad del vuelo. Esto puede incluir la desescalada de situaciones o, en casos extremos, la solicitud de la intervención de las autoridades."
Marina "A veces, los conflictos pueden escalar a amenazas."
Marina "En caso de amenazas a bordo, como una posible bomba a bordo o un intento de secuestro, los TCPs deben seguir protocolos específicos que incluyen notificar inmediatamente a la cabina de mando, asegurar la cabina, y preparar a los pasajeros para una posible evacuación o respuesta de emergencia."
Marina "Mas allá de los problemas generados exclusivamente por personas, están las circunstanciales."
Marina "Para ello, tenemos los procedimientos de seguridad en emergencias."
Marina "La primera y principal, evacuación de emergencia."
Marina "En situaciones donde la seguridad esté comprometida (por ejemplo, un incendio o una amenaza de bomba), los TCPs deben ser capaces de ejecutar una evacuación rápida y segura, utilizando los procedimientos entrenados."
Marina "La segunda, es la coordinación con la cabina de mando."
Marina "Los TCPs deben mantener una comunicación constante con la cabina de mando durante cualquier incidente de seguridad, siguiendo sus instrucciones y proporcionando información sobre la situación en la cabina."
Marina "Todo el tiempo se están desarrollando nuevas técnicas y nuevos procedimientos."
Marina "Es imperante para el TCP la capacitación continua en seguidad."
Marina  "Los TCPs reciben entrenamiento regular en seguridad en aviación, que incluye la identificación de amenazas, manejo de conflictos, procedimientos de evacuación y uso de equipos de seguridad. Este entrenamiento se actualiza periódicamente para incluir nuevas amenazas y tecnologías."
Marina "Participan en simulacros que simulan situaciones de seguridad, como secuestros o amenazas de bomba, para asegurarse de que están preparados para responder de manera efectiva en una situación real."
Marina "Asi como ustedes también participaran, en breve."
Marina "Es una excelente practica tambien mantener buena relacion con las autoridades de seguridad."
Marina "Los TCPs trabajan en conjunto con las autoridades de seguridad aeroportuaria para garantizar que se sigan todos los procedimientos de seguridad antes del vuelo, como el control de equipaje y la verificación de pasajeros."
Marina "Después de cualquier incidente relacionado con la seguridad, los TCPs deben elaborar informes detallados que se envían a la aerolínea y a las autoridades pertinentes para su análisis y acción."
Marina "Como verán, el AVSEC para los TCPs es de gran importancia."
Marina "La principal responsabilidad de los TCPs es garantizar la seguridad de todos a bordo. El conocimiento y la aplicación de los principios AVSEC son fundamentales para cumplir con esta responsabilidad."
Marina "Al estar capacitados en AVSEC, los TCPs pueden identificar y prevenir actos ilícitos antes de que se conviertan en amenazas, protegiendo así el vuelo y todos los involucrados."
Marina "La capacitación en AVSEC refuerza la confianza de los TCPs en su capacidad para manejar situaciones difíciles, lo que a su vez se traduce en una mayor seguridad y tranquilidad para los pasajeros."
Marina "En resumen, AVSEC es una parte integral del rol de los TCPs, que abarca desde la prevención de amenazas hasta la gestión de emergencias de seguridad, garantizando la protección y el bienestar de todos a bordo."

hide iMarina
with dissolve

#Modulo 8 - Mercancias peligrosas


show iMarina at left
with fade

Marina "Buenos dias, cómo están todos el dia de hoy?"
Marina "Espero que estén bien."
Marina "La clase de hoy va a ser un poco mas larga, por lo que vamos a hacer dos descansos de 20 minutos."
Marina "El módulo de hoy es de mercancías peligrosas"
Marina "Para los Tripulantes de Cabina de Pasajeros, el conocimiento sobre mercancías peligrosas es crucial para garantizar la seguridad a bordo. Las mercancías peligrosas son artículos o sustancias que pueden presentar un riesgo para la salud, la seguridad o la propiedad si no se manejan correctamente."
Marina "Aquí te presento un resumen de los aspectos más importantes que un TCP debe conocer sobre mercancías peligrosas."
Marina "Primero debemos entender la clasificación de mercancías peligrosas."
Marina "Existen diferentes categorias de riesgo."
Marina "Las mercancías peligrosas se dividen en varias categorías según el tipo de riesgo que representan. Estas categorías incluyen explosivos, gases, líquidos inflamables, sustancias tóxicas, materiales radiactivos, y otros. Conocer estas categorías ayuda a los TCPs a identificar y manejar los riesgos potenciales."
Marina "Luego deberiamos identificar las etiquetas y marcas"
Marina "Las mercancías peligrosas están etiquetadas con símbolos específicos que indican el tipo de peligro que representan. Los TCPs deben familiarizarse con estas etiquetas para reconocer los riesgos asociados."
Marina "En segundo lugar, conocernos las regulaciones y documentación"
Marina "Cómo se podrán imaginar, existen regulaciones internacionales."
Marina "Los TCPs deben conocer las regulaciones internacionales que rigen el transporte de mercancías peligrosas, como las establecidas por la Organización de Aviación Civil Internacional (OACI) y la Asociación Internacional de Transporte Aéreo (IATA)."
Marina "Y deben conocerse la documentación a bordo"
Marina "Aunque no manejan directamente la documentación de mercancías peligrosas, los TCPs deben saber que se deben llevar documentos específicos que declaren la naturaleza de las mercancías peligrosas transportadas."
Marina "Número tres, identificación y manejo a bordo"
Marina "Los TCPs deben estar atentos a las etiquetas y advertencias en el equipaje y los contenedores de carga que indiquen la presencia de mercancías peligrosas."
Marina "Aunque la manipulación y carga de mercancías peligrosas son responsabilidad del personal de tierra y de la tripulación técnica, los TCPs deben conocer los procedimientos para reportar cualquier sospecha o incidencia relacionada con mercancías peligrosas."
Marina "En cuarto lugar, deben aprender los procedimientos en caso de incidente"
Marina "Los TCPs deben estar capacitados en los procedimientos específicos a seguir en caso de un incidente relacionado con mercancías peligrosas, como derrames, fugas, o incendios. Esto incluye"
Marina "En primer lugar, la tan renombrada evacuación"
Marina "Conocer cómo evacuar la cabina de manera segura si se detecta un peligro relacionado con mercancías peligrosas."
Marina "También es importante saber usar los equipos de seguridad"
Marina "Saber cómo utilizar los equipos de seguridad a bordo, como extinguidores de incendios, y aplicar los procedimientos de emergencia según el tipo de mercancía peligrosa involucrada."
Marina "Y saber hacer reportes. Informar inmediatamente a la cabina de mando y seguir sus instrucciones para manejar la situación de manera efectiva."
Marina "Pasando a la quinta sección, llegamos a la capacitación y procedimientos estándar"
Marina "Empezamos por la capacitación regular"
Marina "Los TCPs deben recibir capacitación regular sobre la identificación y el manejo de mercancías peligrosas. Esta capacitación incluye simulacros y estudios de casos para prepararse para situaciones de emergencia."
Marina "Y los procedimientos de la aerolinea"
Marina "Deben seguir los procedimientos específicos de su aerolínea para el manejo de mercancías peligrosas, que incluyen las directrices para la identificación, la notificación y la gestión de emergencias."
Marina "Llegamos a la sexta sección, la comunicación y coordinación"
Marina "Coordinación con la tripulación"
Marina "Los TCPs deben mantener una comunicación eficaz con la cabina de mando y otros miembros de la tripulación para asegurar que se sigan los procedimientos adecuados en caso de un incidente con mercancías peligrosas."
Marina "Comunicación con los pasajeros"
Marina "Aunque no son responsables de manejar mercancías peligrosas directamente, los TCPs deben estar preparados para comunicar a los pasajeros la información relevante y las instrucciones durante una emergencia relacionada con mercancías peligrosas."
Marina "Y la ultima sección de esta primera parte"
Marina "Llegamos a la revisión de políticas y procedimientos"
Marina "Aqui tenemos un unico punto, la actualización de información."
Marina "Los TCPs deben mantenerse actualizados sobre cualquier cambio en las políticas y procedimientos relacionados con el transporte de mercancías peligrosas, ya que estas regulaciones pueden cambiar con el tiempo."
Marina "Y bien, hasta aqui la primera parte del dia de hoy, nos tomamos un descanso y volvemos en 20 minutos"

hide iMarina
with dissolve

show iDaria
with fade
Daria "..."

hide iDaria
with dissolve

show iMarina at left
with fade

Marina "Bienvenidos de nuevo a la segunda parte del dia de hoy."
Marina "En esta segunda parte vamos a hablar del conocimiento de mercancías peligrosas para los TCPs"
Marina "El conocimiento sobre mercancías peligrosas permite a los TCPs tomar medidas rápidas y efectivas para prevenir y manejar situaciones peligrosas, protegiendo a los pasajeros y a la tripulación."
Marina "Los TCPs deben estar preparados para manejar emergencias relacionadas con mercancías peligrosas, lo que puede minimizar el riesgo y los daños potenciales."
Marina "Cumplir con las regulaciones de seguridad para el transporte de mercancías peligrosas es esencial para el funcionamiento seguro de las operaciones aéreas y para la protección de todos los involucrados en el vuelo."
Marina "En resumen, aunque los TCPs no manejan directamente las mercancías peligrosas, su conocimiento y preparación en este tema son esenciales para garantizar una respuesta segura y efectiva en caso de incidentes relacionados."
Marina "En la aviación, las mercancías peligrosas se clasifican en varias categorías basadas en los riesgos que representan para la seguridad del vuelo, la salud de las personas y la integridad de la aeronave."
Marina "Estas categorías están definidas por las regulaciones internacionales, como las establecidas por la Organización de Aviación Civil Internacional (OACI) y la Asociación Internacional de Transporte Aéreo (IATA)."
Marina "Aquí tienes una lista de las categorías de mercancías peligrosas más comunes"
Marina "Explosivos"
Marina "Son todos aquellos materiales o sustancias que pueden explotar bajo ciertas condiciones, como explosivos, fuegos artificiales y municiones."
Marina "Ejemplos: Dynamita, petardos, municiones."
Marina "Gases"
Marina "Son todas aquellas sustancias que se encuentran en estado gaseoso a temperatura y presión normales o que se convierten en gas bajo condiciones normales."
Marina "Dentro de esta categoría estan los gases comprimidos"
Marina "Gases almacenados a alta presión, como oxígeno y nitrógeno."
Marina "Los gases refrigerados"
Marina "Gases que se convierten en líquido a bajas temperaturas, como el propano."
Marina "Gases tóxicos y corrosivos"
Marina "Gases que pueden ser perjudiciales para la salud o corrosivos para materiales."
Marina "Algunos ejemplos, Oxígeno líquido, dióxido de carbono, cloro."
Marina "Tercero, liquidos inflamables"
Marina "Líquidos que pueden encenderse fácilmente a temperatura ambiente."
Marina "Cuarto, solidos inflamables"
Marina "Sustancias sólidas que pueden causar fuego a través de una reacción química o que son fácilmente inflamables."
Marina "Ejemplos: Azufre, fósforos, magnesio."
Marina "Están anotando todo? lo van a necesitar para el test de hoy"
Marina "Bien, seguimos"
Marina "Sustancias Combustibles"
Marina "Sustancias que son capaces de arder y generar calor en ciertas condiciones."
Marina "Ejemplos: Aceites, grasas, productos químicos industriales."
Marina "Sustancias Tóxicas e Infecciosas"
Marina "Sustancias que pueden causar daño a la salud humana o animal, o que contienen agentes infecciosos."
Marina "De las cuales existen dos categorias"
Marina "Sustancias tóxicas, que pueden causar efectos adversos graves en la salud si se inhalan, ingieren o tocan."
Marina "Y sustancias infecciosas, que contienen patógenos que pueden causar enfermedades."
Marina "Ejemplos: Productos químicos tóxicos, muestras biológicas para laboratorio."
Marina "Materiales Radiactivos"
Marina "Son todos aquellos materiales que emiten radiación ionizante y pueden ser perjudiciales para la salud y el medio ambiente."
Marina "Ejemplos, uranio, cesio, materiales usados en equipos médicos."
Marina "Corrosivos"
Marina "Sustancias que pueden corroer o destruir materiales vivos o no vivos."
Marina "Ejemplos, Ácidos fuertes (como el ácido sulfúrico), bases (como el hidróxido de sodio)."
Marina "Otros Materiales Peligrosos"
Marina "Cualquier otra sustancia o material que, aunque no encaje en las categorías anteriores, presenta un riesgo para la seguridad y debe ser manejado con cuidado."
Marina "Materiales que podrían no estar específicamente clasificados pero que son peligrosos bajo ciertas condiciones."
Marina "Clasificación y Etiquetado"
Marina "Cada tipo de mercancía peligrosa tiene etiquetas específicas que indican el tipo de riesgo que presenta."
Marina "Estas etiquetas incluyen símbolos y colores que deben ser reconocidos por todos los miembros de la tripulación para garantizar una respuesta adecuada."
Marina "Regulaciones y Directrices"
Marina "Las mercancías peligrosas en aviación están reguladas por:"
Marina "ICAO (Organización de Aviación Civil Internacional): A través del Technical Instructions for the Safe Transport of Dangerous Goods by Air (TIs)."
Marina "IATA (Asociación Internacional de Transporte Aéreo): Con el IATA Dangerous Goods Regulations (DGR), que proporciona directrices para el transporte seguro de mercancías peligrosas en la aviación."
Marina "Estos regulaciones aseguran que las mercancías peligrosas se manejen, transporten y carguen de manera segura para minimizar los riesgos durante el vuelo. Los TCPs deben estar familiarizados con estas categorías para identificar y manejar cualquier posible incidente relacionado con mercancías peligrosas que puedan ocurrir a bordo."

hide iMarina
with dissolve


#Modulo 9 - Procedimientos de emergencia

show iMarina at left
with fade

Marina "Buenos dias a todos"
Marina "Hoy vamos a profundizar en los procedimientos de emergencia que venimos hablando las últimas clases"
Marina "Algunos de ellos los vamos intentar en nuestra semana de prácticas"
Marina "Pero hasta entonces, saquen lapiz y papel que vamos a comenzar"
Marina "Los procedimientos de emergencia para los Tripulantes de Cabina de Pasajeros (TCPs) son fundamentales para garantizar la seguridad de todos a bordo en situaciones críticas."
Marina "Estos procedimientos se dividen en diferentes categorías según el tipo de emergencia, y los TCPs deben estar bien entrenados en cada uno de ellos para responder de manera efectiva. Aquí te detallo los procedimientos de emergencia más importantes"
Marina "Procedimientos en Caso de Evacuación de Emergencia"
Marina "Dentro de la preparación tenemos dos puntos"
Marina "Familiarizarse con las salidas de emergencia y las rutas de evacuación de la aeronave. Revisa los equipos y procedimientos de evacuación antes del vuelo."
Marina "Y Asegurarse de que los equipos de evacuación, como las balsas salvavidas y los infladores, estén en buen estado y accesibles."
Marina "Luego, dentro de las acciones tenemos varios puntos"
Marina "En caso de evacuación, sseguir las instrucciones de la cabina de mando para hacer el anuncio. Usa el megáfono si es necesario para garantizar que todos los pasajeros escuchen las instrucciones."
Marina "Abrir las salidas de emergencia según el procedimiento específico de la aeronave. Usa el tobogán de evacuación si está disponible."
Marina "Dirigir a los pasajeros hacia las salidas de emergencia, asegurandose de que se mantengan calmados y sigan las instrucciones. Ayudar a los pasajeros con movilidad reducida si es necesario."
Marina "Y por último, la verificación"
Marina "Asegúrate de que todas las áreas de la cabina estén evacuadas antes de abandonar la aeronave."
Marina "Tambien tenemos un grupo de procedimientos en caso de incendio a bordo"
Marina "En cuanto a la preparación, debemos familiarizarnos con los procedimientos específicos para diferentes tipos de incendios"
Marina "Cómo lo pueden ser incendios en la cabina, en la cocina o en el compartimiento de carga"
Marina "La primera acción que debemos tomar es el control del fuego"
Marina "Usar el extintor apropiado para controlar el fuego. Seguir las instrucciones del fabricante para el uso del extintor."
Marina "Informar a la cabina de mando sobre la situación y sigue sus instrucciones."
Marina "Si el incendio es incontrolable, prepárate para una evacuación parcial o total."
Marina "Procedimientos en Caso de Despresurización"
Marina "En nuestra preparación para este procedimientos debemos conocer la ubicación de las máscaras de oxígeno y cómo usarlas."
Marina "Y familiarizarnos con los procedimientos de emergencia en caso de despresurización de la cabina"
Marina "En las acciones debemos colocar nuestra propia máscara de oxígeno antes de ayudar a los pasajeros. Luego, asiste a los pasajeros en la colocación de sus máscaras."
Marina "Indicar a los pasajeros cómo usar las máscaras de oxígeno y asegurarse de que estén colocadas correctamente."
Marina "Prepárate para el descenso de emergencia si es necesario. Informa a los pasajeros sobre el procedimiento y mantén la calma."
Marina "Procedimientos en Caso de Emergencia Médica"
Marina "Familiarízate con el equipo médico a bordo, como el kit de primeros auxilios y el desfibrilador (AED), si está disponible."
Marina "Evalúa la condición del pasajero y proporciona primeros auxilios básicos según sea necesario."
Marina "Si el pasajero requiere asistencia médica avanzada, informa a la cabina de mando y solicita la ayuda de cualquier profesional médico a bordo."
Marina "Informa a la cabina de mando y coordina con el personal médico en tierra para preparar una atención adecuada a la llegada."
Marina "Procedimientos en Caso de Amenaza de Seguridad"
Marina "Conoce los procedimientos de seguridad para manejar amenazas, como secuestros o bombas."
Marina "Informa inmediatamente a la cabina de mando sobre cualquier amenaza o comportamiento sospechoso."
Marina "Sigue las instrucciones de la cabina de mando y coordina con el resto de la tripulación para asegurar la seguridad de los pasajeros."
Marina "Mantén la calma y asegúrate de que los pasajeros sigan las instrucciones de manera ordenada y segura."
Marina "Procedimientos en Caso de Turbulencia Severas"
Marina "Asegúrate de que los pasajeros estén sentados y con los cinturones de seguridad abrochados durante la turbulencia."
Marina "Permanece sentado con el cinturón de seguridad abrochado durante la turbulencia severa. Evita moverte por la cabina a menos que sea absolutamente necesario."
Marina "Asegúrate de que los pasajeros sigan las instrucciones para su seguridad durante la turbulencia."
Marina "Los procedimientos de emergencia garantizan que los TCPs puedan proteger y evacuar a los pasajeros de manera segura en situaciones críticas."
Marina "Un conocimiento claro y entrenado en los procedimientos de emergencia permite una respuesta rápida y eficiente, reduciendo el riesgo de lesiones y daños."
Marina "Seguir los procedimientos de emergencia asegura el cumplimiento de las normativas y regulaciones de seguridad de la aviación, lo cual es esencial para la operación segura del vuelo."
Marina "En resumen, los procedimientos de emergencia son una parte integral del entrenamiento y la responsabilidad de los TCPs. Estar bien preparado y capacitado en estos procedimientos es esencial para manejar cualquier situación de emergencia que pueda surgir durante el vuelo."

hide iMarina
with dissolve

#Modulo 10 - Primeros auxilios


image iVlad = "crew3.png"
show iVlad at left
with fade

Vlad "Buenas tardes"
Vlad "Y bienvenidos al modulo de primeros auxilios, soporte vital básico, RCP y manejo de desfibrilador"
Vlad "Mi nombre es Vlad, y seré su instructor el resto del dia."
Vlad "Hoy veremos la teoría por detrás de los primeros auxilios, mas adelante tendremos talleres practicos con los que aprueben la prueba."
Vlad "Les sugiero que saquen lápiz y papel para comenzar la clase, pero no se preocupen, podrán usar sus propios apuntes luego"
Vlad "Bien, empecemos"
Vlad "Los Tripulantes de Cabina de Pasajeros deben tener conocimientos sólidos en primeros auxilios para poder manejar emergencias médicas a bordo."
Vlad "Estos conocimientos les permiten proporcionar atención inmediata y adecuada en situaciones de emergencia hasta que se pueda obtener ayuda médica profesional. Aquí están los aspectos clave de primeros auxilios que un TCP debe saber"
Vlad "El primer paso es la evaluación inicial"
Vlad "Verificar el estado de conciencia"
Vlad "Evalúa si la persona está consciente y respondiendo. Si la persona no responde, verifica su respiración y pulso."
Vlad "El segundo paso sería la chequear la seguridad del escenario"
Vlad "Asegúrense de que el área sea segura para ustedes y para la persona afectada antes de proceder."
Vlad "Luego, veremos los pasos a seguir para iniciar una reanimación cardiopulmonar, en caso de que la situación lo amerite"
Vlad "Lo primero que tenemos que aprender es a reconocer una parada cardiaca"
Vlad "Deben realizar compresiones torácicas profundas y rápidas en el centro del pecho. La frecuencia recomendada es de 100-120 compresiones por minuto."
Vlad "Si están capacitados y consideran seguro hacerlo, deberán administrar respiraciones artificiales después de cada 30 compresiones, usando la técnica de boca a boca o un dispositivo de barrera."
Vlad "Ahora, veremos los pasos a seguir para usar un desfibrilador externo automatico. Abreviado DEA"
Vlad "Primero que nada, deben saber donde está la ubicación del DEA dentro de la aeronave"
Vlad "Familiarízate con la ubicación del DEA a bordo y cómo usarlo. El dispositivo proporciona instrucciones claras para administrar una descarga eléctrica si se detecta una arritmia que requiere desfibrilación."
Vlad "Y no nos olvidemos de la preparación"
Vlad "Asegúrate de que la persona esté en una superficie dura y seca antes de aplicar los parches del DEA"
Vlad "Tenemos otros diversos procedimientos con los cuales deberiamos aprender a lidiar"
Vlad "Entre ellos, el manejo de heridas y hemorragias"
Vlad "Para controlar el sangrado, deberán aplicar presión directa sobre la herida con un vendaje limpio para detener el sangrado. Si el sangrado es severo, eleva la extremidad herida."
Vlad "Limpien las heridas con agua limpia si es posible, y cubre con un vendaje estéril. En caso de heridas profundas o graves, aplica un vendaje de presión."
Vlad "Otro de los procedimientos que debemos aprender es el tratamiento de quemaduras"
Vlad "Deberán enfriar la quemadura con agua tibia (no fría) durante al menos 10 minutos. Evitar aplicar hielo directamente sobre la quemadura."
Vlad "Cubre la quemadura con un vendaje estéril y no adhesivo. No rompas las ampollas si se forman."
Vlad "Ahora veremos el procedimiento de manejo de la asfixia"
Vlad "Me imagino que han oído hablar de la maniobra de Heimlich"
Vlad "Deberán realizar la maniobra de Heimlich si una persona está consciente y presenta signos de obstrucción de las vías respiratorias. Asegúrate de seguir la técnica adecuada para adultos, niños y lactantes."
Vlad "Si la persona está inconsciente, realiza compresiones torácicas mientras revisas la boca para posibles objetos que obstruyan las vías respiratorias."
Vlad "Siguiente procedimiento: Tratamiento de deshidratación y shock"
Vlad "En caso de deshidratación, si el paciente está consciente, proporciona líquidos claros si sospechas de deshidratación."
Vlad "En caso de que se requiera un tratamiento de shock, coloca a la persona en posición acostada con las piernas elevadas, mantén su temperatura y asegúrate de que respire adecuadamente. Evita darle comida o bebida si está inconsciente o semiinconsciente."
Vlad "Siguiente procedimiento: Reconocimiento y Manejo de Condiciones Comunes"
Vlad "En caso de ataque de asma, Ayuda a la persona a usar su inhalador de rescate. Si no hay mejora, busca asistencia médica."
Vlad "Para personas con diabetes, observa signos de hipoglucemia (bajo nivel de azúcar en sangre) y administra azúcar o glucosa si están conscientes y pueden tragar."
Vlad "Durante una convulsión, mantén a la persona en un lugar seguro y alejado de objetos peligrosos. No intentes sujetar la lengua ni restringir el movimiento."
Vlad "Atención de Emergencias Médicas Específicas"
Vlad "Convulsiones: Mantén a la persona en una posición segura y monitorea la duración de la convulsión. Después de la convulsión, verifica su conciencia y respira normalmente."
Vlad "Reacciones Alérgicas Severas: Si una persona muestra signos de anaflaxia (dificultad para respirar, hinchazón), utiliza un autoinyector de epinefrina si está disponible."
Vlad "Ahora probablemente el apartado mas importante que verán en el día, el de Comunicación con Personal Médico"
Vlad "Deberán saber informar"
Vlad "Proporcionar detalles claros sobre la condición del paciente a los servicios médicos en tierra para preparar una respuesta adecuada al aterrizar."
Vlad "Y deberán llenar documentación"
Vlad "Lleva un registro de los primeros auxilios proporcionados y cualquier cambio en la condición del paciente."
Vlad "Es de suma importancia que tengan conocimientod e los primeros auxilios apra TCPs"
Vlad "Intervención Rápida: La capacidad de intervenir de manera rápida y efectiva en emergencias médicas puede salvar vidas y reducir la gravedad de las lesiones o enfermedades."
Vlad "Confianza y Eficiencia: Los TCPs capacitados en primeros auxilios pueden actuar con confianza y eficacia, manteniendo la calma y manejando la situación de manera profesional."
Vlad "Cumplimiento de Regulaciones: Las regulaciones de aviación requieren que los TCPs estén capacitados en primeros auxilios como parte de su entrenamiento, asegurando el cumplimiento de normas de seguridad y la preparación para emergencias médicas."
Vlad "En resumen, el conocimiento y la habilidad en primeros auxilios son esenciales para los TCPs, permitiéndoles proporcionar atención inmediata y adecuada durante emergencias médicas y asegurando la seguridad y bienestar de los pasajeros y la tripulación."
Vlad "Nos queda media clase, asi que aprovechen a descansar o estudiar, como prefieran"
Vlad "Nos vemos en la proxima con los talleres practicos"

hide iVlad
with dissolve

#Modulo 11 - Atencion al cliente, servicio a bord y sala VIP

show iMarina at left
with fade

Marina "Buenas tardes, cómo están?"
Marina "Espero que bien. Hoy vamos a hablar de una de nuestras funciones colaterales dentro del avión, que es la atención al cliente, servicio a bordo y sala VIP."
Marina "Quizá no sea el trabajo primario, pero hará parte de su rutina diaria."
Marina "La atención al cliente, el servicio a bordo y los protocolos para los Tripulantes de Cabina de Pasajeros son fundamentales para ofrecer una experiencia de vuelo segura y agradable."
Marina "A continuación, te detallo los aspectos clave en cada una de estas áreas"
Marina "Tomen lápiz y papel que vamos a anotar bastante"
Marina "Empezamos con la Atención al Cliente"
Marina "Cordialidad y Profesionalismo: Los TCPs deben mantener una actitud amable, respetuosa y profesional en todo momento. La cortesía y la empatía son esenciales para crear una atmósfera agradable para los pasajeros."
Marina "Comunicación Eficaz: Es importante comunicarse claramente con los pasajeros, proporcionando información sobre el vuelo, los procedimientos de seguridad y cualquier cambio que pueda ocurrir. Utiliza un lenguaje sencillo y evita jerga técnica cuando sea posible."
Marina "Gestión de Quejas y Solicitudes: Maneja las quejas y solicitudes de los pasajeros con paciencia y resolución. Escucha atentamente, ofrece soluciones apropiadas y busca la ayuda de la cabina de mando si es necesario para resolver problemas que no puedes solucionar directamente."
Marina "Atención Personalizada: Adapta el servicio a las necesidades individuales de los pasajeros, como atender a familias con niños, pasajeros con movilidad reducida, o aquellos con necesidades especiales. Proporciona asistencia personalizada para mejorar su experiencia de vuelo."
Marina "Número 2, servicio a Bordo"
Marina "Distribución de Comidas y Bebidas: Sirve las comidas y bebidas de manera eficiente y ordenada. Asegúrate de seguir los procedimientos específicos de la aerolínea para la distribución de alimentos y bebidas, incluyendo la gestión de dietas especiales y restricciones alimenticias."
Marina "Mantenimiento del Orden en la Cabina: Mantén la cabina limpia y ordenada durante el vuelo. Recoge los desechos de manera oportuna y asegura que los compartimentos de almacenamiento estén organizados."
Marina "Entretenimiento y Confort: Proporciona información sobre los sistemas de entretenimiento a bordo y ayuda a los pasajeros con cualquier problema relacionado. Asegúrate de que los pasajeros estén cómodos y que tengan acceso a mantas, almohadas y otros artículos necesarios."
Marina "Atención a Pasajeros con Necesidades Especiales: Ofrece asistencia a pasajeros con discapacidades, niños no acompañados y otros que puedan requerir ayuda adicional durante el vuelo."
Marina "Número 3. Protocolos de TCP"
Marina "Seguridad y Procedimientos de Emergencia: Asegúrate de que todos los pasajeros conozcan los procedimientos de seguridad y las ubicaciones de las salidas de emergencia. Realiza demostraciones de seguridad al comienzo del vuelo y ofrece información adicional si es necesario."
Marina "Procedimientos de Embarque y Desembarque: Coordina el embarque y desembarque de los pasajeros de manera eficiente. Asegúrate de que todos los pasajeros estén sentados y con el cinturón de seguridad abrochado durante el despegue y el aterrizaje."
Marina "Manejo de Situaciones Especiales: Sigue los procedimientos establecidos para situaciones especiales, como el manejo de mercancías peligrosas, el tratamiento de emergencias médicas y la gestión de comportamientos disruptivos o pasajeros conflictivos."
Marina "Cumplimiento de Regulaciones: Adhiérete a las regulaciones y procedimientos de la aerolínea y las normativas de aviación civil, que incluyen el cumplimiento de las leyes locales e internacionales relacionadas con el servicio a bordo y la seguridad."
Marina "Protocolos de Higiene y Sanitización: Sigue los protocolos de higiene y sanitización para prevenir la propagación de enfermedades, especialmente en áreas de alto contacto. Mantén las áreas de servicio limpias y desinfectadas."
Marina "Número 4. Protocolos Específicos para la Atención a Bordo"
Marina "Control de Temperatura y Clima: Ajusta la temperatura de la cabina y maneja cualquier problema relacionado con el clima a bordo para garantizar el confort de los pasajeros."
Marina "Manejo de Situaciones de Crisis: En caso de crisis, sigue los procedimientos establecidos para asegurar la seguridad de todos a bordo. Mantén la calma y sigue las instrucciones de la cabina de mando."
Marina "Documentación y Reportes: Completa cualquier documentación requerida y reporta incidentes, problemas o situaciones especiales al personal de tierra y a la cabina de mando."
Marina "Número 5. Capacitación y Actualización"
Marina "Entrenamiento Continuo: Participa en capacitaciones regulares para mantener tus habilidades y conocimientos actualizados sobre procedimientos de seguridad, atención al cliente y manejo de emergencias."
Marina "Evaluación y Retroalimentación: Recibe y proporciona retroalimentación para mejorar continuamente el servicio y la seguridad. Participa en evaluaciones de desempeño y sigue las recomendaciones para el desarrollo profesional."
Marina "En resumen, la atención al cliente, el servicio a bordo y los protocolos son aspectos esenciales del trabajo de un TCP."
Marina "Proporcionar un servicio amable y eficiente, seguir los procedimientos de seguridad y manejo de emergencias, y mantenerse actualizado con las normativas y prácticas de la aerolínea son claves para ofrecer una experiencia de vuelo segura y satisfactoria para los pasajeros."
Marina "Las salas VIP, también conocidas como salones VIP o lounges, son áreas exclusivas en los aeropuertos diseñadas para proporcionar un ambiente cómodo y lujoso para los pasajeros que buscan una experiencia de viaje superior."
Marina "Estas salas están disponibles para ciertos pasajeros, generalmente aquellos que cumplen con criterios específicos, como ser miembros de programas de fidelización de aerolíneas, poseer una tarjeta de crédito premium, o comprar acceso a la sala."
Marina "A continuación, se detallan los aspectos clave sobre las salas VIP y los servicios que suelen ofrecer:"
Marina "Primero, Acceso a la sala VIP"
Marina "Membresías de Aerolíneas: Los miembros de programas de fidelización de aerolíneas con estatus de élite a menudo tienen acceso a salas VIP como parte de sus beneficios."
Marina "Tarjetas de Crédito Premium: Algunas tarjetas de crédito ofrecen acceso a salas VIP como un beneficio para sus titulares."
Marina "Compra de Acceso: Los pasajeros pueden comprar acceso a la sala VIP, incluso si no cumplen con los requisitos de membresía o tarjeta de crédito."
Marina "Clase de Servicio: Los pasajeros que vuelan en clase ejecutiva o primera clase a menudo tienen acceso a las salas VIP como parte de su experiencia de viaje."
Marina "Segundo. Servicios y Comodidades Ofrecidas"
Marina "Comidas y Bebidas: La mayoría de las salas VIP ofrecen una variedad de comidas y bebidas de alta calidad, incluyendo opciones calientes y frías, snacks, café, té y bebidas alcohólicas."
Marina "Conexión Wi-Fi: Acceso a internet de alta velocidad para que los pasajeros puedan trabajar o mantenerse conectados."
Marina "Áreas de Descanso: Espacios cómodos para relajarse, que incluyen sofás, sillones reclinables y áreas de descanso privadas."
Marina "Salas de Duchas: Algunas salas VIP cuentan con duchas privadas para que los pasajeros puedan refrescarse antes de su vuelo."
Marina "Servicios de Negocios: Áreas de trabajo equipadas con estaciones de trabajo, impresoras, y otros servicios de oficina."
Marina "Entretenimiento: Televisores, periódicos, revistas y, en algunas ocasiones, zonas de entretenimiento para adultos y niños."
Marina "Servicios de Conserjería: Asistencia personalizada para ayudar con reservas, información sobre vuelos y otros servicios relacionados con el viaje."
Marina "Tercero, Protocolos de Servicio en la Sala VIP"
Marina "Registro y Check-In: Los pasajeros deben presentar una tarjeta de embarque válida y, en algunos casos, una tarjeta de membresía o crédito para acceder a la sala VIP."
Marina "Seguridad y Privacidad: Las áreas dentro de la sala VIP deben ser seguras y garantizar la privacidad de los pasajeros. Los empleados de la sala deben estar capacitados para manejar cualquier situación con discreción y profesionalismo."
Marina "Limpieza y Mantenimiento: El personal de la sala VIP es responsable de mantener las instalaciones limpias y en buen estado, asegurando que todas las áreas y servicios estén en condiciones óptimas."
Marina "Atención al Cliente: El personal de la sala VIP debe proporcionar un alto nivel de servicio al cliente, respondiendo a las solicitudes de los pasajeros y manejando cualquier problema o consulta de manera efectiva."
Marina "Cuarto, Beneficios para los Pasajeros"
Marina "Comodidad y Relax: Las salas VIP ofrecen un entorno cómodo y relajante lejos del bullicio de las áreas comunes del aeropuerto, lo que mejora la experiencia de viaje."
Marina "Eficiencia: Los servicios de la sala VIP permiten a los pasajeros trabajar o descansar antes de su vuelo, lo que puede hacer que el tiempo de espera en el aeropuerto sea más productivo y agradable."
Marina "Privacidad y Exclusividad: Ofrecen un espacio exclusivo para relajarse, disfrutar de comida y bebida sin la multitud típica de las áreas de embarque."
Marina "Quinto, Consideraciones Adicionales"
Marina "Ubicación: Las salas VIP están ubicadas en diferentes partes del aeropuerto, y su acceso puede variar según la aerolínea y el aeropuerto. Es útil verificar la ubicación antes de llegar."
Marina "Normas de Uso: Los pasajeros deben familiarizarse con las normas y políticas específicas de la sala VIP que visitarán, como las horas de operación, el código de vestimenta y las políticas de acceso."
Marina "En resumen, las salas VIP ofrecen un refugio cómodo y exclusivo para los pasajeros en los aeropuertos, con una variedad de servicios y comodidades diseñadas para mejorar la experiencia de viaje."
Marina "Los TCPs deben estar informados sobre las políticas y servicios de las salas VIP, especialmente si están involucrados en el manejo de pasajeros que utilizan estas instalaciones."

hide iMarina
with dissolve

#Modulo 12 - Procedimientos aeroportuarios

show iMarina at left
with fade

Marina "Buenos dias! Ya falta cada vez menos para empezar los módulos de prácticos."
Marina "Los módulos prácticos son bastante mas laxos, dado a que son espacios controlados, y no habrán pruebas al respecto"
Marina "Ya que el instructor de turno les dirá todo lo que necesitan saber y se asegurará de que todos lo practiquen"
Marina "De cualquier forma, deben pasar primero por los módulos teóricos para llegar allí"
Marina "Es una experiencia grandiosa, y espero que todos puedan llegar"
Marina "Vamos a tomar lapiz y papel, para comenzar la clase."
Marina "Hoy hablaremos de los procedimientos aeroportuarios"
Marina "No toda la vida laboral de un TCP es extrictamente sobre vuelo, despues de un tiempo pueden llegar a conseguir trabajo en tierra también"
Marina "En lo personal, no entiendo porqué lo harían. Yo amo volar."
Marina "De cualquier manera, en ambos casos es fundamental que entiendan los procedimientos aeroportuarios por detrás del despegue de un avión."
Marina "Los procedimientos aeroportuarios son fundamentales para garantizar la seguridad y eficiencia en el manejo de vuelos y pasajeros."
Marina "Los Tripulantes de Cabina de Pasajeros deben estar familiarizados con una serie de procedimientos aeroportuarios para desempeñar sus funciones de manera efectiva."
Marina "A continuación se detallan los principales procedimientos aeroportuarios relevantes para los TCPs:"
Marina "Primero, procedimientos de embarque"
Marina "Verificación de Documentos: Asegúrate de que los pasajeros tengan sus tarjetas de embarque y documentos de identificación listos al embarcar. Verifica que los pasajeros sean los correctos para el vuelo."
Marina "Orden de Embarque: Sigue el procedimiento de embarque establecido por la aerolínea, que puede estar basado en grupos, clases de servicio o prioridad de embarque."
Marina "Asistencia a Pasajeros: Proporciona asistencia a pasajeros con necesidades especiales, como personas con movilidad reducida, familias con niños pequeños, y pasajeros que necesiten ayuda adicional."
Marina "Segundo, Procedimientos de Desembarque"
Marina "Organización del Desembarque: Coordina el desembarque de los pasajeros de manera ordenada. Normalmente, el desembarque se realiza por grupos o filas para evitar congestiones."
Marina "Asistencia en el Desembarque: Ayuda a los pasajeros a recoger su equipaje de mano y a abandonar la aeronave de manera segura. Asegúrate de que todos los pasajeros hayan salido antes de cerrar la puerta."
Marina "Verificación de la Cabina: Realiza una inspección final de la cabina para asegurar que no se haya olvidado ningún objeto personal o pertenencias."
Marina "Tercero, Procedimientos de Carga y Descarga de Equipaje"
Marina "Revisión de Equipaje: Asegúrate de que el equipaje de mano esté adecuadamente almacenado en los compartimentos superiores y debajo de los asientos, siguiendo las normativas de la aerolínea."
Marina "Manejo de Equipaje Especial: Proporciona asistencia con el manejo de equipaje especial, como sillas de ruedas, equipos deportivos o instrumentos musicales."
Marina "Cuarto, Procedimientos de Seguridad y Control"
Marina "Control de Seguridad: Asegúrate de que los pasajeros pasen por los controles de seguridad de manera eficiente y segura, siguiendo las instrucciones del personal de seguridad del aeropuerto."
Marina "Seguridad a Bordo: Verifica que todos los pasajeros sigan las instrucciones de seguridad antes del despegue, incluyendo el uso de cinturones de seguridad y el almacenamiento adecuado de equipaje."
Marina "Quinto, Procedimientos en Caso de Retrasos y Cancelaciones"
Marina "Comunicación con Pasajeros: Informa a los pasajeros sobre cualquier retraso o cancelación del vuelo y proporciona actualizaciones oportunas. Mantén la calma y ofrece asistencia según sea necesario."
Marina "Reubicación de Pasajeros: Ayuda a los pasajeros a encontrar información sobre reubicaciones en otros vuelos, hoteles o transporte alternativo si el vuelo es cancelado."
Marina "Sexto, Procedimientos en Emergencias"
Marina "Plan de Emergencia: Conoce y sigue el plan de emergencia del aeropuerto y de la aerolínea en caso de situaciones críticas, como evacuaciones o incidentes de seguridad."
Marina "Coordinación con el Personal del Aeropuerto: Trabaja en conjunto con el personal del aeropuerto para coordinar la respuesta a emergencias y garantizar la seguridad de los pasajeros y la tripulación."
Marina "Septimo, Procedimientos de Comunicación"
Marina "Informes de Vuelo: Completa y presenta informes de vuelo y cualquier documentación requerida a la llegada o salida del vuelo."
Marina "Comunicación con la Cabina de Mando: Mantén una comunicación constante con la cabina de mando para recibir instrucciones y proporcionar información relevante sobre la cabina y los pasajeros."
Marina "Octavo, Procedimientos de Inspección Pre-Vuelo"
Marina "Revisión de la Cabina: Antes del embarque, realiza una inspección de la cabina para asegurarte de que todos los equipos de seguridad estén en su lugar y funcionando correctamente."
Marina "Equipos de Emergencia: Verifica que los equipos de emergencia, como los chalecos salvavidas y las mascarillas de oxígeno, estén accesibles y en condiciones adecuadas."
Marina "Noveno, Procedimientos de Check-In"
Marina "Asistencia en el Check-In: Proporciona asistencia a los pasajeros en el proceso de check-in en el aeropuerto, si es parte de tus funciones, y asegúrate de que todos los documentos y requisitos estén en orden."
Marina "Decimo, Procedimientos de Coordinación con Otros Departamentos"
Marina "Coordinación con Servicios de Tierra: Trabaja con el personal de tierra, incluyendo personal de carga, servicios de limpieza y personal de atención al cliente para asegurar que todas las operaciones se realicen de manera fluida."
Marina "Interacción con Personal del Aeropuerto: Colabora con el personal de seguridad, control de tráfico aéreo y otros departamentos del aeropuerto para garantizar el cumplimiento de las normativas y la seguridad de las operaciones."
Marina "En resumen, los procedimientos aeroportuarios para los TCPs abarcan una variedad de tareas relacionadas con el embarque, desembarque, manejo de equipaje, seguridad, y comunicación."
Marina "Seguir estos procedimientos de manera efectiva es crucial para mantener la seguridad, eficiencia y comodidad durante el vuelo y en el aeropuerto."

hide iMarina
with dissolve

#Modulo 13 - Inglés técnico aeronautico

show iMarina at left
with fade

Marina "El inglés técnico aeronáutico es fundamental para los Tripulantes de Cabina de Pasajeros (TCPs), ya que es el idioma internacional de la aviación y se utiliza para la comunicación entre la tripulación y el personal de tierra, así como para la comprensión de procedimientos y normativas. "
Marina "Aquí tienes una guía de los términos y frases clave en inglés técnico aeronáutico que un TCP debe conocer:"
Marina "Terminología Básica de Aviación"
Marina "Anoten todos los terminos porque los van a necesitar"
Marina "- **Aircraft:** Aeronave
- **Cabin Crew:** Tripulación de Cabina
- **Cockpit:** Cabina de pilotaje
- **Galley:** Cocina a bordo
- **Lavatory:** Baño
- **Seatbelt:** Cinturón de seguridad
- **Emergency Exit:** Salida de emergencia
- **Overhead Bin:** Compartimento superior
- **Tray Table:** Mesa de asiento"

Marina "Procedimientos de Seguridad y Emergencia"
Marina "- **Safety Demonstration:** Demostración de seguridad
- **Life Vest:** Chaleco salvavidas
- **Oxygen Mask:** Mascarilla de oxígeno
- **Fire Extinguisher:** Extintor de incendios
- **First Aid Kit:** Botiquín de primeros auxilios
- **Evacuation:** Evacuación
- **Bracing Position:** Posición de protección
- **Decompression:** Despresurización"

Marina "Comunicación a Bordo"
Marina "- **Boarding:** Embarque
- **Disembark:** Desembarcar
- **Takeoff:** Despegue
- **Landing:** Aterrizaje
- **Turbulence:** Turbulencia
- **Cruise:** Crucero
- **Flight Attendant:** Asistente de vuelo
- **Passenger Briefing:** Informe a los pasajeros
- **Cabin Pressure:** Presión en la cabina"

Marina "Manejo de Equipaje y Asistencia"
Marina "- **Carry-On Luggage:** Equipaje de mano
- **Checked Baggage:** Equipaje facturado
- **Special Assistance:** Asistencia especial
- **Stowage:** Almacenamiento
- **Lost Luggage:** Equipaje perdido"
Marina "Atención al Cliente"
Marina "- **Service:** Servicio
- **Request:** Solicitud
- **Complaints:** Quejas
- **Feedback:** Retroalimentación
- **Assistance:** Asistencia
- **Comfort:** Confort"
Marina "Procedimientos de Embarque y Desembarque"
Marina "- **Boarding Pass:** Tarjeta de embarque
- **Gate:** Puerta de embarque
- **Priority Boarding:** Embarque prioritario
- **Final Call:** Última llamada
- **Disembarkation:** Desembarque"
Marina "Frases Comunes de Comunicación"
Marina "- **Please fasten your seatbelt.:** Por favor, abróchese el cinturón de seguridad.
- **In case of emergency, follow the illuminated exit signs.:** En caso de emergencia, siga las señales de salida iluminadas.
- **We are experiencing turbulence. Please remain seated with your seatbelt fastened.:** Estamos experimentando turbulencia. Por favor, permanezca sentado con el cinturón de seguridad abrochado.
- **If you need any assistance, please let us know.:** Si necesita ayuda, por favor, avísenos.
- **We will be landing shortly. Please return to your seat and fasten your seatbelt.:** Estaremos aterrizando en breve. Por favor, regrese a su asiento y abróchese el cinturón de seguridad."
Marina "Términos Relacionados con el Clima y Condiciones de Vuelo"
Marina "- **Weather Conditions:** Condiciones meteorológicas
- **Visibility:** Visibilidad
- **Altitude:** Altitud
- **Storm:** Tormenta
- **Clear Skies:** Cielo despejado"
Marina "Gestión de Emergencias"
Marina "- **Emergency Procedures:** Procedimientos de emergencia
- **Emergency Landing:** Aterrizaje de emergencia
- **Evacuation Procedure:** Procedimiento de evacuación
- **Medical Emergency:** Emergencia médica"
Marina "Protocolos de Servicio"
Marina "- **Pre-Flight Briefing:** Información previa al vuelo
- **In-Flight Service:** Servicio a bordo
- **Customer Service:** Atención al cliente
- **Handling Complaints:** Manejo de quejas"
Marina "Consejos para el Aprendizaje del Inglés Técnico Aeronáutico"
Marina "- **Estudiar Glosarios:** Utiliza glosarios de aviación para familiarizarte con términos técnicos.
- **Simulaciones de Situaciones:** Practica escenarios de vuelo y emergencias para mejorar tu comprensión y fluidez.
- **Participar en Cursos de Capacitación:** Realiza cursos de capacitación específicos para TCPs en inglés, que incluyen aspectos técnicos y de servicio."
Marina "En resumen, dominar el inglés técnico aeronáutico es crucial para la comunicación efectiva y el manejo adecuado de las operaciones de vuelo y el servicio a bordo."
Marina "Familiarizarse con la terminología y los procedimientos te ayudará a realizar tus funciones con mayor confianza y eficiencia."
Marina "Ahora les voy a pedir que hagan grupos de a dos o tres, y practiquen lo aprendido entre ustedes."
Marina "Seguro mas de uno ya sabe inglés, asi que se podrán ayudar"
Marina "Al final de la clase tendremos la prueba"
Marina "Mucha suerte! "

hide iMarina
with dissolve

#Modulo 14 - Imagen y presentación personal

show iMarina at left
with fade

Marina "Hola a todos, hoy vamos a hablar de algo fundamental para cualquier Tripulante de Cabina de Pasajeros: la imagen y la presentación personal."
Marina "Estos son aspectos clave que no solo nos permiten mantener un estándar profesional, sino que también garantizan una experiencia de vuelo segura y agradable para todos los pasajeros."
Marina "Primero, hablemos del uniforme y la apariencia personal. Como TCPs, debemos llevar el uniforme de la aerolínea con orgullo y de acuerdo con las directrices establecidas."
Marina "Esto significa que el uniforme debe estar siempre limpio, bien planchado y en buen estado."
Marina "Nada de chaquetas arrugadas o camisas sueltas; cada detalle cuenta. Los zapatos, por supuesto, deben ser de color negro, bien lustrados, y cómodos."
Marina "Recuerden que estarán de pie y caminando durante largas horas, así que la elección del calzado es esencial."
Marina "Y en cuanto a los accesorios, la regla de oro es la discreción. Evitemos las joyas llamativas que puedan distraer o interferir con nuestro trabajo."
Marina "Ahora, pasando a la higiene personal. No podemos subestimar la importancia de mantenernos pulcros y profesionales en todo momento"
Marina "Esto incluye una ducha diaria, el uso de desodorante y asegurar que nuestro aliento esté siempre fresco. El cabello debe estar limpio y bien peinado, y los estilos deben ser adecuados para el entorno de trabajo."
Marina "En cuanto al maquillaje, menos es más: debe ser discreto y natural. Las uñas, limpias y cortas, con esmalte en colores neutros si deciden usarlo."
Marina "La postura y el lenguaje corporal también juegan un papel crucial en cómo nos perciben los pasajeros. Una postura erguida transmite confianza y profesionalismo, y una sonrisa genuina ayuda a crear una atmósfera acogedora."
Marina "No olvidemos el contacto visual, que demuestra atención y compromiso con el servicio al cliente."
Marina "Pero no todo es apariencia. La actitud y el comportamiento son igual de importantes. Debemos ser siempre corteses y respetuosos, usando un tono de voz amigable y profesional."
Marina "Proyectar confianza y seguridad es clave, especialmente en situaciones de emergencia. Y, por supuesto, la paciencia es una virtud que debemos practicar continuamente, sobre todo cuando las cosas se complican."
Marina "En cuanto a la comunicación y la atención al cliente, debemos ser claros y evitar el uso de jerga técnica que pueda confundir a los pasajeros."
Marina "Escuchar activamente sus necesidades y responder con empatía es esencial para brindar un servicio de calidad."
Marina "No podemos olvidar la preparación para emergencias. Nuestra apariencia y comportamiento durante estas situaciones deben transmitir calma y control."
Marina "Estar bien preparados y conocer a fondo los procedimientos de emergencia es fundamental."
Marina "Finalmente, tenemos que cumplir siempre con las normativas y políticas de la aerolínea. Esto incluye estar al tanto de cualquier actualización en los estándares de la empresa y de las regulaciones de la industria."
Marina "En resumen, la imagen y presentación personal son más que solo una cuestión de apariencia; son parte integral de la experiencia del pasajero y del éxito general del servicio a bordo."
Marina "Recuerden que la primera impresión que damos puede influir en cómo los pasajeros perciben todo el vuelo. Así que, cuidemos cada detalle, mantengamos una actitud profesional y amigable, y contribuyamos al éxito de nuestra aerolínea."

hide iMarina
with dissolve


#Modulo 15 - Teoria y practica de la busqueda

show iMarina at left
with fade

Marina "Hola a todos, hoy nos adentraremos en el proceso de búsqueda de empleo como Tripulante de Cabina de Pasajeros, o TCP, que es un camino que requiere tanto de una preparación teórica sólida como de una práctica efectiva."
Marina "Vamos a abordar cada aspecto clave que necesitas dominar para destacar en esta competitiva industria."
Marina "Empezaremos con la teoría de la búsqueda laboral, que es fundamental para entender el entorno en el que te moverás y cómo posicionarte mejor. El primer paso es el conocimiento del mercado. "
Marina "Es vital que investigues el sector de la aviación de manera exhaustiva."
Marina "¿Qué aerolíneas son las más relevantes? ¿Qué requisitos específicos tienen para sus TCPs? ¿Qué tendencias actuales están dominando la industria?"
Marina "Por ejemplo, algunas aerolíneas pueden estar enfocándose en la sostenibilidad y la experiencia del cliente, lo que podría influir en los perfiles que buscan."
Marina "Pasando a los requisitos y certificaciones, es esencial que te familiarices con lo que necesitas para calificar como TCP, dependiendo de la región en la que quieras trabajar."
Marina "En Europa, por ejemplo, podrías necesitar una certificación de la EASA, mientras que en Estados Unidos, la FAA tiene sus propios requisitos. Esto incluye, sin duda, una formación rigurosa en seguridad, certificaciones médicas y posiblemente pruebas adicionales según la aerolínea."
Marina "Un elemento crítico en tu búsqueda es la elaboración del CurrículuMarina Vitae (CV). Aquí es donde debes destacarte. Tu CV debe comenzar con un resumen profesional conciso pero impactante, que resalte tus habilidades y experiencias más relevantes para el rol de TCP."
Marina "Recuerda mencionar cualquier formación específica en aviación y cualquier experiencia previa en servicio al cliente, ya que ambas son extremadamente valoradas. "
Marina "Luego, en la sección de experiencia y habilidades, asegúrate de detallar roles anteriores que demuestren tu capacidad para manejar situaciones de alta presión, como en la atención al cliente, y resalta cualquier experiencia relacionada con la aviación. "
Marina "Las formaciones y certificaciones deben estar claramente enumeradas, mostrando que estás más que calificado para el puesto."
Marina "La siguiente fase en nuestra teoría es la preparación para entrevistas. Es fundamental que te prepares para las preguntas comunes que suelen hacerse en estas entrevistas, tales como tu experiencia en manejo de situaciones difíciles o emergencias. "
Marina "Estas son situaciones donde tu capacidad de mantener la calma y tomar decisiones rápidas será evaluada. Por ello, practicar simulaciones de entrevistas es una excelente estrategia."
Marina "Ensaya cómo manejarías situaciones de emergencia o cómo abordarías un desafío con un pasajero difícil. Esto no solo te da confianza, sino que también demuestra a los reclutadores que estás preparado para lo inesperado."
Marina "Ahora, cambiando de enfoque, pasemos a la práctica de la búsqueda laboral. Aquí es donde la teoría cobra vida. Comencemos con la búsqueda de ofertas de trabajo."
Marina "Es crucial que te familiarices con portales de empleo especializados en la industria de la aviación. Sitios como AviationJobSearch o AirlineCareer son excelentes recursos para encontrar las últimas ofertas."
Marina "Además, no subestimes el poder de las redes profesionales. LinkedIn, por ejemplo, no solo es útil para encontrar trabajos, sino también para conectar con profesionales del sector, unirte a grupos de aviación y estar al tanto de las novedades y oportunidades que pueden no estar publicadas en otros lugares. "
Marina "No olvides revisar regularmente las páginas web de las aerolíneas. Muchas veces, las oportunidades de trabajo más exclusivas se publican directamente en sus portales de carrera."
Marina "La aplicación y seguimiento es otra parte crucial. Tu carta de presentación debe ser personalizada para cada aplicación. Explica por qué eres el candidato ideal y destaca cómo tu experiencia y habilidades se alinean con lo que la aerolínea busca."
Marina "Asegúrate de que tu aplicación en línea esté completa y profesional, siguiendo todas las instrucciones al pie de la letra. No dejes cabos sueltos, ya que cualquier error podría costarte la oportunidad. Después de enviar tu solicitud, un seguimiento adecuado es clave."
Marina "Un correo electrónico cortés que reitere tu interés en el puesto y confirme la recepción de tu solicitud puede hacer que te destaques entre otros candidatos."
Marina "Prepararse para evaluaciones y pruebas es una fase donde muchos fallan por falta de preparación. Es probable que te enfrentes a pruebas de habilidad, que pueden incluir desde evaluaciones de conocimientos técnicos hasta pruebas de comunicación y resolución de problemas."
Marina "Por ello, practicar y prepararse con anticipación es esencial. Además, algunas aerolíneas podrían incluir simulaciones de situaciones reales como parte del proceso de evaluación."
Marina "Aquí es donde tu capacidad para manejar situaciones de vuelo o servicio al cliente de manera efectiva será evaluada en un entorno controlado."
Marina "Desarrollar continuamente tus habilidades es un componente que no debes descuidar. Considera la posibilidad de realizar capacitación adicional. "
Marina "Cursos en primeros auxilios, manejo de emergencias, o incluso en idiomas extranjeros pueden hacer que tu perfil sea mucho más atractivo. Además, adquirir experiencia voluntaria en roles relacionados con la atención al cliente puede fortalecer tu CV y ofrecerte una experiencia valiosa que los empleadores valorarán."
Marina "Por último, quiero darles algunos consejos adicionales que pueden marcar la diferencia en su búsqueda laboral. La red de contactos es invaluable en la industria de la aviación. "
Marina " Asistir a eventos de la industria, ferias de empleo, y expandir tu red profesional puede abrirte puertas que ni siquiera sabías que existían."
Marina "Además, la actualización continua de tus habilidades y conocimientos es vital en un sector tan dinámico como este. Mantente al día con las últimas regulaciones y tendencias."
Marina "Y por último, mantente flexible. Estar dispuesto a considerar oportunidades en diferentes regiones o con aerolíneas más pequeñas puede ser la puerta de entrada para tu carrera como TCP."
Marina "En resumen, buscar trabajo como Tripulante de Cabina de Pasajeros no es solo enviar currículos. Es un proceso que combina preparación teórica y práctica, conocimiento del mercado, y estrategias efectivas de búsqueda y aplicación."
Marina "Si te tomas el tiempo para preparar un CV sólido, practicar para tus entrevistas, y aplicar con diligencia, estarás bien encaminado hacia el éxito en esta emocionante y desafiante carrera en la aviación"

hide iMarina
with dissolve


#Modulo 16 - Emergencias médicas, RCP y uso de desfibrilador externo automático, a cargo del grupo de SUAT

show iVlad at left
with fade

Vlad "¡Hola a todos! Hoy vamos a hablar de un tema crucial para cualquier Tripulante de Cabina de Pasajeros (TCP): la preparación y manejo de emergencias médicas a bordo. Este es un aspecto vital del rol de un TCP, ya que, en situaciones críticas, la vida de un pasajero puede depender de la rapidez y efectividad con la que actúen."
Vlad "A lo largo de esta sesión, vamos a desglosar los procedimientos y las habilidades esenciales que todo TCP debe dominar para enfrentarse a estas situaciones."
Vlad "Comenzaremos con la teoría, luego avanzaremos hacia la práctica, y finalmente discutiremos algunas consideraciones adicionales que son fundamentales para el desempeño en estas situaciones."
Vlad "Comencemos por entender qué es una emergencia médica a bordo y cómo se debe actuar en tales casos. Una emergencia médica puede surgir en cualquier momento durante un vuelo y puede variar desde algo relativamente menor, como un mareo, hasta situaciones mucho más graves, como un paro cardíaco."
Vlad "Los TCPs deben estar atentos y ser capaces de identificar los síntomas que indican que un pasajero necesita ayuda médica inmediata."
Vlad "Es fundamental que los TCPs sean capaces de reconocer rápidamente los signos de una emergencia médica. Algunos de los síntomas comunes que pueden indicar la presencia de un problema grave incluyen dolor en el pecho, dificultad para respirar, pérdida de conciencia, y reacciones alérgicas severas."
Vlad "Imaginen un pasajero que de repente comienza a mostrar signos de dificultad para respirar o que se desmaya sin razón aparente. En este caso, es esencial que el TCP realice una evaluación rápida para determinar la gravedad de la situación."
Vlad "Esta evaluación inicial puede ser crítica para decidir los próximos pasos a seguir, como la administración de primeros auxilios o la notificación inmediata a la cabina de mando."
Vlad "Una vez que se ha identificado una emergencia médica, es importante seguir protocolos claros y definidos. Primero, el TCP debe notificar a la cabina de mando sobre la situación."
Vlad "Esto no solo permite que los pilotos estén al tanto, sino que también les da la oportunidad de coordinarse con personal médico en tierra y preparar cualquier asistencia adicional que pueda ser necesaria al aterrizar."
Vlad "Después de la notificación, el TCP debe brindar la asistencia al paciente lo más pronto posible. Esto puede incluir la realización de primeros auxilios básicos mientras se espera la llegada de ayuda médica en tierra o, en situaciones más graves, la preparación para un aterrizaje de emergencia. "
Vlad "Además, es crucial que se documente toda la información relevante sobre el incidente. Esto incluye detalles sobre los síntomas, el tratamiento administrado, y cualquier intervención médica que se haya realizado. "
Vlad "Esta documentación será esencial no solo para el seguimiento médico, sino también para cumplir con los procedimientos de la aerolínea y para mejorar la respuesta a futuras emergencias."
Vlad "Ahora, hablemos sobre una de las habilidades más cruciales que un TCP debe dominar: la reanimación cardiopulmonar o RCP."
Vlad "La RCP es un procedimiento de emergencia que se realiza cuando una persona ha dejado de respirar o su corazón ha dejado de latir. Es una técnica que puede salvar vidas, pero solo si se realiza correctamente y con rapidez."
Vlad "El proceso de RCP comienza con la verificación de la conciencia de la persona. "
Vlad "Si la persona no responde, esto es una señal de que se necesita actuar inmediatamente. En primer lugar, es importante llamar por ayuda. "
Vlad "Si es posible, alguien debe comunicarse con la cabina de mando para informarles de la situación mientras otro TCP comienza con las compresiones torácicas."
Vlad "Las compresiones torácicas son el corazón de la RCP. Para realizarlas, coloca a la persona en una superficie firme y plana. Luego, coloca una mano sobre el centro del pecho de la persona, con la otra mano encima, y usa el peso de tu cuerpo para aplicar compresiones fuertes y rápidas."
Vlad "La profundidad de las compresiones debe ser de 5 a 6 centímetros, y la frecuencia debe ser de 100 a 120 compresiones por minuto."
Vlad "Es crucial mantener el ritmo y la fuerza durante todo el proceso para asegurar que se esté suministrando suficiente flujo sanguíneo al cerebro y otros órganos vitales."
Vlad "Después de cada 30 compresiones, si estás entrenado, debes alternar con 2 ventilaciones. Inclina la cabeza de la persona hacia atrás, levanta el mentón, y realiza las ventilaciones asegurándote de que el pecho se eleve, lo que indica que el aire está entrando correctamente en los pulmones."
Vlad "Otra herramienta vital en la respuesta a una emergencia médica es el desfibrilador externo automático, o DEA. El DEA es un dispositivo que puede restablecer el ritmo cardíaco normal de una persona mediante una descarga eléctrica controlada. "
Vlad "Todos los TCPs deben estar capacitados para usar un DEA, ya que este dispositivo puede marcar la diferencia entre la vida y la muerte en un paro cardíaco."
Vlad "El primer paso en el uso de un DEA es encenderlo y seguir las instrucciones que proporciona el dispositivo. Luego, se deben colocar los electrodos en el pecho desnudo de la persona, uno en la parte superior derecha y el otro en la parte inferior izquierda del pecho. El DEA analizará automáticamente el ritmo cardíaco de la persona y determinará si es necesaria una descarga."
Vlad "Si el DEA indica que se debe administrar una descarga, asegúrate de que nadie esté en contacto con la persona y presiona el botón de descarga."
Vlad "Después de la descarga, continúa con la RCP si el DEA lo recomienda. Es importante seguir las indicaciones del DEA en todo momento hasta que llegue la ayuda médica o la persona recupere la conciencia."
Vlad "Hemos hablado de los procedimientos, pero es igual de importante mantener nuestras habilidades y conocimientos actualizados. Los TCPs deben participar en cursos de capacitación y reentrenamiento en primeros auxilios, RCP, y uso del DEA de manera regular."
Vlad "Las certificaciones deben mantenerse actualizadas para cumplir con los requisitos de seguridad y competencia."
Vlad "Las simulaciones regulares también son una herramienta invaluable. Estas simulaciones permiten a los TCPs practicar y perfeccionar sus habilidades en un entorno controlado, lo que mejora su capacidad de respuesta en situaciones reales. Recuerden, la práctica hace al maestro, y en este caso, la práctica puede salvar vidas."
Vlad "Un aspecto que a menudo se pasa por alto en la gestión de emergencias médicas es la documentación y el reporte posterior al incidente. Después de manejar una emergencia médica, es esencial que los TCPs documenten todos los detalles del incidente."
Vlad "Esto incluye el tiempo, los síntomas observados, las acciones realizadas, y la respuesta del paciente al tratamiento. Esta información no solo es importante para el seguimiento médico, sino que también es crucial para las revisiones internas de la aerolínea."
Vlad "El reporte a la aerolínea debe hacerse lo antes posible, siguiendo los procedimientos internos establecidos. Esto podría incluir la presentación de informes formales y la participación en revisiones de incidentes. "
Vlad "Estos reportes ayudan a la aerolínea a mejorar sus procedimientos de emergencia y a garantizar que todos los TCPs estén preparados para enfrentar situaciones similares en el futuro."
Vlad "Finalmente, quiero hablar sobre algunas consideraciones adicionales que todo TCP debe tener en cuenta. Primero, es vital estar familiarizado con el equipo médico disponible a bordo y su ubicación."
Vlad "Esto incluye botiquines de primeros auxilios, medicamentos de emergencia, y equipos de monitoreo. Saber dónde se encuentran estos elementos y cómo utilizarlos puede ahorrar tiempo crucial en una emergencia."
Vlad "Además, en casos de emergencias médicas graves, es probable que haya pasajeros que sean profesionales médicos. En estos casos, los TCPs deben colaborar con estos profesionales y seguir sus recomendaciones. La colaboración efectiva puede mejorar significativamente el resultado de la emergencia."
Vlad "En resumen, la preparación y la capacidad de respuesta a emergencias médicas son habilidades fundamentales para cualquier TCP. La capacitación en RCP y el uso de un DEA, combinadas con la capacidad de identificar y manejar una emergencia médica, pueden marcar la diferencia en la vida de un pasajero. "
Vlad "Mantener una preparación adecuada, una actitud calmada, y seguir los procedimientos establecidos no solo garantiza la seguridad de los pasajeros, sino que también refuerza la confianza en la capacidad del equipo de vuelo para manejar cualquier situación. "
Vlad " Al final del día, estar bien preparado es la clave para proporcionar una respuesta efectiva y segura en cualquier emergencia médica a bordo."

hide iVlad
with dissolve

#Modulo 17 - Servicio a bordo

show iMarina at left
with fade

Marina "¡Bienvenidos! Hoy vamos a explorar en detalle uno de los aspectos más cruciales del trabajo de un Tripulante de Cabina de Pasajeros: el servicio a bordo."
Marina "Este componente del rol no solo define la experiencia del pasajero, sino que también refleja el nivel de profesionalismo y cuidado que ofrece la aerolínea."
Marina "Vamos a desglosar cada etapa del servicio a bordo, desde la preparación previa al vuelo hasta el post-servicio, para asegurarnos de que comprendes completamente las responsabilidades y mejores prácticas involucradas."
Marina "Primero, abordemos la preparación para el servicio a bordo."
Marina "Antes de que los pasajeros embarquen, es fundamental que realices una revisión exhaustiva de la cabina. Esto incluye asegurarte de que el espacio esté limpio y organizado. Cada rincón debe estar impecable, porque una cabina ordenada y pulcra es la primera impresión que recibirán nuestros pasajeros."
Marina "Además, verifica que todos los equipos y suministros estén disponibles y en óptimas condiciones. Los carros de servicio deben estar bien preparados, con todos los productos necesarios a mano, desde alimentos y bebidas hasta utensilios y productos de confort."
Marina "Es esencial que cada artículo esté correctamente almacenado y organizado para garantizar un servicio fluido y eficiente."
Marina "Con el menú en mente, familiarízate con todas las opciones disponibles. Esto no solo incluye las ofertas generales, sino también las opciones especiales para dietas, alergias y preferencias. Conocer estos detalles te permitirá ofrecer un servicio personalizado y adecuado a cada pasajero."
Marina "Durante el embarque, tu rol se vuelve aún más crucial."
Marina "La bienvenida a bordo debe ser cálida y profesional. Saluda a cada pasajero con una sonrisa genuina y ofrece ayuda para encontrar sus asientos y almacenar su equipaje de mano."
Marina "Esta es una oportunidad para establecer una primera impresión positiva y asegurar que cada pasajero se sienta bienvenido y cómodo desde el principio."
Marina "Es igualmente importante que los pasajeros reciban una demostración clara y comprensible de las instrucciones de seguridad antes del despegue."
Marina "Reitera la importancia de seguir estas instrucciones y de estar atentos a las señales. La seguridad es nuestra prioridad, y una comunicación efectiva es clave para asegurar que todos estén preparados para cualquier eventualidad."
Marina "Ahora, pasemos al servicio de alimentos y bebidas, un aspecto fundamental de la experiencia a bordo."
marina "Distribuir alimentos y bebidas de manera eficiente es esencial para mantener un alto nivel de satisfacción. Asegúrate de que todos los pasajeros reciban lo que han solicitado, utilizando un sistema organizado para el servicio, como servir por filas o grupos."
Marina "Atender las necesidades especiales de los pasajeros, como dietas específicas o alergias, requiere atención y precisión. Las opciones especiales deben estar claramente identificadas y entregadas correctamente para evitar inconvenientes."
Marina "Mientras sirves, no olvides manejar los residuos de manera ordenada y rápida. La cabina debe mantenerse limpia y cómoda durante todo el servicio. "
Marina "En cuanto a las bebidas, ofrece una variedad que incluya agua, jugos, refrescos y, si está permitido, bebidas alcohólicas. "
Marina "Cumple con las regulaciones sobre el servicio de alcohol y verifica la edad de los pasajeros si es necesario. Realiza rondas periódicas para ofrecer más bebidas y atender cualquier solicitud adicional, manteniendo siempre un equilibrio entre rapidez y atención personalizada."
Marina "Cuando se trata de atención al cliente y solución de problemas, la comunicación clara es esencial."
Marina "Habla con los pasajeros de manera amable y efectiva. Escucha sus necesidades y preocupaciones con atención y responde de manera eficiente. "
Marina "En caso de problemas o quejas, maneja cada situación con calma y profesionalismo, buscando soluciones adecuadas y ofreciendo compensaciones si es necesario. "
Marina "Proporcionar comodidad es otra parte importante de tu rol. Ayuda a ajustar los asientos, proporciona mantas o almohadas cuando se soliciten, y asegúrate de que la cabina esté bien ventilada y que los pasajeros tengan acceso a las instalaciones necesarias."
Marina "Además, es crucial estar preparado para procedimientos especiales."
Marina "En caso de emergencias a bordo, tu capacidad para actuar rápidamente es vital. Sigue los procedimientos establecidos para garantizar la seguridad de los pasajeros y la tripulación. "
Marina "En una evacuación, proporciona instrucciones claras y guías para asegurar que todos salgan del avión de manera segura y ordenada. "
Marina "Durante situaciones de vuelo especiales, como turbulencia, informa a los pasajeros y asegúrate de que estén seguros. Ofrece asistencia para garantizar que los cinturones de seguridad estén abrochados y que los objetos estén almacenados adecuadamente. "
Marina "En caso de retrasos o cambios en el itinerario, mantén a los pasajeros informados y proporciona actualizaciones regulares. Ofrece entretenimiento o asistencia adicional si es necesario para mejorar su experiencia."
Marina "Finalmente, en el post-servicio, la limpieza y organización son clave."
Marina "Realiza una limpieza básica de la cabina después del servicio de alimentos para mantener un entorno agradable. Retira todos los residuos y organiza el área para el próximo servicio. Revisa que todos los equipos y suministros estén en su lugar y en condiciones óptimas para el próximo vuelo."
Marina "Comunica cualquier problema o situación relevante a la cabina de mando y al resto de la tripulación para asegurar una coordinación efectiva y una respuesta adecuada."
Marina "Consideraciones adicionales incluyen la capacitación continua y la recopilación de feedback."
Marina "Participa en cursos de capacitación y actualizaciones sobre servicio al cliente, seguridad y procedimientos de la aerolínea. "
Marina "Recoge y analiza el feedback de los pasajeros para identificar áreas de mejora en el servicio y para implementar cambios positivos."
Marina "En resumen, el servicio a bordo para los TCPs involucra una combinación de preparación, atención al cliente y gestión eficiente de recursos. "
Marina "La clave es ofrecer un servicio amigable y profesional mientras se garantiza la comodidad y seguridad de los pasajeros durante el vuelo."
Marina "¡Gracias por su atención, y espero que esta guía te ayude a brindar un excelente servicio a bordo!"

hide iMarina
with dissolve

#Modulo 18 - Ditching, simulacro de evacuación y técnicas de supervivencia en el mar, realizado en piscina cerrada climatizada.

show iMarina at left
with fade

Marina "¡Bienvenidos! Hoy quiero hablarles de un aspecto crucial en la formación de los Tripulantes de Cabina de Pasajeros (TCPs), uno que puede marcar la diferencia entre la vida y la muerte en situaciones extremas: el entrenamiento en ditching y simulacros de evacuación."
Marina "Estos entrenamientos no son solo una formalidad; son una parte esencial de la preparación para emergencias y se llevan a cabo en entornos controlados, como piscinas cerradas climatizadas, para asegurar que la tripulación esté lista para enfrentar cualquier situación crítica en el agua."
Marina "Primero, enfoquémonos en el ditching, que es el aterrizaje forzoso en el agua. Imaginemos el escenario: un avión está en una emergencia que requiere un aterrizaje en el mar."
Marina "La preparación para este tipo de evento empieza mucho antes del vuelo. Los TCPs deben conocer al detalle los procedimientos de evacuación para un aterrizaje forzoso en el agua. "
Marina "Esto incluye la localización precisa de las salidas de emergencia, el acceso a las balsas salvavidas y los equipos de flotación."
Marina "Es vital que cada miembro de la tripulación esté familiarizado con el equipo de flotación disponible, como los chalecos salvavidas y las balsas inflables, y que sepa cómo utilizar estos dispositivos de manera correcta y eficaz."
Marina "Durante el aterrizaje en el agua, el rol de los TCPs se vuelve aún más crítico. Primero, es necesario dar instrucciones claras a los pasajeros."
Marina "Los TCPs deben explicar cómo prepararse para el aterrizaje en el agua, instruir sobre el uso de chalecos salvavidas y guiar a los pasajeros a adoptar la posición de braceo para minimizar el impacto."
Marina "Al momento del impacto, deben seguir los procedimientos de seguridad establecidos para asegurar una evacuación ordenada."
Marina "Una vez que el avión está estabilizado, la evacuación hacia las balsas salvavidas debe ser rápida y organizada. "
Marina "Cada segundo cuenta, y es esencial que todos los pasajeros salgan de la aeronave de manera efectiva, utilizando las salidas de emergencia y los equipos de flotación de forma eficiente."
Marina "Ahora, pasemos a los simulacros de evacuación, que son igualmente importantes. La preparación para estos simulacros comienza con un profundo conocimiento del avión. "
Marina "Los TCPs deben familiarizarse con el diseño del avión, las ubicaciones de las salidas de emergencia, las escaleras de evacuación y las balsas salvavidas. "
Marina "Durante el simulacro, realizado en una piscina cerrada climatizada, los TCPs practican la evacuación rápida y segura del avión. "
Marina " Estos simulacros imitan situaciones reales de emergencia en el agua, y permiten a los TCPs practicar la evacuación utilizando balsas salvavidas y asumir diferentes roles y responsabilidades, desde la supervisión de los pasajeros hasta la coordinación de la salida de emergencia."
Marina "Es crucial realizar una evaluación posterior al simulacro. Esto permite identificar áreas de mejora y ajustar procedimientos según sea necesario, garantizando que cada aspecto de la evacuación se maneje con la máxima eficiencia."
Marina "La capacitación también incluye técnicas de supervivencia en el mar. Saber cómo usar los equipos de flotación es vital. Los TCPs deben aprender a inflar y ajustar correctamente los chalecos salvavidas, asegurándose de que proporcionen la flotación adecuada."
Marina "Las balsas salvavidas también deben ser manejadas con destreza: desde el inflado y lanzamiento hasta el abordaje y mantenimiento de la balsa en condiciones óptimas."
Marina "En el agua, la flotación y orientación son esenciales. Los TCPs practican técnicas para mantenerse a flote, mantener la cabeza por encima del agua y conservar energía."
Marina "Además, deben estar capacitados en el uso de señales de emergencia, como bengalas, luces de emergencia y silbatos, para atraer la atención y solicitar ayuda."
Marina "La comunicación y coordinación entre supervivientes también es clave. Los TCPs deben saber cómo mantener la calma, coordinarse con otros supervivientes y comunicarse claramente con la tripulación y los equipos de rescate."
Marina "Finalmente, el reentrenamiento y la revisión de procedimientos son cruciales. La participación en sesiones de reentrenamiento periódicas asegura que las habilidades se mantengan actualizadas y que los procedimientos se ajusten a las mejores prácticas y normativas vigentes."
Marina "En resumen, el entrenamiento en ditching, los simulacros de evacuación y las técnicas de supervivencia en el mar son esenciales para preparar a los TCPs para enfrentar emergencias en el agua."
Marina "La práctica constante en entornos controlados asegura que, en caso de una emergencia real, los TCPs puedan responder de manera efectiva y segura, protegiendo así la vida de los pasajeros y de la tripulación."

hide iMarina
with dissolve

#Modulo 19 - Combate al fuego y manipulación de extintores

show iMarina at left
with fade

Marina "Muy buenos días a todos. Hoy vamos a hablar sobre un tema de vital importancia para nuestra seguridad a bordo: el combate al fuego y la manipulación de extintores."
Marina "Como Tripulantes de Cabina de Pasajeros, ustedes saben que los incendios en un avión pueden representar una amenaza significativa. "
Marina "Por eso, es fundamental que estemos bien preparados y sepamos cómo actuar en caso de emergencia."
Marina "Vamos a comenzar repasando los tipos de fuegos que podemos encontrar a bordo. Primero, tenemos los fuegos de Clase A, que involucran materiales sólidos como madera, papel o telas. "
Marina "Luego, están los fuegos de Clase B, que son aquellos que involucran líquidos inflamables, como gasolina, aceites o alcohol. También tenemos los fuegos de Clase C, que se generan por equipos eléctricos, algo muy relevante en el entorno de una aeronave."
Marina "Además, existen los fuegos de Clase D, que incluyen metales combustibles como magnesio o sodio, y, aunque menos comunes en aviones, los fuegos de Clase K, que son los que involucran aceites de cocina o grasas."
Marina "Ahora bien, los riesgos específicos en aeronaves no se limitan a estos tipos de fuego. "
Marina "Hay que considerar la cantidad de materiales combustibles que tenemos a bordo: plásticos, productos químicos, textiles, entre otros."
Marina "Además, el equipo eléctrico de la cabina y la cabina de mando puede convertirse en un foco de riesgo en caso de fallos o cortocircuitos."
Marina "Es aquí donde entra en juego la manipulación adecuada de los extintores. Hay varios tipos que debemos conocer."
Marina "Por ejemplo, los extintores de agua, que son efectivos para fuegos de Clase A, pero no deben utilizarse en fuegos de Clase B o C, ya que podrían propagar el fuego o causar cortocircuitos. "
Marina "Los extintores de espuma son útiles tanto para fuegos de Clase A como B, ya que la espuma sofoca las llamas y previene la liberación de vapores inflamables."
Marina "Por otro lado, los extintores de CO2 son eficaces para fuegos de Clase B y C. El CO2 desplaza el oxígeno y apaga el fuego sin dejar residuos. Sin embargo, no se recomienda su uso en fuegos de Clase A porque no enfrían el material combustible."
Marina "Finalmente, tenemos los extintores de polvo seco (ABC), que son eficaces para fuegos de Clase A, B y C, ya que interfieren con la reacción química del fuego."
Marina "Cuando usamos un extintor, es crucial seguir el método PASS: P de “Pull”, tirar del pasador para desbloquear el extintor; A de “Aim”, apuntar la boquilla hacia la base del fuego; S de “Squeeze”, apretar el mango para liberar el agente extintor; y S de “Sweep”, mover la boquilla de lado a lado para cubrir toda la base del fuego."
Marina "En cuanto a los procedimientos de combate al fuego a bordo, lo primero es la detección y notificación. Es fundamental identificar rápidamente la fuente del fuego y evaluar su gravedad."
Marina "Si es pequeño, intentamos apagarlo con el extintor adecuado. Si no, seguimos el procedimiento de evacuación. Y recuerden, siempre hay que informar de inmediato a la cabina de mando para coordinar la respuesta y preparar una posible evacuación."
Marina "En caso de que el fuego no pueda ser controlado, evaluamos los riesgos, aseguramos a los pasajeros, y utilizamos el extintor adecuado. Si el extintor se agota o no logramos controlar el fuego, buscamos ayuda y seguimos los procedimientos de evacuación."
Marina "Por último, la capacitación y el reentrenamiento son esenciales. Participar en simulacros regulares de combate al fuego es vital para mantener nuestras habilidades y conocimientos al día."
Marina "Además, realizar pruebas de competencia y recibir retroalimentación nos ayuda a mejorar continuamente."
Marina "En resumen, el combate al fuego y la manipulación de extintores son habilidades que deben ser parte de nuestro día a día como TCPs."
Marina "Entrenarnos regularmente nos prepara para proteger a los pasajeros y a la tripulación de manera efectiva en caso de un incendio a bordo."
Marina "¡Así que sigan practicando, manténganse informados y siempre listos para cualquier eventualidad!"

hide iMarina
with dissolve

#Modulo 20 - Supervivencia en tierra, simulando un crash landing, organziación de medios de supervivencia

show iMarina at left
with fade

Marina "Buenos días a todos. Hoy vamos a profundizar en un tema crucial para la seguridad de todos a bordo: la supervivencia en tierra después de un aterrizaje forzoso."
Marina "Como Tripulantes de Cabina de Pasajeros, su entrenamiento no se limita a los procedimientos en vuelo. También deben estar preparados para situaciones de emergencia una vez que el avión está en tierra, especialmente si nos encontramos en un entorno remoto o desafiante."

Marina "Primero, hablemos de lo que deben hacer inmediatamente después de un aterrizaje forzoso. Lo primero es realizar una evaluación de la situación de manera rápida y efectiva."
Marina "Es fundamental que comprueben la condición de la aeronave. Deben identificar si hay riesgos de incendio, derrames de combustible u otros peligros que puedan poner en riesgo a las personas a bordo."
Marina "Asegúrense de que todos los pasajeros y miembros de la tripulación estén seguros. Si es posible, deben proceder a evacuar la aeronave utilizando las salidas de emergencia y cualquier equipo disponible, como los toboganes inflables."

Marina "Una vez que hayan logrado evacuar la aeronave, el siguiente paso es organizar a las personas. Reúnan a todos los pasajeros y miembros de la tripulación en un lugar seguro y visible."
Marina "Es importante hacer un recuento de todas las personas y evaluar su estado físico. Después, deben revisar los recursos disponibles en la aeronave, como equipos de emergencia, primeros auxilios y suministros de supervivencia, y organizarlos para su uso adecuado."

Marina "En cuanto a las técnicas de supervivencia en tierra, lo primero es construir refugios. Utilicen materiales de la aeronave o elementos naturales del entorno para protegerse del clima adverso."
Marina "Asegúrense de que los refugios sean adecuados para protegerse del frío y la humedad. También es importante que los refugios tengan buena ventilación para evitar la acumulación de dióxido de carbono, lo cual puede ser perjudicial."

Marina "En cuanto a la obtención de agua y alimentos, deben buscar fuentes de agua potable en el entorno, como riachuelos o agua de lluvia. Utilicen cualquier equipo de filtración disponible o hierva el agua si es posible para eliminar contaminantes."
Marina "Respecto a los alimentos, comiencen usando los suministros de emergencia que se encuentran en la aeronave. Si estos se agotan, identifiquen fuentes seguras de alimentos en el entorno y eviten consumir plantas o animales desconocidos sin asegurarse de que sean seguros."

Marina "También es crucial utilizar técnicas de señalización y comunicación para hacerse visibles a los equipos de rescate. Utilicen bengalas, reflejos y silbatos, y mantengan una señalización continua durante el día y la noche."
Marina "Si tienen acceso a radios o teléfonos satelitales, úsenlos para contactar a los servicios de rescate y proporcionar información sobre la ubicación y las condiciones."

Marina "Para organizar los medios de supervivencia, asegúrense de que los kits de primeros auxilios estén completos y accesibles. Utilícenlos para tratar cualquier lesión o problema de salud."
Marina "Organicen equipos como linternas, bengalas y radios de emergencia. Asegúrense de que estén operativos y listos para usar. Asignen roles y responsabilidades entre los miembros de la tripulación y los pasajeros para manejar los recursos de manera efectiva."

Marina "Es importante practicar estos procedimientos a través de simulacros de supervivencia en tierra. Realicen simulacros en entornos controlados para practicar la evacuación, la construcción de refugios, la obtención de agua y alimentos, y la señalización."
Marina "Después de cada simulacro, revisen los procedimientos seguidos y proporcionen retroalimentación para mejorar las técnicas y la coordinación."

Marina "Finalmente, mantengan siempre una buena preparación mental y física. Una buena condición física y una actitud mental positiva son cruciales para manejar cualquier situación de supervivencia."
Marina "La capacidad de coordinar, liderar y comunicarse efectivamente puede marcar la diferencia entre una evacuación desorganizada y una que sea segura y exitosa."

Marina "En resumen, estar preparados para la supervivencia en tierra después de un aterrizaje forzoso es fundamental. La práctica continua y el entrenamiento adecuado son claves para garantizar la seguridad y el bienestar de los pasajeros y la tripulación en situaciones extremas."

hide iMarina
with dissolve
