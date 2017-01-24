from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
app = Flask(__name__)

app.secret_key = 'helloworld'

@app.route('/', methods = ['POST', 'GET'])
def index():
  nom = request.form.get('nom') or request.args.get('nom')
  methode = request.method

  # Si GET
  if (methode == 'GET' and request.args.get('nom')):
    return "Hello %s" % nom

  # Si POST
  elif(methode == 'POST'):
    if (request.form.get('nom_produit') or request.form.get('prix') or request.form.get('quantite')):
      quantite = int(request.form['quantite'] or 0)
      nom_produit = request.form.get('nom_produit')
      taxe = float(request.form.get('taxe2') or 5.5)
      prix = float(request.form['prix'] or 0) * quantite

      session['quantite'] += quantite
      session['prix'] += prix
      session['prixTTC'] += prix+(prix*(taxe/100.0))
      TVA = session['prixTTC'] - session['prix']

      if not (nom_produit in session['liste'] or quantite < 1):
        session['nb_produit'] += 1
        session['liste'].append(nom_produit)
      return render_template('index.html', nb_liste=session['nb_produit'], quantite=session['quantite'], prix=session['prix'], prixTTC=session['prixTTC'], TVA=TVA)
    elif (nom):
      return render_template('index.html', nom=nom)
    elif not (request.form.get('ajout_produit')):
      return render_template('index.html', nom="World")

  session['quantite'] = 0
  session['nb_produit'] = 0
  session['prix'] = 0
  session['liste'] = []
  session['prixTTC'] = 0

  return render_template('index.html')

@app.route('/RAZ')
def reset():
  session['quantite'] = 0
  session['nb_produit'] = 0
  session['prix'] = 0
  session['liste'] = []
  session['prixTTC'] = 0
  return redirect("/")

if __name__ == '__main__':
   app.run(debug = True)
