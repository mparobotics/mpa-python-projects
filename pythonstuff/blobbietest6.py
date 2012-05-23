from visual import *
import os.path
import math

# set window attributes
scene.width = 320
scene.height = 240
scene.fullscreen = 0

#charframe initialization
charframe = frame()
charbody = sphere(frame = charframe, pos=(0,0,0), radius=0.5)
charbody.color = (1,1,0)
charbody.type = 'char'
charlefteye = sphere(frame = charframe, pos=(0.19,0.1,.5), radius=0.12)
charlefteye.color = (0,0,0)
charlefteye.type = 'char'
charighteye = sphere(frame = charframe, pos=(-0.19,0.1,.5), radius=0.12)
charighteye.color = (0,0,0)
charighteye.type = 'char'

#initialization of the arms
charightarm = sphere(pos=(-0.6,0,.2), radius=0.2)
charightarm.color = (1,1,0)
charightarm.xvelo = 0
charightarm.yvelo = 0
charightarm.zvelo = 0
charightarm.restlength = 1.5
charightarm.springconstant = 0.02
charightarm.type = 'char'
charleftarm = sphere(pos=(0.6,0,.2), radius=0.2)
charleftarm.color = (1,1,0)
charleftarm.xvelo = 0
charleftarm.yvelo = 0
charleftarm.zvelo = 0
charleftarm.type = 'char'

#general initialization
charframe.y = 5
dir = 0
camdir = 0
blinktmr = 0
charframe.grav = 0
lowesty = 0

# set the scene attributes
scene.autocenter = 0
scene.autoscale = 0
scene.userzoom = 0
scene.userspin = 0
scene.scale = (10,10,10)
scene.ambient = 0.7
scene.background = (0,0,.65)

camxvelo = 0
camyvelo = 0
camzvelo = 0
camx = 0
camy = 0
camz = 0
cycle = 0
onground = 0
charframe.prevx = 0
charframe.prevz = 0
blockvector = (0,0,0)
mouserightpress = 0
mouseleftpress = 0
mousemiddlepress = 0
charframe.grab = 'none'
autocam = 1
pos = (1000,1000,1000)
charframe.xvelo = 0
charframe.zvelo = 0
level = 1


