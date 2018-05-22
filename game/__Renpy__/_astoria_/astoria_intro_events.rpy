#LETTER FROM THE MINISTRY OF MAGIC
#Dear Albus Dubmbledore, as we are sure you are aware,
#an unforgivable curse has been detected within the grounds of Hogwarts.
#While the punishment for such a curse is usually lifetime incarceration in the
#prison, Azkaban, we are allowing you to address this matter at your own discretion.
#This is due to the possible nature of the spell being cast by a minor who has not
#fully grasped the serious nature of the curse. If this is the case we expect no further communication from 
#you regarding this unfortunate event. If, however, you believe the curse has been cast by someone other than a student,
#or if any other complications arise we expect direct communication. Lastly, the detection of any further curses will 
#result in the immediate dispatchment of an auror to Hogwarts.

#Cornelius Fudge, 
#Department Head: Improper Use of Magic Office

#m "That doesn't sound good..."
#m "Perhaps I should tell Snape about this."
#m "Or maybe miss granger?"


#TELL HERMIONE ABOUT THE LETTER
label letter_intro_hermione:
    m "I received a letter not too long ago."
    her "I assume you receive hundreds of letters each day. You're the headmaster of hogwarts after all..."
    m "this one was different."
    m "Apparently they've detected something called an \'unforgivable\' curse at the school."
    her "AN unforgivable CURSE!!!"
    her "SOMEONE COULD BE DEAD!"
    her "OR TORTURED!!"
    her "OR WORSE!!!"
    m "really?"
    her "Those are the only things that can happen with an unforgivable curse [genie_name]!"
    m "of course... I'm just making sure you were aware of them..."
    her "It's the first lesson we ever received in defense against the dark arts."
    m "Well, one's been cast somewhere on the school."
    m "and I need your help finding out who did it..."
    her "Why do you need my help?"
    her "Surely you're able to detect them?"
    m "Unfortunately not... I must have been... asleep... when the thing happened..."
    m "I missed my chance, so to speak..."
    her "So how do you expect me to find out who did it?"
    m "I'm certain that it's the work of another student..."
    m "(or Snape has finally snapped...)"
    m "so I'll need you to go undercover to find out who."
    her "really? You're depending on me to find a criminal student within our school?"
    m "If it's not too much troub-"
    her "I'd be honored [genie_name]!"
    her "It's no doubt the work of one of those despicable \'slytherins\'..."
    her "Nothing would give me greater pleasure than to see scum like that sent to \'Azkaban\'..."
    m "And what's Azkaban?"
    her "...Is this another test sir?"
    m "Sure..."
    her "It's the prison of the damned... An impenetrable rocky outcrop surrounded by the harsh North Sea..."
    her "the guards are the deathly eaters of all happy thoughts and emotions known as dementors..."
    her "They endlessly patrol the prison, devouring all hope from the prisoners, driving them mad within a few days..."
    her "Tormenting them relentlessly for the rest of their miserable lives..."
    her "And the perfect place to house all those dirty \'slytherins\'!"
    m "ah... very good."
    menu:
        "-just tell her to find the student-":
            m "Whatever..."
            m "just find them so we can send them to Akabur..."
            her "Azkaban, sir..."
            m "Just go!"
        "-Tell her you're not going to send them to Azkaban-":
            m "By the gods [hermione_name], what's wrong with you?"
            her "What are you talking about [genie_name]?"
            her "Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse..."
            m "I've been given special permission to punish them as I see fit."
            her "Oh..."
            her "So no Azkaban?"
            m "Not unless they've killed someone..."
            her "Really? So there's still a chance?"
            m "Only if you find a body..."
            her "yay!"
    ">hermione quickly exits your office."
    if astoria_intro_flag_1 == True:
        m "I wonder if she'll find them before Snape..."
    else:
        m "I should probably go tell Snape as well..."

    jump day_main_menu

label letter_intro_snape:
    m "I got some letter from the ministry of magic..."
    sna "Really?"
    sna "Why are you telling me?"
    m "Apparently they've detected something called an \'unforgivable\' curse at the school, and if they detect another one they're going to send an \'auror\' or something."
    sna "oh shit... this isn't good..."
    sna "This really isn't good..."
    m "Why, are the curses that bad?"
    sna "Forget about the damn curses, if they send an auror here they might find out what we've been doing."
    m "What?"
    sna "THe favour trading! Fucking our students isn't something teachers are supposed to do genie!"
    sna "If an auror finds out what's going on here we're both going to Azkaban!"
    m "so what are we going to do?"
    sna "We'll just have to make sure that no more curses are cast..."
    m "How do we manage that?"
    sna "We have to find out who's been casting them."
    sna "Normally the real Dubmbledore would be able to detect who had cast them, but seeing as how you're here instead..."
    sna "We'll have to find them the old fashioned way."
    m "So you want me to launch a manhunt?"
    sna "Are you crazy? We can't let anyone know what's happened. All the students will panic thinking someone's been murdered..."
    sna "It's probably just an imperio or crucio that's been cast."
    sna "I'll start the search immediately. In the mean time you just stay here and keep yourself busy."
    m "You don't want my help?"
    sna "Not really... With how potent your magic is you'll probably just attract more attention from the ministry and then they'll definitely send an auror."
    sna "Don't worry Genie, I'll find that student in no time."
    ">Snape quickly exits your office, his cape billowing menacingly behind him as he leaves."
    m "Drama queen..."

    jump day_main_menu

