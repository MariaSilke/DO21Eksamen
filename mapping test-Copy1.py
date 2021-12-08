#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install folium


# In[3]:


import folium
import pandas as pd
from folium.plugins import MarkerCluster


# In[4]:


m = folium.Map(location=[55.675758, 12.569020])
m


# In[5]:


#jeg foretager test for placering af location

ml = folium.Map(location=[55.675758, 12.569020], zoom_start=12, tiles="Stamen Terrain")

folium.Marker(
    location=[55.65870292280947, 12.60364145994735],
    popup="Solstrålen og Smørhullet",
    icon=folium.Icon(icon="cloud"),
).add_to(ml)


ml


# In[6]:


#jeg foretager test af color

mlm = folium.Map(location=[55.675758, 12.569020], zoom_start=12, tiles="Stamen Terrain")

folium.Marker(
    location=[55.65870292280947, 12.60364145994735],
    popup="Solstrålen og Smørhullet",
    icon=folium.Icon(color="red", icon="cloud"),
).add_to(mlm)


mlm


# In[7]:


#jeg foretager test af icon

mlml = folium.Map(location=[55.675758, 12.569020], zoom_start=12, tiles="Stamen Terrain")

folium.Marker(
    location=[55.65870292280947, 12.60364145994735],
    popup="Solstrålen og Smørhullet",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(mlml)


mlml


# In[8]:


map = folium.Map(location=[55.675758, 12.569020], zoom_start=12, tiles="Stamen Terrain")

folium.Marker(
    location=[55.65870292280947, 12.60364145994735],
    popup="Solstrålen og Smørhullet",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69349412277640, 12.559608539952723],
    popup="Børnehuset Urtehaven",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.66021961281015, 12.595556529948388],
    popup="Vuggestuen Sundholm",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.639039152835800, 12.605015899947217],
    popup="Ingolf",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6654989427991, 12.606799479946917],
    popup="Børnehuset Lygtemagerstien",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65084776282255, 12.596787299948254],
    popup="Kastanien",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64242989282879, 12.612174939946268],
    popup="Idrætsinstitution Hoppeland",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6678483628005, 12.593221239948665 ],
    popup="Den Grønne Planet",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65414120280868, 12.623976189944647],
    popup="Børnehuset ved Volden",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64711172282135, 12.61523435994585],
    popup="Børnenes Poppelhus",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65788348281312, 12.596195449948311],
    popup="Skattekisten",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.63683306284468, 12.587839589949427],
    popup="Jorden Rundt",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64273951283008, 12.607185699946925],
    popup="M-Husets Vuggestue",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6594164128145, 12.585866819949615],
    popup="Sejlhuset",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.634463942849635, 12.582701859950074],
    popup="Børnehuset Gullfossgade",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65350678280929, 12.624640179944558],
    popup="Viften",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64756673281958, 12.61847880994541],
    popup="Østen for Solen",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65601104281399, 12.601229429947667],
    popup="Snorretoppen",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6635430628019, 12.606483209946962],
    popup="De 5 Årstider",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.7106060027593, 12.53960518995499],
    popup="Havblik",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70933632276681, 12.520800629957074],
    popup="Paletten",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70930551276808, 12.516793349957505],
    popup="Amagerhus",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.7078667727703, 12.515902429957602],
    popup="Børnehuset Gro",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71587445274824, 12.551767469953587],
    popup="Gullandsgården",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71129576275824, 12.539960199954955],
    popup="Hundredemeterskoven",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.68329278278778, 12.567744389951779],
    popup="Filosofvænget",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.683094532785965, 12.574187769951],
    popup="Solstrålen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.67126756279676, 12.590479029949003],
    popup="Regnskoven",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.80405070262392, 12.561198599952268],
    popup="Enighedens Børnehus",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.85628175256146, 12.530258929955709],
    popup="Børnehuset Englegård",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.679050262790874, 12.576067279950783],
    popup="Klatretræet",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6702391528013, 12.581003789950193],
    popup="Småbørnenes Forsamlingshus",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69198262277253, 12.577960039950515],
    popup="Ørnen",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69639775277413, 12.554361959953333],
    popup="Lundsgade",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.709916132755815, 12.553651639953385],
    popup="Kongehatten",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.695672732776764, 12.549208449953934],
    popup="Krudthuset",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.53030207309337, 12.176785999982592],
    popup="Vartov",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70479122275389, 12.58130681995007],
    popup="Klerkegade",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.82343270259395, 12.571133299951024],
    popup="Titanrosen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64449192286203, 12.499289949959476],
    popup="Den Grønne Giraf",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.652839502842404, 12.526648969956565],
    popup="Cismofytten",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6467373328692, 12.463695579962973],
    popup="Stenurten",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.49911707316622, 11.981650119989686],
    popup="Kastaniehuset - Vuggestue og Børnehave",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6517597428477, 12.514086359957918],
    popup="Krible-Krable",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.59330529297385, 12.33998403997315],
    popup="7-Springeren",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64618865287003, 12.463386569963001],
    popup="Murergården",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.662736972834765, 12.507080479958635],
    popup="Sølund",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.692769642798964, 12.489061079960415],
    popup="Valby Vuggestue",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70864772278081, 12.476365649961636 ],
    popup="Labyrinten",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71073585274803, 12.574259859950924],
    popup="Børnekompasset",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69809580278654, 12.50638869995863],
    popup="Børnehuset Troldehøj",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71042052278233, 12.462396439962971],
    popup="Børnehuset Savannen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.65869666283488, 12.52510468995672],
    popup="Villa Valby",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69764748278706, 12.506753699958592],
    popup="Børnehuset Fengersvej",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.697582472795354, 12.478659939961432],
    popup="Duetten",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.713804742771565, 12.483976429960878],
    popup="Vuggestuen Rugvej",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.774332762673126, 12.535018169955364],
    popup="Vindsuset",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.669637222811794, 12.551206529953765],
    popup="Tusindfryd",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.77552834270387, 12.421655999966518],
    popup="Drivhuset",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6662465028164, 12.55124477995377],
    popup="Stjerneskuddet",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.66962446281133, 12.55267430995359],
    popup="Slottet",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)


