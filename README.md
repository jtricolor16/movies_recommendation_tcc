# SOLUÇÃO PARA RECOMENDAÇÃO DE FILMES COM BASE EM CONTEÚDO

Este projeto destina-se ao desenvolvimento de um modelo e de um serviço de recomendação de filmes com base em conteúdo.

Nas seções a seguir, serão mostrados os passos necessários para instalar todas as dependências.

Ressalta-se que o projeto foi desenvolvido utilizando um sistema operacional derivado do Unix. Por isso, o passo a passo listado tende a se portar bem em dispositivos **Linux** e **MacOs**.

## PRÉ-REQUISITOS:
- Python 3 ou mais;
- Tableau para visualizar os dados de forma mais interativa.
- MongoDB.

## INSTALAÇÃO

Crie um ambiente virtual usando o comando venv

```
python3 -m venv NOME_DO_SEU_AMBIENTE_VIRTUAL 
```

Para ativá-lo, execute:

```
source NOME_DO_SEU_AMBIENTE_VIRTUAL/bin/activate
```

Instale o ipykernel para utilizarmos o Jupyter Notebook em um ambiente controlado:

```
pip install ipykernel
```

Instale um novo Kernel para trabalharmos no ambiente controlado, em vez de utilizar as dependências do sistema

```
ipython kernel install --user --name=NOME_DO_KERNEL
```

Abra o Jupyter Notebook e selecione o seu ambiente em *New button*, selecionando a opção **NOME_DO_KERNEL**.

```
jupyter notebook
``` 

Instale as dependências do serviço e do modelo de recomendação através do comando a seguir:

```
pip install -r requirements.txt
```

