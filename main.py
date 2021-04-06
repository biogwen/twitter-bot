from api import api
import datetime

# limite tweets => 180 pour 15 minutes
# limites recherches => 300 pour 3 heures

tweets = 0
recherche = 0

limite_tweets = 180
limite_recherche = 300


# partie recherche
def search(sujet, quantity):
    global recherche
    result_tweets = api.GetSearch(term=sujet, count=quantity, result_type='recent')
    recherche += 1
    print(result_tweets)
    keywords = ['flat earth', 'sheep', 'idiots']
    for result in result_tweets:
        print(result.text, keywords, result.user.screen_name, result.id)

        #reply(result.text, keywords, result.user.screen_name, result.id)


# réponse
def reply(texte, keywords, screen_name, id_autor):
    global tweets
    for keyword in keywords:
        if texte.endswith(keyword):
            print('trouvé')
            repondre('@' + screen_name + ' we are all around the globe', id_autor)
            tweets += 1

def repondre(texte, id_autor):
    api.PostUpdate(status=texte, in_reply_to_status_id=id_autor)

def plus15minutes():
    plus15 = datetime.datetime.now() + datetime.timedelta(minutes=15)
    return plus15


def plus3heures():
    plus3 = datetime.datetime.now() + datetime.timedelta(hours=3)
    return plus3


def start(subject, quantity):
    stop = False
    pourquoi = ""
    while not stop:
        if tweets >= limite_tweets:
            pourquoi = 'limite des tweets atteinte. attendre ' + plus15minutes().strftime("%H : %M : %S") + ' avant de continuer.'
            stop = True

        elif recherche >= limite_recherche:
            pourquoi = 'limite des recherches atteinte. attendre ' + plus3heures().strftime("%H : %M : %S") + ' avant de continuer.'
            stop = True

        else:
            try:
                search(subject, quantity)
            except:
                print("erreur surement de quota")
    print(pourquoi)


# start("flat earth", 20)
search("flat earth", 20)