folium.Marker(
    location=[55.672388422807565, 12.552664929953588],
    popup="Børnehuset ByToften",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.6484424228496, 12.522802499956994],
    popup="Lærkereden",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.66411100282259, 12.540897949954955],
    popup="Midtfløjene/Grostedet",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.668060, 12.552470],
    popup="Klatretræet på Vesterbro",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69984468275925, 12.585553369949551],
    popup="BørnenesVerden",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71374538274213, 12.579703559950248],
    popup="Barndommens Gade",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70479206275143, 12.588692709949141],
    popup="Daginstitutionen Vesterbro Børneliv",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.700085582759804, 12.58284827994989],
    popup="Stubmøllen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70864225274675, 12.58689175994936],
    popup="Børnehuset Scandiagade",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.704422492754226, 12.581783419950012],
    popup="Vesterbro Børnegård",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.704442642754145, 12.581971099949987],
    popup="Idrætsinstitutionen Bavnehøj",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.701019722756136, 12.590057179948982],
    popup="Flora",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71605254274418, 12.563660039952188],
    popup="Charlottehaven",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.715480, 12.565050],
    popup="Mælkebøtten",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70413285275413, 12.583249289949832],
    popup="Villa Nova",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.71270933277433, 12.479537019961317],
    popup="Vokseværket",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.720442892761604, 12.48694718996057],
    popup="Vuggestuen Junglebo",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.710361622779196, 12.473834039961876],
    popup="Konkylien",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.676826762797674, 12.564490239952184],
    popup="Børnehusene ved Skoven",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.66515441282183, 12.538726689955197],
    popup="Rosenvang",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69498913277743, 12.550070589953833],
    popup="Studsgården",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.686658752809294, 12.482259799961097],
    popup="Stjernen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69198262277253, 12.577960039950515],
    popup="Børnejunglen",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.69500368278589, 12.522659559956898],
    popup="Børnehuset Støberigade",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.655687902850225, 12.48725030996067],
    popup="Forfatterhuset",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.667994042825796, 12.513054989957991],
    popup="Børnehuset Vesterbro",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.86316582255901, 12.506755639958234],
    popup="Damperen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.72406298273279, 12.564926219952019],
    popup="Hulahophuset",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.64783348284658, 12.535276399955622],
    popup="Børnehuset Tusindfryd",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.667800022797884, 12.601141989947644],
    popup="Humlehuset",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.652190, 12.532400],
    popup="Børnegården Frederiksholm",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.66553687282417, 12.529564239956214],
    popup="Børnehuset Håbets Allé - Børnehave",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.77433276267312, 12.535018169955364],
    popup="Grøndalen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.667994042825796, 12.513054989957991],
    popup="Isbjørnen",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.619818852873806, 12.570047169951662],
    popup="Børnehuset Jorn",
    icon=folium.Icon(color="orange", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.70191385276709, 12.55272761995351],
    popup="Olympia",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.643193, 12.508651],
    popup="Lyngholmen",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

folium.Marker(
    location=[55.664760, 12.595950],
    popup="Børnehuset i Svinget",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

map

