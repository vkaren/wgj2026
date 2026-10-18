# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

default nombre_jugador = ""
default cansancio = 0 
default estres =0 
default culpa =0
default dinero = 0
default frases_libreta = 4
define boss = Character("Jefe Nushi")
define ms = Character("Mizuno-san")
define ks = Character("Kawauso-senpai")
define mom = Character("Mensaje de mamá")

# El juego comienza aquí.

label start:

    
    $ renpy.call_screen("pedir_nombre")

    $ nombre_jugador = nombre_jugador.strip()

    if nombre_jugador == "":
        $ nombre_jugador = "P"
   
    jump intro

label intro:
    #with  Fade(2.0, 0.5, 2.0)
    call screen presentacion ("Desde pequeña he tenido un sueño…. \n Logré conseguir trabajo en una reconocida empresa, la cual parece ser una oportunidad prometedora para crecer…\n Pronto será mi momento de brillar…necesito ahorrar 1.000.000 de dólares para lograrlo!\nPERO…. ¿A que costo?...")
    jump capitulo1

label capitulo1:
    show screen barra_estadisticas
    scene fondo
    #show eileen happy with easeinleft
    boss "¡Hola! Bienvenida, soy el jefe Nushi. Antes que nada, necesito que revises este reporte sumamente importante."
    nombre_jugador "{i}Debo decirle que sí para mantener mi primer empleo y caerle bien a todos.{/i}"
    menu:
        "¡Sí, claro!":
            pass
        "¡Puedo hacerlo!":
            pass
  
    call screen presentacion("2 horas más tarde...")
    pass
    boss "¿Ya está listo el reporte?"
    nombre_jugador "¡Sí, listo!"
    $ cansancio +=10
    $ dinero += 500
    boss "Muchas gracias."
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $[dinero] en la cuenta bancaria")
    jump capitulo2
    
label capitulo2:
    call screen presentacion("Capítulo 2: más favores\n [nombre_jugador]: Ingreso al trabajo, 08 am.")
    ms "Oye, [nombre_jugador], necesito que hagas esta carga de datos. Te doy 100 dólares para que me ayudes pronto."

    menu:
        "¡Sí, entendido!":
            $ cansancio += 20
            $ estres += 20
            $ culpa -=10
            $ dinero +=100
            ms "¡Gracias, [nombre_jugador]! Ya me voy a casa."
            pass
        "Lo cargo después del almuerzo":
            $ cansancio += 10
            $ estres += 10
            $ culpa +=10
            $ dinero +=100
            ms "[nombre_jugador]... ¿y la carga? La necesitaba hace una hora."
            pass
    boss "Hola, [nombre_jugador], ayúdame con esta presentación."
    menu:
        "Por supuesto.":
            $ cansancio += 20
            $ estres += 10
            $ dinero +=500
            call screen presentacion("2 horas más tarde...")
            boss "Buen trabajo, [nombre_jugador]. Mañana te espero temprano."
            
    call screen presentacion("6:00 pm. En el escritorio del fondo, una silueta pequeña con corbata apaga su computadora y se va tranquilamente.")
    nombre_jugador "{i}¿Alguien se va a las 6? Yo todavía tengo trabajo...{/i}"
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria")
    jump capitulo3

