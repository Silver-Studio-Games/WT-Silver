

label hg_pf_TimeForAnal: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TimeForAnal_OBJ.points == 0:
        m "{size=-4}(Should I ask her to have anal sex with me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_ballDress_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("In what?","open","worriedL") 
                m "Your ball dress."
                if whoring >= 22:
                    call her_main("What?","scream","wide") 
                    her "You got me a new ball dress?"
                    m "Indeed I did, but you'll have to earn it."
                    call her_main("Of course!","angry","wide") 
                    call her_main("Let me go try it on!","base","baseL",cheeks="blush") 
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_ballDress_OBJ) 
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"
    
    #Intro
    if hg_pf_TimeForAnal_OBJ.points == 0:
        m "[hermione_name]..."
        call her_main("[genie_name]..?","annoyed","suspicious") 
        m "How familiar you are with the term \"Anal Sex\"?"

        if whoring < 21:
            jump too_much

        call her_main("90 house points...","annoyed","annoyed") 
        m "What?"
        call her_main(".............................","disgust","glance") 
        m "Well alright then. 90 house points it is."
        hide screen hermione_main  
        
        label lucky_guess:
        
        call blkfade 
        stop music fadeout 1.0
        
        call her_head("...........","annoyed","worriedL") 
        m "Let's see..."
        call her_head(".................","angry","worriedCl",emote="05") 
        m "Hm..."
        call her_head("!!!","angry","wide") 
        g4 "Oh, come on!"
        call her_head("Ouch!","mad","worriedCl",tears="soft_blink") 
        m "Just try to loosen up a little, would you?"
        call her_head("I'm trying!","angry","base",tears="soft") 
        m "Ok, what if I do this..?"
        call her_head("Ouch! What are you doing, [genie_name]?","mad","worriedCl",tears="soft_blink") 
        m "Yeah, this won't work either..."
        m "Hm..."
        m "Alright, I think I know what we should do."
        
        menu:
            m "..."
            "\"I think I'll spit on it and just force it in!\"":
                call play_music("playful_tension") # SEX THEME.
                call her_head("Force it in, [genie_name]?!","angry","wide") 
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g4 "*SPIT!*"
                call her_head("Eeeeeew!","scream","worriedCl") 
                call her_head("No, [genie_name], wait! Maybe if I just relax--","open","base") 
                m "No need, here I come!"
                with hpunch
                call her_head("ARGH!","angry","base",tears="soft") 
                call her_head("Ouch! Ouch! Ouch!","mad","worriedCl",tears="soft_blink") 
                g4 "Almost in!"
                call her_head("No, you're hurting me! You are hurting me!","scream","worriedCl") 
                g4 "Almost! Almost!"
                call her_head("Ah! It hurts!","scream","worriedCl") 
                g4 "Shut it, [hermione_name]! I'm doing you a favour!"
                g4 "Your anus is so tight it's completely un-fuckable!"
                call her_head("Then stop, please!","mad","worriedCl",tears="soft_blink") 
                m "No! We need to loosen up your asshole a little!"
                call her_head("But I don't want you to!","mad","worriedCl",tears="soft_blink") 
                m "Really? How do you expect people to fuck you up your ass then?"
                call her_head("What people?","shock","worriedCl") 
                g4 "You know... people."
                g4 "Argh, dammit... My dick is hurting too now."
                call her_head("Stop then! Stop, [genie_name]!","open","worriedCl") 
                call her_head("I've changed my mind! I don't need 90 points!") 
                g4 "I think I'm almost..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide") 
                g4 "YES!!!"
                call her_head("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!","scream","wide") 
                g4 "Let us pump this little asshole full of semen then, shall we?"
                call her_head("Yes... Please, I just want this to end...","scream","worriedCl",cheeks="blush",tears="crying") 
                
                
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left
                
                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u
                
                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft") 
                    show screen ccg
                    
                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc 
                
                
                #SCHUSH!
                g4 "Agh... You want this to end sooner?"
                g4 "Help me out then!"
                call her_head("*sob!* How?","shock","baseL",cheeks="blush",tears="soft") 
                g4 "You know..."
                call her_head("Oh...","shock","baseL",cheeks="blush",tears="soft") 
                #$ ccg2 = 6
                call her_head("I am a whore??","clench","worried",cheeks="blush",tears="soft") 
                g9 "Yes you are!"
                call her_head("*Sob!* I am a whore...","angry","suspicious",cheeks="blush") 
                call her_head("I love to suck cock...") 
                call her_head("And now my tiny asshole is getting ripped to pieces... *Sob!*","angry","dead",cheeks="blush",tears="crying") 
                g4 "Yes! Yes!"
                g4 "Agrh! Yes!"
                call her_head("No! Is it getting bigger?! I'm scared!","open","surprised",cheeks="blush",tears="messy") 
                g4 "ARGH!"
                
            "\"Suck me off first. Lubricate my cock!\"":
                call her_head("Oh... Alright...","open","base") 
                call play_music("playful_tension") # SEX THEME.
                
                #SUCKING
                call her_chibi("hide") 
                hide screen genie
                show screen chair_left
                
                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u
                
                hide screen blktone
                hide screen bld1
                call hide_blkfade 
                call ctc 
                
                call her_head("*Slurp!* *Slurp!* *Slurp!*") 
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Alright, I think that's enough. Back on the desk now."
                call blkfade 
                
                #ON THE DESK
                call her_head(".............","open","base") 
                g4 "Yes! Almost!"
                call her_head("Ouch!","scream","worriedCl") 
                m "Relax. Almost in."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide") 
                g4 "YES!!!"
                call her_head("My... my...","scream","wide") 
                call her_head("It hurts!","shock","worriedCl") 
                g4 "Let's pump this little asshole full of semen then, shall we?"
                call her_head(".....................","angry","suspicious",cheeks="blush") 
                
                # SEX 
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left
                
                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u
                
                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft") 
                    show screen ccg
                    
                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc 
                
                call her_head(".....................","shock","baseL",cheeks="blush",tears="soft") 
                m "You alright there, slut?"
                call her_head("Ah... You are... stretching me out from the inside... [genie_name].","clench","worried",cheeks="blush",tears="soft") 
                call her_head("And it still hurts...","angry","suspicious",cheeks="blush") 
                m "Hm..."
                m "Maybe not enough lubrication...?"
                m "Come on down, [hermione_name]. Suck my dick some more."
                call her_head("What? But...","clench","worried",cheeks="blush",tears="soft") 
                call her_head("But it's dirty... It's been inside already.","shock","baseL",cheeks="blush",tears="soft") 
                m "Yes, it's been inside, but that doesn't mean it's dirty now."
                m "Come on, [hermione_name]. Suck my cock some more."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft") 
                call blkfade 
                
                #SUCKING
                hide screen ccg
                $ face_on_cg = False
                hide screen hermione_face
                call h_update_hair 
                call her_chibi("hide") 
                hide screen genie
                show screen chair_left
                
                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u
                
                hide screen blktone
                hide screen bld1
                call hide_blkfade 
                call ctc 
                
                call her_head("*Slurp!* *Slurp!* *Slurp!*",xpos="base",ypos="base") 
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Can you taste your ass on my dick?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Alright, Maybe that's enough."
                call blkfade 
                
                # SEX 
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left
                
                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u
                
                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft") 
                    show screen ccg
                    
                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc 
                
                call her_head("Ah...","shock","baseL",cheeks="blush",tears="soft") 
                m "Better now?"
                call her_head("It still hurts...","clench","worried",cheeks="blush",tears="soft") 
                call her_head("But I think I will be fine...") 
                m "I'll take it slow for now..."
                call her_head("Ah... thank you, [genie_name].","angry","suspicious",cheeks="blush") 
                m "Oh... yes... this feels great..."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft") 
                m "Oh... So tight..."
                call her_head("................","shock","down_raised",cheeks="blush",tears="crying") 
                m "Why are you being so quiet [hermione_name]?"
                call her_head("Because this is painful...","clench","worried",cheeks="blush",tears="soft") 
                call her_head("And I just want you to cum sooner, [genie_name]...") 
                m "So you stifle your cries of pain?"
                call her_head("yes [genie_name]. *Sob!*","angry","dead",cheeks="blush",tears="crying") 
                m "Don't do that."
                m "Sob, scream and cry as much as you wish!"
                call her_head("B-but--","clench","worried",cheeks="blush",tears="soft") 
                m "That will make me cum sooner."
                call her_head("Really? *Sob!*","angry","dead",cheeks="blush",tears="crying") 
                call her_head("*Sob!* It hurts! *Sob!* It hurts so much! *Sob!*","shock","baseL",cheeks="blush",tears="soft") 
                m "Yes, yes..."
                call her_head("*SOB!*","angry","suspicious",cheeks="blush",tears="messy") 
                m "You poor little kid..."
                m "A Big, evil man is raping your asshole!"
                call her_head("*SOB!* Yeees! *SOB!*","scream","suspicious",cheeks="blush",tears="messy") 
                g4 "Argh!"
                call her_head("No, I'm scared! *SOB!*","scream","worriedCl",cheeks="blush",tears="messy") 
                
        menu:
            "-Fill Hermione up with cum-":
                g4 "Argh!"
                call her_head("No! AH!","scream","wide") 
                call cum_block 
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                
                $ g_c_u_pic = "sex_cum_in_ani"
                hide screen bld1
                with d3
                
                call cum_block 
                call ctc 
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                
                call her_head("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}","open","surprised",cheeks="blush",tears="messy") 
                g4 "Yes, you whore! Yes!"
                call her_head("It hurts, it hurts!","angry","suspicious",cheeks="blush",tears="messy") 
                g4 "Shut up!"
                with hpunch
                call her_head("No, I am already full! Stop cumming, you bastard!","scream","surprised",cheeks="blush",tears="messy") 
                g4 "Shut the fuck up, slut! I am not done yet!"
                call her_head("No! Please! My stomach! I will explode!","scream","suspicious",cheeks="blush",tears="messy") 
                g4 "ARGH!"
                call her_head("No, I think I will throw up...","open","surprised",cheeks="blush",tears="messy") 
                with hpunch
                play sound "sounds/burp.mp3"
                call her_head("{size=+7}*BURP!*!!!!!{/size}","full","surprised",tears="messy") 
                call her_head(".......................","full","base",tears="messy") 
                call her_head(".............") 
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_head("{size=+7}*GULP!*{/size}","cum","worriedCl") 
                call her_head("*SOB!* I HATE YOU...","angry","suspicious",cheeks="blush",tears="messy") 
                call her_head("{size=+5}I HATE YOU AND YOUR NASTY OLD COCK?{/size}","scream","angry",cheeks="blush",tears="messy") 
                call her_head("{size=+5}I HATE YOU! YOU HEAR ME?!{/size}") 
                g4 "Agh...Shut it, whore!"
                call her_head("*sob!* *Sob!*...","angry","suspicious",cheeks="blush",tears="messy") 
                
                # AFTER CUM INSIDE
                hide screen bld1
                with d3
                call ctc 
                
                $ g_c_u_pic = "ani_her_sex_cum_inside_blink"
                
                call her_head("*Sob!*...","angry","dead",cheeks="blush",tears="crying") 
                m "Whew!... I think that was the last of it."
                m "You alright?"
                call her_head("Yes... *Sob!*","angry","dead",cheeks="blush",tears="crying") 
                m "Are You crying?"
                call her_head("My butt hurts, but I am alright, [genie_name]...","angry","dead",cheeks="blush",tears="crying") 
                m "Well, you took my dick stoically, I must say..."
                call her_head("Thank you [genie_name]...","angry","dead",cheeks="blush",tears="crying") 
                hide screen bld1
                with d3
                call ctc 
                
                call blkfade 
                $ face_on_cg = False
                hide screen hermione_face
                call h_update 
                call h_update_hair 
                
                call her_head("I apologize for saying that I hate you, [genie_name]...","base","baseL",cheeks="blush",tears="mascara",xpos="base",ypos="base") 
                call her_head("And your cock is not nasty...",cheeks="blush",tears="mascara") 
                call her_head("I don't know what's gotten into me...","grin","concerned",cheeks="blush",tears="mascara") 
                g9 "My dick!"
                call her_head("I suppose it's as when you call me a \"whore\". I know you actually don't mean it...","grin","concerned",cheeks="blush",tears="mascara") 
                m "Yeah, sure..."
                m "Does it still hurt?"
                call her_head("A little...","open","concerned",cheeks="blush",tears="mascara") 
                call her_head("I also feel full and warm inside...","grin","closed",cheeks="blush",tears="mascara") 
                m "You plan to keep it in? My cum I mean."
                call her_head("Yes...","grin","glance",cheeks="blush",tears="mascara") 
                
                if daytime:
                    call her_head("I hope it won't start leaking during my classes...",cheeks="blush",tears="mascara") 
                else:
                    call her_head("I hope it won't start leaking before I get to my room...",cheeks="blush",tears="mascara") 
                    
                m "Well, good luck on your journey."
                call her_head("Can I get paid now please?","grin","closed",cheeks="blush",tears="mascara") 
                
            "-Pull out and cum on Hermione-":
                $ g_c_u_pic = "sex_cum_out_ani"
                hide screen bld1
                with d3
                
                call cum_block 
                call ctc 
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") 
                g4 "Yes!!! Allover your ass!"
                call her_head("Ah... It's so hot!","silly","ahegao") 
                hide screen bld1
                with d3
                call ctc 
                
                call blkfade 
                
                call blkfade 
                $ face_on_cg = False
                hide screen hermione_face
                call h_update 
                call h_update_hair 
                
                m "Well, I'm done... You can get off my desk now."
                call her_head("Yes, [genie_name]...","silly","worried",cheeks="blush",tears="soft",xpos="base",ypos="base") 
                m "You feeling alright?"
                call her_head("Yes, [genie_name]. It still hurts a little, but...","shock","baseL",cheeks="blush",tears="soft") 
                m "But what?"
                call her_head("But in a good way... [genie_name].","silly","worried",cheeks="blush",tears="soft") 
                m "In a good way, huh?"
                g9 "Heh... You cute, little mynx."
                call her_head("Can I get paid now, [genie_name]?","silly","worried",cheeks="blush",tears="soft") 
    
    #Second time event.
    elif hg_pf_TimeForAnal_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","soft","base") 
        m "I will be buying another favour from you today..."
        call her_main(".............","open","suspicious") 
        m "Care to guess what the favour will be?"
        m "You have three attempts to find out."
        call her_main("...........","annoyed","frown") 
        call her_main("Anal sex?","disgust","glance") 
        g4 "Wha..........?!"
        g4 "How did you...?"
        call her_main("Just a lucky guess, [genie_name]...","angry","angry") 
        m "Sometimes you scare me, [hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3 
        jump lucky_guess
    
    #Third time event.
    elif hg_pf_TimeForAnal_OBJ.points >= 2:
        m "How about another assfuck, [hermione_name]?"
        call her_main("Of course, [genie_name].","base","ahegao_raised") 
        g9 "Come here, you little mynx!"
        
        hide screen hermione_main     
        call blkfade 
        
        stop music fadeout 1.0
        
        call her_head("........","annoyed","worriedL") 
        m "Hm..."
        call her_head("...........","open","base") 
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide") 
        g4 "Oh, ye-es!"
        call her_head("Ah...","soft","ahegao") 
        m "It seems like your butthole became a bit more welcoming, [hermione_name]."
        call her_head("Ah... It still hurts a little.","base","glance") 
        call her_head("And please, just call me \"whore\", [genie_name].","base","suspicious") 
        g4 "Agh! You slut! You always get me with your words!"
        
        call her_chibi("hide") 
        hide screen genie
        show screen chair_left
        
        $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen g_c_u
        
        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","closed") 
            show screen ccg
                    
        hide screen blktone
        hide screen bld1
        call hide_blkfade 
        call ctc 
        
        call play_music("playful_tension") # SEX THEME.
        
        #INSERTION
        call her_head("Ah... Ah...","open","closed") 
        call her_head("Ah...") 
        call her_head("[genie_name]?","base","glance") 
        m "Yes, whore?"
        call her_head("Em...","angry","base") 
        call her_head("Would you marry me, [genie_name]?","angry","down_raised") 
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me you're pregnant, [hermione_name]!"
        call her_head("I couldn't get pregnant the way we are doing it, [genie_name]...","angry","wink") 
        m "What is this talk of marriage then?"
        call her_head("You misunderstood me [genie_name].","angry","base") 
        call her_head("I meant to say, would you marry a girl {size=+5}like{/size} me?","angry","down_raised") 
        call her_head("I would never propose to a man with his cock in my ass, [genie_name]...","angry","worriedCl",emote="05") 
        m "Good. Because I don't think any man would be able to say \"no\" to then."
        call her_head("Ah{image=textheart}...","open","closed") 
        call her_head("What I meant... ah{image=textheart} {w} ...to say was ah{image=textheart}... {w}...do you think someone would ever ah{image=textheart}... {w} ...want to marry a girl like me?","angry","down_raised") 
        m "Huh?"
        call her_head("I mean, with all that was happening lately... ah{image=textheart}...","angry","down_raised") 
        call her_head("I can't help but feel unclean... damaged even.") 
        call her_head("And in a no way innocent...") 
        call her_head("Who would want a wife like that?","angry","base") 
        
        menu:
            m "..."
            "\"I would marry you in a heartbeat!\"":
                call her_head("What?","open","base") 
                m "Well, hypothetically speaking of course..."
                call her_head("...of course...{image=textheart}","base","baseL") 
                call her_head("..............","base","squint") 
                call her_head("But why do you say that, [genie_name]?","soft","base") 
                m "Huh?"
                m "What do you mean \"why\", whore?"
                m "You are young and attractive..."
                m "Tight asshole, full tits and wet little pussy..."
                call her_head("Ah...{image=textheart}","open","closed") 
                m "You will make some lucky guy a very happy man one day, whore."
                m "Ehm, I mean, [hermione_name]."
                call her_head("No, \"whore\" is good. Call me that, [genie_name].","silly","ahegao") 
                m "There, you see? You are a great catch, I'm telling you, whore."
                call her_head("Ah...{image=textheart} Thank you, [genie_name].","angry","dead",cheeks="blush",tears="crying") 
                m "Huh?"
                m "Are you crying?"
                label among_other_things:
                call her_head("Among other things, [genie_name]...{image=textheart}{image=textheart}{image=textheart}","silly","dead") 
                m "Among other things?"
                call her_head("I'm cumming [genie_name]...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao") 
                g4 "Agh! My cock!" 
                g4 "Relax your muscles a little, would you?"
                call her_head("BUT I'M CUMMING!{image=textheart}{image=textheart}{image=textheart}","open","worriedCl") 
                g4 "Fine! Have it your way whore!"
                with hpunch
                call her_head("{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}","scream","wide") 
                g4 "{size=+7}Argh!{/size}"
                
            "\"Marriage is out of the picture for you.\"":
                call her_head("That's what I thought...","shock","down_raised",cheeks="blush",tears="crying") 
                m "Oh... I just love that little asshole of yours!"
                call her_head(".....................","angry","dead",cheeks="blush",tears="crying") 
                call her_head("Yes... After all the things I had to do for my house...") 
                call her_head("...no one will ever want me...","angry","suspicious",cheeks="blush",tears="messy") 
                m "Oh, they will want you alright!"
                call her_head("What? But you said...","open","surprised",cheeks="blush",tears="messy") 
                m "Marriage, [hermione_name]. Marriage is impossible for you."
                m "But as a man-pleaser you are a great catch!"
                call her_head("Really?","open","surprised",cheeks="blush",tears="messy") 
                m "Are you kidding me?!"
                m "Young, hot and slutty. You could have any man you want!"
                m "Or a wizard or whatever you are into..."
                call her_head("I think you may be right, [genie_name].","base","concerned",cheeks="blush",tears="soft") 
                m "I know I am right, whore."
                m "Now wiggle that little ass of yours a little."
                call her_head("Like this?","silly","worried",cheeks="blush",tears="soft") 
                m  "Yes, that's a good whore."
                call her_head("I am a whore, aren't I?","silly","dead") 
                m "You just sold me your asshole for 90 house points. How would you call that?"
                call her_head("Yes, yes...{image=textheart} I am a whore...{image=textheart}","silly","worried",cheeks="blush",tears="soft") 
                m "Are you crying?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "-Fill Hermione up with cum-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_in_ani"
                
                call cum_block 
                call ctc 
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                
                call her_head("!!!","scream","wide") 
                m "Yes! Argh!"
                call her_head("Ah!{image=textheart} It's filling me up!{image=textheart} I can feel it!{image=textheart}","silly","ahegao") 
                m "Shut up, whore!"
                call her_head("Ah! I AM A WHORE!!!!{image=textheart}{image=textheart}{image=textheart}","scream","worriedCl",cheeks="blush",tears="crying") 
                m "Agh!"
                call her_head("Ah...{image=textheart} your cum, [genie_name]...{image=textheart}","open","surprised",cheeks="blush",tears="messy") 
                m "Yes, yes..."
                call her_head("Ah...{image=textheart}","angry","suspicious",cheeks="blush",tears="messy") 
                m "......"
                hide screen bld1
                with d3
                call ctc 
                
                call blkfade 
                
            "-Cum all over Hermione-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_ani"
                
                call cum_block 
                call ctc 
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                
                call her_head("Ah-aha! You're cumming! {image=textheart}{image=textheart}{image=textheart}","silly","dead") 
                g4 "{size=+7}Yes I do, whore!{/size}"
                call her_head("Ah, me too! Me too!","scream","worriedCl",cheeks="blush",tears="messy") 
                g4 "{size=+7}FUCKING SLUT!{/size}"
                call her_head("Ah...{image=textheart} your cum...{image=textheart}","angry","dead",cheeks="blush",tears="crying") 
                call her_head("I'm so full...{image=textheart}{image=textheart}{image=textheart}") 
                g4 "Yes!!! All over your ass!"
                call her_head("Ah... It's so hot!","silly","ahegao") 
                hide screen bld1
                with d3
                call ctc 
                
                call blkfade 
                
        #Ending
        $ face_on_cg = False
        call h_update_hair 
        
        m "Well, this was intense..."
        call her_head("Ah-ha...{image=textheart} ah...{image=textheart}","grin","dead",cheeks="blush",tears="messy",xpos="base",ypos="base") 
        m "Are You alright, [hermione_name]?"
        call her_head("I think so... I'm not sure...","grin","dead",cheeks="blush",tears="messy") 
        call her_head("I think I may still be cumming, [genie_name].","grin","dead",cheeks="blush",tears="messy") 
        call her_head("Or maybe not...","grin","dead",cheeks="blush",tears="messy") 
        call her_head("Everything is in a daze... and my legs feel so weak...") 
        if whoring < 24:
            her "Can I just get paid now, [genie_name]?"
        stop music fadeout 1.0
   
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    hide screen ccg
    if not daytime:
        show screen candlefire
        
    call her_chibi("stand","desk","base") 
    show screen genie
    call hide_blkfade 
    
    if whoring < 24:
        m "Yes, [hermione_name]. 90 points to \"Gryffindor\"." 
        $ gryffindor +=90
        
    call her_main("Thank you, [genie_name]...","angry","suspicious",cheeks="blush",xpos="right",ypos="base") 
    
    if whoring < 24: #Adds points till 24.
        $ whoring +=1

    if hg_pf_TimeForAnal_OBJ.points == 0:
        $ new_request_31_heart = 1
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_TimeForAnal_OBJ.points == 1:
        $ new_request_31_heart = 2
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_TimeForAnal_OBJ.points >= 2:
        $ new_request_31_heart = 3
        $ hg_pf_TimeForAnal_OBJ.hearts_level = 3 #Event hearts level (0-3)
    
    $ hg_pf_TimeForAnal_OBJ.points += 1
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.

    $ custom_outfit_old = temp_outfit

    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
    





