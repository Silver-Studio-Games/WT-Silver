

### Wear My Cum ###

label hg_ps_WearMyCum: #Walk around school covered in genies cum 
    hide screen hermione_main
    with d3
    
    m "{size=-4}(Should I ask her to walk around with my cum on her face?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
            
    m "[hermione_name]?"
    call her_main("Yes, [genie_name].",xpos="right",ypos="base") 
    
    call play_music("playful_tension") # SEX THEME.
    m "Today I have another small favor to ask of you."
    call her_main("What is it?","base","base") 
    m "I'd like you to attend class."
    call her_main("Of course...","base","base") 
    m "After I cum on you...."
    
    if whoring < 10:
        jump too_much
    elif whoring < 15: 
        jump hg_ps_WearMyCum_Scene_1
    elif whoring < 20:
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 2
    else:
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 3







label hg_ps_WearMyCum_Scene_1:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("What?!?","shock","wide") 
    call her_main("You can't be serious!","angry","angry") 
    call her_main("It's bad enough that I let you cum on me in private!","annoyed","annoyed") 
    call her_main("But in public?","angry","annoyed",emote="01") 
    call her_main("I think I better leave...","annoyed","angry") 
    m "Wait, wait, wait."
    m "What about if nobody could see it?"
    call her_main("Well I suppose that would be alright...","annoyed","annoyed") 
    call her_main("But what's the point if they can't see it?","annoyed","worriedL") 
    m "You'll know it's there."
    call her_main("Hmmmm...","annoyed","angryL") #Haggle here
    call her_main("How much will I be paid?","annoyed","suspicious") 
    m "30 points."
    call her_main("30! I expect at least 70 for such a filthy act!","scream","worriedCl") 
    m "40."
    call her_main("60!","scream","angryCl") 
    m "50 points, final offer."
    call her_main("Ok, I'll do it.","annoyed","worriedL") 
    m "Really?"
    call her_main("As long as nobody can see it then I don't see the big issue.","annoyed","angryL") 
    m "Splendid. Care to give me a hand?"
    call her_main("...","base","down") 
    
    #Start jerk off chibis
    hide screen hermione_main
    call blkfade 

    call her_chibi("hide") 
    call gen_chibi("handjob","desk","base") 
    
    show screen chair_left
    hide screen desk
    show screen desk
    
    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    call ctc 
    
    call her_head("Why are you making me do this, [genie_name]?","angry","base") 
    m "What do you mean?"
    call her_head("Why are you making me jerk you off...","angry","down_raised") 
    call her_head("So that you can cum on me...","soft","ahegao") 
    call her_head("And make me wear it around the school?","open","worriedCl") 
    m "I'm not making you do anything."
    m "You're doing this because I asked you to."
    call her_head("But if I don't, Gryffindor will lose the house cup.","shock","worriedCl") 
    m "And?"
    call her_head("Harry and Ron will be so dissapointed...","angry","worried") 
    m "So that's why you are doing this? For those two boys?"
    call her_head("Sort of... I'm not sure that they'd be too upset though.","annoyed","worriedL") 
    m "Are you sure it's not because you love it."
    call her_head("What?","upset","wink") 
    m "Coming in here whenever I summon you."
    m "Doing whatever I tell you, whenever I tell you."
    m "Doing slutty things in front of your peers because I tell you."
    call her_head("...","disgust","down_raised") 
    m "I'll tell you what, I'll make things interesting."
    m "So long as I cum on you and you wear it around classes today, Gryffindor will get 50 points."
    call her_head("How does that make it interesting?","disgust","glance") 
    m "Because I'll let you choose where I cum."
    call nar(">You fell her hands tense around your cock.") 
    call her_head("You're letting me choose?","smile","baseL") 
    m "Anywhere, as long as it's on you. It can be your shoes for all I care."
    call her_head("Ok...","base","squint") 
    m "Well hurry up [hermione_name], classes will start soon."
    call nar(">She starts jerking your cock with renewed vigour.") 
    m "So where are you going to hide it?"
    call her_head("I'm not sure.","upset","wink") 
    call her_head("I'm trying to think of somewhere no one will be able to see it.","upset","wink") 
    m "Well you better think of some place soon!"
    call her_head("Why's that?","angry","wink") 
    g9 "Because I'm about to cum!"
    call her_head("Already? Where should I-","angry","wide") 
    
    menu:
        "-Stay Silent-": # Cum under shirt
            $ cum_location = 1
            call nar(">Hermione swiftly pulls her shirt up...","start") 
            call nar(">You can feel her incredibly soft tits rubbing against the tip of your cock, making you cum!","end") 
            g4 "{size=+5}ARGH! YES!!!{/size}"
            
            hide screen hermione_main
            hide screen bld1
            call gen_chibi("cumming_under_shirt") 
            call cum_block 
            pause.5

            call her_head("!!!!!!!!!!!","shock","wide") 

            $ aftersperm = True

            call her_main("Well, this shouldn't be too bad...","upset","wink") 
            m "I'm sure no one will notice."
            call her_main("They better not.","angry","angry") 

        "\"Just keep on jerking [hermione_name]!\"": # Cum on skirt 
            $ cum_location = 2
            
            call nar(">Hermionely keeps jerking your cock, her eyes darting between it and herself.") 
            g4 "Get ready whore, here it comes!"
            call her_head("Wait, where am I supposed to-","angry","worried") 
            g9 "{size=+5}ARGH! YES!!!{/size}"
            
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            
            hide screen hermione_main
            hide screen bld1
            call gen_chibi("cumming_on_shirt") 
            call cum_block 
            pause.5
            
            $ u_sperm = "characters/hermione/face/auto_11.png"
            $ uni_sperm = True
            
            call her_main("!!!!!!!!!!!","shock","wide") 
            m "That's it, all over you slut."
            call her_main("...","annoyed","down") 
            
            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause") 
            call ctc 
            
            call her_main("Will that be all [genie_name].","annoyed","ahegao") 
            m "I don't suppose you could kiss it for good luck?"
            call her_main("I don't think so.","annoyed","angryL") 
            m "Well then that should be all then [hermione_name]."

        "\"Take it on your face slut!\"":
            $ cum_location = 3
            
            call nar(">Hermione bends down and place your cock in front of her face.") 
            m "Get ready slut, here it comes!"
            call her_head("...","scream","wide_stare") 
            g9 "{size=+5}ARGH! YES!!!{/size}"
            call her_head("I can't...","clench","down_raised") 
            
            call nar(">Hermione moves your cock away from her face at the last second.","start") 
            call nar(">You erupt over the top of her head, covering her hair in your spunk.","end") 
            
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt") 
            call cum_block 
            pause.5
            
            $ u_sperm = "characters/hermione/face/auto_12.png"
            $ uni_sperm = True
            
            call her_main("!!!!!!!!!!!","shock","wide") 
            m "Yes... I Feel so much better now..."
            call her_main("..............","normal","worriedCl") 
            
            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause") 
            call ctc 
            
            call her_main("How could you!","scream","worriedCl") 
            m "How could I?"
            call her_main("You told me to let you cum on my face!","scream","angryCl") 
            m "I did."
            call her_main("Why would you say something like that!","mad","worriedCl",tears="soft_blink") 
            call her_main("If I hadn't moved at the last second my face would be covered!","angry","base",tears="soft") 
            m "You didn't have to listen to me."
            call her_main("What?","angry","worried") 
            m "I only said that you had to have my cum on you."
            m "I never said where."
            call her_main("You mean I didn't have to...","annoyed","worriedL") 
            m "Not at all."

    hide screen hermione_main
    call blkfade 
    
    ">You tuck your cock back into your robe."
    
    call gen_chibi("hide") 
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") 
    
    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    
    
    m "Oh and one last thing before you head to class."
    call her_main("Yes...","annoyed","annoyed",xpos="right",ypos="base") 
    m "If you return to this office after classes without any cum on you, Slytherin will get 200 points." 
    call her_main("{size=+10}200! That is not fair!{/size}","shock","wide") 
    m "It's Only unfair if you clean it off."
    call her_main("...","angry","angry") 

    jump end_hg_pf