label astoria_captured_intro:
    #play knock sound effect
    "*knock* *knock* *knock*"
    m "Who is it?"
    her "It's hermione granger, sir, although I'm not alone."
    m "Come in."
    ">hermione enters your office."
    show screen hermione_main
    m "I thought you said you weren't alone?"
    her "I'm not."
    her "Get in here Astoria!"
    ast "No!"
    her "Do you want to make this worse?"
    ast "no..."
    ">Slowly, a small girl enters your office."
    call ast_main("...")
    m "..."
    m "Who's this?"
    call ast_main("My name is Astoria Greengrass, sir.")
    m "And why are you here?"
    her "You asked me to bring you the person who cast the unforgivable curse sir."
    her "Here she is."
    m "I thought it would be some angsty teen who listens to death metal or something..."
    m "not some little girl..."
    call ast_main("I am not a little girl!")
    m "What are you then, a 600 year old vampire?"
    call ast_main("Vampires aren't real!")
    m "..."
    m "So how are you not a little girl then?"
    call ast_main("I'm older than I look!")
    m "I've heard that one before..."
    her "It's true sir. She was a cursed child, born with a frailty that affects her growth."
    call ast_main("Told you!")
    m "Whatever... that still doesn't get you out of punishment."
    call ast_main("punishment? for what?")
    her "You know what you did!"
    call ast_main("I never cast Imperio on anyone! I swear sir! Hermione's just being a know-it-all tattle-tail!")
    m "Miss Granger..."
    her "I overheard her boasting about it to a group of slytherins in the library."
    her "By the sounds of it she used Imperio to control another student."
    call ast_main("Did not!")
    m "Well, given the severity of the situation, I'm sure there's something we can use to get a clear answer out of you..."
    her "Shall I go fetch a vial of veritaserum from professor snape sir?"
    call ast_main("v-veritaserum? Isn't that against the rules?")
    her "Not when you've been casting unforgivable curses you evil little witch!"
    call ast_main("OK... I'll tell you what happened sir...")
    call ast_main("But only if Hermione leaves!")
    her "Not a chance!"
    m "Miss granger..."
    her "professor! I think it's only fair, given that I was the one to catch her!"
    m "We'll talk about your reward later..."
    her "*hmph*"
    her "Fine..."
    her "I'll go back to my room then..."
    her "Goodbye sir..."
    her "Goodbye Astoria..."
    ">Hermione quietly leaves your office."
    m "Right, well now that Hermione's gone, why don't you tell me exactly what-"
    #magic sound effect and screen shake
    call ast_main("IMPERIO!!!")
    m "..."
    m "What was that?"
    call ast_main("I just cast Imperio on you professor! Now you have to do everything I say!")
    m "So you just cast another unforgivable curse?"
    call ast_main("yes... but it should have... why aren't you...")
    m "Ugh..."
    m "I better get Snape up here."
    call ast_main("professor snape? I command you not to!")
    m "yeah, no. I'm bringing him up here because now we're probably going to have to deal with something called an auror coming to the school."
    call ast_main("An auror?!")
    call ast_main("But they'll send me to Azkaban!")
    m "I'm sure they'll be lenient, you're only a child after all."
    call ast_main("I am not!")
    m "ugh... I better get Snape."
    ">you summon snape to your office."
    sna "gen- oh, you've I see you already have a visitor."
    sna "Little young isn't she? even for you..."
    m "It's not that sort of visit."
    sna "Really? Then what's she doing here."
    m "She's the one who's been casting those curses."
    sna "Truthfully? A slytherin?"
    sna "I expect better than this from my students miss Greengrass..."
    sna "The very first lesson I give you is to not. get. caught!"
    sna "Do you have anything to say for yourself?"
    call ast_main("I-I'm sorry sir... It won't happen again.")
    sna "Well as long as you only cast it once..."
    call ast_main("Twice...")
    sna "TWICE!?!"
    sna "But that means..."
    sna "There's probably an auror on the way right now!"
    sna "Who did you cast them on you little idiot?"
    sna "Who did you curse?"
    call ast_main("Well the first time I was just testing it out on Susan Bones...")
    call ast_main("She was being so mean to me so I might have used imperio to embarrass her a little...")
    sna "And the second time?"
    call ast_main("I just tried to use imperio on professor Dumbledore then, so he wouldn't get me in trouble...")
    call ast_main("But it didn't work!")
    sna "Really? It must be because he's a geni-"
    sna "Genius wizard!"
    sna "But this is no good... If they're sending an auror here then they'll want to talk to you... Dumbledore..."
    m "me?"
    sna "I'm afraid so..."
    m "How long until they get here?"
    sna "I'm not sure, but I don't intend to find out!"
    ">Snape quickly turns to leave your office, sprinting out the door."
    m "COWARD!"
    call ast_main("So there really is an auror coming?")
    call ast_main("I've heard that they're all trained by madeye moody...")
    call ast_main("PLEASE SIR!")
    call ast_main("YOU CAN'T LET THEM SEND ME TO Azkaban!")
    call ast_main("I promise I'll be good! I won't cast anymore curses!")
    call ast_main("I'll do Whatever you want!")
    m "Calm down..."
    call ast_main("b-b-but... I don't want to... go to Azkaban...")
    m "I'm not going to let them take you to Azkaban."
    call ast_main("r-r-r-really? even after I tried to control you?")
    m "we'll talk about your punishment later. For now, I think it's better for you to go back to your room."
    call ast_main("A-a-alright... but what about the auror?")
    m "I'll just explain to them that this was all a simple misunderstanding."
    call ast_main("T-thank you sir...")
    m "However I do expect you to come to my office whenever I summon you from now on."
    call ast_main("Why?")
    m "I might have to call you up here to see the auror. Not to mention we still have the matter of your punishment."
    call ast_main("But I thought it was all just a misunderstanding?")
    m "You've committed a very serious offense here young girl. Just because you're not going to Azkaban, doesn't mean you're getting out of punishment."
    call ast_main("Alright sir...")
    m "Good. Now go back to your room until I summon you."
    m "And by the gods stop cursing people!"
    call ast_main("yes sir...")
    ">Astoria turns to leave your office, looking slightly dejected at the prospect of future punishment."
    m "(Gods, I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed on for...)"

    jump day_main_menu

