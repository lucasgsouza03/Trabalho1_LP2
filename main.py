from disciplina import disciplina
from professor import professor

D = disciplina()
lista_disp = []
lista_disp_P1 = []
lista_carga_P1=[]
lista_dispP2 = []
lista_carga_P2=[]
prof = professor()
prof.set_apelido("GUGU")
prof.get_apelido()
D.altera_nome("LP")
D.altera_carga(80)
lista_disp.append(D.get_nome())
lista_disp.append(D.get_carga())
prof.adiciona_disciplina(lista_disp_P1,lista_carga_P1,D.get_nome(),D.get_carga())


D.altera_nome("SQL")
D.altera_carga(80)
lista_disp.append(D.get_nome())
lista_disp.append(D.get_carga())
prof.adiciona_disciplina(lista_disp_P1,lista_carga_P1,D.get_nome(),D.get_carga())


prof.set_apelido("Yuri")
prof.get_apelido()
D.altera_nome("DevOPs")
D.altera_carga(80)
lista_disp.append(D.get_nome())
lista_disp.append(D.get_carga())
prof.adiciona_disciplina(lista_dispP2,lista_carga_P2,D.get_nome(),D.get_carga())

D.altera_nome("TecWeb")
D.altera_carga(80)
lista_disp.append(D.get_nome())
lista_disp.append(D.get_carga())
prof.adiciona_disciplina(lista_dispP2,lista_carga_P2,D.get_nome(),D.get_carga())

D.altera_nome("Engenharia")
D.altera_carga(80)
lista_disp.append(D.get_nome())
lista_disp.append(D.get_carga())
prof.adiciona_disciplina(lista_dispP2,lista_carga_P2,D.get_nome(),D.get_carga())

print(lista_disp)

print(lista_disp_P1,lista_carga_P1)

print(lista_dispP2,lista_carga_P2)

print(prof.total_carga_horaria(lista_carga_P1))

print(prof.total_carga_horaria(lista_carga_P2))