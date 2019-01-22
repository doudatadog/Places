import utils,nearby_stops
apikey                          = '95180978743a4a4a843f2a47647bd4ae'

def 		Process(dep,arr)	:
			
			d,a                 = dep,arr
			infos               = [('departure',d),('arrival',a)]
			Geo                 = lambda X : (X[0],utils.Geocode(X[1],apikey) )
			infos               = dict(map(Geo,infos))
			departures,arrivals = nearby_stops.compute_nearest([infos['departure'],infos['arrival']])
			infos['arrival']    = {'latlon':[['{}'.format(a)],infos['arrival']],'stops':arrivals.fillna(0).apply(lambda x : [x[0],x['stop_lat'],x['stop_lon'],x['route_type']],1).tolist()}
			infos['departure']  = {'latlon':[['{}'.format(d)],infos['departure']],'stops':departures.fillna(0).apply(lambda x : [x[0],x['stop_lat'],x['stop_lon'],x['route_type']],1).tolist()}
			return                infos	