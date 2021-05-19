 # Remember to pip install flask
from flask import render_template
import connexion

# Create an application instance (__name__ & template_folder are built in with Flask)
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route for "/" in our application
@app.route("/")
def home():
  return render_template('home.html')

# This part I don't get
if __name__ == '__main__':
  app.run(debug=True)

