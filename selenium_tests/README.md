# Testes Selenium - Restful Booker Platform

Este diretório contém testes automatizados de interface usando Selenium para a aplicação Restful Booker Platform.

## Pré-requisitos
- Python 3.11 ou superior instalado.
- Bibliotecas necessárias: `selenium` (instale com `pip install selenium`).
- ChromeDriver compatível com a versão do Chrome instalada (deve estar no PATH ou especificar o caminho no script).
- Aplicação rodando em `http://localhost:3003`.

## Cenários de Teste
1. **Login Bem-Sucedido (`test_login_success`)**: Faz login com credenciais corretas (`admin`, `password`) e verifica o redirecionamento para `/admin/rooms`, confirmando a presença do quarto 101 na lista.
2. **Login com Senha Incorreta (`test_login_wrong_password`)**: Tenta login com senha errada (`admin`, `wrongpassword`) e valida a mensagem de erro "Invalid credentials".
3. **Verificação da Página de Quartos (`test_login_verify_rooms_page`)**: Faz login e verifica a presença do quarto 101 na lista de quartos.
4. **Login com Campos Vazios (`test_login_empty_credentials`)**: Tenta login sem preencher os campos e valida a mensagem de erro "Invalid credentials".

## Como Executar os Testes
1. Certifique-se de que a aplicação está rodando (`http://localhost:3003`).
2. Navegue até o diretório `selenium_tests` no terminal.
3. Execute os testes com o comando:
   ```bash
   python test_login.py