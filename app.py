from   flask                import request,Flask, render_template
from static.Stops           import geocode_stops

app                         = Flask(__name__)


@app.route('/')
def home()                  : 
	return render_template('home.html')

@app.route('/geocode',methods=['POST'])

def geocode()               :
	dep,arr                 = request.form.values()
	result                  = geocode_stops.Process(dep,arr)
	return                    render_template('result.html',
					 result=result['departure']['stops'],
					   home=result['departure']['latlon'],
					   work=result['arrival']['latlon'])



if __name__ == '__main__'  :
	app.run(debug = True)