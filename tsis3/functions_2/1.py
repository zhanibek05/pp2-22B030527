# Dictionary of movies

Movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def goodMovie(movie):
    for mov in Movies:
        if mov["name"] == movie and mov["imdb"] > 5.5:
            return True
    return False
print(goodMovie("Exam"))
            



#2
def goodMovies(movies):
    sublist = []
    for movie in movies:
        if goodMovie(movie):
            sublist.append(movie["name"])
    return sublist
#print(goodMovies(movies))


#3
def Category(categ):
    sublist = []
    for movie in Movies:
        if movie["category"] == categ:
            sublist.append(movie["name"])
    return sublist
#print(Category("Romance"))


#4
def averageIMDB(lstofmovies):
    sum = 0
    for mov in Movies:
        if mov["name"] in lstofmovies:
            sum = sum + mov["imdb"]
    return sum/len(lstofmovies)
mylist = ["Exam", "We Two"]
#print(averageIMDB(mylist))

#5
def averageIMDBcateg(categ):
    mylist = [mov["name"] for mov in Movies if mov["category"] == categ]
    return averageIMDB(mylist)
#print(averageIMDBcateg("Romance"))