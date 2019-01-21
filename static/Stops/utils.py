from opencage.geocoder             import OpenCageGeocode
import                             sys,pandas,numpy as np
from scipy.spatial                 import distance

dlim                                = 0.024960428141358584#euclidian dist for 31 mins

def Geocode(address,apikey) 		: 
	geocoder                        = OpenCageGeocode(apikey)
	result                          = geocoder.geocode(address)
	result                          = (0.,)*2 if len(result) == 0 else result[0][u'geometry'].values()
	return                          result
def Timer(x) 					    : return np.ceil(x*(31/dlim));