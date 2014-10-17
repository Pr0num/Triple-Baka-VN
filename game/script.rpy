label start:
    
    stop music fadeout 2.0
    
    jump prolog1

image bg main = "bg/menu.png"

label chapter_select:
    
    stop music fadeout 2.0
    
    scene bg main
    
    menu:

        "Prolog":
        
            jump prolog1
       
        "Akt 1":
            
            jump akt1_1
            
return


