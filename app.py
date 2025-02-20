from flask import Flask,flash,session, request, jsonify,render_template,redirect,url_for
from flask_session import Session
app=Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
app.secret_key='mysecretkey'
app.config['SESSION_TYPE']='filesystem'
app.config['SESSION_PERMANENT']=False
Session(app)
# This is a todo app to create, update and delete todos
todos=[]

@app.route('/')
def index():

    if len(todos)>0:
        session['todos']=todos
        return render_template('index.html',todos=todos)
    else:
        flash('Welcome to the Todo App')
        return render_template('index.html')


@app.route('/add',methods=['POST'])
def add():
    flash('Todo Added')
    todo=request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete')
def delete():
    flash('Todo Deleted')
    id=request.args.get('id')
    todos.remove(id)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error':'Page not found'}),404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error':'Internal server error'}),500





if __name__=='__main__':
    app.run(host='0.0.0.0',port='8000')