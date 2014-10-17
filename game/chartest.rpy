#chardefines
define p = Character('Panda')
define po = Character('Panda und Orange')
define o = Character('Orange', color="#ff6f00")

#charbilder
image p happy o erstaunt = "cs/phappyoerstaunt.png"
image p happy o happy = "cs/phappyohappy.png"
image p happy o neutral = "cs/phappyoneutral.png"
image p happy o normal = "cs/phappyonormal.png"
image p happy o schlaf = "cs/phappyoschlaf.png"
image p neutral o schlaf = "cs/pneutraloschlaf.png"

#BGs
image bg paper = "a00.jpg"


label chartest:
        scene bg paper at truecenter
        show p neutral o schlaf with moveintop
        
        p "Wo sind wir?" with hpunch
        
        p "Hallo?"
        
        show p happy o schlaf with dissolve
        p "Hey, wir sind in der TB VN!"
        
        p "Orange, wach auf! Wir sind in der TB VN!"
        
        show p happy o normal with dissolve
        o "Hö? Was ist los? Was willst du?"
        
        show p happy o erstaunt with dissolve
        o "Warte, ist das die TB VN? Sie lebt?"
        
        p "Jawohl, meine Orange!"
        
        show p happy o happy with dissolve
        o "Exzellent, weitermachen."
        
        return
