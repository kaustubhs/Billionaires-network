import zen
import numpy
import unicodedata
import sys
sys.path.append('../zend3js/')
import d3js
import csv
import progressbar
import numpy.linalg as la
import matplotlib.pyplot as plt
plt.ioff()
from scipy.linalg import solve
from numpy import *
from time import sleep
import random

G_1=zen.io.gml.read('Billion_1.gml')

def print_top(G,v, num=5):
	idx_list = [(i,v[i]) for i in range(len(v))]
	idx_list = sorted(idx_list, key = lambda x: x[1], reverse=True)
	for i in range(min(num,len(idx_list))):
		nidx, score = idx_list[i]
		print '  %i. %s (%1.4f)' % (i+1,G.node_object(nidx),score)


#####Eigenvector centrality
print '\nEigenvector Centrality (by Zen):'
V1= zen.algorithms.centrality.eigenvector_centrality_(G_1,weighted=True)
print_top(G_1,V1, num=5)

#Degree Centrality
print 'Degree Centrality'
N = G_1.num_nodes
A = G_1.matrix()
A_sum=[]
for i in range(G_1.num_nodes):
      A_sumi=sum (A[i,:])
      A_sum.append(A_sumi)
K=A_sum
print_top(G_1,K)

##### Betweenness Centrality
print '\nBetweenness Centrality'
V3=zen.algorithms.centrality.betweenness_centrality_(G_1,weighted=True)
print_top(G_1,V3, num=5)

###Degree Distribution
print 'The one who knows the maximum number of people but not'
print 'necessarily he has indepth connections with a particular person is'
dist=[]       
for i in range(G_1.num_nodes):
        deg=G_1.degree_(i)
        dist.append(deg)

plt.plot(numpy.arange(0,548),dist)
plt.show()

array=numpy.array(dist)
index=numpy.argmax(array)
print G_1.node_object(index)


#Diameter
print 'Diameter of the graph is:'
print zen.diameter(G_1)

