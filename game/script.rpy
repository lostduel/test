# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define pov = Character("[povname]")
define heshe = ["she","he"]
define hisher = ["her","his"]
define himher = ["her","him"]
define fb= "images/char/female/body/"
define fc= "images/char/female/clothes/"
define fh= "images/char/female/hair/"
define mb= "images/char/male/body/"
define mc= "images/char/male/clothes/"
define mh= "images/char/male/hair/"


# The game starts here.


label start:

    # Show a background. This uses a placuholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene blk

    #$ ac = generatecharacter()

    #define b = Character("allen",image ="allen.jpg")
    #define a = Character("[ac[0]]",image="[ac[1]]")
    #b "123"


    "Greetings! Welcome to the game."
    "As you already know, this game is an interactive fiction, and I hope you can learn something after playing this game."
    "Now first, please enter your name:"
    python:
        povname = renpy.input("What's your name? (your name will not be uploaded)",length=20)
        povname = povname.strip()

        if not povname:
             povname = "Player"


    "Hello, [povname]!"
    "This fiction is constructed by four different units. Each of them has multiple choice questions that you can choose from."
    "Please be careful, your choices matter: different choices will lead to various endings for this game."


    call firststory from _call_firststory

    scene blk with dissolve

    call secondstory from _call_secondstory

    scene blk with dissolve

    call thirdstory from _call_thirdstory

    scene blk with dissolve

    call fourthstory from _call_fourthstory

    return

label firststory:
    #language
    "Chapter one"
    python:
        chars=generatechar(4)
        ex= [[] for i in range(4)]
        for i in range(4):
            ex[i] = generatecharimage(chars[i])
    image a1 = Composite(
        (300, 175),
        (-1240, -1754), "[ex[0][3]]",
        (-1240, -1754), "[ex[0][0]]",
        (-1240, -1754), "[ex[0][1]]",
        (-1240, -1754), "[ex[0][2]]")
    image b1 = Composite(
        (300, 175),
        (-1240, -1754), "[ex[1][3]]",
        (-1240, -1754), "[ex[1][0]]",
        (-1240, -1754), "[ex[1][1]]",
        (-1240, -1754), "[ex[1][2]]")
    image c1 = Composite(
        (300, 175),
        (-1240, -1754), "[ex[2][3]]",
        (-1240, -1754), "[ex[2][0]]",
        (-1240, -1754), "[ex[2][1]]",
        (-1240, -1754), "[ex[2][2]]")
    image d1 = Composite(
        (300, 175),
        (-1240, -1754), "[ex[3][3]]",
        (-1240, -1754), "[ex[3][0]]",
        (-1240, -1754), "[ex[3][1]]",
        (-1240, -1754), "[ex[3][2]]")





    define a = Character("[chars[0][5]]")
    define b = Character("[chars[1][5]]")
    define c = Character("[chars[2][5]]")
    define d = Character("[chars[3][5]]")
    define abc = Character("[chars[0][5]]&[chars[1][5]]&[chars[2][5]]")
    define t = Character("Teacher")

    label refirststory:

    scene mcr

    "You are a high school student."

    "One day, during the break, you are sitting in your seat, looking at your mobile phone, and gradually being attracted to the noise of a group of people talking next to you... "

    show a1 at center,shaking:
        xzoom -0.4 yzoom 0.4
        xpos 400



    a "Hahaha I think it's great! "

    show b1 at center,shaking:
        xzoom 0.4 yzoom 0.4
        xpos 1000



    b "I agree hahaha..  "



    "Although they are too loud, you choose to remain in the classroom as the class is going to start shortly. "

    "At this point, you hear them mention [d]'s name. "

    "[d] is a student in your class whom you don't know very well. However, you still have vivid memory of [chars[3][4]] because [chars[3][2]] has a birthmark on [chars[3][3]] face."

    show c1 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400


    abc "{size=-10}...tease...take...homework...{/size}"

    "You seem to hear something, again."

    show a1 at shaking
    show b1 at shaking
    show c1 at shaking

    abc "Hahahahaha..."

    "Their laughter is somewhat gloating."

    show d1 at center,left with dissolve:
        xzoom -0.4 yzoom 0.4
        linear 3  xoffset 3000

    show a1:
        linear 2  xoffset 0
        xzoom 0.4
        linear 2  xoffset -3000
    show b1:
        linear 2  xoffset 0
        linear 2  xoffset -3000
    show c1:
        linear 2  xoffset 0
        linear 2  xoffset -3000

    "A while later, [d] returns to the classroom. At the same time, you see the three people immediately return to their seats, while making eye contacts with each other."
    $ renpy.pause(3.0, hard=True)
    hide a1
    hide b1
    hide c1
    hide d1

    menu:
        "Remind [d].":
            "You feel something is wrong, but fortunately you have [d]'s number. You decide to text [chars[3][4]]."

            pov "{image=phone.png}\"Hey dude, I just heard that some people talking something about your homework. \""

            show d1 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1000
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"Huh? What do they want to do? \""

            pov "{image=phone.png}\"I'm not really sure, but you should be careful anyway.\""
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"Oh, Ok, thanks.\""

            hide d1 with dissolve

            "After class, you are relieved to see [chars[3][4]] leave the classroom with [chars[3][3]] homework in [chars[3][3]] hands. "



            scene mct with dissolve

            "It's lunch time. You feel happy because you helped a classmate."

            "..."



            scene mcr with dissolve

            show d1 at center:
                xpos 1000
                xzoom 0.4 yzoom 0.4
                linear 0.5
                xzoom -0.4
                linear 0.5
                repeat


            "However, when you return to the classroom, you find [d] anxiously rummaging through [chars[3][3]] bag. "

            "You walk over."

            pov "What happened?"

            show d1 at center,shaking:
                xpos 1000
                xzoom 0.4 yzoom 0.4

            d " I can't find my wallet. I put it in my bag and it was gone when I came back from lunch. "

            pov "..."

            "You think it's the same group of people, that tried to steal [d]'s homework, took [d]'s wallet. You feel angry."

            pov "Remember what I told you before? I think [a], [b], [c] tried to steal your homework. Now I think they took your wallet. "

            d "What's wrong with them? What are they doing? I need to talk to them. "

            show d1:
                xzoom -0.4
                linear 2  xoffset 1500

            "..."

            hide d1

            show a1 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 800
            show b1 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1200
            show c1 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1600

            "They [a], [b], [c] are surprised to see [d] come up to them. "

            a "What's the matter?"

            show d1 at center,shaking:
                xzoom -0.4 yzoom 0.4
                xpos 400

            d "Did you take my stuff? "

            a "Huh? What are you talking about? "

            d "My wallet."

            b "No, why would you think we took it?"

            pov "Stop pretending. I heard what you said before."

            show c1 at shaking

            c "Oops, you've got great hearing. "

            "..."

            a "Alright then. There's nothing we can do since we're heard. "

            show a1:
                xzoom -0.4
                linear 1
                linear 2  xoffset 1500
                xzoom 0.4
                linear 2  xoffset 600

            "[a] walks to a corner of the classroom and takes out the wallet."

            $ renpy.pause(5.0, hard=True)

            pov "Don't do that again. It's stealing, okay? "

            b "Why are you so serious? It's only a small joke, bro."

            pov "I don't find it funny though."

            d "..."

            d "OKAY! Then Forget it."

            show d1:
                xzoom 0.4
                linear 2 xoffset -500

            "[d] drags you back to [chars[3][3]] seat. "

            hide d1
            hide a1 with dissolve
            hide b1 with dissolve
            hide c1 with dissolve

            "[d] looks upset. "

            show d1 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1000

            d "...Thank you."

            pov "It's what I should do."

            "..."

            hide d1 with dissolve

            "[d] gets up and walks out of the classroom.\nYou think [chars[3][2]] just needs some time alone."



            "When [chars[3][2]] comes back, the class is over."

            "..."

            "Well done for stepping up to the plate!"

            "Keep going!"

        "Don't think too much about it.":

            "You leave [a], [b], [c] alone because you don't know what they want to do. "

            "After class, [d] goes out and you see the three of them gather around. "

            show a1 at center with dissolve:
                xzoom 0.2 yzoom 0.2
                xpos 2000 ypos 1000
                linear 2 xoffset -800
                xzoom 0.2
            show b1 at center with dissolve:
                xzoom 0.2 yzoom 0.2
                xpos 2000 ypos 1000
                linear 2 xoffset -1000
            show c1 at center with dissolve:
                xzoom 0.2 yzoom 0.2
                xpos 2000 ypos 1000
                linear 2 xoffset -1200
                xzoom -0.2

            "You don't feel right. "

            menu:

                "Stop them.":

                    "So you walk over."

                    show a1:
                        linear 2 xzoom 0.4 yzoom 0.4 xpos 2200
                    show b1:
                        linear 2 xzoom 0.4 yzoom 0.4 xpos 2000
                    show c1:
                        linear 2 xzoom -0.4 yzoom 0.4 xpos 1600

                    pov "What are you doing? Can I join you guys?"

                    show a1 at speaking

                    a "Er..no? Nothing. Just chatting."

                    show b1 at speaking

                    b "Yeah, yeah, we're just talking. "

                    "..."

                    "They avoid your eye contacts and look a little embarrassed."

                    menu:
                        "Warn them":

                            pov "I actually heard you guys talking earlier. And, I don't think it's good behavior to poke fun at other people like that."

                            show c1 at speaking

                            c "I don't know what you're talking about. "

                            pov "Are you gonna take [d]'s homework?"

                            show a1 at speaking
                            show b1 at speaking
                            show c1 at speaking

                            abc "..."

                            pov "This is already considered as theft. "

                            b "...We won't do it again. Don't you tell [chars[3][4]]."

                            pov "Don't do this to others either."

                            a "Ok, I won't do it again......"

                            show a1 :
                                xzoom -0.4 yzoom 0.4
                                linear 1 xoffset 1500
                                xzoom -0.2
                            show b1 :
                                xzoom -0.4 yzoom 0.4
                                linear 1 xoffset 1500
                            show c1 :
                                xzoom -0.4 yzoom 0.4
                                linear 1 xoffset 1500

                            "They leave and you return to your seat."

                            hide a1
                            hide b1
                            hide c1

                            "[d] returns to the classroom as the bell rings, but [chars[3][2]] doesn't know what happened."

                            "Well done for preventing a bully event from happening. Preaction is better tham reaction. No one will get hurt."

                            "..."
                        #111
                        "Stall time.":

                            pov "Eh, so can I join you? "

                            show a1 at shaking

                            a "Uh, nothing really, just thinking about my homework."

                            pov "Ah, I actually can't quite figure out how to write my homework, let's do it together!"

                            show b1 at shaking

                            b "Oh, oh well, then ...... it's almost time for class, so let's go back to our seats and have a look."

                            show c1 at speaking

                            c "Yeah right, let's go sit down and discuss."

                            "So you go back to your seats. \nYou pretend to continue the discussion with them."

                            show a1 :
                                xzoom -0.4 yzoom 0.4
                                linear 3 xoffset 1500

                            show b1 :
                                xzoom -0.4 yzoom 0.4
                                linear 3 xoffset 1500
                            show c1 :
                                xzoom -0.4 yzoom 0.4
                                linear 3 xoffset 1500

                            "Class starts and [d] returns to the class, unaware of what has happened. "

                            "[a], [b], [c] think you have an eye on them. Nothing happen to [d] or any other ever after. "

                            "Well done, you stopped a bullying event in advance."

                            "But you should just warn them not to do such things ever again. Otherwise, they might have continued to do so when you are not present."

                            "..."

                "Pretend you don't see it":

                    hide a1 with dissolve
                    hide b1 with dissolve
                    hide c1 with dissolve



                    hide d1

                    "You see three of them huddled around [d]'s seat and after a while they leave with weird smiles on their faces."



                    "..."

                    show d1 at center,left with dissolve:
                        xzoom -0.4 yzoom 0.4
                        linear 3  xoffset 3000

                    "[d] comes back, but doesn't notice that anything has been taken."

                    hide d1

                    menu:

                        "Remind [chars[3][4]].":

                            "Fortunately you have [d]'s number."

                            pov "{image=phone.png}\"Hi, I just saw some people taking something out of your school bag.\""

                            show d1 at center with dissolve:
                                xzoom 0.4 yzoom 0.4
                                xpos 1000
                            voice "/audio/msg.mp3"
                            d "{image=phone.png}\"Jesus, thank you, let me check...\""

                            "[d] rummages through [chars[3][3]] bag."

                            "After a while, [chars[3][2]] finds that something is missing."

                            show d1 at shaking
                            voice "/audio/msg.mp3"
                            d "{image=phone.png}\"Someone took my homework. Do you know who did this?\""

                            pov "{image=phone.png}\"Yeah, I think is [a], [b] and [c].\""
                            voice "/audio/msg.mp3"
                            d "{image=phone.png}\"Thank you.\""

                            hide d1 with dissolve

                            "Suprisingly, [chars[3][2]] doesn't look very angry, as if [chars[3][2]]'s used to this sort of thing."

                            "And [chars[3][2]] asks for [chars[3][3]] homework back from those people afterwards."

                            "..."

                            "Although [chars[3][2]] seems to be used to this kind of events, it doesn't mean [d] wouldn't get hurt."

                            "Maybe you can try to stop from happening in advance next time."

                            "Let's try it again!"

                            hide a1
                            hide b1
                            hide c1
                            hide d1

                            jump refirststory

                        "Pretend you don't see it":

                            hide d1

                            "By the time classes start in the afternoon."

                            t "All right, turn in your homework."

                            "Everyone is going through his or her bags, and give his or her homework to the teacher."

                            show d1 at center:
                                xpos 1000
                                xzoom 0.4 yzoom 0.4
                                linear 0.5
                                xzoom -0.4
                                linear 0.5
                                repeat

                            "However, [d] is still finding."

                            "..."

                            "After a while..."

                            show d1 at center,speaking:
                                xpos 1000
                                xzoom 0.4 yzoom 0.4

                            d "Sorry, I think I forgot my homework at home..."

                            t "Well, are you sure you have finished it?"

                            d "Yes..."

                            t "Never mind, come to my office after the class."

                            d "Yes..."

                            "..."



                            "[d] looks really upset."

                            show a1 at center,shaking:
                                xzoom 0.2 yzoom 0.2
                                xpos 1600 ypos 1000


                            show b1 at center,shaking:
                                xzoom 0.2 yzoom 0.2
                                xpos 1500 ypos 1000


                            show c1 at center,shaking:
                                xzoom 0.2 yzoom 0.2
                                xpos 1400 ypos 1000



                            abc "{size=-10}Hahahahaha...{/size}"

                            "And you hear some people are secretly laughing."

                            hide a1 with dissolve
                            hide b1 with dissolve
                            hide c1 with dissolve
                            hide d1 with dissolve

                            "..."

                            "Let's try it again."



                            jump refirststory










    return