Outro ponto necessário é configurar o banco de dados documental MongoDB. Para tal há duas opções:
- Seguindo o passo a passo da [página oficial do MongoDB](https://docs.mongodb.com/manual/installation/).
- Utilizando o **docker-compose.yml** presente neste projeto. Caso opte por esta opção, [siga o passo a passo desta documentação](https://medium.com/@renato.groffe/mongodb-mongo-express-docker-compose-montando-rapidamente-um-ambiente-para-uso-824f25ca6957
). Inclusive o próprio docker-compose foi extraído das dicas apresentadas na página referenciada.

## COMO RODAR O SERVIÇO DE RECOMENDAÇÃO

Antes de iniciar o processo de configuração do serviço de recomendação, é de suma importância que você já tenha executado todas as células do arquivo **modelo_recomendacao.ipynb**. Isso porque ele será o responsável por salvar os dados de filmes recomendados no MongoDB.

Outro passo fundamental é se certificar que as env vars **MONGODB_HOST** e **MONGODB_PORT** estão populadas com os valores correspondentes ao endereço do MongoDB e a sua respectiva porta. Aconselha-se utilizar o arquivo env.sh e executar o seguinte comando:

```
source env.sh
```

Com todos esses passos executados, basta rodar os seguintes comandos:

```
set FLASK_APP=servico_recomendacao.py
```

e

```
python -m flask run
```

Com isso, o serviço deverá ser hospedado localmente.

## REALIZAR REQUISIÇÕES AO SERVIÇO DE RECOMENDAÇÃO

O serviço de recomendação disponibiliza dois endpoints de consulta para o retorno dos filmes com as suas recomendações.

Todas as requisições utilizam o método **GET** do protocolo http.

### GET /movies/{id}

Busca de filmes com base no id da obra.

<details>
    <summary>Clique para mais informações sobre requisições a **/movies/id**</summary>

Exemplo de request: `curl localhost:5000/movies/1`

Exemplo de retorno:

```
{
    "_id": 1,
    "genres": "adventure|animation|children|comedy|fantasy",
    "movieId": 1,
    "moviesRecommendation": [
        {
            "id": 3114,
            "title": "Toy Story 2 (1999)"
        },
        {
            "id": 120474,
            "title": "Toy Story That Time Forgot (2014)"
        },
        {
            "id": 78499,
            "title": "Toy Story 3 (2010)"
        },
        {
            "id": 116461,
            "title": "How the Toys Saved Christmas (1996)"
        },
        {
            "id": 45517,
            "title": "Cars (2006)"
        },
        {
            "id": 6377,
            "title": "Finding Nemo (2003)"
        },
        {
            "id": 4886,
            "title": "Monsters, Inc. (2001)"
        },
        {
            "id": 596,
            "title": "Pinocchio (1940)"
        },
        {
            "id": 115879,
            "title": "Toy Story Toons: Small Fry (2011)"
        },
        {
            "id": 208112,
            "title": "Rudolph the Red-Nosed Reindeer & the Island of Misfit Toys (2001)"
        },
        {
            "id": 2355,
            "title": "Bug's Life, A (1998)"
        },
        {
            "id": 8961,
            "title": "Incredibles, The (2004)"
        },
        {
            "id": 1920,
            "title": "Small Soldiers (1998)"
        },
        {
            "id": 5539,
            "title": "Care Bears Movie II: A New Generation (1986)"
        },
        {
            "id": 201588,
            "title": "Toy Story 4 (2019)"
        },
        {
            "id": 260,
            "title": "Star Wars: Episode IV - A New Hope (1977)"
        },
        {
            "id": 155366,
            "title": "Monster High: Great Scarrier Reef (2016)"
        },
        {
            "id": 4306,
            "title": "Shrek (2001)"
        },
        {
            "id": 595,
            "title": "Beauty and the Beast (1991)"
        }
    ],
    "tag": "owned|imdb top 250|pixar|time travel|children|comedy|funny|witty|rated-g|animation|computer animation|good cartoon chindren|friendship|bright|daring rescues|fanciful|heroic mission|humorous|light|rousing|toys come to life|unlikely friendships|warm|disney|boy|boy next door|bullying|friends|jealousy|martial arts|mission|neighborhood|new toy|rescue|resourcefulness|rivalry|toy|toy comes to life|walkie talkie|clever|tom hanks|toys|fun|dolls|national film registry|adventure|animated|cgi|family|fantasy|classic|watched|action figure|action figures|buzz lightyear|cg animation|woody|nostalgic|tim allen|childish|buddy movie|3d|ya boy|cute|story|voice acting|toys played|cowboy|dinosaur|fun family movie|best of rotten tomatoes: all time|john lasseter|the boys|soothing|cartoon|kids|disney animated feature|pixar animation|tã©a leoni does not star in this movie|exciting plot|funny lines|touching story|2009 reissue in stereoscopic 3-d|55 movies every kid should see--entertainment weekly|bd-video|clv|dvd-video|cgi classic|rainy day watchlist|villian hurts toys|itaege|family film|animmation|avi|buy|light hearted|whimsica|great movie|kids and family|action|kids movie|favorite|tumey's to see again|tumey's vhs|sci-fi|want to see again|innovative|good time|engaging|want|é ̃®ä ̧€é ̧£|first cgi film|joss whedon|very good|unny|usa|lots of heart|american animation",
    "title": "Toy Story (1995)"
}
```
</details>

### GET /movies/search?q={VALOR}

Realiza a busca por filmes com base no título da obra.

<details>
    <summary>Clique para mais informações sobre requisições a **/movies/search?q={VALOR}**</summary>

O valor correspondente ao título deve ser passado na query string **q**

Exemplo de request: `curl localhost:5000/movies/search?q=toy story`

Exemplo de resposta:

```
{
    "movies": [
        {
            "_id": 1,
            "genres": "adventure|animation|children|comedy|fantasy",
            "movieId": 1,
            "moviesRecommendation": [
                {
                    "id": 3114,
                    "title": "Toy Story 2 (1999)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 78499,
                    "title": "Toy Story 3 (2010)"
                },
                {
                    "id": 116461,
                    "title": "How the Toys Saved Christmas (1996)"
                },
                {
                    "id": 45517,
                    "title": "Cars (2006)"
                },
                {
                    "id": 6377,
                    "title": "Finding Nemo (2003)"
                },
                {
                    "id": 4886,
                    "title": "Monsters, Inc. (2001)"
                },
                {
                    "id": 596,
                    "title": "Pinocchio (1940)"
                },
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 208112,
                    "title": "Rudolph the Red-Nosed Reindeer & the Island of Misfit Toys (2001)"
                },
                {
                    "id": 2355,
                    "title": "Bug's Life, A (1998)"
                },
                {
                    "id": 8961,
                    "title": "Incredibles, The (2004)"
                },
                {
                    "id": 1920,
                    "title": "Small Soldiers (1998)"
                },
                {
                    "id": 5539,
                    "title": "Care Bears Movie II: A New Generation (1986)"
                },
                {
                    "id": 201588,
                    "title": "Toy Story 4 (2019)"
                },
                {
                    "id": 260,
                    "title": "Star Wars: Episode IV - A New Hope (1977)"
                },
                {
                    "id": 155366,
                    "title": "Monster High: Great Scarrier Reef (2016)"
                },
                {
                    "id": 4306,
                    "title": "Shrek (2001)"
                },
                {
                    "id": 595,
                    "title": "Beauty and the Beast (1991)"
                }
            ],
            "tag": "owned|imdb top 250|pixar|time travel|children|comedy|funny|witty|rated-g|animation|computer animation|good cartoon chindren|friendship|bright|daring rescues|fanciful|heroic mission|humorous|light|rousing|toys come to life|unlikely friendships|warm|disney|boy|boy next door|bullying|friends|jealousy|martial arts|mission|neighborhood|new toy|rescue|resourcefulness|rivalry|toy|toy comes to life|walkie talkie|clever|tom hanks|toys|fun|dolls|national film registry|adventure|animated|cgi|family|fantasy|classic|watched|action figure|action figures|buzz lightyear|cg animation|woody|nostalgic|tim allen|childish|buddy movie|3d|ya boy|cute|story|voice acting|toys played|cowboy|dinosaur|fun family movie|best of rotten tomatoes: all time|john lasseter|the boys|soothing|cartoon|kids|disney animated feature|pixar animation|tã©a leoni does not star in this movie|exciting plot|funny lines|touching story|2009 reissue in stereoscopic 3-d|55 movies every kid should see--entertainment weekly|bd-video|clv|dvd-video|cgi classic|rainy day watchlist|villian hurts toys|itaege|family film|animmation|avi|buy|light hearted|whimsica|great movie|kids and family|action|kids movie|favorite|tumey's to see again|tumey's vhs|sci-fi|want to see again|innovative|good time|engaging|want|é ̃®ä ̧€é ̧£|first cgi film|joss whedon|very good|unny|usa|lots of heart|american animation",
            "title": "Toy Story (1995)"
        },
        {
            "_id": 3114,
            "genres": "adventure|animation|children|comedy|fantasy",
            "movieId": 3114,
            "moviesRecommendation": [
                {
                    "id": 1,
                    "title": "Toy Story (1995)"
                },
                {
                    "id": 78499,
                    "title": "Toy Story 3 (2010)"
                },
                {
                    "id": 4886,
                    "title": "Monsters, Inc. (2001)"
                },
                {
                    "id": 201588,
                    "title": "Toy Story 4 (2019)"
                },
                {
                    "id": 2355,
                    "title": "Bug's Life, A (1998)"
                },
                {
                    "id": 126405,
                    "title": "The Adventures of André and Wally B. (1984)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 45517,
                    "title": "Cars (2006)"
                },
                {
                    "id": 116461,
                    "title": "How the Toys Saved Christmas (1996)"
                },
                {
                    "id": 170293,
                    "title": "Lilo & Stitch 2: Stitch has a Glitch (2005)"
                },
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 50872,
                    "title": "Ratatouille (2007)"
                },
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 115875,
                    "title": "Toy Story Toons: Hawaiian Vacation (2011)"
                },
                {
                    "id": 356,
                    "title": "Forrest Gump (1994)"
                },
                {
                    "id": 52287,
                    "title": "Meet the Robinsons (2007)"
                },
                {
                    "id": 87876,
                    "title": "Cars 2 (2011)"
                },
                {
                    "id": 595,
                    "title": "Beauty and the Beast (1991)"
                },
                {
                    "id": 109993,
                    "title": "George & A.J. (2009)"
                }
            ],
            "tag": "disney|owned|imdb top 250|original|animation|pixar|bright|daring rescues|fanciful|humorous|light|race against time|toys come to life|whimsical|airplane|collector|duringcreditsstinger|flea market|friendship|garage sale|identity crisis|inanimate objects coming to life|museum|personification|prosecution|rescue team|teamwork|toy comes to life|funny|sequel|tom hanks|dolls|comedy|oscar nominee|tim allen|childish|toys|abandonment|computer animation|cute|funny as hell|pixar animation|characters|music|story|voice acting|cgi|best of the saga|best of rotten tomatoes: all time|john lasseter|lee unkrich|2009 reissue in stereoscopic 3-d|bd-video|dvd-video|want|3d|sequel better than original|divx|very good but the first was better|joan cusack|john cusack|avi|buy|kids and family|tumey's vhs|plane|childhood classic|dvd1|tom hanks. humorous",
            "title": "Toy Story 2 (1999)"
        },
        {
            "_id": 78499,
            "genres": "adventure|animation|children|comedy|fantasy|imax",
            "movieId": 78499,
            "moviesRecommendation": [
                {
                    "id": 3114,
                    "title": "Toy Story 2 (1999)"
                },
                {
                    "id": 1958,
                    "title": "Terms of Endearment (1983)"
                },
                {
                    "id": 1357,
                    "title": "Shine (1996)"
                },
                {
                    "id": 1944,
                    "title": "From Here to Eternity (1953)"
                },
                {
                    "id": 909,
                    "title": "Apartment, The (1960)"
                },
                {
                    "id": 1225,
                    "title": "Amadeus (1984)"
                },
                {
                    "id": 63082,
                    "title": "Slumdog Millionaire (2008)"
                },
                {
                    "id": 1,
                    "title": "Toy Story (1995)"
                },
                {
                    "id": 5123,
                    "title": "Touch of Class, A (1973)"
                },
                {
                    "id": 1943,
                    "title": "Greatest Show on Earth, The (1952)"
                },
                {
                    "id": 174055,
                    "title": "Dunkirk (2017)"
                },
                {
                    "id": 50068,
                    "title": "Letters from Iwo Jima (2006)"
                },
                {
                    "id": 8921,
                    "title": "Rose Tattoo, The (1955)"
                },
                {
                    "id": 56782,
                    "title": "There Will Be Blood (2007)"
                },
                {
                    "id": 348,
                    "title": "Bullets Over Broadway (1994)"
                },
                {
                    "id": 5005,
                    "title": "Separate Tables (1958)"
                },
                {
                    "id": 356,
                    "title": "Forrest Gump (1994)"
                },
                {
                    "id": 69481,
                    "title": "Hurt Locker, The (2008)"
                },
                {
                    "id": 1961,
                    "title": "Rain Man (1988)"
                }
            ],
            "tag": "tear jerker|owned|childhood|children|friendship|bittersweet|fun and deep|visually appealing|animation|barbie|college|day care|duringcreditsstinger|escape|hostage|inanimate objects coming to life|personification|teddy bear|toy|toy comes to life|toy story|pixar|tom hanks|annemari|dolls|good versus evil|kindergarten|overrated|toys|toys come to life|watch the credits|adventure|oscar (best animated feature)|oscar nominee: best picture|tense|oscar nominee: best picture 2010|franchise|must see|pixar animation|sequel|story|torture|violence|big budget|action|deus ex machina|loyalty|peril|alive toys|weird|nostalgic|music|score|timothy dalton|characters|funny|sad|witty|worn out story|emotional|i cried|don rickles|tim allen|lee unkrich|sinister|bd-video|imax dmr 3-d|stereoscopic 3-d|itaege|boring|na dysku|comedy|animação|interrogation|cgi|computer animation|oppression|toplist10|childhood classic|ken|joan cusack|tearjerker|imaginative|overly sentimental|anthropomorphism|bechdel test:pass|betrayal|day care center|eye|g|going home|losing a hat|loss of eye|manipulation|moviepig top pick|oscar (best music - original song)|oscar nominee: adapted screenplay|oscar nominee: sound editing|screenwriter:michael arndt|seen 2013|terror|women disguised as men",
            "title": "Toy Story 3 (2010)"
        },
        {
            "_id": 106022,
            "genres": "animation|children|comedy",
            "movieId": 106022,
            "moviesRecommendation": [
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 126012,
                    "title": "The Fat Albert Halloween Special (1977)"
                },
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 125948,
                    "title": "Fright to the Finish (1954)"
                },
                {
                    "id": 125962,
                    "title": "Charlie Brown's Christmas Tales (2002)"
                },
                {
                    "id": 181771,
                    "title": "Uncle Donald's Ants (1952)"
                },
                {
                    "id": 181945,
                    "title": "Wet Paint (1946)"
                },
                {
                    "id": 199021,
                    "title": "Tweet-Tweet (2018)"
                },
                {
                    "id": 109993,
                    "title": "George & A.J. (2009)"
                },
                {
                    "id": 190163,
                    "title": "Leaning Towards Solace (2012)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 187163,
                    "title": "Side of the moon (1984)"
                },
                {
                    "id": 182127,
                    "title": "Newman Laugh-O-Grams (1921)"
                },
                {
                    "id": 182271,
                    "title": "Goldilocks and the Jivin' Bears (1944)"
                },
                {
                    "id": 180063,
                    "title": "Wasteland No. 1: Ardent Verdant (2017)"
                },
                {
                    "id": 182013,
                    "title": "Donald's Gold Mine (1942)"
                },
                {
                    "id": 182071,
                    "title": "Donald's Happy Birthday (1949)"
                },
                {
                    "id": 182075,
                    "title": "Chef Donald (1941)"
                },
                {
                    "id": 182101,
                    "title": "The Flying Jalopy (1943)"
                }
            ],
            "tag": "pixar|short|halloween|toys|franchise|angus maclane|bd-r|bd-video|short film",
            "title": "Toy Story of Terror (2013)"
        },
        {
            "_id": 115875,
            "genres": "adventure|animation|children|comedy|fantasy",
            "movieId": 115875,
            "moviesRecommendation": [
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 109993,
                    "title": "George & A.J. (2009)"
                },
                {
                    "id": 140341,
                    "title": "Lava (2015)"
                },
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 126405,
                    "title": "The Adventures of André and Wally B. (1984)"
                },
                {
                    "id": 95375,
                    "title": "Boundin' (2003)"
                },
                {
                    "id": 95856,
                    "title": "Knick Knack (1989)"
                },
                {
                    "id": 95858,
                    "title": "For the Birds (2000)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 109425,
                    "title": "Dug's Special Mission (2009)"
                },
                {
                    "id": 83803,
                    "title": "Day & Night (2010)"
                },
                {
                    "id": 120470,
                    "title": "The Legend of Mor'du (2012)"
                },
                {
                    "id": 109423,
                    "title": "Your Friend the Rat (2007)"
                },
                {
                    "id": 109420,
                    "title": "Mater and the Ghostlight (2006)"
                },
                {
                    "id": 164929,
                    "title": "Air Mater (2011)"
                },
                {
                    "id": 95311,
                    "title": "Presto (2008)"
                },
                {
                    "id": 184963,
                    "title": "Taking Flight (2015)"
                },
                {
                    "id": 72356,
                    "title": "Partly Cloudy (2009)"
                },
                {
                    "id": 108983,
                    "title": "La Luna (2011)"
                }
            ],
            "tag": "pixar|short|pixar animation|toy story|gary rydstrom",
            "title": "Toy Story Toons: Hawaiian Vacation (2011)"
        },
        {
            "_id": 115879,
            "genres": "adventure|animation|children|comedy|fantasy",
            "movieId": 115879,
            "moviesRecommendation": [
                {
                    "id": 106022,
                    "title": "Toy Story of Terror (2013)"
                },
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 115875,
                    "title": "Toy Story Toons: Hawaiian Vacation (2011)"
                },
                {
                    "id": 109993,
                    "title": "George & A.J. (2009)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 95858,
                    "title": "For the Birds (2000)"
                },
                {
                    "id": 140341,
                    "title": "Lava (2015)"
                },
                {
                    "id": 126405,
                    "title": "The Adventures of André and Wally B. (1984)"
                },
                {
                    "id": 95856,
                    "title": "Knick Knack (1989)"
                },
                {
                    "id": 109425,
                    "title": "Dug's Special Mission (2009)"
                },
                {
                    "id": 83803,
                    "title": "Day & Night (2010)"
                },
                {
                    "id": 138702,
                    "title": "Feast (2014)"
                },
                {
                    "id": 95375,
                    "title": "Boundin' (2003)"
                },
                {
                    "id": 182005,
                    "title": "Donald's Garden (1942)"
                },
                {
                    "id": 181995,
                    "title": "Old MacDonald Duck (1941)"
                },
                {
                    "id": 174225,
                    "title": "Farmer Al Falfa Sees New York (1916)"
                },
                {
                    "id": 182101,
                    "title": "The Flying Jalopy (1943)"
                },
                {
                    "id": 125960,
                    "title": "The Trip to Squash Land (1967)"
                },
                {
                    "id": 181955,
                    "title": "Soup's On (1948)"
                }
            ],
            "tag": "funny|pixar|short|fast food|fast food restaurant|pixar animation|toy story|toys|angus maclane|animation|family|short film",
            "title": "Toy Story Toons: Small Fry (2011)"
        },
        {
            "_id": 120468,
            "genres": "animation|children|comedy",
            "movieId": 120468,
            "moviesRecommendation": [
                {
                    "id": 181213,
                    "title": "Aztec Rex (2007)"
                },
                {
                    "id": 120474,
                    "title": "Toy Story That Time Forgot (2014)"
                },
                {
                    "id": 115875,
                    "title": "Toy Story Toons: Hawaiian Vacation (2011)"
                },
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 109993,
                    "title": "George & A.J. (2009)"
                },
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 181959,
                    "title": "Sleepy Time Donald (1947)"
                },
                {
                    "id": 94005,
                    "title": "Ballad of Nessie, The (2011)"
                },
                {
                    "id": 126807,
                    "title": "Weekender (2011)"
                },
                {
                    "id": 116461,
                    "title": "How the Toys Saved Christmas (1996)"
                },
                {
                    "id": 106022,
                    "title": "Toy Story of Terror (2013)"
                },
                {
                    "id": 140341,
                    "title": "Lava (2015)"
                },
                {
                    "id": 133151,
                    "title": "Barbie and the Three Musketeers (2009)"
                },
                {
                    "id": 181939,
                    "title": "Donald's Dilemma (1947)"
                },
                {
                    "id": 181841,
                    "title": "Donald's Dream Voice (1948)"
                },
                {
                    "id": 181941,
                    "title": "Donald's Crime (1945)"
                },
                {
                    "id": 155366,
                    "title": "Monster High: Great Scarrier Reef (2016)"
                },
                {
                    "id": 125962,
                    "title": "Charlie Brown's Christmas Tales (2002)"
                },
                {
                    "id": 1920,
                    "title": "Small Soldiers (1998)"
                }
            ],
            "tag": "party|pixar|short|toys|bath tub|bubble|house music|rubber duck|sponge|strobe light|toy story|tyrannosaurus rex|water|mark a. walsh|rave|unexpected",
            "title": "Toy Story Toons: Partysaurus Rex (2012)"
        },
        {
            "_id": 120474,
            "genres": "animation|children",
            "movieId": 120474,
            "moviesRecommendation": [
                {
                    "id": 175831,
                    "title": "Lou (2017)"
                },
                {
                    "id": 115875,
                    "title": "Toy Story Toons: Hawaiian Vacation (2011)"
                },
                {
                    "id": 133151,
                    "title": "Barbie and the Three Musketeers (2009)"
                },
                {
                    "id": 115879,
                    "title": "Toy Story Toons: Small Fry (2011)"
                },
                {
                    "id": 126405,
                    "title": "The Adventures of André and Wally B. (1984)"
                },
                {
                    "id": 182041,
                    "title": "Wide Open Spaces (1947)"
                },
                {
                    "id": 182153,
                    "title": "Donald's Cousin Gus (1939)"
                },
                {
                    "id": 174225,
                    "title": "Farmer Al Falfa Sees New York (1916)"
                },
                {
                    "id": 182029,
                    "title": "Bootle Beetle (1947)"
                },
                {
                    "id": 172613,
                    "title": "Le noeud cravate (2008)"
                },
                {
                    "id": 181937,
                    "title": "Clown of the Jungle (1947)"
                },
                {
                    "id": 181805,
                    "title": "The Flying Squirrel (1954)"
                },
                {
                    "id": 181955,
                    "title": "Soup's On (1948)"
                },
                {
                    "id": 181995,
                    "title": "Old MacDonald Duck (1941)"
                },
                {
                    "id": 182005,
                    "title": "Donald's Garden (1942)"
                },
                {
                    "id": 182011,
                    "title": "Bellboy Donald (1942)"
                },
                {
                    "id": 179999,
                    "title": "Trois petits points (2010)"
                },
                {
                    "id": 181949,
                    "title": "The Pelican and the Snipe (1944)"
                },
                {
                    "id": 181813,
                    "title": "The Story of Anyburg U.S.A. (1957)"
                }
            ],
            "tag": "animation|pixar|short|toys|toy|toy story|animated|dinosaurs|steve purcell|bd-video|etaege|computer animation|short film|cute",
            "title": "Toy Story That Time Forgot (2014)"
        },
        {
            "_id": 201588,
            "genres": "adventure|animation|children|comedy",
            "movieId": 201588,
            "moviesRecommendation": [
                {
                    "id": 170293,
                    "title": "Lilo & Stitch 2: Stitch has a Glitch (2005)"
                },
                {
                    "id": 126405,
                    "title": "The Adventures of André and Wally B. (1984)"
                },
                {
                    "id": 116461,
                    "title": "How the Toys Saved Christmas (1996)"
                },
                {
                    "id": 161812,
                    "title": "VeggieTales: The Ballad of Little Joe (2003)"
                },
                {
                    "id": 5539,
                    "title": "Care Bears Movie II: A New Generation (1986)"
                },
                {
                    "id": 208693,
                    "title": "Pippi Longstocking (1997)"
                },
                {
                    "id": 156137,
                    "title": "Jock of the Bushveld (2011)"
                },
                {
                    "id": 197539,
                    "title": "Wheely (2018)"
                },
                {
                    "id": 207065,
                    "title": "Minuscule 2: Mandibles From Far Away (2019)"
                },
                {
                    "id": 176299,
                    "title": "Tom and Jerry: Willy Wonka and the Chocolate Factory (2017)"
                },
                {
                    "id": 208939,
                    "title": "Klaus (2019)"
                },
                {
                    "id": 109102,
                    "title": "Little Brother, Big Trouble: A Christmas Adventure (Niko 2: Lentäjäveljekset) (2012)"
                },
                {
                    "id": 189591,
                    "title": "Jungle Emperor Leo (1997)"
                },
                {
                    "id": 202932,
                    "title": "The Big Trip (2019)"
                },
                {
                    "id": 166765,
                    "title": "Tri bogatyrya i Shamakhanskaya tsaritsa (2010)"
                },
                {
                    "id": 124919,
                    "title": "The Wind in the Willows (1995)"
                },
                {
                    "id": 199694,
                    "title": "Despicable Me Presents: Minion Madness (2010)"
                },
                {
                    "id": 199832,
                    "title": "How to Train Your Dragon - Legends (2010)"
                },
                {
                    "id": 122335,
                    "title": "The Land Before Time IX: Journey to the Big Water (2002)"
                }
            ],
            "tag": "pixar|sequel|bittersweet|touching|jim's list|reviewed|friendship|antique store|children|computer animation|family|family film|kindergarten|love|purpose|tim allen|tom hanks|toys|key and peele|emotional",
            "title": "Toy Story 4 (2019)"
        }
    ]
}
```

</details>

## REFERÊNCIAS

https://medium.com/datavizbr/3-dicas-para-criar-uma-visualiza%C3%A7%C3%A3o-de-dados-de-sucesso-dica-0-n%C3%A3o-comece-pela-visualiza%C3%A7%C3%A3o-73154f5e56f3

https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo