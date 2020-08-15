from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def contato(request):
    # Instancia o form em forms.py
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        # print(f'Post: {request.POST}')
        if form.is_valid():
            form.send_mail()

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # Check data - remove from the code
            # print('Mensagem Enviada:')
            # print(f'Nome: {nome}')
            # print(f'email: {email}')
            # print(f'assunto: {assunto}')
            # print(f'mensagem: {mensagem}')

            messages.success(request, 'Email Enviado com Sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    # POST has upload function
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)

        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preco: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')
            messages.success(request, 'Produto salvo com sucesso!')
        else:
            messages.error(request, 'Erro ao salvar o produto!')

    else:
        form = ProdutoModelForm()
        context = {
            'form': form
        }

    return render(request, 'produto.html', context)