label hg_ps_WearMyCum_Scene_2:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Again?","shock","wide") 
    call her_main("You can not be serious!","angry","angry") 
    call her_main("I already let you do this to me once, isn't that enough?","annoyed","annoyed") 
    m "It's enough when I say it's enough."
    m "Besides, was it really such an issue last time?"
    call her_main("Well I guess not...","annoyed","base") 
    call her_main("But will it still be hidden this time?","annoyed","worriedL") 
    m "That's up to you."
    call her_main("Hmmmm...","annoyed","angryL") #Haggle here
    call her_main("How much will I be paid this time then?","annoyed","suspicious") 
    m "20 points."
    call her_main("20! we agreed on 50 last time!","scream","worriedCl") 
    m "40."
    call her_main("70!","scream","angryCl") 
    m "50 points, final offer."
    call her_main("80 and I'll let people see it.","base","glance") 
    m "Really?"
    call her_main("As long as it isn't too obvious.","base","down") 
    m "Deal."
    call her_main("...","base","down") 

    #Start jerk off chibis
    hide screen hermione_main
    call blkfade 

    call her_chibi("hide") 
    call gen_chibi("handjob","desk","base") 
    
    show screen chair_left
    hide screen desk
    show screen desk
    
    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    call ctc 
    
    call her_head("Why are you asking me to do this [genie_name]?","angry","base") 
    m "This question again?"
    m "Let me answer your question with one of my own."
    call her_head("Ok...","angry","down_raised") 
    m "Why are you jerking me off [hermione_name]?"
    call her_head("Because you asked me to...","soft","ahegao") 
    m "And is that the only reason?"
    call her_head("No...","open","worriedCl") 
    m "Are you sure?"
    m "What is your other reason then?"
    call her_head("if I don't, Gryffindor will lose the house cup.","shock","worriedCl") 
    m "That lie again?"
    call her_head("It's not a lie...","angry","worried") 
    m "So you'd rather win the house cup than make me happy?"
    call her_head("Maybe... Can't I do both?","annoyed","worriedL") 
    m "You can..."
    call her_head("Good","base","squint") 
    m "But I want you to be honest."
    m "So I'm going to give you a choice."
    m "You can stop jerking me off right now, leave the room and I'll give you the 80 points. However, I'll be very upset."
    call her_head("or?","open","base") 
    m "Or, you can keep jerking me off, wear my cum around the school and get no points."
    call her_head("NO POINTS?","scream","worriedCl") 
    m "None. You will make an old man very happy though."
    call her_head("Can't you just pay me for wearing your cum?","angry","worriedCl",emote="05") 
    m "No."
    call nar(">You fell her hands tense around your cock.") 
    call her_head("You're making me choose? Between getting 80 points for doing nothing.","annoyed","annoyed") 
    call her_head("Or getting paid nothing for wearing your cum around the school.","angry","annoyed",emote="01") 
    m "Indeed I am [hermione_name]."
    call her_head("{size=-5}Ok...{/size}","disgust","down_raised") 
    m "Well hurry up [hermione_name], classes will start soon, best make your decision."
    call nar(">She starts jerking your cock with renewed vigour.") 
    call her_head("...","annoyed","suspicious") 
    call her_head("You better appreciate this.","annoyed","angryL") 
    m "Oh I'm appreciating it!"
    call her_head("Really?","open","base") 
    g9 "You're about to see how much I'm appreciating it!"
    call her_head("What, Already? Where should I-","angry","wide") 
    
    menu:
        "-Stay Silent-": # Legs
            $ cum_location = 4
            
            call nar(">Hermionely keeps jerking your cock, her eyes darting between it and herself.") 
            g4 "Get ready slut, here it comes!"
            call her_head("Wait, where am I supposed to-","angry","worried") 
            g9 "{size=+5}ARGH! YES!!!{/size}"
            
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt") 
            call cum_block 
            pause.5
            
            $ u_sperm = "characters/hermione/face/auto_13.png"
            $ uni_sperm = True
            
            call her_main("!!!!!!!!!!!","shock","wide") 

            m "That's it, all over your milky thighs."
            call her_main("...","annoyed","down") 
            
            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause") 
            call ctc 
            
            call her_main("Will that be all [genie_name].","annoyed","ahegao") 
            m "I don't suppose you could kiss it for good luck?"
            call her_main("...{p}...","base","ahegao_raised") 
            
            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("handjob_kiss") 
            $ renpy.play('sounds/kiss.mp3') 
            with kissiris
            call ctc 
            
            call gen_chibi("cumming_on_shirt_pause") 
            m "Good girl."

        "\"Just keep on jerking [hermione_name]!\"": # Cum on shirt front 
            $ cum_location = 5
            
            call nar(">Hermionely keeps jerking your cock, her eyes focused intently on it.") 
            g4 "Get ready whore, here i come!"
            call her_head("...","angry","worried") 
            g9 "{size=+5}ARGH! YES!!! RIGHT ON THOSE TITS!{/size}"
            
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt") 
            call cum_block 
            pause.5
            
            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True
            
            call her_main("!!!!!!!!!!!","shock","wide") 
            m "That's it, all over you slut."
            call her_main("...","annoyed","down") 
            
            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause") 
            call ctc 
            
            call her_main("It's all over me.","annoyed","ahegao") 
            m "That it is."
            call her_main("I think I should go now...","annoyed","down") 

        "\"Take it on your face slut!\"":
            $ cum_location = 6
            
            call nar(">Hermione bends down and place your cock in front of her face.") 
            m "Get ready slut, here it comes!"
            call her_head("...","scream","wide_stare") 
            g9 "{size=+5}ARGH! YES!!!{/size}"
            call her_head("...","clench","down_raised") 
            call nar(">You erupt onto her face, dousing her in your spunk.") 

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt") 
            call cum_block 
            pause.5
            
            $ u_sperm = "characters/hermione/face/auto_07.png"
            $ uni_sperm = True
        
            call her_main("!!!!!!!!!!!","shock","wide") 
            m "Yes... I Feel so much better now..."
            call her_main("..............","normal","worriedCl") 

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause") 
            call ctc 
            
            call her_main("How could you!","scream","worriedCl") 
            m "How could I?"
            call her_main("You came all over my face!","scream","angryCl") 
            m "I did."
            call her_main("Why would you ask me to do that!","mad","worriedCl",tears="soft_blink") 
            call her_main("I'm completely covered in your cum!","angry","base",tears="soft") 
            m "You didn't have to listen to me."
            call her_main("...","angry","worried") 
            m "I only said that you had to have my cum on you."
            m "I never said where."
            call her_main("You told me to do it though...","annoyed","worriedL") 

    hide screen hermione_main
    call blkfade 
    
    ">You tuck your cock back into your robe."
    
    call gen_chibi("hide") 
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") 
    
    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    
    m "Oh and one last thing before you head to class."
    call her_main("Yes...","soft","ahegao",xpos="right",ypos="base") 
    m "If you return to this office after classes without any cum on you, I'll be very upset." 
    call her_main("Yes [genie_name].","base","ahegao_raised") 
    m "Have fun. Say hi to your friends for me."
    call her_main("...","base","closed") 

    jump end_hg_pf