label tonks_intro_event: #occurs a day or two after the last event
    "*knock* *knock* *knock*"
    m "Ugh..."
    m "Who is it?"
    call ton_main("Nymphadora Tonks sir.")
    call ton_main("I've been sent by the ministry of magic.")
    m "Ah yes... come in."
    call ton_main("Thank you sir... I assume you know why I'm here then?")
    m "The curses I'd imagine."
    call ton_main("Yes. As I'm sure you're aware, it's ministry protocol to have an auror investigate every instance of an unforgivable curse being cast.")
    call ton_main("The ministry was willing to ignore one curse given the likelihood that it was just a student playing about...")
    call ton_main("Two curses on the other hand, cannot be ignored.")
    m "I understand..."
    call ton_main("Well, first things first, do you know who it was that cast the spells?")
    m "I do."
    call ton_main("Fantastic, that saves me most of the effort involved with divination and location spells.")
    call ton_main("Secondly, are you aware of what spell was cast?")
    m "(Shit... what was it called again?)"
    menu:
        "\'Imperio\'":
            call ton_main("I thought as much.")
        "\'Imperial\'":
            call ton_main("Do you mean imperio sir?")
            m "Yes of course, forgive me..."
        "\'Imp Pio?\'":
            call ton_main("...")
            call ton_main("This is a serious matter sir, I'd prefer if you kept the jokes to a minimum.")
            m "certainly..."
    call ton_main("Well, I'm not surprised, It usually is Imperio. Most students don't have the guts to cast crucio on another person, let alone Avada Cadavara...")
    call ton_main("And lastly, are you aware who the curse was cast on?")
    m "I am."
    call ton_main("If you wouldn't mind...")
    m "Susan Bones."
    m "(Whoever that is...)"
    call ton_main("Susan Bones!")
    m "Is there something wrong?"
    call ton_main("Of course there's something wrong!")
    call ton_main("Susan's my niece!")
    call ton_main("and you just let her have an unforgivable curse cast on her?")
    call ton_main("Aren't you supposed to protect your students from these sort of things?")
    m "There's only so much I can do-"
    call ton_main("Typical! You're just like the ministry, never willing to take responsibility for your failings.")
    call ton_main("At least bring the son of a bitch who cursed my niece up here so I can escort them to Azkaban.")
    m "Azkaban? I thought that I was being put in charge of their punishment?"
    call ton_main("That was before I found out who it was that had been cursed, Dumbledore!")
    call ton_main("Now they're going to be punished to the full extent of the law.")
    call ton_main("Which means a lifetime sentence in Azkaban!")
    m "..."
    call ton_main("Well are you going to bring them up here or not?")
    m "I really don't think-"
    call ton_main("I don't care if it was Harry {b}fucking{/b} Potter himself that did it, they're going to Azkaban!")
    call ton_main("so... Bring. {size=+2}them. {size=+2}up. {size=+2}here. {size=+2}now!{/size}")
    m "alright..."
    ">You summon Astoria up to your office."
    call ast_main("Hello professor.")
    call ton_main("...")
    call ast_main("Hello mam.")
    call ton_main("H-hello...")
    call ast_main("You wanted to see me sir?")
    m "I'm afraid not, it was actually Miss Tonks here who wanted you brought up here."
    call ast_main("Oh...")
    call ast_main("Is everything alright?")
    call ton_main("You can't be serious Dumbledore...")
    call ton_main("Bring the actual caster up here.")
    m "You're looking at her."
    call ton_main("Honestly?")
    m "Truly."
    call ast_main("Is this about the imperio I cast...")
    call ast_main("I'm really sorry! I promise I won't ever cast it again!")
    call ton_main("Really? It was you that cast the spell?")
    call ton_main("but...")
    call ton_main("but.......")
    call ton_main("But you're so {size=+20}cute!{/size}")
    m "..."
    call ast_main("...")
    call ton_main("It couldn't possibly have been someone like you!")
    call ast_main("I'm sorry miss... it was me...")
    call ton_main("really?")
    call ast_main("please don't send me to Azkaban!")
    call ast_main("I don't want to go where the dementors are!")
    call ton_main("Don't worry, It won't come to that...")
    call ast_main("r-r-r-really?")
    call ton_main("Of course not! THe ministry isn't going to lock away a cute little thing like yourself for life over a little harmless fun.")
    m "..."
    call ton_main("So what did you make susan do anyway? RUn around like a chicken?")
    call ast_main("Not exactly...")
    call ton_main("Well come on then, no need to be secretive here.")
    call ast_main("I might have made her show her boobs to some second years...")
    call ast_main("Just for a second!")
    call ton_main("hahahaha!")
    m "(what's going on here?)"
    call ton_main("Is that all? You probably did Susan some good then, lord knows she needs to loosen up a bit.")
    call ton_main("She always has been very sensitive about her body for some reason.")
    call ast_main("So I'm not going to get in trouble?")
    call ton_main("I didn't say that... You still cast a very serious spell...")
    call ton_main("However, given the circumstances, I'm going to leave your punishment in the hands of professor Dumbledore.")
    m "Me?"
    call ton_main("That's not going to be an issue is it sir?")
    m "Not at all!"
    call ton_main("fantastic. Now as part of standard ministry proceedings, I'm going to be staying at the school a little while longer just to ensure that there is nothing else at play.")
    call ton_main("Ever since the imperio recursion event at Beauxbatons last year they've been on edge over dark wizards and these sort of spells...")
    m "Alright..."
    call ton_main("I assume that I'll be allowed to sleep in the teachers quarters?")
    m "Of course, I'll have a bed made up for you immediately."
    m "(I didn't even realize we had beds here, I've just been sleeping in this chair...)"
    m "(I really need to clean this thing...)"
    m "asd"



