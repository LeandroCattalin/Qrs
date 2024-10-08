from pathlib import Path
import pyodbc   
import sqlite3
import smtplib
from sqlite3 import Error
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


class Database:
    """
        Clase que se utiliza para obtener información y realizar consultas a la base de datos
    """
    _instance = None
    
    def __init__(self, *args, **kwargs):
        pass
    
    def crear_qr(self):
        pass
    
    # Creación de singleton
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

class DatabaseSqlLite(Database):
    """
    Clase que se utiliza para obtener información y realizar consultas a la base de datos
    """
    _instance = None
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = self.create_connection()

    def create_connection(self):
        """Crea una conexión a la base de datos SQLite"""
        try:
            connection = sqlite3.connect(self.connection_string)
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def crear_qr(self, data):
        """Método placeholder para crear un código QR"""
        pass

    def execute_query(self, query, params=()):
        """Ejecuta una consulta SQL"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def fetch_all(self, query, params=()):
        """Recupera todas las filas de una consulta"""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close_connection(self):
        """Cierra la conexión a la base de datos"""
        if self.connection:
            self.connection.close()

    # Creación de singleton
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

class EmailSender:
    """
    Clase para enviar correos electrónicos
    """
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        
    def send_email(self, destinatario, subjeto, body):
        """
        Envía un correo electrónico.
        :param to_email: destinatario del correo
        :param subject: asunto del correo
        :param body: cuerpo del correo
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = destinatario
            msg['Subject'] = subjeto
            msg.attach(MIMEText(body, 'plain'))
            #! TODO: implementación de configuración de mail_sender
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                raise NotImplementedError
                server.starttls()  # Inicia la conexión TLS
                server.login(self.username, self.password)
                server.send_message(msg)                
            print(f"Correo enviado a {destinatario} con éxito.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")


class PDFGenerator:
    """
    Clase para generar archivos PDF
    """
    
    def __init__(self, output_directory: Path|str):
        self.output_directory = output_directory
        
    def generate_pdf(self, filename, data: dict) -> Path:
        """
        Genera un archivo PDF.
        :param filename: nombre del archivo PDF a crear
        :param data: datos a incluir en el PDF
        """
        pdf_path = os.path.join(self.output_directory, filename)
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        
        # Agregar contenido al PDF
        c.drawString(100, height - 100, f"Nombre: {data['apellidoNombre']}")
        c.drawString(100, height - 120, f"Legajo: {data['legajo']}")
        c.drawString(100, height - 140, f"Charla: {data['charlaN']}")
        c.drawString(100, height - 160, f"Fecha: {data['fecha']}")
        
        c.save()
        print(f"PDF generado: {pdf_path}")
        
        return Path(pdf_path)