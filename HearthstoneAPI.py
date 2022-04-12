import os
import time

#https://develop.battle.net/documentation/guides/getting-started
#curl -u {client_id}:{client_secret} -d grant_type=client_credentials https://us.battle.net/oauth/token

for cardId in range(1000,1500):
    time.sleep(0.05)
    #inputCardId = 35

    #curl -H "Authorization: Bearer {access_token}" https://us.api.blizzard.com/data/wow/token/?namespace=dynamic-us
    firstHalfCommand  = 'curl --header "Authorization: Bearer " https://us.api.blizzard.com/hearthstone/cards/'
    secondHalfCommand = '?locale=en_US'
    command = firstHalfCommand + str(cardId) + secondHalfCommand

    res = os.popen(command).read()#Type in command and store HTTP Return in variable

    #print(res)

    noExistMsg = '{"error":{"status":404,"statusMessage":"Not Found","message":"No such card"}}'

    if(not(res == noExistMsg)):
        #strOut = """{"id":36,"collectible":1,"slug":"36-cenarius","classId":2,"multiClassIds":[],"cardTypeId":4,"cardSetId":3,"rarityId":5,"artistName":"Alex Horley Orlandelli","health":8,"attack":5,"manaCost":8,"name":"Cenarius","text":"<b>Choose One -</b> Give your other minions +2/+2; or Summon two 2/2 Treants with <b>Taunt</b>.","image":"https://d15f34w2p8l1cc.cloudfront.net/hearthstone/975d9f3fad9300e9dcf82747a971ffd860f69fa5e162c988534e25a68d06891c.png","imageGold":"https://d15f34w2p8l1cc.cloudfront.net/hearthstone/0232d288dc0f7a5fb15f08abc5dbe5011f9940c4f071d97259a9c2aac7151e31.png","flavorText":"Yes, he's a demigod. No, he doesn't need to wear a shirt.","cropImage":"https://d15f34w2p8l1cc.cloudfront.net/hearthstone/75bfd42165394b1635edd50957bc3d25a4c1e01e02be039f63664529c88f7bae.png","childIds":[364,678,1145],"keywordIds":[1],"duels":{"relevant":true,"constructed":true}}"""
        strOut = res

        print(strOut)

        strList = strOut.split(",")
        #print(strList)
        cardDict = {}
                        
        for i in range(0, len(strList)):
            pair = strList[i].split(":")
            #SI:7 Agent ARERGGGG (1117)
            
            #print(pair)
            if(not(len(pair) == 2)):
                continue
            key = pair[0].split('"')[1]
            value = pair[1]
            cardDict[key] = value

        #print(cardDict["id"])
        #print(cardDict["name"])
        #id
        #classId
        #health
        #attack
        #manaCost
        #name

        #relevantInfo = [cardDict["id"],cardDict["classId"],cardDict["name"],cardDict["manaCost"],cardDict["attack"],cardDict["health"]]
        #print(relevantInfo)
        #print(cardDict['collectible']) #1 or 0 If Collectable 
        print(f"ID {cardId} is card {cardDict['name']}")
    else:
        print(f"ID {cardId} has no card")
