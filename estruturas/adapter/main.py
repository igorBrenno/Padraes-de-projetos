class Target:
    def request(self):
        return "Target: The default Target's beheviour."
    
class Adaptee:
    def specific_request(self):
        return "agsagsag"
    
# class Adapter(Target, Adaptee):
#     def request(self):
#         return "Alguma coisa de metodo especifico: "

class Adapter(Target):
    def __init__(self, aux):
        self.adaptee = aux

    def request(self):
        aux = self.adaptee.specific_request()
        return aux
    
class Adapter2(Target, Adaptee):
    def __init__(self):
        pass

    def request(self):
        aux = super().specific_request()
        return aux

def client_code(target: "Target"):
    print(target.request())
    

if __name__ == "__main__":
    print("Primeiro exemplo ---")
    target = Target()
    client_code(target)
    print("-----------")

    print("Segundo exemplo ---")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
    print("-----------")

    print("Terceiro exemplo ---")
    adapter = Adapter2()
    client_code(adapter)
    print("-----------")