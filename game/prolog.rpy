﻿define n = Character('Nicolas', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define d = Character('Dreidel', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define m = Character('Mutter', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define narrator = Character(None, what_slow_cps=True, ctc=anim.Blink("arrow.png"))

image bg flur = "bg/prolog/flur.jpg"
image bg küche = "bg/prolog/esszimmer.jpg"
image bg zimmer = "bg/prolog/zimmer.jpg"
image bg pc = "bg/prolog/pc.jpg"
image bg prolog = "bg/prolog.jpg"

label prolog1:
    
    scene bg prolog with fade
    
    pause 2
    
    hide bg prolog with fade
    
    scene bg flur
    
    pause 0.1
    
    play sound "se/tuerzu.ogg"
    
    "Ich knallte die Tür hinter mir zu und warf meinen Kram in die Ecke." with hpunch

    n "Ich bin zu Hause."

    "Meine Mutter kam aus der Küche."

    m "Willkommen daheim, Schatz."

    "Sie nicht weiter wahrnehmend, machte ich mich auf in Richtung Treppe, hoch in mein Zimmer."

    m "Musst du gleich wieder an den PC? Es gibt gleich Essen!"

    "Ja, musste ich."
    
    jump prolog2
label prolog2:
    scene bg zimmer with dissolve
    
    play sound "se/tuerzu.ogg"
    
    "Uff, endlich wieder in meinem Zimmer." with hpunch

    "Ich lies meinen Blick durchs Zimmer schweifen und setzte mich auf meinen Bürostuhl."

    "Was für ein Drecks-Schultag ..."

    "Mein Zimmer war im oberen Bereich des Hauses."

    "Die Wand gegenüber der Tür ging schräg nach unten."

    "Ein einzelnes Fenster spendete dieser Höhle ein wenig Licht."

    "Links der Tür befand sich mein Bett, rechts neben der Tür, in der Ecke, mein Computerschreibtisch mit Bürostuhl."

    "Ein Haufen Schrott sammelte sich in einer Kiste neben meinem PC."

    "Paar alte Elektrogeräte, sogar eine kaputte Mikrowelle die ich mal auf der Straße gefunden hatte standen dort herum."

    n "Mhh ..."

    "Nochmal ins TuS und im 'Triple Baka'-Thread nachschauen?"

    play sound "se/hochfahren.ogg"

    "Mein PC fuhr brummend hoch."

    "Ich legte den Kopf nach hinten und drehte mich in meinem Bürostuhl im Kreis."

    "Auch heute würde ich wieder nichts Sinnvolles gemacht werden."

    "Wie jeden Tag."

    "Mein Leben war langweilig."

    "Ich bremste ab und schaute in Richtung einer Zeichnung an der Wand."

    "... seufzte."

    n "Ach Yui."

    play sound "se/klopfen.ogg"

    "Das Klopfen an meiner Tür riss mich aus den Gedanken."

    d "Nicolas! Komm runter, es gibt Essen!"

    n "Ja ja ..."

    "Nicht mal ins Internet konnte ich jetzt."

    "Missmutig stapfte ich die Treppe runter."
    
    jump prolog3
label prolog3:
    scene bg küche with fade
    
    "Mein Bruder saß bereits zu Tisch und verschlang das Essen."

    "Er sah aus wie ein Mähdrescher."

    "Mein Blick schweifte durch das Esszimmer."

    "Ich zog mir einen Stuhl heran und setzte mich."

    m "Wie war dein Tag, Nicolas?"

    n "So wie immer."

    "Ich mochte keine Gespräche am Esstisch."

    d "Arbeitet Vater heute Abend wieder länger?"

    m "Sieht wohl so aus. Ich halte ihm das Essen im Ofen warm."

    "Es wurde wieder stiller am Tisch."

    d "Kann ich mal meine Freundin zum Essen mitbringen?"

    m "Sicher, natürlich doch."

    "Nicht das schon wieder!"

    "Gleich würde er wieder fra–"

    d "Hey Bruderherz, wann bringst du eigentlich deine Freundin mit?"

    n "..."

    m "Aber Dreidel! Hör auf deinen Bruder zu ärgern. Er findet schon noch eine."

    n "..."

    "Wie oft hatte ich bereits erwähnt, dass ich 3D Mädchen hasse?"

    "Sie stanken, waren nervig und kosteten Geld!"

    "Wozu die unnötige Last einer Freundin?"

    "Wie dem auch sei ..."

    "Ich aß schnell und stand auf."

    "Mein Bruder holte sich schon seinen vierten Nachschlag."

    "Sein Platz sah aus wie ein Schlachtfeld - seine Klamotten auch."

    "Ich brachte mein Geschirr in die Küche und räumte es weg."

    "Jetzt kann ich endlich wieder zurück in mein Zimmer."
    
    jump prolog4
label prolog4:
    play music "bgm/nicolas zimmer.ogg"
    scene bg zimmer with fade

    "Oben angekommen lies ich mich wieder in meinen Bürostuhl fallen und zog mich an meinen PC heran."
    
    scene bg pc with dissolve
    play sound "se/computer.ogg"

    "Ein paar gekonnte Klicks später war ich auch schon im Internet."

    "Ich durchsuchte die üblichen Fansubberseiten nach neuen Animefolgen."

    "Nur Moeblubkram ... Nonsense Anime ..."

    "Sofort mal geladen!"

    play sound "se/klicken.ogg"

    "Nebenher lief wieder ein Lied von ihr."

    "Mein Herz wurde schwer."

    "Ich hörte ihr Lied ... "

    "Ich war glücklich - für den Moment."

    "Wieso gab es solche Mädchen nicht wirklich?"

    "Ich seufzte wieder."

    "..."

    "....."

    "......."

    "Während der Anime lud könnte ich mal wieder ins TuS."

    n "Wo ist er?"

    "..."

    n "Da."

    "Ich klickte auf den täglichen TB-Thread."

    "TB steht für Triple Baka und entstand damals durch ein Video, welches ich gepostet hatte."

    "Man könnte also sagen, dass ich der Gründer war!"

    "Ich durchflog den Thread."

    "Shana hasste wieder, echt heftag."

    "Zeitmaschinen, Parallelwelten, Shota, diverser anderer Kram und Theorien."

    "Seit sie alle diesen Anime über eine Mikrowellenzeitmaschine gesehen hatten, wurde dauernd darüber geredet."

    "Gut, ich hatte damit angefangen."

    "Ich konnte froh sein, solche Idioten zu kennen."

    "In meiner Umgebung gab es niemand in der Art."

    "Den einzigen sozialen Kontakt, den ich noch hatte, war ein alter Freund."

    "Wahrscheinlich wäre diese zwischenmenschliche Beziehung verkümmert, wenn er mich nicht dauernd belästigt hätte."

    "Meistens kam er nur um sich auszuweinen, wenn eine seiner Freundinnen ihn schon wieder verlassen hatte."

    "Dass mich das nicht interessierte, schien er nicht zu merken."

    "Oder er wollte es nicht bemerken."

    "Keine Ahnung."

    "..."

    "Was machte ich eigentlich aus meinem Leben?"

    "Noch ein paar Monate und ich würde mein Abitur abgelegt haben ..."

    "Und danach?"

    "..."

    "Ich hatte keine Ahnung."

    "Mein Schnitt war nicht besonders berauschend."

    "Aber wenigstens war ich mit der Schule fertig."

    "Ich saß dort sowieso nur stumm in der Ecke."

    "Der Anblick der anderen weckte immer eine blinde Wut in mir."

#   "b-b-b-bird bird bird b-bird's the word"

#   "well everybody knows that the bird is the word"

    "Ich löse meinen Blick vom Bildschirm und lies ihn über den Schreibtisch wandern."

    "Er war schmutzig. Ich könnte ihn mal wieder saubermachen."

    "Papierhaufen stapelten sich in die Höhe, ein Haufen Müll, Essensreste und eine angefangene Flasche Korn."

    "Ich hatte es nicht so wirklich mit Alkohol, lag vielleicht daran, dass ich ihn weder mochte, noch welchen vertrug."

    "Anderseits war Korn das einzig Hochprozentige was schmeckte."

    "Mein Blick wanderte weiter und blieb an der Packung Taschentücher hängen."

    "Ich hatte heute noch ..."

    "Nicht viel denkend fing ich an."
    
    scene bg zimmer with Fade(0.5, 2, 0.5)
    
    "... und war auch schnell wieder fertig."

    "Eine leichte Drehbewegung des Bürostuhls, ein gekonnter Wurf und ..."

    n "Treffer!"

    "Ich traf in den Papierkorb."

    "Gott war mir langweilig ..."

    "..."
    
    jump prolog5
label prolog5:
    scene bg pc
    
    play sound "se/xfire.ogg"

    "Ein kleines Chatfenster tauchte auf dem Bildschirm auf."

    "Ah, es war Kyon."

    "Ein User aus dem Forum."

    "Ich mochte ihn und wir verstanden uns - eine Seltenheit."

    "Wir unterhielten uns über den TB-Thread und Parallelwelten."

    "Er war von diesen ganzen Dingen begeistert."

    "Wie wäre wohl die Welt, wenn ich die Vergangenheit ändern könnte?"

    "Es gäbe viel zu ändern. Viel Gutes zu tun."

    "Meine Geburt zu verhindern wäre ein Anfang gewesen - Haha ..."

    "Kyon" "Schau dir das mal an Nic!"

    "Kyon sendete mir einen Link."

    "Einen Link zu einem PDF, scheinbar eine Forschungsarbeit eines Professors."

    "Ich überfliog sie, las sie aber nicht wirklich."

    "Eine Theorie über Parallelwelten, Bahnen, sogenannte Weltenlinien."

    "Ich lies das Dokument offen, beschäftigte mich aber nicht weiter damit."

    "..."

    "Trotz dem Geplänkel mit Kyon stieg meine Langeweile."

    "Ich entschied mich ein paar frisch geladene Animefolgen auf meinen USB-Stick zu schieben."

    "Auf meinem neuen Fernseher war es ein Genuss, sie zu schauen."
    
    scene bg zimmer with dissolve

    "Ich steckte den USB-Stick in eine Klappe an der Seite des Fernsehers und machte es mir auf dem Bett bequem."

    "..."

    "....."

    "......."

    "Der Anime ist rührend."

    "Es geht um einen Jungen, der sich aus der Gesellschaft zurückgezogen hatte."

    "Früher hatte er viele Freunde, heute nicht mehr."

    "Wiederkennungswert pur."

    "Aus dem Augenwinkel lächelte mich die Schnapsflasche an."

    "Der Abend war sowieso beschissen, da konnte ein kleiner Schluck nicht schaden."

    "Alles, was meine Stimmung aufbesserte, war hilfreich."

    "Ich nahm ein altes Glas, welches schon länger auf dem Schreibtisch rumstand und füllte es mit Korn und Dk Pepper auf."

    "Mit dem Gemisch trottete ich zurück aufs Bett."

    "Der erste Schluck war unangenehm, aber mit jedem Mal floss es leichter die Kehle runter."

    "Das Glas war schneller als erwartet leer."

    "Während der Epilog ablief stand ich wieder auf, um die Schnapsflasche mit Dk Pepper aufzufüllen."

    "Noch 19 Folgen Anime warteten auf mich."

    "Ich musste meinen täglichen Bedarf decken."

    "Es sollte noch ein langer Abend werden."

    "..."

    "Mit jeder Folge weniger und jedem Glas mehr kam es mir vor, als würde meine Sicht verschwimmen."

    "Ich war ein erbärmlicher Anblick ..."

    "..."

    "Ein dumpfes Gefühl drückte meinen Kopf."

    "Meine Handlungen wurden immer kantiger."

    "Es war schwer dem Anime zu folgen, aber es fühlte sich so gut an."

    "Keine Trauer, keine Gedanken zu meiner Situation, keine Langeweile."

    "Nur Ruhe."

    "Ich wurde müde ..."

    "Will die Folge noch zu Ende schauen ..."

    "Ich musste wach bleiben ..."

    "Ich musste wa ..."

    "..."

    "....."

    "......."
    
    hide bg zimmer with Fade(2.0, 0, 0.5)
    
    stop music fadeout 1.0
    
    jump akt1_1
return


