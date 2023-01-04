print("Tabla de multiplicar\n")

for i in range(10):
    if i >= 1:
        print(f"{i}X")
        
        for a in range(9):
            print(f"{i}x{a+1}={i*(a+1)}")    
        print("")