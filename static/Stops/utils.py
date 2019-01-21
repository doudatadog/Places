from opencage.geocoder 				import OpenCageGeocode
import 								sys,pandas,math
from scipy.spatial      			import distance

dlim								= 0.024960428141358584#euclidian dist for 31 mins

def Geocode(address,apikey) 		: 
	geocoder 						= OpenCageGeocode(apikey)
	result 							= geocoder.geocode(address)
	result							= (None,)*2 if len(result) == 0 else result[0][u'geometry'].values()
	return 							  result
def Timer(x) 					    :
	return 							pandas.np.ceil(x*(31/dlim))