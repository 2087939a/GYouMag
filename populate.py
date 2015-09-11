import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GYou_Mag.settings')

import django
django.setup()

from app.models import Category, Article



def populate():
    cultureCat = add_cat('Culture')
    
    add_article(cat = cultureCat ,
    title = 'French people are fashionably lazy' , 
    content = "sabrina "*1500,
    author = "Hank"
    )

    add_article(cat = cultureCat ,
    title = 'Vous etes fan de Benoit Magimel ?' , 
    content = "Je suis fan de Benoit Magimel, Sebastien."*1500,
    author = "Kemar"
    )
    
    add_article(cat = cultureCat ,
    title = "La creme glacee c'est michto" , 
    content = "Lucien Coquin "*1500,
    author = "TerryBadTrip"
    )	
    
    musicCat = add_cat('Music')
    
    add_article(cat = musicCat ,
    title = 'La deep house musique de connard ? Explication' , 
    content = "J'adore les sons dark c'est enorme haha!"*1500,
    author = "Marc-Olivier Fogiel"
    )
    
    
    
    
    politicsCat = add_cat('Politics')
    lifestyleCat = add_cat('Lifestyle')
    featuresCat = add_cat('Features')
    columnsCat = add_cat('Columns')



def add_article(cat, title, content, author, views = 0):
    a = Article.objects.get_or_create(category=cat, title=title)[0]
    a.views = views
    a.content = content
    a.author = author
    a.save()
    return a

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting GYou_Mag population script..."
    populate()