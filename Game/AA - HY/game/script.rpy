# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image splash = im.Scale("splash.png", 1024, 768)
image splash1 = im.Scale("splash1.png", 1024, 768)
image splash2 = im.Scale("splash2.png", 1024, 768)
image wright_anything_agency = im.Scale("waa.png", 1024, 768)

# Declare characters used by this game.
define s = Character('Siegfried Tobias', color="#c8ffc8")
define PA = Character('PA System' , color="#0B610B")
define c = Character('Catlyn Skye' , color="#3399FF")
define pw = Character('Phoenix Wright', color="0066FF")
define kw = Character('Karyn Wright' , color="3399FF")
define la = Character('Loyld Aspund', color="#909090")
define ec = Character('Elise Cykes', color="282828")
define MA = Character('Manager')



#the color means the color of their name as it appears in dialogue. make sure to distinguish colors! 




# The game starts here. 
label splashscreen:
scene black
with Pause(1)
play music "open.mp3"


show splash with dissolve
with Pause (3)

show splash1 with dissolve
with Pause (3)

show splash2 with dissolve
with Pause (4)

stop music

label start:

"Subway Car \n August 15th, 2014 \n 4:30 PM" 

s "I hope this compartment has been comfortable, yes?"

s "Oh, Excuse me for my intrusion. I am Siegfried Tobias, an associate of your father, Miles Edgeworth. Could I ask your name?"
$ pn = renpy.input("What's your name, player?")
$ pn = pn.strip()
if pn == "temp":
    $ pn ="Yamato"
else:
    s "It’s good to meet you %(pn)s We will be arriving in the States shortly. I will escort you to your living quarters upon arrival."
define m = DynamicCharacter("pn", color="#0174DF")
m "(I am %(pn)s. Edgeworth. My father, Miles Edgeworth, is an esteemed prosecutor and was formerly the High Prosecutor of the LAPD. My mother is Franziska von Karma, an equally talented prosecutor.  My parents both had to leave for Japan to investigate a smuggling ring. They sent me to live in the States with a friend of Father’s."
menu:
    "Stay in your Cabin":
        m "I will be attending a High School in this area after several days. I’ve only been to the States a few times. Usually to visit my Father’s friend, Phoenix Wright. I’ve heard that Mr. Wright and Father used to be fierce rivals in court. My mother likes to reminisce about the “Good old days” where she would whip Mr. Wright into submission. Geez, Mr. Wright must be a forgiving man. "
        PA "We have arrived in Chicago’s Union Station. This will be our final stop."
    "Head to the Dining Car":
        pass

m "(Well, Might as well get the final bit of free food out of this train before we get off.)"
#Need to add Dining Car FX
m "(This place is surprisingly empty, I guess everyone is packing their things before we come to a stop.)"
m "Could I get a Coffee. Black please."
#Need a catlyn skye

menu:
    "Attempt to talk to her":
        m "Hello there."
        c "Quiet, please. It's snack time."
        m "(Well that was rude. Why would you even come down here if you just wanted to eat snacks from your compartment?)"
        menu:
            "Attempt to continue conversing with her":
                m "So what brings you here?"
                c "Can't you see I'm trying to snack here? Idiot."
                m "(God damn, what a prick.)"
                m "What brings you to Chicago?"
                c "I’m attending Pravada Academy in the Fall. Now if you could please leave me to my snacking."
                m "Your parent’s must have a lot of influence if you’re attending Pravada."
                c "Pff. My mother is a world class detective. Not like a pleb like you would know. "
                m "(Who does she think shes calling a plebeian? Does she not see this fabulous cravat?)"
                menu:
                    "Continue to speak with her":
                        m "(Against my better judgement I have decided to continue conversing with her.)"
                        m "So who is your father?"
                        c "Pff. That filthy coxcomb. Always thinking he's a prince in the investigation... What a glimmerous fop!" 
                        c "MUNCH MUNCH MUNCH"
                        c "One time this guy got murdered during one of his concerts-"
                        c "MUNCH MUNCH MUNCH"
                        c "Also his brother got executed for murder. (MUNCH MUNCH MUNCH MUNCH) Serves that scumbag right for disbarring Mr. Wright . . ."
                        c "MUNCH MUNCH MUNCH"
                        m "(As much as I’d hate to leave this cup of coffee half empty she’s not going to stop anytime soon.)"
                        #FANCY TRAIN HALLWAY FX
                        m "(That woman... She said her father disbarred Mr. Wright and was a in a band. That can't mean...)"
                        m "Her father is Klavier Gavin!?!?"
                        "*Bag of snackoos falls to the ground*"
                        m "(Shit, I didn't say that outloud did I?)"
                        c "WHO ARE YOU? HOW DO YOU KNOW MY FATHER?"
                        m "Well, not that many people are both lawyers and singers..."
                        c "If you let anyone know he's my father. I'll slit your throat."
                        m "(Then what? Have him prosecute you? I get the feeling she really doesn't like her father.)"

                    "Leave with your sanity":
                         m "I really must be going."
                         c "Like I care."
                         m "We’ll arrive soon, you should probably head back to your compartment."
                         c "Don’t tell me how to live my life."
                         m "(Holy shit woman.)"
                         jump label_1
                    
            "Take the coffee and leave":
                "You decided to not waste any additional segments of your life conversing with this lady."
                jump label_1
    "Ignore her and keep drinking coffee":
        "You choose to ignore the lady who walked in and enjoy your coffee. Her loud obnoxious chewing deters you."
        jump label_1
