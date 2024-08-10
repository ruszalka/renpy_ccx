#Personajes
define Marina = Character('Instructora Marina', color="#FFF000")
define Sabino = Character('Capitán Gentile', color="#000FFF")

#Inicio del juego - Modulo 1 - introduccion a la aviacion comercial y a la funcion del tcp
label start:

image colegio = "background1.png"
scene colegio

image iMarina = "crew1.png"
show iMarina
with fade

"Bienvenidos al entrenamiento de tripulante de cabina de pasajeros de Sky-Blue Airlines."

Marina "Mi nombre es Marina, y seré su principal instructora a lo largo de esta capacitación."
Marina "Antes que nada me gustaría felicitarlos por haber sido seleccionados para esta capacitación tras un riguroso proceso. Cientos de candidatos se postulan año a año, siendo apenas unos pocos los egreados que lleguen a los estandares para volar con nosotros."
Marina "Asi que no se preocupen. Si bien hay etapas en este proceso que son excluyentes, en caso de quedar fuera de la selección final en esta oportunidad, podrán volver a postularse luego de dos meses tantas veces como quieran."
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