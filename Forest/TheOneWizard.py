# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.

def spellList(target):
        if hero.canCast("chain-lightning", target):
            hero.cast("chain-lightning", target)
        elif hero.canCast("lightning-bolt", target):
            hero.cast("lightning-bolt", target)
        else:
            hero.attack(target)


while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        
        if distance < 15:
            if hero.canCast("root", enemy):
                hero.cast("root", enemy)
                
        if enemy.type == "scout":
            hero.moveXY(3, 36)
            spellList(enemy)
        elif enemy.type == "catapult":
            if hero.canCast("lightning-bolt", enemy):
                hero.cast("lightning-bolt", enemy)
            else:
                pass
        elif enemy.type == "ogre":
            hero.moveXY(7, 41)
            spellList(enemy)
        else:
            spellList(enemy)
            
    if (hero.health <= 70):
        hero.cast("regen", hero)
    
