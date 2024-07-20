#código que calcula depreciação do bem

class informacao_bens(): 
    def info(self):
        while True:
            print("\n\t1.informações sobre os bens depreciáveis e não depreciáveis.\n\t2.Informações sobre valor residual e vida útil\n\t3.Prosseguir com a aplicação.")
            q_1=int(input("\nEscolha uma opção:"))
            if q_1 == 1:
                print("-"*30)
                print("\nOs bens depreciavéis são:\n\tEquipamentos e maquinários;\n\tVeículos;\n\tImóveis comerciais e industriais;\n\tSoftwares e sistemas de tecnologia.")
                print("\nOs bens não depreciáveis são aqueles que não perdem valor ao longo do tempo, ou possuem uma vida útil indefinida, tais como:\n\tTerrenos;\n\tObras de arte e antiguidades;\n\tInvestimentos financeiros de longo prazo, tais como ações e títulos.")
                print("-"*30)            
            elif q_1 == 2:
                print("-"*30) 
                print("\nO valor residual é o valor que se espera que ele valha ao final de sua vida útil. Alguns ativos, por exemplo, têm um valor residual mínimo, enquanto outros não têm valor residual.")
                print("\nA vida útil é uma variável que a organização/empresa avalia sobre quanto tempo um determinado ativo pode durar. ")
                print("-"*30) 
            else:
                print("Entendido! Então, vamos prosseguir com a aplicação. ")
                break
    
    def met_calc(self):
        while True:
            print("-"*30)
            print("\n\t1.Depreciação Linear\n\t2.-Em construção-\n\t3.Sair")
            calc_type=int(input("\nEscolha uma opção: "))
            if calc_type == 1:
                a_nome=input("Nome do ativo: ")
                a_value=float(input("\nInsira o valor do ativo: "))
                r_value=float(input("\nAgora, me informe o valor residual: "))
                u_value=float(input("\nPor fim, me informe a vida útil do ativo (em anos): "))
                d_calc=((a_value-r_value)/u_value)
                print("-"*30)
                print(f"Nome do ativo: {a_nome}\nDepreciação anual do ativo: {d_calc:2f}")
                print("-"*30)
            elif calc_type == 2:
                print("Mais opções estão sendo implementadas, por gentileza aguarde novas atualizações! ")
                break 
            elif calc_type == 3: 
                print("Saindo...")
                break
            else:
                print("Opção inválida, por favor digite novamente!")

info_bens = informacao_bens()
info_bens.info()
info_bens.met_calc()