#Modularity for industry
print 'Modularity of the graph is:'
c = { 	'Real Estate': ['James Packer','Leonard Stern','Mitchell Goldhar','Anas Sefrioui','Samuel Tak Lee','Carlo Fidani','Angela Leong','Asok Kumar Hiranandani','Daniel Pritzker','Anthony Pritzker','Ina Chan','Bahaa Hariri','Dean White',
                        'Alexandra Schorghuber','Edward DeBartolo, Jr.','Kushal Pal Singh','Kwee brothers','Samih Sawiris','Thomas Pritzker','Alfred Taubman','Donald Bren','Kirk Kerkorian','Walter Kwok','Yang Huiyan','Jennifer Pritzker',
                        'Lin Rong San','Richard Marriott','Pansy Ho','John Gandel','John Pritzker','Marilyn Carlson Nelson','Penny Pritzker','Jean (Gigi) Pritzker','Nicholas Pritzker, II.','Raj Kumar & Kishin RK','Alexander Skorobogatko',
                        'Chen Lip Keong','Igor Olenicoff','Lawrence Ho','Linda Pritzker','Alexander Ponomarenko','Barbara Carlson Gage','Bill Marriott, Jr.','Eyal Ofer','Fredrik Lundberg','Eduardo Eurnekian','Georg von Opel','Edward Roski, Jr.',
                        'Karen Pritzker','Hui Wing Mau','Jay Robert (J.B.) Pritzker'],
        
 	'Diversed Financial': ['Isabel dos Santos','Jose Ermirio de Moraes Neto','Michael Milken','Robert Ziff','Yasseen Mansour','Sun Guangxin','Suna Kirac','Robert Kuok','Sebastian Pinera','Vincent Tan','Albert von Thurn und Taxis',
                               'Bassam Alghanim','Daniel Ziff','Alberto Cortina','Alexander Mamut','Chairul Tanjung','Charles Koch','Dirk Ziff','Stephan Schmidheiny','Andrew Tan','Clemmie Spangler, Jr.','Juan Abello','Mohamed Mansour',
                               'Stefan Olsson','Sukanto Tanoto','Zhang Hongwei','Robert Rowling','Bidzina Ivanishvili','Wilma Tisch','Kerr Neilson','Kutayba Alghanim','Neide Helena de Moraes','Youssef Mansour','Murdaya Poo','Joan Tisch',
                               'Li Ka-shing','Peter Kellogg','Prince Alwaleed Bin Talal Alsaud','Richard Scaife','Alberto Alcocer','Henry Hillman','Madeleine Olsson Ericksson','Antonia Johnson','Chen Jinxia','Anil Ambani',
                               'August von Finck','Dan Olsson','Alexander Vik','Antonio Ermirio de Moraes','David Koch','Eli Broad','Cheng Yu-tung','H. Wayne Huizenga','Jose Roberto Ermirio de Moraes','Maria Helena Moraes Scripilliti',
                               'Suleiman Kerimov','Vincent Bollore','Ermirio Pereira de Moraes','Ira Rennert','James Irving','Mustafa Rahmi Koc'],
        
 	'Consumer': ['Jorge Paulo Lemann','Liu Yongxing','Mary Alice Dorrance Malone','Patricia Matte','Anthony Pratt','Jeremy Jacobs, Sr.','Rishad Naoroji','Suh Kyung-Bae','Susanne Klatten','Tsai Eng-Meng','Jean Pierre Cayard',
                     'Robert Ingham','S. Curtis Johnson','Stefan Reimann-Andersen','Jean-Michel Besnier','John Fisher','Vikram Lal','Theo Mueller','Thomas Straumann','William Ford, Sr.','Alberto Bombassei','August Oetker',
                     'Charoen Sirivadhanabhakdi','Christopher Goldsbury','Robert Fisher','Robert Rich, Jr.','Sylvia Stroher','Winnie Johnson-Marquart','Aerin Lauder Zinterhofer','Ahsen Ozokur','Axel Oberwelland','Carl Ferdinand Oetker',
                     'Chung Mong-Koo','Alfred Oetker','Chey Tae-Won','Christian Oetker','Hans Peter Wild','Guilherme Peirao Leal','Hans Rausing','Ioan Niculae','Stefan Quandt','Charlotte Colket Weber','Cho Yang-Rai','Eliodoro Matte',
                     'Forrest Mars, Jr.','Imogene Powers Johnson','William Fisher','Wolfgang Reimann','Julia Oetker','Michael Hartono','Nicola Bulgari','Renate Reimann-Haas','Lei Jun','Stefan Persson','Wolfgang Herz','Ronald Lauder',
                     'Timothy Boyle','William Wrigley, Jr.','Anton Kathrein, Jr.','Ashwin Dani','Benedicta Chamberlain','Bennett Dorrance','Charlene de Carvalho-Heineken','Chung Mong-Joon','Helen Johnson-Leipold','Hubert d Ornano',
                     'Julio Ponce','Laurent Burelle','Leonard Lauder','Vladimir Scherbakov','Murat Ulker','Renzo Rosso','Liselott Persson','Paolo Bulgari','Marie Besnier Beauvalot','Matthias Reimann-Andersen','Kirsten Rausing',
                     'Nicolas Puech','Petro Poroshenko','Pier Luigi Loro Piana','Richard Oetker','Charles Bronfman','Heloise Waislitz','Jane Lauder','Alain Wertheimer','Bergit Douglas','Bernardo Matte','Carlos Ardila Lulle',
                     'Chung Eui-Sun','Daniela Herz','Andrea Della Valle','James Jannard','Richard Yuengling, Jr.','Andrei Guriev','David Murdock','Erika Pohl-Stroher','Fiona Geminder','Francisco Ivens de Sa Dias Branco','Gerard Wertheimer',
                     'Guenter Herz & Family','Jacqueline Mars','James Leprino','Prince Sultan bin Mohammed bin Saud Al Kabeer','Emanuele (Lino) Saputo','Horst Brandstaetter','H. Fisk Johnson','Herbert Louis','Ingeburg Herz',
                     'John Dorrance, III.','Rosely Schweizer','Vadim Moshkovich','Emmanuel Besnier','John Mars','Jose and Francisco Jose Calderon Rojas','Kjeld Kirk Kristiansen','Hanni Toosbuy Kasprzak','Johanna Quandt','Jean Burelle',
                     'Michael Herz','Michael Pieper','Patrizio Bertelli','Rahul Bajaj','Ravi Jaipuria','Miuccia Prada','Nobutada Saji'],
        
        'Retail and Restaurant': ['Juan Roig','Robert Piccinini','S. Robson Walton','Albert Blokker','Alice Walton','Stefano Pessina','Walter Frey','Shin Dong-Bin','Dieter Schwarz','Shari Arison','Shin Dong-Joo','Anders Holch Povlsen',
                                  'Dan Friedkin','Donald Hall','Els Blokker','Sergei Katsiev','David Sainsbury','Stelios Haji-Ioannou','Thomas Bruch','Anne Gittinger','Diego Della Valle','Igor Kesaev','Lee Myung-Hee','Micky Arison',
                                  'Mark Shoen','Jim Walton','Carol Jenkins Barnett','Fernando Roig','Karl Albrecht','M.A. Yusuff Ali','Bruce Nordstrom','Belmiro de Azevedo','Abilio dos Santos Diniz','Ann Walton Kroenke','Chung Yong-Jin',
                                  'Edward Stack','Drayton McLane, Jr.','Heidi Horten','Johan Johannson','Giuseppe De Longhi','Isidoro Alvarez','Joyce Raley Teel','Nancy Walton Laurie','Michael Klein'],
        
 	'Energy': ['Mokhzani Mahathir','Gordon Getty','Sid Bass','Robert Bass','Daisy Igel','George Kaiser','Vagit Alekperov','William Moncrief, Jr.','Ahmet Calik','Americo Amorim','Arthur Irving','Gian Marco Moratti','Daniel Harrison, III.',
                   'Rubens Ometto Silveira Mello','W. Herbert Hunt','William Koch','Evgeny (Eugene) Shvidler','Lee Bass','Lynn Schusterman','Mikhail Gutseriev','Ray Lee Hunt','Massimo Moratti','Mukesh Ambani','Farkhad Akhmedov',
                   'David Rockefeller, Sr.','Edward Bass','Folorunsho Alakija','Gennady Timchenko','Idan Ofer','Igor Makarov','Gregorio Perez Companc'],
        
        'Mining and metals': ['Patrice Motsepe','Patricia Angelini Rossi','Ana Maria Brescia Cafferata','Bulat Utemuratov','Dan Gertler','Alex Beard','Angela Bennett','Roberto Angelini Rossi','Claude Dauphin','Gina Rinehart','Tor Peterson',
                   'Margarita Louis-Dreyfus','Monique Louis-Dreyfus','Rosa Brescia Cafferata','Kumar Birla','Oleg Deripaska','Marie-Jeanne Meyer','Aristotelis Mistakidis','Beny Steinmetz','Daniel Mate','Eduardo Hochschild',
                   'Edwin Soeryadjaya','Ivan Glasenberg','Desmond Sacco','Vladimir Potanin','Jim Justice, II.','Pavel Tykac'],
        
        'Construction': ['Juan-Miguel Villar Mir','Arkady Rotenberg','Fahd Hariri','Riley Bechtel','Simonpietro Salini','Rossana Camargo de Arruda Botelho','D. Leopoldo Del Pino y Calvo-Sotelo','Francesco Saverio Salini','Zhu Xingliang',
                        'Alicia Koplowitz','Benu Gopal Bangur','Saad Hariri','Ali Ibrahim Agaoglu','Thomas Schmidheiny','Stephen Bechtel, Jr.','Walter Scott, Jr.','Yoshiko Mori','Maria Del Pino y Calvo-Sotelo','Pallonji Mistry',
                        'Renata de Camargo Nascimento','Mehmet Sinan Tara','Regina de Camargo Pires Oliveira Dias','Ayman Hariri','Elena Baturina','Ziyad Manasir','Rafael Del Pino y Calvo-Sotelo','Nassef Sawiris'],
        
        'Non-consumer industrial': ['Magdalena Martullo-Blocher','Anita Zucker','Georg Schaeffler','Scott Duncan','Vladimir Lisin','Alexander Abramov','Roman Abramovich','Antti Herlin','Francisco Jose Riberas Mera','Friedhelm Loh','Hans Melchers',
                                    'Catherine Lozick','Martin Viessmann','Max Turnauer','Milane Frantz','Randa Williams','Victor Pinchuk','Mitchell Jacobson','Lilian Werninghaus','Niklas Herlin','Miriam Blocher','Richard Kinder','Jose Maria Aristrain',
                                    'Maria-Elisabeth Schaeffler','Rahel Blocher','Reinhold Wuerth','Bachtiar Karim','Dannine Avara','Ilkka Herlin','Ilona Herlin','Lakshmi Mittal','Dieter Schnabel'],
        
        'Technology': ['Martin Haefner','Koo Bon-Neung','Sean Parker','Bent Jensen','David Cheriton','Eva Maria Bucher-Haefner','Evan Williams','Zhou Hongyi','Mark Vadon','Lee Boo-Jin','Lee Seo-Hyun','Venugopal Dhoot','Koo Bon-Moo',
                                'Jay Y. Lee','Lee Kun-Hee','Hong Ra-Hee','Azim Premji','H. Ross Perot, Jr.','Pat Stryker','Ronda Stryker','Stewart Rahr','Yusuf Hamied','Bernard (Barry) Sherman','Curt Engelhorn','Bulent Eczacibasi',
                                'Alberto Roemmers','Maja Oeri','Ludwig Merckle','Niels Peter Louis-Hansen','Pankaj Patel','Paul Ramsay','Phillip Frost','Randal Kirk','Henri Beaufour','Faruk Eczacibasi','Anne Beaufour','Shoji Uehara',
                                'Jacques Servier','Jon Stryker','Gary Michelson','Jeanine Dick','Frederik Paulsen'],

        'Money Management': ['Aloysio de Andrade Faria','Joao Moreira Salles','Dinara Kulibaeva','Rupert Johnson, Jr.','Walther Moreira Salles Junior','Timur Kulibaev','Warren Stephens','Rolf Gerling','Yuri Kovalchuk','Austen Cargill, II.',
                             'Carlos Rodriguez-Pastor','Deniz Sahenk','Fayez Sarofim','Gwendolyn Sontheim Meyer','James Cargill, II.','Benjamin de Rothschild','Filiz Sahenk','Tsai Hong-tu','Lily Safra','Marianne Liebmann',
                             'Pedro Moreira Salles','Susan Hirt Hagen','Whitney MacMillan','Ana Lucia de Mattos Barretto Villela','Fernando Roberto Moreira Salles','Wee Cho Yaw','Lina Maria Aguiar','Pauline MacMillan Keinath',
                             'Lia Maria Aguiar','Nikolai Tsvetkov','Luis Enrique Yarur Rey','Othman Benjelloun','Jaime Gilinski Bacal','Alfredo Egydio Arruda Villela Filho','Abigail Johnson','Charles Johnson','Bernard Saul, II.',
                             'Jaime Botin','Helena Revoredo','Edward Johnson, III.','Husnu Ozyegin'],
        
        'Media': ['Joao Roberto Marinho','Gary Magness','Indu Jain','Samuel Newhouse, Jr.','Stefan von Holtzbrinck','Emilio Azcarraga Jean','Sumner Redstone','Vladimir Yevtushenkov','Alan Rydge','Craig McCaw','Taha Mikati',
                  'Denis O Brien','Hary Tanoesoedibjo','Naguib Sawiris','Jim Kennedy','Lee Jay-Hyun','Yasumitsu Shigeta','Jose Roberto Marinho','Monika Schoeller','Najib Mikati','Andrei Kuzyaev','Blair Parry-Okeden','Krit Ratanarak',
                  'Donald Trump','Anne Cox Chambers','Brian Roberts','A. Jerrold Perenchio','Mark Cuban','Donald Newhouse','Friede Springer','Hubert Burda','Jonathan Harmsworth','Lee Hwa-Kyung','Richard Li','Mike Adenuga',
                  'Patrick McGovern'],

        'Other': ['Stanley Kroenke','Helmut Sohmen','Steven Udvar-Hazy','Sunny Varkey','Ana Maria Marcondes Penido Sant Anna','Baba Kalyani','Finn Rausing','Jorn Rausing','Peter Sperling','James France','Victor Fung',
                  'Sergio Mantegazza','Soichiro Fukutake','James Irsay','Philip Niarchos','John Fredriksen','Otto Happel','Kjell Inge Rokke','William Fung','Klaus-Michael Kuehne','Ranjan Pai','Denise York','Vincent McMahon','John Doerr',
                  'Daniel Och','Julian Robertson, Jr.','John Arnold','Danil Khachaturov','Leon G. Cooperman','Shin Chang-Jae','George Soros'],

 	}


Q=zen.modularity(G_1,c)
print Q


#Power law
print 'Power law'
def calc_powerlaw(G,kmin):
	ddist = zen.degree.ddist(G,normalize=False)
	cdist = zen.degree.cddist(G,inverse=True)
	k = numpy.arange(len(ddist))
	
	plt.figure(figsize=(8,12))
	plt.subplot(211)
	plt.bar(k,ddist, width=0.8, bottom=0, color='b')

	plt.subplot(212)
	plt.loglog(k,cdist)
	
	alpha = 0
	print '%1.2f' % alpha
	
	plt.show()

calc_powerlaw(G_1,1)