label snape_spell_intro: #Snape tells genie that he has adjusted the magic shield
    ">Snape quickly bursts into your office, his cowl flaring around him as he enters."
    sna "I've done it Genie!"
    m "Done what?"
    m "You haven't killed anyone have you?"
    m "I can't bring people back to life Snape! don't expect me to get you out of this one..."
    sna "What? No... I've solved our problem with the ministry!"
    m "oh... really? How?"
    sna "It was rather ingenious honestly. I modified the underage masking spell to include unforgivable curses!"
    m "The underage masking spell? That sounds a little suspect..."
    sna "no, no, It's nothing like that... The magic in this world is closely monitored by the ministry of magic."
    sna "One of the rules that we have to follow is that children under 18 aren't allowed to cast spells on their own."
    sna "For obvious reasons..."
    sna "But here at Hogwarts they have to be able to practice magic to learn..."
    sna "So we set up a masking spell to hide the children casting spells so as to not send false flags to the ministry."
    sna "With that in mind I was able to modify it to include unforgivable curses!"
    m "And that should stop the ministry coming here?"
    sna "So long as they don't get wind of the favour trading that's happening, we shouldn't hear anymore from them!"
    sna "Aren't you impressed Genie?"
    m "I suppose..."
    m "(this means I could get that little Astoria Greengrass to show me some magic...)"
    sna "What? Well what's the most impressive thing you've done with magic then?"
    m "I once changed the world into a desolate Arabian wasteland..."
    sna "..."
    sna "......"
    sna "........."
    sna "Wanna get drunk?"
    m "Do I!"
    ">You and Snape spend the rest of the evening drinking and reminiscing about past conquests..."
    jump day_main_menu