label secondstory:
    #language
    "Chapter two"
    python:
        chars=generatechar(5)
        ex2= [[] for i in range(5)]
        for i in range(5):
            ex2[i] = generatecharimage(chars[i])
    image a2 = Composite(
        (300, 175),
        (-1240, -1754), "[ex2[0][3]]",
        (-1240, -1754), "[ex2[0][0]]",
        (-1240, -1754), "[ex2[0][1]]",
        (-1240, -1754), "[ex2[0][2]]")
    image b2 = Composite(
        (300, 175),
        (-1240, -1754), "[ex2[1][3]]",
        (-1240, -1754), "[ex2[1][0]]",
        (-1240, -1754), "[ex2[1][1]]",
        (-1240, -1754), "[ex2[1][2]]")
    image c2 = Composite(
        (300, 175),
        (-1240, -1754), "[ex2[2][3]]",
        (-1240, -1754), "[ex2[2][0]]",
        (-1240, -1754), "[ex2[2][1]]",
        (-1240, -1754), "[ex2[2][2]]")
    image d2 = Composite(
        (300, 175),
        (-1240, -1754), "[ex2[3][3]]",
        (-1240, -1754), "[ex2[3][0]]",
        (-1240, -1754), "[ex2[3][1]]",
        (-1240, -1754), "[ex2[3][2]]")
    image e2 = Composite(
        (300, 175),
        (-1240, -1754), "[ex2[4][3]]",
        (-1240, -1754), "[ex2[4][0]]",
        (-1240, -1754), "[ex2[4][1]]",
        (-1240, -1754), "[ex2[4][2]]")


    $ chars=generatechar(5)
    define a = Character("[chars[0][5]]")
    define b = Character("[chars[1][5]]")
    define c = Character("[chars[2][5]]")
    define d = Character("[chars[3][5]]")
    define e = Character("[chars[4][5]]")


    label resecondstory:
        hide a2
        hide b2
        hide c2
        hide d2
        hide e2



    #3 around 1 2 friends.

    "It's the first day of a new semester. You are surrounded by people, most of whom you barely know."

    scene mcr

    "You sit anxiously in your chair alone, trying to find someone you possibly know."

    show d2 at center,shaking:
        xzoom -0.4 yzoom 0.4
        linear 2
        xpos 800
        linear 2 xoffset 1500
    show e2 at center,shaking:
        xzoom -0.4 yzoom 0.4
        linear 2
        xpos 1200
        linear 2 xoffset 1500


    "Luckily, you see two of your former classmates [d] and [e]. You greet them, but they are seated far away from you."

    "..."

    hide d2
    hide e2

    "At the end of the first day, you get to know the people around you a little more."

    show a2 at center,speaking with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 400

    a "Hey, would you like to have dinner together? So that we can get to know each other better."

    show b2 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    b "Good idea! I'd like to have some chips!"

    pov "Sure, sounds great."

    show c2 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400

    c "..Sorry, I'm not available tonight."

    show a2 at shaking

    a "That's fine, but you have to join us next time."

    show c2 at speaking

    c "Haha, ok. Have fun."

    "..."

    hide a2
    hide b2
    hide c2


    "..."

    "You have a great time with them. You really like these people from the new class."

    "\"It's a good start.\" You talk to yourself."

    "..."

    "For the next few days, you enjoy a normal school life."

    "You spend most of your lunch time or breaks with people that sit around you in the classroom. But, you still get to chat or hang out with [d] and [e] occasionally."





    "..."

    scene mct with dissolve

    "..."

    "..."

    "One day"

    show b2 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    b "[c], why are you eating this again?"

    show c2 at center,speaking with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 400

    c "Err, I just like it..."

    show a2 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400

    a "Such a Spaghetti zealot! You should have some meat and vegetables. Always eating spaghetti is not healthy."

    pov "Well...but I think [chars[2][2]]'s healthier than you."

    show a2 at shaking

    a "Huh? Why?"

    pov "Look, [chars[2][2]] never buys drinks, only drinks water, but you have coke everyday."

    pov "That's a lot of sugar you know."

    show a2 at speaking

    a "...Make sense...wait, but last time I gave [chars[2][4]] a can of coke and [chars[2][2]] took it, which means [chars[2][2]] also drinks it right?"

    c "Haha..."

    "You notice [c] smiling awkwardly."

    pov "Correct. But [chars[2][2]] still drinks much less coke than you do."

    show a2 at speaking

    a "Wait and see. I'll drink diet coke, starting from tomorrow."

    pov "Haha, I bet it won't last for more than two days."

    "..."

    hide a2
    hide b2
    hide c2

    show mcr with dissolve

    "..."

    "However, the longer you know [c], the more you think [chars[2][3]] family might not be well off."

    show a2 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400

    a "Let's create a WhatsApp group, shall we? We can discuss our homework there."

    show b2 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    b "Oh that's great, we should be friends on WhatsApp first."

    show c2 at center:
        xzoom -0.4 yzoom 0.4
        xpos 400

    "..."

    show a2 at shaking
    show b2 at shaking

    "All of you take your phone out, except [c]."

    pov "[c], is there anything wrong? What's your account?"

    c "...[c]@hmail.com"

    "..."

    pov "Alright, got it, I have already send you the application. You gonna approve it."

    c "Ah, ok."

    "Finally [chars[2][2]] takes [chars[2][3]] phone out."

    show a2 at shaking


    a "Wow, is it jphone6 or 6s? I miss it so much!"

    show b2 at shaking

    b "It is, it has been what... six years?"

    c "Yeah...my mom used it."

    pov "All done. I've added you all. I'll create a group."

    hide a2
    hide b2
    hide c2

    "..."

    hide mct

    "Also, [chars[2][2]] barely changes [chars[2][3]] clothes."


    scene blk with dissolve

    "After a while, you find that [chars[2][2]] doesn't like to join your conversations. Actually [chars[2][2]] doesn't join any of your activities at all."

    "Gradually, people stop inviting [chars[2][4]] to after-school activities."

    "..."

    "..."

    "..."

    "A month past by."

    scene mcr

    "One day after the class, you are about to have lunch."

    show a2 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show b2 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    show c2 at center:
        xzoom 0.2 yzoom 0.2
        xpos 400
    with dissolve
    "At the moment, [c] is discussing a problem with the teacher and you are waiting for [chars[2][4]] to join you."

    show a2 at speaking:
        xzoom -0.4
        linear 2 xoffset 1500

    a "Let's go to the canteen."

    show b2 at speaking:
        xzoom -0.4
        xpos 1400
        linear 2 xoffset 1500

    b "[pov], hurry up or there will be a queue later."

    pov "Oh, ok. alright. Coming!"

    hide c2 with dissolve

    hide a2
    hide b2

    "You're a bit surprised that they didn't wait for [c]. You wonder if [c] said ahead of time not to wait for [chars[2][4]] or [chars[2][2]]'s not going to lunch today."


    scene mct with dissolve

    "..."

    show a2 at center:
        xzoom -0.4 yzoom 0.4
        xpos 600
    show b2 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1200

    "..."

    show c2 at left,speaking:
        xzoom -0.2 yzoom 0.2
        ypos 1000
        linear 5 xoffset 3000

    "While eating, you notice that [c] has come to the canteen and has found a seat to eat alone."

    "You are a little confused."

    pov "Why does [c] come to lunch alone?"

    show b2 at speaking

    b "Because [chars[2][2]] doesn't have anyone else to eat with, right?"

    pov "So why not come to us?"

    show a2 at speaking

    a "Maybe [chars[2][2]] has found out that we don't want to eat with [chars[2][4]]."

    pov "Huh? No? Why? "

    show a2 at speaking

    a "Don't you think [chars[2][2]] can't actually fit in our group?"

    pov "Does [chars[2][2]]?"

    show b2 at speaking

    b "[c] never goes out with us, [chars[2][3]] phone doesn't support the latest games, and [chars[2][2]] doesn't even join us for casual conversations."

    pov "Huh..."

    "You don't know what to say and eat in silence."

    hide a2
    hide b2
    hide c2

    "..."

    scene mcr with dissolve


    "..."



    show a2 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show b2 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400

    "..."

    show c2 at left,speaking:
        xzoom -0.4 yzoom 0.4
        xpos 0
        linear 3 xoffset 400


    "After eating and returning to class, [c] come back a while later, but [chars[2][2]] doesn't ask where you had gone to eat. "

    hide c2 with dissolve

    "It's as if [chars[2][2]]'s used to being treated this way. And, in fact, when you think back, you realise that [chars[2][2]] has never initiated a conversation with you. "

    hide a2
    hide b2

    "But [chars[2][2]] was very willing to respond when you approached [chars[2][4]] to talk. It's not the case that [chars[2][2]] doesn't want to talk to you. "

    "You decide to..."

    menu:
        "Ask [chars[2][4]] to join you for lunch.":

            "..."

            scene blk with dissolve

            "..."

            scene mcr with dissolve



            "The next day at noon."

            pov "You guys go ahead and eat today. I have something to do."

            "You walk out of the classroom. "

            scene mcd with dissolve

            "..."

            show a2 at left:
                xzoom -0.2 yzoom 0.2
                xpos -200
                ypos 1000
                linear 5 xoffset 3000

            show b2 at left:
                xzoom -0.2 yzoom 0.2
                xpos 0
                ypos 1000
                linear 5 xoffset 3000

            "After [a] and [b] have left, you go back to the classroom. "

            "..."

            scene mcr with dissolve
            hide a2
            hide b2
            show c2 at center:
                xzoom -0.4 yzoom 0.4
                ypos 1000 xpos 1000

            pov "Want to go to lunch together? "

            show c2 at speaking

            c "Huh? Uh....yeah....let's go...... "

            show c2:
                xzoom -0.4 yzoom 0.4
                ypos 1000
                linear 5 xoffset 3000


            scene mct with dissolve

            "So you go to the canteen together and pick a seat away from [a] and [b]. "

            "..."
            hide c2

            "You eat your meal quietly. "

            "..."


            scene mcr with dissolve

            "..."

            show a2 at center:
                xzoom -0.4 yzoom 0.4
                xpos 600

            show b2 at center:
                xzoom 0.4 yzoom 0.4
                xpos 1200

            "When you return to class, you notice that [a] and [b] look at you a bit strangely and don't offer to greet you. "

            hide a2 with dissolve
            hide b2 with dissolve

            "Feeling a little strange, you sit down and take out your phone. You find a message from [d]. "

            show d2 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1000
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"What's going on with you guys? I was sitting behind [a] and [b] just now and they seem to be upset with you. \""

            pov "{image=phone.png}\"Ah, maybe because I didn't go to lunch with them?\""
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"They said they just told you something yesterday and today you act this or something.\""

            pov "{image=phone.png}\"...... I see, thank you.\""

            hide d2 with dissolve

            "You didn't expect them to find out you were planning to have lunch with [c] and it was a bit embarrassing."

            scene blk with dissolve

            "..."

            scene mcr with dissolve

            "..."

            "And the next day noon, they don't invite you and go for the lunch by themselves."

            show a2 at center:
                xzoom 0.4 yzoom 0.4
                xpos 2200
                linear 5 xoffset -3000

            show b2 at center:
                xzoom 0.4 yzoom 0.4
                xpos 2000
                linear 5 xoffset -3000

            $ renpy.pause(3.0, hard=True)


            "..."

            show c2 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1000

            c "You don't have to do this. It's not worthy for you to lose friends for me."

            pov "It's okay, I'd rather be with you."

            "..."

            hide c2 with dissolve
            hide a2
            hide b2

            "..."

            scene blk with dissolve

            "..."

            scene mcr with dissolve

            "..."

            "[a] and [b] have stopped inviting you to their events for a week. Although you will have dinner with [c]. /nAnd [d] and [e] strike up a conversation with you. "

            "But sitting next to someone and not being able to communicate makes you uncomfortable."

            menu:
                "Keep doing this.":

                    show c2 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000

                    "So you become better with [c]. [c], as a response, becomes more forthcoming with you. However, the rest of the class doesn't get along as well with you because of [a] and [b]."

                    "..."

                    hide c2 with dissolve

                    "The next year, you are in different classes and you meet new classmates."

                    "However, [c] doesn't meet anyone like you, and becomes alone again as before."

                    "..."

                    "It's good for you to help a person like [chars[2][4]], but sometimes the power of one person is just not enough."

                    "Let's try it again!"

                    scene blk with dissolve

                    "..."

                    scene mcr with dissolve

                    "..."

                    jump resecondstory

                "You can't hold on to this anymore.":

                    "Obviously it's better for you to be on good terms with [a] and [b]."

                    "So find a time when [c] isn't around."

                    show a2 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200


                    show b2 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 600


                    pov "Can I join you for lunch today?"

                    "[a] and [b] look at each other."

                    show b2 at center:
                        xpos 600
                        xzoom -0.4 yzoom 0.4
                        linear 2
                        xzoom 0.4 yzoom 0.4
                    $ renpy.pause(1.0, hard=True)

                    show a2 at speaking
                    a "Sure."
                    show b2 at speaking
                    b "Wise choice."

                    scene blk with dissolve

                    "..."

                    hide a2
                    hide b2
                    hide c2

                    scene mct with dissolve

                    "..."

                    show a2 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200


                    show b2 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 600
                    with dissolve

                    "At noon, you go to lunch together."

                    show c2 at left:
                        xzoom -0.2 yzoom 0.2
                        linear 3 xoffset 3000

                    "When you see [c] eating alone at lunch time, you feel a bit bad but you can't do anything about it. "

                    hide a2
                    hide b2
                    hide c2

                    "..."

                    scene mcr with dissolve

                    "..."

                    show c2 at left:
                        xzoom -0.4 yzoom 0.4
                        linear 3 xoffset 3000

                    "Back in the classroom, [c] doesn't say anything to you as if [chars[2][2]] can see it coming. "

                    "..."

                    "That's how you get through a normal year. "

                    "The following year, you move to different classes, meet new friends and [c] remains on [chars[2][3]] own. "

                    "..."

                    "At least you tried, but sometimes it's hard to keep up with the decision."

                    "Let's try it again!"

                    scene blk with dissolve

                    "..."

                    scene mcr with dissolve

                    "..."

                    jump resecondstory



        "Keep hanging out with [a] and [b].":

            "You can't take the risk of being alienated."

            "You've had a normal year, and you maintain friendly relationships with most people. But you've been sorry for [c] secretly in your heart."

            "Every time you see [chars[2][4]] being alone, you always feel like you should have done something about it. But it's too late."

            "The following year, you move to different classes and never speak to each other again. "

            "It's hard to take the risk, but maybe you can have a try."

            "Let's do it again."

            scene blk with dissolve

            "..."

            scene mcr with dissolve

            "..."

            jump resecondstory

        "Ask [d] and [e] what I should do.":

            "You don't think you can handle this alone, so you call up [d] and [e] after class."

            show d2 at center:
                xzoom 0.4 yzoom 0.4
                xpos 1200


            show e2 at center:
                xzoom -0.4 yzoom 0.4
                xpos 600
            with dissolve

            "You tell them what's going on. "

            show d2 at speaking

            d "......This kind of thing happens all the time. Some people are like this."

            show e2 at speaking

            e "I don't think people should alienate others just because of that."

            pov "Yes, so I wondered if I could help [chars[2][4]]. "

            show d2 at speaking

            d "Yes, we haven't had any contact with [chars[2][4]] before and don't know about [chars[2][4]], but we're happy to have a try. "
            show e2 at speaking
            e "En."

            scene blk with dissolve

            "..."

            scene mcr with dissolve

            "So the next day at noon."

            pov "You guys go ahead and eat today, I have something to do."

            "You said to [a] and [b] while you walk out of the classroom."

            scene mcd with dissolve

            "..."

            show a2 at left:
                xzoom -0.2 yzoom 0.2
                xpos -200
                ypos 1000
                linear 5 xoffset 3000

            show b2 at left:
                xzoom -0.2 yzoom 0.2
                xpos 0
                ypos 1000
                linear 5 xoffset 3000


            "After [a] and [b] have left, you go back to the classroom. "

            "..."

            scene mcr with dissolve
            hide a2
            hide b2
            show c2 at center:
                xzoom -0.4 yzoom 0.4
                ypos 1000 xpos 1000

            pov "Want to go to lunch together? "

            c "Huh? Uh...yeah....let's go. "

            "..."

            hide c2

            scene mcd with dissolve

            "On the way."

            show c2 at center,speaking:
                xzoom -0.4 yzoom 0.4
                ypos 1000 xpos 1000

            c "You don't have to do this, you'll be alienated by them if you stay with me. "

            pov "What? Why do you say that? I just came back and saw you were still here so I asked you to come along. "

            c "I see..."

            "..."

            scene mct with dissolve

            hide c2

            "..."

            show c2 at center:
                xzoom -0.4 yzoom 0.4
                ypos 1000 xpos 400

            show d2 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                ypos 1000 xpos 1000

            show e2 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                ypos 1000 xpos 1400

            "When you get to the canteen, after serving your meal, you take [c] straight to your friends."

            show c2 at speaking

            "[c] is somewhat surprised. "

            pov "They are all from our class, I was also in same class with them last year! "

            show d2 at speaking

            d "Hi, my name is [d]."

            show e2 at speaking

            e "I'm [e]."

            show c2 at speaking

            c "Ah, hello! My name is [c]."

            pov "You don't have to give up on yourself, we'd all like to be your friends. "

            c "...Thanks..."

            "..."

            scene blk with dissolve

            "After that, you have lunch together every day, and you usually talk to [chars[2][4]]."

            "Although [chars[2][2]] is still unable to participate in the after-school activities, this does not hinder your relationship."

            "The rest of the class gradually become friends with [c] when they see how close you four are. "

            "Slowly [chars[2][2]] settles into the class. "

            "The next year, you're not in the same class, but you still keep in touch with [c]."

            "[c] is grouped with some of the others in the class and they maintain the same good relationships. [c] integrate perfectly into the new class."

            "Great job! You changed your friend's social life."

            scene blk with dissolve

            "..."
    return

