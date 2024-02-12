import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

def validar_renda(renda):
    limite_minimo = 1000
    return renda >= limite_minimo

def calcular_prestacoes(valor_emprestimo, taxa_juros_mensal, prazo):
    try:
        
        #Nova forma de cálculo de prestação, usando a fórmula em https://en.wikipedia.org/wiki/Equated_monthly_installment
        #A nova fórmula de cálculo da prestação funciona igual a calculadora do banco central: https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormFinanciamentoPrestacoesFixas.do?method=exibirFormFinanciamentoPrestacoesFixas
        taxa_juros_mensal_decimal = taxa_juros_mensal/100
        prestacao = ((valor_emprestimo * taxa_juros_mensal_decimal) * ((1 + taxa_juros_mensal_decimal) ** (prazo)))/(((1 + taxa_juros_mensal_decimal)**(prazo))-1)
        return prestacao
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero")

def calculate_loan():
    renda = float(renda_entry.get())
    if validar_renda(renda):
        valor_emprestimo = float(valor_emprestimo_entry.get())
        if valor_emprestimo > renda * 10:
            messagebox.showerror("Erro", "O valor do empréstimo excede 10x a renda!")
        else:
            prazo = int(prazo_entry.get())
            if prazo < 0:
                messagebox.showerror("Erro", "O prazo informado é menor do que zero")
            else:
                taxa_juros_mensal = float(taxa_juros_mensal_entry.get())
                taxa_juros_anual = ((1 + taxa_juros_mensal / 100) ** (12) - 1) * 100
                prestacao = calcular_prestacoes(valor_emprestimo, taxa_juros_mensal, prazo)
                custo_total = (prestacao * prazo)

                results_text.config(state=tk.NORMAL)
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END,
                    f'Renda mensal informada: R$ {renda:.2f}\n'
                    f'Valor tomado como empréstimo: R$ {valor_emprestimo:.2f}\n'
                    f"Taxa de Juros anual: {taxa_juros_anual:.2f}% ao ano\n"
                    f"Taxa de Juros mensal: {taxa_juros_mensal:.2f}% ao mês\n"
                    f"Prazo em meses: {prazo} meses\n"
                    f"Valor das Prestações Mensais: R$ {prestacao:.2f}\n"
                    f"Custo Total do Empréstimo: R$ {custo_total:.2f}"
                )
    else:
        messagebox.showerror("Erro", "Desculpe, sua renda não atende aos requisitos mínimos para o empréstimo.")


def copy_to_clipboard():
    text = results_text.get(1.0, tk.END)
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

# Create the main window
window = tk.Tk()
window.title("Calculadora de Prestação de Empréstimo")
window['background']='#19bfcf'

# Create and configure the input fields
style = ttk.Style()
style.configure("TLabel", foreground="#1757cf", background="#19bfcf", font=("Arial", 12))
style.configure("TButton", foreground="#1757cf", background="#19bfcf", font=("Arial", 12))
style.configure("TFrame", background="#19bfcf")

frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)

ttk.Label(frame, text="Renda Mensal:").grid(row=0, column=0, padx=10, pady=5)
renda_entry = ttk.Entry(frame)
renda_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Valor do Empréstimo:").grid(row=1, column=0, padx=10, pady=5)
valor_emprestimo_entry = ttk.Entry(frame)
valor_emprestimo_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Prazo (em meses):").grid(row=2, column=0, padx=10, pady=5)
prazo_entry = ttk.Entry(frame)
prazo_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame, text="Taxa de Juros mensal (%):").grid(row=3, column=0, padx=10, pady=5)
taxa_juros_mensal_entry = ttk.Entry(frame)
taxa_juros_mensal_entry.grid(row=3, column=1, padx=10, pady=5)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_loan)
calculate_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Create a label for displaying the results
results_text = tk.Text(window, wrap=tk.WORD, height=10, width=40)
results_text.pack(pady=10)
results_text.config(state=tk.DISABLED)

# Create a context menu for the Text widget
context_menu = Menu(results_text, tearoff=0)
context_menu.add_command(label="Copy", command=copy_to_clipboard)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

results_text.bind("<Button-3>", show_context_menu)  # Right-click event

window.mainloop()