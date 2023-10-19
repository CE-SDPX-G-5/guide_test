from flask import Flask,jsonify


app = Flask (__name__)

app.app_context().push()

@app.route('/')
def index():
    return 'welcome'

@app.route('/next2/<i>',methods=['GET'])
def next2(i):

    try:
        try:
            i = int(i)
            resp = { 'msg' : (i+2) }
        except:
            i = int(i)    
            if i <= 0 :
                resp = { 'msg' : (i+2) }         
                
    except ValueError:
        try:
            i = float(i)
            resp = { 'msg' : (i+2) }
        except:
            i = str(i)
            resp = { 'msg' : 'error' }
     
    return jsonify(resp)   

if __name__ == "__main__":
    app.run()