label astoria_susan_intro: #have astoria demonstrate the imperio spell for the first time on Susan
    ">You summon Astoria to your office."
    call ast_main("You wanted to see me sir?")
    m "Yes. I think it's about time we addressed the issue of your punishment."
    call ast_main("oh... I was hoping you'd forgotten about that.")
    m "Afraid not."
    call ast_main("What am I going to have to do then?")
    call ast_main("I won't have to clean the toilets will I?")
    m "Don't worry, it's nothing like that."
    call ast_main("Oh...")
    call ast_main("Then what will it be?")
    m "First things first, I expect you to come to this office whenever I summon you from now on."
    call ast_main("What? Can't we just get this all over with at once?")
    m "Something like an unforgivable curse isn't so easily forgiven miss Greengrass."
    m "You know what the usual punishment is..."
    call ast_main("life in Azkaban...")
    m "That's right... Now unless you want me to send you away, I think you better agree to this arrangement."
    call ast_main("...")
    call ast_main("fine... but you better not be up to anything!")
    m "me? Never..."
    call ast_main("...")
    call ast_main("What's your second request.")
    m "My second, and last request, is that you cast an unforgivable curse."
    call ast_main("{size=+10}What?{/size}")
    call ast_main("But I don't want to go to Azkaban! You heard what that nasty lady said!")
    m "Don't worry, you won't go to Azkaban."
    call ast_main("How can you be so sure? Won't she be able to tell if I cast another one?")
    m "Not anymore, I've made sure that no one will be any the wiser."
    call ast_main("...")
    call ast_main("But why do you want me to cast unforgivable curses?")
    m "Let's just say I'm curious."
    m "(I wanna see someone get mind controlled!)"
    call ast_main("...")
    call ast_main("This isn't a test is it?")
    call ast_main("You're just getting me to cast one so that I really do get sent to Azkaban aren't you?")
    call ast_main("Well I won't do it!")
    m "I think that you're forgetting that I can already send you to Azkaban."
    call ast_main("Oh...")
    call ast_main("But I still don't understand why would you want to see me cast a curse like that?")
    m "(Ugh...)"
    m "Because of you're exceptional skill! Not every can just cast a curse like that!"
    call ast_main("I suppose not... I was pretty angry when I cast it though...")
    call ast_main("I'm not sure if I could do it again...")
    m "Consider this a test then!"
    call ast_main("...")
    call ast_main("Alright...")
    call ast_main("But I better not end up in Azkaban!")
    m "Scout's honor."
    call ast_main("Well who do you want me to cast it on?")
    call ast_main("It didn't work the last time I tried it on you...")
    m "Who did you say you cast it on last time?"
    call ast_main("Susan Bones, sir.")
    m "Let's just try that again, seeing as how we know that worked."
    call ast_main("What? You want me to cast a curse on another student?")
    m "They won't remember that we've done it will they?"
    call ast_main("I suppose not...")
    call ast_main("I just didn't expect you to be OK with us doing something like this...")
    m "Believe me, I've done worse..."
    call ast_main("...")
    call ast_main("Alright... I'll do it.")
    m "Fantastic!"
    call ast_main("...")
    call ast_main("Are you going to summon her?")
    m "I can't."
    call ast_main("Why not?")
    m "Because she hasn't visited my office yet. For some reason I can only summon people I've met before."
    call ast_main("That seems stupid.")
    m "You're telling me!"
    call ast_main("Should I go and get her then?")
    m "If you wouldn't mind."
    call ast_main("OK... what should I say to her?")
    m "About?"
    call ast_main("To get her to come up here!")
    call ast_main("I need to tell her something.")
    m "Just tell her I want to have a word with her."
    call ast_main("Really? Can't it be something a little more fun?")
    m "Fun?"
    call ast_main("You know, something to make her think she's in trouble so she's all scared and nervous when she gets up here.")
    m "You can tell her whatever you want, so long as you get her up here."
    call ast_main("yay!")
    call ast_main("I'll be right back.")
    show screen blkfade
    with d3
    ">Astoria leaves your office, skipping and humming as she goes."
    "..."
    pause
    "......"
    pause
    "........."
    pause
    "............"
    pause
    "*knock* *knock* *knock*"
    m "Come in."
    ">Astoria and Susan slowly enter your office."
    show screen astoria_greengrass
    show screen susan_bones
    g9 "!!!"
    g9 "(LOOK AT THOSE KNOCKERS!)"
    m "and Who is this?!?"
    call sus_main("My name is S-Susan Bones sir...")
    call sus_main("Astoria said you n-needed to see me urgently.")
    m "Yes... need to see... them..."
    call sus_main("...")
    call sus_main("If you don't mind me asking sir... what's this about?")
    m "Oh, um... Did Astoria not tell you?"
    call sus_main("N-no sir...")
    m "Well, Miss Greengrass and I were discussing how best to further the educat-"
    call ast_main("IMPERIO!!!")
    ">A puff of yellow smoke appears in front of Susan's face."
    call sus_main("W-what is thi-")
    ">As quick as it appeared, it seems to fly up Susan's nose, her expression relaxing as it moves."
    call sus_main("...")
    ">Susan's eye's seem to empty as her body relaxes."
    call ast_main("Yay! It worked!")
    m "Fantastic!"
    call ast_main("So what should we do now?")
    call ast_main("Want me to make her dance like a chicken?")
    m "Not exactly..."
    call ast_main("What then?")
    m "Well what did you do to her the first time?"
    call ast_main("...")
    call ast_main("I can't say...")
    call ast_main("It's too embarrassing!")
    m "embarrassing? Now I have to know!"
    call ast_main("OK... but you have to promise that you won't get mad at me!")
    m "Sure."
    call ast_main("...")
    call ast_main("Well a few of the other girls have been talking about...")
    call ast_main("...")
    call ast_main("they were talking about breasts sir!")
    g9 "(JACKPOT!)"
    m "go on..."
    call ast_main("they were talking about how boys only like big ones...")
    call ast_main("and that only the girls with big boobs would get asked to the autumn ball...")
    m "Was Susan one of these girls?"
    call ast_main("No sir. It was just a few of the \'Slytherin\' girls talking in the common room.")
    m "So how did Susan become involved in all this then?"
    call ast_main("It was her own fault!")
    m "..."
    call ast_main("What does she expect to happen when she keeps flaunting those disgusting udders of hers!")
    call ast_main("It's only fair that someone put her in her place!")
    m "And this someone was you?"
    call ast_main("...")
    call ast_main("yes...")
    m "So what did you do?"
    call ast_main("...")
    call ast_main("I might have... made her...")
    call ast_main("I made her walk around without a shirt on...")
    m "What? Really?"
    call ast_main("I'm sorry sir! It was just around the common-room.")
    call ast_main("I was just so angry about her getting all the attention from the boys.")
    call ast_main("So I gave her all the attention she could ever ask for!")
    call ast_main("Although it was only around the girls common-room so it wasn't that big a deal...")
    call ast_main("And it's not like she can remember it anyway...")
    call ast_main("It was just so {b}exciting{/b} to see her taken down a notch...")
    m "and What did the other girls do once you started parading her around?"
    call ast_main("They were all shocked at first...")
    call ast_main("A few of them just told her to stop showing off and put a top on...")
    call ast_main("So I had to make things a little more embarrassing for her...")
    m "How's that?"
    call ast_main("I may have made her do a little dance...")
    m "A dance?"
    call ast_main("Well... it was sort of just making her shake her boobs for them...")
    m "Can you make her do it again?"
    call ast_main("WHAT!")
    call ast_main("professor! I can't do something like that!")
    menu:
        "\"Why not?\"":
            call ast_main("Because... because it's wrong!")
            call ast_main("You're too old!")
            call ast_main("And you're her teacher!")
            m "So what?"
        "\"come on...\"":
            call ast_main("...")
            call ast_main("Is this a joke sir?")
            m "Maybe..."

    call ast_main("You can't expect me to do something like that!")
    call ast_main("Unless...")
    m "Unless?"
    call ast_main("Maybe if you made it worth my while...")
    call ast_main("Maybe I would be OK...")
    call ast_main("With making Susan dance with you...")
    call ast_main("Maybe!")
    m "And what sort of reward would that be?"
    call ast_main("I want points!")
    m "What's your house called?"
    call ast_main("Slytherin! You should know that!")
    m "of course I do... I was just making sure you knew."
    call ast_main("...")
    m "Is that-"
    call ast_main("Not done!")
    call ast_main("I also expect you to teach me some new spells!")
    m "What?"
    call ast_main("All the spells I've been learning in class are so {b}boring!{/b}")
    call ast_main("Those dumb teachers only want us to learn safe spells...")
    call ast_main("that's part of the reason why I cursed Susan in the first place...")
    call ast_main("The unforgivable curses were the first fun spells I learned about!")
    call ast_main("Well maybe not crucio or avada kadavra...")
    call ast_main("But imperio!")
    call ast_main("It's so much fun!!!")
    call ast_main("I wanna learn more spells like this!")
    call ast_main("So I expect you to teach me them, I'm sure you know them all old man.")
    m "(I don't know shit.)"
    m "Alright..."
    call ast_main("yay!")
    call ast_main("Well in that case...")
    call ast_main("Susan, give professor Dumbledore a nice dance...")
    call sus_main("yes...")
    ">Susan start moving her hips slowly to the sides, barely moving."
    call ast_main("That's terrible!")
    call sus_main("oh...")
    call ast_main("Take your top off at least...")
    call ast_main("Don't worry Dumby, I'll make sure you get a good show!")
    m "Dumby?"
    call ast_main("short for Dumbledore!")
    m "oh... right..."
    ">As the two of you talk Susan slowly removes her vest."
    call ast_main("That's it Susy, one piece at a time.")
    m "You seemed to have changed your tone..."
    call ast_main("Because now know this isn't a test.")
    ">Susan quietly removes her tie."
    call ast_main("Before I was certain you were going to expel me as soon as I cast Imperio.")
    call ast_main("but after asking to see Susy's boobs, well...")
    ">Susan peels her stressed shirt off."
    call ast_main("And now I get to learn some cool new spells!")
    call ast_main("They better be cool old man!")
    call ast_main("I don't want something boring like fireworks or something.")
    m "What did you have in mind?"
    call ast_main("Hmmm")
    call ast_main("Something no one else will know!")
    m "so you want secret spells?"
    call ast_main("Yes! And they have to be fun as well! I don't want a secret spell to find a frog!")
    ">Susan slowly moves her arms to unclip her bra..."
    m "ah... sure... whatever you said..."
    call ast_main("Oh...")
    call ast_main("Are you excited to see her boobs old man?")
    m "Yeah... it's not every day you get to see a pair like these..."
    call ast_main("Hmph")
    call ast_main("Typical...")
    m "Shh..."
    call ast_main("...")
    ">Susan unceremoniously removes her bra, letting it fall to the floor."
    m "Incredible..."
    call ast_main("They're gross...")
    call ast_main("Everyone {size=-2}knows {size=-2}that {size=-2}flat {size=-2}boobs {size=-2}are {size=-2}justice...{/size}")
    m "DIdn't you say something about making her dance..."
    call ast_main("Not anymore!")
    call ast_main("I think you've seen enough old man!")
    m "You can't be serious!"
    call ast_main("Put your clothes on, go back to your room and go to sleep Susan!")
    call sus_main("yes...")
    m "Aw, but we were just getting to the best bit!"
    call ast_main("You can save that for next time old man, I think you've had enough fun today.")
    call ast_main("Any more and you're heart will probably give out!")
    call ast_main("In the mean time I want you to think up fun and secret spells!")
    m "Sure..."
    call ast_main("Alright, well don't bring me up here again until you've got them!")
    call ast_main("Good bye professor!")
    m "Good bye child..."
    call ast_main("*hmph*(I'm not a child...)")
    ">Astoria turns heel and exits your office."
    jump day_main_menu