label hg_ps_WearMyCum_Scene_3:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Are you serious?","shock","wide") 
    call her_main("Can I?","grin","ahegao") 
    m "well-"
    call her_main("I was going to ask you if I could seeing as how it made you so happy last time [genie_name].","smile","happyCl",emote="06") 
    call her_main("I'll even do it for free if that would make you happier!","base","ahegao_raised") 
    m "really?"
    m "Well let's get started then!"
    #Start jerk off chibis
    hide screen hermione_main            
    hide screen bld1
    with d3
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3

    hide screen genie
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "handjob_ani"
    show screen chair_left
    show screen g_c_u
    show screen desk_02
    hide screen blktone
    hide screen hermione_walk_01 
    hide screen blkfade
    $ hermione_head_ypos = 235
    m "Gods, you're good at this, [hermione_name]!"
    call her_head("Thank you... I've been thinking about what you asked me last time...","soft","ahegao") 
    m "Last time?"
    call her_head("about why I do this... sell you these sort of favours.","upset","closed") 
    call her_head("At the start it was just to get points, so that \'gryffindor\' could win the house cup...","angry","wink") 
    call her_head("but lately...","base","down") 
    call her_head("...it’s been more than that... now I do it to make you happy, [genie_name].","base","glance") 
    call her_head("Because making you happy, makes me happy...","base","suspicious") 
    m "That's great... but what would really make me happy right now is you focusing a little more on the task at hand..."
    call her_head("Oh! Of course, [genie_name]...","open","worriedCl") 
    call her_head("Do you need some extra encouragement?","open","closed") 
    m "it would help..."
    call her_head("well... do you know how much I've been thinking about this? How much I wanted to ask you to cover me again?","base","down") 
    call her_head("I've become such a slut [genie_name], it's all I've been able to think about... going to class covered in your {image=textheart}cum{image=textheart}","grin","ahegao") 
    call her_head("I Imagine it staining my uniform, so much that I can never wash it out. I imagine being covered in your cum constantly. So everyone knows who and what I am.”","grin","dead") 
    call her_head("not just A slut... a cumslut...","soft","ahegao") 
    call her_head("Your {image=textheart}cum{image=textheart}slut...","silly","ahegao") 
    g9 "That did it slut!"
    g4 "HERE IT COMES!!!"
    call her_head("Shoot it wherever you want [genie_name]...","open_wide_tongue","ahegao") 
    menu:
        "\"take it on your tits!\"": # Cum on shirt front 
            $ cum_location = 7
            call her_head("Please cover my tits with your sticky cum! I need it, [genie_name]!","grin","ahegao") 
            ">Hermionely keeps jerking your cock, her eyes focused intently on it."
            g4 "Get ready whore, here i come!"
            call her_head("...","silly","dead") 
            ">Hermione leans forward, lining up her tits directly with your cock."
            g9 "{size=+5}ARGH! YES!!! RIGHT in between your TITS!{/size}"
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
            $ uni_sperm = True
            call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down") 
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            m "That's it, all over you slut."
            call her_main("......","soft","ahegao") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("It's so warm...{image=textheart}","grin","dead") 
            m "That it is."
            call her_main("If it's alright with you, I think I better head to class now...","base","down") 

        "\"Take it on your face, slut!\"":
            $ cum_location = 8
            ">Hermione bends down and place your cock in front of her face."
            m "Get ready slut, here it comes!"
            call her_head("Please give it to me! I need it, [genie_name]!","grin","ahegao") 
            g9 "{size=+5}ARGH! YES!!!{/size}"
            call her_head("...","open_wide_tongue","ahegao") 
            ">You erupt onto her face, dousing her in your thick spunk."
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
            $ uni_sperm = True
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            call her_main("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao") 
            m "Yes... I Feel so much better now..."
            call her_main("me too...","normal","worriedCl") 
    show screen hermione_stand 
    hide screen chair_left
    hide screen desk_02
    show screen genie
    hide screen g_c_u
    $ her_head_ypos = her_head_tits
    hide screen blkfade
    with d5
    ">You tuck your cock back into your robe."
    m "I’ll see you after classes. And as before, if you come back without any cum on you, I’ll be very disappointed."
    call her_main("of course [genie_name]...","soft","ahegao") 
    call her_main("(I can't wait to see the look on peoples faces...)","grin","dead") 

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 500 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_blink #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3

    jump end_hg_pf



