# Try to get the best grade (gold) at the magic exam.
# Move to each X mark, then use a spell.

def castSpell(spell):
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    if enemy:
        if hero.canCast(spell, enemy):
            hero.cast(spell, enemy)
    elif friend:
        if hero.canCast(spell, friend):
            hero.cast(spell, friend)

def go(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    char={"scout":"poison-cloud", "brawler":"shrink", "goliath":"grow", "soldier":"heal", "paladin":"regen", "ogre":"force-bolt"}
    if enemy:
        type = enemy.type
        for k,v in char.items():
            if type == k:
                spell = v
                castSpell(spell)
    elif friend:
        type = friend.type
        for k,v in char.items():
            if type == k:
                spell = v
                castSpell(spell)
    else:
        hero.cast("grow", hero)
        item = hero.findNearestItem()
        if item:
            pos = item.pos
            hero.moveXY(pos.x,pos.y)
        
    

go(17, 40)
go(17, 24)
go(34, 40)
go(34, 24)
go(50, 40)
go(50, 24)
go(66, 40)
go(66, 24)