label thirdstory:
    #language
    "Chapter three"
    python:
        chars=generatechar(4)
        ex3= [[] for i in range(4)]
        for i in range(4):
            ex3[i] = generatecharimage(chars[i])
    image a3 = Composite(
        (300, 175),
        (-1240, -1754), "[ex3[0][3]]",
        (-1240, -1754), "[ex3[0][0]]",
        (-1240, -1754), "[ex3[0][1]]",
        (-1240, -1754), "[ex3[0][2]]")
    image b3 = Composite(
        (300, 175),
        (-1240, -1754), "[ex3[1][3]]",
        (-1240, -1754), "[ex3[1][0]]",
        (-1240, -1754), "[ex3[1][1]]",
        (-1240, -1754), "[ex3[1][2]]")
    image c3 = Composite(
        (300, 175),
        (-1240, -1754), "[ex3[2][3]]",
        (-1240, -1754), "[ex3[2][0]]",
        (-1240, -1754), "[ex3[2][1]]",
        (-1240, -1754), "[ex3[2][2]]")
    image d3 = Composite(
        (300, 175),
        (-1240, -1754), "[ex3[3][3]]",
        (-1240, -1754), "[ex3[3][0]]",
        (-1240, -1754), "[ex3[3][1]]",
        (-1240, -1754), "[ex3[3][2]]")



    $ chars=generatechar(4)
    define a = Character("[chars[0][5]]")
    define b = Character("[chars[1][5]]")
    define c = Character("[chars[2][5]]")
    define d = Character("[chars[3][5]]")

    define f = Character("Professor")

    define x = 0

    label rethirdstory:
        hide a3
        hide b3
        hide c3
        hide d3

    scene ucr with dissolve


    $ x = 0

    "You are a Computer Science student. This semester, you have enrolled in a course with medical students, and today is the first day of the course."

    f "...Alright, please follow the instructions on the screen to find your groups and start your discussion."
    f "Introduce yourself first and choose a disease you are interested."

    "..."

    show a3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 700
    show b3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1300
    show c3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1700
    show d3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 300
    with dissolve

    "All your group members sit around the table. You find out that you don't know any of them."

    show a3 at speaking

    a "Hi guys, I'm [a], and I major in Health Data Science."

    show b3 at speaking

    b "My major is Health Data Science too, I'm [b], nice to meet you!"

    show c3 at speaking

    c "Me too, you can call me [c]."

    pov "My name is [pov], I major in Computer Science. I'm new to the medical field. But I am excited to explore and it's really nice to be in the same group as you guys."

    show a3 at speaking

    a "Haha, sure."

    d "{size=-10}...Hello everyone, my name is [d], uhh I major in Biotechnology.{/size}"

    "You find that it's really hard to hear [d]'s voice, maybe [chars[3][2]] is not good at speaking English."

    show a3 at speaking

    a "So, then we need to choose a disease, right?"

    show a3 at speaking
    show b3 at speaking
    show c3 at speaking

    "yeeeees. \nyeah.\nright.\n{size=-10}...yes.{/size}"

    a "Any ideas?"

    d "{size=-10}...Chronic pharyng...{/size}"

    show b3 at speaking

    b "How about COVID-19? It should be interesting to learn about it."

    show a3 at shaking

    a "Oh that's good. I agree. What do you think?"

    show c3 at speaking

    c "Sounds great, and maybe we could get more marks since it's a relatively new disease."

    pov "*Nod"

    "You think [chars[0][2]] gets a point."

    d "{size=-10}..But I heard teacher say it's better to choose a......chronic disease. COVID-19 may not be a proper one...{/size}"

    pov "Oh yes, the professor did say that, I almost forgot."

    show a3 at speaking

    a "Forgot what?"

    show b3 at speaking
    show c3 at speaking

    "Meanwhile, both [b] and [c] look at you in confusion."

    pov "[d] just said we should choose a chronic disease, right?"

    "You are the only one that heard [chars[3][3]] since you sit next to [d]."

    d "{size=-10}..Yes, it's what the professor said...{/size}"

    show a3 at speaking

    a "Oh, Ok, so any other ideas?"

    d "{size=-10}...I'm a little bit interested in chronic pharyng...{/size}"

    show c3 at speaking

    c "How about Rheumatoid Arthritis? My grandpa has this disease, so I want to learn something about it."

    show a3 at shaking

    a "Cool! He would be so proud of you! How do you guys think? I'd like to research on this."

    d "{size=-10}Ah, sure, good idea...{/size}"

    pov "I think it's pretty good."

    show b3 at shaking

    b "Let's do it!"

    "In order to communicate after the class, you followed each other on social media and created a WhatsApp group."

    show a3 at shaking
    show b3 at shaking
    show c3 at shaking

    "[a], [b] and [c] seem to be very chatty, while you and [d] just say hello politely."

    "..."

    hide a3
    hide b3
    hide c3
    hide d3
    with dissolve

    scene drm with dissolve

    "After dinner, you decide to do something."

    menu:
        "It's time to relax!":
            $ x=x
            pov "I can't wait to watch the Love, Death & Robots 2! It's must be better than season 1!"

            "..."

            scene blk with dissolve
        "I should find some information about Rheumatoid Arthritis.":

            pov "Let me see if I can find anything on Google..."

            pov "Rheumatoid Arthritis...enter."

            image google = "images/assets/google.png"
            show google at center with dissolve

            pov "Oh, there's a lot of useful information. I have to write them down..."
            pov "Alright, they can save us a lot of time..."

            hide google with dissolve

            pov "Ok then. It's time to rest?"
            menu:
                "Yes!":
                    pov "I can't wait to watch the Love, Death & Robots 2! It's must be better than season 1!"
                    "..."
                    scene blk with dissolve
                "Maybe I can share them with the group.":
                    $ x+=1
                    pov "I wonder if they searched for useful information as well."
                    pov "{image=phone.png}\"Hey guys, I found some information about the Rheumatoid Arthritis, hope it helps.\""
                    show a3 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"Oh sweet! You are so hardworking! We are still having party with [b] and [c]! I'll check with them later!\""
                    pov "{image=phone.png}\"LOL, Have fun!\""
                    show d3 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 800
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"I found something, too. You can check them out as well.\""
                    voice "/audio/msg.mp3"
                    d """{image=phone.png}\"https://www.nice.org.uk/... It's about causes of disease\"\n
                         \"https://www.versusarthritis.org/... basic information\"\n
                         \"https://www.... treatment\"\n
                         \"......\"

                    """
                    pov "{image=phone.png}\"OMG that's a LOT, you're amazing!\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"Thank you haha,,\""
                    "You spend a lot of time to browse all websites through, and, surprisingly, they are all very useful."
                    hide d3
                    hide a3
                    with dissolve
                    "..."

                    scene blk with dissolve

    "..."

    show ucr with dissolve
    "A week later"

    show a3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 700
    show b3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1300
    show c3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1700
    show d3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 300
    with dissolve

    "Today is your second session of the class, and you have a group conversation after the lecture as well."

    show a3 at speaking

    a "Wow, it's been a week, so what we need to do today?"

    show b3 at speaking

    b "We should summarise the information we found."

    d "{size=-10}...we also need to plan our uhhh swimlane diagram, I'll send an example to the group chat...{/size}"
    #222
    show a3 at speaking

    a "Ok! Summarise..summarise, what we have right now? Oh, let me check our group chat..."

    "[a] starts to use [chars[0][3]] phone."

    show c3 at speaking

    c "You haven't seen them yet? It has already been a week."

    show a3 at shaking

    a "Sorry I was drunk! I totally forgot them."

    show b3 at speaking

    b "Alright alright, we can do it now."

    if (x >=1):

        pov "Actually I have read them so maybe I can help. And [d] has already commented on the contents about every website after the links."

        d "{size=-10}...yeah, those are easy to summarise, so I just wrote them out...{/size}"

        show a3 at speaking

        a "Oh [povname] you are so kind! Let's begin..."

    "..."

    scene blk with dissolve
    hide a3
    hide b3
    hide c3
    hide d3

    "..."



    scene ucr with dissolve

    show a3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 700
    show b3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1300
    show c3 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1700
    show d3 at center:
        xzoom -0.4 yzoom 0.4
        xpos 300
    with dissolve

    "..."

    show a3 at shaking

    a "Oh this article is gonna be useful. There is a lot of data."

    show b3 at speaking

    b "Yeah, and this one as well. We don't need to find data ourselves, lucky!"

    d "{size=-10}...uhhh it's only half an hour left. I think we need to talk about the swim..uhh..diagram...{/size}"

    show c3 at speaking

    c "How about this? It describes some symptoms. I think it's pretty complete."

    show a3 at speaking

    a "Indeed, they all can be used in our report."

    pov "Well..I think we can do it later, and talk about our swimlane diagram?"

    show a3 at shaking

    a "Oh! Thank you for the reminder /n(*Look at the clock)/nWe need to hurry up! Come on, [b], [c], let's do it first."

    show b3 at speaking

    b "Uhhh, What is swimlane?"

    d "{size=-10}...It's a kind of , ehhh, flowchart, I have sent one example in the group ch......{/size}"

    show a3 at shaking

    c "I see! Look, I found an example."

    "You find that [c]'s example is exactly the same as [d]'s."

    d "..."

    menu:
        "Say something":
            $ x+=1
            pov "It's quite a coincidence haha."

            show a3 at speaking

            a "What coincidence?"

            pov "Look, [c] has showed the same example as [d] did."

            c "...Wow, quite a coincidence indeed."

        "Say nothing":
            $ x=x

    show a3 at speaking

    a "Alright, now we know what it looks like, so...I think we first have to decide how many phases we need?"

    pov "Well, if we go to the hospital, we need to do some examinations first?"

    d "{size=-10}...maybe we need to make an appointment before th......{/size}"

    show b3 at speaking

    b "Yup, and then the doctor will diagnose us with the result."

    show c3 at speaking

    c "Then comes the treatment phase?"

    show a3 at speaking

    a "Exactly. Hey guys, I just realise something: do we need to include appointments?"

    show c3 at speaking

    c "Oh totally. It definitely is an important phase. Thank you [a]."

    d "..."

    "You noticed [d] might want to say something, but in the end [chars[3][2]] didn't say a word."

    show a3 at speaking

    a "Perfect, then what roles do we need?"

    show c3 at speaking

    c "Who is in charge of making appointments in clinics?"

    show b3 at speaking

    b "Nurse?"

    pov "And we can also do it on website. I remember our professor said we should think about the data part as well. That's why I am in this group haha."

    show b3 at speaking

    b "Yeah, make sense."

    hide a3
    hide b3
    hide c3
    hide d3
    with dissolve

    scene blk with dissolve

    "..."

    "...You continue the discussion, but [d] doesn't participate anymore and takes some notes on [chars[3][3]] own."

    scene drm with dissolve

    "The same evening, you start to work on that swimlane diagram."

    "Looking at the notes you took, you decide to..."

    menu:
        "Do it on your own.":
            "You think you have had enough discussion with the group this afternoon and start drawing swimlane diagram from your notes."

            pov "It's quite easssssy, I've already got all the phases and roles. I just need to link them together..."

            "..."

            pov "Wait, what do podiatrists do...I forgot to note that down..."

            "..."

            pov "OMG there are too many lines here. I have to separate them a bit..."

            "..."

            pov "Can't these boxes be fixed in the grid? I have to put them in everytime I resize the grid!"

            "..."

            "..."


            pov "Alright! I'm done today, counting on you, tomorrow's me!"

            "..."

            scene blk with dissolve

            "..."

            "..."


            if (x >=2):

                scene drm with dissolve

                show d3 at center with dissolve:
                    xpos 1000
                    xzoom 0.4 yzoom 0.4
                voice "/audio/msg.mp3"
                d "{image=phone.png}\"..Are you available?\""

                "Suddenly, [d] sends you a message"

                pov "{image=phone.png}\"Yeah, what's up?\""

                jump asking

            "Two days later."

            scene drm with dissolve

            pov "Finally...before the deadline..."

            pov "Now just upload it..."

            pov "I've drawn up all we have discussed. So I should get high marks, right?"

            pov "Forget it, that's it! I can at last get back to watch my Love, Death & Robots 2!"

            scene blk with dissolve

            jump final

            jump normal

        "Discuss in the group.":
            "You are worried about missing something and suggest in the group chat that you want to do it together."

            pov "{image=phone.png}\"Hi guys, do you want to finish the swimlane diagram together? I'm afraid I've missed some points.\""

            show a3 at center with dissolve:
                xpos 800
                xzoom -0.4 yzoom 0.4
            voice "/audio/msg.mp3"
            a "{image=phone.png}\"Sure, but I think we have alreally found them all.\""

            show b3 at center with dissolve:
                xpos 1200
                xzoom 0.4 yzoom 0.4
            voice "/audio/msg.mp3"
            b "{image=phone.png}\"Come on! Believe in ourselves, just follow the notes and we will get good grades.\""

            pov "{image=phone.png}\"Lol I hope so.\""

            hide a3
            hide b3
            with dissolve

            scene blk with dissolve

            "..."

            "..."

            if (x >=2):

                scene drm with dissolve
                voice "/audio/msg.mp3"
                d "{image=phone.png}\"...Hi, are you available now?\""

                "Suddenly [d] sends you a message."

                pov "{image=phone.png}\"Yeah, what's up?\""

                jump asking

            "Two days later."

            scene drm with dissolve

            pov "Finally...before the deadline..."

            pov "Now just upload it..."

            pov "I've drawn up all the discussion, so I should get high marks, right?"

            pov "Forget it, that's it! I can at last get back to watching my Love, Death & Robots 2!"

            scene blk with dissolve

            call final from _call_final

            jump normal


        "Discuss with [d].":
            pov "{image=phone.png}\"Hi, are you available?\""

            "You send a message to [d]."

            show d3 at center with dissolve:
                xpos 1000
                xzoom 0.4 yzoom 0.4
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"I am. Is there anything wrong?\""

            pov "{image=phone.png}\"Yeah...I'm just not sure about our diagram...\""

            pov "{image=phone.png}\"I don't know, but I'm afraid we missed something...\""

            if (x>=1):
                voice "/audio/msg.mp3"
                d "{image=phone.png}\"I agree...\""

                jump asking
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"...Really? I think it's pretty good. I'll just follow what we discussed.\""

            pov "{image=phone.png}\"Oh really? I'm relieved then, thank you.\""
            voice "/audio/msg.mp3"
            d "{image=phone.png}\"...No problem...\""

            hide d3 with dissolve
            scene blk with dissolve

            "..."

            "..."

            scene drm with dissolve
            "Two days later."

            pov "Finally...before the deadline..."

            pov "Now just upload it..."

            pov "I've drawn up all the discussion, so I should get high marks, right?"

            pov "Forget it, that's it! I can at last get back to watching my Love, Death & Robots 2!"

            scene blk with dissolve


            call final from _call_final_1

            jump normal




    label final:

        "..."

        scene ucr with dissolve

        "Week three"

        f "...Well, that's it for today's lecture. If you have any more questions you can come and see me later."
        f "The rest of the time is reserved for you to discuss your presentations and PPTs for next week. "
        f "By the way, I have finished looking at all the swimlane diagrams you submitted from last week. The gradings and rubrics will be uploaded to the website by Thursday. "

        "..."

        show a3 at center:
            xzoom -0.4 yzoom 0.4
            xpos 700
        show b3 at center:
            xzoom 0.4 yzoom 0.4
            xpos 1300
        show c3 at center:
            xzoom 0.4 yzoom 0.4
            xpos 1700
        show d3 at center:
            xzoom -0.4 yzoom 0.4
            xpos 300
        with dissolve

        "..."

        show b3 at speaking

        b "Hey, how were your swimlane diagrams?"

        show a3 at speaking

        a "Easy peasy, I just spent a day on it."

        show c3 at speaking

        c "Me too. We've had enough discussions, haven't we?"

        pov "Well, I'm still not familiar with the medical field so it took me a few days."

        show b3 at speaking

        b "Let's see how many points we can score."

        show b3 at shaking

        c "We gonna win this!"

        "..."

        hide a3
        hide b3
        hide c3
        hide d3

        scene blk with dissolve

        "..."



        return

    label normal:

        scene drm with dissolve

        "..."

        show a3 at center:
            xzoom -0.4 yzoom 0.4
            xpos 700
        show b3 at center:
            xzoom 0.4 yzoom 0.4
            xpos 1300
        show c3 at center:
            xzoom 0.4 yzoom 0.4
            xpos 1700
        show d3 at center:
            xzoom -0.4 yzoom 0.4
            xpos 300
        with dissolve

        "..."
        voice "/audio/msg.mp3"
        b "{image=phone.png}\"Jesus, I just got 50...the professor said I missed a big part!\""
        voice "/audio/msg.mp3"
        c "{image=phone.png}\"Me too! Why?? We should have found them all!\""
        voice "/audio/msg.mp3"
        a "{image=phone.png}\"I don't understand. I'll talk to him.\""

        "You find your grade is not good as well."

        "You don't say anything, so as [d]..."

        hide a3
        hide b3
        hide c3
        hide d3

        scene blk with dissolve

        "..."

        scene drm with dissolve

        show a3 at center:
            xzoom 0.4 yzoom 0.4
            xpos 1000

        "The next day."

        voice "/audio/msg.mp3"
        a "{image=phone.png}\"I just asked the teacher about our diagram.\""
        voice "/audio/msg.mp3"
        a "{image=phone.png}\"He said we all missed the relapse phase, except [d]??\""
        voice "/audio/msg.mp3"
        a "{image=phone.png}\"Why [chars[3][2]] didn' tell us??\""

        pov "{image=phone.png}\"Really? what the...\""
        voice "/audio/msg.mp3"
        a "{image=phone.png}\"[d] is so selfish! We are a team. How could [chars[3][2]] do this??\""

        pov "{image=phone.png}\"...\""
        voice "/audio/msg.mp3"
        a "{image=phone.png}\"Forget it. We can do well on ourselves!\""

        scene blk with dissolve

        "After this, you never talk to [d] again."

        "[d] has never joined the discussion since then. It seems like there are only 4 of you in the group."

        "Things have gotten worse."

        "Oops! You don't seem to be very good at getting on with [d]. Maybe you should try to talk to [chars[3][4]] more."

        "Let's try it again!"

        "..."

        jump rethirdstory

        return

    label asking:
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"I think they missed a big part...\""
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"Rheumatoid arthritis is not a disease that can be easily cured. I have looked into it before and found that many patients have relapsed.\""

        pov "{image=phone.png}\"Oh really?? I totally missed it..\""
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"...Yeah, if our professor is familiar with this or have looked it up like I did,  he will have thought that our swimlane diagram should have had a relapse phase...\""

        pov "{image=phone.png}\"Oh my god...thank you very much...I certainly wouldn't have realised this if you hadn't warned me.\""
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"It's okay, after all, you've helped me before...\""

        pov "{image=phone.png}\"Have I? I just did what I had to do.\""
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"At least I know someone would listen to me.\""

        pov "{image=phone.png}\"Because what you said does make a lot of sense.\""
        voice "/audio/msg.mp3"
        d "{image=phone.png}\"...Thank you...\""

        pov "Wait...What would happen if they found out we were the only two who scored higher...I don't think anything good will come out of it..."

        pov "Should I remind [chars[3][4]]?"

        menu:
            "May be I should give it a try.":
                pov "{image=phone.png}\"Do you want to tell them about this? I am sure they will be very grateful to you.\""
                if (x == 2):
                    "After a while"
                    d "{image=phone.png}\"...Well, if you want, but I don't think they'll thank me anyway...\""

                    pov "{image=phone.png}\"At least I'll thank you for them.\""

                    scene blk with dissolve
                    hide d3 with dissolve

                    "..."

                    scene drm with dissolve

                    "..."

                    pov "{image=phone.png}\"Hey guys, I just discussed with [d] and [chars[3][2]] found something I think is really important.\""

                    pov "{image=phone.png}\"To be honest, I think I would have failed this assignment if [chars[3][2]] hadn't warned me.\""

                    "You send a screenshot of your conversation with [d]."

                    show c3 at center with dissolve:
                        xzoom -0.4 yzoom 0.4
                        xpos 700
                    voice "/audio/msg.mp3"
                    c "{image=phone.png}\"Wait what is it, relapse phase? Really?\""


                    show b3 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1300
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Holy...that's close...\""

                    pov "{image=phone.png}\"[d] said [chars[3][2]] is not good at communications but it's really important for our group, so [chars[3][2]] asked me to tell you about this.\""

                    pov "{image=phone.png}\"And I think we should discuss about our roles again. What do you think, [d]?\""
                    hide c3
                    hide b3
                    with dissolve

                    show d3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    with dissolve
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...You don't have to do this...\""

                    "[d] send you a personal message."

                    pov "{image=phone.png}\"You deserve it. They should know what you did.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...Alright...\""

                    "..."
                    hide d3

                    scene blk with dissolve

                    "..."


                    scene drm with dissolve

                    "..."

                    show d3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...Actually it is not only the relapse phase. Medicines for rheumatoid arthritis can cause some other side effects.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"Like lung infection, which is a common side effect. So we need to include Pulmonologist in our diagram.\""

                    show b3 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1300
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Make sense.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"And Orthopedist is also required...\""

                    scene blk with dissolve

                    "..."

                    scene drm with dissolve

                    "..."

                    "After a long discussion."

                    show a3 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 700
                    with dissolve
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"...You are right, we did miss a lot of things.\""

                    show d3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200

                    pov "{image=phone.png}\"Haha, although [chars[3][3]] voice is relatively low and you may not notice it, I sat next to [chars[3][4]] and I found that the points [chars[3][2]] made were important.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...Well, I just have time to read more articles about it...\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"No, you've really helped. Thank you very much.\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\" I will take your thoughts more seriously in the future.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...I'll try my best\""

                    hide a3
                    hide d3
                    hide b3
                    with dissolve


                    "..."

                    scene blk with dissolve

                    "..."


                    call final from _call_final_2

                    scene drm with dissolve

                    "..."

                    show a3 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 700
                    show b3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1300
                    show c3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1700
                    show d3 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 300
                    with dissolve
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Hey! I've seen my results! I can't believe it! I've never gotten a score above 90!\""
                    voice "/audio/msg.mp3"
                    c "{image=phone.png}\"Me too! It's crazy! Thanks to [d].\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"*Similing We all did a good job.\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"You saved us.\""

                    pov "{image=phone.png}\"We can't do this without you.\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"...ok.ok, and thank you all,,,\""

                    hide a3
                    hide b3
                    hide c3
                    hide d3
                    with dissolve

                    "..."

                    scene blk with dissolve

                    "..."

                    "After this, the group always pays more attention to what [d] has to say and will take the initiative to ask [chars[3][4]] what [chars[3][2]] thinks."
                    "[d] gradually settles into the group and is able to talk more confidently."

                    "You become very good friends."

                    "Good job! You've made every choice right."

                    "Hope you make good decisions as well in the rest of the stories."



                else:
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"I'm not sure...I don't think they will pay attention to it, so it might be better to keep it just between us...\""

                    pov "{image=phone.png}\"Never mind! It's all up to you. Thank you anyway!\""
                    voice "/audio/msg.mp3"
                    d "{image=phone.png}\"You are welcome.\""

                    "..."

                    scene blk with dissolve

                    "..."

                    call final from _call_final_3

                    "..."

                    scene drm with dissolve

                    show a3 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 400
                    show b3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    show c3 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1400


                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Jesus, I just got 50...the teacher said I missed a big part!\""
                    voice "/audio/msg.mp3"
                    c "{image=phone.png}\"Me too! Why?? We should have found them all!\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"I don't understand, I'll talk to him.\""

                    "You didn't say anything, so as [d]..."

                    scene blk with dissolve

                    "..."

                    "..."

                    scene drm with dissolve

                    "The next day."

                    show a3 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"I just asked the professor about our diagram.\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"He said we all missed relapse part, but you and [d] did not??\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"Why you didn' tell us??\""

                    pov "{image=phone.png}\"Calm down, calm down. [d] told me about this but I'm not sure it's right or not, so...\""
                    voice "/audio/msg.mp3"
                    a "{image=phone.png}\"We could discuss about it, right?\""

                    pov "{image=phone.png}\"My bad, I'll tell you next time, I promise.\""

                    pov "If you had listened to [chars[3][4]] before..."

                    scene blk with dissolve
                    hide a3 with dissolve

                    "..."

                    "After this, nothing has changed among the group."

                    "You are the only one who talk to [d], and [chars[3][2]] doesn't really fit in with the group."

                    "You are still the same."

                    "Not bad! You become a friend of [d], but maybe you can do it better, can't you?"

                    "Let's try it again!"

                    "..."

                    jump rethirdstory


            "That's fine, they will not even thank [chars[3][4]] if we tell them about this.":

                call final from _call_final_4

                "..."

                scene drm with dissolve

                "..."

                show a3 at center:
                    xzoom -0.4 yzoom 0.4
                    xpos 400
                show b3 at center:
                    xzoom 0.4 yzoom 0.4
                    xpos 1000
                show c3 at center:
                    xzoom 0.4 yzoom 0.4
                    xpos 1400
                with dissolve
                voice "/audio/msg.mp3"
                b "{image=phone.png}\"Jesus, I just got 50...the teacher said I missed a big part!\""
                voice "/audio/msg.mp3"
                c "{image=phone.png}\"Me too! Why?? We should have found them all!\""
                voice "/audio/msg.mp3"
                a "{image=phone.png}\"I don't understand, I'll talk to him.\""

                "You didn't say anything, so as [d]..."

                "..."

                scene blk with dissolve

                "..."

                scene drm with dissolve

                "The next day."

                show a3 at center with dissolve:
                    xzoom 0.4 yzoom 0.4
                    xpos 1000
                voice "/audio/msg.mp3"
                a "{image=phone.png}\"I just asked the professor about our diagram.\""
                voice "/audio/msg.mp3"
                a "{image=phone.png}\"He said we all missed the relapse phase, but you and [d] did not??\""
                voice "/audio/msg.mp3"
                a "{image=phone.png}\"Why you didn' tell us??\""

                pov "{image=phone.png}\"Calm down, calm down. [d] told me about this but I'm not sure it's right or not, so...\""
                voice "/audio/msg.mp3"
                a "{image=phone.png}\"We could discuss about it, right?\""

                pov "{image=phone.png}\"My bad. I'll tell you next time, I promise.\""

                pov "If you had listened to [chars[3][4]] before..."

                "..."

                scene blk with dissolve

                "After this, nothing has changed among the group."

                "You are the only one who talk to [d], and [chars[3][2]] doesn't really fit in with the group."

                "Not bad! You become a friend of [d], but maybe you can think about how to help [d] become friends with other people in the group, can't you?"

                "Let's try it again!"

                "..."

                jump rethirdstory

                return








    return