label hg_ps_WearMyCum_complete: #Hermione returns from her day of wearing your cum
    $ hg_ps_WearMyCum_OBJ.inProgress = False
    $ hg_ps_WearMyCum_OBJ.complete = True
    if cum_location <= 3:
        jump hg_ps_WearMyCum_complete_1
    else:
        jump hg_ps_WearMyCum_complete_2


label hg_ps_WearMyCum_complete_1:

    call play_sound("door") 
    call her_walk("door","mid",2) 
    
    if cum_location == 1: #Cum under shirt
        $ aftersperm = True
        call her_main("...I did it, [genie_name].","base","squint",xpos="right",ypos="base") 
        call her_main("I kept your cum on me all day.","base","baseL") 
        
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                call her_main("Thank you [genie_name], will that be all?","soft","base") 
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","open","closed") 
                m "And do you think that anyone noticed?"
                call her_main("I don't think so [genie_name]. Ginny Weasley asked me about it during transfiguration class though.","soft","base") 
                m "And what did you tell her?"
                call her_main("I just said that I spilled some Wiggenweld potion on myself in potions class.","open","base") 
                m "Very cunning of you. 50 points to Gryffindor."
                $ gryffindor += 50
                call her_main("Thank you [genie_name], if that's all I might head to bed.","soft","base") 
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","base","base") 
                
    elif cum_location == 2: #Cum on skirt 
        $ u_sperm = "characters/hermione/face/auto_11.png"
        $ uni_sperm = True
        
        call her_main("...I did it [genie_name].","normal","worriedCl",xpos="right",ypos="base") 
        call her_main("I kept your cum on me all day.","angry","worriedCl",emote="05") 
        
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                call her_main("Thank you [genie_name], will that be all?","annoyed","worriedL") 
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                $ sc34CG(1, 10, 2)
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","annoyed","worriedL",xpos="base",ypos="base") 
                m "And do you think that anyone noticed?"
                call her_main("I think a few people did [genie_name]. I could hear The first years all whispering as I walked past.","grin","worriedCl") 
                m "And how did you feel?"
                call her_main("Excited. I just wish that they knew why I was doing this.","base","down") 
                m "Speaking of that, 50 points to Gryffindor."
                $ gryffindor += 50
                call her_main("Oh, right the points, Thank you [genie_name]. if that's all I might head to bed.","open","down") 
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","annoyed","closed") 
                
    else: #Cum on hair
        $ u_sperm = "characters/hermione/face/auto_12.png"
        $ uni_sperm = True
        
        call her_main("...I did it [genie_name].","upset","dead",tears="mascara",xpos="right",ypos="base") 
        call her_main("I kept your cum on me {p}all day.","upset","worriedCl",tears="mascara_soft_blink") 
        
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                $ mad += 5
                call her_main("...","annoyed","annoyed",tears="mascara_soft") 
                m "Well [hermione_name], you may leave now."
                call her_main("Hmmmphh...","angry","annoyed",emote="01",tears="mascara") 
            "\"Tell me about your day.\"":
                $ mad += 10
                $ sc34CG(1, 8, 8)
                call her_main("My day...","normal","worriedCl",tears="mascara_soft_blink",xpos="base",ypos="base") 
                call her_main("This was the worst day of my life!","scream","worriedCl",tears="mascara_soft_blink") 
                call her_main("I've never been so ashamed!","angry","worriedCl",emote="05",tears="mascara_soft_blink") 
                m "Did your friends treat you poorly?"
                call her_main("No! That's the worst part!","scream","angryCl",tears="mascara_soft_blink") 
                call her_main("I expected to be an outcast, to sit by myself and not have Ginny or Luna talk to me.","annoyed","worriedL",tears="mascara_soft_blink") 
                call her_main("But they didn't even acknowledge the fact that I was covered in cum!","annoyed","angryL",tears="mascara_soft_blink") 
                call her_main("They acted as if nothing was wrong.","mad","worriedCl",tears="mascara_soft_blink") 
                call her_main("I even tried to provoke a response from Ginny by asking her what she thought of my hair!","angry","base",tears="mascara_soft") 
                m "And what was her reaction?"
                call her_main("She said that it suited me!","upset","worriedCl",tears="mascara_soft_blink") 
                m "Maybe they're just used to you acting like this."
                call her_main("That's the problem! They think that this slutty persona is who I am now!","angry","worried",tears="mascara_soft") 
                m "Isn't it?"
                call her_main("...","upset","worriedCl",tears="mascara_soft_blink") 
                call her_main("Good night, [genie_name].","normal","worriedCl",tears="mascara_soft_blink") 

    hide screen sccg 
    show screen blkfade
    with fade
    jump end_hg_pf


