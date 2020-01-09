import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from EA_transport_1 import simulate_EA, load_route_graph_from_file, load_dest_mat_from_file, create_to_file_graph, create_new_dest_mat_file
import networkx as nx
from copy import deepcopy
from typing import List
matplotlib.use("TkAgg")

'''def do_sth(name):
    print('mumu', name)

#initialize

root = tk.Tk()

root.title('MMWD lzami Pucia oblane')

button = tk.Button(root, text='do sth', command=lambda: do_sth('kurwa'))
button.pack()

#Start program
root.mainloop()'''

LARGE_FONT = ("Verdana", 12)

nobjfun = 100
mut = 0.6
pop_size = 100
par_size = 2
sel_coef = 1.5
graph_size = 10
ticket = 5
fuel = 2
line = 10


class ParameterContainer():
    def __init__(self):
        self.nobjfun = 100
        self.mut = 0.6
        self.pop_size = 100
        self.par_size = 2
        self.sel_coef = 1.5
        self.graph_size = 10
        self.ticket = 5
        self.fuel = 2
        self.line = 10


class Ea_tranapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        global graph_size
        create_new_dest_mat_file(graph_size)
        create_to_file_graph(graph_size)
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'EA mass transport PPP')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (StartPage, DefaultPage, ParameterPage):
            frame_temp = frame(container, self)
            self.frames[frame] = frame_temp
            frame_temp.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame =self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Witamy w programie realizującym projekt MMWD', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        text = tk.Text(self)
        text.config(state='normal')
        text.tag_configure("center", justify='center')
        with open('start_page_text_gui.txt', 'r') as f:
            text.insert(tk.END, f.read())
        text.tag_add("center", "1.0", "end")
        text.config(state='disabled')

        text.pack()
        btn_next = tk.Button(self, text='Go next',
                             command=lambda: controller.show_frame(DefaultPage))
        btn_next.pack()





class DefaultPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(fig, self)


        self.label = tk.Label(self, text='Simulation page', font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.btn_run_sim = tk.Button(self, text='Start simulation',
                                command=lambda: self.run_sim(self))
        self.btn_run_sim.pack()
        self.btn_next = tk.Button(self, text='Change parameters',
                             command=lambda: controller.show_frame(ParameterPage))
        self.btn_next.pack()
        self.lbl_income = tk.Label(self, text='Generated income: {}'.format(0))
        self.lbl_income.pack()
        self.lbl_routes = tk.Label(self, text='Generated best routes:')
        self.lbl_routes.pack()

        route = load_route_graph_from_file()
        pos = nx.circular_layout(route)
        '''
        f = Figure(figsize=(5, 5), dpi=100)
        ax=f.subplots(2)
        nx.draw_networkx_nodes(route, pos, node_size=600, ax=ax[0])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        '''

    def refresh_graph(self):
        #self.fig.clear()
        #self.canvas.draw()
        #self.canvas.
        self.canvas.get_tk_widget().delete('all')
        self.canvas.get_tk_widget().pack_forget()




    def visualize_graph(self, route: nx.Graph, best_sol: List):
        pos = nx.circular_layout(route)
        self.refresh_graph()

        bus_lines_edges = []
        for bus in best_sol[0]:
            bus_line_edges = []
            for b_stop in range(len(bus) - 1):
                bus_line_edges.append((bus[b_stop], bus[b_stop + 1]))
            bus_lines_edges.append(deepcopy(bus_line_edges))
        directed_graph_lines = []
        for line in bus_lines_edges:
            directed_graph_lines.append(nx.DiGraph())
            directed_graph_lines[-1].add_edges_from(line)

        if len(directed_graph_lines) > 1:
            fig = Figure(figsize=(5, 5), dpi=100)
            ax = fig.subplots(len(directed_graph_lines))


            for idx, line_graph in enumerate(directed_graph_lines):
                nx.draw_networkx_nodes(route, pos, node_size=600, ax=ax[idx])
                nx.draw_networkx_edges(
                    route,
                    pos,
                    ax=ax[idx],
                    width=1
                )
                nx.draw_networkx_labels(route, pos, font_size=10, ax=ax[idx])
                nx.draw_networkx_edges(
                    line_graph,
                    pos,
                    edge_color='r',
                    arrowsize=15,
                    width=2,
                    ax=ax[idx]

                )
                ax[idx].set_title('Linia numer {}'.format(idx + 1), fontsize=10)

        else:
            fig = Figure(figsize=(5, 5), dpi=100)
            ax = fig.subplots(2)
            nx.draw_networkx_nodes(route, pos, node_size=600, ax=ax[0])
            nx.draw_networkx_edges(
                route,
                pos,
                width=1,
                ax=ax[0]
            )
            nx.draw_networkx_labels(route, pos, font_size=10, ax=ax[0])
            nx.draw_networkx_edges(
                directed_graph_lines[0],
                pos,
                edge_color='r',
                arrowsize=15,
                width=2,
                ax = ax[0]

            )
            #plt.title('Linia numer {}'.format(1), fontsize=10)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    @staticmethod
    def run_sim(self):
        global nobjfun
        global mut
        global pop_size
        global par_size
        global sel_coef
        global graph_size
        global ticket
        global fuel
        global line
        route_graph = load_route_graph_from_file()
        mat = load_dest_mat_from_file()

        best_sol = simulate_EA(route_graph, pop_size, mat, mut, nobjfun, sel_coef, par_size, ticket, fuel, line)
        print(best_sol)
        self.lbl_income.config(text='Generated income: {}'.format(best_sol[1]))
        routes_str =''
        for route in best_sol[0]:
            routes_str += '\n'
            routes_str += str(route)
        self.lbl_routes.config(text='Generated best routes:'+routes_str)
        self.visualize_graph(route_graph, best_sol)


class ParameterPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)



        sim_lbl = tk.Label(self, text='Simulation parameters', font=LARGE_FONT)
        sim_lbl.grid(row=1, column=0, sticky='w')


        #liczba wywolan
        nobjfun_lbl = tk.Label(self, text='Num of objective function iteration')
        nobjfun_lbl.grid(row=2, column=0, sticky='w')
        self.nobjfun_ent = tk.Entry(self)
        self.nobjfun_ent.grid(row=2, column=1, sticky='n')

        #prawdop mutacji
        mut_lbl = tk.Label(self, text='Mutation probability')
        mut_lbl.grid(row=3, column=0, sticky='w')
        self.mut_ent = tk.Entry(self)
        self.mut_ent.grid(row=3, column=1, sticky='n')

        pop_lbl = tk.Label(self, text='Population parameters', font=LARGE_FONT)
        pop_lbl.grid(row=1, column=3, sticky='w')
        #wielkosc populacji
        pop_size_lbl = tk.Label(self, text='Population size')
        pop_size_lbl.grid(row=2, column=3, sticky='w')
        self.pop_size_ent = tk.Entry(self)
        self.pop_size_ent.grid(row=2, column=4, sticky='n')
        #wpolczynnik rodzicow
        par_size_lbl = tk.Label(self, text='Parent size coef')
        par_size_lbl.grid(row=3, column=3, sticky='w')
        self.par_size_ent = tk.Entry(self)
        self.par_size_ent.grid(row=3, column=4, sticky='n')
        #wspolczynnik liniowy selekcji
        sel_coef_lbl = tk.Label(self, text='Linear selection coef')
        sel_coef_lbl.grid(row=4, column=3, sticky='w')
        self.sel_coef_ent = tk.Entry(self)
        self.sel_coef_ent.grid(row=4, column=4, sticky='n')

        #Nowy graf
        route_lbl = tk.Label(self, text='Route parameters', font=LARGE_FONT)
        route_lbl.grid(row=47, sticky='w')

        graph_size_lbl = tk.Label(self, text='Graph size')
        graph_size_lbl.grid(row=48, column=0, sticky='w')
        self.graph_size_ent = tk.Entry(self)
        self.graph_size_ent.grid(row=48, column=1, sticky='n')

        btn_new_graph = tk.Button(self, text='New route graph', command=lambda: self.new_graph())
        btn_new_graph.grid(row=49)

        btn_new_mat = tk.Button(self, text='New Matrix of passenger', command=lambda: self.new_matrix())
        btn_new_mat.grid(row=50)

        #Parametry kosztow
        cost_lbl = tk.Label(self, text='Cost parameters')
        cost_lbl.grid(row=47, column=3, sticky='w')


        #Cena biletu
        ticket_lbl = tk.Label(self, text='Ticket cost')
        ticket_lbl.grid(row=48, column=3, sticky='w')
        self.ticket_ent = tk.Entry(self)
        self.ticket_ent.grid(row=48, column=4, sticky='n')

        # Cena paliwa
        fuel_lbl = tk.Label(self, text='Fuel cost')
        fuel_lbl.grid(row=49, column=3, sticky='w')
        self.fuel_ent = tk.Entry(self)
        self.fuel_ent.grid(row=49, column=4, sticky='n')

        # Cena linii
        line_lbl = tk.Label(self, text='New line cost')
        line_lbl.grid(row=50, column=3, sticky='w')
        self.line_ent = tk.Entry(self)
        self.line_ent.grid(row=50, column=4, sticky='n')

        btn_save = tk.Button(self, text='Save changes', command=lambda: self.on_save_btn())
        btn_save.grid(row=199, column=2)

        btn_prev = tk.Button(self, text='Go prev',
                             command=lambda: controller.show_frame(DefaultPage))
        btn_prev.grid(row=200, column=2)

        global nobjfun
        global mut
        global pop_size
        global par_size
        global sel_coef
        global graph_size
        global ticket
        global fuel
        global line

        self.nobjfun_ent.insert(0,str(nobjfun))
        self.mut_ent.insert(0, str(mut))
        self.pop_size_ent.insert(0, str(pop_size))
        self.par_size_ent.insert(0, str(par_size))
        self.sel_coef_ent.insert(0, str(sel_coef))
        self.graph_size_ent.insert(0, str(graph_size))
        self.ticket_ent.insert(0, str(ticket))
        self.fuel_ent.insert(0, str(fuel))
        self.line_ent.insert(0, str(line))




    def new_matrix(self):
        global graph_size
        create_new_dest_mat_file(graph_size)

    def new_graph(self):
        global graph_size
        create_to_file_graph(graph_size)

    def on_save_btn(self):
        global nobjfun
        global mut
        global pop_size
        global par_size
        global sel_coef
        global graph_size
        global ticket
        global fuel
        global line
        nobjfun = int(self.nobjfun_ent.get())
        mut = float(self.mut_ent.get())
        pop_size = int(self.pop_size_ent.get())
        par_size = int(self.par_size_ent.get())
        sel_coef = float(self.sel_coef_ent.get())
        graph_size = int(self.graph_size_ent.get())
        ticket = float(self.ticket_ent.get())
        fuel = float(self.fuel_ent.get())
        line = float(self.line_ent.get())

    def print_entry(self):
        global nobjfun
        print(self.nobjfun_ent.get())
        print(nobjfun)







app = Ea_tranapp()
app.mainloop()