label capitulo3:
    call screen presentacion("Capítulo 3:  La nutria del escritorio del fondo\n {i}2 semanas después{/i}")
    nombre_jugador "{i}Son las 8 pm y la oficina sigue llena. Nadie se va antes que el jefe.{/i}"
    nombre_jugador "{i}Llevo dos semanas saliendo a las 10 pm... pero mi cuenta crece. Debo aguantar.{/i}"
    ks "Tú eres la nueva, ¿verdad? Llevo 15 años aquí. Soy la única que sale a las 6 pm todos los días."
    nombre_jugador "¿Cómo lo hace? ¿No la regañan?"
    ks "Nunca digo “no”... pero tampoco digo “sí” a todo. Escucha bien, pequeña."
    #ms llega corriendo
    ms "[nombre_jugador], ¿me ayudas con mis correos pendientes? Te doy 50 dólares."
    menu:
        "¡Claro, ahora mismo!":
            $ cansancio += 20
            $ estres += 10
            $ dinero +=50
            $ culpa -=10
            pass
        "¡Lo pongo en mi lista para revisarlo.":        
            $ estres -= 10
            $ culpa +=10
            ks "¿Ves? No le dijiste que no. Solo no le dijiste que sí ahora."
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria")        
    call screen presentacion("Se desbloquea: 📓 Libreta de frases (ahí se guardan las maneras de decir que no que se van aprendiendo).")
    jump capitulo4

label capitulo4:
    call screen presentacion("Capítulo 4: El precio del “sí”\n {i}3 meses después{/i}")
    mom "Hija, hace semanas que no llamas. ¿Estás comiendo bien? ¿Y tu sueño?"
    nombre_jugador "{i}Mi sueño... ya casi ni lo recuerdo.{/i}"    
    boss "[nombre_jugador], el cliente adelantó la entrega. Necesito que te quedes el fin de semana."
    menu:
        "Por supuesto, jefe":
            $ cansancio += 30
            $ estres += 20
            $ dinero +=800
            $ culpa -=10
            pass
        "Déjame ver cómo lo puedo acomodar":        
            $ estres -= 10
            $ culpa +=10
            $ dinero +=300
    ms "Oye, ¿vienes al nomikai (cena con los compañeros) esta noche? Todos van... el jefe también."
    menu:
        "Sí, voy":
            $ cansancio += 20
            $ dinero -=100
            $ culpa -=10
            pass
        "En un momento te confirmo qué puedo hacer.":        
            $ cansancio -= 10
            $ culpa +=10
    if cansancio >= 80:
        call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria")
        call screen presentacion("¡Te has quedado dormida en el tren! El jefe te ha regañado por llegar tarde.")
        $ estres += 20
        $ culpa += 20
        ks "Decir que sí a todos significa decirte que no a ti misma. Recuérdalo."
    jump capitulo5

label capitulo5:
    call screen presentacion("Capítulo 5: Límites con alternativas\n {i}6 meses después{/i}")
    nombre_jugador "{i}Ya manejo las frases indirectas, pero las tareas siguen regresando.{/i}"
    ms "[nombre_jugador], me dijiste que lo tenías ‘en el radar’... ¡hace tres semanas!"
    nombre_jugador "{i}Las frases indirectas solo pausan el problema...{/i}"
    ks "El siguiente nivel es decir que no y ofrecer otra cosa. Así cuidas la relación y también tu tiempo."
    call screen presentacion("Se desbloquean nuevas frases en la Libreta:\n\n‘Hoy no puedo, pero el jueves sí tengo espacio.’\n‘Puedo hacer esta parte, pero no todo.’\n‘Si tomo esto, ¿qué tarea dejo para después?’")
    boss "[nombre_jugador], necesito el reporte mensual, la presentación del cliente y que revises el trabajo de Mizuno. Todo para hoy."
    menu:
        "Sí, jefe.":
            $ cansancio += 30
            $ estres += 30
            $ dinero += 600
        "Si tomo esto, ¿qué tarea dejo para después?":
            $ estres -= 10
            $ culpa += 10
            $ dinero += 400
            $ frases_libreta += 1
            boss "Mmm... la presentación primero."
        "Lo tengo en el radar.":
            $ culpa += 20
            $ estres += 10
            ms "Esa frase ya no funciona igual que antes, [nombre_jugador]."
    ms "Oye... gracias por ser honesta. Yo tampoco puedo con todo."
    call screen presentacion("Mizuno se vuelve tu aliado: en los próximos capítulos ya no te pedirá favores con dinero.\n\nCansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria")
    jump capitulo6

