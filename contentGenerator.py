# -*- coding: utf-8 -*
import nltk
#import newspaper

"""ep_paper = newspaper.build('http://elpais.com', language='es')
articles=[]
for item in ep_paper.articles[0:10]:
	item.download()
	item.parse()
	item.nlp()
	dic={}
	dic['content']=item.text
	dic['authors']=item.authors
	dic['title']=item.title
	dic['keywords']=item.keywords
	print dic
	articles.append(dic)"""


articles=[{"content":"Israel anuncia un alto el fuego humanitario de siete horas. La tregua no se aplicará en diversas zonas de la ciudad de Rafah, donde los militares israelíes continúan su ofensiva contra Hamás."},
		  {"content":"Israel mata a un jefe de la Yihad antes de iniciar una tregua parcial en Gaza.Israel ha declarado este lunes una tregua unilateral y parcial de siete horas en la franja de Gaza. Esta ventana humanitaria —como así lo llama el Ejército— ha empezado a las 8.00 hora local (las nueve en la España peninsular) y tiene previsto terminar a las 16.00 horas. La Yihad Islámica ha confirmado que durante la noche su líder en el sector norte, Danyal Mansur, ha muerto en un ataque israelí en su casa de Jabalia, informa France Presse."},
		  {"content":"El Gobierno israelí inicia una tregua humanitaria de siete horas en Gaza."},
		  {"content":"Israel no asocia sus bombardeos a la muerte de diez civiles dentro de la escuela de la ONU.Según investigaciones preliminares realizadas por las Fuerzas de Defensa, no se hace evidente que el daño a la escuela se haya debido a la ofensiva."},
		  {"content":"Israel anuncia un alto el fuego de siete horas.La tregua será aplicable en toda la Franja de Gaza, pero advierten que en caso de que se produzcan disparos, el Ejército responderá con firmeza."}]

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

content_text = ' '.join(article['content'] for article in articles)
tokenized_content = tokenizer.tokenize(content_text)
content_model = nltk.NgramModel(3, tokenized_content)

words_to_generate =30
starting_words = content_model.generate(150)[-4:]
starting_words = ['Israel']
content = content_model.generate(words_to_generate, starting_words)
print ' '.join(content)