#Personajes
define Marina = Character('Instructora Marina', color="#FFF000")
define Sabino = Character('Capitán Gentile', color="#000FFF")

#Inicio del juego - Modulo 1 - introduccion a la aviacion comercial y a la funcion del tcp
label start:

image sala = "background1.png"
scene sala

image iMarina = "crew1.png"
show iMarina
with fade

"Bienvenidos al entrenamiento de tripulante de cabina de pasajeros de Sky-Blue Airlines."

Marina "Mi nombre es Marina, y seré su principal instructora a lo largo de esta capacitación."
Marina "Antes que nada me gustaría felicitarlos por haber sido seleccionados para esta capacitación tras un riguroso proceso. Cientos de candidatos se postulan año a año, siendo apenas unos pocos los egreados que lleguen a los estandares para volar con nosotros."
Marina "Asi que no se preocupen. Si bien hay etapas en este proceso que son excluyentes, en caso de quedar fuera de la selección final en esta oportunidad, podrán volver a postularse luego de seis meses tantas veces como quieran."
Marina "La capacitación inicial dentro de la aerolinea tiene una duración total de un mes, donde aprenderán todo lo necesário tanto a nivel práctico como técnico y legal, para tripular con tranquilidad y garantizar un vuelo seguro a otros."
Marina "Durante este periodo, estaremos viendo un módulo por dia, con una prueba al final de cada módulo. Esta instancia es excluyente, solo serán aptos para volver al siguiente dia quienes hayan aprobado la prueba anterior."
Marina "Parece exigente y realmente lo es. En Sky-Blue Airlines no escatimamos recursos para mantener nuestros estandares de excelencia."
Marina "El dia de hoy aprenderemos sobre la historia de la aviación comercial y como el rol del Tripulante de Cabina de Pasajeros, o sea, ustedes, ha cambiado a lo largo del tiempo."
Marina "Les sugiero que tomen nota de las siguientes informaciones porque podrán usar los descansos para estudiar y revisar sus apuntes antes de la prueba."
Marina "Todos listos? Empecemos."

image PScreen ="projectionscreen.png"
show PScreen 
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
"..."
image iMarina = "crew1.png"
show iMarina
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

image iMarina = "crew1.png"
show iMarina
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

image iMarina = "crew1.png"
show iMarina
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

#Modulo 4 - procedimientos de rutina, obligaciones y repsonsabilidades

image iSabino = "crew2.png"
show iSabino
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

image iSabino = "crew2.png"
show iSabino
with fade

Sabino "Buenos dias a todos. Hoy concluimos la primera semana de curso. Asi que daremos un ultimo empujon hasta el tan deseado fin de semana, que me imagino estarán esperando."
Sabino "Como habrán visto en el calendário del curso, hoy daremos el módulo de meteorología básica."
Sabino "El conocimiento básico de meteorología es crucial para los Tripulantes de Cabina de Pasajeros, ya que les permite entender las condiciones atmosféricas que pueden afectar el vuelo y prepararse para manejar situaciones relacionadas con el clima de manera eficaz. Aquí te presento un resumen de los conceptos meteorológicos esenciales para los TCPs."
Sabino "Empecemos con los fundamentos de la meteorología."
Sabino "Primero. Los TCPs deben entender que la atmósfera está compuesta por varias capas (troposfera, estratosfera, etc.), pero la mayoría de los fenómenos meteorológicos que afectan el vuelo ocurren en la troposfera, que se extiende hasta unos 12 km de altura."
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

#Modulo 6 - CRM Crew Resource MAgnament

image iMarina = "crew1.png"
show iMarina
with fade

