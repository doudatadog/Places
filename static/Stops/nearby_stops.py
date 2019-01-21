import utils

def 	compute_nearest(latlons)										:

		stops  															= utils.pandas.read_csv('./static/Stops/data/stops.txt')

		coords 															= stops[['stop_lat','stop_lon']].values

		result 															= utils.distance.cdist(latlons,coords)

		result 															= utils.pandas.DataFrame(result).T

		result.columns 													= ['departure','arrival']

		result 															= utils.pandas.concat([stops,result],axis=1).assign(


			va 															= lambda DF : True,
			vd 															= lambda DF : True)

		arrivals   														= result[result.va].sort_values('arrival').head(10)

		departures 														= result[result.vd].sort_values('departure').head(10)

		arrivals['minutes'] 											= arrivals.arrival.apply(utils.Timer)
		departures['minutes'] 											= departures.departure.apply(utils.Timer)

		return  departures,arrivals