from flask import Flask, render_template, redirect, request,flash, session

app = Flask(__name__)

app.secret_key ='unisales'


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/bem-vindo')
def perfil():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Usuario não autenticado, realize o login para acessar a pagina!')
        return redirect('/')
    return render_template('bem-vindo.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'admin' == request.form['senha'] and 'admin' == request.form['usuario']:
        session['usuario_logado'] = request.form['usuario']
        return redirect('/bem-vindo')
    else:
        flash('Usuario não autenticado, tente de novo!')
        return redirect('/')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect('/')

app.run(debug=True)