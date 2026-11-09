# E2 — Diagramas UML

## 1. Diagrama de Casos de Uso (atores e funcionalidades)
```mermaid
flowchart LR
    C([Cliente])
    G([Gerente])
    A([Administrador])

    subgraph MiniBank
        UC1((Autenticar))
        UC2((Consultar saldo))
        UC3((Consultar extrato))
        UC4((Depositar))
        UC5((Sacar))
        UC6((Transferir))
        UC7((Cadastrar cliente))
        UC8((Abrir conta))
        UC9((Bloquear/encerrar conta))
        UC10((Consultar auditoria))
        UC11((Gerenciar usuários))
    end

    C --- UC1 & UC2 & UC3 & UC4 & UC5 & UC6
    G --- UC1 & UC7 & UC8 & UC9
    A --- UC1 & UC10 & UC11
```

## 2. Diagrama de Classes (domínio)
```mermaid
classDiagram
    class Cliente {
        +int id
        +String nome
        +String cpf
        +String email
        +Date dataNascimento
    }
    class Usuario {
        +int id
        +String login
        +String senhaHash
        +Perfil perfil
        +autenticar(senha) bool
    }
    class Conta {
        +int id
        +String numero
        +String agencia
        +Decimal saldo
        +StatusConta status
        +depositar(valor)
        +sacar(valor)
        +bloquear()
        +encerrar()
    }
    class ContaCorrente {
        +Decimal limiteChequeEspecial
    }
    class ContaPoupanca {
        +Decimal taxaRendimento
    }
    class Transacao {
        +int id
        +TipoTransacao tipo
        +Decimal valor
        +DateTime dataHora
        +Decimal saldoApos
    }
    class Auditoria {
        +int id
        +String acao
        +DateTime dataHora
    }

    Cliente "1" --> "1..*" Conta : possui
    Cliente "1" --> "0..1" Usuario : acessa com
    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Conta "1" --> "0..*" Transacao : registra
    Usuario "1" --> "0..*" Auditoria : gera
```

## 3. Diagrama de Sequência — Transferência entre contas (RF06)
```mermaid
sequenceDiagram
    actor Cliente
    participant UI as Interface Web
    participant API as API REST
    participant Auth as Autenticação
    participant Svc as Serviço de Transferência
    participant DB as Banco de Dados

    Cliente->>UI: Informa conta destino e valor
    UI->>API: POST /transferencias (token)
    API->>Auth: validar token e perfil
    Auth-->>API: autorizado
    API->>Svc: transferir(origem, destino, valor)
    Svc->>DB: iniciar transação
    Svc->>DB: buscar contas origem/destino
    DB-->>Svc: contas
    alt contas ativas e saldo suficiente
        Svc->>DB: debitar origem, creditar destino, gravar transações e auditoria
        Svc->>DB: confirmar (commit)
        Svc-->>API: sucesso
        API-->>UI: 201 Created + comprovante
        UI-->>Cliente: exibe comprovante
    else inválida
        Svc->>DB: desfazer (rollback)
        Svc-->>API: erro (saldo insuficiente / conta bloqueada)
        API-->>UI: 422 + mensagem
        UI-->>Cliente: exibe erro
    end
```

## 4. Diagrama de Atividades — Saque
```mermaid
flowchart TD
    A([Início]) --> B[Cliente informa valor]
    B --> C{Valor > 0?}
    C -- Não --> X[Rejeitar: valor inválido]
    C -- Sim --> D{Conta ativa?}
    D -- Não --> Y[Rejeitar: conta bloqueada]
    D -- Sim --> E{Saldo suficiente?}
    E -- Não --> Z[Rejeitar: saldo insuficiente]
    E -- Sim --> F[Debitar saldo]
    F --> G[Registrar transação e auditoria]
    G --> H[Exibir comprovante]
    H --> I([Fim])
    X --> I
    Y --> I
    Z --> I
```