def loadlevel(levelnum):
    # levels hard-coded into memory
    if (levelnum == 1):
        levelbuffer = [(0.0, -4.0, 0.0), (1.0, -4.0, 0.0), (0.0, -4.0, -1.0), (1.0, -4.0, -1.0), (1.0, -2.0, -2.0), (1.0, 2.0, -2.0), (0.0, -2.0, -2.0), (0.0, -2.0, -3.0), (1.0, -2.0, -3.0), (1.0, 1.0, -4.0), (1.0, 1.0, -5.0), (1.0, 1.0, -6.0), (0.0, 1.0, -6.0), (0.0, 1.0, -7.0), (1.0, 1.0, -7.0), (2.0, 1.0, -7.0), (2.0, 1.0, -6.0), (-1.0, 1.0, -6.0), (-1.0, 1.0, -7.0), (-2.0, 1.0, -6.0), (-2.0, 1.0, -7.0), (-3.0, 1.0, -6.0), (-4.0, 1.0, -6.0), (-5.0, 1.0, -6.0), (-6.0, 3.0, -6.0), (-6.0, 3.0, -7.0), (-6.0, 3.0, -8.0), (-6.0, 3.0, -9.0)]
    if (levelnum == 2):
        levelbuffer = [(0.0, -4.0, 0.0), (1.0, -3.0, 0.0), (2.0, -2.0, -1.0), (2.0, -2.0, 1.0), (2.0, -2.0, 0.0), (3.0, -2.0, 1.0), (3.0, -1.0, 0.0), (3.0, 0.0, -1.0), (4.0, 0.0, -1.0), (4.0, 1.0, -2.0), (4.0, 4.0, -3.0), (4.0, 2.0, -4.0), (3.0, 3.0, -6.0), (2.0, 4.0, -6.0), (1.0, 5.0, -6.0), (1.0, 5.0, -5.0), (1.0, 5.0, -4.0), (1.0, 6.0, -3.0), (1.0, 7.0, -3.0), (1.0, 8.0, -3.0), (1.0, 9.0, -3.0), (1.0, 10.0, -3.0), (0.0, 6.0, -3.0), (1.0, 7.0, -2.0), (2.0, 8.0, -3.0), (1.0, 9.0, -4.0), (0.0, 9.0, -3.0), (0.0, 10.0, -2.0), (3.0, 12.0, -3.0)]
    if (levelnum == 3):
        levelbuffer = [(0.0, -4.0, 0.0), (0.0, -3.0, 0.0), (1.0, -3.0, 0.0), (1.0, -3.0, 1.0), (0.0, -3.0, 1.0), (1.0, -2.0, -1.0), (0.0, -2.0, -1.0), (0.0, 1.0, -2.0), (1.0, 1.0, -2.0), (2.0, -1.0, -3.0), (-1.0, 3.0, -3.0), (-1.0, 3.0, -4.0), (-1.0, 3.0, -5.0), (-1.0, 3.0, -7.0), (-1.0, 4.0, -7.0), (-1.0, 5.0, -7.0), (-1.0, 6.0, -7.0), (-1.0, 7.0, -7.0), (1.0, 4.0, -6.0), (-2.0, 5.0, -8.0), (-1.0, 4.0, -8.0), (0.0, 4.0, -8.0), (-1.0, 5.0, -6.0), (-2.0, 6.0, -7.0), (0.0, 10.0, -7.0), (0.0, 10.0, -8.0), (0.0, 10.0, -6.0), (1.0, 10.0, -6.0), (1.0, 10.0, -6.0), (1.0, 10.0, -7.0), (1.0, 9.0, -8.0), (1.0, 12.0, -8.0), (1.0, 8.0, -9.0), (2.0, 8.0, -8.0), (2.0, 6.0, -9.0), (3.0, 5.0, -9.0), (5.0, 7.0, -9.0), (8.0, 10.0, -8.0), (7.0, 8.0, -6.0)]

    # the actual loading of the level
    cycle = 0
    lowesty = 0
    levelinfo = []
    while (cycle < len(levelbuffer)):
        levelinfo.append(box(pos=(levelbuffer[cycle]), length=1, height=1, width=1))
        if not cycle == len(levelbuffer) - 1:
            levelinfo[cycle].color = (.6,.6,.6)
            levelinfo[cycle].type = 'block'
        else:
            levelinfo[cycle].color = (0,5,0)
            levelinfo[cycle].type = 'finish'
            
        if ((levelbuffer[cycle])[1]) < lowesty:
            lowesty = ((levelbuffer[cycle])[1])
        cycle = cycle + 1

    # return the loaded level
    return levelinfo, lowesty
        