label snape_book_intro: #Have genie ask for a book of sex spells
    m "So to use your magic, you have to say words to cast your spells right?"
    sna "Of course! You don't think we just wiggle our noses do you?"
    m "I suppose not..."
    m "Well do you happen to have any secret spells?"
    sna "Secret spells? What for?"
    m "It's um..."
    m "It's for a student..."
    sna "What? Miss granger? You can forget all about me giving her anything!"
    m "Calm down Severus, it's not Hermione, it's someone else..."
    sna "Oh, you finally got yourself another one did you?"
    m "in a way... I'm still trying to get her to come around."
    m "But in exchange she wants me to teach her secret spells or something."
    m "I've got no idea if that's even a thing with your magic."
    sna "It is..."
    m "really? So you have some secret spells?"
    sna "I do..."
    m "What kind?"
    sna "You may find this hard to believe, but I had a bit of a troubled childhood."
    m "(Shocker...)"
    sna "..."
    sna "Anyway, I sort of turned to spell creation as a way to channel my emotions at the time."
    sna "At the age of nine I invented one of my favorite spells, {b}septum sempra{/b}."
    sna "A curse of such terrible power... Even to this day I still see all the faces of-"
    m "Yeah yeah yeah, do you have anything fun?"
    sna "Ugh, you could of at least let me finish my story."
    m "go on then..."
    sna "As I was saying, I used spells as a way to funnel my frustrations. So when I hit puberty, the spells became a little more..."
    sna "Sexual in nature..."
    m "Really? What did they do."
    sna "It's too embarrassing..."
    m "Come on man! Don't hold out on me."
    sna "I'm not going to stand here and explain them all to you."
    sna "Just take the book."
    ">Snape hands you a pink leather book."
    sna "I've written notes explaining what the spells do as well as how to cast them."
    sna "Keep in mind this sort of magic isn't quite what most students will be used to."
    sna "It's based on a far more primal magic, based off of emotions rather than words."
    sna "It'll take a fair bit of practice before they'll be able to give them a go."
    m "Thanks, even if she can't manage to cast them, the fact you made them should get her off my back."
    sna "Will that be all Genie?"
    m "I guess... Unless you fancy a drink?"
    sna "I thought you'd never ask."
    ">You and Snape sit next to the fire, recounting past conquests and enjoying the platonic company."
    jump day_main_menu
    























