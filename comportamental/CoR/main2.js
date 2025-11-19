class Handler {
    constructor() {
        this.proximo = null;
    }

    setProximo(proximo) {
        this.proximo = proximo;
        return proximo;
    }

    handle(requisicao) {
        if (this.proximo) return this.proximo.handle(requisicao);
        
        // Se for o último, retorna a requisição final
        return requisicao
    }
}

class ObjA extends Handler {
    handle(requisicao) {
        // Chama o método 'handle' da classe pai (Handler) para passar adiante
        return super.handle(requisicao + "ObjA, ");
    }
}

class ObjB extends Handler {
    handle(requisicao) {
        return super.handle(requisicao + "ObjB, ");
    }
}

// Montagem da Cadeia
const objetoA = new ObjA();
// Liga os elos em sequência: ObjA -> ObjB -> ObjB -> ObjA
objetoA.setProximo(new ObjB()).setProximo(new ObjB()).setProximo(new ObjA());

console.log(objetoA.handle("Inicial, "))