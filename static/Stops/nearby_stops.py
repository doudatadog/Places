import utils

def 	compute_nearest(latlons)     :
		stops                        = utils.pandas.read_hdf('./static/Stops/data/stops.h5',key='table')
		coords                       = stops[['stop_lat','stop_lon']].values
		result                       = utils.distance.cdist(latlons,coords)
		result                       = utils.pandas.DataFrame(result).T
		result.columns               = ['departure','arrival']
		result                       = utils.pandas.concat([stops,result],axis=1)
		arrivals                     = result.sort_values('arrival').head(100)
		departures                   = result.sort_values('departure').head(100)
		arrivals['minutes']          = arrivals.arrival.apply(utils.Timer)
		departures['minutes']        = departures.departure.apply(utils.Timer)
		return  departures,arrivals