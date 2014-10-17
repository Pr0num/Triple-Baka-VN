﻿define n = Character('Nicolas', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define d = Character('Dreidel', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define m = Character('Mutter', what_slow_cps=True, ctc=anim.Blink("arrow.png"))
define narrator = Character(None, what_slow_cps=True, ctc=anim.Blink("arrow.png"))

image bg flur = "bg/prolog/flur.jpg"
image bg küche = "bg/prolog/esszimmer.jpg"
image bg zimmer = "bg/prolog/zimmer.jpg"
image bg pc = "bg/prolog/pc.jpg"

label prolog1k:
    scene bg flur
    
    pause 0.1
    
    play sound "se/tuerzu.ogg"
    
    "Ich knalle die Tür hinter mir zu und werfe meinen Kram in die Ecke." with hpunch

    n "Ich bin zu Hause"

    "Meine Mutter kommt aus der Küche."

    m "Willkommen daheim, Schatz."

    "Sie nicht weiter wahrnehmend, mache ich mich auf in Richtung Treppe, hoch in mein Zimmer."

    m "Musst du gleich wieder an den PC? Es gibt gleich Essen!"

    "Ja, muss ich."
    
    jump prolog2k
label prolog2k:
    scene bg zimmer with dissolve
    
    play sound "se/tuerzu.ogg"
    
    "Uff, endlich wieder in meinem Zimmer." with hpunch

    "Ich lass meinen Blick durchs Zimmer schweifen und setze mich auf meinen Bürostuhl."

    "Was für ein drecks Schultag..."

    "Mein Zimmer ist im oberen Bereich des Hauses."

    "Die Wand gegenüber der Tür geht schräg nach unten. Ein einzelnes Fenster spendet dieser Höhle ein wenig Licht."

    "Links der Tür befindet sich mein Bett, rechts neben der Tür, in der Ecke, mein Computerschreibtisch mit Bürostuhl."

    "Ein haufen Schrott sammelt sich in einer Kiste neben meinem PC. Paar alte Elektrogeräte, sogar eine kaputte Mikrowelle die ich mal auf der Straße gefunden hatte steht dort rum."

    n "Mhh..."

    "Nochmal ins TuS und im “Triple Baka“-Thread nachschauen?"

    play sound "se/hochfahren.ogg"

    "Mein PC fährt brummend hoch."

    "Ich lege den Kopf nach hinten und drehe mich in meinem Bürostuhl im Kreis. Auch heute würde ich wieder nichts Sinnvolles machen."

    "Wie jeden Tag. Mein Leben ist langweilig."

    "Ich bremse ab und schaue in Richtung einer Zeichnung an der Wand, seufze."

    n "Ach Yui"

    play sound "se/klopfen.ogg"

    "Das Klopfen an meiner Tür reißt mich aus den Gedanken."

    d "Nicolas! Komm runter, es gibt Essen!"

    n "Ja ja..."

    "Nichtmal ins Internet kann ich jetzt."

    "Missmutig stapfe ich die Treppe runter."
    
    jump prolog3k
label prolog3k:
    scene bg küche with fade
    
    "Mein Bruder sitzt bereits zu Tisch und verschlingt das Essen."

    "Er sieht aus wie ein Mähdrescher."

    "Mein Blick schweift durch das Esszimmer"

    "Ich ziehe mir einen Stuhl heran und setze mich."

    m "Wie war dein Tag, Nicolas?"

    n "So wie immer."

    "Ich mag keine Gespräche am Esstisch."

    d "Arbeitet Vater heute Abend wieder länger?"

    m "Sieht wohl so aus. Ich halte ihm das Essen im Ofen warm."

    "Es wird wieder stiller am Tisch."

    d "Kann ich mal meine Freundin zum Essen mitbringen?"

    m "Sicher, natürlich doch."

    "Nicht das schon wieder! Gleich würde er wieder fra–"

    d "Hey Bruderherz, wann bringst du eigentlich deine Freundin mit?"

    n "........................."

    m "Aber Dreidel! Hör auf deinen Bruder zu ärgern. Er findet schon noch eine."

    n "........................."

    "Wie oft habe ich bereits erwähnt, dass ich 3D Mädchen hasse? Sie stinken, sind nervig und kosten Geld! Wozu die unnötige Last einer Freundin?"

    "Wie dem auch sei... Ich esse schnell auf und stehe auf."

    "Mein Bruder holt sich schon seinen vierten Nachschlag. Sein Platz sieht aus wie ein Schlachtfeld - seine Klamotten auch."

    "Ich bringe mein Geschirr in die Küche und räume es weg."

    "Jetzt kann ich endlich wieder zurück in mein Zimmer."
    
    jump prolog4k
label prolog4k:
    play music "bgm/nicolas zimmer.ogg"
    scene bg zimmer with fade

    "Oben angekommen lasse ich mich wieder in meinen Bürostuhl fallen und ziehe mich an meinen PC heran."
    
    scene bg pc with dissolve
    play sound "se/computer.ogg"

    "Ein paar gekonnte Klicks später bin ich auch schon im Internet."

    "Ich durchsuche die üblichen Fansubberseiten nach neuen Animefolgen. Nur Moeblubkram... Nonsense Anime..."

    "Sofort mal laden!"

    play sound "se/klicken.ogg"

    "Nebenher läuft wieder ein Lied von ihr, mein Herz wird schwer."

    "Ich höre ihr Lied... Ich bin glücklich - für den Moment."

    "Wieso gibt es solche Mädchen nicht wirklich?"

    "Ich seufze wieder."

    "......................................................................................................."

    "Während der Anime lädt könnte ich mal wieder ins TuS."

    n "Wo ist er?"

    n "Da."

    "Ich klicke auf den täglichen TB-Thread."

    "TB steht für Triple Baka und entstand damals durch ein Video, welches ich gepostet hatte. Man könnte also sagen, dass ich der Gründer bin!"

    "Ich durchfliege den Thread."

    "Shana hasst wieder, echt heftag."

    "Zeitmaschinen, Parallelwelten, Shota, diverser anderer Kram und Theorien."

    "Seit sie alle diesen Anime über eine Mikrowellenzeitmaschine gesehen haben, wird dauernd darüber geredet."

    "Gut, ich hab damit angefangen."

    "Ich kann froh sein, solche Idioten zu kennen. In meiner Umgebung gab es niemand in der Art."

    "Den einzigen sozialen Kontakt, den ich noch habe, ist ein alter Freund. Wahrscheinlich wäre diese zwischenmenschliche Beziehung verkümmert, wenn er mich nicht dauernd belästigen würde."

    "Meistens kommt er nur um sich auszuweinen, wenn eine seiner Freundinnen ihn schon wieder verlassen hatte. Dass mich das nicht interessierte, schien er nicht zu merken."

    "Oder er wollte es nicht bemerken. Keine Ahnung."

    show bg zimmer with fade
    
    "Was mache ich eigentlich aus meinem Leben?"

    "Noch ein paar Monate und ich würde mein Abitur ablegen... Und danach? Ich habe keine Ahnung."

    "Mein Schnitt ist nicht besonders berauschend, aber wenigstens bin ich mit der Schule fertig. Ich saß dort sowieso nur stumm in der Ecke."

    "Der Anblick der anderen weckte immer eine blinde Wut in mir."

#   "b-b-b-bird bird bird b-bird's the word"

#   "well everybody knows that the bird is the word"

    "Ich löse meinen Blick vom Bildschirm und lasse ihn über den Schreibtisch wandern."

    "Er ist schmutzig. Ich könnte ihn mal wieder saubermachen. Papierhaufen stapeln sich in die Höhe, ein haufen Müll, Essensreste und eine angefangene Flasche Korn"

    "Ich habe es nicht so wirklich mit Alkohol, liegt vielleicht daran, dass ich ihn weder mag, noch welchen vertrug. Anderseits ist Korn das einzig Hochprozentige was schmeckte."

    "Mein Blick wandert weiter und bleibt an der Packung Taschentücher hängen."

    "Ich hatte heute noch..."

    "Nicht viel denkend rufe ich einen Yui Doujin auf, fange an..."
    
    scene bg zimmer with Fade(0.5, 2, 0.5)
    
    "...und bin auch schnell wieder fertig."

    "Eine leichte Drehbewegung des Bürostuhls, ein gekonter Wurf und ..."

    n "Treffer!"

    "Ich treffe in den Papierkorb."

    "Gott ist mir langweilig..."

    jump prolog5k
label prolog5k:
    scene bg pc with fade
    
    play sound "se/xfire.ogg"

    "Ein kleines Chatfenster taucht auf dem Bildschirm auf."

    "Ah, es ist Kyon. Ein User aus dem Forum. Ich mag ihn und wir verstehen uns - eine Seltenheit."

    "Wir unterhalten uns über den TB-Thread und Parallelwelten. Er ist von diesen ganzen Dingen begeistert."

    "Wie wäre wohl die Welt, wenn ich die Vergangenheit ändern könnte? Es gäbe viel zu ändern. Viel Gutes zu tun."

    "Meine Geburt zu verhindern wäre ein Anfang - Haha..."

    "Kyon" "Schau dir das mal an Nic!"

    "Kyon sendet mir einen Link zu einem PDF, scheinbar eine Forschungsarbeit eines Professors."

    "Ich überfliege sie, lese sie aber nicht wirklich."

    "Eine Theorie über Parallelwelten, Bahnen, sogenannte Weltenlinien."

    "Ich lasse das Dokument offen, beschäftige mich aber nicht weiter damit. Trotz dem Geplänkel mit Kyon steigt meine Langeweile."

    "Ich entscheide mich ein paar frischgeladene Animefolgen auf meinen USB-Stick zu schieben. Auf meinem neuen Fernseher ist es ein Genuß, sie zu schauen."

    scene bg zimmer with dissolve

    "Ich stecke den USB-Stick in eine Klappe an der Seite des Fernsehers und mache es mir auf dem Bett bequem."

    show bg zimmer with fade

    "Der Anime ist rührend. Es geht um einen Jungen, der sich aus der Gesellschaft zurückgezogen hatte. Früher hatte er viele Freunde, heute nicht mehr."

    "Wiederkennungswert pur."

    "Aus dem Augenwinkel lächelt mich die Schnapsflasche an."

    "Der Abend ist sowieso beschissen, da kann ein kleiner Schluck nicht schaden. Alles, was meine Stimmung aufbesserte, ist hilfreich."

    "Ich nehme ein altes Glas, welches schon länger auf dem Schreibtisch rumsteht und fülle es mit Korn und Dk Pepper auf."

    "Mit dem Gemisch trotte ich zurück aufs Bett."

    "Der erste Schluck ist unangenehm, aber mit jedem Mal fließt es leichter die Kehle runter. Das Glas ist schneller als erwartet leer."

    "Während der Epilog abläuft, steh ich wieder auf, um die Schnapsflasche mit Dk Pepper aufzufüllen."

    "Noch 19 Folgen Anime warten auf mich. Ich muss meinen täglichen Bedarf decken. Ich habe mir sogar eine Tabellenkalkulation erstellt, die errechnet, wie viele Folgen ich am Tag schauen muss."

    "Es würde noch ein langer Abend werden... Mit jeder Folge weniger und jedem Glas mehr, kommt es mir vor, als würde meine Sicht verschwimmen."

    "Ich bin ein erbärmlicher Anblick..."

    "Ein dumpfes Gefühl drückt meinen Kopf. Meine Handlungen werden immer kantiger."

    "Es ist schwer dem Anime zufolgen, aber es fühlt sich so gut an."

    "Keine Trauer, keine Gedanken zu meiner Situation, keine Langeweile. Nur Ruhe."

    "Ich werde müde..."

    "Will die Folge noch zu ende schauen..."

    "Ich muss wach bleiben..."

    "Ich muss wa..."

    "............"

    "................."

    "......................"
    
    hide bg zimmer with Fade(2.0, 0, 0.5)
    
    jump akt1_1