label hg_ps_WearMyCum_complete_2:

    call play_sound("door") 
    call her_walk("door","mid",2) 
    
    if cum_location == 4: #Cum on legs
        $ u_sperm = "characters/hermione/face/auto_13.png"
        $ uni_sperm = True
        
        call her_main("...I did it, [genie_name].","base","squint",xpos="right",ypos="base") 
        call her_main("I kept your cum on me all day.","base","baseL") 
        
        menu:
            "\"Good Work!\"":
                call her_main("Thank you [genie_name], will that be all?","soft","base") 
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, well, except for Luna...","open","closed") 
                m "Luna?"
                call her_main("Luna Lovegood, sir.","soft","base") 
                m "What happened with miss Lovegood?"
                call her_main("She kept trying to tell me that a Cornish pixie had given me a present.","annoyed","angryL") 
                m "A cornish pixie had given you a present?"
                call her_main("I didn't know what she was talking about either. Cornish pixies are nasty little things that would never do anything nice.","disgust","glance") 
                m "Well what happened after that?"
                call her_main("Well I asked her what she was talking about and then she ran her finger up my leg, scooping up some of your cum!","smile","glance") 
                m "Really?"
                call her_main("That's not the worst part. She then proceded to taste it!","open_tongue","glance") 
                m "I don't believe you."
                call her_main("I was as shocked as you were.","open","closed") 
                m "Well you have certainly made this old man very happy."
                call her_main("Thank you [genie_name]. if that's all I might head to bed.","open","down") 
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","annoyed","closed") 
                
    elif cum_location == 5: #Cum on shirt 
        $ u_sperm = "characters/hermione/face/auto_06.png"
        $ uni_sperm = True
        
        call her_main("...I did it, [genie_name].","normal","worriedCl",xpos="right",ypos="base") 
        call her_main("I kept your cum on me all day.","angry","worriedCl",emote="05") 
        
        menu:
            "\"Good Work!\"":
                call her_main("Thank you [genie_name], will that be all?","annoyed","worriedL") 
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                $ sc34CG(1, 14, 7)
                call her_main("It was a pretty normal day, I had Defense against the dark arts class and then herbology.","annoyed","worriedL",xpos="base",ypos="base") 
                m "And do you think that anyone noticed?"
                call her_main("I think most people did [genie_name]. I'm not sure if they all knew it was cum though.","grin","worriedCl") 
                m "And how did you feel?"
                call her_main("Excited. Getting to see everyone's faces as they realised what it was...","base","down") 
                m "So you don't mind them knowing?"
                call her_main("I suppose not... As long as it makes you happy.","open","down") 
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","annoyed","closed") 
                
    else: #Cum on face
        $ u_sperm = "characters/hermione/face/auto_07.png"
        $ uni_sperm = True
        
        call her_main("...I did it, [genie_name].","annoyed","dead",tears="mascara",xpos="right",ypos="base") 
        call her_main("I kept your cum on me {p}all day.","annoyed","dead",tears="mascara") 
        
        menu:
            "\"Good Work!\"":
                call her_main("...","annoyed","dead",tears="mascara") 
                m "Well [hermione_name], you may leave now."
                call her_main("Did I at least make you happy?","open","annoyed",tears="mascara") 
                m "You did."
                call her_main("Good.","annoyed","closed",tears="mascara") 
            "\"Tell me about your day.\"":
                $ sc34CG(1, 16, 6)
                call her_main("My day...","normal","worriedCl",tears="mascara",xpos="base",ypos="base") 
                call her_main("It was completely normal.","scream","worriedCl",tears="mascara") 
                m "Really? Nothing strange happened at all?"
                call her_main("No. Everyone treated me how I deserved to be treated.","scream","angryCl",tears="mascara") 
                m "And how's that?"
                call her_main("Like a slut.","annoyed","worriedL",tears="mascara") 
                call her_main("Boys cat called me.","annoyed","angryL",tears="mascara") 
                call her_main("Put me down.","mad","worriedCl",tears="soft_blink",tears="mascara") 
                call her_main("Snape made me stand out the front of the class During defense against the dark arts.","angry","base",tears="mascara_soft") 
                m "What did he make you do in front of the class?"
                call her_main("Nothing, I just had to stand there for the whole lesson.","upset","worriedCl",tears="mascara_soft_blink") 
                m "Did your friends say anything?"
                call her_main("Nothing.","angry","worried",tears="mascara_soft") 
                call her_main("...","upset","worriedCl",tears="mascara_soft_blink") 
                call her_main("Did I{p}make you happy?","open","annoyed",tears="mascara_soft") 
                m "You did."
                call her_main("Good night, [genie_name].","normal","worriedCl",tears="mascara_soft") 
           
    hide screen sccg 
    show screen blkfade
    with fade
    jump end_hg_pf