Marina "Buenos dias a todos."
Marina "Espero hayan disfrutado de las clases del jueves y viernes con el Capitán Gentile."
Marina "Sabino Gentile es de las personas que mas tiempo han estado dentro de la companía en su rol."
Marina "Ha instruido a generaciones de excelentes profesionales. Inclusve a mi."
Marina "El día que empiecen a volar con nosotros, entenderán que es un referente, sobre todo para los nuevos ingresos."
Marina "Más allá de ello, espero que también hayan podido disfrutar de su primer fin de semana, trás un arduo entrenamiento."
Marina "Que hayan podido aprovechar para distenderse, y sobre todo, estudiar mas."
Marina "Si realmente desean esta posición, sabrán aprovechar cada instante, y el entrenamiento terminará antes de que puedan darse cuenta."
Marina "El dia de hoy hablaremos del CRM y sus implicaciones."
Marina "Saquen lápiz y papel, que hoy vamos a anotar mucho."
Marina "El Crew Resource Management (CRM), o Gestión de los Recursos de la Tripulación, es un conjunto de procedimientos de capacitación diseñados para mejorar la seguridad en la aviación mediante la promoción de una comunicación efectiva, la toma de decisiones, la resolución de problemas, y la coordinación entre todos los miembros de la tripulación, incluidos los pilotos, los Tripulantes de Cabina de Pasajeros (TCPs), y otros miembros del equipo."
Marina "Para los TCPs, el CRM es esencial porque su rol va más allá de atender a los pasajeros; son una parte crítica de la tripulación en la gestión de situaciones normales y de emergencia. El CRM ayuda a los TCPs a interactuar de manera efectiva con el resto de la tripulación y a contribuir a la seguridad del vuelo."
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
Marina "El primero sería el manejo de pasajeros conflictivos. El CRM incluye técnicas para manejar y desescalar conflictos con pasajeros, asegurando que el vuelo se mantenga seguro y que las situaciones potencialmente peligrosas se resuelvan de manera adecuada."
Marina "Y la negociación y persuasión. Los TCPs deben ser capaces de utilizar la persuasión y la negociación para obtener la cooperación de los pasajeros en situaciones difíciles."
Marina "Y bien, que les ha parecido? Son bastantes cosas que recordar, pero considero que todas ellas bastante intuitivas, una vez que entiendes el trabajo del TCP."
Marina "Ahora veremos la aplicación del CMR en situaciones reales."
Marina "Evacuaciones de Emergencia: En caso de una evacuación de emergencia, el CRM asegura que todos los miembros de la tripulación trabajen juntos de manera eficiente, siguiendo los procedimientos establecidos y comunicándose constantemente para asegurar que todos los pasajeros salgan del avión de manera segura."
Marina "Incidentes de Salud a Bordo: Si un pasajero sufre una emergencia médica, los TCPs deben coordinarse con los pilotos, otros TCPs, y, si es necesario, con el personal médico en tierra. Aquí, la comunicación efectiva y la toma rápida de decisiones son esenciales."
Marina "Turbulencia o Mal Tiempo: Durante turbulencia severa o condiciones meteorológicas adversas, los TCPs deben aplicar el CRM para asegurar que todos los pasajeros están seguros, comunicarse con la cabina de mando sobre las condiciones en la cabina, y coordinar cualquier acción necesaria para mantener la seguridad."
Marina "El CRM trae muchisimos beneficios para todos los TCPs, porque sistematiza procesos que son dificiles de deducir en situaciones complejas. El poder organizar estas practicas mentalmente nos ayuda a recordarlas."
Marina "Ni que hablar como mejoran la seguridad del vuelo. Al promover la comunicación y la coordinación efectiva, el CRM reduce el riesgo de errores humanos y mejora la respuesta de la tripulación en situaciones críticas."
Marina "Aumenta la Eficiencia Operacional. Una tripulación que utiliza CRM de manera efectiva puede manejar situaciones inesperadas de manera más fluida, minimizando interrupciones y asegurando un vuelo más eficiente."
Marina "Fortalece el Trabajo en Equipo. El CRM fomenta un ambiente de trabajo en equipo, donde todos los miembros de la tripulación se apoyan mutuamente y trabajan juntos hacia un objetivo común: la seguridad y el éxito del vuelo."
Marina "El CRM es, por lo tanto, una herramienta fundamental para los TCPs, ayudándolos a desempeñar su papel de manera efectiva y asegurando que contribuyen positivamente a la seguridad y el bienestar de todos a bordo."

hide iMarina
with dissolve