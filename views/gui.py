import tkinter as tk
from tkinter import filedialog
from models.model import DataModel
from controler.download import DownloadController

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Download PDF's")
        self.dir = None
        self.df = None

        # add a button to select a file
        self.select_file_button = tk.Button(
            root,
            text="Arquivo CSV",
            command=self.select_file
        )
        self.select_file_button.pack(pady=20)

        # add a button to select a directory
        self.select_directory_button = tk.Button(
            root,
            text="Diretório de Download",
            command=self.select_directory
        )
        self.select_directory_button.pack(pady=20)

        # add download button
        self.download_button = tk.Button(
            root,
            text="Download PDF's",
            command=self.download_pdfs
        )
        self.download_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Selecionar arquivo",
            filetypes=(("CSV", "*.csv"), ("All files", "*.*"))
        )
        if file_path:
            print(f"Arquivo selecionado: {file_path}")
            self.model = DataModel(file_path)
            self.df = self.model.df
        else:
            print("Nenhum arquivo selecionado")
    
    def select_directory(self):
        directory_path = filedialog.askdirectory(
            title="Selecionar diretório"
        )
        if directory_path:
            self.dir = directory_path
            print(f"Diretório selecionado: {directory_path}")
        else:
            print("Nenhum diretório selecionado")

    def download_pdfs(self):
        if self.dir and self.df is not None:
            downloader = DownloadController(self.df, self.dir)
            downloader.download_files()