label astoria_tonks_intro: #occurs after you get the book from Snape
    "*knock* *Knock* *Thwump*"
    ">Your door is flung open as Tonks enters the room, a worried look covering her face."
    call ton_main("Sir, I have reason to believe that there is in fact a dark wizard operating somewhere on the grounds.")
    m "A dark wizard?"
    m "Surely you meant to say an African American wizard?"
    call ton_main("This isn't the time for your stupid jokes Dumbledore!")
    call ton_main("I've recently detected another instance of an unforgivable curse being cast in my vicinity.")
    call ton_main("But what's really troubling is that the ministry hasn't contacted me...")
    call ton_main("It must mean that the wizard is concealing themselves to the ministries global detection spell.")
    call ton_main("We have to evacuate the school until they're caught... We can't risk the death of a student...")
    m "Oh... I think those spells you were picking up on might have involved me..."
    call ton_main("you can't mean...")
    call ton_main("You're the dark wizard???")
    m "I told you, I don't think you can say that anymore..."
    call ton_main("THIS IS NO LAUGHING MATTER!")
    m "I'm not a \'dark\' wizard! the spells are occurring under my strict supervision."
    call ton_main("You mean you've been letting students cast unforgivable curses? And hiding it from the Ministry?")
    call ton_main("What are you thinking?")
    m "As headmaster of this school, I believe that teaching students is my business, thank you very much."
    call ton_main("Well unforgivable curses are my business Dumbledore!")
    call ton_main("I demand you explain what's going on before I Floo back to the ministry and tell them everything!")
    m "(Shit...)"
    m "Alright fine..."
    m "I've been tutoring a student..."
    call ton_main("In the dark arts? Are you crazy?")
    m "Don't worry, I'm not letting her kill anyone..."
    call ton_main("Her? Who exactly are you tutoring then?")
    m "Astoria Greengrass. I believe you've met."
    call ton_main("Astoria? You mean that cute little l-{p}lady...")
    call ton_main("Why on earth are you teaching her curses?")
    m "Miss Greengrass approached me about wanting to learn some more advanced spells."
    call ton_main("So you decided to teach her how to cast Imperio???")
    call ton_main("And if she's casting imperio under your supervision, then who is the cursee?")
    call ton_main("I don't suppose you'd let her curse you.")
    m "Remember your niece?"
    call ton_main("SUSAN?")
    call ton_main("You cannot be serious!!! {p}What sort of school are you running here?")
    m "A magic one?"
    call ton_main("...")
    call ton_main("What are you and Astoria making Susan do then?")
    m "Oh... um..."
    m "Dancing like a chicken?"
    call ton_main("Really...")
    call ton_main("You honestly expect me to believe that?")
    m "It was worth a shot."
    call ton_main("So let me get this straight...")
    call ton_main("You've been teaching dark arts to a student, concealing your actions from the ministry of magic...")
    call ton_main("And controlling my niece to do who knows what?")
    call ton_main("Do you have any idea how much trouble you're in?")
    m "Is that a rhetorical question?"
    call ton_main("...")
    call ton_main("This probably means that those letters from Miss Granger were actually telling the truth as well.")
    m "What letters?"
    call ton_main("The ministry received a formal complaint from miss granger a few weeks ago about a sexual favour ring at hogwarts.")
    call ton_main("Obviously the ministry ignored the matter. I mean who could believe that the famous Albus Dumbledore would let something like that happen...")
    call ton_main("But now I'm not so sure...")
    m "..."
    call ton_main("So is it true then?")
    call ton_main("Are you fucking your students Dumbledore?")
    call ton_main("Or are you just covering up for the other teachers here?")
    menu:
        "-lie-":
            m "I'd never allow-"
        "-tell the truth-":
            m "It all started-"
    call ton_main("I don't care, either way you're going to Azkaban for the rest of your life...")
    m "*gulp*"
    call ton_main("Unless...")
    m "Unless what?"
    call ton_main("Do you have an opening for a defense against the dark arts professor?")
    m "..."
    m "......"
    m "........."
    m "............"
    m "What?"
    call ton_main("Ugh... You can't think I like being an auror do you?")
    call ton_main("It's just constant busy work...")
    call ton_main("Not to mention the hours.")
    call ton_main("And the mortality rate...")
    call ton_main("If I'd realised the benefits of being a teacher at hogwarts I would have signed up straight away!")
    m "benefits?"
    m "You mean the favour trading?"
    call ton_main("no, I mean the health care... Of course I mean the favour trading Dumbledore!")
    call ton_main("I always assumed that you and Snape wouldn't allow holding hands in the corridors...")
    call ton_main("But if you're playing around with your students...")
    call ton_main("Well let's just say I want in.")
    m "Done!"
    m "Consider yourself the new defense of the ancients teacher or whatever..."
    call ton_main("What about Quirrel?")
    m "Who?"
    call ton_main("The current defense against the dark arts professor...")
    m "Oh yeah... I'll get snape to deal with him..."
    call ton_main("So snape is in on this too?")
    m "Yeah..."
    call ton_main("Huh... I didn't think that sad sack even knew what fun was...")
    call ton_main("So what's the going rate around here then?")
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?")
    m "Again, it depends on the student."
    call ton_main("...")
    m "But if I had to guess, I'd say about 25 points."
    call ton_main("Wait...")
    call ton_main("You pay them in points?")
    m "Most of them."
    call ton_main("So you've managed to convince these girls to offer themselves up for a bunch of imaginary points that don't mean anything?")
    m "Works for the internet..."
    call ton_main("what?")
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("how so?")
    m "Well most of them aren't going to just do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("Awww really... Can't I just use cheats?")
    m "..."
    m "Just take it slow alright, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("And what if I want a girl?")
    m "Whatever floats your boat."
    call ton_main("Well what if I want a specific girl?")
    m "Who?"
    call ton_main("Astoria Greengrass.")
    m "Astoria? Isn't she a little-"
    call ton_main("She's perfect! She's just so cute and innocent... I want to gobble her up!")
    call ton_main("mmm...")
    m "I'm not sure if she'd be up for that to be honest-"
    call ton_main("Well you better make her up for it then...")
    call ton_main("Unless I need to tell the ministry about all this...")
    m "Fine..."
    call ton_main("Good... I expect her to pay me a little visit tonight.")
    m "..."
    call ton_main("Now if that's all I'll be off.")
    m "Sure..."
    ">Tonks turns and leaves your office."
    m "..."
    m "Did I just become a pimp?"

    jump day_main_menu
    







label astoria_book_intro: #Summon Astoria and tell her that you have a book of spells as well as the pimping with Tonks
    #Summon Astoria to your office
    #Tell her you have a book of new spells for her
    #She's very excited, says she can't wait to learn them all
    #Tell her that as payment for her learning these new spells, she'll have to do something for Genie
    #Explain that she will have to go see Tonks now
    #Astoria shocked, upset that she has to go see the Auror, scared about Azkaban
    #Genie tells her not to worry, that she will come back to his office afterwards just to make sure she's alright
    #She reluctantly agrees
    

























