label hg_ps_WearMyCum_complete_3:
    if cum_location == 7: #Cleavage
        $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
        $ uni_sperm = True
        ">Hermione returns to your office, her shirt still covered in cum."
        call her_main("...I did it [genie_name].","open","suspicious") 
        call her_main("I kept your cum on me all day.","grin","worriedCl",emote="05") 
        menu:
            "\"Good Work!\"":
                call her_main("Thank you [genie_name], will that be all?","base","base") 
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                $ sc34CG(1, 17, 7)
                call her_main("It was actually quite frustrating [genie_name]...","annoyed","angryL") 
                m "frustrating?"
                call her_main("yes! Having to spend the whole day smelling your delicous cum but not being able to taste any of it!","open","baseL") 
                call her_main("It was like looking at a glass of water in the desert...","soft","ahegao") 
                m "did anyone else notice?"
                call her_main("I couldn't say [genie_name]... I was too distracted by the smell...","angry","wink") 
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","grin","dead") 
    else: #Cum on face
        $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
        $ uni_sperm = True
        ">Hermione returns to your office."
        call her_main("I did it, [genie_name].","open","suspicious") 
        call her_main("I kept your cum on me all day.","base","base") 
        menu:
            "\"Good Work!\"":
                call her_main("Thank you, [genie_name]. Is that everything?","soft","squintL") 
                m "yes [hermione_name], you can go clean up now."
                call her_main("clean up?","open","baseL") 
                m "Only if you want to..."
                call her_main("thank you [genie_name]!","grin","ahegao") 
            "\"Tell me about your day.\"":
                $ sc34CG(1, 17, 6)
                call her_main("My day...","soft","squintL") 
                call her_main("It was a normal day [genie_name]. Well what is normal for me now.","soft","ahegao") 
                call her_main("I got called names again, and some of the boys groped me.","grin","dead") 
                call her_main("Susan Bones even said she liked how I looked in my shirt.","base","down") 
                m "And how did that make you feel?"
                call her_main("Excited, I almost came when Moaning Myrtle started yelling to everyone about your cum on my shirt.","silly","dead") 
                m "Truly?"
                call her_main("Of course, it made me even happier knowing that it makes you happy.","base","down") 
                m "that you did..."
                call her_main("...{image=textheart}","grin","ahegao") 
                call her_main("thank you [genie_name]. well, goodnight.","open","baseL") 
                m "goodnight [hermione_name]."
    hide screen sccg 
    with fade
    jump end_hg_pf

    return
