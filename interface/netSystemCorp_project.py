from tkinter import *  # Importa toda biblioteca do Tkinter
from tkinter import ttk
import tkinter.messagebox as tkMessagebox
from PIL import ImageTk, Image
import sqlite3


# CLASSE REFERENTE A JANELA DE CONSULTA
class consulta_window:

    def quit_window(self):
        self.root_consulta.destroy()

    def open_principalWindow(self):
        self.quit_window()
        principalwindow()

    def __init__(self):
        self.root_consulta = Tk()
        self.root_consulta.title("NetSystemCorp - Consulta")
        self.root_consulta['bg'] = "grey21"
        self.root_consulta.geometry('700x400+400+100')
        self.root_consulta.iconbitmap('img\logo01.ico')
        self.root_consulta.resizable(0, 0)
        self.root_consulta.overrideredirect(True)
        # ----------------------------------------------------

        # CENTRALIZA TELA
        self.root_consulta.withdraw()
        self.root_consulta.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_consulta.winfo_screenwidth() - self.root_consulta.winfo_reqwidth()) / 2
        y = (self.root_consulta.winfo_screenheight() - self.root_consulta.winfo_reqheight()) / 4
        self.root_consulta.geometry("+%d+%d" % (x, y))

        frameTop = Frame(
            self.root_consulta,
            height=70,
            width=700,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_InfTop = Label(
            frameTop,
            text='Consulta',
            bg="grey21",
            fg='#f2f2f2',
            font='Arial 10 bold')

        # ----------------------------------------------------
        frameCenter = Frame(
            self.root_consulta,
            relief='groove',
            bd=4,
            height=100,
            width=650,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_codConsulta = Label(
            self.root_consulta,
            text='CÓDIGO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_nomeConsulta_funcao = Label(
            self.root_consulta,
            text='NOME',
            bg='grey21',
            font='Arial 7 ',
            fg='#f2f2f2')
        label_prodConsulta = Label(
            self.root_consulta,
            text='PROD.',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_clienteConsulta = Label(
            self.root_consulta,
            text='CLIENTE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_funcConsulta = Label(
            self.root_consulta,
            text='FUNC.',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cargoConsulta = Label(
            self.root_consulta,
            text='FUNÇÃO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')

        opcao = IntVar()
        rbtn_prod = Radiobutton(self.root_consulta, text='Produto', bg='grey21', fg='white', variable=opcao, value=1)
        rbtn_cliente = Radiobutton(self.root_consulta, text='Cliente', bg='grey21', fg='white', variable=opcao, value=2)
        rbtn_func = Radiobutton(self.root_consulta, text='Funcionario', bg='grey21', fg='white', variable=opcao,
                                value=3)
        rbtn_cargos = Radiobutton(self.root_consulta, text='Função', bg='grey21', fg='white', variable=opcao, value=4)
        rbtn_prod.select()

        frameSearch = Frame(
            self.root_consulta,
            relief='groove',
            bd=4,
            height=200,
            width=650,
            bg="grey21"
        )
        # BOTÃO ------------------------------
        btn_sair = Button(self.root_consulta, text='CANCELAR', width=10, command=lambda: self.open_principalWindow())
        btn_atualizar = Button(self.root_consulta, text='ATUALIZAR', width=15)
        btn_pesquisar = Button(self.root_consulta, text='PESQUISAR', width=15)

        # RADIOBUTTON
        rbtn_prod.place(x=205, y=140)
        rbtn_cliente.place(x=310, y=140)
        rbtn_func.place(x=405, y=140)
        rbtn_cargos.place(x=510, y=140)
        # ENTRY

        txt_codConsulta = Entry(self.root_consulta, width=13)
        txt_nomeConsulta = Entry(self.root_consulta, width=65)

        # ----------------------------------------------------

        frameRodape = Frame(
            self.root_consulta,
            height=10,
            width=700,
            bg="grey21",
        )
        label_InfRodape = Label(
            frameRodape,
            text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
            bg="grey21",
            fg='white',
            font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTop.grid(row=0, column=0)

        frameCenter.grid(row=1, column=0, padx=22)

        frameSearch.grid(row=2, column=0, padx=22)

        frameRodape.grid(row=3, column=0, columnspan=3)

        # BOTÃO
        btn_sair.place(x=595, y=40)
        btn_atualizar.place(x=465, y=40)
        btn_pesquisar.place(x=550, y=95)

        # LABEL

        label_InfTop.place(x=20, y=10)
        label_codConsulta.place(x=40, y=75)
        label_nomeConsulta_funcao.place(x=140, y=75)
        label_InfRodape.grid(row=2, column=0, columnspan=3)

        # ENTRY
        txt_codConsulta.place(x=40, y=95, height=25)
        txt_nomeConsulta.place(x=140, y=95, height=25)

        self.root_consulta.deiconify()
        self.root_consulta.mainloop()


# CLASSE REFERENTE A JANELA CADASTRO DE FUNÇÃO
class cadFuncao_window:
    def quit_window(self):
        self.root_cadFuncao.destroy()

    def open_principalWindow(self):
        self.quit_window()
        principalwindow()

    def __init__(self):
        self.root_cadFuncao = Tk()
        self.root_cadFuncao.title("NetSystemCorp - Cadastro de Função")
        self.root_cadFuncao['bg'] = "grey21"
        self.root_cadFuncao.geometry('700x400+400+100')
        self.root_cadFuncao.iconbitmap('img\logo01.ico')
        self.root_cadFuncao.resizable(0, 0)
        self.root_cadFuncao.overrideredirect(True)
        # ----------------------------------------------------

        # CENTRALIZA TELA
        self.root_cadFuncao.withdraw()
        self.root_cadFuncao.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_cadFuncao.winfo_screenwidth() - self.root_cadFuncao.winfo_reqwidth()) / 2
        y = (self.root_cadFuncao.winfo_screenheight() - self.root_cadFuncao.winfo_reqheight()) / 4
        self.root_cadFuncao.geometry("+%d+%d" % (x, y))

        frameTop = Frame(
            self.root_cadFuncao,
            height=70,
            width=700,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_InfTop = Label(
            frameTop,
            text='Cadastro de Função',
            bg="grey21",
            fg='#f2f2f2',
            font='Arial 10 bold')

        # BOTÃO ------------------------------
        btn_cancelar = Button(self.root_cadFuncao, text='CANCELAR', width=10,
                              command=lambda: self.open_principalWindow())
        btn_gravar = Button(self.root_cadFuncao, text='GRAVAR', width=10)

        # ----------------------------------------------------
        frameCenter = Frame(
            self.root_cadFuncao,
            relief='groove',
            bd=4,
            height=300,
            width=650,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_cod_funcao = Label(
            self.root_cadFuncao,
            text='COD.FUNÇÃO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_nomeFuncao_funcao = Label(
            self.root_cadFuncao,
            text='NOME DA FUNÇÃO',
            bg='grey21',
            font='Arial 7 ',
            fg='#f2f2f2')
        label_salario_funcao = Label(
            self.root_cadFuncao,
            text='SALÁRIO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_setor_funcao = Label(
            self.root_cadFuncao,
            text='SETOR',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')

        # ENTRY

        txt_cod_funcao = Entry(self.root_cadFuncao, width=13)
        txt_numCadastro_funcao = Entry(self.root_cadFuncao, width=50)
        txt_salario_funcao = Entry(self.root_cadFuncao, width=20)
        txt_setor_funcao = Entry(self.root_cadFuncao, width=11)
        txt_cod_funcao.focus()
        # ----------------------------------------------------

        frameRodape = Frame(
            self.root_cadFuncao,
            height=10,
            width=700,
            bg="grey21",
        )
        label_InfRodape = Label(
            frameRodape,
            text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
            bg="grey21",
            fg='white',
            font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTop.grid(row=0, column=0)

        frameCenter.grid(row=1, column=0, padx=22)

        frameRodape.grid(row=2, column=0, columnspan=3)

        # BOTÃO
        btn_cancelar.place(x=490, y=40)
        btn_gravar.place(x=590, y=40)

        # LABEL

        label_InfTop.place(x=20, y=10)
        label_cod_funcao.place(x=40, y=75)
        label_nomeFuncao_funcao.place(x=140, y=75)
        label_salario_funcao.place(x=455, y=75)
        label_setor_funcao.place(x=590, y=75)
        label_InfRodape.grid(row=2, column=0, columnspan=3)

        # ENTRY
        txt_cod_funcao.place(x=40, y=95, height=25)
        txt_numCadastro_funcao.place(x=140, y=95, height=25)
        txt_salario_funcao.place(x=455, y=95, height=25)
        txt_setor_funcao.place(x=590, y=95, height=25)

        self.root_cadFuncao.deiconify()
        self.root_cadFuncao.mainloop()


# CLASSE REFERENTE A JANELA CADASTRO DE FUNCIONÁRIOS
class cadFuncionario_window:
    def quit_window(self):
        self.root_cadFuncionario.destroy()

    def open_principalWindow(self):
        self.quit_window()
        principalwindow()

    def __init__(self):
        self.root_cadFuncionario = Tk()
        self.root_cadFuncionario.title("NetSystemCorp - Cadastro de Funcionário")
        self.root_cadFuncionario['bg'] = "grey21"
        self.root_cadFuncionario.geometry('700x700+400+100')
        self.root_cadFuncionario.iconbitmap('img\logo01.ico')
        self.root_cadFuncionario.resizable(0, 0)
        self.root_cadFuncionario.overrideredirect(True)
        # ----------------------------------------------------

        # CENTRALIZA TELA
        self.root_cadFuncionario.withdraw()
        self.root_cadFuncionario.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_cadFuncionario.winfo_screenwidth() - self.root_cadFuncionario.winfo_reqwidth()) / 2
        y = (self.root_cadFuncionario.winfo_screenheight() - self.root_cadFuncionario.winfo_reqheight()) / 4
        self.root_cadFuncionario.geometry("+%d+%d" % (x, y))

        frameTop = Frame(
            self.root_cadFuncionario,
            height=70,
            width=700,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_InfTop = Label(
            frameTop,
            text='Cadastro de Funcionário',
            bg="grey21",
            fg='#f2f2f2',
            font='Arial 10 bold')

        # BOTÃO ------------------------------
        btn_cancelar = Button(
            self.root_cadFuncionario,
            text='CANCELAR',
            width=10,
            command=lambda: self.open_principalWindow()
        )
        btn_gravar = Button(
            self.root_cadFuncionario,
            text='GRAVAR',
            width=10)
        # ----------------------------------------------------

        frameCenter = Frame(
            self.root_cadFuncionario,
            relief='groove',
            bd=4,
            height=400,
            width=650,
            bg="grey21")

        frameboxLogin = Frame(
            self.root_cadFuncionario,
            relief='groove',
            bd=4,
            height=170,
            width=650,
            bg="grey21"
        )
        btn_cadastrarUsuario = Button(self.root_cadFuncionario, text='CADASTRAR', width=10)
        label_InfBoxLogin = Label(
            self.root_cadFuncionario,
            text='Cadastro de Usuário para o uso do sistema',
            bg="grey21",
            fg='#f2f2f2',
            font='Arial 10 bold')
        # LABEL ------------------------------
        label_cod_funcionario = Label(
            self.root_cadFuncionario,
            text='COD.FUNC',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_nome_funcionario = Label(
            self.root_cadFuncionario,
            text='NOME',
            bg='grey21',
            font='Arial 7 ',
            fg='#f2f2f2')
        label_sexo_funcionario = Label(
            self.root_cadFuncionario,
            text='SEXO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_estadoCivil_funcionario = Label(
            self.root_cadFuncionario,
            text='ESTADO CIVIL',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_rg_funcionario = Label(
            self.root_cadFuncionario,
            text='RG',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cpf_funcionario = Label(
            self.root_cadFuncionario,
            text='CPF',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cnh_funcionario = Label(
            self.root_cadFuncionario,
            text='CNH',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_dataDeNascimento_funcionario = Label(
            self.root_cadFuncionario,
            text='DATA DE NASC.',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_ufNascimento_funcionario = Label(
            self.root_cadFuncionario,
            text='UF',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_filhos_funcionario = Label(
            self.root_cadFuncionario,
            text='FILHOS',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_ctps_funcionario = Label(
            self.root_cadFuncionario,
            text='CTPS',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_pis_funcionario = Label(
            self.root_cadFuncionario,
            text='PIS',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_escolaridade_funcionario = Label(
            self.root_cadFuncionario,
            text='ESCOLARIDADE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_rua_funcionario = Label(
            self.root_cadFuncionario,
            text='RUA / AV.',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_numero_funcionario = Label(
            self.root_cadFuncionario,
            text='N°',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_complemento_funcionario = Label(
            self.root_cadFuncionario,
            text='COMPLEMENTO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_bairro_funcionario = Label(
            self.root_cadFuncionario,
            text='BAIRRO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cidade_funcionario = Label(
            self.root_cadFuncionario,
            text='CIDADE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cep_funcionario = Label(
            self.root_cadFuncionario,
            text='CEP',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_ufAtual_funcionario = Label(
            self.root_cadFuncionario,
            text='UF',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_email_funcionario = Label(
            self.root_cadFuncionario,
            text='E-MAIL',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_dddTelefone_funcionario = Label(
            self.root_cadFuncionario,
            text='DDD',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_telefone_funcionario = Label(
            self.root_cadFuncionario,
            text='TELEFONE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_dddCelular_funcionario = Label(
            self.root_cadFuncionario,
            text='DDD',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_celular_funcionario = Label(
            self.root_cadFuncionario,
            text='CELULAR',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_funcao_funcionario = Label(
            self.root_cadFuncionario,
            text='FUNÇÃO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_salario_funcionario = Label(
            self.root_cadFuncionario,
            text='SALÁRIO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_turno_funcionario = Label(
            self.root_cadFuncionario,
            text='TURNO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_tipoDeContrato_funcionario = Label(
            self.root_cadFuncionario,
            text='TIPO DE CONTRATO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_usuarioCadLogin_funcionario = Label(
            self.root_cadFuncionario,
            text='USUÁRIO',
            bg='grey21',
            font='Arial 10 bold',
            fg='#f2f2f2')
        label_senhaCadLogin_funcionario = Label(
            self.root_cadFuncionario,
            text='SENHA ',
            bg='grey21',
            font='Arial 10 bold',
            fg='#f2f2f2')
        self.photo = PhotoImage(file="img\photoUsuario.png")
        label_photo = Label(self.root_cadFuncionario, image=self.photo, width=110, height=97, bg='grey21')
        # ENTRY

        txt_cod_funcionario = Entry(self.root_cadFuncionario, width=9)
        txt_nome_funcionario = Entry(self.root_cadFuncionario, width=35)
        txt_sexo_funcionario = Entry(self.root_cadFuncionario, width=11)
        txt_estadoCivil_funcionario = Entry(self.root_cadFuncionario, width=13)
        txt_rg_funcionario = Entry(self.root_cadFuncionario, width=15)
        txt_cpf_funcionario = Entry(self.root_cadFuncionario, width=15)
        txt_cnh_funcionario = Entry(self.root_cadFuncionario, width=15)
        txt_dataDeNascimento_funcionario = Entry(self.root_cadFuncionario, width=15)
        txt_ufNascimento_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_filhos_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_ctps_funcionario = Entry(self.root_cadFuncionario, width=35)
        txt_pis_funcionario = Entry(self.root_cadFuncionario, width=35)
        txt_escolaridade_funcionario = Entry(self.root_cadFuncionario, width=12)
        txt_rua_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_numero_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_complemento_funcionario = Entry(self.root_cadFuncionario, width=12)
        txt_bairro_funcionario = Entry(self.root_cadFuncionario, width=34)
        txt_cidade_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_cep_funcionario = Entry(self.root_cadFuncionario, width=10)
        txt_ufAtual_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_email_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_dddTelefone_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_telefone_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_dddCelular_funcionario = Entry(self.root_cadFuncionario, width=8)
        txt_celular_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_funcao_funcionario = Entry(self.root_cadFuncionario, width=25)
        txt_salario_funcionario = Entry(self.root_cadFuncionario, width=25)
        txt_turno_funcionario = Entry(self.root_cadFuncionario, width=25)
        txt_tipoDeContrato_funcionario = Entry(self.root_cadFuncionario, width=17)
        txt_usuarioCadLogin_funcionario = Entry(self.root_cadFuncionario, width=36)
        txt_senhaCadLogin_funcionario = Entry(self.root_cadFuncionario, width=36)

        # ----------------------------------------------------

        frameButtom = Frame(
            self.root_cadFuncionario,
            height=10,
            width=700,
            bg="grey21",
        )
        label_InfButtom = Label(
            frameButtom,
            text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
            bg="grey21",
            fg='white',
            font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTop.grid(row=0, column=0)
        frameCenter.grid(row=1, column=0, padx=22)
        frameboxLogin.grid(row=2, column=0)
        frameButtom.grid(row=3, column=0, columnspan=3)

        # BOTÃO
        btn_cancelar.place(x=490, y=40)
        btn_gravar.place(x=590, y=40)
        btn_cadastrarUsuario.place(x=270, y=600)

        # LABEL

        label_InfTop.place(x=20, y=10)
        label_cod_funcionario.place(x=167, y=75)
        label_nome_funcionario.place(x=250, y=75)
        label_sexo_funcionario.place(x=485, y=75)
        label_estadoCivil_funcionario.place(x=575, y=75)
        label_rg_funcionario.place(x=167, y=130)
        label_cpf_funcionario.place(x=280, y=130)
        label_cnh_funcionario.place(x=390, y=130)
        label_dataDeNascimento_funcionario.place(x=500, y=130)
        label_ufNascimento_funcionario.place(x=605, y=130)
        label_filhos_funcionario.place(x=45, y=180)
        label_ctps_funcionario.place(x=115, y=180)
        label_pis_funcionario.place(x=350, y=180)
        label_escolaridade_funcionario.place(x=580, y=180)
        label_rua_funcionario.place(x=45, y=230)
        label_numero_funcionario.place(x=285, y=230)
        label_complemento_funcionario.place(x=355, y=230)
        label_bairro_funcionario.place(x=450, y=230)
        label_cidade_funcionario.place(x=45, y=280)
        label_cep_funcionario.place(x=285, y=280)
        label_ufAtual_funcionario.place(x=368, y=280)
        label_email_funcionario.place(x=440, y=280)
        label_dddTelefone_funcionario.place(x=45, y=330)
        label_telefone_funcionario.place(x=115, y=330)
        label_dddCelular_funcionario.place(x=363, y=330)
        label_celular_funcionario.place(x=442, y=330)
        label_funcao_funcionario.place(x=45, y=380)
        label_salario_funcionario.place(x=215, y=380)
        label_turno_funcionario.place(x=385, y=380)
        label_tipoDeContrato_funcionario.place(x=555, y=380)
        label_InfBoxLogin.place(x=200, y=480)
        label_usuarioCadLogin_funcionario.place(x=200, y=525)
        label_senhaCadLogin_funcionario.place(x=215, y=560)
        label_InfButtom.grid(row=3, column=0, columnspan=3)
        label_photo.place(x=45, y=80)

        # ENTRY
        txt_cod_funcionario.place(x=170, y=95, height=25)
        txt_nome_funcionario.place(x=250, y=95, height=25)
        txt_sexo_funcionario.place(x=485, y=95, height=25)
        txt_estadoCivil_funcionario.place(x=575, y=95, height=25)
        txt_rg_funcionario.place(x=170, y=145, height=25)
        txt_cpf_funcionario.place(x=280, y=145, height=25)
        txt_cnh_funcionario.place(x=390, y=145, height=25)
        txt_dataDeNascimento_funcionario.place(x=500, y=145, height=25)
        txt_ufNascimento_funcionario.place(x=605, y=145, height=25)
        txt_filhos_funcionario.place(x=45, y=195, height=25)
        txt_ctps_funcionario.place(x=115, y=195, height=25)
        txt_pis_funcionario.place(x=350, y=195, height=25)
        txt_escolaridade_funcionario.place(x=580, y=195, height=25)
        txt_rua_funcionario.place(x=45, y=245, height=25)
        txt_numero_funcionario.place(x=285, y=245, height=25)
        txt_complemento_funcionario.place(x=355, y=245, height=25)
        txt_bairro_funcionario.place(x=450, y=245, height=25)
        txt_cidade_funcionario.place(x=45, y=295, height=25)
        txt_cep_funcionario.place(x=285, y=295, height=25)
        txt_ufAtual_funcionario.place(x=368, y=295, height=25)
        txt_email_funcionario.place(x=440, y=295, height=25)
        txt_dddTelefone_funcionario.place(x=45, y=345, height=25)
        txt_telefone_funcionario.place(x=115, y=345, height=25)
        txt_dddCelular_funcionario.place(x=363, y=345, height=25)
        txt_celular_funcionario.place(x=442, y=345, height=25)
        txt_funcao_funcionario.place(x=45, y=395, height=25)
        txt_salario_funcionario.place(x=215, y=395, height=25)
        txt_turno_funcionario.place(x=385, y=395, height=25)
        txt_tipoDeContrato_funcionario.place(x=555, y=395, height=25)
        txt_usuarioCadLogin_funcionario.place(x=270, y=525, height=25)
        txt_senhaCadLogin_funcionario.place(x=270, y=560, height=25)
        txt_cod_funcionario.focus()

        self.root_cadFuncionario.deiconify()
        self.root_cadFuncionario.mainloop()


# CLASSE REFERENTE A JANELA CADASTRO DE CLIENTE
class cadCliente_window:
    def quit_window(self):
        self.root_cadCliente.destroy()

    def open_principalWindow(self):
        self.quit_window()
        principalwindow()

    def __init__(self):
        self.root_cadCliente = Tk()
        self.root_cadCliente.title("NetSystemCorp - Cadastro de Cliente")
        self.root_cadCliente['bg'] = "grey21"
        self.root_cadCliente.geometry('700x400+400+100')
        self.root_cadCliente.iconbitmap('img\logo01.ico')
        self.root_cadCliente.resizable(0, 0)
        self.root_cadCliente.overrideredirect(True)
        # ----------------------------------------------------

        # CENTRALIZA TELA
        self.root_cadCliente.withdraw()
        self.root_cadCliente.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_cadCliente.winfo_screenwidth() - self.root_cadCliente.winfo_reqwidth()) / 2
        y = (self.root_cadCliente.winfo_screenheight() - self.root_cadCliente.winfo_reqheight()) / 4
        self.root_cadCliente.geometry("+%d+%d" % (x, y))

        frameTop = Frame(
            self.root_cadCliente,
            height=70,
            width=700,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_InfTop = Label(
            frameTop,
            text='Cadastro de Cliente',
            bg="grey21",
            fg='#f2f2f2',
            font='Arial 10 bold')

        # BOTÃO ------------------------------
        btn_cancelar_cliente = Button(self.root_cadCliente, text='CANCELAR', width=10,
                                      command=lambda: self.open_principalWindow())
        btn_gravar_cliente = Button(self.root_cadCliente, text='GRAVAR', width=10)

        # ----------------------------------------------------
        frameCenter = Frame(
            self.root_cadCliente,
            relief='groove',
            bd=4,
            height=300,
            width=650,
            bg="grey21"
        )

        # LABEL ------------------------------
        label_cod_cliente = Label(
            self.root_cadCliente,
            text='COD.CLIENTE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')

        label_nome_cliente = Label(
            self.root_cadCliente,
            text='NOME',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_nomeFantasia_cliente = Label(
            self.root_cadCliente,
            text='NOME FANTASIA',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_rua_cliente = Label(
            self.root_cadCliente,
            text='RUA / AV.',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_numero_cliente = Label(
            self.root_cadCliente,
            text='NUMERO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_bairro_cliente = Label(
            self.root_cadCliente,
            text='BAIRRO',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_email_cliente = Label(
            self.root_cadCliente,
            text='E-MAIL',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_ddd_cliente = Label(
            self.root_cadCliente,
            text='DDD',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_telefone_cliente = Label(
            self.root_cadCliente,
            text='TELEFONE',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_cnpj_cliente = Label(
            self.root_cadCliente,
            text='CNPJ',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_insEstadual_cliente = Label(
            self.root_cadCliente,
            text='INS.ESTADUAL',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')
        label_insMunicipal_cliente = Label(
            self.root_cadCliente,
            text='INS.MUNICIPAL',
            bg='grey21',
            font='Arial 7',
            fg='#f2f2f2')

        # ENTRY

        txt_cod_cliente = Entry(self.root_cadCliente, width=13)
        txt_nome_cliente = Entry(self.root_cadCliente, width=48)
        txt_nomeFantasia_cliente = Entry(self.root_cadCliente, width=50)
        txt_rua_cliente = Entry(self.root_cadCliente, width=48, )
        txt_numero_cliente = Entry(self.root_cadCliente, width=7)
        txt_bairro_cliente = Entry(self.root_cadCliente, width=38)
        txt_email_cliente = Entry(self.root_cadCliente, width=48)
        txt_ddd_cliente = Entry(self.root_cadCliente, width=7)
        txt_telefone_cliente = Entry(self.root_cadCliente, width=38)
        txt_cnpj_cliente = Entry(self.root_cadCliente, width=30)
        txt_insEstadual_cliente = Entry(self.root_cadCliente, width=30)
        txt_insMunicipal_cliente = Entry(self.root_cadCliente, width=32)
        txt_cod_cliente.focus()

        # ----------------------------------------------------

        frameButtom = Frame(
            self.root_cadCliente,
            height=10,
            width=700,
            bg="grey21",
        )
        label_InfButtom = Label(
            frameButtom,
            text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
            bg="grey21",
            fg='white',
            font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTop.grid(row=0, column=0)

        frameCenter.grid(row=1, column=0, padx=22)

        frameButtom.grid(row=2, column=0, columnspan=3)

        # BOTÃO
        btn_cancelar_cliente.place(x=490, y=40)
        btn_gravar_cliente.place(x=590, y=40)

        # LABEL

        label_InfTop.place(x=20, y=10)
        label_cod_cliente.place(x=40, y=75)
        label_nome_cliente.place(x=40, y=130)
        label_nomeFantasia_cliente.place(x=355, y=130)
        label_rua_cliente.place(x=40, y=180)
        label_numero_cliente.place(x=355, y=180)
        label_bairro_cliente.place(x=430, y=180)
        label_email_cliente.place(x=40, y=230)
        label_ddd_cliente.place(x=355, y=230)
        label_telefone_cliente.place(x=430, y=230)
        label_cnpj_cliente.place(x=40, y=280)
        label_insEstadual_cliente.place(x=250, y=280)
        label_insMunicipal_cliente.place(x=460, y=280)
        label_InfButtom.grid(row=2, column=0, columnspan=3)

        # ENTRY
        txt_cod_cliente.place(x=40, y=95, height=25)
        txt_nome_cliente.place(x=40, y=150, height=25)
        txt_nomeFantasia_cliente.place(x=355, y=150, height=25)
        txt_rua_cliente.place(x=40, y=200, height=25)
        txt_numero_cliente.place(x=355, y=200, height=25)
        txt_bairro_cliente.place(x=425, y=200, height=25)
        txt_email_cliente.place(x=40, y=250, height=25)
        txt_ddd_cliente.place(x=355, y=250, height=25)
        txt_telefone_cliente.place(x=425, y=250, height=25)
        txt_cnpj_cliente.place(x=40, y=300, height=25)
        txt_insEstadual_cliente.place(x=250, y=300, height=25)
        txt_insMunicipal_cliente.place(x=460, y=300, height=25)
        txt_cod_cliente.focus()
        self.root_cadCliente.deiconify()
        self.root_cadCliente.mainloop()


# CLASSE REFERENTE A JANELA CADASTRO DE PRODUTOS
class cadProduto_window:

    def validacaoCadProduto(self, codigo, numCadastro, descricao, unidade, observacao, fornecedor, fabricante,
                            valorUnit, codBarras, peso, ):

        codigo = codigo.get()
        numCadastro = numCadastro.get()

        descricao = descricao.get()
        unidade = unidade.get()
        observacao = observacao.get()
        fornecedor = fornecedor.get()
        fabricante = fabricante.get()
        valorUnit = valorUnit.get()
        codBarras = codBarras.get()
        peso = peso.get()

        if codigo == "":

            label_aviso = Label(self.root_cadProduto, text='Insira o codigo do produto          ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif numCadastro == "":
            label_aviso = Label(self.root_cadProduto, text='Insira um número para o produto     ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif descricao == "":

            label_aviso = Label(self.root_cadProduto, text='Insira uma descrição para o produto   ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif unidade == "":
            label_aviso = Label(self.root_cadProduto, text='Insira uma unidade para o produto       ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)


        elif observacao == "":
            label_aviso = Label(self.root_cadProduto, text='Insira uma observação para o produto      ', bg="grey21",
                                fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif fornecedor == "":
            label_aviso = Label(self.root_cadProduto, text='Insira o nome do fornecedor                ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)


        elif fabricante == "":
            label_aviso = Label(self.root_cadProduto, text='Insira o nome do fabricante do produto         ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif valorUnit == "":
            label_aviso = Label(self.root_cadProduto, text='insira o valor unitario do produto              ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)


        elif codBarras == "":
            label_aviso = Label(self.root_cadProduto, text='insira o código de barras do produto              ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)

        elif peso == "":
            label_aviso = Label(self.root_cadProduto, text='Insira o peso do produto                      ', bg="grey21", fg='red',
                                font='Arial 10 bold')
            label_aviso.place(x=20, y=30)
        else:
            tkMessagebox.showinfo("ATENÇÃO!!!", "Produto Cadastrado com sucesso!")
            self.open_principalWindow()

    def quit_window(self):
        self.root_cadProduto.destroy()

    def open_principalWindow(self):
        self.quit_window()
        principalwindow()

    def __init__(self):

        self.root_cadProduto = Tk()
        self.root_cadProduto.title("NetSystemCorp - Cadastro de Produto")
        self.root_cadProduto['bg'] = "grey21"
        self.root_cadProduto.geometry('700x400+400+100')
        self.root_cadProduto.iconbitmap('img\logo01.ico')
        self.root_cadProduto.resizable(0, 0)
        self.root_cadProduto.overrideredirect(True)
        # ----------------------------------------------------

        # CENTRALIZA TELA
        self.root_cadProduto.withdraw()
        self.root_cadProduto.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_cadProduto.winfo_screenwidth() - self.root_cadProduto.winfo_reqwidth()) / 2
        y = (self.root_cadProduto.winfo_screenheight() - self.root_cadProduto.winfo_reqheight()) / 4
        self.root_cadProduto.geometry("+%d+%d" % (x, y))

        frameTop = Frame(self.root_cadProduto, height=70, width=700, bg="grey21")

        # LABEL ------------------------------
        label_InfTop = Label(frameTop, text='Cadastro de Produtos', bg="grey21", fg='#f2f2f2', font='Arial 10 bold')

        # ----------------------------------------------------
        frameCenter = Frame(self.root_cadProduto, relief='groove', bd=4, height=300, width=650, bg="grey21"
                            )

        # LABEL ------------------------------
        label_cod_cadastro = Label(self.root_cadProduto, text='COD.CADASTRO', bg='grey21', font='Arial 7', fg='#f2f2f2')

        label_numCad_cadastro = Label(self.root_cadProduto, text='NUM. CADASTRO', bg='grey21', font='Arial 7 ',
                                      fg='#f2f2f2')

        label_descricao_cadastro = Label(self.root_cadProduto, text='DESCRIÇÃO', bg='grey21', font='Arial 7',
                                         fg='#f2f2f2')

        label_unidade_cadastro = Label(self.root_cadProduto, text='UNIDADE', bg='grey21', font='Arial 7', fg='#f2f2f2')
        label_observacao_cadastro = Label(self.root_cadProduto, text='OBSERVAÇÃO', bg='grey21', font='Arial 7',
                                          fg='#f2f2f2')

        label_fornecedor_cadastro = Label(self.root_cadProduto, text='FORNECEDOR', bg='grey21', font='Arial 7',
                                          fg='#f2f2f2')

        label_marca_cadastro = Label(self.root_cadProduto, text='FABRICANTE', bg='grey21', font='Arial 7', fg='#f2f2f2')
        label_valorUnit_cadastro = Label(self.root_cadProduto, text='VALOR UNIT', bg='grey21', font='Arial 7',
                                         fg='#f2f2f2')

        label_codDeBarras_cadastro = Label(self.root_cadProduto, text='COD. DE BARRAS', bg='grey21', font='Arial 7',
                                           fg='#f2f2f2')

        label_peso_cadastro = Label(self.root_cadProduto, text='PESO', bg='grey21', font='Arial 7', fg='#f2f2f2')

        # ENTRY

        txt_cod_cadastro = Entry(self.root_cadProduto, width=13)
        txt_numCadastro_cadastro = Entry(self.root_cadProduto, width=11)
        txt_descricao_cadastro = Entry(self.root_cadProduto, width=86)
        txt_unidade_cadastro = Entry(self.root_cadProduto, width=11)
        txt_observacao_cadastro = Entry(self.root_cadProduto, width=103)
        txt_fornecedor_cadastro = Entry(self.root_cadProduto, width=51)
        txt_marca_cadastro = Entry(self.root_cadProduto, width=46)
        txt_valorUnit_cadastro = Entry(self.root_cadProduto, width=16)
        txt_codBarras_cadastro = Entry(self.root_cadProduto, width=61)
        txt_peso_cadastro = Entry(self.root_cadProduto, width=16)
        txt_cod_cadastro.focus()

        # ----------------------------------------------------
        # BOTÃO ------------------------------
        btn_cancelar = Button(self.root_cadProduto, text='CANCELAR', width=10,
                              command=lambda: self.open_principalWindow())
        btn_gravar = Button(self.root_cadProduto, text='SALVAR', width=10,
                            command=lambda: self.validacaoCadProduto(txt_cod_cadastro, txt_numCadastro_cadastro,
                                                                     txt_descricao_cadastro, txt_unidade_cadastro,
                                                                     txt_observacao_cadastro, txt_fornecedor_cadastro,
                                                                     txt_marca_cadastro, txt_valorUnit_cadastro,
                                                                     txt_codBarras_cadastro, txt_peso_cadastro))

        frameButtom = Frame(self.root_cadProduto, height=10, width=700, bg="grey21")
        label_InfButtom = Label(frameButtom, text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
                                bg="grey21", fg='white', font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTop.grid(row=0, column=0)

        frameCenter.grid(row=1, column=0, padx=22)

        frameButtom.grid(row=2, column=0, columnspan=3)

        # BOTÃO
        btn_cancelar.place(x=490, y=40)
        btn_gravar.place(x=590, y=40)

        # LABEL

        label_InfTop.place(x=20, y=10)

        label_cod_cadastro.place(x=40, y=75)
        label_numCad_cadastro.place(x=585, y=75)
        label_descricao_cadastro.place(x=40, y=130)
        label_unidade_cadastro.place(x=585, y=130)
        label_observacao_cadastro.place(x=40, y=180)
        label_fornecedor_cadastro.place(x=40, y=230)
        label_marca_cadastro.place(x=380, y=230)
        label_valorUnit_cadastro.place(x=40, y=280)
        label_codDeBarras_cadastro.place(x=163, y=280)
        label_peso_cadastro.place(x=555, y=280)
        label_InfButtom.grid(row=2, column=0, columnspan=3)

        # ENTRY
        txt_cod_cadastro.place(x=40, y=95, height=25)
        txt_numCadastro_cadastro.place(x=590, y=95, height=25)
        txt_descricao_cadastro.place(x=40, y=150, height=25)
        txt_unidade_cadastro.place(x=590, y=150, height=25)
        txt_observacao_cadastro.place(x=40, y=200, height=25)
        txt_fornecedor_cadastro.place(x=40, y=250, height=25)
        txt_marca_cadastro.place(x=381, y=250, height=25)
        txt_valorUnit_cadastro.place(x=40, y=300, height=25)
        txt_codBarras_cadastro.place(x=165, y=300, height=25)
        txt_peso_cadastro.place(x=560, y=300, height=25)
        txt_cod_cadastro.focus()

        self.root_cadProduto.deiconify()
        self.root_cadProduto.mainloop()


# CLASSE REFERENTE A JANELA MAIN (PRINCIPAL)
class principalwindow:
    def logout(self):
        mensagem = tkMessagebox.askokcancel('LOGOUT', 'Deseja realmente sair do programa?', )
        if mensagem == True:
            self.quit_window()
            # telaLogin()

    def quit_window(self):
        self.main_window.destroy()

    def chamarConsulta(self):
        try:
            self.quit_window()
            consulta_window()
        except:
            raise Exception('Não foi possivel abrir a janela de Consulta')

    def chamarCadastroFuncao(self):
        try:
            self.quit_window()
            cadFuncao_window()
        except:
            raise Exception('Não foi possivel abrir a janela "Cadastro de funcionário"')

    def chamarCadastroFuncionario(self):
        try:
            self.quit_window()
            cadFuncionario_window()
        except:
            raise EXCEPTION('Não foi possivel abrir a janela "Cadastro de Funcionários"')

    def chamarCadastroClientes(self):
        try:
            self.quit_window()
            cadCliente_window()
        except:
            raise Exception('Não foi possivel abrir a janela "Cadastro de cliente"')

    def chamarCadastroProduto(self):
        try:
            self.quit_window()
            cadProduto_window()
        except:
            raise Exception('Não foi possivel abrir a janela "Cadastro de produtos"')

    def confirmacaofecharJanela(self):
        if tkMessagebox.askokcancel("AVISO!", "Deseja sair do programa?"):
            self.quit_window()

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("NetSystemCorp - Bem Vindo!")
        self.main_window['bg'] = "grey21"
        self.main_window.resizable(False, False)
        self.main_window.protocol('WM_DELETE_WINDOW', self.confirmacaofecharJanela)
        self.main_window.iconbitmap('img\logo01.ico')
        self.main_window.resizable(0, 0)

        # CENTRALIZA TELA
        self.main_window.withdraw()
        self.main_window.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.main_window.winfo_screenwidth() - self.main_window.winfo_reqwidth()) / 2
        y = (self.main_window.winfo_screenheight() - self.main_window.winfo_reqheight()) / 4
        self.main_window.geometry("+%d+%d" % (x, y))

        # CRIANDO MENU HORIZONTAL TOPO

        menuTopo = Menu(self.main_window)
        menuTopo.add_command(label='File')

        fileMenu = Menu(menuTopo)
        fileMenu.add_command(label='Sair', command=lambda: self.quit_window())
        menuTopo.add_command(label='Sobre')

        self.main_window.config(menu=menuTopo)

        # ----------------------------------------------------

        frameTopo = Frame(self.main_window, bg="grey21")
        self.img = ImageTk.PhotoImage(Image.open("img\letraMedia.png"))

        self.panel = Label(frameTopo, image=self.img, bg='grey21')
        self.panel.grid(row=0, column=0, columnspan=3, sticky=W + E)

        # ----------------------------------------------------
        frameLeft = Frame(self.main_window, relief='groove', bd=4, bg="grey21")

        # LABEL ------------------------------
        label_cadastro = Label(
            self.main_window, text='CADASTRO', bg='grey21', font='Arial 10 bold', fg='#f2f2f2')

        # BOTÃO ------------------------------
        btn_cad_cadastro = Button(frameLeft, text='PRODUTO', width=25,
                                  command=lambda: self.chamarCadastroProduto())
        btn_cad_cliente = Button(frameLeft, text='CLIENTE', width=25,
                                 command=lambda: self.chamarCadastroClientes()
                                 )
        btn_cad_funcionario = Button(frameLeft, text='FUNCIONÁRIO', width=25,
                                     command=lambda: self.chamarCadastroFuncionario()
                                     )
        btn_cad_cargo = Button(frameLeft, text='CARGO', width=25, command=lambda: self.chamarCadastroFuncao()
                               )

        # ----------------------------------------------------
        frameRight = Frame(self.main_window, relief='groove', bd=4, bg="grey21")

        # LABEL ------------------------------
        label_consulta = Label(frameRight, text='CONSULTAR \ ATUALIZAR', bg='grey21', font='Arial 10 bold',
                               fg='#f2f2f2')

        # BOTÃO ------------------------------
        btn_consulta_cadastro = Button(frameRight, text='CONSULTAR \ ATUALIZAR', width=25,
                                       command=lambda: self.chamarConsulta())

        btn_logout = Button(frameRight, text='LOGOUT', width=15, font='Arial 8', bg='grey', fg='white',
                            command=lambda: self.logout())

        # ----------------------------------------------------

        frameRodape = Frame(self.main_window, bg="grey21", )
        label_InfButtom = Label(frameRodape, text='© Copyright 2020-2020 NetSystem.com.br - All Rights Reserved!',
                                bg="grey21", fg='white', font='Arial 8')

        # Layout
        # ----------------------------------------------------

        # FRAMES
        frameTopo.grid(row=0, column=0, columnspan=3, pady=10, sticky=N)
        frameLeft.grid(row=1, column=0, padx=7, pady=0, )

        frameRight.grid(row=1, column=1, padx=7, columnspan=2, rowspan=4, sticky=N)
        frameRodape.grid(row=2, column=0, columnspan=2)

        # LABEL
        label_InfButtom.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=(70, 0))

        label_cadastro.grid(row=1, column=0, sticky=N, pady=20)

        label_consulta.grid(row=1, column=2, sticky=N, pady=20)

        # BOTÃO CADASTRO
        btn_cad_cadastro.grid(row=1, column=1, pady=(50, 10), padx=10, sticky=W + E)
        btn_cad_cliente.grid(row=2, column=1, pady=10, padx=10, sticky=W + E)
        btn_cad_funcionario.grid(row=3, column=1, pady=10, padx=10, sticky=W + E)
        btn_cad_cargo.grid(row=4, column=1, pady=10, padx=10, sticky=W + E)

        # BOTÃO CONSULTAR
        btn_consulta_cadastro.grid(row=1, column=2, pady=(50, 10), padx=10, sticky=W + E)

        # BOTÃO LOGOUT
        btn_logout.grid(row=4, column=2, pady=(107, 5), padx=10, sticky=W + E)

        self.main_window.deiconify()
        self.main_window.mainloop()


# CLASSE REFERENTE A JANELA DE LOGIN/SENHA.
class telaLogin():
    def quit_window(self):
        self.root_password.destroy()

    def validador(self, user, password):
        self.usuario = 'root'
        self.senha = '123'
        usuarioDigitado = user.get()
        senhaDigitada = password.get()
        if usuarioDigitado == self.usuario and senhaDigitada == self.senha:
            try:
                self.quit_window()
                principalwindow()


            except:
                raise Exception()
        elif usuarioDigitado == '' and senhaDigitada == '':
            tkMessagebox.showinfo('ERRO', 'Favor insira usuário e senha.')
        else:
            tkMessagebox.showinfo('ERRO', 'Usuário ou senha errada, tente novamente.')

    def __init__(self):
        # Criação da Janela(GUI)
        self.root_password = Tk()
        self.root_password.title("NetSystemCorp - Login")
        self.root_password['bg'] = "grey21"
        self.root_password.resizable(False, False)
        self.root_password.protocol("WM_DELETE_WINDOW")
        self.root_password.iconbitmap('img\logo01.ico')
        self.img01 = ImageTk.PhotoImage(Image.open("img\logoFull.png"))

        # CENTRALIZA TELA
        self.root_password.withdraw()
        self.root_password.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root_password.winfo_screenwidth() - self.root_password.winfo_reqwidth()) / 2
        y = (self.root_password.winfo_screenheight() - self.root_password.winfo_reqheight()) / 4
        self.root_password.geometry("+%d+%d" % (x, y))

        self.panel = Label(self.root_password, image=self.img01, bg='grey21')
        self.panel.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # ----------------------------------------------------
        # widgets

        label_usuario = Label(self.root_password,
                              text='Usuário: ',
                              bg="grey21",
                              fg='white',
                              height=3,
                              font=('Verdana', '10', 'bold'),

                              )
        label_password = Label(self.root_password, text='Senha: ',
                               bg="grey21",
                               fg='white',
                               font=('Verdana', '10', 'bold')
                               )

        text_usuario = Entry(self.root_password)
        text_password = Entry(self.root_password, show='*')

        btn_entrar = Button(self.root_password,
                            text='Entrar',
                            bg="grey20",
                            fg='white',
                            font=('Verdana', '10', 'bold'),
                            command=lambda: self.validador(text_usuario, text_password)
                            )

        # ----------------------------------------------------
        # Layout

        label_usuario.grid(row=1, column=0, sticky=E)
        text_usuario.grid(row=1, column=1, sticky=W + E, padx=10)
        text_usuario.focus()

        label_password.grid(row=2, column=0, sticky=E)
        text_password.grid(row=2, column=1, sticky=W + E, padx=10)

        btn_entrar.grid(row=3, column=1, columnspan=3, pady=20, padx=38, sticky=E)
        self.root_password.deiconify()
        self.root_password.mainloop()


try:
    telaLogin()
except:
    raise Exception('Não pode ser criado o telaLogin')