label fourthstory:
    #language
    "Chapter Four"
    $ chars=generatechar(3)

    python:
        chars=generatechar(3)
        ex4= [[] for i in range(3)]
        for i in range(3):
            ex4[i] = generatecharimage(chars[i])
    image a4 = Composite(
        (300, 175),
        (-1240, -1754), "[ex4[0][3]]",
        (-1240, -1754), "[ex4[0][0]]",
        (-1240, -1754), "[ex4[0][1]]",
        (-1240, -1754), "[ex4[0][2]]")
    image b4 = Composite(
        (300, 175),
        (-1240, -1754), "[ex4[1][3]]",
        (-1240, -1754), "[ex4[1][0]]",
        (-1240, -1754), "[ex4[1][1]]",
        (-1240, -1754), "[ex4[1][2]]")
    image c4 = Composite(
        (300, 175),
        (-1240, -1754), "[ex4[2][3]]",
        (-1240, -1754), "[ex4[2][0]]",
        (-1240, -1754), "[ex4[2][1]]",
        (-1240, -1754), "[ex4[2][2]]")



    define a = Character("[chars[0][5]]")
    define b = Character("[chars[1][5]]")
    define c = Character("[chars[2][5]]")

    define x = 0

    label refourthstory:

    $ x = 0

    scene drm with dissolve


    "You live in a student residence hall with three other roommates."

    scene ktc with dissolve

    "Although you have a single room, you four share bathroom, toilet and kitchen. The four of you usually hangout and chat in the common areas."

    show a4 at center:
        xzoom -0.4 yzoom 0.4
        xpos 400
    show b4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show c4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    with dissolve

    "Your room is the farthest from the entry, [a]'s room is next to yours, then [b]'s, and finally [c]'s."

    "One day, after dinner, the four of you sit in the sofa and chat together."

    show b4 at shaking

    b "Have you ever heard about Supercall's new game? It looks so cool!"

    pov "Oh really? I've seen its advertisement before and it was quite interesting."

    show b4 at shaking

    b "Yes! We can play it next week. Let's do it together!"

    pov "Sure, how about you two?"

    show a4 at speaking

    a "It sounds interesting, but we both need to work on our group work you know, maybe we can play again after we finish the due?"

    show c4 at speaking

    c "It's reaaaaally hard, I'm so jealous you didn't take this course."

    show b4 at shaking

    b "Haha! This is where the importance of ratemyprofessor.com comes into play."

    pov "Well, actually my course is kind of hard too. Tt's all about medication and I know nothing about it!"

    pov "I'm particularly scared of it now for the assigned homework this week. I might have to spend ages on it."

    show a4 at speaking

    a "So why on the earth did you register for that?"

    pov "I thought it would be an easy course but I was wrong."

    show b4 at speaking

    b "God bless you bro."

    show a4 at speaking

    a "Speaking of which, were you singing in the room yesterday?"

    pov "Oops, you heard that? Sorry. I don't mean to disturb you."

    show a4 at speaking

    a "Oh no worries. The soundproof sucks here. You really are good at singing. I really enjoyed it."

    show c4 at shaking

    c "Wow, I want to hear you sing! Come on!"

    pov "Wait, hold on hold on...this is unexpected."

    show b4 at speaking

    b "Come on! Don't be such a disappointment! This is your stage, please."

    pov "Alright alright..."

    scene blk with dissolve

    "..."
    scene ktc with dissolve

    "..."

    "Same time a week later"

    show a4 at center:
        xzoom -0.4 yzoom 0.4
        xpos 400
    show b4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show c4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    with dissolve

    pov "Hey [b], I can't play that game tomorrow. My professor just assigned a new homework, and I have totally no idea on how to do it."

    show b4 at speaking

    b "No worries. I've asked some of my friends to join me and I'll definitely carry you when you're done with your homework."

    pov "Sounds great. Sorry about blowing off again."

    show a4 at speaking

    a "Now it's your turn! We're almost done."

    pov "Nooooo!"

    scene blk with dissolve

    "..."

    scene ktc with dissolve

    "The next day."

    show a4 at center:
        xzoom -0.4 yzoom 0.4
        xpos 600
    show c4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1200
    with dissolve

    "After dinner, you went back to the dormitory, but [b] is not in the kitchen as usual."

    pov "Where is [b]?"

    show c4 at speaking

    c "Flew back to the room right after the dinner."

    show b4 at center,shaking:
        xzoom 0.2 yzoom 0.2
        xpos 1800 alpha 0.5
    with dissolve

    b "{size=-10}...watch out!...{/size}"

    show a4 at speaking

    a "*Sigh Now you hear [chars[1][4]]. That game seems so attractive."

    pov "I want to try that too...I need to hurry up."

    show a4 at speaking

    a "Good luck dude. I've heard [chars[1][4]] screaming in the house all day. I'm even tempted to give it a go."

    pov "Stop seducing me. I can't resist it!"

    show b4 at shaking

    b "{size=-10}.....good job!......{/size}"

    a "Haha alright, do your homework then."

    pov "Roger that sir."

    show b4 at shaking

    b "{size=-10}......kidding me? What the ...... are you doing??...{/size}"

    "You shrug at them and walk back to your room."

    scene blk with dissolve

    "..."

    scene drm with dissolve

    "..."

    "12p.m."

    show a4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Holy moly...you're still playing the game.\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"I remember you have class tomorrow morning, right?\""

    scene blk with dissolve

    "..."

    scene drm with dissolve

    "Next day, you find they were chatting after you went to sleep."

    "1 a.m."

    show b4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 600
        alpha 1
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Come on! I just started to play this game. There are a lot to catch up on.\""

    show a4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1200
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"...OK...But if you spend that time studying, you wouldn't fail the course.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Don't be so mean *Cry\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"G9, I'll get back to playing!\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"*Sigh I hope I could I have a g9...\""

    hide b4
    hide a4
    with dissolve

    pov "Why is [a] up this late? It's not like [chars[0][4]]."

    "You whisper and mutter."

    scene blk with dissolve

    "..."

    scene ktc with dissolve

    "After washing up, you walk out of the room. There only are [a] and [c] having their breakfast."

    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 600
    show c4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1200


    pov "Morning! Did [b] go to school already?"

    show a4 at speaking

    a "*Yawn Maybe [chars[1][2]] is still dreaming about [chars[1][3]] game."

    pov "Really? What time did [chars[1][2]] sleep yesterday?"

    show a4 at speaking

    a "After 3 a.m.? I'm not sure...*Yawn It wouldn't be very early anyway."

    pov "Jesus, it's crazy."

    show c4 at speaking

    c "Who says it isn't?"

    scene blk with dissolve

    "..."

    scene ucr with dissolve

    "After the breakfast, [b] still doesn't show up, so you go to school without [chars[1][4]]."

    "12 p.m."

    show b4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 600
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Jeez, I've slept in!\""

    pov "{image=phone.png}\"Good morning! How is your course?\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Let me check...\""

    "..."
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Oh shoot, my professor has called the roll!!\""

    show a4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1200
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Congrats.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"And I supposed to turn in my homework in the class!!\""

    pov "{image=phone.png}\"You have to pray that the professor is still at school.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"GTG\""

    pov "{image=phone.png}\"Good luck lol\""

    scene blk with dissolve

    "..."

    scene ktc with dissolve
    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 400
    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show c4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    "At dinner, you four sit together."



    pov "Did you find the professor?"

    show b4 at speaking

    b "Thank god yes, but the professor said it's the last time, so if I do it again I maybe fail the course..."

    show c4 at speaking

    c "Can I say you deserve it?"

    b "Well..."

    pov "So how about the game? "

    show b4 at shaking

    b "Wonderful! I haven't been such excited for years. Supercall is the god! "

    show a4 at speaking

    a "Then are you gonna play all night today?"

    show b4 at speaking

    b "Won't be that long, but I don't have to get up early tomorrow, so I need to take the chance!"

    show a4 at speaking

    a "Well, I have to though. *Yawn"

    pov "You look so sleepy. Why you sleep that late yesterday? "

    show a4 at speaking

    a "*Sigh Not a big deal. Hope it won't last too long... "

    "You don't quite understand, but you choose not to ask."

    "..."
    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
        linear 2 xoffset 2000

    "After the dinner, [b] rush to the room. And soon [chars[1][3]] voice come out again."

    scene blk with dissolve

    "..."

    scene drm with dissolve

    "Second day, you find them talking in the group chat very late again."

    "2:27 a.m."

    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 400
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Do your friends stay up at night too?\""

    "2:53 a.m."

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"They are not in UK lol, they just finished their dinner.\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Jeez I forgot that...I thought your friends were planning to skip school too.\""

    "3:09 a.m."
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"It was an accident! I didn't plan that.\""

    show c4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"So you planned to sleep just 4 hours yesterday?\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"I planned to catch up on sleep in class lol.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"But I was so tired that I forgot to set my alarm clock\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Why are you both awake. Don't you need to get up at morning?\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"You guess...\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Guess what?\""
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"g9\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"g9!\""

    hide a4
    hide b4
    hide c4
    with dissolve

    scene blk with dissolve

    "..."

    "You become more confused, but both [a] and [c] went to school, so you decide to ask them after dinner."

    "..."

    "However when you get home, [b] is the only one at home having [chars[1][3]] dinner in the kitchen. You decide to do your homework first, so you go back to your own room."

    scene drm with dissolve

    "Saturday, after you waking up, you find another chat."

    "1 a.m."

    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 600
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Come on dude, you know the soundproof here is not that great, right? @[b]\""

    "1:13 a.m."

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1200
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Oh sorry, did I disturb you?\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"It has been 3 days…\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Sorry I didn’t mean to do that. You should tell me in the first day!\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"I thought it won’t last too long…\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"I’m not trying to stop you from playing, but you screamed so loud…\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Got that. I will definitely pay attention to that, sorry bro.\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"It’s ok, I know you didn’t mean to it.\""

    hide a4
    hide b4
    with dissolve

    pov "Oh…that’s it, I finally got it…"

    pov "It’s good to see them have solved it peacefully though..."

    "So you decide to focus on your homework for now."

    scene blk with dissolve

    "..."

    scene ktc with dissolve

    show a4 at center:
        xzoom -0.4 yzoom 0.4
        xpos 600

    show c4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1200
    with dissolve

    "You used all your weekend to finish your homework. Now you finally have time to chat with your roommates."

    "As \"usual\", [b] does not join you, you decide to "

    menu:

        "Do some small talk.":
            "You talk about your daily life as before, mostly about your courses."



        "Talk about the chat that night.":
            $ x+=1
            pov "I saw your chat on Friday night. How's it going on?"

            show a4 at speaking

            a "Just like I said, [chars[1][2]] was so noisy at night, and I could barely sleep those days."

            show a4 at speaking

            a "I thought it would be just first one or two days after that game releasing, but [b] kept screaming, so I had to tell [chars[1][4]]."

            pov "Well...that must had been a hard time. I'm also very sensitive to noise. Luckily I don't live next to [chars[1][4]]..."

            show a4 at speaking

            a "That's so terrible...you will never know when [chars[1][2]] would suddenly fright you!"

            pov "So what's the situation now?"

            show a4 at speaking

            a "Much better...at least [chars[1][2]] will not yell all the time, but [chars[1][2]] still screams sometimes when [chars[1][2]] gets excited. So I still have hard time sleeping, occasionally."

            pov "Haha...how about [c]? Don't you have this problem?"

            show c4 at speaking

            c "Not as bad. But it is still a little bit annoying...I can't totally ignore that though."

            pov "Oh no that's bad. Hope you both sleep well in the future."

            show a4 at speaking

            a "I wish I could...We have an exam on Friday morning, we need to rest well..."

            "After this conversation, you chat for a while and then go back to your rooms."

    scene blk with dissolve

    "..."

    "Nothing much happened during this time, you live your lives as usual."

    "Until Friday."

    scene drm with dissolve

    "0 a.m."

    show a4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    voice "/audio/msg.mp3"
    a "{image=phone.png}\"@[b] Dude I told you we have exam tomorrow right? And you said you won't play today.\""

    show b4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 400
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"I didn't want to play, but my friends kept asking me to join them and I was doing my best not to make a sound...\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Please try harder.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Alright.\""
    hide a4
    hide b4
    with dissolve

    "2:15 a.m."

    show c4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"I've had enough of this. Is it so hard not to disturb others?\""
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"You don't know how to keep your word?\""
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"I'm ashamed to be in a school with people like you.\""

    "..."

    hide c4
    hide a4
    hide b4

    "..."

    "There's a lot more left, all of which is [c] speaking to [b]."

    "You are scared, right now, you decide to:"

    menu:
        "Keep quiet.":
            "You think you'd better not get involved in the conflict, so you say nothing."

        "Talk to [b].":

            $ x+=1

            "You send a message to [b] and ask [chars[1][4]] what happened, but apparently [chars[1][2]] is still sleeping at this time, so you wash up first and have a breakfast."

            scene ktc with dissolve

            show a4 at center:
                xzoom -0.4 yzoom 0.4
                xpos 600
            show c4 at center:
                xzoom 0.4 yzoom 0.4
                xpos 1200
            with dissolve

            "You go to the kitchen and find that [a] and [c] have already finished their meal and are cleaning up, and they look very sleepy."

            show a4 at speaking

            a "Morning, we need to go, see you at dinner."

            pov "Oh, yes, see you."

            show c4 at speaking

            "[c] waves to you and leaves."

            hide a4
            hide c4
            with dissolve

            pov "They are going to take the exam. Guess I'll just have to wait for [b] to wake up..."

            scene blk with dissolve

            "..."

            "..."

            scene drm with dissolve

            "Around mid day"

            show b4 at center with dissolve:
                xzoom 0.4 yzoom 0.4
                xpos 1000
            voice "/audio/msg.mp3"

            b "{image=phone.png}\"IDK actually...I didn't make much noise last night for sure...\""

            pov "{image=phone.png}\"But [c] looked totally pissed off...\""
            voice "/audio/msg.mp3"
            b "{image=phone.png}\"I have no idea! [c] have never told me about this!\""
            voice "/audio/msg.mp3"
            b "{image=phone.png}\"It's always [a]. I thought [c] didn't care about this.\""

            pov "{image=phone.png}\"Maybe [c] just didn't say it...and you pushed [chars[2][4]] too hard this time...\""
            voice "/audio/msg.mp3"
            b "{image=phone.png}\"You're right...but I'm sure I was very quiet yesterday. It's really hard for a person not to make any sound at all...\""

            pov "{image=phone.png}\"I was not there so I can't judge that...\""


        "Talk to [a] and [c].":
            $ x+=1

            scene ktc with dissolve
            "You take a look at the time and think [a] and [c] should have their breakfast right now, so you wash up quickly and go to the kitchen."
            show a4 at center:
                xzoom -0.4 yzoom 0.4
                xpos 600
            show c4 at center:
                xzoom 0.4 yzoom 0.4
                xpos 1200
            with dissolve

            "They are still eating, so you ask them directly."

            pov "What happened yesterday? You looked so angry."

            show c4 at speaking

            c "I was very angry. [a] had told [chars[1][4]] to keep quiet just for yesterday, and [chars[1][2]] had promised."

            show a4 at speaking

            a "But [chars[1][2]] still played for a long time and made plenty of noise."

            show c4 at speaking

            c "I was doing my best to stay calm, but [chars[1][2]] went too far."

            pov "I understand..."

            show a4 at speaking

            a "We got to go, we have an exam later."

            pov "OK, good luck."

            "..."

            scene blk with dissolve

            "..."

            menu:
                "I already know everything about this, the only thing I can do for now is waiting.":

                    scene drm with dissolve

                    "So you go back to your room and do your homework."



                "Maybe I should ask [b] about this.":

                    $ x+=1

                    scene drm with dissolve

                    "You send a message to [b] and ask [chars[1][4]] what happened, but apparently [chars[1][2]] is still sleeping at this time."

                    "So you go back to your room and start to do your homework."

                    "..."

                    "..."

                    "Around mid day"

                    show b4 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"IDK actually...I didn't make much noise last night for sure...\""

                    pov "{image=phone.png}\"But [c] looked totally pissed off...\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"I have no idea! [chars[2][2]] have never told me about this!\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"It's always [a]. I thought [c] didn't care about this.\""

                    pov "{image=phone.png}\"Maybe [c] just didn't say it...and you pushed [chars[2][4]] too hard this time...\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"You're right...but I'm sure I was very quiet yesterday. It's really hard for a person not to make any sound at all...\""

                    pov "{image=phone.png}\"I was not there so I can't judge that...\""

    scene blk with dissolve

    "..."

    scene ktc with dissolve

    show a4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    show c4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 1400
    with dissolve
    "Evening, you have dinner with [a] and [c]."

    show b4 at center with dissolve:
        xzoom -0.3 yzoom 0.3
        xpos 0
        linear 2 xoffset 400

    "Minutes later, [b] comes back from school, and starts to cook."

    show b4 at speaking

    b "Evening."

    "[b] looks awkward."

    pov "Evening, how's your school?"

    show b4 at speaking

    b "Not very good. I was so sleepy, maybe I should go to bed earier from today haha..."

    pov "Yeah, it's more healthy."

    show b4 at speaking

    b "Oh I'm so hungry. Let me see what I can eat tonight..."

    show b4 :
        xzoom 0.3 yzoom 0.3


    "[b] starts to cook [chars[1][3]] dinner."

    show a4 at speaking

    a "I finished. See you tomorrow."

    show c4 at speaking

    c "Me too. See ya."

    pov "Ah, oh, see you, good night."

    b "Good night."

    hide a4
    hide c4
    with dissolve

    "It seems that [a] and [c] don't want to stay around, and they leave very quickly."

    b "...*Sigh"

    "..."

    show b4 at speaking

    b "Well, I'll eat in my room."

    pov "Yeah, I'll go back then, bye."

    b "..."

    scene blk with dissolve

    "The vibe between your roommates is clearly not right, but they all go back to their rooms, so you can do nothing about it."

    "However, the situation has not improved after a week."

    show a4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"Hey [pov], I found a good resturant. You have to go with us tonight.\""

    pov "{image=phone.png}\"Sure, four of us?\""
    voice "/audio/msg.mp3"
    a "{image=phone.png}\"You, me and [c].\""

    pov "{image=phone.png}\"OK\""


    "Apprently they don't want to invite [b]."

    "..."

    scene ktc with dissolve

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1400

    "..."

    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 0
        linear 2 xoffset 400

    show c4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 0
        linear 2 xoffset 800
    "After a really good meal, you three go back to the kitchen."

    "[b] is having dinner."

    show b4 at speaking

    b "Where were you guys?"

    pov "We went to a new resturant. It's really delicious."

    b "Oh, great, I'll try it next time."

    "[b] looks a little bit depressed."

    scene blk with dissolve

    "..."

    "..."

    scene ucr with dissolve

    "School"

    show c4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"Wanna have lunch with us?\""

    pov "{image=phone.png}\"Yup, where are you?\""
    voice "/audio/msg.mp3"
    c "{image=phone.png}\"Ground floor of canteen, right hand side of the entrance.\""

    pov "{image=phone.png}\"Be right there.\""

    "..."

    scene uct with dissolve

    "At canteen, while you're serving the meal"

    show b4 at center,speaking with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    b "Yo, what's your lunch today?"

    pov "Just some pasta. How about you?"

    show b4 at speaking

    b "Nah, I don't know yet. You alone?"

    pov "No, [c] asked me to join them."

    show b4 at speaking

    b "...Alright, then I will eat alone."

    pov "Uh, see you tonight."

    scene blk with dissolve

    "..."

    scene ktc with dissolve

    "Another day"

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    "You're having a rest at kitchen with [b]."

    show a4 at center with dissolve:
        xzoom -0.4 yzoom 0.4
        xpos 0
        linear 2 xoffset 400

    "[a] opens the door"

    show a4 at speaking

    a "[pov] do you have any extra charge cables for JPhone? My devices are dead."

    pov "No, I only have an android device."

    show a4 at speaking

    a "Huhhh, I'll ask the guy next door."

    show a4 at center:
        xzoom 0.4 yzoom 0.4
        xpos 200
        linear 2 xoffset -600

    "[a] go out of the kitchen."

    show b4 at speaking

    b "...I have that cable, why don't [chars[0][2]] ask me?"

    pov "...No idea."

    scene blk with dissolve

    "..."

    scene drm with dissolve

    "And another day."

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Do anyone see my spoon? I put it on the table.\""

    pov "{image=phone.png}\"It's not there? I just saw it.\""
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"No, I didn't find it...\""

    scene blk with dissolve

    "..."

    scene drm with dissolve
    voice "/audio/msg.mp3"
    b "{image=phone.png}\"Oh I found it. It's under the sofa, weird.\""

    pov "Under the sofa? That's quite far from table..."

    pov "I just had dinner with [a] and [c]. There was no one else. Something like this shouldn't happen..."

    pov "....It shouldn't..."

    scene blk with dissolve

    "..."

    "..."

    scene uct with dissolve

    "Two weeks later."

    "You are having lunch with [b]."

    show b4 at center with dissolve:
        xzoom 0.4 yzoom 0.4
        xpos 1000

    "..."

    show b4 at speaking

    b "Don't you think they're a bit too childish?"

    show b4 at speaking

    b "They just refuse to talk to me."

    pov "I don't know what they want. We live in a same suite. By acting like this doesn't solve anything."

    show b4 at speaking

    b "And all of my stuff, don't you suspect them of doing it? That's so weird."

    pov "I'm not sure...At least you don't have the evidence..."

    show b4 at speaking

    b "But only they had the chance."

    show b4 at speaking

    b "They just want to isolate me, but it's impossible. I have you and it's two versus two, right?"

    pov "Haha, I hope it's better to be four together and without v.s."

    scene blk with dissolve

    "..."

    "A month later."

    "Although [b] is still eating and talking with you, it is clear that [chars[1][2]] is not as optimistic as [chars[1][2]] was before."

    "But still there's no any improvements between their relationships. In the opposite, things get even worse."

    "At this point, you think you should..."

    menu:
        "Do something for them.":
            "You can't just wait like this, so you decide to make some changes."

            "To solve this, you need to talk with all of them."

            "Who do you prefer to talk with first?"

            menu:
                "[b]":

                    scene drm with dissolve

                    "Whoever started the trouble should end it..."

                    pov "{image=phone.png}\"Are you OK?\""

                    show b4 at center with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Yeah, why?\""

                    pov "{image=phone.png}\"I'm just asking. Actually I want to talk to you about that thing.\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"Well...what happened? It's so sudden.\""

                    pov "{image=phone.png}\"It has been a month. I think there's nothing good to keep this way for all of us.\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"...Yes...\""

                    pov "{image=phone.png}\"..I want to help you, but we need to sort it out again.\""
                    voice "/audio/msg.mp3"
                    b "{image=phone.png}\"..Alright, let's find a place.\""

                    scene blk with dissolve

                    "..."

                    "..."

                    scene cps with dissolve

                    show b4 at center,speaking with dissolve:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000

                    b "So you know what happened at first right?"

                    pov "Yes, because of playing game at night?"

                    show b4 at speaking

                    b "It was [a] who always talked to me about that, but [c] never did, so I thought [a] was too sensitive, and I didn't care about it much."

                    show b4 at speaking

                    b "I thought it was fine until that night. I just played the game, and I swear I was not making noises."

                    pov "I don't know how they felt...but maybe you should stop playing just for that night?"

                    show b4 at speaking

                    b "And I think I did do it wrong."

                    pov "Have you apologised to them?"

                    show b4 at speaking

                    b "No, I have no opportunity at all. They don't talk to me."

                    pov "Alright..maybe I could talk to them and find a way to solve this."

                    show b4 at speaking

                    b "Thank you."

                    pov "That's what friends for, right?"

                    show b4 at speaking

                    b "Sure."

                    scene blk with dissolve

                    "..."

                    "..."

                    scene ktc with dissolve
                    show a4 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200
                    show c4 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 600
                    with dissolve

                    "Evening, after the dinner, you sit on the sofa with [a] and [c]."

                    pov "I talked with [b] today."

                    show a4 at speaking

                    a "About What?"

                    pov "Err, about that thing you know."

                    show a4 at speaking

                    a "Oh, then? What did [chars[1][2]] say?"

                    pov "Well, [chars[1][2]] said [chars[1][2]] didn't realise at that time what trouble [chars[1][2]] was causing you."

                    pov "And [chars[1][2]] wouldn't have done that if [chars[1][2]]'d known."

                    pov "[b] knows [chars[1][2]] was wrong, and [chars[1][2]] would like to apologise to you, but you haven't give [chars[1][4]] a chance."

                    show c4 at speaking


                    c "Did [chars[1][2]] really say that?"

                    pov "Yeah, of course, face to face."

                    show c4 at speaking

                    c "Well, I didn't expect that. But if it's [chars[1][3]] real thought so, I can give it a try. How about you?"

                    show a4 at speaking

                    a "I had thought [chars[1][2]] had no intention of repenting at all...Since that's what [chars[1][2]] thinks, I agree."

                    pov "Wonderful! Let's get some time together and talk?"

                    show c4 at speaking

                    c "OK."

                    show a4 at speaking

                    a "En."

                    scene blk with dissolve

                    "..."

                    "..."

                    scene ktc with dissolve

                    pov "Well, we're all here."

                    show a4 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1400
                    show c4 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1000
                    show b4 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 400
                    with dissolve


                    "The second day, all of you are sitting around the table."

                    show b4 at speaking

                    b "It has been a long time huh."

                    show a4 at speaking

                    a "Who says it isn't?"

                    show c4 at speaking

                    c "Alright, let's get to the point."

                    show b4 at speaking

                    b "...Yes, so thank you for giving me this chance. And I have to apologise to you two."

                    show b4 at speaking

                    b "I didn't know how annoying I was, and I'm really sorry for what I did. I hope you can forgive me."

                    show c4 at speaking

                    c "Now that you've apologised, of course we're willing to forgive you. But also we need to say sorry to you."

                    show a4 at speaking

                    a "Yes, we know we also did something wrong to you. Whatever the reason, I'm sorry."

                    scene blk with dissolve

                    "..."

                    "..."

                    "Finally, all the people in this room become friends again."

                    "Well done! You saved your friendship and helped all of them."

                    return


                "[a] and [c]":

                    pov "First I have to get [a] and [c] to be willing to talk..."

                    scene ktc with dissolve

                    show a4 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1200
                    show c4 at center:
                        xzoom -0.4 yzoom 0.4
                        xpos 600
                    with dissolve

                    "Evening, after the dinner, you sit on the sofa with [a] and [c]."

                    pov "So you're still not going to forgive [chars[1][4]]?"

                    show a4 at speaking

                    a "Why should I? [b] doesn't deserve it."

                    pov "Is that serious?"

                    show a4 at speaking

                    a "Yes. You know what happened, right?"

                    pov "Because of playing game at night?"

                    show a4 at speaking

                    a "Yes, and [chars[1][2]] kept doing that after I had told [chars[1][4]] lots of times."

                    pov "En..."
                    show c4 at speaking
                    c "Actually that's not the point."

                    pov "What?"

                    c "What I can't tolerate is [chars[1][3]] attitude. [b] didn't care what we said at all."

                    c "And [chars[1][2]] has no remorse at all. [b] doesn't think that [chars[1][2]] was wrong."

                    show a4 at speaking

                    a "Till this day [chars[1][2]] has not apologised to us. this is the point."

                    show a4 at speaking

                    a "So we'll not forgive [chars[1][4]]."
                    show c4 at speaking
                    c "Just in case, did [chars[1][2]] say that [chars[1][2]] think [chars[1][2]] was wrong?"

                    pov "..."

                    "You reminisce for a moment."

                    pov "No..."
                    show c4 at speaking
                    c "Then I have nothing else to say. We can't get along with such a person."
                    show c4 at speaking
                    c "And I think you should drop the matter and leave it to us."

                    pov "Huh..."

                    scene blk with dissolve

                    "..."

                    "..."

                    "Are you going to listen to [chars[2][4]]?"

                    menu:
                        "Just leave it to them.":

                            "It was [b] who made the mistake in the first place, so [chars[1][2]] should have taken the initiative to deal with it."

                            jump leave

                        "Tell [b]":

                            scene drm with dissolve

                            "After the chat, you stay at your room."

                            pov "No, if I leave it to them, they will never get back again..."

                            pov "{image=phone.png}\"Hi. I have to tell you something.\""

                            show b4 at center with dissolve:
                                xzoom 0.4 yzoom 0.4
                                xpos 1000
                            voice "/audio/msg.mp3"
                            b "{image=phone.png}\"What's up?\""

                            "..."

                            "You tell [chars[1][4]] your conversation with [a] and [c]."

                            pov "{image=phone.png}\"So they are waiting for your apology I think...\""
                            voice "/audio/msg.mp3"
                            b "{image=phone.png}\"Are they serious? They were the ones who didn't talk to me.\""
                            voice "/audio/msg.mp3"
                            b "{image=phone.png}\"No way my friend. I know you did it for me, but they do not deserve it.\""
                            voice "/audio/msg.mp3"
                            b "{image=phone.png}\"They isolated me, and they even threw my stuff everywhere. And now they're blaming me?\""
                            voice "/audio/msg.mp3"
                            b "{image=phone.png}\"Listen, just leave it, they are unreasonable.\""

                            "..."

                            menu:
                                "Try one more time.":
                                    pov "{image=phone.png}\"Come on! You know they just talked tough, right?\""

                                    if (x >=2):

                                        "..."
                                        voice "/audio/msg.mp3"
                                        b "{image=phone.png}\"I'll think about it.\""

                                        scene blk with dissolve

                                        "..."

                                        "..."
                                        scene drm with dissolve

                                        "One day, you feel a little bit hungry when you are studying."

                                        "So you decide to get some snacks from fridge."

                                        "You take off the headphones, but before you open the door, you faintly hear some people speaking."

                                        show b4 at center with dissolve:
                                            xzoom -0.3 yzoom 0.3
                                            xpos 400 alpha 0.5

                                        b "{size=-10}...so I apologise....{/size}"

                                        show a4 at center with dissolve:
                                            xzoom 0.3 yzoom 0.3
                                            xpos 1000 alpha 0.5

                                        a "{size=-10}.....we need to say sorry to......{/size}"

                                        show c4 at center with dissolve:
                                            xzoom 0.3 yzoom 0.3
                                            xpos 1400 alpha 0.5

                                        c "{size=-10}.......should have found a better........{/size}"

                                        "..."

                                        hide a4
                                        hide b4
                                        hide c4
                                        with dissolve

                                        "Somehow You feel really relieved."

                                        pov "Finally..."

                                        "You sit back, and a moment later."

                                        show b4 at center with dissolve:
                                            xzoom 0.4 yzoom 0.4
                                            xpos 1000 alpha 1
                                        voice "/audio/msg.mp3"
                                        b "{image=phone.png}\"Hi, I talked to them, and we're good now.\""

                                        pov "{image=phone.png}\"Really?? Oh my god that's awesome!\""

                                        pov "{image=phone.png}\"We can finally play togeter again.\""
                                        voice "/audio/msg.mp3"
                                        b "{image=phone.png}\"Yes, and it all thanks to you.\""

                                        pov "{image=phone.png}\"No, you did it yourself. Good job.\""

                                        scene blk with dissolve

                                        "..."

                                        "..."

                                        "Finally, all the people in this room become friends again."

                                        "Well done! You saved your friendship and helped all of them."

                                        return



                                    else:
                                        voice "/audio/msg.mp3"
                                        b "{image=phone.png}\"I have decided.\""

                                        pov "{image=phone.png}\"Alright...\""

                                        scene blk with dissolve

                                        "..."

                                        "..."

                                        "After this, they become even worse."

                                        "You can't continue to live with them anymore."

                                        "So you decide to move out."

                                        "[b], [a], [c] and you become strangers."

                                        "..."

                                        "Oops, it does not look great...Maybe you need to change your strategy."

                                        "Let's try it again!"

                                        "..."

                                        jump refourthstory

                                "Alright":

                                    pov "{image=phone.png}\"OK, I got it, if you insist.\""
                                    voice "/audio/msg.mp3"
                                    b "{image=phone.png}\"Thank you, but I can handle it.\""

                                    pov "{image=phone.png}\"Alright...\""

                                    scene blk with dissolve

                                    "..."

                                    "..."

                                    "After this, they become even worse."

                                    "You can't continue to live with them anymore."

                                    "So you decide to leave here."

                                    "[b], [a], [c] and you become strangers."

                                    "..."

                                    "Oops, it does not look great...Maybe you need to change your strategy."

                                    "Let's try it again!"

                                    "..."

                                    jump refourthstory

        "Leave their problems themselves.":

            "It's a conflict between them, and it was [b] who did the wrong thing first. So it's reasonable for [a] and [c] to do such a thing to [b]."

            "And their conflict does not impact your relationships with all of them, so it's totally alright to keep this way."

            "Or you thought it will keep this way."

            "..."

            call psy from _call_psy

            "What should you do?"

            menu:
                "The counselor must be able to solve [chars[1][3]] problems better than I can. There is no need for me to intervene anymore.":

                    label leave:

                        "Two days later."

                        scene drm with dissolve

                        "In the morning, when you are still asleep, you faintly hear the sound of someone moving something outside."

                        pov "Who is moving things around?"

                        "You don't care too much about it. Maybe it won't last for long."

                        "..."

                        scene blk with dissolve

                        "..."

                        "However, it lasts for over half an hour, and you can't fall asleep again due to the noise."

                        scene drm with dissolve

                        "So you have to get up, and go out to check."

                        scene ktc with dissolve

                        pov "What are you doing?"

                        show b4 at center with dissolve:
                            xzoom 0.4 yzoom 0.4
                            xpos 1000

                        "Surprisingly, you find [b] is moving [chars[1][3]] stuff out."

                        show b4 at speaking

                        b "Oh, morning. Did I wake you up?"

                        pov "No, I just heard the sound and come to check. So..?"
                        show b4 at speaking
                        b "Ehh, just as you can see, I'm gonna leave here."

                        pov "Leave? Why?"
                        show b4 at speaking
                        b "...Clearly there is no place for me here anymore. It's not your fault, and I have to thank you for the last month, or I would not have been able to stand it any sooner."

                        pov "You don't have to leave. We can solve this."
                        show b4 at speaking
                        b "I have talked with my therapist, and she said I should change my environment as soon as possible."

                        pov "..."

                        pov "Sorry."
                        show b4 at speaking
                        b "Why do you have to apologise, you did nothing wrong."

                        pov "I could have done better. Let me help you with these."
                        show b4 at speaking
                        b "Thank you my friend."

                        scene blk with dissolve

                        "..."

                        "You really regret it, but what you can do to change it..?"

                        "Let's try it again."

                        "..."

                    jump refourthstory

                "No matter what, [chars[1][2]] is in need. I should do something for [chars[1][4]].":

                    "So you send messages to [a] and [c] to talk."

                    scene cps with dissolve

                    show a4 at center,speaking:
                        xzoom -0.4 yzoom 0.4
                        xpos 600

                    show c4 at center:
                        xzoom 0.4 yzoom 0.4
                        xpos 1400
                    with dissolve
                    a "What happened? Why can't we just stay in the suite and talk?"

                    pov "I think there's something wrong with [b]. I saw [chars[1][4]] went to the therapist."

                    show c4 at speaking

                    c "Wow, that really surprised me."

                    pov "I think what happened hurt [b]. We need to do something about it."
                    show c4 at speaking
                    c "There's a reason for us to do this to [chars[1][3]]."
                    show a4 at speaking

                    a "Yes, you know that at first, we, or I discussed with [chars[1][4]] very gentle, right? But [chars[1][2]] didn't listen to me."
                    show a4 at speaking
                    a "I talked with [chars[1][4]] about it twice or three times? And [chars[1][2]] never cared about it."
                    show a4 at speaking
                    a "After that night, [chars[1][2]] didn't apologise to us either, and [chars[1][2]] didn't even take it personally."
                    show a4 at speaking
                    a "That's the point really pissed us off. And so we did something to [chars[1][4]]."
                    show c4 at speaking
                    c "We know that we may do it too far, but it's all because of [chars[1][4]]."

                    pov "Yeah...But [chars[1][2]]'s not in good condition right now. I'm afraid that something irreversible will happen if this situation continues..."
                    show c4 at speaking
                    c "Huh...But still, if [chars[1][2]] has no remorse whatsoever, we don't know how to get along with [chars[1][4]]."
                    show c4 at speaking
                    c "However, If [chars[1][2]] could apologise to us, then we will do it as well for what we did. Is that reasonable?"

                    pov "I agree. It's good for all of us. So I will talk to [chars[1][4]] about it tomorrow. I hope we could be friends as we used to be."
                    show a4 at speaking
                    a "I hope so."
                    scene blk with dissolve

                    "..."

                    jump leave



    label psy:

        scene cps with dissolve


        "One day, you are on your way home."

        show b4 at center:
            xpos 1000
            xzoom -0.2 yzoom 0.2
            linear 5 xoffset 2000

        "You notice [b] walk out of a building, but not the building where [chars[1][3]] classroom is."

        pov "What's that building for? [chars[1][2]] is not a person to hang around."

        "You walk closer, and find the Psychological Consultation Room written next to the front door."

        pov "..Psychological consultation? What's going on?"

        "You are not sure if [chars[1][2]] came here to consult, or if it's about that problem."

        scene blk with dissolve

        "..."

        scene ktc with dissolve

        "..."

        show b4 at center:
            xpos 1000
            xzoom 0.4 yzoom 0.4

        "When you back to dorm, [b] is just like usual."

        "However, you can not ask [chars[1][4]] about the detail, since it is a private matter."

        scene blk with dissolve

        "..."

    return