label capitulo6:
    call screen presentacion("Capítulo 6: El colapso\n {i}1 año después{/i}")
    call screen presentacion("Ingreso al trabajo, 08 am.\nCuenta bancaria: $[dinero]. Muy lejos del 1.000.000.")
    nombre_jugador "{i}Un año y apenas tengo una pequeña parte. A este ritmo voy a necesitar... ¿40 años?{/i}"
    boss "Felicidades, [nombre_jugador]. Desde hoy eres líder de equipo. Claro, vas a necesitar quedarte hasta tarde... todos los días."
    menu:
        "¡Gracias, acepto!":
            $ dinero += 2000
            $ cansancio += 40
            $ estres += 30
            if cansancio >= 100 or estres >= 100 or culpa >= 100:
                jump final_agotamiento
        "Para hacerlo bien, necesitaría liberar un poco de tiempo.":
            $ culpa += 20
            boss "Entonces no estás lista."
        "No, gracias. Ahora no puedo aceptar más responsabilidades." if frases_libreta >= 5:
            $ culpa += 30
            $ estres -= 20
            $ cansancio -= 20
            boss "Entiendo. Tendré que buscar otra persona."
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria")
    ks "¿Sabes por qué salgo a las 6? A los 25 años terminé en el hospital. Ese día entendí que la empresa iba a seguir funcionando sin mí... pero yo no podía seguir sin mí."
    nombre_jugador "¿Y nunca quiso irse?"
    ks "Ese fue mi error. Mi sueño era abrir una tiendita de té junto al río. Todavía no lo hago."
    nombre_jugador "{i}No quiero llegar a los 40 diciendo ‘todavía no lo hago’.{/i}"
    jump capitulo7

label final_agotamiento:
    call screen presentacion("FINAL MALO: AGOTAMIENTO")
    nombre_jugador "{i}No puedo más...{/i}"
    call screen presentacion("Te desmayas en la oficina. Al despertar, estás en el hospital.")
    ks "La empresa puede seguir sin ti. Ahora tienes que aprender a cuidarte."
    return

label capitulo7:
    call screen presentacion("Capítulo 7: La última palabra\n {i}Algunas semanas después{/i}")
    nombre_jugador "{i}No llego al 1.000.000... pero hay suficiente para dar el primer paso.{/i}"
    nombre_jugador "{i}Creía que necesitaba el millón para empezar. En realidad necesitaba aprender a decir que no.{/i}"
    boss "[nombre_jugador], el proyecto del año empieza el lunes. Te quiero al frente. Son tres años de contrato, buen salario..."
    menu:
        "Lo tengo en el radar.":
            $ culpa += 10
            boss "Necesito una respuesta concreta."
            jump capitulo7
        "Déjame ver cómo lo puedo acomodar.":
            $ culpa += 10
            boss "No hay mucho que acomodar, [nombre_jugador]."
            jump capitulo7
        "Tendría que revisar mis prioridades.":
            $ culpa += 10
            boss "Tómate el tiempo que necesites."
            jump capitulo7
        "No. Gracias por todo, jefe Nushi, pero renuncio.":
            $ cansancio = 0
            $ estres = 0
            $ culpa = 0
            boss "...Yo también tenía un sueño, ¿sabes? Buena suerte, [nombre_jugador]."
            ms "¡Te voy a extrañar! Mándame fotos."
            ks "Pequeña... gracias. Me recordaste algo."
    jump epilogo

label epilogo:
    call screen presentacion("Epílogo: 1 año después")
    nombre_jugador "{i}Por fin estoy cumpliendo mi sueño.{/i}"
    call screen presentacion("Entra una clienta con corbata, sonriendo. Es Kawauso-senpai, que por fin también renunció. <3")
    call screen presentacion("Decir que no a otros a veces es decirte que sí a ti.")
    return

