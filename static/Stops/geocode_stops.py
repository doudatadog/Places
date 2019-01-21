import utils,nearby_stops

apikey                          = '95180978743a4a4a843f2a47647bd4ae'


def 		Processe(dep,arr)	:
			
			d,a 				= dep,arr
			infos 				= [('departure',d),('arrival',a)]
			Geo 				= lambda X : (X[0],utils.Geocode(X[1],apikey) )
			infos				= dict(map(Geo,infos))
			departures,arrivals	= nearby_stops.compute_nearest([infos['departure'],infos['arrival']])
			infos['arrival']	= {'latlon':infos['arrival'],'stops':arrivals.fillna(0).apply(lambda x : [x['stop_name'],x['stop_lat'],x['stop_lon']],1).tolist()}
			infos['departure']	= {'geo':infos['departure'],'stops':departures.fillna(0).apply(lambda x : [x['stop_lat'],x['stop_lon']],1).tolist()}
			return 				  infos	