init:
    transform shaking:
        linear 0.1  yoffset 6
        linear 0.1  yoffset -8
        linear 0.1  yoffset -6
        linear 0.1  yoffset 8
        linear 0.1  yoffset 0

    transform speaking:
        linear 0.1  yoffset 4
        linear 0.1  yoffset 0
        linear 0.1  yoffset 4
        linear 0.1  yoffset 0

init python:

    import os


    def generatecharimage(char):

        body = (fb if char[0] == 0 else mb) +str(char[1])+".png"
        clothes = (fc if char[0] == 0 else mc) + "c" + str(char[6]+1)

        my_file = clothes+"w"+".png"

        if renpy.exists(my_file):
            clothes = clothes + str(char[1])+".png"
        else:
            clothes += ".png"
        hair = (fh if char[0] == 0 else mh) + "h" + str(char[7]+1) +".png"
        my_file = (fh if char[0] == 0 else mh) + "h" + str(char[7]+1) + "b.png"
        if renpy.exists(my_file):
            hairb = my_file
        else:
            hairb = hair



        ex= ["","","",""]
        ex[0]=body
        ex[1]=clothes
        ex[2]=hair
        ex[3]=hairb


        return ex

    def generatechar(n):
        #0sex,1color,2heshe,3hisher,4himher,5name,6clothes,7hair
        #colors = ["y","w","bl","br"]
        colors = ["w","bl"]
        names = [["Amanda","Bella","Caroline","Daisy","Eileen","Flora","Grace","Hannah","Jane","Kelly","Laura","Marry","Nancy","Olina","Polly","Quentina","Rachel","Sara"],
                ["Alex","Bert","Carl","David","Elliot","Felix","George","Henry","John","Kevin","Leo","Max","Nick","Owen","Paul","Quentin","Ron","Sean"]]

        char= [[] for i in range(n)]
        for i in range(n):
            sex = renpy.random.randint(0,1)
            color = renpy.random.randint(0,len(colors[sex])-1)
            name = renpy.random.randint(0,len(names[sex])-1)
            clothes = renpy.random.randint(0,11)
            hair = renpy.random.randint(0,11)
            char[i].append(sex)
            char[i].append(colors[color])

            char[i].append(heshe[char[i][0]])
            char[i].append(hisher[char[i][0]])
            char[i].append(himher[char[i][0]])
            char[i].append(names[sex][name])
            char[i].append(clothes)
            char[i].append(hair)

            del names[sex][name]
        return char
