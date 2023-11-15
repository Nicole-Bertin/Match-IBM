import tkinter as tk
from tkinter import messagebox

def calcular_tempo_necessario():
    try:
        meta_financeira = float(entry_meta.get().replace(",", "."))
        economia_mensal = float(entry_economia.get().replace(",", "."))

        if meta_financeira <= 0 or economia_mensal <= 0:
            messagebox.showerror("Erro", "Por favor, insira valores válidos maiores que zero.")
            return

        tempo_necessario = meta_financeira / economia_mensal
        resultado_label.config(text=f"Tempo necessário: {tempo_necessario:.2f} meses", fg="#4CAF50")

        historico_text.config(state=tk.NORMAL)
        historico_text.insert(tk.END, f"Meta: R${meta_financeira:.2f}\nTempo necessário: {tempo_necessario:.2f} meses\n\n")
        historico_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

def limpar_campos():
    entry_meta.delete(0, tk.END)
    entry_economia.delete(0, tk.END)
    resultado_label.config(text="", fg="black")

root = tk.Tk()
root.title("Calculadora Financeira")

window_width = 350
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

label_info = tk.Label(root, text="Use o ponto (.) para separar os decimais (ex: 1000.50)", bg="#f4f4f4", fg="#666666", font=("Arial", 10, "italic"))
label_info.pack(pady=10)

label_meta = tk.Label(root, text="Meta Financeira (R$):", bg="#f4f4f4", fg="#333333", font=("Arial", 12))
label_meta.pack(pady=5)

entry_meta = tk.Entry(root, font=("Arial", 11), bg="#ffffff", fg="#333333", relief=tk.FLAT, borderwidth=2)
entry_meta.pack(padx=10, pady=5, fill=tk.X)

label_economia = tk.Label(root, text="Economia Mensal (R$):", bg="#f4f4f4", fg="#333333", font=("Arial", 12))
label_economia.pack(pady=5)

entry_economia = tk.Entry(root, font=("Arial", 11), bg="#ffffff", fg="#333333", relief=tk.FLAT, borderwidth=2)
entry_economia.pack(padx=10, pady=5, fill=tk.X)

calcular_button = tk.Button(root, text="Calcular", command=calcular_tempo_necessario, bg="#4CAF50", fg="#ffffff", font=("Arial", 12, "bold"), relief=tk.FLAT)
calcular_button.pack(padx=10, pady=10, fill=tk.X)

limpar_button = tk.Button(root, text="Limpar", command=limpar_campos, bg="#FF5722", fg="#ffffff", font=("Arial", 12, "bold"), relief=tk.FLAT)
limpar_button.pack(padx=10, pady=5, fill=tk.X)

resultado_label = tk.Label(root, text="", bg="#f4f4f4", fg="black", font=("Arial", 12))
resultado_label.pack(padx=10, pady=5)

historico_label = tk.Label(root, text="Histórico:", bg="#f4f4f4", fg="#333333", font=("Arial", 12))
historico_label.pack(padx=10, pady=5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

historico_text = tk.Text(root, height=12, width=35, font=("Arial", 11), bg="#ffffff", fg="#333333", relief=tk.FLAT, borderwidth=2, yscrollcommand=scrollbar.set)
historico_text.config(state=tk.DISABLED)
historico_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

scrollbar.config(command=historico_text.yview)

root.mainloop()