label label_1:
     PA "We will be arriving in Chicago’s Union Station shortly. All passengers are to disembark here."
     #FANCY TRAIN STATION FX
     pw "Oi, Yamato, over here."
     #FANCY PHOENIX FX
     menu:
        "It's good to meet you.":
            pw "Ha, ha. It’s been a while. I trust your father has been well?"
            m "As fine as when he first started his career."
            jump label_2
        "Who are you again?":
            pw "I’m Phoenix Wright. A long time friend of your fathers. I trust I haven’t aged enough to be unrecognizable after five years."
            m "I apologize sir. I didn’t mean it that way."
            jump label_2
            
label label_2:
pw "Shall we get going? It’s still quite a drive back to my house. I’ll find us a taxi."
"Wright Anything Agency \n August 15th, 2014 \n 5:15 PM" 
scene wright_anything_agency
pw "It’s a bit cluttered here, but please, make yourself at home."
m "(Is that levitating pasta over there?)"
pw "I’ll have dinner ready soon. Feel free to explore my house, or agency."
#GET A ROOM FX
m "It’s smaller than what I was expecting, but it will do."
#FANCY FADE IN FADE OUT SOME TIME PASS THINGY
pw "Let’s eat."
"Yamoto and Phoenix settle down to eat."
pw "Your parents are overseas was it? Investigating some smuggling ring in Japan was it? Getting dragged all the way across the country because of your parents. It must suck being a kid."
pw "Well, as long as you’re stranded out here this will be your home. If you need anything, just ask."
menu:
    "Yessir":
        pass
    "Thank you for your kindness":
        pass
    ".....":
        jump label_3
pw "No need to be that formal. Ha ha."
jump label_3

label label_3:
pw "It’s just me and Karyn here. My wife went out to her hometown out west."
pw "Say hello Karyn."
kw " … Hello."
pw "She’s a bit shy around new people."
"News Reporter" "We have recently gotten report of the murder of Mr. Tim Burr, a wealthy businessman, in a small Chicago suburb. This was only the most recent murder in a string of murders. The police are still investigating whether these murders are related. For the time being, no suspect has been apprehended in association with any of these murders."
pw "These murders have had the local pendict in a frenzy. For the past four weeks, every tuesday, someone drops dead. I’m pretty sure if your father was over here he’d have the culprit apprehended and tried already. Ha ha…"
"You finish eating."
"After the long journey here you feel exhausted. You retire to your room for the night."
"END OF DAY ONE"
#FADE IN FADE OUT FX
"Wright Anything Agency \n August 16th, 2014 \n 8:15 AM"
"The start of a new day."
"You go downstairs for breakfast."
m "Oh, It’s just you Karyn?"
kw " Daddie is having an argument with Mommy over step ladders and ladders."
m "(She talks about that like it’s a regular occurrence.)"
menu:
    "Do you usually do the cooking around here?":
        kw "Usually Daddie brings something home. But I have to make breakfast because Daddie never wakes up in time."
        jump label_4
    "Can you cook anything else?":
        kw "Not really, Daddie usually brings something home for Dinner, but I can toast bread and cook eggs in the morning."
        jump label_4
    "…":
        pass
jump label_4

label label_4:
"Schools starts tomorrow. You decide to explore the town."
#Fancy Change HERE
"Lordly Taylor Department Store  \n August 16th, 2014 \n 10:15 AM"
m "(I didn’t know there would be such a high class department store in this place.)"
"You proceed to look around."
ec "Oi! Watch out!"
m "Er… Wha-OH SHIT!"
"Elise crashes her shopping cart into you."
m "(Oh god, ow.)"
m "Out of curiosity, how do manage to lose control of a shopping cart like that?"
ec "Oh my god. I’m so sorry. I’ll see if my manager can get you a coupon or something?"
m "(This airhead works here?!?!)"
ec "Could you come with me."
#FANCY OFFICE FX
"Lordly Taylor, Manager's Office  \n August 16th, 2014 \n 10:21 AM"
MA "What did you do this time Elise?"
ec "I kind of hit a customer with a shopping cart."
MA "Wait wait wait. YOU HIT A CUSTOMER WITH A SHOPPING CART?"
m "Oh, it could have been worse."
MA "You must be the poor chap who got struck with a cart."
MA "Here, take these. The manager has to take responsibility for her workers."
"You leave the room."
ec "I’m so sorry."
menu:
    "You better be sorry, punk.":
        ec "Sorry..."
    "It wasn’t that bad.":
        ec "You don’t need to sugarcoat it. I’m so clumsy this always happens."
    "How did you even get hired here?":
        ec "Er… I don’t really even know."
ec "Here, take this."
ec "We’re looking for part time work. If you have the time come down would ya?"
"It seems as if getting hit by  shopping cart distorted your sense of time. You decide to head home."
"Wright Anything Agency \n August 16th, 2014 \n 4:10 PM" 
kw "Welcome home."
m "Is your father not home?"
kw "*Sigh"
kw "He's out gambling again"
menu:
    "Wait...Gambling!?!":
        kw "Dad used to gamble a lot before I was born. Usually when he goes out to gamble he doesn’t return until the next morning."
        jump label_gambling
    "Oh, that's nice":
        pass
    "...":
        pass
jump label_gambling

label label_gambling:
kw "I have some water boiling. I’ll have some ramen ready soon."
m "(This reminds me of a certain subordinate of my father’s…)"
"You eat with Karyn"








         
     


    


return
