# create class
class Diary:
    
    def __init__(self):
        self.contactos = []

    # program menu
    def menu(self):
        print()
        menu=[
            ['Agenda Personal'],
            ['1. Añadir Contacto', "añadir"],
            ['2. Listar contacto'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]

        for x in range(6):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion==1:
            self.añadir()
        elif opcion==2:
            self.listar()
        elif opcion==3:
            self.buscar()
        elif opcion==4:
            self.editar()
        elif opcion==5:
            print("Saliendo de la agenda ...")
            exit()
        
        # Volvamos a llamar al menú
        self.menu()

    def añadir(self):
      print("---------------------")
      print("Añadir nuevo contacto")
      print("---------------------")
      nom = input("Introduzca el nombre: ")
      telf = int(input("Introduzca el teléfono: ")) 
      email = input("Introduzca el email: ")
      self.contactos.append({'nombre': nom, 'telf':telf, 'email': email})

    def listar(self):
      print("---------------------")
      print("Añadir nuevo contacto")
      print("---------------------")
      if len(self.contactos)==0:
          print("No hay ningún contacto en la lista")
      else:
          for x in range(len(self.contactos)):
              print(self.contactos[x]['nombre'])
    
    def buscar(self):
      print("---------------------")
      print("Buscar por nombre")
      print("---------------------")
      nom=input("Introduzca el nombre del contacto: ")
      for x in range(len(self.contactos)):
          if nom==self.contactos[x]["nombre"]:
              print("Datos del contacto")
              print("Nombre: ", self.contactos[x]["nombre"])
              print("Teléfono: ", self.contactos[x]["telf"])
              print("Email: ", self.contactos[x]["email"])
              return x
    def editar():
        pass
    
    

          

       
diary = Diary()
diary.menu()
    
        