totalevelinfo = loadlevel(level)
levelinfo = totalevelinfo[0]
lowesty = totalevelinfo[1] - 2
while 1:


    #COLLISION SCRIPTS


    onground = 0

    #Cycle through the blocks and find collisions
    cycle = 0
    while (cycle < len(levelinfo)):
        
        #calculate the vector from the character to the block and calculate the scalar of that. Since the scalar is the same as the distance, we can do a collision check using that.
        blockvector = (charframe.x - levelinfo[cycle].x, charframe.y - levelinfo[cycle].y, charframe.z - levelinfo[cycle].z)
        blockscalar = sqrt((blockvector[0])**2 + (blockvector[1])**2 + (blockvector[2])**2)
        
        # do a bounding sphere check using the above knowledge
        if (blockscalar < 1.2):
            # do a bounding box check
            if ((abs(blockvector[0]) < 1) and (abs(blockvector[1])<1) and (abs(blockvector[2])<1)):
                # find out if the collision is with a ceiling/floor or a wall
                charframe.x = charframe.prevx
                charframe.y = charframe.prevy
                charframe.z = charframe.prevz
                if abs(blockvector[1]) > .7:
                    # determine beetween a ceiling and a floor
                    if (charframe.y > levelinfo[cycle].y):
                        charframe.grav = charframe.grav * -.45
                        if charframe.grav < .05:
                            if not (abs(blockvector[0]) > .8 or abs(blockvector[2]) > .8):
                                onground = 1
                        charframe.y = levelinfo[cycle].y + 1.000
                    else:
                        charframe.grav = abs(charframe.grav) * -.6
                        charframe.y = levelinfo[cycle].y - 1.005
                if abs(blockvector[0]) > .7:
                    charframe.xvelo = charframe.xvelo * -.6
                    if charframe.x > levelinfo[cycle].x:
                        charframe.x = levelinfo[cycle].x + 1.005
                    else:
                        charframe.x = levelinfo[cycle].x - 1.005
                if abs(blockvector[2]) > .7:
                    charframe.zvelo = charframe.zvelo * -.6
                    if charframe.z > levelinfo[cycle].z:
                        charframe.z = levelinfo[cycle].z + 1.005
                    else:
                        charframe.z = levelinfo[cycle].z - 1.005
                charframe.x = charframe.x + charframe.xvelo
                charframe.y = charframe.y + charframe.grav
                charframe.z = charframe.z + charframe.zvelo
                # find out if we hit the finish
                if cycle == len(levelinfo) - 1:
                    level = level + 1
                    cycle = 0
                    while cycle < len(levelinfo):
                        levelinfo[cycle].visible = 0
                        cycle = cycle + 1
                    totalevelinfo = loadlevel(level)
                    levelinfo = totalevelinfo[0]
                    lowesty = totalevelinfo[1] - 2
                    cycle = 10000
                    charightarm.xvelo = 0
                    charightarm.yvelo = 0
                    charightarm.zvelo = 0
                    charleftarm.xvelo = 0
                    charleftarm.yvelo = 0
                    charleftarm.zvelo = 0
                    charframe.pos = (0,0,0)
                    charightarm.pos = (-0.6,0,.2)
                    charleftarm.pos = (0.6,0,0.2)
                    charframe.y = 5
                    dir = 0
                    camdir = 0
                    blinktmr = 0
                    charframe.grav = 0
                    camxvelo = 0
                    camyvelo = 0
                    camzvelo = 0
                    camx = 0
                    camy = 0
                    camz = 0
                    cycle = 0
                    onground = 0
                    charframe.prevx = 0
                    charframe.prevz = 0
                    blockvector = (0,0,0)
                    mouserightpress = 0
                    mouseleftpress = 0
                    mousemiddlepress = 0
                    charframe.grab = 'none'
                    autocam = 1
                    pos = (1000,1000,1000)
                    charframe.xvelo = 0
                    charframe.zvelo = 0


        cycle = cycle + 1

    #store the previous position
    charframe.prevx = charframe.x
    charframe.prevz = charframe.z
    charframe.prevy = charframe.y

    #find out if we have a "collision" from the right arm to its destination while it is in flight
    if charframe.grab == 'throw':
        blockscalar = math.sqrt((charightarm.x - pos[0]) ** 2 + (charightarm.y - pos[1]) ** 2 + (charightarm.z - pos[2]) ** 2)
        if blockscalar < 1:
            charframe.grab = 'collide'
            charightarm.xvelo = 0
            charightarm.yvelo = 0
            charightarm.zvelo = 0
            charightarm.pos = pos
        


    # MOUSE SCRIPTS AND REACTIONS

    
    #'poll' the mouse
    if scene.mouse.events:
        
        m = scene.mouse.getevent()
        if m.press == 'middle':
            mouseleftpress = 0
            mouserightpress = 0
            mousemiddlepress = 1
            autocam = 0
        if m.press == 'right':
            mouserightpress = 5
            if autocam == 0:
                autocam = 1
        if m.release == 'right':
            mouserightpress = 0    
        if m.press == 'left':
            mouseleftpress = 1
            if charframe.grab != 'collide':
                if charframe.grab == 'idle':
                    # find the position that the mouse was clicked, and change the arm velocity according to it.
                    if scene.mouse.pick:
                        if scene.mouse.pick.type == 'block':
                            pos = scene.mouse.pickpos
                            vectortomouse = (pos[0] - charightarm.x, pos[1] - charightarm.y, pos[2] - charightarm.z)
                            scalartomouse = math.sqrt(vectortomouse[0] ** 2 + vectortomouse[1] ** 2 + vectortomouse[2] ** 2)
                            if scalartomouse < 7:
                                charightarm.xvelo = vectortomouse[0] * .1
                                charightarm.yvelo = vectortomouse[1] * .1
                                charightarm.zvelo = vectortomouse[2] * .1
                                charframe.grab = 'throw'
                            else:
                                vectortomouse = (vectortomouse[0] / scalartomouse, vectortomouse[1] / scalartomouse, vectortomouse[2] / scalartomouse)
                                charightarm.xvelo = vectortomouse[0] * .7
                                charightarm.yvelo = vectortomouse[1] * .7
                                charightarm.zvelo = vectortomouse[2] * .7
                                charframe.grab = 'none'
                
                    else:
                        pos = scene.mouse.pos
                        charframe.grab = 'none'
                        vectortomouse = (pos[0] - charightarm.x + math.cos(math.radians(dir + 90)), pos[1] - charightarm.y, pos[2] - charightarm.z + math.sin(math.radians(dir + 90)))
                        charightarm.xvelo = vectortomouse[0] * .3
                        charightarm.yvelo = vectortomouse[1] * .3
                        charightarm.zvelo = vectortomouse[2] * .3
            else:
                charframe.grab = 'none'
        if m.release == 'left':
            mouseleftpress = 0
        if m.release == 'middle':
            mousemiddlepress = 0
            
        scene.mouse.events = 0

    #take action upon mouse events    
    if mouserightpress > 0:
        mousepos = scene.mouse.pos
        mousex = mousepos[0]
        mousez = mousepos[2]

        #get the direction to the mouse
        dirtomouse = degrees(math.atan2(charframe.z - mousez, charframe.x - mousex)) + 90

        #apply modulus on the direction
        if (dir - dirtomouse) > 180:
            dirdif = (dir - dirtomouse) - 360
        else:
            dirdif = (dir - dirtomouse)

        dirdif = ((dirdif + 180) % 360) - 180

        #change the direction
        if not abs(dirdif) < 10:
            dir = dir - dirdif / 40

        # modify the velocities from information about the mouse position
        mousevector = (charframe.z - mousez, charframe.x - mousex)
        distomouse = math.sqrt(mousevector[0] ** 2 + mousevector[1] ** 2)

        if distomouse > .3 and abs(dirdif) < 45:
            if charframe.grab != 'collide':
                charframe.xvelo  = charframe.xvelo * .5 + (math.cos(math.radians(dir + 90))) * distomouse / 20
                charframe.zvelo = charframe.zvelo * .5 + (math.sin(math.radians(dir + 90))) * distomouse / 20
            else:
                charframe.xvelo  = charframe.xvelo * .9 + (math.cos(math.radians(dir + 90))) * distomouse / 40
                charframe.zvelo = charframe.zvelo * .9 + (math.sin(math.radians(dir + 90))) * distomouse / 40

        
    # CHARACTER BODY SCRIPTS
    
    
    # get the directions converted to radians
    diradians = math.radians(dir)
    camdiradians = math.radians(dir+90)

    # take action for gravity and jumping
    if onground == 0:
        charframe.grav = charframe.grav - .008
    if onground == 1:
        charframe.grav = 0
        if mouserightpress > 2:
            if scene.mouse.pick:
                if scene.mouse.pick.frame == charframe:
                    charframe.grav = .25
    
    # 'count down' the mouse timer
    if mouserightpress > 1:
        mouserightpress = mouserightpress - 1

    #blinking scripts
    blinktmr = blinktmr + 1
    if blinktmr>140 and blinktmr<160:
        charighteye.z = .2
        charlefteye.z = .2
    if blinktmr>160:
        charighteye.z = .5
        charlefteye.z = .5
        blinktmr = 0
        
    # set the general character direction
    charframe.axis = (math.cos(diradians), 0, math.sin(diradians))

    
    #change character's position based off velocity
    charframe.y = charframe.y + charframe.grav
    charframe.x = charframe.x + charframe.xvelo
    charframe.z = charframe.z + charframe.zvelo

    #apply damping based on weather on a spring or not.
    if charframe.grab != 'collide':
        charframe.xvelo = charframe.xvelo * .7
        charframe.zvelo = charframe.zvelo * .7
    else:
        charframe.xvelo = charframe.xvelo * .98
        charframe.zvelo = charframe.zvelo * .98
        charframe.grav = charframe.grav * .99
    charframe.grav = charframe.grav * .99

    #find if the character has died, and reset the level
    if charframe.y < lowesty:
        charightarm.xvelo = 0
        charightarm.yvelo = 0
        charightarm.zvelo = 0
        charleftarm.xvelo = 0
        charleftarm.yvelo = 0
        charleftarm.zvelo = 0
        charframe.pos = (0,0,0)
        charightarm.pos = (-0.6,0,.2)
        charleftarm.pos = (0.6,0,0.2)
        charframe.y = 5
        dir = 0
        camdir = 0
        blinktmr = 0
        charframe.grav = 0
        camxvelo = 0
        camyvelo = 0
        camzvelo = 0
        camx = 0
        camy = 0
        camz = 0
        cycle = 0
        onground = 0
        charframe.prevx = 0
        charframe.prevz = 0
        blockvector = (0,0,0)
        mouserightpress = 0
        mouseleftpress = 0
        mousemiddlepress = 0
        charframe.grab = 'none'
        autocam = 1
        pos = (1000,1000,1000)
        charframe.xvelo = 0
        charframe.zvelo = 0
        


    #CHARACTER ARM SCRIPTS
    

    # ready the right arm for another throw if it isn't already being thrown and isn't colliding with something, and also make sure it is near the character
    if charframe.grab != 'throw' and charframe.grab != 'collide' and math.sqrt((charightarm.x - charframe.x) ** 2 + (charightarm.y - charframe.y) ** 2 + (charightarm.z - charframe.z) ** 2) < 2:
        charframe.grab = 'idle'
    # move the arms
    if charframe.grab == 'none' or charframe.grab == 'idle':
        charightarm.xvelo = charightarm.xvelo + ((charframe.x+(math.cos(diradians)*-0.6))-charightarm.x)/150
        charightarm.zvelo = charightarm.zvelo + ((charframe.z+(math.sin(diradians)*-0.6))-charightarm.z)/150
        charightarm.yvelo = charightarm.yvelo + (charframe.y - charightarm.y)/150

    elif charframe.grab == 'collide':
        #use simple vector spring physics to make the character become anchored to a spring
        
        armvector = (charightarm.x - charframe.x, charightarm.y - charframe.y, charightarm.z - charframe.z)
        armscalar = math.sqrt(armvector[0] ** 2 + armvector[1] ** 2 + armvector[2] ** 2)
        armvector = (armvector[0] / armscalar, armvector[1] / armscalar, armvector[2] / armscalar)

        generalaccel = (armscalar - charightarm.restlength) * charightarm.springconstant

        charframe.xvelo = charframe.xvelo + armvector[0] * generalaccel * 1.4
        charframe.grav = charframe.grav + armvector[1] * generalaccel
        charframe.zvelo = charframe.zvelo + armvector[2] * generalaccel * 1.4

    #change the right arm's position based off of velocity and apply damping
    charightarm.x = charightarm.x + charightarm.xvelo
    charightarm.z = charightarm.z + charightarm.zvelo
    charightarm.y = charightarm.y + charightarm.yvelo

    charightarm.zvelo = charightarm.zvelo * .97
    charightarm.xvelo = charightarm.xvelo * .97
    charightarm.yvelo = charightarm.yvelo * .97
    
    #change the left arm's velocity based off of relative position and change position based off of velocity and apply damping.
    charleftarm.xvelo = charleftarm.xvelo + ((charframe.x+(math.cos(diradians)*0.6))-charleftarm.x)/200
    charleftarm.zvelo = charleftarm.zvelo + ((charframe.z+(math.sin(diradians)*0.6))-charleftarm.z)/200
    charleftarm.yvelo = charleftarm.yvelo + (charframe.y - charleftarm.y)/200

    charleftarm.x = charleftarm.x + charleftarm.xvelo
    charleftarm.z = charleftarm.z + charleftarm.zvelo
    charleftarm.y = charleftarm.y + charleftarm.yvelo

    charleftarm.zvelo = charleftarm.zvelo * .97
    charleftarm.xvelo = charleftarm.xvelo * .97
    charleftarm.yvelo = charleftarm.yvelo * .97


    #CAMERA SCRIPTS
    

    #camera stuff
    if autocam == 1:
        camxvelo = camxvelo + ((charframe.x + (3 * math.cos(camdiradians)) - camx) / 75)
        camyvelo = camyvelo + ((charframe.y - 2 - camy)/75)
        camzvelo = camzvelo + ((charframe.z + (3 * math.sin(camdiradians)) - camz) / 75)
    else:
        if mousemiddlepress == 1:
            # rotate the screen according to mouse position if middle button pressed
            mousepos = scene.mouse.pos
            camxvelo = camxvelo + ((charframe.x - (mousepos[0]))) / 100
            camyvelo = camyvelo + ((charframe.y - (mousepos[1]))) / 100
            camzvelo = camzvelo + ((charframe.z - (mousepos[2]))) / 100
    
    #change camera position by velocity
    camx = camx + camxvelo
    camz = camz + camzvelo
    camy = camy + camyvelo

    #change the camera state
    scene.center = (charframe.x, charframe.y, charframe.z)
    scene.forward = (camx - charframe.x, camy - charframe.y, camz - charframe.z)
    scene.range = (3,3,3)

    #damp the camera    
    camxvelo = camxvelo * .925
    camyvelo = camyvelo * .97
    camzvelo = camzvelo * .925
    
    # refresh and limit the animation
    rate(30)
    
