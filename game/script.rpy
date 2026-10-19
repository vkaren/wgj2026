# Coloca el código de tu juego en este archivo.

# Canal propio para las voces, separado de efectos y música
init python:
    renpy.music.register_channel("voz", mixer="voice", loop=False)

    def voz_masculina(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/male-voice.mp3", channel="voz")
        elif event == "slow_done":
            renpy.sound.stop(channel="voz")

    def voz_kawauso(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/kawauso-voice.mp3", channel="voz")
        elif event == "slow_done":
            renpy.sound.stop(channel="voz")

# Declara los personajes usados en el juego como en el ejemplo:

default nombre_jugador = ""
default cansancio = 0 
default estres =0 
default culpa =0
default dinero = 0
default ayudo_a_mizuno = False
define boss = Character("Jefe Nushi", callback=voz_masculina)
define ms = Character("Mizuno-san", callback=voz_masculina)
define ks = Character("Kawauso-senpai", callback=voz_kawauso)

# El juego comienza aquí.

label start:

    play music "audio/backgroundmusic.mp3" fadeout 0.5 fadein 1.0
    
    $ renpy.call_screen("pedir_nombre")

    $ nombre_jugador = nombre_jugador.strip()

    if nombre_jugador == "":
        $ nombre_jugador = "P"
   
    jump intro

label intro:
    #with  Fade(2.0, 0.5, 2.0)
    call screen presentacion ("Desde pequeña he tenido un sueño…. \n Logré conseguir trabajo en una reconocida empresa, la cual parece ser una oportunidad prometedora para crecer…\n Pronto será mi momento de brillar…necesito ahorrar 1.000.000 de dólares para lograrlo!\nPERO…. ¿A que costo?...") with Dissolve(1)
    jump capitulo1

label capitulo1:
    show screen barra_estadisticas
    call cambiar_escenario("bg escenario1")

    show nushi
    with dissolve
    boss "¡Hola! Bienvenida, soy el jefe Nushi. Antes que nada, necesito que revises este reporte sumamente importante."
    nombre_jugador "{i}Debo decirle que sí para mantener mi primer empleo y caerle bien a todos.{/i}"
    menu:
        "¡Sí, claro!":
            pass
        "¡Puedo hacerlo!":
            pass

    call cambiar_escenario("bg escenario2")
    call screen presentacion("2 horas más tarde...") with Dissolve(1)

    show nushi
    with dissolve
    boss "¿Ya está listo el reporte?"
    nombre_jugador "¡Sí, listo!"
    $ cansancio += 10
    $ dinero += 500
    boss "Muchas gracias."
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $[dinero] en la cuenta bancaria") with Dissolve(1)
    jump capitulo2
    
label capitulo2:
    call cambiar_escenario("bg escenario1")
    call screen presentacion("Capítulo 2: más favores\n [nombre_jugador]: Ingreso al trabajo, 08 am.") with Dissolve(1)

    show mizuno
    with dissolve
    ms "Oye, [nombre_jugador], necesito que hagas esta carga de datos. Te doy 100 dólares para que me ayudes pronto."

    menu:
        "¡Sí, entendido!":
            $ ayudo_a_mizuno = True
            $ cansancio += 20
            $ estres += 20
            $ culpa -= 10
            $ dinero += 100
            ms "¡Gracias, [nombre_jugador]! Ya me voy a casa."
            call cambiar_escenario("bg escenario2")

        "Lo cargo después del almuerzo":
            $ ayudo_a_mizuno = False
            $ cansancio += 10
            $ estres += 10
            $ culpa += 10
            $ dinero += 100
            ms "[nombre_jugador]... ¿y la carga? La necesitaba hace una hora."

    hide mizuno
    show nushi
    with dissolve
    boss "Hola, [nombre_jugador], ayúdame con esta presentación."

    menu:
        "Por supuesto.":
            $ cansancio += 20
            $ estres += 10
            $ dinero += 500

    if ayudo_a_mizuno:
        call cambiar_escenario("bg escenario3")
    else:
        call cambiar_escenario("bg escenario2")

    call screen presentacion("2 horas más tarde...") with Dissolve(1)

    show nushi
    with dissolve
    boss "Buen trabajo, [nombre_jugador]. Mañana te espero temprano."

    hide nushi
    with dissolve

    call screen presentacion("6:00 pm. En el escritorio del fondo, una silueta pequeña con corbata apaga su computadora y se va tranquilamente.") with Dissolve(1)
    nombre_jugador "{i}¿Alguien se va a las 6? Yo todavía tengo trabajo...{/i}"
    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria") with Dissolve(1)
    jump capitulo3

label capitulo3:
    call cambiar_escenario("bg escenario1")
    call screen presentacion("Capítulo 3:  La nutria del escritorio del fondo\n {i}2 semanas después{/i}") with Dissolve(1)

    nombre_jugador "{i}Son las 8 pm y la oficina sigue llena. Nadie se va antes que el jefe.{/i}"
    nombre_jugador "{i}Llevo dos semanas saliendo a las 10 pm... pero mi cuenta crece. Debo aguantar.{/i}"

    # Llega Kawauso
    show kawauso
    with dissolve
    ks "Tú eres la nueva, ¿verdad? Llevo 15 años aquí. Soy la única que sale a las 6 pm todos los días."
    nombre_jugador "¿Cómo lo hace? ¿No la regañan?"
    ks "Nunca digo “no”... pero tampoco digo “sí” a todo. Escucha bien, pequeña."

    # Mizuno llega corriendo (Kawauso se queda)
    show mizuno
    with moveinright
    ms "[nombre_jugador], ¿me ayudas con mis correos pendientes? Te doy 50 dólares."

    menu:
        "¡Claro, ahora mismo!":
            $ cansancio += 20
            $ estres += 10
            $ dinero += 50
            $ culpa -= 10
            hide mizuno
            with dissolve

        "¡Lo pongo en mi lista para revisarlo!":
            $ estres -= 10
            $ culpa += 10
            hide mizuno
            with dissolve
            ks "¿Ves? No le dijiste que no. Solo no le dijiste que sí ahora."

    hide kawauso
    with dissolve

    call screen presentacion("Cansancio: [cansancio], estrés: [estres], culpa: [culpa], $ [dinero] en la cuenta bancaria") with Dissolve(1)
    return

label cambiar_escenario(fondo):
    window hide
    scene expression fondo
    show jugadora
    with fade
    $ renpy.pause(3.0, hard=True)
    return