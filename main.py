from usuario import Usuario

cuenta1 = Usuario("maria","maria_villegas@dojo.com")
cuenta2 = Usuario("pepito","pepito_canales@dojo.com")
cuenta3 = Usuario("federica","federica_ludovico@dojo.com")

cuenta1.hacerDeposito(200).hacerDeposito(1000).hacerDeposito(2000).hacerDeposito(2000).hacerRetiro(39).mostrarBalanceUsuario()
cuenta2.hacerDeposito(5000).hacerDeposito(1000).hacerRetiro(1000).hacerRetiro(1500).mostrarBalanceUsuario()
cuenta3.hacerDeposito(1000).hacerRetiro(200).hacerRetiro(200).hacerRetiro(200).mostrarBalanceUsuario()
cuenta1.transferirDinero(100,cuenta3)