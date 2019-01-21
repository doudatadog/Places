import utils

def 	compute_nearest(latlons)										:

		stops  															= utils.pandas.read_csv('./static/Stops/data/stops.txt')

		coords 															= stops[['stop_lat','stop_lon']].values

		result 															= utils.distance.cdist(latlons,coords)

		result 															= utils.pandas.DataFrame(result).T

		result.columns 													= ['departure','arrival']

		result 															= utils.pandas.concat([stops,result],axis=1).assign(


			va 															= lambda DF : DF.arrival<utils.dlim/10.,
			vd 															= lambda DF : DF.departure<utils.dlim/10.)

		arrivals   														= result[result.va]

		departures 														= result[result.vd]

		arrivals['minutes'] 											= arrivals.arrival.apply(utils.Timer)
		departures['minutes'] 											= departures.departure.apply(utils.Timer)

		return  departures,arrivals