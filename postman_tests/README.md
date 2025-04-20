# Testes Postman - Restful Booker Platform

Este diretório contém testes automatizados de API usando o Postman para a aplicação Restful Booker Platform.

## Pré-requisitos
- Postman instalado (versão mais recente recomendada).
- Aplicação rodando em `http://localhost:3003` (ou `http://localhost:3000` para o endpoint de reservas, conforme usado na coleção).

## Coleção de Testes
A coleção de testes está no arquivo `Testes API Restful Booker.postman_collection.json`. Ela inclui os seguintes cenários:

### Cenários de Teste
1. **Listar Todos os Quartos**:
   - Endpoint: `GET http://localhost:3003/api/room`
   - Validação:
     - Status 200 OK.
     - Corpo da resposta contém uma lista de quartos (`rooms`) não vazia.
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Verifica a presença de uma lista de quartos (`pm.expect(jsonData.rooms).to.be.an("array")`).

2. **Criar Quarto - Positivo**:
   - Endpoint: `POST http://localhost:3003/api/room`
   - Corpo: Quarto 104 (Double, preço 150, sem acessibilidade, com TV, WiFi, Mini Fridge).
   - Validação:
     - Status 200 OK.
     - Resposta confirma a criação bem-sucedida (`success: true`).
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Verifica o sucesso da criação (`pm.expect(jsonData.success).to.be.true`).

3. **Criar Quarto - Negativo (Dados Inválidos)**:
   - Endpoint: `POST http://localhost:3003/api/room`
   - Corpo: Quarto 104 com tipo inválido (`"InvalidType"`).
   - Validação:
     - Status 400 Bad Request.
     - Resposta contém uma lista de erros de validação.
   - Testes:
     - Verifica o status (`pm.response.to.have.status(400)`).
     - Verifica a presença de erros (`pm.expect(jsonData.errors).to.be.an("array")`).

4. **Deletar Quarto 102**:
   - Endpoint: `DELETE http://localhost:3003/api/room/2`
   - Validação:
     - Status 200 OK.
     - Resposta confirma a exclusão (ou é vazia).
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Verifica a resposta (confirmação ou corpo vazio).

5. **Atualizar Quarto 103**:
   - Endpoint: `PUT http://localhost:3003/api/room/3`
   - Corpo: Atualiza o quarto 103 (Double, preço 200, com TV, WiFi, Mini Fridge, Air Conditioning).
   - Validação:
     - Status 200 OK.
     - Resposta confirma a atualização (ou é vazia).
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Verifica a resposta (confirmação ou corpo vazio).

6. **Atualizar Quarto 103 - Negativo (Sem Autenticação)**:
   - Endpoint: `PUT http://localhost:3003/api/room/3`
   - Corpo: Mesmo corpo do teste anterior, mas sem autenticação.
   - Validação:
     - Status 401 Unauthorized.
     - Resposta contém mensagem de erro "Authentication required".
   - Testes:
     - Verifica o status (`pm.response.to.have.status(401)`).
     - Verifica a mensagem de erro (`pm.expect(jsonData.errors[0]).to.include("Authentication required")`).

7. **Buscar Quarto 103**:
   - Endpoint: `GET http://localhost:3003/api/room/3`
   - Validação:
     - Status 200 OK.
     - Resposta contém os dados corretos do quarto 103 (Double, preço 200, etc.).
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Valida os campos do quarto (`pm.expect(jsonData.roomName).to.equal("103")`, etc.).

8. **Criar Reserva - Quarto 103**:
   - Endpoint: `POST http://localhost:3000/booking/`
   - Corpo: Reserva para o quarto 103 (Lucas Alcantara, check-in 2025-07-01, check-out 2025-07-05).
   - Validação:
     - Status 200 OK.
     - Resposta contém os dados da reserva criada.
   - Testes:
     - Verifica o status (`pm.response.to.have.status(200)`).
     - Valida os dados da reserva (`pm.expect(jsonData.bookings[0].roomid).to.equal(3)`).

## Autenticação
- A autenticação é gerenciada por meio de cookies. Para requisições que requerem autenticação (ex.: `PUT` e `DELETE`), um cookie de sessão é usado, obtido após um login bem-sucedido.
- **Nota**: A coleção não inclui uma requisição explícita para login (`POST /auth`), mas assume que o cookie de autenticação já foi obtido. Para configurar:
  1. Faça uma requisição manual `POST http://localhost:3003/auth` com o corpo `username=admin&password=password`.
  2. Copie o cookie de sessão retornado (ex.: `session` ou similar) da resposta.
  3. No Postman, adicione o cookie manualmente na coleção (aba "Cookies" ou via script com `pm.cookies.set()`), ou garanta que o Postman gerencie automaticamente os cookies da sessão.
- O teste "Atualizar Quarto 103 - Negativo" desativa a autenticação para validar o comportamento de erro (falta de cookie).

## Como Executar os Testes
1. Certifique-se de que a aplicação está rodando (`http://localhost:3003` e `http://localhost:3000`).
2. Configure a autenticação:
   - Faça uma requisição `POST http://localhost:3003/auth` com `username=admin` e `password=password` para obter o cookie de sessão.
   - Certifique-se de que o Postman está gerenciando os cookies automaticamente (ou adicione o cookie manualmente na coleção).
3. Abra o Postman.
4. Importe a coleção `Testes API Restful Booker.postman_collection.json` (File > Import > selecione o arquivo).
5. Execute a coleção:
   - Clique na coleção no Postman.
   - Clique em "Run Collection".
   - Configure para rodar em sequência e clique em "Run Testes API Restful Booker".
6. Verifique os resultados na aba "Test Results" do Postman.

## Resultados Esperados
- Todos os testes devem passar, indicando que os endpoints de gerenciamento de quartos e reservas estão funcionando corretamente.
- Em caso de falha, verifique:
  - O estado da aplicação (ex.: se os quartos 102 e 103 existem).
  - Os logs de erro no Postman (aba Console).
  - A presença do cookie de autenticação para requisições que o exigem (ex.: `PUT` e `DELETE`).

## Notas
- O endpoint de reservas usa uma porta diferente (`http://localhost:3000`), enquanto os outros usam `http://localhost:3003`. Certifique-se de que ambos os serviços estão ativos.
- A variável `baseUrl` na coleção está definida como `https://www.automationintesting.online`, mas os testes usam URLs fixas (`http://localhost:3003`). Atualize a variável ou os testes, se necessário.